--- ENGLISH ---

IF YOU ARE DOWNLOADING FROM GITHUB: the game will not work because all audio and video resources are missing.

On Windows and Linux the game must be run with Python 2 and the following versions of the libraries: pygame==1.9.6, cx-freeze==5.1.1, psutil==5.8.0.
On MacOS the game must be run with Python 3 and the following versions of the libraries: pygame==2.1.2, cx-freeze==6.13.1, psutil==5.8.0.

To run the code correctly you need:
	1- set the operating system in "FileProgetto/GlobalHWVar.py", line 12 (choose between "Windows", "Linux" or "Mac");
	2- set the variable "usando_python3" to False if you are using Windows or Linux, OR to True if you are using MacOS (in "FileProgetto/GlobalHWVar.py", line 14).

To create the executable you need:
	1- set the operating system in "FileProgetto/setup.py", line 4 (choose between "Windows", "Linux" or "Mac");
	2- set to True the variable "eseguibile" in "FileProgetto/GlobalHWVar.py", line 13;
	3- run the file corresponding to your operating system:
		- On Windows => "Convertire_in_eseguibile_windows.bat";
		- On Linux => "Convertire_in_eseguibile_linux.sh";
		- On Mac => "Convertire_in_eseguibile_mac.sh";
	4- the executable will be located inside the folder "build".

==========================================================================================================================================================================
--- ITALIANO ---

SE STAI SCARICANDO DA GITHUB: il gioco non funzionerà perché mancano tutte le risorse audio e video.

Su Windows e Linux il gioco deve essere eseguito con Python 2 e le seguenti versioni delle librerie: pygame==1.9.6, cx-freeze==5.1.1, psutil==5.8.0.
Su MacOS il gioco deve essere eseguito con Python 3 e le seguenti versioni delle librerie: pygame==2.1.2, cx-freeze==6.13.1, psutil==5.8.0.

Per eseguire correttamente il codice è necessario:
	1- impostare il sistema operativo nel file "FileProgetto/GlobalHWVar.py" alla riga 12 (scegli tra "Windows", "Linux" o "Mac");
	2- impostare la variabile "usando_python3" a False se si sta usando Windows o Linux, OPPURE a True se si sta usando MacOS (in "FileProgetto/GlobalHWVar.py", riga 14).

Per creare l'eseguibile è necessario:
	1- impostare il sistema operativo nel file "FileProgetto/setup.py" alla riga 4 (scegli tra "Windows", "Linux" o "Mac");
	2- impostare a True la variabile "eseguibile" nel file "FileProgetto/GlobalHWVar.py" alla riga 13;
	3- eseguire il file corrispondente al sistema operativo in uso:
		- Su Windows => "Convertire_in_eseguibile_windows.bat";
		- Su Linux => "Convertire_in_eseguibile_linux.sh";
		- Su Mac => "Convertire_in_eseguibile_mac.sh";
	4- l'eseguibile si troverà dentro la cartella "build".
