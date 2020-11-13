# -*- coding: utf-8 -*-

import os
import sys
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
pygame.init()

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

opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE
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
schermoIntero = True
print ("Modificato", gsx, gsy)

maxGsx = gsx
maxGsy = gsy

# dimensione personaggio
gpx = gsx // 32
gpy = gsy // 18

def quit():
    sys.exit()

def loadImage(path, aumentaRisoluzione, convert=False):
    if convert:
        img = pygame.image.load(gamePath + path).convert()
    else:
        img = pygame.image.load(gamePath + path)
    if aumentaRisoluzione:
        sizeX, sizeY = img.get_rect().size
        img = pygame.transform.scale(img, (sizeX * 4, sizeY * 4))
    return img

def loadSound(path):
    sound = pygame.mixer.Sound(gamePath + path)
    return sound

def loadFile(path, mode):
    file = open(gamePath + path, mode)
    return file

# nome-icona
pygame.display.set_caption("Gioco 2")
icona = loadImage("Immagini/Icona.png", False)
pygame.display.set_icon(icona)

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

linguaImpostata = "inglese"

# vettore che conterrà tutti i dati dei salvataggi
vetDatiSalvataggi = []

# dichiaro le variabili globali della funzione loadImgs
global puntatore
global puntatorevecchio
global puntatIn
global puntatOut
global puntatDif
global puntatAtt
global puntatArc
global puntatPor
global puntatCof
global puntatSpinta
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
global sfondostax3
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
global campoattaccabile1
global campoattaccabile2
global campoattaccabileRobo
global caselleattaccabiliRobo
global campoattaccabilemostro
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
global puntatoreorigi
global puntatoreorigivecchio
global avvelenatoo
global surriscaldatoo
global attaccopiuo
global difesapiuo
global velocitapiuo
global efficienzapiuo
global roboo
global perso
global persob
global puntatoreImpostazioniDestra
global puntatoreImpostazioniSinistra
global puntatoreImpostazioniDestraBloccato
global puntatoreImpostazioniSinistraBloccato
global tutorialTastieraInGioco
global tutorialTastieraInMenu
global tutorialMouse
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
global sconosciutoOggettoMenu
global sconosciutoOggettoIcoMenu
global imgMappa1
global imgMappa2
global imgMappa3
global imgMappa4
global imgMappa5
global imgMappa6
global imgMappa7
global imgMappa8
global imgMappa9
global imgMappa10
global imgMappa11
global imgMappa12
global imgMappa13
global imgMappa14
global imgOmbreggiaturaContorniMappaMenu
global dictionaryImgNemici
global imgDanneggiamentoCausaRallo
global imgDanneggiamentoCausaColco

