# -*- coding: utf-8 -*-

import os
import sys
import gc
import pygame


sistemaOperativo = "Windows"
eseguibile = False

gamePath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/"
# modifico il path se sto creando l'eseguibile (su windows nascondo anche la console)
if eseguibile:
    if sistemaOperativo == "Windows":
        vetGamePath = gamePath.split("/")
        vetGamePath.pop(len(vetGamePath) - 1)
        vetGamePath.pop(len(vetGamePath) - 1)
        gamePath = ""
        for dir in vetGamePath:
            gamePath += dir + "/"
        import win32gui, win32con
        programToHide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(programToHide, win32con.SW_HIDE)
    if sistemaOperativo == "Linux":
        vetGamePath = gamePath.split("/")
        vetGamePath.pop(len(vetGamePath) - 1)
        vetGamePath.pop(len(vetGamePath) - 1)
        vetGamePath.pop(len(vetGamePath) - 1)
        gamePath = ""
        for dir in vetGamePath:
            gamePath += dir + "/"

# i suoni vengono velocizzati: metti 0,8 in velocità di audacity per risolvere
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.font.init()
pygame.display.init()

gsx = 0
gsy = 0
# adattamento schermo
if sistemaOperativo == "Windows":
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()
    gsx = ctypes.windll.user32.GetSystemMetrics(0)
    gsy = ctypes.windll.user32.GetSystemMetrics(1)
elif sistemaOperativo == "Linux":
    # libreria da importare per far funzionare l'eseguibile di linux
    import encodings
    import subprocess
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    gsx = int(resolution[0])
    gsy = int(resolution[1])

print ("Origine", gsx, gsy)
if gsx % 32 != 0 or gsy % 18 != 0:
    while gsx % 32 != 0:
        gsx = gsx - 1
    while gsy % 18 != 0:
        gsy = gsy - 1
if gsx // 16 < gsy // 9:
    print ("Altezza piu grande")
    gsy = gsx * 9 // 16
elif gsx // 16 > gsy // 9:
    print ("Larghezza piu grande")
    gsx = gsy * 16 // 9
print ("Modificato", gsx, gsy)

# metto il fullhd come risoluzione massima
if gsy > 1080:
    gsx = 1920
    gsy = 1080
maxGsx = gsx
maxGsy = gsy

# dimensione personaggio
gpx = gsx // 32
gpy = gsy // 18
schermoIntero = True

# nome-icona
titolo = "Still waiting"
pygame.display.set_caption(titolo)
icona = pygame.image.load(gamePath + "Immagini/Icone/Icona.png")
pygame.display.set_icon(icona)
fontUtilizzato = gamePath + "Font/LiberationSerif-Regular.ttf"
fontUtilizzatoItalic = gamePath + "Font/LiberationSerif-Italic.ttf"
fontUtilizzatoBold = gamePath + "Font/LiberationSerif-Bold.ttf"
listaTastiPremuti = []
primoAvvio = True

# clock
clockMainLoop = pygame.time.Clock()
clockInterazioni = pygame.time.Clock()
clockMenu = pygame.time.Clock()
clockAnimazioni = pygame.time.Clock()
clockVideo = pygame.time.Clock()
clockFadeToBlack = pygame.time.Clock()
fpsMainLoop = 60
fpsInterazioni = 30
fpsMenu = 30
fpsAnimazioni = 30
fpsVideo = 12
fpsFadeToBlack = 30

# colori
nero = (0, 0, 0)
grigioscuPiuScu = (40, 40, 40)
grigioscu = (50, 50, 50)
grigioscurino = (70, 70, 70)
grigio = (80, 80, 80)
grigiochi = (230, 230, 230)
bianco = (255, 255, 255)
rosso = (255, 130, 0)
verde = (130, 255, 0)
verdeScuro = (80, 90, 80)
verdeScuroPiuScuro = (70, 80, 70)
blu = (0, 0, 255)
bluScuro = (80, 80, 90)
bluScuroPiuScuro = (70, 70, 80)
rossoScuro = (100, 80, 80)
rossoScuroPiuScuro = (90, 70, 70)

# nascondo subito il cursore
pygame.mouse.set_visible(False)
mouseVisibile = False

def quit():
    sys.exit()

def loadFile(path, mode):
    if not os.path.exists(gamePath + path):
        creazione = open(gamePath + path, "w+")
        creazione.close()
    file = open(gamePath + path, mode)

    # per poter chiudere il gioco durante il caricamento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    global listaTastiPremuti
    listaTastiPremuti = []

    return file

