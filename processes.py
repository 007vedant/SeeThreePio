import subprocess
from datetime import date


def add_notes(text):
    week = date.today().isocalendar()[1]
    file = fr"E:\notes\week{week}.txt"
    with open(file, "a") as f:
        f.write(text + "\n")

    subprocess.Popen(["notepad.exe", file])


if __name__ == "__main__":
    add_notes("test")
