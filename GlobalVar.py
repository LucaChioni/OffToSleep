# -*- coding: utf-8 -*-

import ctypes
from GenericFuncC import *
import win32gui, win32con

# hide the console
# The_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(The_program_to_hide, win32con.SW_HIDE)

# i suoni vengono velocizzati: metti 0,8 in velocità di audacity per risolvere
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
# pygame.mixer.init(44100, -16, 1, 512)
# pygame.mixer.init(22100, -16, 2, 64)
pygame.init()

# adattamento schermo
ctypes.windll.user32.SetProcessDPIAware()
gsx = ctypes.windll.user32.GetSystemMetrics(0)
gsy = ctypes.windll.user32.GetSystemMetrics(1)
opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE
print (gsx, gsy)
if gsx % 32 != 0 or gsy % 18 != 0:
    while gsx % 32 != 0:
        gsx = gsx - 1
    while gsy % 18 != 0:
        gsy = gsy - 1
if gsx // 16 < gsy // 9:
    print("altezza piu grande")
    gsy = gsx * 9 // 16
elif gsx // 16 > gsy // 9:
    print("larghezza piu grande")
    gsx = gsy * 16 // 9
schermoIntero = True
print (gsx, gsy)

maxGsx = gsx
maxGsy = gsy

# dimensione personaggio
gpx = gsx // 32
gpy = gsy // 18

