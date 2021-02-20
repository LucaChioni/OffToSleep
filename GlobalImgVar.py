# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar


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
global lucy1GrafMenu
global lucy2GrafMenu
global fraMaggioreGrafMenu
global robograf0
global robograf1
global robograf1b
global robograf2
global robograf2b
global robograf3
global robograf4
global imgDialogoFraMaggiore
global imgDialogoLucy1
global imgDialogoLucy2
global imgFraMaggioreMenuOggetti
global imgLucy1MenuOggetti
global imgLucy2MenuOggetti
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
global persoLucy1
global persoLucy2
global persobLucy
global persoFraMaggiore
global persobFraMaggiore
global schemataDiCaricamento

def loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True):
    img = pygame.image.load(GlobalHWVar.gamePath + path)

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

    GlobalHWVar.listaTastiPremuti = []

    return img

numImgTotali = 1092
def caricaImmagineMostrandoAvanzamento(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True):
    global numImgCaricataTemp
    immagine = loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscuPiuScu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 6.5, int(GlobalHWVar.gpx * 16), GlobalHWVar.gpy * 1))
    numImgCaricataTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 15.0 / numImgTotali) * numImgCaricataTemp
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 6.5, int(caricamentoCompiuto), GlobalHWVar.gpy * 1))
    GlobalHWVar.aggiornaSchermo()
    return immagine
def caricaImmagineCambioRisoluzione(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True):
    global numImgCaricataTemp
    immagine = loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscuPiuScu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 10, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 1))
    numImgCaricataTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 31.0 / numImgTotali) * numImgCaricataTemp
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 10, int(caricamentoCompiuto), GlobalHWVar.gpy * 1))
    GlobalHWVar.aggiornaSchermo()
    return immagine

