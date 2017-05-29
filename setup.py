import sys
from cx_Freeze import setup, Executable

setup(  name = "QWebview-plus",
        version = "1.0",
        description = "QWebview supports Kiwoom Open API+ for JavaScript",
        author = "sculove",
        executables = [Executable("qwebviewplus.py", base="Win32GUI")])