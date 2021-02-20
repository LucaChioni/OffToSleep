python FileProgetto\setup.py build
xcopy /s ".\FileProgetto\Risorse" ".\build\exe.win-amd64-2.7\Risorse\"
xcopy /s ".\FileProgetto\DatiSalvati" ".\build\exe.win-amd64-2.7\DatiSalvati\"
move ".\build\exe.win-amd64-2.7\Risorse\Immagini\Icone\icona.ico" ".\build\exe.win-amd64-2.7\icona.ico"