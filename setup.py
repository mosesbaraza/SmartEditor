import cx_Freeze
from cx_Freeze import setup, Executable

setup(
    name="Smart Editor 2017",
    version="1.0.0005",
    executables = [Executable('main.py', base='Win32GUI', icon="ico\\smart.ico")]
    )