def loadImgs(numImgCaricata, cambioRisoluzione=False):
    global numImgCaricataTemp
    numImgCaricataTemp = numImgCaricata

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
    global lucy1GrafMenu
    global lucy2GrafMenu
    global fraMaggioreGrafMenu
    global robograf0
    global robograf1
    global robograf1b
    global robograf2
    global robograf2b
    global robograf3
    global robograf4
    global imgDialogoFraMaggiore
    global imgDialogoLucy1
    global imgDialogoLucy2
    global imgFraMaggioreMenuOggetti
    global imgLucy1MenuOggetti
    global imgLucy2MenuOggetti
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
    global persoLucy1
    global persoLucy2
    global persobLucy
    global persoFraMaggiore
    global persobFraMaggiore
    global schemataDiCaricamento

    if cambioRisoluzione:
        funzionePerCaricareImmagini = caricaImmagineCambioRisoluzione
    else:
        funzionePerCaricareImmagini = caricaImmagineMostrandoAvanzamento

    # puntatore
    puntatore = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/Puntatore.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True)
    puntatorevecchio = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/Puntatorevecchio.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True)
    puntatIn = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/InquadraCVin.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatOut = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/InquadraCVout.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatSfo = funzionePerCaricareImmagini('Immagini/Oggetti/sfondoOggettoLanciato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatDif = funzionePerCaricareImmagini('Immagini/Oggetti/Difesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatAtt = funzionePerCaricareImmagini('Immagini/Oggetti/Attacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatArc = funzionePerCaricareImmagini('Immagini/Oggetti/AttaccoDistanza.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatPor = funzionePerCaricareImmagini('Immagini/Oggetti/ApriChiudiPorta.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatCof = funzionePerCaricareImmagini('Immagini/Oggetti/ApriCofanetto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatAnalisi = funzionePerCaricareImmagini('Immagini/Oggetti/AnalizzaColco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBom = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto6Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBoV = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto7Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatEsc = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto8Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBoA = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto9Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBoP = funzionePerCaricareImmagini('Immagini/Oggetti/Oggetto10Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSu = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriOggettiSu.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriGiu = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriOggettiGiu.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatDialoghi = funzionePerCaricareImmagini('Immagini/Oggetti/IcoDialogo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreInquadraNemici = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/InquadraNemicoSelezionato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniDestra = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestra.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniSinistra = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistra.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniDestraBloccato = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestraBloccato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniSinistraBloccato = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistraBloccato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # immagini personaggio
    persw = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswb = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persa = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persab = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perso = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persob = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    perss = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssb = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persd = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdb = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssm = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdm = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio2mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio2movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio2movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persam = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio3mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persamb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio3movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persamb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio3movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswm = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio4mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmb1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio4movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmb2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio4movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmbAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio4movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persambAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio3movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmbAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmbAttacco = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio2movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persmbDifesa = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/PersonaggiomovbDifesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persAvvele = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/PersonaggioAvvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persoLucy1 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persoLucy2 = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy2/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persobLucy = funzionePerCaricareImmagini('Immagini/Personaggi/Lucy1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persoFraMaggiore = funzionePerCaricareImmagini('Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persobFraMaggiore = funzionePerCaricareImmagini('Immagini/Personaggi/FratelloMaggiore/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)

    # immagini robot
    robow = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboa = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboo1 = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    roboo2 = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    robos = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    robod = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    robomo = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot0.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    robodp = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot2p.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboap = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/Robot3p.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    armrobmo = funzionePerCaricareImmagini('Immagini/EquipRobo/Batteria00.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboSurrisc = funzionePerCaricareImmagini('Immagini/Personaggi/Colco/RobotSurriscaldato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = funzionePerCaricareImmagini("Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgDanneggiamentoCausaColco = funzionePerCaricareImmagini("Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img menu mercante
    mercanteMenu = funzionePerCaricareImmagini('Immagini/Personaggi/Mercante/MercanteDialogo.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    scorriSuGiu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccato = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccatoGiu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccatoSu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoSu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoDialogoMercante = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/SfondoDialogoMercante.png', GlobalHWVar.gpx * 9.5, GlobalHWVar.gpy * 4.5, False)
    faretra1Menu = funzionePerCaricareImmagini('Immagini/Oggetti/Faretra1Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra2Menu = funzionePerCaricareImmagini('Immagini/Oggetti/Faretra2Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra3Menu = funzionePerCaricareImmagini('Immagini/Oggetti/Faretra3Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    frecciaMenu = funzionePerCaricareImmagini('Immagini/Oggetti/FrecciaMenu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)

    # sfondi
    sfondoRallo = funzionePerCaricareImmagini('Immagini/Status/SfondoRallo.png', GlobalHWVar.gpx * 6, GlobalHWVar.gpy, False)
    sfondoColco = funzionePerCaricareImmagini('Immagini/Status/SfondoColco.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy, False)
    sfondoMostro = funzionePerCaricareImmagini('Immagini/Status/SfondoNemici.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy, False)
    sfondoEsche = funzionePerCaricareImmagini('Immagini/Status/SfondoEsche.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoStartBattaglia = funzionePerCaricareImmagini('Immagini/Oggetti/SfondoStartBattaglia.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 10, False)
    sfondoTriangolinoAltoDestra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloAltoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoAltoSinistra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoDestra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloBassoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoSinistra = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # status
    appiccicoso = funzionePerCaricareImmagini('Immagini/Status/Appiccicoso.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    avvelenatoMenu = funzionePerCaricareImmagini('Immagini/Status/Avvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    avvelenato = funzionePerCaricareImmagini('Immagini/Status/Avvelenato.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    surriscaldatoMenu = funzionePerCaricareImmagini('Immagini/Status/Surriscaldato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    surriscaldato = funzionePerCaricareImmagini('Immagini/Status/Surriscaldato.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    attaccopiuMenu = funzionePerCaricareImmagini('Immagini/Status/Attaccopiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    attaccopiu = funzionePerCaricareImmagini('Immagini/Status/Attaccopiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    difesapiuMenu = funzionePerCaricareImmagini('Immagini/Status/Difesapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    difesapiu = funzionePerCaricareImmagini('Immagini/Status/Difesapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    velocitapiuMenu = funzionePerCaricareImmagini('Immagini/Status/Velocitapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    velocitapiu = funzionePerCaricareImmagini('Immagini/Status/Velocitapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    efficienzapiuMenu = funzionePerCaricareImmagini('Immagini/Status/Efficienzapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    efficienzapiu = funzionePerCaricareImmagini('Immagini/Status/Efficienzapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    imgNumFrecce = funzionePerCaricareImmagini('Immagini/Status/NumFrecce.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)

    # menu alto destra
    sfochiaveocchio = funzionePerCaricareImmagini("Immagini/Oggetti/SfondoOcchioChiave.png", GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, False)
    occhioape = funzionePerCaricareImmagini('Immagini/Status/OcchioAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    occhiochiu = funzionePerCaricareImmagini('Immagini/Status/OcchioChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    chiaveroboacc = funzionePerCaricareImmagini('Immagini/Oggetti/ChiaveColcoAcc.png', GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True)
    chiaverobospe = funzionePerCaricareImmagini('Immagini/Oggetti/ChiaveColcoSpe.png', GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True)

    # oggetti sulla schermata
    esche = funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto8Ico.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sacchettoDenaroStart = funzionePerCaricareImmagini('Immagini/Oggetti/SacchettoDenaroSinistra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaroMercante = funzionePerCaricareImmagini('Immagini/Oggetti/SacchettoDenaroDestra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart0 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra0Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart1 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra1Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart2 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra2Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart3 = funzionePerCaricareImmagini('Immagini/EquipLucy/Faretre/Faretra3Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaro = funzionePerCaricareImmagini('Immagini/Oggetti/SacchettoDenaroIco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaLanciata = funzionePerCaricareImmagini('Immagini/Oggetti/Freccia.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # cofanetti
    cofaniaper = funzionePerCaricareImmagini("Immagini/Oggetti/CofanettoAperto.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    cofanichiu = funzionePerCaricareImmagini("Immagini/Oggetti/CofanettoChiuso.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfocontcof = funzionePerCaricareImmagini("Immagini/Oggetti/SfondoContenutoCofanetto.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 3, False)

    # immagini salvataggi
    s1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Salvataggi/S1.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, False)
    s2 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Salvataggi/S2.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, False)
    s3 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Salvataggi/S3.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, False)

    # caselle attaccabili
    campoattaccabileRallo1 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    campoattaccabileRallo2 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False)
    campoattaccabileRallo3 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    campoattaccabileRallo4 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False)
    campoattaccabileRallo5 = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    campoattaccabileRobo = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Campoattaccabile3.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    caselleattaccabiliRobo = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/CaselleattaccabiliRobo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    caselleattaccabilimostro = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Caselleattaccabilimostro.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    caselleattaccabili = funzionePerCaricareImmagini('Immagini/Status/Campiattaccabili/Caselleattaccabili.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # aumento livello
    saliliv = funzionePerCaricareImmagini('Immagini/Status/Levelup/Saliliv.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    saliliv1 = funzionePerCaricareImmagini('Immagini/Status/Levelup/Saliliv1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    saliliv2 = funzionePerCaricareImmagini('Immagini/Status/Levelup/Saliliv2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    vetImgSpadeMenu = []
    vetImgArchiMenu = []
    vetImgArmatureMenu = []
    vetImgScudiMenu = []
    vetImgGuantiMenu = []
    vetImgCollaneMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadeMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Spade/Spada%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArchiMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Archi/Arco%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArmatureMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Armature/Armatura%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgScudiMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Scudi/Scudo%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgGuantiMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Guanti/Guanti%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgCollaneMenu.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Collane/Collana%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        contatoreGlobale += 1
    imgGambitSconosciuta = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/GrafGambit/Sconosciuto.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    vetImgCondizioniMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(funzionePerCaricareImmagini("Immagini/DecorazioniMenu/GrafGambit/GrafCondizioni/Condizione%i.png" % contatoreGlobale, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False))
        contatoreGlobale += 1
    vetImgTecnicheMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(funzionePerCaricareImmagini("Immagini/DecorazioniMenu/GrafGambit/GrafTecniche/Tecnica%i.png" % contatoreGlobale, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(funzionePerCaricareImmagini("Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetIcoBatterieMenu.append(funzionePerCaricareImmagini("Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False))
        vetImgOggettiMercante.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False))
        vetImgOggettiStart.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False))
        vetIcoOggettiMenu.append(funzionePerCaricareImmagini("Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
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
        vetImgSpadePixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Spade/Spada%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArchiPixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Archi/Arco%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArmaturePixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Armature/Armatura%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgScudiPixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Scudi/Scudo%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgGuantiPixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Guanti/Guanti%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgCollanePixellate.append(funzionePerCaricareImmagini("Immagini/EquipLucy/Collane/Collana%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Bomba.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgAnimaBombaVeleno = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/BombaVeleno.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaBombaAppiccicosa = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/BombaAppiccicosa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaBombaPotenziata = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/BombaPotenziata.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    imgAnimaPozione1 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Pozione1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaPozione2 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Pozione2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaMedicina1 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Medicina1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaMedicina2 = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Medicina2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaCaricabatterie = funzionePerCaricareImmagini('Immagini/AnimazioniOggetti/Caricabatterie.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img animazioni tecniche
    imgDanneggiamentoColco = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/Danneggiamento.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            imgSelf = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnimaSelf.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(imgSelf)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, True)
            img2 = funzionePerCaricareImmagini("Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/FrecciaLanciata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaEletttricaLanciataP = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/FrecciaLanciata+.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaEletttricaLanciataPP = funzionePerCaricareImmagini('Immagini/AnimazioniTecniche/FrecciaLanciata++.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img sfondi dialoghi
    sfondoDialoghi = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/SfondoSotto.png', GlobalHWVar.gsx, GlobalHWVar.gsy // 3, False)

    # img tutorial
    tutorialTastieraInGioco = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/TastieraInGioco.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialTastieraInMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/TastieraInMenu.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialMouse = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/Mouse.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialControllerInGioco = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ControllerInGioco.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialControllerInMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ControllerInMenu.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    impostazioniController = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoController.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroce = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroce.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCerchio = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerCerchio.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerQuadrato = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerQuadrato.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerTriangolo = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerTriangolo.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerL1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerL1.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerR1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerR1.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerStart = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerStart.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)

    # img grafiche / dialoghi
    persGrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/NeilGrafMenu.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    lucy1GrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/Lucy1GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    lucy2GrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/Lucy2GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    fraMaggioreGrafMenu = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf0 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf0.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf1b = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf2 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf2b = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf3 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf3.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf4 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    imgDialogoFraMaggiore = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/FratelloMaggioreDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoLucy1 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/Lucy1Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoLucy2 = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Dialoghi/Lucy2Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgFraMaggioreMenuOggetti = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/FratelloMaggioreMenu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgLucy1MenuOggetti = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Lucy1Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgLucy2MenuOggetti = funzionePerCaricareImmagini('Immagini/DecorazioniMenu/Lucy2Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)

    # indicatori vita
    indvita = funzionePerCaricareImmagini('Immagini/Status/Barrevita/Indvita.png', 0, 0, True)
    fineindvita = funzionePerCaricareImmagini('Immagini/Status/Barrevita/FineIndVita.png', GlobalHWVar.gpx // 12, GlobalHWVar.gpy // 4, True)
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
    sfondoOggettoMenu = funzionePerCaricareImmagini("Immagini/EquipLucy/SfondoOggetto.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False)
    sconosciutoEquipMenu = funzionePerCaricareImmagini("Immagini/Oggetti/SconosciutoEquip.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False)
    sconosciutoOggettoMenu1 = funzionePerCaricareImmagini("Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sconosciutoOggettoMenu2 = funzionePerCaricareImmagini("Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    sconosciutoOggettoMenu3 = funzionePerCaricareImmagini("Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    sconosciutoOggettoIcoMenu = funzionePerCaricareImmagini("Immagini/Oggetti/SconosciutoIco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, False)

    # img mappe
    imgMappa1A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa1B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa2A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa2B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa3A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa3B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa4A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa4B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa5A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa5B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa6A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa6B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa7A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa7B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa8A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa8B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa9A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa9B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa10A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa10B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa11A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa11B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa12A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa12B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa13A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa13B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa14A = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa14B = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgOmbreggiaturaContorniMappaMenu = funzionePerCaricareImmagini("Immagini/DecorazioniMenu/Mappe/OmbreggiaturaContorniMappaMenu.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "Cinghiale", "LupoGrigio", "LupoNero", "LupoBianco", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = funzionePerCaricareImmagini("Immagini/Nemici/NemicoAvvelenato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = funzionePerCaricareImmagini("Immagini/Nemici/NemicoAppiccicato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png", GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png", GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = funzionePerCaricareImmagini("Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = funzionePerCaricareImmagini("Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = funzionePerCaricareImmagini("Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni

    schemataDiCaricamento = loadImage("Immagini/DecorazioniMenu/SchermataDiCaricamento.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
