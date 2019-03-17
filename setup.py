import cx_Freeze
executables=[cx_Freeze.Executable("Gioco2.py")]
cx_Freeze.setup(
    name="Gioco",
    options={"buid_exe":{"packages":["pygame","ctypes"]}},
    description="un gran gioco",
    executables=executables
    )
