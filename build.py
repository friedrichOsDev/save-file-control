from PyInstaller.__main__ import run
import os

if __name__ == "__main__":
    # delete previous build files (windows, mac and linux support)
    if os.path.exists("dist"):
        os.system("rmdir /s /q dist" if os.name == "nt" else "rm -rf dist")
    if os.path.exists("build"):
        os.system("rmdir /s /q build" if os.name == "nt" else "rm -rf build")
    if os.path.exists("SaveFileControl.spec"):
        os.remove("SaveFileControl.spec")

    run([
        "main.py",
        "--noconsole",
        "--onefile",
        "--name", "SaveFileControl"
    ])
    
    # clean up build files
    if os.path.exists("build"):
        os.system("rmdir /s /q build" if os.name == "nt" else "rm -rf build")
    if os.path.exists("SaveFileControl.spec"):  
        os.remove("SaveFileControl.spec")
