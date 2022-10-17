#!/bin/bash

#/usr/bin/python FileProgetto/setup.py build
#/Users/lucachioni/Desktop/venv2conda/bin/python FileProgetto/setup.py build
/Users/lucachioni/Desktop/venv3/bin/python FileProgetto/setup.py build
sudo cp -r FileProgetto/Risorse/ build/exe.macosx-10.14.6-x86_64-3.8/Risorse/
sudo cp -r FileProgetto/DatiSalvati/ build/exe.macosx-10.14.6-x86_64-3.8/DatiSalvati/
sudo chmod 777 build/exe.macosx-10.14.6-x86_64-3.8/DatiSalvati/Impostazioni/*
sudo chmod 777 build/exe.macosx-10.14.6-x86_64-3.8/DatiSalvati/Salvataggi/*

# metto libreria SDL aggiornata per evitare il bug dello schermo vuoto
#sudo cp /usr/local/opt/sdl2/lib/libSDL2-2.0.0.dylib /Users/lucachioni/Desktop/OffToSleep/build/exe.macosx-10.7-x86_64-2.7/lib/pygame/.dylibs/
#sudo rm /Users/lucachioni/Desktop/OffToSleep/build/exe.macosx-10.7-x86_64-2.7/lib/pygame/.dylibs/libSDL-1.2.0.dylib

#touch build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo '#!/bin/bash' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo 'SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo 'cd "$SCRIPT_DIR"' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo 'export DYLD_FALLBACK_LIBRARY_PATH=./lib' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo './OffToSleep' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#sudo chmod 755 build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
