python setup.py build
xcopy /s ".\Immagini" ".\build\exe.win-amd64-2.7\Immagini\"
xcopy /s ".\Salvataggi" ".\build\exe.win-amd64-2.7\Salvataggi\"
xcopy /s ".\Video" ".\build\exe.win-amd64-2.7\Video\"
xcopy /s ".\Audio" ".\build\exe.win-amd64-2.7\Audio\"
xcopy /s ".\Impostazioni" ".\build\exe.win-amd64-2.7\Impostazioni\"
move ".\build\exe.win-amd64-2.7\Immagini\Icone\icona.ico" ".\build\exe.win-amd64-2.7\icona.ico"