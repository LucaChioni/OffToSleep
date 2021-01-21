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
icona = pygame.image.load(gamePath + "Immagini/Icone/Icona.png")
pygame.display.set_icon(icona)
fontUtilizzato = "Liberation Serif"
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

    # aumento la risoluzione per evitare imprecisioni delle img piccole e bug dello smoothscale per le img grandi (lo smoothscle ha problemi nel ridurre la risoluzione)
    if aumentaRisoluzione:
        risoluzioneXPerFix = xScale
        risoluzioneYPerFix = yScale
    else:
        risoluzioneXPerFix = xScale * 2
        risoluzioneYPerFix = yScale * 2
    sizeX, sizeY = img.get_rect().size
    moltiplicatore = 1
    while sizeX * moltiplicatore < risoluzioneXPerFix and sizeY * moltiplicatore < risoluzioneYPerFix:
        moltiplicatore += 1
    img = pygame.transform.scale(img, (sizeX * moltiplicatore, sizeY * moltiplicatore))

    if xScale != 0 and yScale != 0:
        img = pygame.transform.smoothscale(img, (int(xScale), int(yScale)))
    if canale_alpha:
        img = img.convert_alpha()
    else:
        img = img.convert()

    # per poter chiudere il gioco durante il caricamento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    global listaTastiPremuti
    listaTastiPremuti = []

    return img

def loadSound(path):
    try:
        sound = pygame.mixer.Sound(gamePath + path)
    except Exception:
        print ("Impossibile caricare " + path)
        sound = False

    # per poter chiudere il gioco durante il caricamento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    return sound

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

def caricaImmagineMostrandoAvanzamento(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True):
    global numImgCaricata
    immagine = loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha)
    disegnaRettangoloSuSchermo(schermo, grigioscuPiuScu, (int(gpx * 0.5), gpy * 6.5, int(gpx * 16), gpy * 1))
    numImgCaricata += 1
    caricamentoCompiuto = (gpx * 15.0 / numImgTotali) * numImgCaricata
    disegnaRettangoloSuSchermo(schermo, grigio, (int(gpx * 0.5), gpy * 6.5, int(caricamentoCompiuto), gpy * 1))
    aggiornaSchermo()
    return immagine
def caricaImmagineCambioRisoluzione(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True):
    global numImgCaricata
    immagine = loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha)
    disegnaRettangoloSuSchermo(schermo, grigioscuPiuScu, (int(gpx * 0.5), gpy * 10, int(gpx * 31), gpy * 1))
    numImgCaricata += 1
    caricamentoCompiuto = (gpx * 31.0 / numImgTotali) * numImgCaricata
    disegnaRettangoloSuSchermo(schermo, grigio, (int(gpx * 0.5), gpy * 10, int(caricamentoCompiuto), gpy * 1))
    aggiornaSchermo()
    return immagine

