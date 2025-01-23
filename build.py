import PyInstaller.__main__

def build():
    PyInstaller.__main__.run([
        '--onefile',
        '--name=hello',
        'hello.py',
    ])


if __name__ == "__main__":
    build()
