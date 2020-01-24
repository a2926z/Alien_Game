from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\Chris\Anaconda3\envs\Alien_Game\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Chris\Anaconda3\envs\Alien_Game\tcl\tk8.6"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("alien_invasion.py", base=base)]

includefiles = ['sounds/background_music.wav', 'sounds/game_start.wav', 'sounds/bullet_sound.wav',
                'sounds/fleet_excting.wav', 'sounds/game_end.wav', 'sounds/game_end.wav', 'images/adonis3.png',
                'images/tsipras4.png']
packages = ["os", "idna", "sys", "time", "pygame", "settings", "game_stats", "scoreboard", "button", "ship", "bullet", "alien", "tkinter"]
options = {
    'build_exe': {
        'packages': packages, 'include_files': includefiles
    },
}

setup(
    name = "alien_invasion",
    options = options,
    version = "1.1",
    description = 'alien game',
    executables = executables
)