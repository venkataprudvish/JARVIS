import webbrowser

WEBSITES = {
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "spotify": "https://open.spotify.com",
    "whatsapp": "https://web.whatsapp.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "x": "https://x.com",
    "twitter": "https://x.com"
}


def open_website(name):

    name = name.lower().strip()

    if name in WEBSITES:
        webbrowser.open(WEBSITES[name])
        return f"Opening {name.title()} in your browser, Sir."

    # IMPORTANT
    return None