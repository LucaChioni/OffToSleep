from cx_Freeze import setup, Executable
setup(
    name="Gioco",
    version="1.0",
    description="un gran gioco",
    executables=[Executable("FileProgetto/StillWaiting.py")]
)
