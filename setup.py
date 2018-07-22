from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "console"
executables = [Executable("main.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "MantisBTClientx86",
    version = "0.1",
    description = 'MantisBT client python program build on windows x86 platform',
    options = options,
    executables = executables
)
