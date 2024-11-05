from subprocess import run
from pathlib import Path

if __name__ == '__main__':
    currDir = Path(__file__).parent
    pysidercc = currDir.joinpath(".venv", "Scripts", "pyside6-uic.exe")
    uidir = currDir / "UI"
    for ui in uidir.glob("*.ui"):
        run([pysidercc, str(ui), "-o", str(ui.with_suffix(".py"))])
