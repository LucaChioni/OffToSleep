#!/bin/bash

python2 FileProgetto/setup.py build
sudo cp -r FileProgetto/Risorse/ build/exe.linux-x86_64-2.7/
sudo cp -r FileProgetto/DatiSalvati/ build/exe.linux-x86_64-2.7/
sudo chmod 777 build/exe.linux-x86_64-2.7/DatiSalvati/Impostazioni/*
sudo chmod 777 build/exe.linux-x86_64-2.7/DatiSalvati/Salvataggi/*
