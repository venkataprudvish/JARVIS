import winreg


def scan_registry():

    apps = {}

    registry_paths = [

        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"
        ),

        (
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"
        )
    ]

    for hive, path in registry_paths:

        try:

            key = winreg.OpenKey(hive, path)

            i = 0

            while True:

                try:

                    subkey_name = winreg.EnumKey(key, i)

                    subkey = winreg.OpenKey(key, subkey_name)

                    exe_path, _ = winreg.QueryValueEx(subkey, "")

                    app_name = subkey_name.replace(".exe", "").lower()

                    apps[app_name] = exe_path

                    i += 1

                except OSError:
                    break

        except FileNotFoundError:
            continue

    return apps