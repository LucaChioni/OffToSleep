# -*- coding: utf-8 -*-

import os
import sys
import gc
import pygame
from SetAvanzamentiStanzePorteCofanetti import *


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
icona = pygame.image.load("Immagini/Icona.png")
pygame.display.set_icon(icona)
listaTastiPremuti = []

# clock
clockAttacco = pygame.time.Clock()
clockAnimazioni = pygame.time.Clock()
clockVideo = pygame.time.Clock()
clockMenu = pygame.time.Clock()
clockFadeToBlack = pygame.time.Clock()
fpsAnimazioni = 30
fpsInquadra = 20
fpsVideo = 12
fpsMenu = 30
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

# vettore che conterrà tutti i dati dei salvataggi
vetDatiSalvataggi = []
# vettore che conterrà i dati di salvataggio del file gameover
vetDatiSalvataggioGameOver = []
numSalvataggioCaricato = 0

# nascondo subito il cursore
pygame.mouse.set_visible(False)
mouseVisibile = False

def quit():
    sys.exit()

def loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True):
    img = pygame.image.load(gamePath + path)
    if aumentaRisoluzione:
        sizeX, sizeY = img.get_rect().size
        moltiplicatore = 1
        while sizeX * moltiplicatore < xScale and sizeY * moltiplicatore < yScale:
            moltiplicatore += 1
        img = pygame.transform.scale(img, (sizeX * moltiplicatore, sizeY * moltiplicatore))
    if xScale != 0 and yScale != 0:
        img = pygame.transform.smoothscale(img, (int(xScale), int(yScale)))
    if canale_alpha:
        img = img.convert_alpha()
    else:
        img = img.convert()
    pygame.event.pump()
    return img

def loadSound(path):
    try:
        sound = pygame.mixer.Sound(gamePath + path)
    except Exception:
        print ("Impossibile caricare " + path)
        sound = pygame.mixer.Sound(gamePath + "Audio/RumoriAmbiente/Acquisto.wav")
    return sound

def loadFile(path, mode):
    file = open(gamePath + path, mode)
    return file

# dichiaro le variabili globali della funzione loadImgs
global puntatore
global puntatorevecchio
global puntatIn
global puntatOut
global puntatSfo
global puntatDif
global puntatAtt
global puntatArc
global puntatPor
global puntatCof
global puntatAnalisi
global puntatBom
global puntatBoV
global puntatEsc
global puntatBoA
global puntatBoP
global scorriSu
global scorriGiu
global puntatDialoghi
global puntatoreInquadraNemici
global persw
global perswb
global persa
global persab
global perss
global perssb
global persd
global persdb
global perssm
global perssmb1
global perssmb2
global persdm
global persdmb1
global persdmb2
global persam
global persamb1
global persamb2
global perswm
global perswmb1
global perswmb2
global perswmbAttacco
global persambAttacco
global perssmbAttacco
global persdmbAttacco
global persmbDifesa
global persAvvele
global robow
global roboa
global robos
global robod
global robomo
global robodp
global roboap
global armrobmo
global roboSurrisc
global mercanteMenu
global scorriSuGiu
global scorriSuGiuBloccato
global scorriSuGiuBloccatoGiu
global scorriSuGiuBloccatoSu
global sfondoDialogoMercante
global faretra1Menu
global faretra2Menu
global faretra3Menu
global frecciaMenu
global sfondoRallo
global sfondoColco
global sfondoMostro
global sfondoEsche
global sfondoStartBattaglia
global sfondoTriangolinoAltoDestra
global sfondoTriangolinoAltoSinistra
global sfondoTriangolinoBassoDestra
global sfondoTriangolinoBassoSinistra
global appiccicoso
global avvelenato
global surriscaldato
global attaccopiu
global difesapiu
global velocitapiu
global efficienzapiu
global imgNumFrecce
global sfochiaveocchio
global occhioape
global occhiochiu
global chiaveroboacc
global chiaverobospe
global esche
global sacchettoDenaroStart
global sacchettoDenaroMercante
global faretraFrecceStart0
global faretraFrecceStart1
global faretraFrecceStart2
global faretraFrecceStart3
global sacchettoDenaro
global imgFrecciaLanciata
global cofaniaper
global cofanichiu
global sfocontcof
global s1
global s2
global s3
global campoattaccabileRallo1
global campoattaccabileRallo2
global campoattaccabileRallo3
global campoattaccabileRallo4
global campoattaccabileRallo5
global campoattaccabileRobo
global caselleattaccabiliRobo
global caselleattaccabilimostro
global caselleattaccabili
global saliliv
global saliliv1
global saliliv2
global vetImgSpadeMenu
global vetImgArchiMenu
global vetImgArmatureMenu
global vetImgScudiMenu
global vetImgGuantiMenu
global vetImgCollaneMenu
global imgGambitSconosciuta
global vetImgCondizioniMenu
global vetImgTecnicheMenu
global vetImgBatterieMenu
global vetIcoBatterieMenu
global vetImgOggettiMenu
global vetImgOggettiMercante
global vetImgOggettiStart
global vetIcoOggettiMenu
global vetImgSpadePixellate
global vetImgArchiPixellate
global vetImgArmaturePixellate
global vetImgScudiPixellate
global vetImgGuantiPixellate
global vetImgCollanePixellate
global imgAnimaBomba
global imgAnimaBombaVeleno
global imgAnimaBombaAppiccicosa
global imgAnimaBombaPotenziata
global imgAnimaPozione1
global imgAnimaPozione2
global imgAnimaMedicina1
global imgAnimaMedicina2
global imgAnimaCaricabatterie
global imgDanneggiamentoColco
global vetAnimazioniTecniche
global imgFrecciaEletttricaLanciata
global imgFrecciaEletttricaLanciataP
global imgFrecciaEletttricaLanciataPP
global sfondoDialoghi
global avvelenatoMenu
global surriscaldatoMenu
global attaccopiuMenu
global difesapiuMenu
global velocitapiuMenu
global efficienzapiuMenu
global roboo1
global roboo2
global perso
global persob
global puntatoreImpostazioniDestra
global puntatoreImpostazioniSinistra
global puntatoreImpostazioniDestraBloccato
global puntatoreImpostazioniSinistraBloccato
global tutorialTastieraInGioco
global tutorialTastieraInMenu
global tutorialMouse
global tutorialControllerInGioco
global tutorialControllerInMenu
global impostazioniController
global impostaControllerCroce
global impostaControllerCerchio
global impostaControllerQuadrato
global impostaControllerTriangolo
global impostaControllerL1
global impostaControllerR1
global impostaControllerStart
global impostaControllerCroceDirezionale
global persGrafMenu
global saraGrafMenu
global fraMaggioreGrafMenu
global robograf0
global robograf1
global robograf1b
global robograf2
global robograf2b
global robograf3
global robograf4
global imgDialogoFraMaggiore
global imgDialogoSara
global imgFraMaggioreMenuOggetti
global imgSaraMenuOggetti
global indvita
global fineindvita
global vitanemico00
global vitanemico0
global vitanemico1
global vitanemico2
global vitanemico3
global vitanemico4
global vitanemico5
global vitanemico6
global vitanemico7
global vitanemico8
global vitanemico9
global vitapersonaggio
global vitarobo
global sfondoOggettoMenu
global sconosciutoEquipMenu
global sconosciutoOggettoMenu1
global sconosciutoOggettoMenu2
global sconosciutoOggettoMenu3
global sconosciutoOggettoIcoMenu
global imgMappa1A
global imgMappa1B
global imgMappa2A
global imgMappa2B
global imgMappa3A
global imgMappa3B
global imgMappa4A
global imgMappa4B
global imgMappa5A
global imgMappa5B
global imgMappa6A
global imgMappa6B
global imgMappa7A
global imgMappa7B
global imgMappa8A
global imgMappa8B
global imgMappa9A
global imgMappa9B
global imgMappa10A
global imgMappa10B
global imgMappa11A
global imgMappa11B
global imgMappa12A
global imgMappa12B
global imgMappa13A
global imgMappa13B
global imgMappa14A
global imgMappa14B
global imgOmbreggiaturaContorniMappaMenu
global dictionaryImgNemici
global imgDanneggiamentoCausaRallo
global imgDanneggiamentoCausaColco

