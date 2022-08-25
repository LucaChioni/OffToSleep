#!/bin/bash

python2 FileProgetto/setup.py build
sudo cp -r FileProgetto/Risorse/ build/exe.linux-x86_64-2.7/
sudo cp -r FileProgetto/DatiSalvati/ build/exe.linux-x86_64-2.7/
sudo chmod 777 build/exe.linux-x86_64-2.7/DatiSalvati/Impostazioni/*
sudo chmod 777 build/exe.linux-x86_64-2.7/DatiSalvati/Salvataggi/*

touch build/exe.linux-x86_64-2.7/run_OffToSleep.sh
echo '#!/bin/bash' >> build/exe.linux-x86_64-2.7/run_OffToSleep.sh
echo 'SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )' >> build/exe.linux-x86_64-2.7/run_OffToSleep.sh
echo 'cd "$SCRIPT_DIR"' >> build/exe.linux-x86_64-2.7/run_OffToSleep.sh
echo 'export LD_LIBRARY_PATH=./lib' >> build/exe.linux-x86_64-2.7/run_OffToSleep.sh
echo './OffToSleep' >> build/exe.linux-x86_64-2.7/run_OffToSleep.sh