numSndTotali = 55
numSndCaricato = 0
def caricaSuonoMostrandoAvanzamento(path):
    global numSndCaricato
    suono = loadSound(path)
    disegnaRettangoloSuSchermo(schermo, grigioscuPiuScu, (int(gpx * 0.5), gpy * 6.5, int(gpx * 16), gpy * 1))
    numSndCaricato += 1
    caricamentoCompiuto = (gpx * 15) + ((gpx * 1.0 / numSndTotali) * numSndCaricato)
    disegnaRettangoloSuSchermo(schermo, grigio, (int(gpx * 0.5), gpy * 6.5, int(caricamentoCompiuto), gpy * 1))
    aggiornaSchermo()
    return suono

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
global lucyGrafMenu
global fraMaggioreGrafMenu
global robograf0
global robograf1
global robograf1b
global robograf2
global robograf2b
global robograf3
global robograf4
global imgDialogoFraMaggiore
global imgDialogoLucy
global imgFraMaggioreMenuOggetti
global imgLucyMenuOggetti
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
global persoLucy
global persobLucy
global persoFraMaggiore
global persobFraMaggiore
global schemataDiCaricamento
def loadImgs(cambioRisoluzione=False):
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
    global lucyGrafMenu
    global fraMaggioreGrafMenu
    global robograf0
    global robograf1
    global robograf1b
    global robograf2
    global robograf2b
    global robograf3
    global robograf4
    global imgDialogoFraMaggiore
    global imgDialogoLucy
    global imgFraMaggioreMenuOggetti
    global imgLucyMenuOggetti
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
    global persoLucy
    global persobLucy
    global persoFraMaggiore
    global persobFraMaggiore
    global schemataDiCaricamento

    if cambioRisoluzione:
        funzionePerCaricareImmagini = caricaImmagineCambioRisoluzione
    else:
        funzionePerCaricareImmagini = caricaImmagineMostrandoAvanzamento

    # puntatore
    puntatore = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/Puntatore.png", gpx // 2, gpy // 2, True)
    puntatorevecchio = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/Puntatorevecchio.png", gpx // 2, gpy // 2, True)
    puntatIn = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/InquadraCVin.png', gpx, gpy, True)
    puntatOut = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/InquadraCVout.png', gpx, gpy, True)
    puntatSfo = funzionePerCaricareImmagini('Immagini/Oggetti/sfondoOggettoLanciato.png', gpx, gpy, True)
    puntatDif = funzionePerCaricareImmagini('Immagini/Oggetti/Difesa.png', gpx, gpy, True)
    puntatAtt = funzionePerCaricareImmagini('Immagini/Oggetti/Attacco.png', gpx, gpy, True)
    puntatArc = funzionePerCaricareImmagini('Immagini/Oggetti/AttaccoDistanza.png', gpx, gpy, True)
    puntatPor = funzionePerCaricareImmagini('Immagini/Oggetti/ApriChiudiPorta.png', gpx, gpy, True)
    puntatCof = funzionePerCaricareImmagini('Immagini/Oggetti/ApriCofanetto.png', gpx, gpy, True)
    puntatAnalisi = funzionePerCaricareImmagini('Immagini/Oggetti/AnalizzaColco.png', gpx, gpy, True)
    puntatBom = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto6Ico.png', gpx, gpy, True)
    puntatBoV = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto7Ico.png', gpx, gpy, True)
    puntatEsc = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto8Ico.png', gpx, gpy, True)
    puntatBoA = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto9Ico.png', gpx, gpy, True)
    puntatBoP = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto10Ico.png', gpx, gpy, True)
    scorriSu = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriOggettiSu.png", gpx, gpy, True)
    scorriGiu = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriOggettiGiu.png", gpx, gpy, True)
    puntatDialoghi = funzionePerCaricareImmagini('Immagini/Oggetti/IcoDialogo.png', gpx, gpy, True)
    puntatoreInquadraNemici = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/InquadraNemicoSelezionato.png", gpx, gpy, True)
    puntatoreImpostazioniDestra = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestra.png", gpx, gpy, True)
    puntatoreImpostazioniSinistra = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistra.png", gpx, gpy, True)
    puntatoreImpostazioniDestraBloccato = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestraBloccato.png", gpx, gpy, True)
    puntatoreImpostazioniSinistraBloccato = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistraBloccato.png", gpx, gpy, True)

    # immagini personaggio
    persw = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio4.png', gpx, gpy, True)
    perswb = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio4b.png', gpx, gpy, True)
    persa = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio3.png', gpx, gpy, True)
    persab = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio3b.png', gpx, gpy, True)
    perso = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1.png', gpx * 5, gpy * 5, True)
    persob = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1b.png', gpx * 5, gpy * 5, True)
    perss = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1.png', gpx, gpy, True)
    perssb = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1b.png', gpx, gpy, True)
    persd = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio2.png', gpx, gpy, True)
    persdb = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio2b.png', gpx, gpy, True)
    perssm = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1mov.png', gpx, gpy, True)
    perssmb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1movb1.png', gpx, gpy, True)
    perssmb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1movb2.png', gpx, gpy, True)
    persdm = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio2mov.png', gpx, gpy, True)
    persdmb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio2movb1.png', gpx, gpy, True)
    persdmb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio2movb2.png', gpx, gpy, True)
    persam = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio3mov.png', gpx, gpy, True)
    persamb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio3movb1.png', gpx, gpy, True)
    persamb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio3movb2.png', gpx, gpy, True)
    perswm = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio4mov.png', gpx, gpy, True)
    perswmb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio4movb1.png', gpx, gpy, True)
    perswmb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio4movb2.png', gpx, gpy, True)
    perswmbAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio4movbAttacco.png', gpx, gpy, True)
    persambAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio3movbAttacco.png', gpx, gpy, True)
    perssmbAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1movbAttacco.png', gpx, gpy, True)
    persdmbAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio2movbAttacco.png', gpx, gpy, True)
    persmbDifesa = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/PersonaggiomovbDifesa.png', gpx, gpy, True)
    persAvvele = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/PersonaggioAvvelenato.png', gpx, gpy, True)
    persoLucy = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1.png', gpx * 5, gpy * 5, True)
    persobLucy = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy/Personaggio1b.png', gpx * 5, gpy * 5, True)
    persoFraMaggiore = funzionePerCaricareImmagini('Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', gpx * 5, gpy * 5, True)
    persobFraMaggiore = funzionePerCaricareImmagini('Immagini/Personaggi/FratelloMaggiore/Personaggio1b.png', gpx * 5, gpy * 5, True)

    # immagini robot
    robow = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot4.png', gpx, gpy, True)
    roboa = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot3.png', gpx, gpy, True)
    roboo1 = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot1.png', gpx * 5, gpy * 5, True)
    roboo2 = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot1.png', gpx * 3, gpy * 3, True)
    robos = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot1.png', gpx, gpy, True)
    robod = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot2.png', gpx, gpy, True)
    robomo = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot0.png', gpx, gpy, True)
    robodp = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot2p.png', gpx, gpy, True)
    roboap = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot3p.png', gpx, gpy, True)
    armrobmo = funzionePerCaricareImmagini('Immagini/EquipRobo/Batteria00.png', gpx, gpy, True)
    roboSurrisc = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/RobotSurriscaldato.png', gpx, gpy, True)

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = funzionePerCaricareImmagini("Immagini/Nemici/DannoRallo.png", gpx, gpy, True)
    imgDanneggiamentoCausaColco = funzionePerCaricareImmagini("Immagini/Nemici/DannoColco.png", gpx, gpy, True)

    # img menu mercante
    mercanteMenu = funzionePerCaricareImmagini('Immagini/Personaggi/Mercante/MercanteDialogo.png', gpx * 12, gpy * 9, False)
    scorriSuGiu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiu.png', gpx, gpy, True)
    scorriSuGiuBloccato = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccato.png', gpx, gpy, True)
    scorriSuGiuBloccatoGiu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoGiu.png', gpx, gpy, True)
    scorriSuGiuBloccatoSu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoSu.png', gpx, gpy, True)
    sfondoDialogoMercante = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/SfondoDialogoMercante.png', gpx * 9.5, gpy * 4.5, False)
    faretra1Menu = funzionePerCaricareImmagini('Immagini/Oggetti/Faretra1Menu.png', gpx * 8, gpy * 8, False)
    faretra2Menu = funzionePerCaricareImmagini('Immagini/Oggetti/Faretra2Menu.png', gpx * 8, gpy * 8, False)
    faretra3Menu = funzionePerCaricareImmagini('Immagini/Oggetti/Faretra3Menu.png', gpx * 8, gpy * 8, False)
    frecciaMenu = funzionePerCaricareImmagini('Immagini/Oggetti/FrecciaMenu.png', gpx * 8, gpy * 8, False)

    # sfondi
    sfondoRallo = funzionePerCaricareImmagini('Immagini/Status/SfondoRallo.png', gpx * 6, gpy, False)
    sfondoColco = funzionePerCaricareImmagini('Immagini/Status/SfondoColco.png', gpx * 4, gpy, False)
    sfondoMostro = funzionePerCaricareImmagini('Immagini/Status/SfondoNemici.png', gpx * 3, gpy, False)
    sfondoEsche = funzionePerCaricareImmagini('Immagini/Status/SfondoEsche.png', gpx, gpy, True)
    sfondoStartBattaglia = funzionePerCaricareImmagini('Immagini/Oggetti/SfondoStartBattaglia.png', gpx * 7, gpy * 10, False)
    sfondoTriangolinoAltoDestra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloAltoDestra.png', gpx, gpy, True)
    sfondoTriangolinoAltoSinistra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', gpx, gpy, True)
    sfondoTriangolinoBassoDestra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloBassoDestra.png', gpx, gpy, True)
    sfondoTriangolinoBassoSinistra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', gpx, gpy, True)

    # status
    appiccicoso = funzionePerCaricareImmagini('Immagini/Status/Appiccicoso.png', gpx * 3 // 4, gpy * 3 // 4, True)
    avvelenatoMenu = funzionePerCaricareImmagini('Immagini/Status/Avvelenato.png', gpx, gpy, True)
    avvelenato = funzionePerCaricareImmagini('Immagini/Status/Avvelenato.png', gpx * 3 // 4, gpy * 3 // 4, True)
    surriscaldatoMenu = funzionePerCaricareImmagini('Immagini/Status/Surriscaldato.png', gpx, gpy, True)
    surriscaldato = funzionePerCaricareImmagini('Immagini/Status/Surriscaldato.png', gpx * 3 // 4, gpy * 3 // 4, True)
    attaccopiuMenu = funzionePerCaricareImmagini('Immagini/Status/Attaccopiu.png', gpx, gpy, True)
    attaccopiu = funzionePerCaricareImmagini('Immagini/Status/Attaccopiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    difesapiuMenu = funzionePerCaricareImmagini('Immagini/Status/Difesapiu.png', gpx, gpy, True)
    difesapiu = funzionePerCaricareImmagini('Immagini/Status/Difesapiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    velocitapiuMenu = funzionePerCaricareImmagini('Immagini/Status/Velocitapiu.png', gpx, gpy, True)
    velocitapiu = funzionePerCaricareImmagini('Immagini/Status/Velocitapiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    efficienzapiuMenu = funzionePerCaricareImmagini('Immagini/Status/Efficienzapiu.png', gpx, gpy, True)
    efficienzapiu = funzionePerCaricareImmagini('Immagini/Status/Efficienzapiu.png', gpx * 3 // 4, gpy * 3 // 4, True)
    imgNumFrecce = funzionePerCaricareImmagini('Immagini/Status/NumFrecce.png', gpx * 3 // 4, gpy * 3 // 4, True)

    # menu alto destra
    sfochiaveocchio = funzionePerCaricareImmagini("Immagini/Oggetti/SfondoOcchioChiave.png", gpx * 5, gpy * 2, False)
    occhioape = funzionePerCaricareImmagini('Immagini/Status/OcchioAperto.png', gpx, gpy, True)
    occhiochiu = funzionePerCaricareImmagini('Immagini/Status/OcchioChiuso.png', gpx, gpy, True)
    chiaveroboacc = funzionePerCaricareImmagini('Immagini/Oggetti/ChiaveColcoAcc.png', gpx * 2, gpy * 2, True)
    chiaverobospe = funzionePerCaricareImmagini('Immagini/Oggetti/ChiaveColcoSpe.png', gpx * 2, gpy * 2, True)

    # oggetti sulla schermata
    esche = funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto8Ico.png", gpx, gpy, True)
    sacchettoDenaroStart = funzionePerCaricareImmagini('Immagini/Oggetti/SacchettoDenaroSinistra.png', gpx * 4, gpy * 4, False)
    sacchettoDenaroMercante = funzionePerCaricareImmagini('Immagini/Oggetti/SacchettoDenaroDestra.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart0 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra0Menu.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart1 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra1Menu.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart2 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra2Menu.png', gpx * 4, gpy * 4, False)
    faretraFrecceStart3 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra3Menu.png', gpx * 4, gpy * 4, False)
    sacchettoDenaro = funzionePerCaricareImmagini('Immagini/Oggetti/SacchettoDenaroIco.png', gpx, gpy, True)
    imgFrecciaLanciata = funzionePerCaricareImmagini('Immagini/Oggetti/Freccia.png', gpx, gpy, True)

    # cofanetti
    cofaniaper = funzionePerCaricareImmagini("Immagini/Oggetti/CofanettoAperto.png", gpx, gpy, True)
    cofanichiu = funzionePerCaricareImmagini("Immagini/Oggetti/CofanettoChiuso.png", gpx, gpy, True)
    sfocontcof = funzionePerCaricareImmagini("Immagini/Oggetti/SfondoContenutoCofanetto.png", gpx * 16, gpy * 3, False)

    # immagini salvataggi
    s1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Salvataggi/S1.png', gpx * 3, gpy * 3, False)
    s2 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Salvataggi/S2.png', gpx * 3, gpy * 3, False)
    s3 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Salvataggi/S3.png', gpx * 3, gpy * 3, False)

    # caselle attaccabili
    campoattaccabileRallo1 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', gpx * 13, gpy * 13, False)
    campoattaccabileRallo2 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', gpx * 11, gpy * 11, False)
    campoattaccabileRallo3 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', gpx * 13, gpy * 13, False)
    campoattaccabileRallo4 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', gpx * 11, gpy * 11, False)
    campoattaccabileRallo5 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', gpx * 9, gpy * 9, False)
    campoattaccabileRobo = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile3.png', gpx * 13, gpy * 13, False)
    caselleattaccabiliRobo = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/CaselleattaccabiliRobo.png', gpx, gpy, True)
    caselleattaccabilimostro = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Caselleattaccabilimostro.png', gpx, gpy, True)
    caselleattaccabili = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Caselleattaccabili.png', gpx, gpy, True)

    # aumento livello
    saliliv = funzionePerCaricareImmagini('Immagini/Status/Levelup/Saliliv.png', gpx, gpy, True)
    saliliv1 = funzionePerCaricareImmagini('Immagini/Status/Levelup/Saliliv1.png', gpx, gpy, True)
    saliliv2 = funzionePerCaricareImmagini('Immagini/Status/Levelup/Saliliv2.png', gpx, gpy, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    vetImgSpadeMenu = []
    vetImgArchiMenu = []
    vetImgArmatureMenu = []
    vetImgScudiMenu = []
    vetImgGuantiMenu = []
    vetImgCollaneMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadeMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Spade/Spada%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgArchiMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Archi/Arco%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgArmatureMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Armature/Armatura%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgScudiMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Scudi/Scudo%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgGuantiMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Guanti/Guanti%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        vetImgCollaneMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Collane/Collana%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        contatoreGlobale += 1
    imgGambitSconosciuta = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/GrafGambit/Sconosciuto.png', gpx * 12, gpy * 9, False)
    vetImgCondizioniMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(funzionePerCaricareImmagini("Immagini/DecorazioniMenu/GrafGambit/GrafCondizioni/Condizione%i.png" % contatoreGlobale, gpx * 12, gpy * 9, False))
        contatoreGlobale += 1
    vetImgTecnicheMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(funzionePerCaricareImmagini("Immagini/DecorazioniMenu/GrafGambit/GrafTecniche/Tecnica%i.png" % contatoreGlobale, gpx * 12, gpy * 9, False))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(funzionePerCaricareImmagini("Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetIcoBatterieMenu.append(funzionePerCaricareImmagini("Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale, gpx * 2, gpy * 2, False))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, gpx * 10, gpy * 10, False))
        vetImgOggettiMercante.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, gpx * 8, gpy * 8, False))
        vetImgOggettiStart.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, gpx * 4, gpy * 4, False))
        vetIcoOggettiMenu.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale, gpx, gpy, True))
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
        vetImgSpadePixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Spade/Spada%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgArchiPixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Archi/Arco%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgArmaturePixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Armature/Armatura%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgScudiPixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Scudi/Scudo%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgGuantiPixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Guanti/Guanti%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        vetImgCollanePixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Collane/Collana%is.png" % contatoreGlobale, gpx * 5, gpy * 5, True))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Bomba.png', gpx * 3, gpy * 3, True)
    imgAnimaBombaVeleno = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/BombaVeleno.png', gpx, gpy, True)
    imgAnimaBombaAppiccicosa = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/BombaAppiccicosa.png', gpx, gpy, True)
    imgAnimaBombaPotenziata = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/BombaPotenziata.png', gpx * 5, gpy * 5, True)
    imgAnimaPozione1 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Pozione1.png', gpx, gpy, True)
    imgAnimaPozione2 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Pozione2.png', gpx, gpy, True)
    imgAnimaMedicina1 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Medicina1.png', gpx, gpy, True)
    imgAnimaMedicina2 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Medicina2.png', gpx, gpy, True)
    imgAnimaCaricabatterie = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Caricabatterie.png', gpx, gpy, True)

    # img animazioni tecniche
    imgDanneggiamentoColco = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/Danneggiamento.png', gpx, gpy, True)
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale, gpx, gpy * 2, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale, gpx, gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale, gpx * 2, gpy, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale, gpx * 2, gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale, gpx, gpy * 2, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale, gpx, gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale, gpx * 2, gpy, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale, gpx * 2, gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            imgSelf = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnimaSelf.png" % contatoreGlobale, gpx, gpy, True)
            vetAnimaImgTecniche.append(imgSelf)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale, gpx, gpy, True)
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale, gpx * 13, gpy * 13, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale, gpx * 13, gpy * 13, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/FrecciaLanciata.png', gpx, gpy, True)
    imgFrecciaEletttricaLanciataP = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/FrecciaLanciata+.png', gpx, gpy, True)
    imgFrecciaEletttricaLanciataPP = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/FrecciaLanciata++.png', gpx, gpy, True)

    # img sfondi dialoghi
    sfondoDialoghi = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/SfondoSotto.png', gsx, gsy // 3, False)

    # img tutorial
    tutorialTastieraInGioco = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/TastieraInGioco.png', gpx * 7, gpy * 11, False)
    tutorialTastieraInMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/TastieraInMenu.png', gpx * 7, gpy * 11, False)
    tutorialMouse = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/Mouse.png', gpx * 7, gpy * 11, False)
    tutorialControllerInGioco = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ControllerInGioco.png', gpx * 7, gpy * 11, False)
    tutorialControllerInMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ControllerInMenu.png', gpx * 7, gpy * 11, False)
    impostazioniController = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoController.png', gpx * 14, gpy * 14, False)
    impostaControllerCroce = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroce.png', gpx * 14, gpy * 14, False)
    impostaControllerCerchio = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerCerchio.png', gpx * 14, gpy * 14, False)
    impostaControllerQuadrato = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerQuadrato.png', gpx * 14, gpy * 14, False)
    impostaControllerTriangolo = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerTriangolo.png', gpx * 14, gpy * 14, False)
    impostaControllerL1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerL1.png', gpx * 14, gpy * 14, False)
    impostaControllerR1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerR1.png', gpx * 14, gpy * 14, False)
    impostaControllerStart = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerStart.png', gpx * 14, gpy * 14, False)
    impostaControllerCroceDirezionale = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale.png', gpx * 14, gpy * 14, False)

    # img grafiche / dialoghi
    persGrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/NeilGrafMenu.png', gpx * 18, gpy * 18, False)
    lucyGrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/LucyGrafMenu.png', gpx * 10, gpy * 10, False)
    fraMaggioreGrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', gpx * 10, gpy * 10, False)
    robograf0 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf0.png', gpx * 18, gpy * 18, False)
    robograf1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', gpx * 18, gpy * 18, False)
    robograf1b = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', gpx * 10, gpy * 10, False)
    robograf2 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', gpx * 18, gpy * 18, False)
    robograf2b = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', gpx * 10, gpy * 10, False)
    robograf3 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf3.png', gpx * 18, gpy * 18, False)
    robograf4 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', gpx * 18, gpy * 18, False)
    imgDialogoFraMaggiore = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/FratelloMaggioreDialogo.png', gpx * 16, gpy * 12, False)
    imgDialogoLucy = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/LucyDialogo.png', gpx * 16, gpy * 12, False)
    imgFraMaggioreMenuOggetti = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/FratelloMaggioreMenu.png', gpx * 3, gpy * 3, True)
    imgLucyMenuOggetti = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/LucyMenu.png', gpx * 3, gpy * 3, True)

    # indicatori vita
    indvita = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Indvita.png', 0, 0, True)
    fineindvita = funzionePerCaricareImmagini('Immagini/Status/Barrevita/FineIndVita.png', gpx // 12, gpy // 4, True)
    vitanemico00 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico00.png', 0, 0, True)
    vitanemico0 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico0.png', 0, 0, True)
    vitanemico1 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico1.png', 0, 0, True)
    vitanemico2 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico2.png', 0, 0, True)
    vitanemico3 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico3.png', 0, 0, True)
    vitanemico4 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico4.png', 0, 0, True)
    vitanemico5 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico5.png', 0, 0, True)
    vitanemico6 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico6.png', 0, 0, True)
    vitanemico7 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico7.png', 0, 0, True)
    vitanemico8 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico8.png', 0, 0, True)
    vitanemico9 = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitanemico9.png', 0, 0, True)
    vitapersonaggio = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitapersonaggio.png', 0, 0, True)
    vitarobo = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Vitarobo.png', 0, 0, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = funzionePerCaricareImmagini("Immagini/EquipLucy/SfondoOggetto.png", gpx * 2, gpy * 2, False)
    sconosciutoEquipMenu = funzionePerCaricareImmagini("Immagini/Oggetti/SconosciutoEquip.png", gpx * 2, gpy * 2, False)
    sconosciutoOggettoMenu1 = funzionePerCaricareImmagini("Immagini/Oggetti/Sconosciuto.png", gpx * 4, gpy * 4, False)
    sconosciutoOggettoMenu2 = funzionePerCaricareImmagini("Immagini/Oggetti/Sconosciuto.png", gpx * 8, gpy * 8, False)
    sconosciutoOggettoMenu3 = funzionePerCaricareImmagini("Immagini/Oggetti/Sconosciuto.png", gpx * 10, gpy * 10, False)
    sconosciutoOggettoIcoMenu = funzionePerCaricareImmagini("Immagini/Oggetti/SconosciutoIco.png", gpx, gpy, False)

    # img mappe
    imgMappa1A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", gpx * 22, gpy * 15, False)
    imgMappa1B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", gpx * 50, gpy * 35, False)
    imgMappa2A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", gpx * 22, gpy * 15, False)
    imgMappa2B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", gpx * 50, gpy * 35, False)
    imgMappa3A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", gpx * 22, gpy * 15, False)
    imgMappa3B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", gpx * 50, gpy * 35, False)
    imgMappa4A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", gpx * 22, gpy * 15, False)
    imgMappa4B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", gpx * 50, gpy * 35, False)
    imgMappa5A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", gpx * 22, gpy * 15, False)
    imgMappa5B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", gpx * 50, gpy * 35, False)
    imgMappa6A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", gpx * 22, gpy * 15, False)
    imgMappa6B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", gpx * 50, gpy * 35, False)
    imgMappa7A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", gpx * 22, gpy * 15, False)
    imgMappa7B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", gpx * 50, gpy * 35, False)
    imgMappa8A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", gpx * 22, gpy * 15, False)
    imgMappa8B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", gpx * 50, gpy * 35, False)
    imgMappa9A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", gpx * 22, gpy * 15, False)
    imgMappa9B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", gpx * 50, gpy * 35, False)
    imgMappa10A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", gpx * 22, gpy * 15, False)
    imgMappa10B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", gpx * 50, gpy * 35, False)
    imgMappa11A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", gpx * 22, gpy * 15, False)
    imgMappa11B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", gpx * 50, gpy * 35, False)
    imgMappa12A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", gpx * 22, gpy * 15, False)
    imgMappa12B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", gpx * 50, gpy * 35, False)
    imgMappa13A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", gpx * 22, gpy * 15, False)
    imgMappa13B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", gpx * 50, gpy * 35, False)
    imgMappa14A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", gpx * 22, gpy * 15, False)
    imgMappa14B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", gpx * 50, gpy * 35, False)
    imgOmbreggiaturaContorniMappaMenu = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/OmbreggiaturaContorniMappaMenu.png", gsx, gsy, False)

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "Cinghiale", "LupoGrigio", "LupoNero", "LupoBianco", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = funzionePerCaricareImmagini("Immagini/Nemici/NemicoAvvelenato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = funzionePerCaricareImmagini("Immagini/Nemici/NemicoAppiccicato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png", gpx, gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png", gpx * 2, gpy, True)
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png", gpx, gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png", gpx * 2, gpy, True)
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = funzionePerCaricareImmagini("Immagini/Nemici/DannoRallo.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = funzionePerCaricareImmagini("Immagini/Nemici/DannoColco.png", gpx, gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni

    schemataDiCaricamento = loadImage("Immagini/DecorazioniMenu/SchermataDiCaricamento.png", gsx, gsy, False)

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

def mostraLogo():
    effettoAvvio = loadSound("Audio/RumoriAmbiente/EffettoAvvio.wav")
    canaleSoundCanzone.play(effettoAvvio)
    logo = loadImage("Immagini/Icone/LogoPresentazione.png", gpx * 12, gpy * 12, True)
    disegnaImmagineSuSchermo(logo, (gpx * 10, gpy * 3))

    rect = pygame.display.get_surface().get_rect()
    vetImg = []
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 250))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 200))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 150))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 100))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 60))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 20))
    vetImg.append(image.convert_alpha(schermo))
    i = 0
    while i <= 5:
        disegnaImmagineSuSchermo(logo, (gpx * 10, gpy * 3))
        disegnaImmagineSuSchermo(vetImg[i], (0, 0))
        aggiornaSchermo()
        pygame.event.pump()
        clockFadeToBlack.tick(fpsFadeToBlack)
        i += 1
    disegnaImmagineSuSchermo(logo, (gpx * 10, gpy * 3))
    aggiornaSchermo()

    pygame.time.wait(1000)

    rect = pygame.display.get_surface().get_rect()
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 100))
    image = image.convert_alpha(schermo)
    i = 0
    while i <= 5:
        disegnaImmagineSuSchermo(image, (0, 0))
        aggiornaSchermo()
        pygame.event.pump()
        clockFadeToBlack.tick(fpsFadeToBlack)
        i += 1
    disegnaColoreSuTuttoLoSchermo(nero)
    aggiornaSchermo()
