import subprocess


def scan_store_apps():

    apps = {}

    try:

        command = (
            "powershell "
            "Get-StartApps | "
            "Select-Object Name,AppID | "
            "ConvertTo-Json"
        )

        result = subprocess.check_output(
            command,
            shell=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        import json

        data = json.loads(result)

        if isinstance(data, dict):
            data = [data]

        for app in data:

            name = app.get("Name", "").lower().strip()

            appid = app.get("AppID", "").strip()

            if name and appid:
                apps[name] = appid

    except Exception:
        pass

    return apps