def loadImgs():
    global puntatore
    global puntatorevecchio
    global puntatIn
    global puntatOut
    global puntatSfo
    global puntatDif
    global puntatAtt
    global puntatArc
    global puntatPor
    global puntatCof
    global puntatAnalisi
    global puntatBom
    global puntatBoV
    global puntatEsc
    global puntatBoA
    global puntatBoP
    global scorriSu
    global scorriGiu
    global puntatDialoghi
    global puntatoreInquadraNemici
    global persw
    global perswb
    global persa
    global persab
    global perss
    global perssb
    global persd
    global persdb
    global perssm
    global perssmb1
    global perssmb2
    global persdm
    global persdmb1
    global persdmb2
    global persam
    global persamb1
    global persamb2
    global perswm
    global perswmb1
    global perswmb2
    global perswmbAttacco
    global persambAttacco
    global perssmbAttacco
    global persdmbAttacco
    global persmbDifesa
    global persAvvele
    global robow
    global roboa
    global robos
    global robod
    global robomo
    global robodp
    global roboap
    global armrobmo
    global roboSurrisc
    global mercanteMenu
    global scorriSuGiu
    global scorriSuGiuBloccato
    global scorriSuGiuBloccatoGiu
    global scorriSuGiuBloccatoSu
    global sfondoDialogoMercante
    global faretra1Menu
    global faretra2Menu
    global faretra3Menu
    global frecciaMenu
    global sfondoRallo
    global sfondoColco
    global sfondoMostro
    global sfondoEsche
    global sfondoStartBattaglia
    global sfondoTriangolinoAltoDestra
    global sfondoTriangolinoAltoSinistra
    global sfondoTriangolinoBassoDestra
    global sfondoTriangolinoBassoSinistra
    global appiccicoso
    global avvelenato
    global surriscaldato
    global attaccopiu
    global difesapiu
    global velocitapiu
    global efficienzapiu
    global imgNumFrecce
    global sfochiaveocchio
    global occhioape
    global occhiochiu
    global chiaveroboacc
    global chiaverobospe
    global esche
    global sacchettoDenaroStart
    global sacchettoDenaroMercante
    global faretraFrecceStart0
    global faretraFrecceStart1
    global faretraFrecceStart2
    global faretraFrecceStart3
    global sacchettoDenaro
    global imgFrecciaLanciata
    global cofaniaper
    global cofanichiu
    global sfocontcof
    global s1
    global s2
    global s3
    global campoattaccabileRallo1
    global campoattaccabileRallo2
    global campoattaccabileRallo3
    global campoattaccabileRallo4
    global campoattaccabileRallo5
    global campoattaccabileRobo
    global caselleattaccabiliRobo
    global caselleattaccabilimostro
    global caselleattaccabili
    global saliliv
    global saliliv1
    global saliliv2
    global vetImgSpadeMenu
    global vetImgArchiMenu
    global vetImgArmatureMenu
    global vetImgScudiMenu
    global vetImgGuantiMenu
    global vetImgCollaneMenu
    global vetImgCondizioniMenu
    global imgGambitSconosciuta
    global vetImgTecnicheMenu
    global vetImgBatterieMenu
    global vetIcoBatterieMenu
    global vetImgOggettiMenu
    global vetImgOggettiMercante
    global vetImgOggettiStart
    global vetIcoOggettiMenu
    global vetImgSpadePixellate
    global vetImgArchiPixellate
    global vetImgArmaturePixellate
    global vetImgScudiPixellate
    global vetImgGuantiPixellate
    global vetImgCollanePixellate
    global imgAnimaBomba
    global imgAnimaBombaVeleno
    global imgAnimaBombaAppiccicosa
    global imgAnimaBombaPotenziata
    global imgAnimaPozione1
    global imgAnimaPozione2
    global imgAnimaMedicina1
    global imgAnimaMedicina2
    global imgAnimaCaricabatterie
    global imgDanneggiamentoColco
    global vetAnimazioniTecniche
    global imgFrecciaEletttricaLanciata
    global imgFrecciaEletttricaLanciataP
    global imgFrecciaEletttricaLanciataPP
    global sfondoDialoghi
    global avvelenatoMenu
    global surriscaldatoMenu
    global attaccopiuMenu
    global difesapiuMenu
    global velocitapiuMenu
    global efficienzapiuMenu
    global roboo1
    global roboo2
    global perso
    global persob
    global puntatoreImpostazioniDestra
    global puntatoreImpostazioniSinistra
    global puntatoreImpostazioniDestraBloccato
    global puntatoreImpostazioniSinistraBloccato
    global tutorialTastieraInGioco
    global tutorialTastieraInMenu
    global tutorialMouse
    global tutorialControllerInGioco
    global tutorialControllerInMenu
    global impostazioniController
    global impostaControllerCroce
    global impostaControllerCerchio
    global impostaControllerQuadrato
    global impostaControllerTriangolo
    global impostaControllerL1
    global impostaControllerR1
    global impostaControllerStart
    global impostaControllerCroceDirezionale
    global persGrafMenu
    global saraGrafMenu
    global fraMaggioreGrafMenu
    global robograf0
    global robograf1
    global robograf1b
    global robograf2
    global robograf2b
    global robograf3
    global robograf4
    global imgDialogoFraMaggiore
    global imgDialogoSara
    global imgFraMaggioreMenuOggetti
    global imgSaraMenuOggetti
    global indvita
    global fineindvita
    global vitanemico00
    global vitanemico0
    global vitanemico1
    global vitanemico2
    global vitanemico3
    global vitanemico4
    global vitanemico5
    global vitanemico6
    global vitanemico7
    global vitanemico8
    global vitanemico9
    global vitapersonaggio
    global vitarobo
    global sfondoOggettoMenu
    global sconosciutoEquipMenu
    global sconosciutoOggettoMenu1
    global sconosciutoOggettoMenu2
    global sconosciutoOggettoMenu3
    global sconosciutoOggettoIcoMenu
    global imgMappa1A
    global imgMappa1B
    global imgMappa2A
    global imgMappa2B
    global imgMappa3A
    global imgMappa3B
    global imgMappa4A
    global imgMappa4B
    global imgMappa5A
    global imgMappa5B
    global imgMappa6A
    global imgMappa6B
    global imgMappa7A
    global imgMappa7B
    global imgMappa8A
    global imgMappa8B
    global imgMappa9A
    global imgMappa9B
    global imgMappa10A
    global imgMappa10B
    global imgMappa11A
    global imgMappa11B
    global imgMappa12A
    global imgMappa12B
    global imgMappa13A
    global imgMappa13B
    global imgMappa14A
    global imgMappa14B
    global imgOmbreggiaturaContorniMappaMenu
    global dictionaryImgNemici
    global imgDanneggiamentoCausaRallo
    global imgDanneggiamentoCausaColco

    # puntatore
    puntatore = loadImage("Immagini/Puntatori/Puntatore.png", gpx // 2, gpy // 2, True)
    puntatorevecchio = loadImage("Immagini/Puntatori/Puntatorevecchio.png", gpx // 2, gpy // 2, True)
    puntatIn = loadImage('Immagini/Puntatori/InquadraCVin.png', gpx, gpy, True)
    puntatOut = loadImage('Immagini/Puntatori/InquadraCVout.png', gpx, gpy, True)
    puntatSfo = loadImage('Immagini/Oggetti/sfondoOggettoLanciato.png', gpx, gpy, True)
    puntatDif = loadImage('Immagini/Oggetti/Difesa.png', gpx, gpy, True)
    puntatAtt = loadImage('Immagini/Oggetti/Attacco.png', gpx, gpy, True)
    puntatArc = loadImage('Immagini/Oggetti/AttaccoDistanza.png', gpx, gpy, True)
    puntatPor = loadImage('Immagini/Oggetti/ApriChiudiPorta.png', gpx, gpy, True)
    puntatCof = loadImage('Immagini/Oggetti/ApriCofanetto.png', gpx, gpy, True)
    puntatAnalisi = loadImage('Immagini/Oggetti/AnalizzaColco.png', gpx, gpy, True)
    puntatBom = loadImage('Immagini/Oggetti/Oggetto6Ico.png', gpx, gpy, True)
    puntatBoV = loadImage('Immagini/Oggetti/Oggetto7Ico.png', gpx, gpy, True)
    puntatEsc = loadImage('Immagini/Oggetti/Oggetto8Ico.png', gpx, gpy, True)
    puntatBoA = loadImage('Immagini/Oggetti/Oggetto9Ico.png', gpx, gpy, True)
    puntatBoP = loadImage('Immagini/Oggetti/Oggetto10Ico.png', gpx, gpy, True)
    scorriSu = loadImage("Immagini/Puntatori/ScorriOggettiSu.png", gpx, gpy, True)
    scorriGiu = loadImage("Immagini/Puntatori/ScorriOggettiGiu.png", gpx, gpy, True)
    puntatDialoghi = loadImage('Immagini/Oggetti/IcoDialogo.png', gpx, gpy, True)
    puntatoreInquadraNemici = loadImage("Immagini/Puntatori/InquadraNemicoSelezionato.png", gpx, gpy, True)
    puntatoreImpostazioniDestra = loadImage("Immagini/Puntatori/ScorriImpostazioniDestra.png", gpx, gpy, True)
    puntatoreImpostazioniSinistra = loadImage("Immagini/Puntatori/ScorriImpostazioniSinistra.png", gpx, gpy, True)
    puntatoreImpostazioniDestraBloccato = loadImage("Immagini/Puntatori/ScorriImpostazioniDestraBloccato.png", gpx, gpy, True)
    puntatoreImpostazioniSinistraBloccato = loadImage("Immagini/Puntatori/ScorriImpostazioniSinistraBloccato.png", gpx, gpy, True)

    # immagini personaggio
    persw = loadImage('Immagini/Personaggi/Sara/Personaggio4.png', gpx, gpy, True)
    perswb = loadImage('Immagini/Personaggi/Sara/Personaggio4b.png', gpx, gpy, True)
    persa = loadImage('Immagini/Personaggi/Sara/Personaggio3.png', gpx, gpy, True)
    persab = loadImage('Immagini/Personaggi/Sara/Personaggio3b.png', gpx, gpy, True)
    perso = loadImage('Immagini/Personaggi/Sara/Personaggio1.png', gpx * 5, gpy * 5, True)
    persob = loadImage('Immagini/Personaggi/Sara/Personaggio1b.png', gpx * 5, gpy * 5, True)
    perss = loadImage('Immagini/Personaggi/Sara/Personaggio1.png', gpx, gpy, True)
    perssb = loadImage('Immagini/Personaggi/Sara/Personaggio1b.png', gpx, gpy, True)
    persd = loadImage('Immagini/Personaggi/Sara/Personaggio2.png', gpx, gpy, True)
    persdb = loadImage('Immagini/Personaggi/Sara/Personaggio2b.png', gpx, gpy, True)
    perssm = loadImage('Immagini/Personaggi/Sara/Personaggio1mov.png', gpx, gpy, True)
    perssmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio1movb1.png', gpx, gpy, True)
    perssmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio1movb2.png', gpx, gpy, True)
    persdm = loadImage('Immagini/Personaggi/Sara/Personaggio2mov.png', gpx, gpy, True)
    persdmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio2movb1.png', gpx, gpy, True)
    persdmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio2movb2.png', gpx, gpy, True)
    persam = loadImage('Immagini/Personaggi/Sara/Personaggio3mov.png', gpx, gpy, True)
    persamb1 = loadImage('Immagini/Personaggi/Sara/Personaggio3movb1.png', gpx, gpy, True)
    persamb2 = loadImage('Immagini/Personaggi/Sara/Personaggio3movb2.png', gpx, gpy, True)
    perswm = loadImage('Immagini/Personaggi/Sara/Personaggio4mov.png', gpx, gpy, True)
    perswmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio4movb1.png', gpx, gpy, True)
    perswmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio4movb2.png', gpx, gpy, True)
    perswmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio4movbAttacco.png', gpx, gpy, True)
    persambAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio3movbAttacco.png', gpx, gpy, True)
    perssmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio1movbAttacco.png', gpx, gpy, True)
    persdmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio2movbAttacco.png', gpx, gpy, True)
    persmbDifesa = loadImage('Immagini/Personaggi/Sara/PersonaggiomovbDifesa.png', gpx, gpy, True)
    persAvvele = loadImage('Immagini/Personaggi/Sara/PersonaggioAvvelenato.png', gpx, gpy, True)

    # immagini robot
    robow = loadImage('Immagini/Personaggi/Colco/Robot4.png', gpx, gpy, True)
    roboa = loadImage('Immagini/Personaggi/Colco/Robot3.png', gpx, gpy, True)
    roboo1 = loadImage('Immagini/Personaggi/Colco/Robot1.png', gpx * 5, gpy * 5, True)
    roboo2 = loadImage('Immagini/Personaggi/Colco/Robot1.png', gpx * 3, gpy * 3, True)
    robos = loadImage('Immagini/Personaggi/Colco/Robot1.png', gpx, gpy, True)
    robod = loadImage('Immagini/Personaggi/Colco/Robot2.png', gpx, gpy, True)
    robomo = loadImage('Immagini/Personaggi/Colco/Robot0.png', gpx, gpy, True)
    robodp = loadImage('Immagini/Personaggi/Colco/Robot2p.png', gpx, gpy, True)
    roboap = loadImage('Immagini/Personaggi/Colco/Robot3p.png', gpx, gpy, True)
    armrobmo = loadImage('Immagini/EquipRobo/Batteria00.png', gpx, gpy, True)
    roboSurrisc = loadImage('Immagini/Personaggi/Colco/RobotSurriscaldato.png', gpx, gpy, True)

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = loadImage("Immagini/Nemici/DannoRallo.png", gpx, gpy, True)
    imgDanneggiamentoCausaColco = loadImage("Immagini/Nemici/DannoColco.png", gpx, gpy, True)

    # img menu mercante
    mercanteMenu = loadImage('Immagini/Personaggi/Mercante/MercanteDialogo.png', gpx * 12, gpy * 9, False)
    scorriSuGiu = loadImage('Immagini/Puntatori/ScorriSuGiu.png', gpx, gpy, True)
    scorriSuGiuBloccato = loadImage('Immagini/Puntatori/ScorriSuGiuBloccato.png', gpx, gpy, True)
    scorriSuGiuBloccatoGiu = loadImage('Immagini/Puntatori/ScorriSuGiuBloccatoGiu.png', gpx, gpy, True)
    scorriSuGiuBloccatoSu = loadImage('Immagini/Puntatori/ScorriSuGiuBloccatoSu.png', gpx, gpy, True)
    sfondoDialogoMercante = loadImage('Immagini/DecorazioniMenu/SfondoDialogoMercante.png', gpx * 9.5, gpy * 4.5, False)
    faretra1Menu = loadImage('Immagini/Oggetti/Faretra1Menu.png', gpx * 8, gpy * 8, False)
    faretra2Menu = loadImage('Immagini/Oggetti/Faretra2Menu.png', gpx * 8, gpy * 8, False)
    faretra3Menu = loadImage('Immagini/Oggetti/Faretra3Menu.png', gpx * 8, gpy * 8, False)
    frecciaMenu = loadImage('Immagini/Oggetti/FrecciaMenu.png', gpx * 8, gpy * 8, False)

    # sfondi
    sfondoRallo = loadImage('Immagini/Status/SfondoRallo.png', gpx * 6, gpy, False)
    sfondoColco = loadImage('Immagini/Status/SfondoColco.png', gpx * 4, gpy, False)
    sfondoMostro = loadImage('Immagini/Status/SfondoNemici.png', gpx * 3, gpy, False)
    sfondoEsche = loadImage('Immagini/Status/SfondoEsche.png', gpx, gpy, True)
    sfondoStartBattaglia = loadImage('Immagini/Oggetti/SfondoStartBattaglia.png', gpx * 7, gpy * 10, False)
    sfondoTriangolinoAltoDestra = loadImage('Immagini/DecorazioniMenu/TriangoloAltoDestra.png', gpx, gpy, True)
    sfondoTriangolinoAltoSinistra = loadImage('Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', gpx, gpy, True)
    sfondoTriangolinoBassoDestra = loadImage('Immagini/DecorazioniMenu/TriangoloBassoDestra.png', gpx, gpy, True)
    sfondoTriangolinoBassoSinistra = loadImage('Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', gpx, gpy, True)

    # status
    appiccicoso = loadImage('Immagini/Status/Appiccicoso.png', gpx * 3 // 4, gpy * 3 // 4, True)
    avvelenatoMenu = loadImage('Immagini/Status/Avvelenato.png', gpx, gpy, True)
    avvelenato = loadImage('Immagini/Status/Avvelenato.png', gpx * 3 // 4, gpy * 3 // 4, True)
    surriscaldatoMenu = loadImage('Immagini/Status/Surriscaldato.png', gpx, gpy, True)
    surriscaldato = loadImage('Immagini/Status/Surriscaldato.png', gpx * 3 // 4, gpy * 3 // 4, True)
    attaccopiuMenu = loadImage('Immagini/Status/Attaccopiu.png', gpx, gpy, True)
    attaccopiu = loadImage('Immagini/Status/Attaccopiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    difesapiuMenu = loadImage('Immagini/Status/Difesapiu.png', gpx, gpy, True)
    difesapiu = loadImage('Immagini/Status/Difesapiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    velocitapiuMenu = loadImage('Immagini/Status/Velocitapiu.png', gpx, gpy, True)
    velocitapiu = loadImage('Immagini/Status/Velocitapiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    efficienzapiuMenu = loadImage('Immagini/Status/Efficienzapiu.png', gpx, gpy, True)
    efficienzapiu = loadImage('Immagini/Status/Efficienzapiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    imgNumFrecce = loadImage('Immagini/Status/NumFrecce.png', gpx * 3 // 4, gpy * 3 // 4, True)

    # menu alto destra
    sfochiaveocchio = loadImage("Immagini/Oggetti/SfondoOcchioChiave.png", gpx * 5, gpy * 2, False)
    occhioape = loadImage('Immagini/Status/OcchioAperto.png', gpx, gpy, True)
    occhiochiu = loadImage('Immagini/Status/OcchioChiuso.png', gpx, gpy, True)
    chiaveroboacc = loadImage('Immagini/Oggetti/ChiaveColcoAcc.png', gpx * 2, gpy * 2, True)
    chiaverobospe = loadImage('Immagini/Oggetti/ChiaveColcoSpe.png', gpx * 2, gpy * 2, True)

    # oggetti sulla schermata
    esche = loadImage("Immagini/Oggetti/Oggetto8Ico.png", gpx, gpy, True)
    sacchettoDenaroStart = loadImage('Immagini/Oggetti/SacchettoDenaroSinistra.png', gpx * 4, gpy * 4, False)
    sacchettoDenaroMercante = loadImage('Immagini/Oggetti/SacchettoDenaroDestra.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart0 = loadImage('Immagini/EquipSara/Faretre/Faretra0Menu.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart1 = loadImage('Immagini/EquipSara/Faretre/Faretra1Menu.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart2 = loadImage('Immagini/EquipSara/Faretre/Faretra2Menu.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart3 = loadImage('Immagini/EquipSara/Faretre/Faretra3Menu.png', gpx * 4, gpy * 4, False)
    sacchettoDenaro = loadImage('Immagini/Oggetti/SacchettoDenaroIco.png', gpx, gpy, True)
    imgFrecciaLanciata = loadImage('Immagini/Oggetti/Freccia.png', gpx, gpy, True)

    # cofanetti
    cofaniaper = loadImage("Immagini/Oggetti/CofanettoAperto.png", gpx, gpy, True)
    cofanichiu = loadImage("Immagini/Oggetti/CofanettoChiuso.png", gpx, gpy, True)
    sfocontcof = loadImage("Immagini/Oggetti/SfondoContenutoCofanetto.png", gpx * 16, gpy * 3, False)

    # immagini salvataggi
    s1 = loadImage('Immagini/Salvataggi/S1.png', gpx * 3, gpy * 3, False)
    s2 = loadImage('Immagini/Salvataggi/S2.png', gpx * 3, gpy * 3, False)
    s3 = loadImage('Immagini/Salvataggi/S3.png', gpx * 3, gpy * 3, False)

    # caselle attaccabili
    campoattaccabileRallo1 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png', gpx * 13, gpy * 13, False)
    campoattaccabileRallo2 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png', gpx * 11, gpy * 11, False)
    campoattaccabileRallo3 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png', gpx * 13, gpy * 13, False)
    campoattaccabileRallo4 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png', gpx * 11, gpy * 11, False)
    campoattaccabileRallo5 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png', gpx * 9, gpy * 9, False)
    campoattaccabileRobo = loadImage('Immagini/Campiattaccabili/Campoattaccabile3.png', gpx * 13, gpy * 13, False)
    caselleattaccabiliRobo = loadImage('Immagini/Campiattaccabili/CaselleattaccabiliRobo.png', gpx, gpy, True)
    caselleattaccabilimostro = loadImage('Immagini/Campiattaccabili/Caselleattaccabilimostro.png', gpx, gpy, True)
    caselleattaccabili = loadImage('Immagini/Campiattaccabili/Caselleattaccabili.png', gpx, gpy, True)

    # aumento livello
    saliliv = loadImage('Immagini/Levelup/Saliliv.png', gpx, gpy, True)
    saliliv1 = loadImage('Immagini/Levelup/Saliliv1.png', gpx, gpy, True)
    saliliv2 = loadImage('Immagini/Levelup/Saliliv2.png', gpx, gpy, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    vetImgSpadeMenu = []
    vetImgArchiMenu = []
    vetImgArmatureMenu = []
    vetImgScudiMenu = []
    vetImgGuantiMenu = []
    vetImgCollaneMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadeMenu.append(loadImage("Immagini/EquipSara/Spade/Spada%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgArchiMenu.append(loadImage("Immagini/EquipSara/Archi/Arco%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgArmatureMenu.append(loadImage("Immagini/EquipSara/Armature/Armatura%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgScudiMenu.append(loadImage("Immagini/EquipSara/Scudi/Scudo%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgGuantiMenu.append(loadImage("Immagini/EquipSara/Guanti/Guanti%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgCollaneMenu.append(loadImage("Immagini/EquipSara/Collane/Collana%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        contatoreGlobale += 1
    imgGambitSconosciuta = loadImage('Immagini/GrafGambit/Sconosciuto.png', gpx * 12, gpy * 9, False)
    vetImgCondizioniMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(loadImage("Immagini/GrafGambit/GrafCondizioni/Condizione%i.png" % contatoreGlobale, gpx * 12, gpy * 9, False))
        contatoreGlobale += 1
    vetImgTecnicheMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(loadImage("Immagini/GrafGambit/GrafTecniche/Tecnica%i.png" % contatoreGlobale, gpx * 12, gpy * 9, False))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(loadImage("Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetIcoBatterieMenu.append(loadImage("Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, gpx * 10, gpy * 10, False))
        vetImgOggettiMercante.append(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, gpx * 8, gpy * 8, False))
        vetImgOggettiStart.append(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, gpx * 4, gpy * 4, False))
        vetIcoOggettiMenu.append(loadImage("Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale, gpx, gpy, True))
        contatoreGlobale += 1

    # img equipaggiamento pixellato
    vetImgSpadePixellate = []
    vetImgArchiPixellate = []
    vetImgArmaturePixellate = []
    vetImgScudiPixellate = []
    vetImgGuantiPixellate = []
    vetImgCollanePixellate = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadePixellate.append(loadImage("Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgArchiPixellate.append(loadImage("Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgArmaturePixellate.append(loadImage("Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgScudiPixellate.append(loadImage("Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgGuantiPixellate.append(loadImage("Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgCollanePixellate.append(loadImage("Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = loadImage('Immagini/AnimazioniOggetti/Bomba.png', gpx * 3, gpy * 3, True)
    imgAnimaBombaVeleno = loadImage('Immagini/AnimazioniOggetti/BombaVeleno.png', gpx, gpy, True)
    imgAnimaBombaAppiccicosa = loadImage('Immagini/AnimazioniOggetti/BombaAppiccicosa.png', gpx, gpy, True)
    imgAnimaBombaPotenziata = loadImage('Immagini/AnimazioniOggetti/BombaPotenziata.png', gpx * 5, gpy * 5, True)
    imgAnimaPozione1 = loadImage('Immagini/AnimazioniOggetti/Pozione1.png', gpx, gpy, True)
    imgAnimaPozione2 = loadImage('Immagini/AnimazioniOggetti/Pozione2.png', gpx, gpy, True)
    imgAnimaMedicina1 = loadImage('Immagini/AnimazioniOggetti/Medicina1.png', gpx, gpy, True)
    imgAnimaMedicina2 = loadImage('Immagini/AnimazioniOggetti/Medicina2.png', gpx, gpy, True)
    imgAnimaCaricabatterie = loadImage('Immagini/AnimazioniOggetti/Caricabatterie.png', gpx, gpy, True)

    # img animazioni tecniche
    imgDanneggiamentoColco = loadImage('Immagini/AnimazioniTecniche/Danneggiamento.png', gpx, gpy, True)
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = loadImage("Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale, gpx, gpy * 2, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale, gpx, gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale, gpx * 2, gpy, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale, gpx * 2, gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale, gpx, gpy * 2, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale, gpx, gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale, gpx * 2, gpy, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale, gpx * 2, gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            imgSelf = loadImage("Immagini/AnimazioniTecniche/%sAnimaSelf.png" % contatoreGlobale, gpx, gpy, True)
            vetAnimaImgTecniche.append(imgSelf)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = loadImage("Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale, gpx, gpy, True)
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = loadImage("Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale, gpx * 13, gpy * 13, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale, gpx * 13, gpy * 13, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata.png', gpx, gpy, True)
    imgFrecciaEletttricaLanciataP = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata+.png', gpx, gpy, True)
    imgFrecciaEletttricaLanciataPP = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata++.png', gpx, gpy, True)

    # img sfondi dialoghi
    sfondoDialoghi = loadImage('Immagini/Dialoghi/SfondoSotto.png', gsx, gsy // 3, False)

    # img tutorial
    tutorialTastieraInGioco = loadImage('Immagini/Tutorial/TastieraInGioco.png', gpx * 7, gpy * 11, False)
    tutorialTastieraInMenu = loadImage('Immagini/Tutorial/TastieraInMenu.png', gpx * 7, gpy * 11, False)
    tutorialMouse = loadImage('Immagini/Tutorial/Mouse.png', gpx * 7, gpy * 11, False)
    tutorialControllerInGioco = loadImage('Immagini/Tutorial/ControllerInGioco.png', gpx * 7, gpy * 11, False)
    tutorialControllerInMenu = loadImage('Immagini/Tutorial/ControllerInMenu.png', gpx * 7, gpy * 11, False)
    impostazioniController = loadImage('Immagini/Tutorial/ImpoController.png', gpx * 14, gpy * 14, False)
    impostaControllerCroce = loadImage('Immagini/Tutorial/ImpoControllerCroce.png', gpx * 14, gpy * 14, False)
    impostaControllerCerchio = loadImage('Immagini/Tutorial/ImpoControllerCerchio.png', gpx * 14, gpy * 14, False)
    impostaControllerQuadrato = loadImage('Immagini/Tutorial/ImpoControllerQuadrato.png', gpx * 14, gpy * 14, False)
    impostaControllerTriangolo = loadImage('Immagini/Tutorial/ImpoControllerTriangolo.png', gpx * 14, gpy * 14, False)
    impostaControllerL1 = loadImage('Immagini/Tutorial/ImpoControllerL1.png', gpx * 14, gpy * 14, False)
    impostaControllerR1 = loadImage('Immagini/Tutorial/ImpoControllerR1.png', gpx * 14, gpy * 14, False)
    impostaControllerStart = loadImage('Immagini/Tutorial/ImpoControllerStart.png', gpx * 14, gpy * 14, False)
    impostaControllerCroceDirezionale = loadImage('Immagini/Tutorial/ImpoControllerCroceDirezionale.png', gpx * 14, gpy * 14, False)

    # img grafiche / dialoghi
    persGrafMenu = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/LucaGrafMenu.png', gpx * 18, gpy * 18, False)
    saraGrafMenu = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/SaraGrafMenu.png', gpx * 10, gpy * 10, False)
    fraMaggioreGrafMenu = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', gpx * 10, gpy * 10, False)
    robograf0 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf0.png', gpx * 18, gpy * 18, False)
    robograf1 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', gpx * 18, gpy * 18, False)
    robograf1b = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', gpx * 10, gpy * 10, False)
    robograf2 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', gpx * 18, gpy * 18, False)
    robograf2b = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', gpx * 10, gpy * 10, False)
    robograf3 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf3.png', gpx * 18, gpy * 18, False)
    robograf4 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', gpx * 18, gpy * 18, False)
    imgDialogoFraMaggiore = loadImage('Immagini/Dialoghi/FratelloMaggioreDialogo.png', gpx * 16, gpy * 12, False)
    imgDialogoSara = loadImage('Immagini/Dialoghi/SaraDialogo.png', gpx * 16, gpy * 12, False)
    imgFraMaggioreMenuOggetti = loadImage('Immagini/DecorazioniMenu/FratelloMaggioreMenu.png', gpx * 3, gpy * 3, True)
    imgSaraMenuOggetti = loadImage('Immagini/DecorazioniMenu/SaraMenu.png', gpx * 3, gpy * 3, True)

    # indicatori vita
    indvita = loadImage('Immagini/Barrevita/Indvita.png', 0, 0, True)
    fineindvita = loadImage('Immagini/Barrevita/FineIndVita.png', gpx // 12, gpy // 4, True)
    vitanemico00 = loadImage('Immagini/Barrevita/Vitanemico00.png', 0, 0, True)
    vitanemico0 = loadImage('Immagini/Barrevita/Vitanemico0.png', 0, 0, True)
    vitanemico1 = loadImage('Immagini/Barrevita/Vitanemico1.png', 0, 0, True)
    vitanemico2 = loadImage('Immagini/Barrevita/Vitanemico2.png', 0, 0, True)
    vitanemico3 = loadImage('Immagini/Barrevita/Vitanemico3.png', 0, 0, True)
    vitanemico4 = loadImage('Immagini/Barrevita/Vitanemico4.png', 0, 0, True)
    vitanemico5 = loadImage('Immagini/Barrevita/Vitanemico5.png', 0, 0, True)
    vitanemico6 = loadImage('Immagini/Barrevita/Vitanemico6.png', 0, 0, True)
    vitanemico7 = loadImage('Immagini/Barrevita/Vitanemico7.png', 0, 0, True)
    vitanemico8 = loadImage('Immagini/Barrevita/Vitanemico8.png', 0, 0, True)
    vitanemico9 = loadImage('Immagini/Barrevita/Vitanemico9.png', 0, 0, True)
    vitapersonaggio = loadImage('Immagini/Barrevita/Vitapersonaggio.png', 0, 0, True)
    vitarobo = loadImage('Immagini/Barrevita/Vitarobo.png', 0, 0, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = loadImage("Immagini/EquipSara/SfondoOggetto.png", gpx * 2, gpy * 2, False)
    sconosciutoEquipMenu = loadImage("Immagini/Oggetti/SconosciutoEquip.png", gpx * 2, gpy * 2, False)
    sconosciutoOggettoMenu1 = loadImage("Immagini/Oggetti/Sconosciuto.png", gpx * 4, gpy * 4, False)
    sconosciutoOggettoMenu2 = loadImage("Immagini/Oggetti/Sconosciuto.png", gpx * 8, gpy * 8, False)
    sconosciutoOggettoMenu3 = loadImage("Immagini/Oggetti/Sconosciuto.png", gpx * 10, gpy * 10, False)
    sconosciutoOggettoIcoMenu = loadImage("Immagini/Oggetti/SconosciutoIco.png", gpx, gpy, False)

    # img mappe
    imgMappa1A = loadImage("Immagini/DecorazioniMenu/MappaMenu1.png", gpx * 22, gpy * 15, False)
    imgMappa1B = loadImage("Immagini/DecorazioniMenu/MappaMenu1.png", gpx * 50, gpy * 35, False)
    imgMappa2A = loadImage("Immagini/DecorazioniMenu/MappaMenu2.png", gpx * 22, gpy * 15, False)
    imgMappa2B = loadImage("Immagini/DecorazioniMenu/MappaMenu2.png", gpx * 50, gpy * 35, False)
    imgMappa3A = loadImage("Immagini/DecorazioniMenu/MappaMenu3.png", gpx * 22, gpy * 15, False)
    imgMappa3B = loadImage("Immagini/DecorazioniMenu/MappaMenu3.png", gpx * 50, gpy * 35, False)
    imgMappa4A = loadImage("Immagini/DecorazioniMenu/MappaMenu4.png", gpx * 22, gpy * 15, False)
    imgMappa4B = loadImage("Immagini/DecorazioniMenu/MappaMenu4.png", gpx * 50, gpy * 35, False)
    imgMappa5A = loadImage("Immagini/DecorazioniMenu/MappaMenu5.png", gpx * 22, gpy * 15, False)
    imgMappa5B = loadImage("Immagini/DecorazioniMenu/MappaMenu5.png", gpx * 50, gpy * 35, False)
    imgMappa6A = loadImage("Immagini/DecorazioniMenu/MappaMenu6.png", gpx * 22, gpy * 15, False)
    imgMappa6B = loadImage("Immagini/DecorazioniMenu/MappaMenu6.png", gpx * 50, gpy * 35, False)
    imgMappa7A = loadImage("Immagini/DecorazioniMenu/MappaMenu7.png", gpx * 22, gpy * 15, False)
    imgMappa7B = loadImage("Immagini/DecorazioniMenu/MappaMenu7.png", gpx * 50, gpy * 35, False)
    imgMappa8A = loadImage("Immagini/DecorazioniMenu/MappaMenu8.png", gpx * 22, gpy * 15, False)
    imgMappa8B = loadImage("Immagini/DecorazioniMenu/MappaMenu8.png", gpx * 50, gpy * 35, False)
    imgMappa9A = loadImage("Immagini/DecorazioniMenu/MappaMenu9.png", gpx * 22, gpy * 15, False)
    imgMappa9B = loadImage("Immagini/DecorazioniMenu/MappaMenu9.png", gpx * 50, gpy * 35, False)
    imgMappa10A = loadImage("Immagini/DecorazioniMenu/MappaMenu10.png", gpx * 22, gpy * 15, False)
    imgMappa10B = loadImage("Immagini/DecorazioniMenu/MappaMenu10.png", gpx * 50, gpy * 35, False)
    imgMappa11A = loadImage("Immagini/DecorazioniMenu/MappaMenu11.png", gpx * 22, gpy * 15, False)
    imgMappa11B = loadImage("Immagini/DecorazioniMenu/MappaMenu11.png", gpx * 50, gpy * 35, False)
    imgMappa12A = loadImage("Immagini/DecorazioniMenu/MappaMenu12.png", gpx * 22, gpy * 15, False)
    imgMappa12B = loadImage("Immagini/DecorazioniMenu/MappaMenu12.png", gpx * 50, gpy * 35, False)
    imgMappa13A = loadImage("Immagini/DecorazioniMenu/MappaMenu13.png", gpx * 22, gpy * 15, False)
    imgMappa13B = loadImage("Immagini/DecorazioniMenu/MappaMenu13.png", gpx * 50, gpy * 35, False)
    imgMappa14A = loadImage("Immagini/DecorazioniMenu/MappaMenu14.png", gpx * 22, gpy * 15, False)
    imgMappa14B = loadImage("Immagini/DecorazioniMenu/MappaMenu14.png", gpx * 50, gpy * 35, False)
    imgOmbreggiaturaContorniMappaMenu = loadImage("Immagini/DecorazioniMenu/OmbreggiaturaContorniMappaMenu.png", gsx, gsy, False)

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "Cinghiale", "LupoGrigio", "LupoNero", "LupoBianco", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = loadImage("Immagini/Nemici/NemicoAvvelenato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = loadImage("Immagini/Nemici/NemicoAppiccicato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png", gpx, gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png", gpx * 2, gpy, True)
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png", gpx, gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png", gpx * 2, gpy, True)
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = loadImage("Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = loadImage("Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = loadImage("Immagini/Nemici/DannoRallo.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = loadImage("Immagini/Nemici/DannoColco.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni

# canali audio / volume (0-1)
volumeCanzoni = 1.0
volumeEffetti = 1.0
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
        loadImgs()
else:
    erroreFileImpostazioni = True
if erroreFileImpostazioni:
    print ("Errore nella lettura del file di configurazione delle impostazioni")
    opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
    schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
    loadImgs()
    initVolumeSounds()

# suoni puntatore
selsta = loadSound("Audio/RumoriPuntatore/SelSta.wav")
selind = loadSound("Audio/RumoriPuntatore/SelInd.wav")
spostapun = loadSound("Audio/RumoriPuntatore/SpostaPun.wav")
selimp = loadSound("Audio/RumoriPuntatore/SelImp.wav")
selezione = loadSound("Audio/RumoriPuntatore/Selezione.wav")
spostaPunBattaglia = loadSound("Audio/RumoriPuntatore/SpostaPunBattaglia.wav")
selObbiettivo = loadSound("Audio/RumoriPuntatore/SelObbiettivo.wav")

# suoni personaggio
rumoreAttaccoSpada = loadSound("Audio/RumoriPersonaggio/AttaccoSpada.wav")
rumoreLancioFreccia = loadSound("Audio/RumoriPersonaggio/LancioFreccia.wav")
rumoreAttaccoArco = loadSound("Audio/RumoriPersonaggio/AttaccoArco.wav")
rumoreParata = loadSound("Audio/RumoriPersonaggio/ParataConScudo.wav")
rumorecamminata = loadSound("Audio/RumoriPersonaggio/Camminata.wav")
rumorelevelup = loadSound("Audio/RumoriPersonaggio/Levelup.wav")
rumoreMorte = loadSound("Audio/RumoriPersonaggio/Morte.wav")

# suoni apertura-chiusura cofanetti-porte
suonoaperturacofanetti = loadSound("Audio/RumoriAmbiente/AperturaCofanetto.wav")
suonoaperturaporteForesta = loadSound("Audio/RumoriAmbiente/AperturaPortaForesta.wav")
suonochiusuraporteForesta = loadSound("Audio/RumoriAmbiente/ChiusuraPortaForesta.wav")
suonoaperturaporteCasa = loadSound("Audio/RumoriAmbiente/AperturaPortaCasa.wav")
suonochiusuraporteCasa = loadSound("Audio/RumoriAmbiente/ChiusuraPortaCasa.wav")

# souno raccolta esca - monete
suonoRaccoltaEsca = loadSound("Audio/RumoriAmbiente/RaccoltaEsca.wav")
suonoRaccoltaMonete = loadSound("Audio/RumoriAmbiente/RaccoltaMonete.wav")
rumoreAcquisto = loadSound("Audio/RumoriAmbiente/Acquisto.wav")

# suoni robo
rumoreCamminataColco = loadSound("Audio/RumoriColco/Camminata.wav")
rumoreScossaFreccia = loadSound("Audio/RumoriColco/ScossaFreccia.wav")
rumoreTempestaElettrica = loadSound("Audio/RumoriColco/TempestaElettrica.wav")
rumoreCuraRobo = loadSound("Audio/RumoriColco/Cura.wav")
rumoreAntidoto = loadSound("Audio/RumoriColco/Antidoto.wav")
rumoreAttPDifP = loadSound("Audio/RumoriColco/AttPDifP.wav")
rumoreAutoricarica = loadSound("Audio/RumoriColco/Autoricarica.wav")
rumoreRaffreddamento = loadSound("Audio/RumoriColco/Raffreddamento.wav")
rumoreVelocizzaEfficienza = loadSound("Audio/RumoriColco/VelocizzaEfficienza.wav")

# suono oggetti
suonoTeleColco = loadSound("Audio/RumoriOggetti/TeleColco.wav")
suonoLancioOggetti = loadSound("Audio/RumoriOggetti/LancioOggetti.wav")
suonoUsoPozione = loadSound("Audio/RumoriOggetti/Pozione.wav")
suonoUsoCaricabatterie = loadSound("Audio/RumoriOggetti/Caricabatterie.wav")
suonoUsoMedicina = loadSound("Audio/RumoriOggetti/Medicina.wav")
suonoUsoBomba = loadSound("Audio/RumoriOggetti/Bomba.wav")
suonoUsoBombaVeleno = loadSound("Audio/RumoriOggetti/BombaVeleno.wav")
suonoUsoEsca = loadSound("Audio/RumoriOggetti/Esca.wav")
suonoUsoBombaAppiccicosa = loadSound("Audio/RumoriOggetti/BombaAppiccicosa.wav")
suonoUsoBombaPotenziata = loadSound("Audio/RumoriOggetti/BombaPotenziata.wav")

# suoni nemici
rumoreMovimentoNemiciPersonaggi = loadSound("Audio/RumoriNemiciPersonaggi/MovimentoNemiciPersonaggi.wav")
rumoreAttaccoNemico = loadSound("Audio/RumoriNemiciPersonaggi/AttaccoVicinoNemico.wav")
rumoreLancioOggettoNemico = loadSound("Audio/RumoriNemiciPersonaggi/AttaccoLontanoNemico.wav")
rumoreMorteNemico = loadSound("Audio/RumoriNemiciPersonaggi/MorteNemico.wav")

# suono mappa
suonoAperturaMappa = loadSound("Audio/RumoriAmbiente/AperturaMappa.wav")

# suoni sottofondi ambientali
audioSottofondoVideoIniziale = loadSound("Video/AudioVideoInizio.wav")
audioAmbienteSogno = loadSound("Audio/RumoriAmbiente/SottofondoPerZona/Sogno.wav")
audioAmbienteCasaInterno = loadSound("Audio/RumoriAmbiente/SottofondoPerZona/CasaInterno.wav")
audioAmbienteCasaEsterno = loadSound("Audio/RumoriAmbiente/SottofondoPerZona/CasaEsterno.wav")
audioAmbienteForesta = loadSound("Audio/RumoriAmbiente/SottofondoPerZona/Foresta.wav")

# suoni canzoni
canzoneMenuPrincipale = loadSound("Audio/Canzoni/Canzone11.wav")
canzoneSogno = loadSound("Audio/Canzoni/Canzone27.wav")
canzoneCasa = loadSound("Audio/Canzoni/Canzone24.wav")
canzoneForesta = loadSound("Audio/Canzoni/Canzone27.wav")

# dati tecniche di Colco [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesa++]
costoTecniche = [5, 10, 10, 5, 10, 10, 1, 20, 10, 10, 15, 20, 20, 30, 20, 30, 1, 20, 20, 40]
dannoTecniche = [40, 30, 0, 30, 20, 0, 150, 120, 160, 130, 15, 10, 10, 15, 100, 250, 300, 320, 260, 200]

# costo oggetti => costoOggetti[frecce, pozione, caricabatterie, medicina, superpozione, caricabatterie migliorato, bomba, bomba veleno, esca, bomba appiccicosa, bomba potenziata, faretra1, faretra2, faretra3]
costoOggetti = [1, 5, 5, 7, 20, 20, 10, 15, 30, 50, 50, 10, 50, 250]
# danno oggetti => dannoOggetti[bomba, bombaVeleno, esca, bombaAppiccicosa, bombaPotenziata]
dannoOggetti = [100, 50, 0, 20, 500]

# dichiaro il dictionary che contiene gli avanzamenti della storia associati agli avvenimenti
dictAvanzamentoStoria = definisciAvanzamentiStoria()
# dichiaro il dictionary che contiene le stanze associate a un nome che le descrive
dictStanze, vetStanzePacifiche = definisciStanze()

# dichiaro i vettori di porte e cofanetti
initVetPorteGlobale = definisciPorte(dictStanze)
initVetCofanettiGlobale = definisciCofanetti(dictStanze)

vistaRobo = 6

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
configuraCursore(False)

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
    pygame.draw.line(schermo, colore, coordinateInizio, coordinateFine, spessore)
    x, y = coordinateInizio
    xFine, yFine = coordinateFine
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
