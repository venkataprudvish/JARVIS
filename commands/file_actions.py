import os


def create_file(filename):
    try:
        with open(filename, "w") as f:
            pass
        return f"Created {filename}"
    except Exception as e:
        return str(e)


def create_folder(foldername):
    try:
        os.makedirs(foldername, exist_ok=True)
        return f"Created folder {foldername}"
    except Exception as e:
        return str(e)