global canzoneMenuPrincipale
def disegnaSchermataDiCaricamento():
    global canzoneMenuPrincipale
    canzoneMenuPrincipale = loadSound("Audio/Canzoni/00-Menu.wav")
    canaleSoundCanzone.play(canzoneMenuPrincipale, -1)

    global schemataDiCaricamento
    schemataDiCaricamento = loadImage("Immagini/DecorazioniMenu/SchermataDiCaricamento.png", gsx, gsy, False)
    disegnaColoreSuTuttoLoSchermo(grigioscu)
    disegnaImmagineSuSchermo(schemataDiCaricamento, (0, 0))
    carattere = pygame.font.SysFont(fontUtilizzato, gpx * 130 // 60)
    testo = carattere.render("Caricamento...", True, grigiochi)
    disegnaImmagineSuSchermo(testo, (gsx // 32 * 1, gsy // 18 * 4))
    screen = schermo.copy().convert()

    rect = pygame.display.get_surface().get_rect()
    vetImg = []
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 250))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 200))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 150))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 100))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 60))
    vetImg.append(image.convert_alpha(schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 20))
    vetImg.append(image.convert_alpha(schermo))
    i = 0
    while i <= 5:
        disegnaImmagineSuSchermo(screen, (0, 0))
        disegnaImmagineSuSchermo(vetImg[i], (0, 0))
        aggiornaSchermo()
        pygame.event.pump()
        clockFadeToBlack.tick(fpsFadeToBlack)
        i += 1
    disegnaImmagineSuSchermo(screen, (0, 0))
    aggiornaSchermo()

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

