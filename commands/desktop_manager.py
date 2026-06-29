import os
import time
import psutil
import subprocess
import pyautogui
import win32gui
import win32con
import win32process
from datetime import datetime


def get_active_window():

    hwnd = win32gui.GetForegroundWindow()

    if not hwnd:
        return None

    title = win32gui.GetWindowText(hwnd)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    try:

        process = psutil.Process(pid)

        return {
            "hwnd": hwnd,
            "title": title,
            "pid": pid,
            "process": process.name()
        }

    except Exception:
        return None


def get_running_processes():

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "exe"]
    ):

        try:

            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "exe": process.info["exe"]
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return processes


def find_process(target):

    target = target.lower().strip()

    processes = get_running_processes()

    # Exact match
    for process in processes:

        name = (process["name"] or "").lower()

        if target == name.replace(".exe", ""):
            return process

    # Partial match
    for process in processes:

        name = (process["name"] or "").lower()

        if target in name:
            return process

    # Executable path match
    for process in processes:

        exe = (process["exe"] or "").lower()

        if target in exe:
            return process

    return None


def close_process(pid):

    try:

        process = psutil.Process(pid)

        exe_name = process.name()

        result = subprocess.run(
            ["taskkill", "/F", "/IM", exe_name],
            capture_output=True,
            text=True
        )

        return result.returncode == 0

    except (
        psutil.NoSuchProcess,
        psutil.AccessDenied,
        psutil.ZombieProcess
    ):
        return False


def close_active_window():

    active = get_active_window()

    if not active:
        return False

    return close_process(active["pid"])


def minimize_active_window():

    active = get_active_window()

    if not active:
        return False

    win32gui.ShowWindow(active["hwnd"], win32con.SW_MINIMIZE)

    return True


def maximize_active_window():

    active = get_active_window()

    if not active:
        return False

    win32gui.ShowWindow(active["hwnd"], win32con.SW_MAXIMIZE)

    return True


import time


def switch_to_window(target):

    target = target.lower().strip()

    windows = []

    def enum_windows(hwnd, _):

        if not win32gui.IsWindowVisible(hwnd):
            return

        title = win32gui.GetWindowText(hwnd).lower()

        if target in title:
            windows.append(hwnd)

    win32gui.EnumWindows(enum_windows, None)

    if not windows:
        return False

    hwnd = windows[0]

    try:

        # Restore if minimized
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        time.sleep(0.2)

        # Bring window to front
        win32gui.BringWindowToTop(hwnd)

        time.sleep(0.2)

        # Set focus
        win32gui.SetActiveWindow(hwnd)

        time.sleep(0.2)

        # Try foreground
        win32gui.SetForegroundWindow(hwnd)

        return True

    except Exception as e:

        print("Switch Window Error:", e)

        return False


def take_screenshot():

    os.makedirs("Screenshots", exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")

    path = os.path.join("Screenshots", filename)

    screenshot = pyautogui.screenshot()

    screenshot.save(path)

    return path


def lock_pc():

    os.system("rundll32.exe user32.dll,LockWorkStation")

    return True