# canali audio / volume (0-1)
volumeCanzoni = 0.5
volumeEffetti = 0.5
pygame.mixer.set_num_channels(11)
canaleSoundCanzone = pygame.mixer.Channel(0)
canaleSoundPuntatoreSposta = pygame.mixer.Channel(1)
canaleSoundPuntatoreSeleziona = pygame.mixer.Channel(2)
canaleSoundPassiRallo = pygame.mixer.Channel(3)
canaleSoundPassiColco = pygame.mixer.Channel(4)
canaleSoundPassiNemiciPersonaggi = pygame.mixer.Channel(5)
canaleSoundMorteNemici = pygame.mixer.Channel(6)
canaleSoundLvUp = pygame.mixer.Channel(7)
canaleSoundInterazioni = pygame.mixer.Channel(8)
canaleSoundAttacco = pygame.mixer.Channel(9)
canaleSoundSottofondoAmbientale = pygame.mixer.Channel(10)
def initVolumeSounds():
    canaleSoundCanzone.set_volume(volumeCanzoni)
    canaleSoundPuntatoreSeleziona.set_volume(volumeEffetti)
    canaleSoundPuntatoreSposta.set_volume(volumeEffetti)
    canaleSoundPassiRallo.set_volume(volumeEffetti)
    canaleSoundPassiColco.set_volume(volumeEffetti)
    canaleSoundPassiNemiciPersonaggi.set_volume(volumeEffetti)
    canaleSoundMorteNemici.set_volume(volumeEffetti)
    canaleSoundLvUp.set_volume(volumeEffetti)
    canaleSoundInterazioni.set_volume(volumeEffetti)
    canaleSoundAttacco.set_volume(volumeEffetti)
    canaleSoundSottofondoAmbientale.set_volume(volumeEffetti)

# freccetta (sized 24x24)
global mouseBloccato
def configuraCursore(bloccato):
    if not bloccato:
        strings = (
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "       XXX              ",
            "       XXXXX            ",
            "       XX..XXX          ",
            "       XX....XXX        ",
            "        XX.....XXX      ",
            "        XX.......XXX    ",
            "        XX........XX    ",
            "        XX......XXX     ",
            "         XX...XXX       ",
            "         XX..XX         ",
            "         XX.XX          ",
            "         XXXX           ",
            "          XX            "
        )
    else:
        strings = (
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "                        ",
            "       ...              ",
            "       .....            ",
            "       ..XX...          ",
            "       ..XXXX...        ",
            "        ..XXXXX...      ",
            "        ..XXXXXXX...    ",
            "        ..XXXXXXXX..    ",
            "        ..XXXXXX...     ",
            "         ..XXX...       ",
            "         ..XX..         ",
            "         ..X..          ",
            "         ....           ",
            "          ..            "
        )
    cursore, mask = pygame.cursors.compile(strings, black='X', white='.', xor='o')
    cursor_sizer = ((24, 24), (7, 11), cursore, mask)
    pygame.mouse.set_cursor(*cursor_sizer)
    global mouseBloccato
    mouseBloccato = bloccato
