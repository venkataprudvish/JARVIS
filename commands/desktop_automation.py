import pyautogui
import keyboard
import pyperclip
import time


# -------------------------
# MOUSE
# -------------------------

def click_mouse():
    pyautogui.click()
    return True


def double_click():
    pyautogui.doubleClick()
    return True


def right_click():
    pyautogui.rightClick()
    return True


def move_mouse(x, y, duration=0.3):
    pyautogui.moveTo(x, y, duration=duration)
    return True


def scroll_screen(amount):
    pyautogui.scroll(amount)
    return True


# -------------------------
# KEYBOARD
# -------------------------

def type_text(text):
    pyautogui.write(text, interval=0.02)
    return True


def press_key(key):
    pyautogui.press(key)
    return True


def hotkey(*keys):
    pyautogui.hotkey(*keys)
    return True


def press_enter():
    pyautogui.press("enter")
    return True


# -------------------------
# SHORTCUTS
# -------------------------

def copy():
    pyautogui.hotkey("ctrl", "c")
    return True


def paste():
    pyautogui.hotkey("ctrl", "v")
    return True


def cut():
    pyautogui.hotkey("ctrl", "x")
    return True


def undo():
    pyautogui.hotkey("ctrl", "z")
    return True


def redo():
    pyautogui.hotkey("ctrl", "y")
    return True


def select_all():
    pyautogui.hotkey("ctrl", "a")
    return True


# -------------------------
# WINDOWS
# -------------------------

def show_desktop():
    pyautogui.hotkey("win", "d")
    return True


def open_run():
    pyautogui.hotkey("win", "r")
    return True


def open_task_manager():
    pyautogui.hotkey("ctrl", "shift", "esc")
    return True


# -------------------------
# CLIPBOARD
# -------------------------

def get_clipboard():
    return pyperclip.paste()


def set_clipboard(text):
    pyperclip.copy(text)
    return True


# -------------------------
# DELAY
# -------------------------

def wait(seconds):
    time.sleep(seconds)
    return True