#!/bin/bash

python2 setup.py build
sudo cp -r Immagini/ build/exe.linux-x86_64-2.7/
sudo cp -r Audio/ build/exe.linux-x86_64-2.7/
sudo cp -r Video/ build/exe.linux-x86_64-2.7/
sudo cp -r Salvataggi/ build/exe.linux-x86_64-2.7/
sudo cp -r Impostazioni/ build/exe.linux-x86_64-2.7/
sudo chmod 777 build/exe.linux-x86_64-2.7/Salvataggi/*
sudo chmod 777 build/exe.linux-x86_64-2.7/Impostazioni/*
