import subprocess
import webbrowser
from datetime import date


def add_notes(text):
    week = date.today().isocalendar()[1]
    file = fr"E:\notes\week{week}.txt"
    with open(file, "a") as f:
        f.write(text + "\n")

    subprocess.Popen(["notepad.exe", file])


def open_websites(website):
    path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(path))
    webbrowser.get("chrome").open_new(f"https://{website}.com")


if __name__ == "__main__":
    add_notes("test")
    open_websites("facebook")
