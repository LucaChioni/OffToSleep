:: usa "C:\Python27-64\python.exe" per l'eseguibile 64 bit // usa "C:\Python27-32\python.exe" per l'eseguibile 32 bit

SET /A osVersion = 64

if %osVersion%==32 (
    C:\Python27-32\python.exe FileProgetto\setup.py build
    xcopy /s ".\FileProgetto\Risorse" ".\build\exe.win32-2.7\Risorse\"
    xcopy /s ".\FileProgetto\DatiSalvati" ".\build\exe.win32-2.7\DatiSalvati\"
    move ".\build\exe.win32-2.7\Risorse\Immagini\Icone\icona.ico" ".\build\exe.win32-2.7\icona.ico"
)

if %osVersion%==64 (
    C:\Python27-64\python.exe FileProgetto\setup.py build
    xcopy /s ".\FileProgetto\Risorse" ".\build\exe.win-amd64-2.7\Risorse\"
    xcopy /s ".\FileProgetto\DatiSalvati" ".\build\exe.win-amd64-2.7\DatiSalvati\"
    move ".\build\exe.win-amd64-2.7\Risorse\Immagini\Icone\icona.ico" ".\build\exe.win-amd64-2.7\icona.ico"
)
