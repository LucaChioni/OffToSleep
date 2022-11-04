import sys
from cx_Freeze import setup, Executable

sistema_operativo = "Windows"

# Tells the build script to hide the console
base = None
if sys.platform == "win32":
    base = "Win32GUI"

lista_librerie_da_includere = ["os", "sys", "gc", "psutil", "datetime", "pygame", "random", "copy", "math", "hashlib"]
lista_shared_lib_da_includere = []
if sistema_operativo == "Windows":
    lista_librerie_da_includere.extend(["ctypes"])
elif sistema_operativo == "Linux":
    lista_librerie_da_includere.extend(["encodings", "subprocess"])
    lista_shared_lib_da_includere.extend(["libffi.so.8", "libffi.so.8.1.0"])
elif sistema_operativo == "Mac":
    lista_librerie_da_includere.extend(["re", "encodings", "subprocess"])
build_exe_options = {
    "packages": lista_librerie_da_includere,
    "bin_includes": lista_shared_lib_da_includere
}
setup(
    name="Off to Sleep",
    version="1.0",
    description="A game...",
    options={"build_exe": build_exe_options},
    executables=[Executable("FileProgetto/OffToSleep.py", base=base)]
)