def loadImgs():
    global puntatore
    global puntatorevecchio
    global puntatIn
    global puntatOut
    global puntatDif
    global puntatAtt
    global puntatArc
    global puntatPor
    global puntatCof
    global puntatSpinta
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
    global sfondostax3
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
    global campoattaccabile1
    global campoattaccabile2
    global campoattaccabileRobo
    global caselleattaccabiliRobo
    global campoattaccabilemostro
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
    global puntatoreorigi
    global puntatoreorigivecchio
    global avvelenatoo
    global surriscaldatoo
    global attaccopiuo
    global difesapiuo
    global velocitapiuo
    global efficienzapiuo
    global roboo
    global perso
    global persob
    global puntatoreImpostazioniDestra
    global puntatoreImpostazioniSinistra
    global puntatoreImpostazioniDestraBloccato
    global puntatoreImpostazioniSinistraBloccato
    global tutorialTastieraInGioco
    global tutorialTastieraInMenu
    global tutorialMouse
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
    global sconosciutoOggettoMenu
    global sconosciutoOggettoIcoMenu
    global imgMappa1
    global imgMappa2
    global imgMappa3
    global imgMappa4
    global imgMappa5
    global imgMappa6
    global imgMappa7
    global imgMappa8
    global imgMappa9
    global imgMappa10
    global imgMappa11
    global imgMappa12
    global imgMappa13
    global imgMappa14
    global imgOmbreggiaturaContorniMappaMenu
    global dictionaryImgNemici
    global imgDanneggiamentoCausaRallo
    global imgDanneggiamentoCausaColco

    # puntatore
    puntatoreorigi = loadImage("Immagini/Puntatori/Puntatore.png", True)
    puntatore = pygame.transform.smoothscale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatoreorigivecchio = loadImage("Immagini/Puntatori/Puntatorevecchio.png", True)
    puntatorevecchio = pygame.transform.smoothscale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    puntatIn = loadImage('Immagini/Puntatori/InquadraCVin.png', True)
    puntatIn = pygame.transform.smoothscale(puntatIn, (gpx, gpy))
    puntatOut = loadImage('Immagini/Puntatori/InquadraCVout.png', True)
    puntatOut = pygame.transform.smoothscale(puntatOut, (gpx, gpy))
    puntatDif = loadImage('Immagini/Oggetti/Difesa.png', True)
    puntatDif = pygame.transform.smoothscale(puntatDif, (gpx, gpy))
    puntatAtt = loadImage('Immagini/Oggetti/Attacco.png', True)
    puntatAtt = pygame.transform.smoothscale(puntatAtt, (gpx, gpy))
    puntatArc = loadImage('Immagini/Oggetti/AttaccoDistanza.png', True)
    puntatArc = pygame.transform.smoothscale(puntatArc, (gpx, gpy))
    puntatPor = loadImage('Immagini/Oggetti/ApriChiudiPorta.png', True)
    puntatPor = pygame.transform.smoothscale(puntatPor, (gpx, gpy))
    puntatCof = loadImage('Immagini/Oggetti/ApriCofanetto.png', True)
    puntatCof = pygame.transform.smoothscale(puntatCof, (gpx, gpy))
    puntatSpinta = loadImage('Immagini/Oggetti/SpingiColco.png', True)
    puntatSpinta = pygame.transform.smoothscale(puntatSpinta, (gpx, gpy))
    puntatBom = loadImage('Immagini/Oggetti/Oggetto6Ico.png', True)
    puntatBom = pygame.transform.smoothscale(puntatBom, (gpx, gpy))
    puntatBoV = loadImage('Immagini/Oggetti/Oggetto7Ico.png', True)
    puntatBoV = pygame.transform.smoothscale(puntatBoV, (gpx, gpy))
    puntatEsc = loadImage('Immagini/Oggetti/Oggetto8Ico.png', True)
    puntatEsc = pygame.transform.smoothscale(puntatEsc, (gpx, gpy))
    puntatBoA = loadImage('Immagini/Oggetti/Oggetto9Ico.png', True)
    puntatBoA = pygame.transform.smoothscale(puntatBoA, (gpx, gpy))
    puntatBoP = loadImage('Immagini/Oggetti/Oggetto10Ico.png', True)
    puntatBoP = pygame.transform.smoothscale(puntatBoP, (gpx, gpy))
    scorriSu = loadImage("Immagini/Puntatori/ScorriOggettiSu.png", True)
    scorriSu = pygame.transform.smoothscale(scorriSu, (gpx, gpy))
    scorriGiu = loadImage("Immagini/Puntatori/ScorriOggettiGiu.png", True)
    scorriGiu = pygame.transform.smoothscale(scorriGiu, (gpx, gpy))
    puntatDialoghi = loadImage('Immagini/Oggetti/IcoDialogo.png', True)
    puntatDialoghi = pygame.transform.smoothscale(puntatDialoghi, (gpx, gpy))
    puntatoreInquadraNemici = loadImage("Immagini/Puntatori/InquadraNemicoSelezionato.png", True)
    puntatoreInquadraNemici = pygame.transform.smoothscale(puntatoreInquadraNemici, (gpx, gpy))
    puntatoreImpostazioniDestra = loadImage("Immagini/Puntatori/ScorriImpostazioniDestra.png", True)
    puntatoreImpostazioniDestra = pygame.transform.smoothscale(puntatoreImpostazioniDestra, (gpx, gpy))
    puntatoreImpostazioniSinistra = loadImage("Immagini/Puntatori/ScorriImpostazioniSinistra.png", True)
    puntatoreImpostazioniSinistra = pygame.transform.smoothscale(puntatoreImpostazioniSinistra, (gpx, gpy))
    puntatoreImpostazioniDestraBloccato = loadImage("Immagini/Puntatori/ScorriImpostazioniDestraBloccato.png", True)
    puntatoreImpostazioniDestraBloccato = pygame.transform.smoothscale(puntatoreImpostazioniDestraBloccato, (gpx, gpy))
    puntatoreImpostazioniSinistraBloccato = loadImage("Immagini/Puntatori/ScorriImpostazioniSinistraBloccato.png", True)
    puntatoreImpostazioniSinistraBloccato = pygame.transform.smoothscale(puntatoreImpostazioniSinistraBloccato, (gpx, gpy))

    # immagini personaggio
    persw = loadImage('Immagini/Personaggi/Sara/Personaggio4.png', True)
    persw = pygame.transform.smoothscale(persw, (gpx, gpy))
    perswb = loadImage('Immagini/Personaggi/Sara/Personaggio4b.png', True)
    perswb = pygame.transform.smoothscale(perswb, (gpx, gpy))
    persa = loadImage('Immagini/Personaggi/Sara/Personaggio3.png', True)
    persa = pygame.transform.smoothscale(persa, (gpx, gpy))
    persab = loadImage('Immagini/Personaggi/Sara/Personaggio3b.png', True)
    persab = pygame.transform.smoothscale(persab, (gpx, gpy))
    perso = loadImage('Immagini/Personaggi/Sara/Personaggio1.png', True)
    perss = pygame.transform.smoothscale(perso, (gpx, gpy))
    persob = loadImage('Immagini/Personaggi/Sara/Personaggio1b.png', True)
    perssb = pygame.transform.smoothscale(persob, (gpx, gpy))
    persd = loadImage('Immagini/Personaggi/Sara/Personaggio2.png', True)
    persd = pygame.transform.smoothscale(persd, (gpx, gpy))
    persdb = loadImage('Immagini/Personaggi/Sara/Personaggio2b.png', True)
    persdb = pygame.transform.smoothscale(persdb, (gpx, gpy))
    perssm = loadImage('Immagini/Personaggi/Sara/Personaggio1mov.png', True)
    perssm = pygame.transform.smoothscale(perssm, (gpx, gpy))
    perssmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio1movb1.png', True)
    perssmb1 = pygame.transform.smoothscale(perssmb1, (gpx, gpy))
    perssmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio1movb2.png', True)
    perssmb2 = pygame.transform.smoothscale(perssmb2, (gpx, gpy))
    persdm = loadImage('Immagini/Personaggi/Sara/Personaggio2mov.png', True)
    persdm = pygame.transform.smoothscale(persdm, (gpx, gpy))
    persdmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio2movb1.png', True)
    persdmb1 = pygame.transform.smoothscale(persdmb1, (gpx, gpy))
    persdmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio2movb2.png', True)
    persdmb2 = pygame.transform.smoothscale(persdmb2, (gpx, gpy))
    persam = loadImage('Immagini/Personaggi/Sara/Personaggio3mov.png', True)
    persam = pygame.transform.smoothscale(persam, (gpx, gpy))
    persamb1 = loadImage('Immagini/Personaggi/Sara/Personaggio3movb1.png', True)
    persamb1 = pygame.transform.smoothscale(persamb1, (gpx, gpy))
    persamb2 = loadImage('Immagini/Personaggi/Sara/Personaggio3movb2.png', True)
    persamb2 = pygame.transform.smoothscale(persamb2, (gpx, gpy))
    perswm = loadImage('Immagini/Personaggi/Sara/Personaggio4mov.png', True)
    perswm = pygame.transform.smoothscale(perswm, (gpx, gpy))
    perswmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio4movb1.png', True)
    perswmb1 = pygame.transform.smoothscale(perswmb1, (gpx, gpy))
    perswmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio4movb2.png', True)
    perswmb2 = pygame.transform.smoothscale(perswmb2, (gpx, gpy))
    perswmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio4movbAttacco.png', True)
    perswmbAttacco = pygame.transform.smoothscale(perswmbAttacco, (gpx, gpy))
    persambAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio3movbAttacco.png', True)
    persambAttacco = pygame.transform.smoothscale(persambAttacco, (gpx, gpy))
    perssmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio1movbAttacco.png', True)
    perssmbAttacco = pygame.transform.smoothscale(perssmbAttacco, (gpx, gpy))
    persdmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio2movbAttacco.png', True)
    persdmbAttacco = pygame.transform.smoothscale(persdmbAttacco, (gpx, gpy))
    persmbDifesa = loadImage('Immagini/Personaggi/Sara/PersonaggiomovbDifesa.png', True)
    persmbDifesa = pygame.transform.smoothscale(persmbDifesa, (gpx, gpy))
    persAvvele = loadImage('Immagini/Personaggi/Sara/PersonaggioAvvelenato.png', True)
    persAvvele = pygame.transform.smoothscale(persAvvele, (gpx, gpy))

    # immagini robot
    robow = loadImage('Immagini/Personaggi/Colco/Robot4.png', True)
    robow = pygame.transform.smoothscale(robow, (gpx, gpy))
    roboa = loadImage('Immagini/Personaggi/Colco/Robot3.png', True)
    roboa = pygame.transform.smoothscale(roboa, (gpx, gpy))
    roboo = loadImage('Immagini/Personaggi/Colco/Robot1.png', True)
    robos = pygame.transform.smoothscale(roboo, (gpx, gpy))
    robod = loadImage('Immagini/Personaggi/Colco/Robot2.png', True)
    robod = pygame.transform.smoothscale(robod, (gpx, gpy))
    robomo = loadImage('Immagini/Personaggi/Colco/Robot0.png', True)
    robomo = pygame.transform.smoothscale(robomo, (gpx, gpy))
    robodp = loadImage('Immagini/Personaggi/Colco/Robot2p.png', True)
    robodp = pygame.transform.smoothscale(robodp, (gpx, gpy))
    roboap = loadImage('Immagini/Personaggi/Colco/Robot3p.png', True)
    roboap = pygame.transform.smoothscale(roboap, (gpx, gpy))
    armrobmo = loadImage('Immagini/EquipRobo/Batteria00.png', True)
    armrobmo = pygame.transform.smoothscale(armrobmo, (gpx, gpy))
    roboSurrisc = loadImage('Immagini/Personaggi/Colco/RobotSurriscaldato.png', True)
    roboSurrisc = pygame.transform.smoothscale(roboSurrisc, (gpx, gpy))

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = loadImage("Immagini/Nemici/DannoRallo.png", True)
    imgDanneggiamentoCausaRallo = pygame.transform.smoothscale(imgDanneggiamentoCausaRallo, (gpx, gpy))
    imgDanneggiamentoCausaColco = loadImage("Immagini/Nemici/DannoColco.png", True)
    imgDanneggiamentoCausaColco = pygame.transform.smoothscale(imgDanneggiamentoCausaColco, (gpx, gpy))

    # img menu mercante
    mercanteMenu = loadImage('Immagini/Personaggi/Mercante/MercanteDialogo.png', True)
    mercanteMenu = pygame.transform.smoothscale(mercanteMenu, (gpx * 12, gpy * 9))
    scorriSuGiu = loadImage('Immagini/Puntatori/ScorriSuGiu.png', True)
    scorriSuGiu = pygame.transform.smoothscale(scorriSuGiu, (gpx, gpy))
    scorriSuGiuBloccato = loadImage('Immagini/Puntatori/ScorriSuGiuBloccato.png', True)
    scorriSuGiuBloccato = pygame.transform.smoothscale(scorriSuGiuBloccato, (gpx, gpy))
    scorriSuGiuBloccatoGiu = loadImage('Immagini/Puntatori/ScorriSuGiuBloccatoGiu.png', True)
    scorriSuGiuBloccatoGiu = pygame.transform.smoothscale(scorriSuGiuBloccatoGiu, (gpx, gpy))
    scorriSuGiuBloccatoSu = loadImage('Immagini/Puntatori/ScorriSuGiuBloccatoSu.png', True)
    scorriSuGiuBloccatoSu = pygame.transform.smoothscale(scorriSuGiuBloccatoSu, (gpx, gpy))
    sfondoDialogoMercante = loadImage('Immagini/DecorazioniMenu/SfondoDialogoMercante.png', True)
    sfondoDialogoMercante = pygame.transform.smoothscale(sfondoDialogoMercante, (int(gpx * 9.5), int(gpy * 4.5)))
    faretra1Menu = loadImage('Immagini/Oggetti/Faretra1Menu.png', False)
    faretra1Menu = pygame.transform.smoothscale(faretra1Menu, (gpx * 8, gpy * 8))
    faretra2Menu = loadImage('Immagini/Oggetti/Faretra2Menu.png', False)
    faretra2Menu = pygame.transform.smoothscale(faretra2Menu, (gpx * 8, gpy * 8))
    faretra3Menu = loadImage('Immagini/Oggetti/Faretra3Menu.png', False)
    faretra3Menu = pygame.transform.smoothscale(faretra3Menu, (gpx * 8, gpy * 8))
    frecciaMenu = loadImage('Immagini/Oggetti/FrecciaMenu.png', False)
    frecciaMenu = pygame.transform.smoothscale(frecciaMenu, (gpx * 8, gpy * 8))

    # sfondi
    sfondostax3 = loadImage('Immagini/Status/Sfondostax3.png', True)
    sfondostax3 = pygame.transform.smoothscale(sfondostax3, (gpx * 4, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoRallo.png', True)
    sfondoRallo = pygame.transform.smoothscale(sfondosta, (gpx * 6, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoColco.png', True)
    sfondoColco = pygame.transform.smoothscale(sfondosta, (gpx * 4, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoNemici.png', True)
    sfondoMostro = pygame.transform.smoothscale(sfondosta, (gpx * 3, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoEsche.png', True)
    sfondoEsche = pygame.transform.smoothscale(sfondosta, (gpx, gpy))
    sfondoStartBattaglia = loadImage('Immagini/Oggetti/SfondoStartBattaglia.png', True)
    sfondoStartBattaglia = pygame.transform.smoothscale(sfondoStartBattaglia, (gpx * 7, gpy * 10))
    sfondoTriangolinoAltoDestra = loadImage('Immagini/DecorazioniMenu/TriangoloAltoDestra.png', True)
    sfondoTriangolinoAltoDestra = pygame.transform.smoothscale(sfondoTriangolinoAltoDestra, (gpx, gpy))
    sfondoTriangolinoAltoSinistra = loadImage('Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', True)
    sfondoTriangolinoAltoSinistra = pygame.transform.smoothscale(sfondoTriangolinoAltoSinistra, (gpx, gpy))
    sfondoTriangolinoBassoDestra = loadImage('Immagini/DecorazioniMenu/TriangoloBassoDestra.png', True)
    sfondoTriangolinoBassoDestra = pygame.transform.smoothscale(sfondoTriangolinoBassoDestra, (gpx, gpy))
    sfondoTriangolinoBassoSinistra = loadImage('Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', True)
    sfondoTriangolinoBassoSinistra = pygame.transform.smoothscale(sfondoTriangolinoBassoSinistra, (gpx, gpy))

    # status
    appiccicosoo = loadImage('Immagini/Status/Appiccicoso.png', True)
    appiccicoso = pygame.transform.smoothscale(appiccicosoo, (gpx * 3 // 4, gpy * 3 // 4))
    avvelenatoo = loadImage('Immagini/Status/Avvelenato.png', True)
    avvelenato = pygame.transform.smoothscale(avvelenatoo, (gpx * 3 // 4, gpy * 3 // 4))
    surriscaldatoo = loadImage('Immagini/Status/Surriscaldato.png', True)
    surriscaldato = pygame.transform.smoothscale(surriscaldatoo, (gpx * 3 // 4, gpy * 3 // 4))
    attaccopiuo = loadImage('Immagini/Status/Attaccopiu.png', True)
    attaccopiu = pygame.transform.smoothscale(attaccopiuo, (gpx * 3 // 4, gpy * 3 // 4))
    difesapiuo = loadImage('Immagini/Status/Difesapiu.png', True)
    difesapiu = pygame.transform.smoothscale(difesapiuo, (gpx * 3 // 4, gpy * 3 // 4))
    velocitapiuo = loadImage('Immagini/Status/Velocitapiu.png', True)
    velocitapiu = pygame.transform.smoothscale(velocitapiuo, (gpx * 3 // 4, gpy * 3 // 4))
    efficienzapiuo = loadImage('Immagini/Status/Efficienzapiu.png', True)
    efficienzapiu = pygame.transform.smoothscale(efficienzapiuo, (gpx * 3 // 4, gpy * 3 // 4))
    imgNumFrecce = loadImage('Immagini/Status/NumFrecce.png', True)
    imgNumFrecce = pygame.transform.smoothscale(imgNumFrecce, (gpx * 3 // 4, gpy * 3 // 4))

    # menu alto destra
    sfochiaveocchio = loadImage("Immagini/Oggetti/SfondoOcchioChiave.png", True)
    sfochiaveocchio = pygame.transform.smoothscale(sfochiaveocchio, (gpx * 5, gpy * 2))
    occhioape = loadImage('Immagini/Status/OcchioAperto.png', True)
    occhioape = pygame.transform.smoothscale(occhioape, (gpx, gpy))
    occhiochiu = loadImage('Immagini/Status/OcchioChiuso.png', True)
    occhiochiu = pygame.transform.smoothscale(occhiochiu, (gpx, gpy))
    chiaveroboacc = loadImage('Immagini/Oggetti/ChiaveColcoAcc.png', True)
    chiaveroboacc = pygame.transform.smoothscale(chiaveroboacc, (gpx * 2, gpy * 2))
    chiaverobospe = loadImage('Immagini/Oggetti/ChiaveColcoSpe.png', True)
    chiaverobospe = pygame.transform.smoothscale(chiaverobospe, (gpx * 2, gpy * 2))

    # oggetti sulla schermata
    esche = loadImage("Immagini/Oggetti/Oggetto8Ico.png", True)
    esche = pygame.transform.smoothscale(esche, (gpx, gpy))
    sacchettoDenaroStart = loadImage('Immagini/Oggetti/SacchettoDenaroSinistra.png', False)
    sacchettoDenaroStart = pygame.transform.smoothscale(sacchettoDenaroStart, (gpx * 4, gpy * 4))
    sacchettoDenaroMercante = loadImage('Immagini/Oggetti/SacchettoDenaroDestra.png', False)
    sacchettoDenaroMercante = pygame.transform.smoothscale(sacchettoDenaroMercante, (gpx * 4, gpy * 4))
    faretraFrecceStart0 = loadImage('Immagini/EquipSara/Faretre/Faretra0Menu.png', False)
    faretraFrecceStart0 = pygame.transform.smoothscale(faretraFrecceStart0, (gpx * 4, gpy * 4))
    faretraFrecceStart1 = loadImage('Immagini/EquipSara/Faretre/Faretra1Menu.png', False)
    faretraFrecceStart1 = pygame.transform.smoothscale(faretraFrecceStart1, (gpx * 4, gpy * 4))
    faretraFrecceStart2 = loadImage('Immagini/EquipSara/Faretre/Faretra2Menu.png', False)
    faretraFrecceStart2 = pygame.transform.smoothscale(faretraFrecceStart2, (gpx * 4, gpy * 4))
    faretraFrecceStart3 = loadImage('Immagini/EquipSara/Faretre/Faretra3Menu.png', False)
    faretraFrecceStart3 = pygame.transform.smoothscale(faretraFrecceStart3, (gpx * 4, gpy * 4))
    sacchettoDenaroo = loadImage('Immagini/Oggetti/SacchettoDenaroIco.png', True)
    sacchettoDenaro = pygame.transform.smoothscale(sacchettoDenaroo, (gpx, gpy))
    imgFrecciaLanciata = loadImage('Immagini/Oggetti/Freccia.png', True)
    imgFrecciaLanciata = pygame.transform.smoothscale(imgFrecciaLanciata, (gpx, gpy))

    # cofanetti
    cofaniaper = loadImage("Immagini/Oggetti/CofanettoAperto.png", True)
    cofaniaper = pygame.transform.smoothscale(cofaniaper, (gpx, gpy))
    cofanichiu = loadImage("Immagini/Oggetti/CofanettoChiuso.png", True)
    cofanichiu = pygame.transform.smoothscale(cofanichiu, (gpx, gpy))
    sfocontcof = loadImage("Immagini/Oggetti/SfondoContenutoCofanetto.png", True)
    sfocontcof = pygame.transform.smoothscale(sfocontcof, (gpx * 16, gpy * 3))

    # immagini salvataggi
    s1 = loadImage('Immagini/Salvataggi/S1.png', True)
    s1 = pygame.transform.smoothscale(s1, (gpx * 3, gpy * 3))
    s2 = loadImage('Immagini/Salvataggi/S2.png', True)
    s2 = pygame.transform.smoothscale(s2, (gpx * 3, gpy * 3))
    s3 = loadImage('Immagini/Salvataggi/S3.png', True)
    s3 = pygame.transform.smoothscale(s3, (gpx * 3, gpy * 3))

    # caselle attaccabili
    campoattaccabile1 = loadImage('Immagini/Campiattaccabili/Campoattaccabile1.png', True)
    campoattaccabile1 = pygame.transform.smoothscale(campoattaccabile1, (gpx * 3, gpy * 3))
    campoattaccabile2 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png', True)
    campoattaccabileRobo = loadImage('Immagini/Campiattaccabili/Campoattaccabile3.png', True)
    campoattaccabileRobo = pygame.transform.smoothscale(campoattaccabileRobo, (gpx * 13, gpy * 13))
    caselleattaccabiliRobo = loadImage('Immagini/Campiattaccabili/CaselleattaccabiliRobo.png', True)
    caselleattaccabiliRobo = pygame.transform.smoothscale(caselleattaccabiliRobo, (gpx, gpy))
    campoattaccabilemostro = loadImage('Immagini/Campiattaccabili/Campoattaccabilemostro.png', True)
    caselleattaccabilimostro = loadImage('Immagini/Campiattaccabili/Caselleattaccabilimostro.png', True)
    caselleattaccabilimostro = pygame.transform.smoothscale(caselleattaccabilimostro, (gpx, gpy))
    caselleattaccabili = loadImage('Immagini/Campiattaccabili/Caselleattaccabili.png', True)
    caselleattaccabili = pygame.transform.smoothscale(caselleattaccabili, (gpx, gpy))

    # aumento livello
    saliliv = loadImage('Immagini/Levelup/Saliliv.png', True)
    saliliv = pygame.transform.smoothscale(saliliv, (gpx, gpy))
    saliliv1 = loadImage('Immagini/Levelup/Saliliv1.png', True)
    saliliv1 = pygame.transform.smoothscale(saliliv1, (gpx, gpy))
    saliliv2 = loadImage('Immagini/Levelup/Saliliv2.png', True)
    saliliv2 = pygame.transform.smoothscale(saliliv2, (gpx, gpy))

    # img equipaggiamento, condizioni, tecniche, oggetti
    vetImgSpadeMenu = []
    vetImgArchiMenu = []
    vetImgArmatureMenu = []
    vetImgScudiMenu = []
    vetImgGuantiMenu = []
    vetImgCollaneMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadeMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipSara/Spade/Spada%iMenu.png" % contatoreGlobale, False), (int(gpx * 2), int(gpy * 2))))
        vetImgArchiMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipSara/Archi/Arco%iMenu.png" % contatoreGlobale, False), (int(gpx * 2), int(gpy * 2))))
        vetImgArmatureMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipSara/Armature/Armatura%iMenu.png" % contatoreGlobale, False), (int(gpx * 2), int(gpy * 2))))
        vetImgScudiMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipSara/Scudi/Scudo%iMenu.png" % contatoreGlobale, False), (int(gpx * 2), int(gpy * 2))))
        vetImgGuantiMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipSara/Guanti/Guanti%iMenu.png" % contatoreGlobale, False), (int(gpx * 2), int(gpy * 2))))
        vetImgCollaneMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipSara/Collane/Collana%iMenu.png" % contatoreGlobale, False), (int(gpx * 2), int(gpy * 2))))
        contatoreGlobale += 1
    vetImgCondizioniMenu = [0]
    contatoreGlobale = 1
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(pygame.transform.smoothscale(loadImage("Immagini/GrafCondizioni/Condizione%i.png" % contatoreGlobale, False), (gpx * 12, gpy * 9)))
        contatoreGlobale += 1
    vetImgTecnicheMenu = [0]
    contatoreGlobale = 1
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(pygame.transform.smoothscale(loadImage("Immagini/GrafTecniche/Tecnica%i.png" % contatoreGlobale, False), (gpx * 12, gpy * 9)))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, True), (gpx * 5, gpy * 5)))
        vetIcoBatterieMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale, False), (gpx * 2, gpy * 2)))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(pygame.transform.smoothscale(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, False), (gpx * 10, gpy * 10)))
        vetImgOggettiMercante.append(pygame.transform.smoothscale(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, False), (gpx * 8, gpy * 8)))
        vetImgOggettiStart.append(pygame.transform.smoothscale(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, False), (gpx * 4, gpy * 4)))
        vetIcoOggettiMenu.append(pygame.transform.smoothscale(loadImage("Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale, True), (gpx, gpy)))
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
        vetImgSpadePixellate.append(loadImage("Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale, True))
        vetImgArchiPixellate.append(loadImage("Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale, True))
        vetImgArmaturePixellate.append(loadImage("Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale, True))
        vetImgScudiPixellate.append(loadImage("Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale, True))
        vetImgGuantiPixellate.append(loadImage("Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale, True))
        vetImgCollanePixellate.append(loadImage("Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale, True))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = loadImage('Immagini/AnimazioniOggetti/Bomba.png', True)
    imgAnimaBomba = pygame.transform.smoothscale(imgAnimaBomba, (gpx * 3, gpy * 3))
    imgAnimaBombaVeleno = loadImage('Immagini/AnimazioniOggetti/BombaVeleno.png', True)
    imgAnimaBombaVeleno = pygame.transform.smoothscale(imgAnimaBombaVeleno, (gpx, gpy))
    imgAnimaBombaAppiccicosa = loadImage('Immagini/AnimazioniOggetti/BombaAppiccicosa.png', True)
    imgAnimaBombaAppiccicosa = pygame.transform.smoothscale(imgAnimaBombaAppiccicosa, (gpx, gpy))
    imgAnimaBombaPotenziata = loadImage('Immagini/AnimazioniOggetti/BombaPotenziata.png', True)
    imgAnimaBombaPotenziata = pygame.transform.smoothscale(imgAnimaBombaPotenziata, (gpx * 5, gpy * 5))
    imgAnimaPozione1 = loadImage('Immagini/AnimazioniOggetti/Pozione1.png', True)
    imgAnimaPozione1 = pygame.transform.smoothscale(imgAnimaPozione1, (gpx, gpy))
    imgAnimaPozione2 = loadImage('Immagini/AnimazioniOggetti/Pozione2.png', True)
    imgAnimaPozione2 = pygame.transform.smoothscale(imgAnimaPozione2, (gpx, gpy))
    imgAnimaMedicina1 = loadImage('Immagini/AnimazioniOggetti/Medicina1.png', True)
    imgAnimaMedicina1 = pygame.transform.smoothscale(imgAnimaMedicina1, (gpx, gpy))
    imgAnimaMedicina2 = loadImage('Immagini/AnimazioniOggetti/Medicina2.png', True)
    imgAnimaMedicina2 = pygame.transform.smoothscale(imgAnimaMedicina2, (gpx, gpy))
    imgAnimaCaricabatterie = loadImage('Immagini/AnimazioniOggetti/Caricabatterie.png', True)
    imgAnimaCaricabatterie = pygame.transform.smoothscale(imgAnimaCaricabatterie, (gpx, gpy))

    # img animazioni tecniche
    imgDanneggiamentoColco = loadImage('Immagini/AnimazioniTecniche/Danneggiamento.png', True)
    imgDanneggiamentoColco = pygame.transform.smoothscale(imgDanneggiamentoColco, (gpx, gpy))
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = loadImage("Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale, True)
            img1 = pygame.transform.smoothscale(img1, (gpx, gpy * 2))
            img2 = pygame.transform.smoothscale(img2, (gpx, gpy * 2))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale, True)
            img1 = pygame.transform.smoothscale(img1, (gpx * 2, gpy))
            img2 = pygame.transform.smoothscale(img2, (gpx * 2, gpy))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale, True)
            img1 = pygame.transform.smoothscale(img1, (gpx, gpy * 2))
            img2 = pygame.transform.smoothscale(img2, (gpx, gpy * 2))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale, True)
            img1 = pygame.transform.smoothscale(img1, (gpx * 2, gpy))
            img2 = pygame.transform.smoothscale(img2, (gpx * 2, gpy))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = loadImage("Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale, True)
            img1 = pygame.transform.smoothscale(img1, (gpx, gpy))
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = loadImage("Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale, True)
            img2 = loadImage("Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale, True)
            img1 = pygame.transform.smoothscale(img1, (gpx * 13, gpy * 13))
            img2 = pygame.transform.smoothscale(img2, (gpx * 13, gpy * 13))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata.png', True)
    imgFrecciaEletttricaLanciata = pygame.transform.smoothscale(imgFrecciaEletttricaLanciata, (gpx, gpy))
    imgFrecciaEletttricaLanciataP = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata+.png', True)
    imgFrecciaEletttricaLanciataP = pygame.transform.smoothscale(imgFrecciaEletttricaLanciataP, (gpx, gpy))
    imgFrecciaEletttricaLanciataPP = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata++.png', True)
    imgFrecciaEletttricaLanciataPP = pygame.transform.smoothscale(imgFrecciaEletttricaLanciataPP, (gpx, gpy))

    # img sfondi dialoghi
    sfondoDialoghi = loadImage('Immagini/Dialoghi/SfondoSotto.png', True)
    sfondoDialoghi = pygame.transform.smoothscale(sfondoDialoghi, (gsx, gsy // 3))

    # img tutorial
    tutorialTastieraInGioco = loadImage('Immagini/Tutorial/TastieraInGioco.png', True)
    tutorialTastieraInGioco = pygame.transform.smoothscale(tutorialTastieraInGioco, (gsx // 32 * 7, gsy // 18 * 11))
    tutorialTastieraInMenu = loadImage('Immagini/Tutorial/TastieraInMenu.png', True)
    tutorialTastieraInMenu = pygame.transform.smoothscale(tutorialTastieraInMenu, (gsx // 32 * 7, gsy // 18 * 11))
    tutorialMouse = loadImage('Immagini/Tutorial/Mouse.png', True)
    tutorialMouse = pygame.transform.smoothscale(tutorialMouse, (gsx // 32 * 7, gsy // 18 * 11))

    # img grafiche / dialoghi
    persGrafMenu = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/LucaGrafMenu.png', False)
    persGrafMenu = pygame.transform.smoothscale(persGrafMenu, (gpx * 18, gpy * 18))
    saraGrafMenu = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/SaraGrafMenu.png', False)
    saraGrafMenu = pygame.transform.smoothscale(saraGrafMenu, (gpx * 10, gpy * 10))
    fraMaggioreGrafMenu = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', False)
    fraMaggioreGrafMenu = pygame.transform.smoothscale(fraMaggioreGrafMenu, (gpx * 10, gpy * 10))
    robograf0 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf0.png', False)
    robograf0 = pygame.transform.smoothscale(robograf0, (gpx * 18, gpy * 18))
    robograf1o = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', False)
    robograf1 = pygame.transform.smoothscale(robograf1o, (gpx * 18, gpy * 18))
    robograf1b = pygame.transform.smoothscale(robograf1o, (gpx * 10, gpy * 10))
    robograf2o = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', False)
    robograf2 = pygame.transform.smoothscale(robograf2o, (gpx * 18, gpy * 18))
    robograf2b = pygame.transform.smoothscale(robograf2o, (gpx * 10, gpy * 10))
    robograf3 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf3.png', False)
    robograf3 = pygame.transform.smoothscale(robograf3, (gpx * 18, gpy * 18))
    robograf4 = loadImage('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', False)
    robograf4 = pygame.transform.smoothscale(robograf4, (gpx * 18, gpy * 18))
    imgDialogoFraMaggiore = loadImage('Immagini/Dialoghi/FratelloMaggioreDialogo.png', False)
    imgDialogoSara = loadImage('Immagini/Dialoghi/SaraDialogo.png', False)
    imgFraMaggioreMenuOggetti = loadImage('Immagini/DecorazioniMenu/FratelloMaggioreMenu.png', True)
    imgFraMaggioreMenuOggetti = pygame.transform.smoothscale(imgFraMaggioreMenuOggetti, (gpx * 3, gpy * 3))
    imgSaraMenuOggetti = loadImage('Immagini/DecorazioniMenu/SaraMenu.png', True)
    imgSaraMenuOggetti = pygame.transform.smoothscale(imgSaraMenuOggetti, (gpx * 3, gpy * 3))

    # indicatori vita
    indvita = loadImage('Immagini/Barrevita/Indvita.png', True)
    fineindvita = loadImage('Immagini/Barrevita/FineIndVita.png', True)
    vitanemico00 = loadImage('Immagini/Barrevita/Vitanemico00.png', True)
    vitanemico0 = loadImage('Immagini/Barrevita/Vitanemico0.png', True)
    vitanemico1 = loadImage('Immagini/Barrevita/Vitanemico1.png', True)
    vitanemico2 = loadImage('Immagini/Barrevita/Vitanemico2.png', True)
    vitanemico3 = loadImage('Immagini/Barrevita/Vitanemico3.png', True)
    vitanemico4 = loadImage('Immagini/Barrevita/Vitanemico4.png', True)
    vitanemico5 = loadImage('Immagini/Barrevita/Vitanemico5.png', True)
    vitanemico6 = loadImage('Immagini/Barrevita/Vitanemico6.png', True)
    vitanemico7 = loadImage('Immagini/Barrevita/Vitanemico7.png', True)
    vitanemico8 = loadImage('Immagini/Barrevita/Vitanemico8.png', True)
    vitanemico9 = loadImage('Immagini/Barrevita/Vitanemico9.png', True)
    vitapersonaggio = loadImage('Immagini/Barrevita/Vitapersonaggio.png', True)
    vitarobo = loadImage('Immagini/Barrevita/Vitarobo.png', True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = loadImage("Immagini/EquipSara/SfondoOggetto.png", False)
    sfondoOggettoMenu = pygame.transform.smoothscale(sfondoOggettoMenu, (int(gpx * 2), int(gpy * 2)))
    sconosciutoEquipMenu = loadImage("Immagini/Oggetti/SconosciutoEquip.png", False)
    sconosciutoEquipMenu = pygame.transform.smoothscale(sconosciutoEquipMenu, (int(gpx * 2), int(gpy * 2)))
    sconosciutoOggettoMenu = loadImage("Immagini/Oggetti/Sconosciuto.png", False)
    sconosciutoOggettoIcoMenu = loadImage("Immagini/Oggetti/SconosciutoIco.png", False)

    # img mappe
    imgMappa1 = loadImage("Immagini/DecorazioniMenu/MappaMenu1.png", False)
    imgMappa2 = loadImage("Immagini/DecorazioniMenu/MappaMenu2.png", False)
    imgMappa3 = loadImage("Immagini/DecorazioniMenu/MappaMenu3.png", False)
    imgMappa4 = loadImage("Immagini/DecorazioniMenu/MappaMenu4.png", False)
    imgMappa5 = loadImage("Immagini/DecorazioniMenu/MappaMenu5.png", False)
    imgMappa6 = loadImage("Immagini/DecorazioniMenu/MappaMenu6.png", False)
    imgMappa7 = loadImage("Immagini/DecorazioniMenu/MappaMenu7.png", False)
    imgMappa8 = loadImage("Immagini/DecorazioniMenu/MappaMenu8.png", False)
    imgMappa9 = loadImage("Immagini/DecorazioniMenu/MappaMenu9.png", False)
    imgMappa10 = loadImage("Immagini/DecorazioniMenu/MappaMenu10.png", False)
    imgMappa11 = loadImage("Immagini/DecorazioniMenu/MappaMenu11.png", False)
    imgMappa12 = loadImage("Immagini/DecorazioniMenu/MappaMenu12.png", False)
    imgMappa13 = loadImage("Immagini/DecorazioniMenu/MappaMenu13.png", False)
    imgMappa14 = loadImage("Immagini/DecorazioniMenu/MappaMenu14.png", False)
    imgOmbreggiaturaContorniMappaMenu = loadImage("Immagini/DecorazioniMenu/OmbreggiaturaContorniMappaMenu.png", False)
    imgOmbreggiaturaContorniMappaMenu = pygame.transform.smoothscale(imgOmbreggiaturaContorniMappaMenu, (gsx, gsy))

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "Cinghiale", "LupoGrigio", "LupoNero", "LupoBianco", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png", True)
        imgW = pygame.transform.smoothscale(imgW, (gpx, gpy))
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png", True)
        imgA = pygame.transform.smoothscale(imgA, (gpx, gpy))
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png", True)
        imgS = pygame.transform.smoothscale(imgS, (gpx, gpy))
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png", True)
        imgD = pygame.transform.smoothscale(imgD, (gpx, gpy))
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png", True)
        imgWMov1 = pygame.transform.smoothscale(imgWMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png", True)
        imgWMov2 = pygame.transform.smoothscale(imgWMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png", True)
        imgAMov1 = pygame.transform.smoothscale(imgAMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png", True)
        imgAMov2 = pygame.transform.smoothscale(imgAMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png", True)
        imgSMov1 = pygame.transform.smoothscale(imgSMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png", True)
        imgSMov2 = pygame.transform.smoothscale(imgSMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png", True)
        imgDMov1 = pygame.transform.smoothscale(imgDMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png", True)
        imgDMov2 = pygame.transform.smoothscale(imgDMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = loadImage("Immagini/Nemici/NemicoAvvelenato.png", True)
        imgAvvelenamento = pygame.transform.smoothscale(imgAvvelenamento, (gpx, gpy))
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = loadImage("Immagini/Nemici/NemicoAppiccicato.png", True)
        imgAppiccicato = pygame.transform.smoothscale(imgAppiccicato, (gpx, gpy))
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png", True)
        imgAttaccoW = pygame.transform.smoothscale(imgAttaccoW, (gpx, gpy * 2))
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png", True)
        imgAttaccoA = pygame.transform.smoothscale(imgAttaccoA, (gpx * 2, gpy))
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png", True)
        imgAttaccoS = pygame.transform.smoothscale(imgAttaccoS, (gpx, gpy * 2))
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png", True)
        imgAttaccoD = pygame.transform.smoothscale(imgAttaccoD, (gpx * 2, gpy))
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = loadImage("Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png", True)
        imgOggettoLanciato = pygame.transform.smoothscale(imgOggettoLanciato, (gpx, gpy))
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = loadImage("Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png", True)
        imgDanneggiamentoOggettoLanciato = pygame.transform.smoothscale(imgDanneggiamentoOggettoLanciato, (gpx, gpy))
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = loadImage("Immagini/Nemici/DannoRallo.png", True)
        imgDanneggiamentoRalloNemico = pygame.transform.smoothscale(imgDanneggiamentoRalloNemico, (gpx, gpy))
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = loadImage("Immagini/Nemici/DannoColco.png", True)
        imgDanneggiamentoColcoNemico = pygame.transform.smoothscale(imgDanneggiamentoColcoNemico, (gpx, gpy))
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni

loadImgs()

# canali audio / volume (0-1)
volumeCanzoni = 0.0
volumeEffetti = 0.0
pygame.mixer.set_num_channels(10)
canaleSoundCanzone = pygame.mixer.Channel(0)
canaleSoundPuntatore = pygame.mixer.Channel(1)
canaleSoundPassiRallo = pygame.mixer.Channel(2)
canaleSoundPassiColco = pygame.mixer.Channel(3)
canaleSoundPassiNemiciPersonaggi = pygame.mixer.Channel(4)
canaleSoundMorteNemici = pygame.mixer.Channel(5)
canaleSoundLvUp = pygame.mixer.Channel(6)
canaleSoundInterazioni = pygame.mixer.Channel(7)
canaleSoundAttacco = pygame.mixer.Channel(8)
canaleSoundSottofondoAmbientale = pygame.mixer.Channel(9)
def initVolumeSounds():
    canaleSoundCanzone.set_volume(volumeCanzoni)
    canaleSoundPuntatore.set_volume(volumeEffetti)
    canaleSoundPassiRallo.set_volume(volumeEffetti)
    canaleSoundPassiColco.set_volume(volumeEffetti)
    canaleSoundPassiNemiciPersonaggi.set_volume(volumeEffetti)
    canaleSoundMorteNemici.set_volume(volumeEffetti)
    canaleSoundLvUp.set_volume(volumeEffetti)
    canaleSoundInterazioni.set_volume(volumeEffetti)
    canaleSoundAttacco.set_volume(volumeEffetti)
    canaleSoundSottofondoAmbientale.set_volume(volumeEffetti)
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

pygame.mouse.set_visible(False)
mouseVisibile = False

# lettura configurazione (ordine => lingua, volEffetti, volCanzoni, schermoIntero, gsx, gsy)
leggi = loadFile("Impostazioni/Impostazioni.txt", "r")
leggifile = leggi.read()
datiFileImpostazioni = leggifile.split("_")
datiFileImpostazioni.pop(len(datiFileImpostazioni) - 1)
erroreFileImpostazioni = False
if len(datiFileImpostazioni) == 6:
    for i in range(0, len(datiFileImpostazioni)):
        try:
            datiFileImpostazioni[i] = int(datiFileImpostazioni[i])
        except ValueError:
            erroreFileImpostazioni = True
    if not erroreFileImpostazioni:
        if datiFileImpostazioni[0] == 0:
            linguaImpostata = "italiano"
        elif datiFileImpostazioni[0] == 1:
            linguaImpostata = "inglese"
        if 0 <= datiFileImpostazioni[1] <= 10:
            volumeEffetti = datiFileImpostazioni[1] / 10.0
        if 0 <= datiFileImpostazioni[2] <= 10:
            volumeCanzoni = datiFileImpostazioni[2] / 10.0
        if schermoIntero == 0 or schermoIntero == 1:
            schermoIntero = datiFileImpostazioni[3]
        if maxGsx >= datiFileImpostazioni[4] and maxGsy >= datiFileImpostazioni[5] and ((maxGsx == datiFileImpostazioni[4] and maxGsy == datiFileImpostazioni[5]) or (datiFileImpostazioni[4] == 800 and datiFileImpostazioni[5] == 450) or (datiFileImpostazioni[4] == 1024 and datiFileImpostazioni[5] == 576) or (datiFileImpostazioni[4] == 1280 and datiFileImpostazioni[5] == 720) or (datiFileImpostazioni[4] == 1920 and datiFileImpostazioni[5] == 1080)):
            gsx = datiFileImpostazioni[4]
            gsy = datiFileImpostazioni[5]
            gpx = gsx // 32
            gpy = gsy // 18
        if schermoIntero:
            opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE
            schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
        else:
            schermo = pygame.display.set_mode((gsx, gsy))
        initVolumeSounds()
        loadImgs()
else:
    erroreFileImpostazioni = True
if erroreFileImpostazioni:
    print ("Errore nella lettura del file di configurazione delle impostazioni")
    schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
leggi.close()

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
configuraCursore(False)
pygame.mouse.set_visible(True)
mouseVisibile = True
