from PyInstaller.__main__ import run
import os

if __name__ == "__main__":
    os.system("rm -rf build dist SaveFileControl.spec")
    
    run([
        'main.py',
        '--noconsole',
        '--onefile',
        '--name', 'SaveFileControl'
    ])
    
    os.system("rm -rf build SaveFileControl.spec")