# nome-icona
pygame.display.set_caption("Gioco 2")
icona = pygame.image.load("Immagini/Icona.png")
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
global sfondoStatAumentata
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
global costoOggetti
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
    global sfondoStatAumentata
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
    global costoOggetti
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

    # puntatore
    puntatoreorigi = loadImage("Immagini/Puntatori/Puntatore.png")
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    puntatoreorigivecchio = loadImage("Immagini/Puntatori/Puntatorevecchio.png")
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 2, gpy // 2))
    puntatIn = loadImage('Immagini/Puntatori/InquadraCVin.png')
    puntatIn = pygame.transform.smoothscale(puntatIn, (gpx, gpy))
    puntatOut = loadImage('Immagini/Puntatori/InquadraCVout.png')
    puntatOut = pygame.transform.smoothscale(puntatOut, (gpx, gpy))
    puntatDif = loadImage('Immagini/Oggetti/Difesa.png')
    puntatDif = pygame.transform.smoothscale(puntatDif, (gpx, gpy))
    puntatAtt = loadImage('Immagini/Oggetti/Attacco.png')
    puntatAtt = pygame.transform.smoothscale(puntatAtt, (gpx, gpy))
    puntatArc = loadImage('Immagini/Oggetti/AttaccoDistanza.png')
    puntatArc = pygame.transform.smoothscale(puntatArc, (gpx, gpy))
    puntatPor = loadImage('Immagini/Oggetti/ApriChiudiPorta.png')
    puntatPor = pygame.transform.smoothscale(puntatPor, (gpx, gpy))
    puntatCof = loadImage('Immagini/Oggetti/ApriCofanetto.png')
    puntatCof = pygame.transform.smoothscale(puntatCof, (gpx, gpy))
    puntatSpinta = loadImage('Immagini/Oggetti/SpingiColco.png')
    puntatSpinta = pygame.transform.smoothscale(puntatSpinta, (gpx, gpy))
    puntatBom = loadImage('Immagini/Oggetti/Oggetto6Ico.png')
    puntatBom = pygame.transform.smoothscale(puntatBom, (gpx, gpy))
    puntatBoV = loadImage('Immagini/Oggetti/Oggetto7Ico.png')
    puntatBoV = pygame.transform.smoothscale(puntatBoV, (gpx, gpy))
    puntatEsc = loadImage('Immagini/Oggetti/Oggetto8Ico.png')
    puntatEsc = pygame.transform.smoothscale(puntatEsc, (gpx, gpy))
    puntatBoA = loadImage('Immagini/Oggetti/Oggetto9Ico.png')
    puntatBoA = pygame.transform.smoothscale(puntatBoA, (gpx, gpy))
    puntatBoP = loadImage('Immagini/Oggetti/Oggetto10Ico.png')
    puntatBoP = pygame.transform.smoothscale(puntatBoP, (gpx, gpy))
    scorriSu = loadImage("Immagini/Puntatori/ScorriOggettiSu.png")
    scorriSu = pygame.transform.scale(scorriSu, (gpx, gpy))
    scorriGiu = loadImage("Immagini/Puntatori/ScorriOggettiGiu.png")
    scorriGiu = pygame.transform.scale(scorriGiu, (gpx, gpy))
    puntatDialoghi = loadImage('Immagini/Oggetti/IcoDialogo.png')
    puntatDialoghi = pygame.transform.smoothscale(puntatDialoghi, (gpx, gpy))
    puntatoreInquadraNemici = loadImage("Immagini/Puntatori/InquadraNemicoSelezionato.png")
    puntatoreInquadraNemici = pygame.transform.smoothscale(puntatoreInquadraNemici, (gpx, gpy))
    puntatoreImpostazioniDestra = loadImage("Immagini/Puntatori/ScorriImpostazioniDestra.png")
    puntatoreImpostazioniDestra = pygame.transform.scale(puntatoreImpostazioniDestra, (gpx, gpy))
    puntatoreImpostazioniSinistra = loadImage("Immagini/Puntatori/ScorriImpostazioniSinistra.png")
    puntatoreImpostazioniSinistra = pygame.transform.scale(puntatoreImpostazioniSinistra, (gpx, gpy))
    puntatoreImpostazioniDestraBloccato = loadImage("Immagini/Puntatori/ScorriImpostazioniDestraBloccato.png")
    puntatoreImpostazioniDestraBloccato = pygame.transform.scale(puntatoreImpostazioniDestraBloccato, (gpx, gpy))
    puntatoreImpostazioniSinistraBloccato = loadImage("Immagini/Puntatori/ScorriImpostazioniSinistraBloccato.png")
    puntatoreImpostazioniSinistraBloccato = pygame.transform.scale(puntatoreImpostazioniSinistraBloccato, (gpx, gpy))

    # immagini personaggio
    persw = loadImage('Immagini/Personaggi/Sara/Personaggio4.png')
    persw = pygame.transform.smoothscale(persw, (gpx, gpy))
    perswb = loadImage('Immagini/Personaggi/Sara/Personaggio4b.png')
    perswb = pygame.transform.smoothscale(perswb, (gpx, gpy))
    persa = loadImage('Immagini/Personaggi/Sara/Personaggio3.png')
    persa = pygame.transform.smoothscale(persa, (gpx, gpy))
    persab = loadImage('Immagini/Personaggi/Sara/Personaggio3b.png')
    persab = pygame.transform.smoothscale(persab, (gpx, gpy))
    perso = loadImage('Immagini/Personaggi/Sara/Personaggio1.png')
    perss = pygame.transform.smoothscale(perso, (gpx, gpy))
    persob = loadImage('Immagini/Personaggi/Sara/Personaggio1b.png')
    perssb = pygame.transform.smoothscale(persob, (gpx, gpy))
    persd = loadImage('Immagini/Personaggi/Sara/Personaggio2.png')
    persd = pygame.transform.smoothscale(persd, (gpx, gpy))
    persdb = loadImage('Immagini/Personaggi/Sara/Personaggio2b.png')
    persdb = pygame.transform.smoothscale(persdb, (gpx, gpy))
    perssm = loadImage('Immagini/Personaggi/Sara/Personaggio1mov.png')
    perssm = pygame.transform.smoothscale(perssm, (gpx, gpy))
    perssmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio1movb1.png')
    perssmb1 = pygame.transform.smoothscale(perssmb1, (gpx, gpy))
    perssmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio1movb2.png')
    perssmb2 = pygame.transform.smoothscale(perssmb2, (gpx, gpy))
    persdm = loadImage('Immagini/Personaggi/Sara/Personaggio2mov.png')
    persdm = pygame.transform.smoothscale(persdm, (gpx, gpy))
    persdmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio2movb1.png')
    persdmb1 = pygame.transform.smoothscale(persdmb1, (gpx, gpy))
    persdmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio2movb2.png')
    persdmb2 = pygame.transform.smoothscale(persdmb2, (gpx, gpy))
    persam = loadImage('Immagini/Personaggi/Sara/Personaggio3mov.png')
    persam = pygame.transform.smoothscale(persam, (gpx, gpy))
    persamb1 = loadImage('Immagini/Personaggi/Sara/Personaggio3movb1.png')
    persamb1 = pygame.transform.smoothscale(persamb1, (gpx, gpy))
    persamb2 = loadImage('Immagini/Personaggi/Sara/Personaggio3movb2.png')
    persamb2 = pygame.transform.smoothscale(persamb2, (gpx, gpy))
    perswm = loadImage('Immagini/Personaggi/Sara/Personaggio4mov.png')
    perswm = pygame.transform.smoothscale(perswm, (gpx, gpy))
    perswmb1 = loadImage('Immagini/Personaggi/Sara/Personaggio4movb1.png')
    perswmb1 = pygame.transform.smoothscale(perswmb1, (gpx, gpy))
    perswmb2 = loadImage('Immagini/Personaggi/Sara/Personaggio4movb2.png')
    perswmb2 = pygame.transform.smoothscale(perswmb2, (gpx, gpy))
    perswmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio4movbAttacco.png')
    perswmbAttacco = pygame.transform.smoothscale(perswmbAttacco, (gpx, gpy))
    persambAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio3movbAttacco.png')
    persambAttacco = pygame.transform.smoothscale(persambAttacco, (gpx, gpy))
    perssmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio1movbAttacco.png')
    perssmbAttacco = pygame.transform.smoothscale(perssmbAttacco, (gpx, gpy))
    persdmbAttacco = loadImage('Immagini/Personaggi/Sara/Personaggio2movbAttacco.png')
    persdmbAttacco = pygame.transform.smoothscale(persdmbAttacco, (gpx, gpy))
    persmbDifesa = loadImage('Immagini/Personaggi/Sara/PersonaggiomovbDifesa.png')
    persmbDifesa = pygame.transform.smoothscale(persmbDifesa, (gpx, gpy))
    persAvvele = loadImage('Immagini/Personaggi/Sara/PersonaggioAvvelenato.png')
    persAvvele = pygame.transform.smoothscale(persAvvele, (gpx, gpy))

    # immagini robot
    robow = loadImage('Immagini/Personaggi/Colco/Robot4.png')
    robow = pygame.transform.smoothscale(robow, (gpx, gpy))
    roboa = loadImage('Immagini/Personaggi/Colco/Robot3.png')
    roboa = pygame.transform.smoothscale(roboa, (gpx, gpy))
    roboo = loadImage('Immagini/Personaggi/Colco/Robot1.png')
    robos = pygame.transform.smoothscale(roboo, (gpx, gpy))
    robod = loadImage('Immagini/Personaggi/Colco/Robot2.png')
    robod = pygame.transform.smoothscale(robod, (gpx, gpy))
    robomo = loadImage('Immagini/Personaggi/Colco/Robot0.png')
    robomo = pygame.transform.smoothscale(robomo, (gpx, gpy))
    robodp = loadImage('Immagini/Personaggi/Colco/Robot2p.png')
    robodp = pygame.transform.smoothscale(robodp, (gpx, gpy))
    roboap = loadImage('Immagini/Personaggi/Colco/Robot3p.png')
    roboap = pygame.transform.smoothscale(roboap, (gpx, gpy))
    armrobmo = loadImage('Immagini/EquipRobo/Batteria00.png')
    armrobmo = pygame.transform.smoothscale(armrobmo, (gpx, gpy))
    roboSurrisc = loadImage('Immagini/Personaggi/Colco/RobotSurriscaldato.png')
    roboSurrisc = pygame.transform.smoothscale(roboSurrisc, (gpx, gpy))

    # img menu mercante
    mercanteMenu = loadImage('Immagini/Personaggi/Mercante/MercanteDialogo.png')
    mercanteMenu = pygame.transform.smoothscale(mercanteMenu, (gpx * 12, gpy * 9))
    scorriSuGiu = loadImage('Immagini/Puntatori/ScorriSuGiu.png')
    scorriSuGiu = pygame.transform.scale(scorriSuGiu, (gpx, gpy))
    scorriSuGiuBloccato = loadImage('Immagini/Puntatori/ScorriSuGiuBloccato.png')
    scorriSuGiuBloccato = pygame.transform.scale(scorriSuGiuBloccato, (gpx, gpy))
    scorriSuGiuBloccatoGiu = loadImage('Immagini/Puntatori/ScorriSuGiuBloccatoGiu.png')
    scorriSuGiuBloccatoGiu = pygame.transform.scale(scorriSuGiuBloccatoGiu, (gpx, gpy))
    scorriSuGiuBloccatoSu = loadImage('Immagini/Puntatori/ScorriSuGiuBloccatoSu.png')
    scorriSuGiuBloccatoSu = pygame.transform.scale(scorriSuGiuBloccatoSu, (gpx, gpy))
    sfondoDialogoMercante = loadImage('Immagini/DecorazioniMenu/SfondoDialogoMercante.png')
    sfondoDialogoMercante = pygame.transform.scale(sfondoDialogoMercante, (int(gpx * 9.5), int(gpy * 4.5)))
    faretra1Menu = loadImage('Immagini/Oggetti/Faretra1Menu.png')
    faretra1Menu = pygame.transform.scale(faretra1Menu, (gpx * 8, gpy * 8))
    faretra2Menu = loadImage('Immagini/Oggetti/Faretra2Menu.png')
    faretra2Menu = pygame.transform.scale(faretra2Menu, (gpx * 8, gpy * 8))
    faretra3Menu = loadImage('Immagini/Oggetti/Faretra3Menu.png')
    faretra3Menu = pygame.transform.scale(faretra3Menu, (gpx * 8, gpy * 8))
    frecciaMenu = loadImage('Immagini/Oggetti/FrecciaMenu.png')
    frecciaMenu = pygame.transform.scale(frecciaMenu, (gpx * 8, gpy * 8))

    # sfondi
    sfondostax3 = loadImage('Immagini/Status/Sfondostax3.png')
    sfondostax3 = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoRallo.png')
    sfondoRallo = pygame.transform.scale(sfondosta, (gpx * 6, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoColco.png')
    sfondoColco = pygame.transform.scale(sfondosta, (gpx * 4, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoNemici.png')
    sfondoMostro = pygame.transform.scale(sfondosta, (gpx * 3, gpy))
    sfondosta = loadImage('Immagini/Status/SfondoEsche.png')
    sfondoEsche = pygame.transform.scale(sfondosta, (gpx, gpy))
    sfondoStartBattaglia = loadImage('Immagini/Oggetti/SfondoStartBattaglia.png')
    sfondoStartBattaglia = pygame.transform.scale(sfondoStartBattaglia, (gpx * 7, gpy * 10))
    sfondoStatAumentata = loadImage('Immagini/Levelup/SfondoStatisticaAumentata.png')
    sfondoStatAumentata = pygame.transform.scale(sfondoStatAumentata, (gpx * 7, gpy * 7))
    sfondoTriangolinoAltoDestra = loadImage('Immagini/DecorazioniMenu/TriangoloAltoDestra.png')
    sfondoTriangolinoAltoDestra = pygame.transform.scale(sfondoTriangolinoAltoDestra, (gpx, gpy))
    sfondoTriangolinoAltoSinistra = loadImage('Immagini/DecorazioniMenu/TriangoloAltoSinistra.png')
    sfondoTriangolinoAltoSinistra = pygame.transform.scale(sfondoTriangolinoAltoSinistra, (gpx, gpy))
    sfondoTriangolinoBassoDestra = loadImage('Immagini/DecorazioniMenu/TriangoloBassoDestra.png')
    sfondoTriangolinoBassoDestra = pygame.transform.scale(sfondoTriangolinoBassoDestra, (gpx, gpy))
    sfondoTriangolinoBassoSinistra = loadImage('Immagini/DecorazioniMenu/TriangoloBassoSinistra.png')
    sfondoTriangolinoBassoSinistra = pygame.transform.scale(sfondoTriangolinoBassoSinistra, (gpx, gpy))

    # status
    appiccicosoo = loadImage('Immagini/Status/Appiccicoso.png')
    appiccicoso = pygame.transform.scale(appiccicosoo, (gpx * 3 // 4, gpy * 3 // 4))
    avvelenatoo = loadImage('Immagini/Status/Avvelenato.png')
    avvelenato = pygame.transform.scale(avvelenatoo, (gpx * 3 // 4, gpy * 3 // 4))
    surriscaldatoo = loadImage('Immagini/Status/Surriscaldato.png')
    surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx * 3 // 4, gpy * 3 // 4))
    attaccopiuo = loadImage('Immagini/Status/Attaccopiu.png')
    attaccopiu = pygame.transform.scale(attaccopiuo, (gpx * 3 // 4, gpy * 3 // 4))
    difesapiuo = loadImage('Immagini/Status/Difesapiu.png')
    difesapiu = pygame.transform.scale(difesapiuo, (gpx * 3 // 4, gpy * 3 // 4))
    velocitapiuo = loadImage('Immagini/Status/Velocitapiu.png')
    velocitapiu = pygame.transform.scale(velocitapiuo, (gpx * 3 // 4, gpy * 3 // 4))
    efficienzapiuo = loadImage('Immagini/Status/Efficienzapiu.png')
    efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx * 3 // 4, gpy * 3 // 4))
    imgNumFrecce = loadImage('Immagini/Status/NumFrecce.png')
    imgNumFrecce = pygame.transform.scale(imgNumFrecce, (gpx * 3 // 4, gpy * 3 // 4))

    # menu alto destra
    sfochiaveocchio = loadImage("Immagini/Oggetti/SfondoOcchioChiave.png")
    sfochiaveocchio = pygame.transform.scale(sfochiaveocchio, (gpx * 5, gpy * 2))
    occhioape = loadImage('Immagini/Status/OcchioAperto.png')
    occhioape = pygame.transform.scale(occhioape, (gpx, gpy))
    occhiochiu = loadImage('Immagini/Status/OcchioChiuso.png')
    occhiochiu = pygame.transform.scale(occhiochiu, (gpx, gpy))
    chiaveroboacc = loadImage('Immagini/Oggetti/ChiaveColcoAcc.png')
    chiaveroboacc = pygame.transform.scale(chiaveroboacc, (gpx * 2, gpy * 2))
    chiaverobospe = loadImage('Immagini/Oggetti/ChiaveColcoSpe.png')
    chiaverobospe = pygame.transform.scale(chiaverobospe, (gpx * 2, gpy * 2))

    # oggetti sulla schermata
    esche = loadImage("Immagini/Oggetti/Oggetto8Ico.png")
    esche = pygame.transform.smoothscale(esche, (gpx, gpy))
    sacchettoDenaroStart = loadImage('Immagini/Oggetti/SacchettoDenaroSinistra.png')
    sacchettoDenaroStart = pygame.transform.scale(sacchettoDenaroStart, (gpx * 4, gpy * 4))
    sacchettoDenaroMercante = loadImage('Immagini/Oggetti/SacchettoDenaroDestra.png')
    sacchettoDenaroMercante = pygame.transform.scale(sacchettoDenaroMercante, (gpx * 4, gpy * 4))
    faretraFrecceStart0 = loadImage('Immagini/EquipSara/Faretre/Faretra0Menu.png')
    faretraFrecceStart0 = pygame.transform.scale(faretraFrecceStart0, (gpx * 4, gpy * 4))
    faretraFrecceStart1 = loadImage('Immagini/EquipSara/Faretre/Faretra1Menu.png')
    faretraFrecceStart1 = pygame.transform.scale(faretraFrecceStart1, (gpx * 4, gpy * 4))
    faretraFrecceStart2 = loadImage('Immagini/EquipSara/Faretre/Faretra2Menu.png')
    faretraFrecceStart2 = pygame.transform.scale(faretraFrecceStart2, (gpx * 4, gpy * 4))
    faretraFrecceStart3 = loadImage('Immagini/EquipSara/Faretre/Faretra3Menu.png')
    faretraFrecceStart3 = pygame.transform.scale(faretraFrecceStart3, (gpx * 4, gpy * 4))
    sacchettoDenaroo = loadImage('Immagini/Oggetti/SacchettoDenaroIco.png')
    sacchettoDenaro = pygame.transform.smoothscale(sacchettoDenaroo, (gpx, gpy))
    imgFrecciaLanciata = loadImage('Immagini/Oggetti/Freccia.png')
    imgFrecciaLanciata = pygame.transform.smoothscale(imgFrecciaLanciata, (gpx, gpy))

    # cofanetti
    cofaniaper = loadImage("Immagini/Oggetti/CofanettoAperto.png")
    cofaniaper = pygame.transform.smoothscale(cofaniaper, (gpx, gpy))
    cofanichiu = loadImage("Immagini/Oggetti/CofanettoChiuso.png")
    cofanichiu = pygame.transform.smoothscale(cofanichiu, (gpx, gpy))
    sfocontcof = loadImage("Immagini/Oggetti/SfondoContenutoCofanetto.png")
    sfocontcof = pygame.transform.scale(sfocontcof, (gpx * 16, gpy * 3))

    # immagini salvataggi
    s1 = loadImage('Immagini/Salvataggi/S1.png')
    s1 = pygame.transform.smoothscale(s1, (gpx * 3, gpy * 3))
    s2 = loadImage('Immagini/Salvataggi/S2.png')
    s2 = pygame.transform.smoothscale(s2, (gpx * 3, gpy * 3))
    s3 = loadImage('Immagini/Salvataggi/S3.png')
    s3 = pygame.transform.smoothscale(s3, (gpx * 3, gpy * 3))

    # caselle attaccabili
    campoattaccabile1 = loadImage('Immagini/Campiattaccabili/Campoattaccabile1.png')
    campoattaccabile1 = pygame.transform.scale(campoattaccabile1, (gpx * 3, gpy * 3))
    campoattaccabile2 = loadImage('Immagini/Campiattaccabili/Campoattaccabile2.png')
    campoattaccabileRobo = loadImage('Immagini/Campiattaccabili/Campoattaccabile3.png')
    campoattaccabileRobo = pygame.transform.scale(campoattaccabileRobo, (gpx * 17, gpy * 17))
    caselleattaccabiliRobo = loadImage('Immagini/Campiattaccabili/CaselleattaccabiliRobo.png')
    caselleattaccabiliRobo = pygame.transform.scale(caselleattaccabiliRobo, (gpx, gpy))
    campoattaccabilemostro = loadImage('Immagini/Campiattaccabili/Campoattaccabilemostro.png')
    caselleattaccabilimostro = loadImage('Immagini/Campiattaccabili/Caselleattaccabilimostro.png')
    caselleattaccabilimostro = pygame.transform.scale(caselleattaccabilimostro, (gpx, gpy))
    caselleattaccabili = loadImage('Immagini/Campiattaccabili/Caselleattaccabili.png')
    caselleattaccabili = pygame.transform.scale(caselleattaccabili, (gpx, gpy))

    # aumento livello
    saliliv = loadImage('Immagini/Levelup/Saliliv.png')
    saliliv = pygame.transform.smoothscale(saliliv, (gpx, gpy))
    saliliv1 = loadImage('Immagini/Levelup/Saliliv1.png')
    saliliv1 = pygame.transform.smoothscale(saliliv1, (gpx, gpy))
    saliliv2 = loadImage('Immagini/Levelup/Saliliv2.png')
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
        vetImgSpadeMenu.append(pygame.transform.scale(loadImage("Immagini/EquipSara/Spade/Spada%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
        vetImgArchiMenu.append(pygame.transform.scale(loadImage("Immagini/EquipSara/Archi/Arco%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
        vetImgArmatureMenu.append(pygame.transform.scale(loadImage("Immagini/EquipSara/Armature/Armatura%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
        vetImgScudiMenu.append(pygame.transform.scale(loadImage("Immagini/EquipSara/Scudi/Scudo%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
        vetImgGuantiMenu.append(pygame.transform.scale(loadImage("Immagini/EquipSara/Guanti/Guanti%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
        vetImgCollaneMenu.append(pygame.transform.scale(loadImage("Immagini/EquipSara/Collane/Collana%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
        contatoreGlobale += 1
    vetImgCondizioniMenu = [0]
    contatoreGlobale = 1
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(pygame.transform.scale(loadImage("Immagini/GrafCondizioni/Condizione%i.png" % contatoreGlobale), (gpx * 12, gpy * 9)))
        contatoreGlobale += 1
    vetImgTecnicheMenu = [0]
    contatoreGlobale = 1
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(pygame.transform.scale(loadImage("Immagini/GrafTecniche/Tecnica%i.png" % contatoreGlobale), (gpx * 12, gpy * 9)))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(pygame.transform.smoothscale(loadImage("Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale), (gpx * 5, gpy * 5)))
        vetIcoBatterieMenu.append(pygame.transform.scale(loadImage("Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale), (gpx * 2, gpy * 2)))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(pygame.transform.scale(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale), (gpx * 10, gpy * 10)))
        vetImgOggettiMercante.append(pygame.transform.scale(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale), (gpx * 8, gpy * 8)))
        vetImgOggettiStart.append(pygame.transform.scale(loadImage("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale), (gpx * 4, gpy * 4)))
        vetIcoOggettiMenu.append(pygame.transform.smoothscale(loadImage("Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale), (gpx, gpy)))
        contatoreGlobale += 1
    # costo oggetti => costoOggetti[frecce, faretra1, faretra2, faretra3, pozione, caricabatterie, medicina, superpozione, caricabatterie migliorato, bomba, bomba veleno, esca, bomba appiccicosa, bomba potenziata]
    costoOggetti = [1, 5, 5, 7, 20, 20, 10, 15, 30, 50, 50, 10, 50, 250]

    # img equipaggiamento pixellato
    vetImgSpadePixellate = []
    vetImgArchiPixellate = []
    vetImgArmaturePixellate = []
    vetImgScudiPixellate = []
    vetImgGuantiPixellate = []
    vetImgCollanePixellate = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadePixellate.append(loadImage("Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale))
        vetImgArchiPixellate.append(loadImage("Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale))
        vetImgArmaturePixellate.append(loadImage("Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale))
        vetImgScudiPixellate.append(loadImage("Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale))
        vetImgGuantiPixellate.append(loadImage("Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale))
        vetImgCollanePixellate.append(loadImage("Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = loadImage('Immagini/AnimazioniOggetti/Bomba.png')
    imgAnimaBomba = pygame.transform.smoothscale(imgAnimaBomba, (gpx * 3, gpy * 3))
    imgAnimaBombaVeleno = loadImage('Immagini/AnimazioniOggetti/BombaVeleno.png')
    imgAnimaBombaVeleno = pygame.transform.smoothscale(imgAnimaBombaVeleno, (gpx, gpy))
    imgAnimaBombaAppiccicosa = loadImage('Immagini/AnimazioniOggetti/BombaAppiccicosa.png')
    imgAnimaBombaAppiccicosa = pygame.transform.smoothscale(imgAnimaBombaAppiccicosa, (gpx, gpy))
    imgAnimaBombaPotenziata = loadImage('Immagini/AnimazioniOggetti/BombaPotenziata.png')
    imgAnimaBombaPotenziata = pygame.transform.smoothscale(imgAnimaBombaPotenziata, (gpx * 5, gpy * 5))
    imgAnimaPozione1 = loadImage('Immagini/AnimazioniOggetti/Pozione1.png')
    imgAnimaPozione1 = pygame.transform.smoothscale(imgAnimaPozione1, (gpx, gpy))
    imgAnimaPozione2 = loadImage('Immagini/AnimazioniOggetti/Pozione2.png')
    imgAnimaPozione2 = pygame.transform.smoothscale(imgAnimaPozione2, (gpx, gpy))
    imgAnimaMedicina1 = loadImage('Immagini/AnimazioniOggetti/Medicina1.png')
    imgAnimaMedicina1 = pygame.transform.smoothscale(imgAnimaMedicina1, (gpx, gpy))
    imgAnimaMedicina2 = loadImage('Immagini/AnimazioniOggetti/Medicina2.png')
    imgAnimaMedicina2 = pygame.transform.smoothscale(imgAnimaMedicina2, (gpx, gpy))
    imgAnimaCaricabatterie = loadImage('Immagini/AnimazioniOggetti/Caricabatterie.png')
    imgAnimaCaricabatterie = pygame.transform.smoothscale(imgAnimaCaricabatterie, (gpx, gpy))

    # img animazioni tecniche
    imgDanneggiamentoColco = loadImage('Immagini/AnimazioniTecniche/Danneggiamento.png')
    imgDanneggiamentoColco = pygame.transform.smoothscale(imgDanneggiamentoColco, (gpx, gpy))
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = loadImage("Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale)
            img2 = loadImage("Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale)
            img1 = pygame.transform.smoothscale(img1, (gpx, gpy * 2))
            img2 = pygame.transform.smoothscale(img2, (gpx, gpy * 2))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale)
            img2 = loadImage("Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale)
            img1 = pygame.transform.smoothscale(img1, (gpx * 2, gpy))
            img2 = pygame.transform.smoothscale(img2, (gpx * 2, gpy))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale)
            img2 = loadImage("Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale)
            img1 = pygame.transform.smoothscale(img1, (gpx, gpy * 2))
            img2 = pygame.transform.smoothscale(img2, (gpx, gpy * 2))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = loadImage("Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale)
            img2 = loadImage("Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale)
            img1 = pygame.transform.smoothscale(img1, (gpx * 2, gpy))
            img2 = pygame.transform.smoothscale(img2, (gpx * 2, gpy))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = loadImage("Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale)
            img1 = pygame.transform.smoothscale(img1, (gpx, gpy))
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = loadImage("Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale)
            img2 = loadImage("Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale)
            img1 = pygame.transform.smoothscale(img1, (gpx * 17, gpy * 17))
            img2 = pygame.transform.smoothscale(img2, (gpx * 17, gpy * 17))
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata.png')
    imgFrecciaEletttricaLanciata = pygame.transform.smoothscale(imgFrecciaEletttricaLanciata, (gpx, gpy))
    imgFrecciaEletttricaLanciataP = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata+.png')
    imgFrecciaEletttricaLanciataP = pygame.transform.smoothscale(imgFrecciaEletttricaLanciataP, (gpx, gpy))
    imgFrecciaEletttricaLanciataPP = loadImage('Immagini/AnimazioniTecniche/FrecciaLanciata++.png')
    imgFrecciaEletttricaLanciataPP = pygame.transform.smoothscale(imgFrecciaEletttricaLanciataPP, (gpx, gpy))

    # img sfondi dialoghi
    sfondoDialoghi = loadImage('Immagini/Dialoghi/SfondoSotto.png')
    sfondoDialoghi = pygame.transform.scale(sfondoDialoghi, (gsx, gsy // 3))

    # img tutorial
    tutorialTastieraInGioco = loadImage('Immagini/Tutorial/TastieraInGioco.png')
    tutorialTastieraInGioco = pygame.transform.smoothscale(tutorialTastieraInGioco, (gsx // 32 * 7, gsy // 18 * 11))
    tutorialTastieraInMenu = loadImage('Immagini/Tutorial/TastieraInMenu.png')
    tutorialTastieraInMenu = pygame.transform.smoothscale(tutorialTastieraInMenu, (gsx // 32 * 7, gsy // 18 * 11))
    tutorialMouse = loadImage('Immagini/Tutorial/Mouse.png')
    tutorialMouse = pygame.transform.smoothscale(tutorialMouse, (gsx // 32 * 7, gsy // 18 * 11))

    # img grafiche / dialoghi
    persGrafMenu = loadImage('Immagini/Disegni/RalloGrafMenu.png')
    persGrafMenu = pygame.transform.scale(persGrafMenu, (gpx * 18, gpy * 18))
    saraGrafMenu = loadImage('Immagini/Disegni/SaraGrafMenu.png')
    saraGrafMenu = pygame.transform.scale(saraGrafMenu, (gpx * 10, gpy * 10))
    fraMaggioreGrafMenu = loadImage('Immagini/Disegni/FratelloMaggioreGrafMenu.png')
    fraMaggioreGrafMenu = pygame.transform.scale(fraMaggioreGrafMenu, (gpx * 10, gpy * 10))
    robograf0 = loadImage('Immagini/Disegni/RobotGraf0.png')
    robograf0 = pygame.transform.scale(robograf0, (gpx * 18, gpy * 18))
    robograf1o = loadImage('Immagini/Disegni/RobotGraf1.png')
    robograf1 = pygame.transform.scale(robograf1o, (gpx * 18, gpy * 18))
    robograf1b = pygame.transform.scale(robograf1o, (gpx * 10, gpy * 10))
    robograf2o = loadImage('Immagini/Disegni/RobotGraf2.png')
    robograf2 = pygame.transform.scale(robograf2o, (gpx * 18, gpy * 18))
    robograf2b = pygame.transform.scale(robograf2o, (gpx * 10, gpy * 10))
    robograf3 = loadImage('Immagini/Disegni/RobotGraf3.png')
    robograf3 = pygame.transform.scale(robograf3, (gpx * 18, gpy * 18))
    robograf4 = loadImage('Immagini/Disegni/RobotGraf4.png')
    robograf4 = pygame.transform.scale(robograf4, (gpx * 18, gpy * 18))
    imgDialogoFraMaggiore = loadImage('Immagini/Dialoghi/FratelloMaggioreDialogo.png')
    imgDialogoSara = loadImage('Immagini/Dialoghi/SaraDialogo.png')
    imgFraMaggioreMenuOggetti = loadImage('Immagini/DecorazioniMenu/FratelloMaggioreMenu.png')
    imgFraMaggioreMenuOggetti = pygame.transform.smoothscale(imgFraMaggioreMenuOggetti, (gpx * 3, gpy * 3))
    imgSaraMenuOggetti = loadImage('Immagini/DecorazioniMenu/SaraMenu.png')
    imgSaraMenuOggetti = pygame.transform.smoothscale(imgSaraMenuOggetti, (gpx * 3, gpy * 3))

    # indicatori vita
    indvita = loadImage('Immagini/Barrevita/Indvita.png')
    fineindvita = loadImage('Immagini/Barrevita/FineIndVita.png')
    vitanemico00 = loadImage('Immagini/Barrevita/Vitanemico00.png')
    vitanemico0 = loadImage('Immagini/Barrevita/Vitanemico0.png')
    vitanemico1 = loadImage('Immagini/Barrevita/Vitanemico1.png')
    vitanemico2 = loadImage('Immagini/Barrevita/Vitanemico2.png')
    vitanemico3 = loadImage('Immagini/Barrevita/Vitanemico3.png')
    vitanemico4 = loadImage('Immagini/Barrevita/Vitanemico4.png')
    vitanemico5 = loadImage('Immagini/Barrevita/Vitanemico5.png')
    vitanemico6 = loadImage('Immagini/Barrevita/Vitanemico6.png')
    vitanemico7 = loadImage('Immagini/Barrevita/Vitanemico7.png')
    vitanemico8 = loadImage('Immagini/Barrevita/Vitanemico8.png')
    vitanemico9 = loadImage('Immagini/Barrevita/Vitanemico9.png')
    vitapersonaggio = loadImage('Immagini/Barrevita/Vitapersonaggio.png')
    vitarobo = loadImage('Immagini/Barrevita/Vitarobo.png')

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = loadImage("Immagini/EquipSara/SfondoOggetto.png")
    sfondoOggettoMenu = pygame.transform.scale(sfondoOggettoMenu, (int(gpx * 2), int(gpy * 2)))
    sconosciutoEquipMenu = loadImage("Immagini/Oggetti/SconosciutoEquip.png")
    sconosciutoEquipMenu = pygame.transform.scale(sconosciutoEquipMenu, (int(gpx * 2), int(gpy * 2)))
    sconosciutoOggettoMenu = loadImage("Immagini/Oggetti/Sconosciuto.png")
    sconosciutoOggettoIcoMenu = loadImage("Immagini/Oggetti/SconosciutoIco.png")

    # img mappe
    imgMappa1 = loadImage("Immagini/DecorazioniMenu/MappaMenu1.png")
    imgMappa2 = loadImage("Immagini/DecorazioniMenu/MappaMenu2.png")
    imgMappa3 = loadImage("Immagini/DecorazioniMenu/MappaMenu3.png")
    imgMappa4 = loadImage("Immagini/DecorazioniMenu/MappaMenu4.png")
    imgMappa5 = loadImage("Immagini/DecorazioniMenu/MappaMenu5.png")
    imgMappa6 = loadImage("Immagini/DecorazioniMenu/MappaMenu6.png")
    imgMappa7 = loadImage("Immagini/DecorazioniMenu/MappaMenu7.png")
    imgMappa8 = loadImage("Immagini/DecorazioniMenu/MappaMenu8.png")
    imgMappa9 = loadImage("Immagini/DecorazioniMenu/MappaMenu9.png")
    imgMappa10 = loadImage("Immagini/DecorazioniMenu/MappaMenu10.png")
    imgMappa11 = loadImage("Immagini/DecorazioniMenu/MappaMenu11.png")
    imgMappa12 = loadImage("Immagini/DecorazioniMenu/MappaMenu12.png")
    imgMappa13 = loadImage("Immagini/DecorazioniMenu/MappaMenu13.png")
    imgMappa14 = loadImage("Immagini/DecorazioniMenu/MappaMenu14.png")
    imgOmbreggiaturaContorniMappaMenu = loadImage("Immagini/DecorazioniMenu/OmbreggiaturaContorniMappaMenu.png")
    imgOmbreggiaturaContorniMappaMenu = pygame.transform.scale(imgOmbreggiaturaContorniMappaMenu, (gsx, gsy))

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "Cinghiale", "LupoGrigio", "LupoNero", "LupoBianco", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png")
        imgW = pygame.transform.smoothscale(imgW, (gpx, gpy))
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png")
        imgA = pygame.transform.smoothscale(imgA, (gpx, gpy))
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png")
        imgS = pygame.transform.smoothscale(imgS, (gpx, gpy))
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png")
        imgD = pygame.transform.smoothscale(imgD, (gpx, gpy))
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png")
        imgWMov1 = pygame.transform.smoothscale(imgWMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png")
        imgWMov2 = pygame.transform.smoothscale(imgWMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png")
        imgAMov1 = pygame.transform.smoothscale(imgAMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png")
        imgAMov2 = pygame.transform.smoothscale(imgAMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png")
        imgSMov1 = pygame.transform.smoothscale(imgSMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png")
        imgSMov2 = pygame.transform.smoothscale(imgSMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png")
        imgDMov1 = pygame.transform.smoothscale(imgDMov1, (gpx, gpy))
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png")
        imgDMov2 = pygame.transform.smoothscale(imgDMov2, (gpx, gpy))
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = loadImage("Immagini/Nemici/NemicoAvvelenato.png")
        imgAvvelenamento = pygame.transform.smoothscale(imgAvvelenamento, (gpx, gpy))
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = loadImage("Immagini/Nemici/NemicoAppiccicato.png")
        imgAppiccicato = pygame.transform.smoothscale(imgAppiccicato, (gpx, gpy))
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png")
        imgAttaccoW = pygame.transform.smoothscale(imgAttaccoW, (gpx, gpy * 2))
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png")
        imgAttaccoA = pygame.transform.smoothscale(imgAttaccoA, (gpx * 2, gpy))
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png")
        imgAttaccoS = pygame.transform.smoothscale(imgAttaccoS, (gpx, gpy * 2))
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = loadImage("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png")
        imgAttaccoD = pygame.transform.smoothscale(imgAttaccoD, (gpx * 2, gpy))
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = loadImage("Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png")
        imgOggettoLanciato = pygame.transform.smoothscale(imgOggettoLanciato, (gpx, gpy))
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = loadImage("Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png")
        imgDanneggiamentoOggettoLanciato = pygame.transform.smoothscale(imgDanneggiamentoOggettoLanciato, (gpx, gpy))
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = loadImage("Immagini/Nemici/DannoRallo.png")
        imgDanneggiamentoRalloNemico = pygame.transform.smoothscale(imgDanneggiamentoRalloNemico, (gpx, gpy))
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = loadImage("Immagini/Nemici/DannoColco.png")
        imgDanneggiamentoColcoNemico = pygame.transform.smoothscale(imgDanneggiamentoColcoNemico, (gpx, gpy))
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni

loadImgs()

# canali audio / volume (0-1)
volumeCanzoni = 0.0
volumeEffetti = 0.0
pygame.mixer.set_num_channels(8)
canaleSoundCanzone = pygame.mixer.Channel(0)
canaleSoundPuntatore = pygame.mixer.Channel(1)
canaleSoundPassiRallo = pygame.mixer.Channel(2)
canaleSoundPassiColco = pygame.mixer.Channel(3)
canaleSoundPassiNemiciPersonaggi = pygame.mixer.Channel(4)
canaleSoundLvUp = pygame.mixer.Channel(5)
canaleSoundInterazioni = pygame.mixer.Channel(6)
canaleSoundAttacco = pygame.mixer.Channel(7)
def initVolumeSounds():
    canaleSoundCanzone.set_volume(volumeCanzoni)
    canaleSoundPuntatore.set_volume(volumeEffetti)
    canaleSoundPassiRallo.set_volume(volumeEffetti)
    canaleSoundPassiColco.set_volume(volumeEffetti)
    canaleSoundPassiNemiciPersonaggi.set_volume(volumeEffetti)
    canaleSoundLvUp.set_volume(volumeEffetti)
    canaleSoundInterazioni.set_volume(volumeEffetti)
    canaleSoundAttacco.set_volume(volumeEffetti)
initVolumeSounds()

# suoni puntatore
selsta = pygame.mixer.Sound("Audio/RumoriPuntatore/SelSta.wav")
selind = pygame.mixer.Sound("Audio/RumoriPuntatore/SelInd.wav")
spostapun = pygame.mixer.Sound("Audio/RumoriPuntatore/SpostaPun.wav")
selimp = pygame.mixer.Sound("Audio/RumoriPuntatore/SelImp.wav")
selezione = pygame.mixer.Sound("Audio/RumoriPuntatore/Selezione.wav")
spostaPunBattaglia = pygame.mixer.Sound("Audio/RumoriPuntatore/SpostaPunBattaglia.wav")
selObbiettivo = pygame.mixer.Sound("Audio/RumoriPuntatore/SelObbiettivo.wav")

# suoni personaggio
rumoreAttaccoSpada = pygame.mixer.Sound("Audio/RumoriPersonaggio/AttaccoSpada.wav")
rumoreLancioFreccia = pygame.mixer.Sound("Audio/RumoriPersonaggio/LancioFreccia.wav")
rumoreAttaccoArco = pygame.mixer.Sound("Audio/RumoriPersonaggio/AttaccoArco.wav")
rumoreParata = pygame.mixer.Sound("Audio/RumoriPersonaggio/ParataConScudo.wav")
rumorecamminata = pygame.mixer.Sound("Audio/RumoriPersonaggio/Camminata.wav")
rumorelevelup = pygame.mixer.Sound("Audio/RumoriPersonaggio/Levelup.wav")
rumoreMorte = pygame.mixer.Sound("Audio/RumoriPersonaggio/Morte.wav")

# suoni apertura-chiusura cofanetti-porte
suonoaperturacofanetti = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaCofanetto.wav")
suonoaperturaporte1 = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaPorta1.wav")
suonoaperturaporte2 = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaPorta2.wav")
suonoaperturaporte3 = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaPorta3.wav")
suonochiusuraporte1 = pygame.mixer.Sound("Audio/RumoriAmbiente/ChiusuraPorta1.wav")
suonochiusuraporte2 = pygame.mixer.Sound("Audio/RumoriAmbiente/ChiusuraPorta2.wav")
suonochiusuraporte3 = pygame.mixer.Sound("Audio/RumoriAmbiente/ChiusuraPorta3.wav")

# souno raccolta esca - monete
suonoRaccoltaEsca = pygame.mixer.Sound("Audio/RumoriAmbiente/RaccoltaEsca.wav")
suonoRaccoltaMonete = pygame.mixer.Sound("Audio/RumoriAmbiente/RaccoltaMonete.wav")
rumoreAcquisto = pygame.mixer.Sound("Audio/RumoriAmbiente/Acquisto.wav")

# suoni robo
rumoreCamminataColco = pygame.mixer.Sound("Audio/RumoriColco/Camminata.wav")
rumoreScossaFreccia = pygame.mixer.Sound("Audio/RumoriColco/ScossaFreccia.wav")
rumoreTempestaElettrica = pygame.mixer.Sound("Audio/RumoriColco/TempestaElettrica.wav")
rumoreCuraRobo = pygame.mixer.Sound("Audio/RumoriColco/Cura.wav")
rumoreAntidoto = pygame.mixer.Sound("Audio/RumoriColco/Antidoto.wav")
rumoreAttPDifP = pygame.mixer.Sound("Audio/RumoriColco/AttPDifP.wav")
rumoreAutoricarica = pygame.mixer.Sound("Audio/RumoriColco/Autoricarica.wav")
rumoreRaffreddamento = pygame.mixer.Sound("Audio/RumoriColco/Raffreddamento.wav")
rumoreVelocizzaEfficienza = pygame.mixer.Sound("Audio/RumoriColco/VelocizzaEfficienza.wav")

# suono oggetti
suonoTeleColco = pygame.mixer.Sound("Audio/RumoriOggetti/TeleColco.wav")
suonoLancioOggetti = pygame.mixer.Sound("Audio/RumoriOggetti/LancioOggetti.wav")
suonoUsoPozione = pygame.mixer.Sound("Audio/RumoriOggetti/Pozione.wav")
suonoUsoCaricabatterie = pygame.mixer.Sound("Audio/RumoriOggetti/Caricabatterie.wav")
suonoUsoMedicina = pygame.mixer.Sound("Audio/RumoriOggetti/Medicina.wav")
suonoUsoBomba = pygame.mixer.Sound("Audio/RumoriOggetti/Bomba.wav")
suonoUsoBombaVeleno = pygame.mixer.Sound("Audio/RumoriOggetti/BombaVeleno.wav")
suonoUsoEsca = pygame.mixer.Sound("Audio/RumoriOggetti/Esca.wav")
suonoUsoBombaAppiccicosa = pygame.mixer.Sound("Audio/RumoriOggetti/BombaAppiccicosa.wav")
suonoUsoBombaPotenziata = pygame.mixer.Sound("Audio/RumoriOggetti/BombaPotenziata.wav")

# suoni nemici
rumoreMovimentoNemiciPersonaggi = pygame.mixer.Sound("Audio/RumoriNemici/MovimentoNemiciPersonaggi.wav")
rumoreAttaccoNemico = pygame.mixer.Sound("Audio/RumoriNemici/AttaccoVicinoNemico.wav")
rumoreLancioOggettoNemico = pygame.mixer.Sound("Audio/RumoriNemici/AttaccoLontanoNemico.wav")

# suono mappa
suonoAperturaMappa = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaMappa.wav")

# suoni canzoni
c11 = pygame.mixer.Sound("Audio/Canzoni/Canzone11.wav")
c27 = pygame.mixer.Sound("Audio/Canzoni/Canzone27.wav")

# dati tecniche di Colco [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesa++]
costoTecniche = [5, 10, 10, 5, 10, 10, 1, 20, 10, 10, 15, 20, 20, 30, 20, 30, 1, 20, 20, 40]
dannoTecniche = [40, 30, 0, 30, 20, 0, 150, 120, 160, 130, 15, 10, 10, 15, 100, 250, 300, 320, 260, 200]

avanzamentoStoriaCambioPersonaggio = 1
avanzamentoStoriaIncontroColco = 2

vistaRobo = 8

pygame.mouse.set_visible(False)
mouseVisibile = False

# lettura configurazione (ordine => lingua, volEffetti, volCanzoni, schermoIntero, gsx, gsy)
leggi = open("Impostazioni/Impostazioni.txt", "r")
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
    print "Errore nella lettura del file di configurazione delle impostazioni"
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