def setCursoreVisibile(visibile):
    global mouseVisibile
    mouseVisibile = visibile
    if visibile:
        pygame.mouse.set_visible(True)
        if sistemaOperativo == "Windows":
            pygame.mouse.set_pos(gsx // 2, gsy // 2)
    else:
        if sistemaOperativo == "Windows":
            pygame.mouse.set_pos(gsx // 2, gsy // 2)
        pygame.mouse.set_visible(False)
configuraCursore(True)
setCursoreVisibile(True)

# lettura configurazione controller: per ogni controller: nome, croce, cerchio, quadrato, triangolo, l1, r1, start, croceDirezionale
padUtilizzato = False
configPadInUso = []
listaPadConnessiConfigurati = []
listaPadConnessiSconosciuti = []
configPadConnessi = []
def inizializzaPad(pad):
    # faccio il vettore con la configurazione dei tasti del pad da usare
    global configPadInUso
    global configPadConnessi
    global padUtilizzato
    padUtilizzato = pad
    configPadInUso = []
    for configPad in configPadConnessi:
        if configPad[1] == padUtilizzato.get_name():
            configTastiPad = []
            configTastiPad.append(configPad[2])
            configTastiPad.append(configPad[3])
            configTastiPad.append(configPad[4])
            configTastiPad.append(configPad[5])
            configTastiPad.append(configPad[6])
            configTastiPad.append(configPad[7])
            configTastiPad.append(configPad[8])

            configPadInUso.append(configPad[0])
            configPadInUso.append(configPad[1])
            configPadInUso.append(configTastiPad)
            configPadInUso.append(configPad[9])
            break
def caricaImpostazioniController():
    impoControllerErrato = False
    leggi = loadFile("Impostazioni/ImpoController.txt", "r")
    leggifile = leggi.read()
    leggi.close()
    datiImpostazioniController = leggifile.split("\n")
    datiImpostazioniController.pop(len(datiImpostazioniController) - 1)
    if len(datiImpostazioniController) == 0:
        impoControllerErrato = True
        print ("File di configurazione dei controller vuoto")
    else:
        contaGlobale = 0
        while contaGlobale < len(datiImpostazioniController):
            setteggioController = datiImpostazioniController[contaGlobale].split("_")
            setteggioController.pop(len(setteggioController) - 1)
            if len(setteggioController) != 9:
                impoControllerErrato = True
                print ("File di configurazione dei controller corrotto 1")
                break
            else:
                for i in range(1, len(setteggioController)):
                    try:
                        test = int(setteggioController[i])
                        if type(test) is not int:
                            impoControllerErrato = True
                            print ("File di configurazione dei controller corrotto 2")
                            break
                    except ValueError:
                        impoControllerErrato = True
                        print ("File di configurazione dei controller corrotto 3")
                        break
            contaGlobale += 1
    if impoControllerErrato:
        # cancello il file se c'è un errore
        scrivi = loadFile("Impostazioni/ImpoController.txt", "w")
        scrivi.close()
    return impoControllerErrato, datiImpostazioniController
def inizializzaModuloJoistick():
    impoControllerErrato, datiImpostazioniController = caricaImpostazioniController()

    if pygame.joystick.get_init():
        pygame.joystick.quit()
    pygame.joystick.init()

    global listaPadConnessiConfigurati
    listaPadConnessiConfigurati = []
    global listaPadConnessiSconosciuti
    listaPadConnessiSconosciuti = []
    global configPadConnessi
    configPadConnessi = []

    joystick_count = pygame.joystick.get_count()
    for idPadGlobale in range(0, joystick_count):
        joystick = pygame.joystick.Joystick(idPadGlobale)
        nomeController = joystick.get_name()
        idController = joystick.get_id()
        configPad = []
        padGiaConfigurato = False
        if not impoControllerErrato:
            contaGlobale = 0
            while contaGlobale < len(datiImpostazioniController):
                setteggioController = datiImpostazioniController[contaGlobale].split("_")
                setteggioController.pop(len(setteggioController) - 1)
                if nomeController == setteggioController[0]:
                    padGiaConfigurato = True
                    listaPadConnessiConfigurati.append(joystick)
                    configPad.append(idController)
                    configPad.append(nomeController)
                    configPad.append(int(setteggioController[1]))
                    configPad.append(int(setteggioController[2]))
                    configPad.append(int(setteggioController[3]))
                    configPad.append(int(setteggioController[4]))
                    configPad.append(int(setteggioController[5]))
                    configPad.append(int(setteggioController[6]))
                    configPad.append(int(setteggioController[7]))
                    configPad.append(int(setteggioController[8]))
                    joystick.init()
                    break
                contaGlobale += 1
        if not padGiaConfigurato:
            listaPadConnessiSconosciuti.append(joystick)
            configPad.append(idController)
            configPad.append(nomeController)
            configPad.append(False)
            configPad.append(False)
            configPad.append(False)
            configPad.append(False)
            configPad.append(False)
            configPad.append(False)
            configPad.append(False)
            configPad.append(False)
        configPadConnessi.append(configPad)
inizializzaModuloJoistick()
usandoIlController = False

# funzioni per disegnare tutto sullo schermo (serve per ottimizzare)
listaRettangoliDaAggiornare = []
aggiornaTuttoLoSchermo = False
def disegnaColoreSuTuttoLoSchermo(colore):
    global schermo
    global gsx
    global gsy
    global listaRettangoliDaAggiornare
    global aggiornaTuttoLoSchermo
    schermo.fill(colore)

    if not aggiornaTuttoLoSchermo:
        listaRettangoliDaAggiornare = []
        listaRettangoliDaAggiornare.append(pygame.Rect(0, 0, gsx, gsy))
        aggiornaTuttoLoSchermo = True
def disegnaLineaSuSchermo(schermo, colore, coordinateInizio, coordinateFine, spessore):
    global listaRettangoliDaAggiornare
    global aggiornaTuttoLoSchermo
    x, y = coordinateInizio
    x = int(x)
    y = int(y)
    xFine, yFine = coordinateFine
    xFine = int(xFine)
    yFine = int(yFine)
    coordinateInizio = (x, y)
    coordinateFine = (xFine, yFine)
    spessore = int(spessore)
    pygame.draw.line(schermo, colore, coordinateInizio, coordinateFine, spessore)
    dimX = xFine - x
    dimY = yFine - y

    if dimX < spessore:
        dimX = spessore
    if dimY < spessore:
        dimY = spessore

    if not aggiornaTuttoLoSchermo:
        # non aggiungo il rettangolo se è già compreso in altri o tolgo quelli che sono contenuti nel rettangolo che sto aggiungendo
        aggiungiRettangolo = True
        rectOrig = pygame.Rect(x, y, dimX, dimY)
        xInizioRectOrig = rectOrig.left
        yInizioRectOrig = rectOrig.top
        xFineRectOrig = rectOrig.right
        yFineRectOrig = rectOrig.bottom
        i = 0
        while i < len(listaRettangoliDaAggiornare):
            rectConfronto = listaRettangoliDaAggiornare[i]
            xInizioRectConfronto = rectConfronto.left
            yInizioRectConfronto = rectConfronto.top
            xFineRectConfronto = rectConfronto.right
            yFineRectConfronto = rectConfronto.bottom
            rettangoloEliminato = False
            if xInizioRectOrig >= xInizioRectConfronto and xFineRectOrig <= xFineRectConfronto and yInizioRectOrig >= yInizioRectConfronto and yFineRectOrig <= yFineRectConfronto:
                aggiungiRettangolo = False
                break
            elif xInizioRectConfronto >= xInizioRectOrig and xFineRectConfronto <= xFineRectOrig and yInizioRectConfronto >= yInizioRectOrig and yFineRectConfronto <= yFineRectOrig:
                del listaRettangoliDaAggiornare[i]
                rettangoloEliminato = True
            if not rettangoloEliminato:
                i += 1
        if aggiungiRettangolo:
            listaRettangoliDaAggiornare.append(rectOrig)
def disegnaRettangoloSuSchermo(schermo, colore, coordinateEDimensione):
    global gsx
    global gsy
    global listaRettangoliDaAggiornare
    global aggiornaTuttoLoSchermo
    pygame.draw.rect(schermo, colore, coordinateEDimensione)
    x, y, dimX, dimY = coordinateEDimensione
    x = int(x)
    y = int(y)
    dimX = int(dimX)
    dimY = int(dimY)

    if x == 0 and y == 0 and dimX == gsx and dimY == gsy and not aggiornaTuttoLoSchermo:
        listaRettangoliDaAggiornare = []
        listaRettangoliDaAggiornare.append(pygame.Rect(0, 0, gsx, gsy))
        aggiornaTuttoLoSchermo = True
    if not aggiornaTuttoLoSchermo:
        # non aggiungo il rettangolo se è già compreso in altri o tolgo quelli che sono contenuti nel rettangolo che sto aggiungendo
        aggiungiRettangolo = True
        rectOrig = pygame.Rect(x, y, dimX, dimY)
        xInizioRectOrig = rectOrig.left
        yInizioRectOrig = rectOrig.top
        xFineRectOrig = rectOrig.right
        yFineRectOrig = rectOrig.bottom
        i = 0
        while i < len(listaRettangoliDaAggiornare):
            rectConfronto = listaRettangoliDaAggiornare[i]
            xInizioRectConfronto = rectConfronto.left
            yInizioRectConfronto = rectConfronto.top
            xFineRectConfronto = rectConfronto.right
            yFineRectConfronto = rectConfronto.bottom
            rettangoloEliminato = False
            if xInizioRectOrig >= xInizioRectConfronto and xFineRectOrig <= xFineRectConfronto and yInizioRectOrig >= yInizioRectConfronto and yFineRectOrig <= yFineRectConfronto:
                aggiungiRettangolo = False
                break
            elif xInizioRectConfronto >= xInizioRectOrig and xFineRectConfronto <= xFineRectOrig and yInizioRectConfronto >= yInizioRectOrig and yFineRectConfronto <= yFineRectOrig:
                del listaRettangoliDaAggiornare[i]
                rettangoloEliminato = True
            if not rettangoloEliminato:
                i += 1
        if aggiungiRettangolo:
            listaRettangoliDaAggiornare.append(rectOrig)
def disegnaImmagineSuSchermo(img, coordinate):
    global schermo
    global gsx
    global gsy
    global listaRettangoliDaAggiornare
    global aggiornaTuttoLoSchermo
    x, y = coordinate
    x = int(x)
    y = int(y)
    schermo.blit(img, (x, y))
    dimX, dimY = img.get_rect().size

    if x == 0 and y == 0 and dimX == gsx and dimY == gsy and not aggiornaTuttoLoSchermo:
        listaRettangoliDaAggiornare = []
        listaRettangoliDaAggiornare.append(pygame.Rect(0, 0, gsx, gsy))
        aggiornaTuttoLoSchermo = True
    if not aggiornaTuttoLoSchermo:
        # non aggiungo il rettangolo se è già compreso in altri o tolgo quelli che sono contenuti nel rettangolo che sto aggiungendo
        aggiungiRettangolo = True
        rectOrig = pygame.Rect(x, y, dimX, dimY)
        xInizioRectOrig = rectOrig.left
        yInizioRectOrig = rectOrig.top
        xFineRectOrig = rectOrig.right
        yFineRectOrig = rectOrig.bottom
        i = 0
        while i < len(listaRettangoliDaAggiornare):
            rectConfronto = listaRettangoliDaAggiornare[i]
            xInizioRectConfronto = rectConfronto.left
            yInizioRectConfronto = rectConfronto.top
            xFineRectConfronto = rectConfronto.right
            yFineRectConfronto = rectConfronto.bottom
            rettangoloEliminato = False
            if xInizioRectOrig >= xInizioRectConfronto and xFineRectOrig <= xFineRectConfronto and yInizioRectOrig >= yInizioRectConfronto and yFineRectOrig <= yFineRectConfronto:
                aggiungiRettangolo = False
                break
            elif xInizioRectConfronto >= xInizioRectOrig and xFineRectConfronto <= xFineRectOrig and yInizioRectConfronto >= yInizioRectOrig and yFineRectConfronto <= yFineRectOrig:
                del listaRettangoliDaAggiornare[i]
                rettangoloEliminato = True
            if not rettangoloEliminato:
                i += 1
        if aggiungiRettangolo:
            listaRettangoliDaAggiornare.append(rectOrig)
def aggiornaSchermo():
    global listaRettangoliDaAggiornare
    global aggiornaTuttoLoSchermo
    pygame.display.update(listaRettangoliDaAggiornare)
    listaRettangoliDaAggiornare = []
    aggiornaTuttoLoSchermo = False
    gc.collect()

# lettura configurazione (ordine => lingua, volEffetti, volCanzoni, schermoIntero, gsx, gsy)
linguaImpostata = "inglese"
leggi = loadFile("Impostazioni/Impostazioni.txt", "r")
leggifile = leggi.read()
leggi.close()
datiFileImpostazioniString = leggifile.split("_")
datiFileImpostazioniString.pop(len(datiFileImpostazioniString) - 1)
erroreFileImpostazioni = False
if len(datiFileImpostazioniString) == 6:
    datiFileImpostazioni = []
    for i in range(0, len(datiFileImpostazioniString)):
        try:
            datiFileImpostazioni.append(int(datiFileImpostazioniString[i]))
        except ValueError:
            erroreFileImpostazioni = True
    if not erroreFileImpostazioni:
        if datiFileImpostazioni[0] == 0:
            linguaImpostata = "italiano"
        elif datiFileImpostazioni[0] == 1:
            linguaImpostata = "inglese"
        if 0 <= int(datiFileImpostazioni[1]) <= 10:
            volumeEffetti = int(datiFileImpostazioni[1]) / 10.0
        if 0 <= int(datiFileImpostazioni[2]) <= 10:
            volumeCanzoni = int(datiFileImpostazioni[2]) / 10.0
        if schermoIntero == 0 or schermoIntero == 1:
            schermoIntero = int(datiFileImpostazioni[3])
        if maxGsx >= datiFileImpostazioni[4] and maxGsy >= datiFileImpostazioni[5] and ((maxGsx == datiFileImpostazioni[4] and maxGsy == datiFileImpostazioni[5]) or (datiFileImpostazioni[4] == 800 and datiFileImpostazioni[5] == 450) or (datiFileImpostazioni[4] == 1024 and datiFileImpostazioni[5] == 576) or (datiFileImpostazioni[4] == 1280 and datiFileImpostazioni[5] == 720) or (datiFileImpostazioni[4] == 1920 and datiFileImpostazioni[5] == 1080)):
            gsx = int(datiFileImpostazioni[4])
            gsy = int(datiFileImpostazioni[5])
            gpx = gsx // 32
            gpy = gsy // 18
        if schermoIntero:
            opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
            schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
        else:
            opzioni_schermo = pygame.DOUBLEBUF
            schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
        initVolumeSounds()
else:
    erroreFileImpostazioni = True
if erroreFileImpostazioni:
    print ("Errore nella lettura del file di configurazione delle impostazioni")
    opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
    schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
    initVolumeSounds()
