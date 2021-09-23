import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["tkinter", "random", "sys"],
                     "excludes": ['pygame'],
                     "include_files": ['favicon.ico','bg-img.png']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="gluong scraper-gui",
      version="1.0",
      description="scrape images and tables from wikipedia",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="maingui.py", base=base)])