global selsta
global selind
global spostapun
global selimp
global selezione
global spostaPunBattaglia
global selObbiettivo
global rumoreAttaccoSpada
global rumoreLancioFreccia
global rumoreAttaccoArco
global rumoreParata
global rumorecamminata
global rumorelevelup
global rumoreMorte
global suonoaperturacofanetti
global suonoaperturaporteForesta
global suonochiusuraporteForesta
global suonoaperturaporteCasa
global suonochiusuraporteCasa
global suonoRaccoltaEsca
global suonoRaccoltaMonete
global rumoreAcquisto
global rumoreCamminataColco
global rumoreScossaFreccia
global rumoreTempestaElettrica
global rumoreCuraRobo
global rumoreAntidoto
global rumoreAttPDifP
global rumoreAutoricarica
global rumoreRaffreddamento
global rumoreVelocizzaEfficienza
global suonoTeleColco
global suonoLancioOggetti
global suonoUsoPozione
global suonoUsoCaricabatterie
global suonoUsoMedicina
global suonoUsoBomba
global suonoUsoBombaVeleno
global suonoUsoEsca
global suonoUsoBombaAppiccicosa
global suonoUsoBombaPotenziata
global rumoreMovimentoNemiciPersonaggi
global rumoreAttaccoNemico
global rumoreLancioOggettoNemico
global rumoreMorteNemico
global suonoAperturaMappa
global rumoreScavare
global audioAmbienteSogno
global audioAmbienteCasaInterno
global audioAmbienteCasaEsterno
global audioAmbienteForesta
global audioAmbienteForestaFuoco
global canzoneSogno
global canzoneCasa
global canzoneForesta
def loadSounds():
    global selsta
    global selind
    global spostapun
    global selimp
    global selezione
    global spostaPunBattaglia
    global selObbiettivo
    global rumoreAttaccoSpada
    global rumoreLancioFreccia
    global rumoreAttaccoArco
    global rumoreParata
    global rumorecamminata
    global rumorelevelup
    global rumoreMorte
    global suonoaperturacofanetti
    global suonoaperturaporteForesta
    global suonochiusuraporteForesta
    global suonoaperturaporteCasa
    global suonochiusuraporteCasa
    global suonoRaccoltaEsca
    global suonoRaccoltaMonete
    global rumoreAcquisto
    global rumoreCamminataColco
    global rumoreScossaFreccia
    global rumoreTempestaElettrica
    global rumoreCuraRobo
    global rumoreAntidoto
    global rumoreAttPDifP
    global rumoreAutoricarica
    global rumoreRaffreddamento
    global rumoreVelocizzaEfficienza
    global suonoTeleColco
    global suonoLancioOggetti
    global suonoUsoPozione
    global suonoUsoCaricabatterie
    global suonoUsoMedicina
    global suonoUsoBomba
    global suonoUsoBombaVeleno
    global suonoUsoEsca
    global suonoUsoBombaAppiccicosa
    global suonoUsoBombaPotenziata
    global rumoreMovimentoNemiciPersonaggi
    global rumoreAttaccoNemico
    global rumoreLancioOggettoNemico
    global rumoreMorteNemico
    global suonoAperturaMappa
    global rumoreScavare
    global audioAmbienteSogno
    global audioAmbienteCasaInterno
    global audioAmbienteCasaEsterno
    global audioAmbienteForesta
    global audioAmbienteForestaFuoco
    global canzoneSogno
    global canzoneCasa
    global canzoneForesta

    # suoni puntatore
    selsta = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/SelSta.wav")
    selind = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/SelInd.wav")
    spostapun = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/SpostaPun.wav")
    selimp = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/SelImp.wav")
    selezione = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/Selezione.wav")
    spostaPunBattaglia = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/SpostaPunBattaglia.wav")
    selObbiettivo = caricaSuonoMostrandoAvanzamento("Audio/RumoriPuntatore/SelObbiettivo.wav")

    # suoni personaggio
    rumoreAttaccoSpada = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/AttaccoSpada.wav")
    rumoreLancioFreccia = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/LancioFreccia.wav")
    rumoreAttaccoArco = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/AttaccoArco.wav")
    rumoreParata = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/ParataConScudo.wav")
    rumorecamminata = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/Camminata.wav")
    rumorelevelup = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/Levelup.wav")
    rumoreMorte = caricaSuonoMostrandoAvanzamento("Audio/RumoriPersonaggio/Morte.wav")

    # suoni apertura-chiusura cofanetti-porte
    suonoaperturacofanetti = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/AperturaCofanetto.wav")
    suonoaperturaporteForesta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/AperturaPortaForesta.wav")
    suonochiusuraporteForesta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/ChiusuraPortaForesta.wav")
    suonoaperturaporteCasa = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/AperturaPortaCasa.wav")
    suonochiusuraporteCasa = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/ChiusuraPortaCasa.wav")

    # souno raccolta esca - monete
    suonoRaccoltaEsca = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/RaccoltaEsca.wav")
    suonoRaccoltaMonete = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/RaccoltaMonete.wav")
    rumoreAcquisto = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/Acquisto.wav")

    # suoni robo
    rumoreCamminataColco = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/Camminata.wav")
    rumoreScossaFreccia = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/ScossaFreccia.wav")
    rumoreTempestaElettrica = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/TempestaElettrica.wav")
    rumoreCuraRobo = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/Cura.wav")
    rumoreAntidoto = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/Antidoto.wav")
    rumoreAttPDifP = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/AttPDifP.wav")
    rumoreAutoricarica = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/Autoricarica.wav")
    rumoreRaffreddamento = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/Raffreddamento.wav")
    rumoreVelocizzaEfficienza = caricaSuonoMostrandoAvanzamento("Audio/RumoriColco/VelocizzaEfficienza.wav")

    # suono oggetti
    suonoTeleColco = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/TeleColco.wav")
    suonoLancioOggetti = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/LancioOggetti.wav")
    suonoUsoPozione = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/Pozione.wav")
    suonoUsoCaricabatterie = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/Caricabatterie.wav")
    suonoUsoMedicina = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/Medicina.wav")
    suonoUsoBomba = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/Bomba.wav")
    suonoUsoBombaVeleno = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/BombaVeleno.wav")
    suonoUsoEsca = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/Esca.wav")
    suonoUsoBombaAppiccicosa = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/BombaAppiccicosa.wav")
    suonoUsoBombaPotenziata = caricaSuonoMostrandoAvanzamento("Audio/RumoriOggetti/BombaPotenziata.wav")

    # suoni nemici
    rumoreMovimentoNemiciPersonaggi = caricaSuonoMostrandoAvanzamento("Audio/RumoriNemiciPersonaggi/MovimentoNemiciPersonaggi.wav")
    rumoreAttaccoNemico = caricaSuonoMostrandoAvanzamento("Audio/RumoriNemiciPersonaggi/AttaccoVicinoNemico.wav")
    rumoreLancioOggettoNemico = caricaSuonoMostrandoAvanzamento("Audio/RumoriNemiciPersonaggi/AttaccoLontanoNemico.wav")
    rumoreMorteNemico = caricaSuonoMostrandoAvanzamento("Audio/RumoriNemiciPersonaggi/MorteNemico.wav")

    # suono mappa
    suonoAperturaMappa = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/AperturaMappa.wav")

    # effetti speciali
    rumoreScavare = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/Scavare.wav")

    # suoni sottofondi ambientali
    audioAmbienteSogno = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/Sogno.wav")
    audioAmbienteCasaInterno = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/CasaInterno.wav")
    audioAmbienteCasaEsterno = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/CasaEsterno.wav")
    audioAmbienteForesta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/Foresta.wav")
    audioAmbienteForestaFuoco = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/ForestaFuoco.wav")

    # suoni canzoni
    canzoneSogno = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/01-Sogno.wav")
    canzoneCasa = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/02-Casa.wav")
    canzoneForesta = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/03-Foresta.wav")

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

numImgTotali = 1092
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
        mostraLogo()
        disegnaSchermataDiCaricamento()
        numImgCaricata = 0
        loadImgs(cambioRisoluzione=False)
        loadSounds()
else:
    erroreFileImpostazioni = True
if erroreFileImpostazioni:
    print ("Errore nella lettura del file di configurazione delle impostazioni")
    opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
    schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
    initVolumeSounds()
    mostraLogo()
    disegnaSchermataDiCaricamento()
    numImgCaricata = 0
    loadImgs(cambioRisoluzione=False)
    loadSounds()

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
