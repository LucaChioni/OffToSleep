#!/bin/bash

#/usr/bin/python FileProgetto/setup.py build
/Users/lucachioni/Desktop/venv2conda/bin/python FileProgetto/setup.py build
sudo cp -r FileProgetto/Risorse/ build/exe.macosx-10.7-x86_64-2.7/Risorse/
sudo cp -r FileProgetto/DatiSalvati/ build/exe.macosx-10.7-x86_64-2.7/DatiSalvati/
sudo chmod 777 build/exe.macosx-10.7-x86_64-2.7/DatiSalvati/Impostazioni/*
sudo chmod 777 build/exe.macosx-10.7-x86_64-2.7/DatiSalvati/Salvataggi/*

#touch build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo '#!/bin/bash' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo 'SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo 'cd "$SCRIPT_DIR"' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo 'export DYLD_FALLBACK_LIBRARY_PATH=./lib' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#echo './OffToSleep' >> build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
#sudo chmod 777 build/exe.macosx-10.7-x86_64-2.7/run_OffToSleep.sh
