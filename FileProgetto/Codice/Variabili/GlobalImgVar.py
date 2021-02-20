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
    puntatore = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/Puntatore.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True)
    puntatorevecchio = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/Puntatorevecchio.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True)
    puntatIn = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/InquadraCVin.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatOut = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/InquadraCVout.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatSfo = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/sfondoOggettoLanciato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatDif = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Difesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatAtt = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Attacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatArc = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/AttaccoDistanza.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatPor = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/ApriChiudiPorta.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatCof = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/ApriCofanetto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatAnalisi = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/AnalizzaColco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBom = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto6Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBoV = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto7Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatEsc = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto8Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBoA = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto9Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatBoP = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto10Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSu = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriOggettiSu.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriGiu = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriOggettiGiu.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatDialoghi = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/IcoDialogo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreInquadraNemici = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/InquadraNemicoSelezionato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniDestra = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestra.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniSinistra = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistra.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniDestraBloccato = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestraBloccato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    puntatoreImpostazioniSinistraBloccato = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistraBloccato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # immagini personaggio
    persw = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswb = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persa = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persab = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perso = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persob = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    perss = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssb = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persd = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdb = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssm = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdm = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio2mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio2movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio2movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persam = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio3mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persamb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio3movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persamb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio3movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswm = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio4mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio4movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio4movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmbAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio4movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persambAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio3movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmbAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmbAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio2movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persmbDifesa = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/PersonaggiomovbDifesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persAvvele = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/PersonaggioAvvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persoLucy1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persoLucy2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy2/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persobLucy = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Lucy1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persoFraMaggiore = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persobFraMaggiore = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/FratelloMaggiore/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)

    # immagini robot
    robow = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboa = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboo1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    roboo2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    robos = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    robod = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    robomo = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot0.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    robodp = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot2p.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboap = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/Robot3p.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    armrobmo = funzionePerCaricareImmagini('Risorse/Immagini/EquipRobo/Batteria00.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    roboSurrisc = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Colco/RobotSurriscaldato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgDanneggiamentoCausaColco = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img menu mercante
    mercanteMenu = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Mercante/MercanteDialogo.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    scorriSuGiu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccato = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccatoGiu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccatoSu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoSu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoDialogoMercante = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/SfondoDialogoMercante.png', GlobalHWVar.gpx * 9.5, GlobalHWVar.gpy * 4.5, False)
    faretra1Menu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Faretra1Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra2Menu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Faretra2Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra3Menu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Faretra3Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    frecciaMenu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/FrecciaMenu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)

    # sfondi
    sfondoRallo = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoRallo.png', GlobalHWVar.gpx * 6, GlobalHWVar.gpy, False)
    sfondoColco = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoColco.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy, False)
    sfondoMostro = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoNemici.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy, False)
    sfondoEsche = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoEsche.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoStartBattaglia = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SfondoStartBattaglia.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 10, False)
    sfondoTriangolinoAltoDestra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloAltoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoAltoSinistra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoDestra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloBassoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoSinistra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # status
    appiccicoso = funzionePerCaricareImmagini('Risorse/Immagini/Status/Appiccicoso.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    avvelenatoMenu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Avvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    avvelenato = funzionePerCaricareImmagini('Risorse/Immagini/Status/Avvelenato.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    surriscaldatoMenu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Surriscaldato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    surriscaldato = funzionePerCaricareImmagini('Risorse/Immagini/Status/Surriscaldato.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    attaccopiuMenu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Attaccopiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    attaccopiu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Attaccopiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    difesapiuMenu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Difesapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    difesapiu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Difesapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    velocitapiuMenu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Velocitapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    velocitapiu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Velocitapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    efficienzapiuMenu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Efficienzapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    efficienzapiu = funzionePerCaricareImmagini('Risorse/Immagini/Status/Efficienzapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)
    imgNumFrecce = funzionePerCaricareImmagini('Risorse/Immagini/Status/NumFrecce.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True)

    # menu alto destra
    sfochiaveocchio = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/SfondoOcchioChiave.png", GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, False)
    occhioape = funzionePerCaricareImmagini('Risorse/Immagini/Status/OcchioAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    occhiochiu = funzionePerCaricareImmagini('Risorse/Immagini/Status/OcchioChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    chiaveroboacc = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/ChiaveColcoAcc.png', GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True)
    chiaverobospe = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/ChiaveColcoSpe.png', GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, True)

    # oggetti sulla schermata
    esche = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto8Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sacchettoDenaroStart = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SacchettoDenaroSinistra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaroMercante = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SacchettoDenaroDestra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart0 = funzionePerCaricareImmagini('Risorse/Immagini/EquipLucy/Faretre/Faretra0Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart1 = funzionePerCaricareImmagini('Risorse/Immagini/EquipLucy/Faretre/Faretra1Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart2 = funzionePerCaricareImmagini('Risorse/Immagini/EquipLucy/Faretre/Faretra2Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart3 = funzionePerCaricareImmagini('Risorse/Immagini/EquipLucy/Faretre/Faretra3Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaro = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SacchettoDenaroIco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaLanciata = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Freccia.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # cofanetti
    cofaniaper = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/CofanettoAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    cofanichiu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/CofanettoChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfocontcof = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SfondoContenutoCofanetto.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 3, False)

    # immagini salvataggi
    s1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Salvataggi/S1.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, False)
    s2 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Salvataggi/S2.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, False)
    s3 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Salvataggi/S3.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, False)

    # caselle attaccabili
    campoattaccabileRallo1 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    campoattaccabileRallo2 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False)
    campoattaccabileRallo3 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    campoattaccabileRallo4 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False)
    campoattaccabileRallo5 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Campoattaccabile2.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    campoattaccabileRobo = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Campoattaccabile3.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    caselleattaccabiliRobo = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CaselleattaccabiliRobo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    caselleattaccabilimostro = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Caselleattaccabilimostro.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    caselleattaccabili = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/Caselleattaccabili.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # aumento livello
    saliliv = funzionePerCaricareImmagini('Risorse/Immagini/Status/Levelup/Saliliv.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    saliliv1 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Levelup/Saliliv1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    saliliv2 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Levelup/Saliliv2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    vetImgSpadeMenu = []
    vetImgArchiMenu = []
    vetImgArmatureMenu = []
    vetImgScudiMenu = []
    vetImgGuantiMenu = []
    vetImgCollaneMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadeMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Spade/Spada%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArchiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Archi/Arco%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArmatureMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Armature/Armatura%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgScudiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Scudi/Scudo%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgGuantiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Guanti/Guanti%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgCollaneMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Collane/Collana%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        contatoreGlobale += 1
    imgGambitSconosciuta = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/GrafGambit/Sconosciuto.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    vetImgCondizioniMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/GrafGambit/GrafCondizioni/Condizione%i.png" % contatoreGlobale, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False))
        contatoreGlobale += 1
    vetImgTecnicheMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/GrafGambit/GrafTecniche/Tecnica%i.png" % contatoreGlobale, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetIcoBatterieMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False))
        vetImgOggettiMercante.append(funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False))
        vetImgOggettiStart.append(funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False))
        vetIcoOggettiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
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
        vetImgSpadePixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Spade/Spada%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArchiPixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Archi/Arco%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArmaturePixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Armature/Armatura%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgScudiPixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Scudi/Scudo%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgGuantiPixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Guanti/Guanti%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgCollanePixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/Collane/Collana%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/Bomba.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgAnimaBombaVeleno = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/BombaVeleno.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaBombaAppiccicosa = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/BombaAppiccicosa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaBombaPotenziata = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/BombaPotenziata.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    imgAnimaPozione1 = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/Pozione1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaPozione2 = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/Pozione2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaMedicina1 = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/Medicina1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaMedicina2 = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/Medicina2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgAnimaCaricabatterie = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniOggetti/Caricabatterie.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img animazioni tecniche
    imgDanneggiamentoColco = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniTecniche/Danneggiamento.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            img2 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            img2 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            img2 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            img2 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            imgSelf = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%sAnimaSelf.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(imgSelf)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True)
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, True)
            img2 = funzionePerCaricareImmagini("Risorse/Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, True)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniTecniche/FrecciaLanciata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaEletttricaLanciataP = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniTecniche/FrecciaLanciata+.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaEletttricaLanciataPP = funzionePerCaricareImmagini('Risorse/Immagini/AnimazioniTecniche/FrecciaLanciata++.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img sfondi dialoghi
    sfondoDialoghi = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SfondoSotto.png', GlobalHWVar.gsx, GlobalHWVar.gsy // 3, False)

    # img tutorial
    tutorialTastieraInGioco = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/TastieraInGioco.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialTastieraInMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/TastieraInMenu.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialMouse = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/Mouse.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialControllerInGioco = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ControllerInGioco.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialControllerInMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ControllerInMenu.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    impostazioniController = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoController.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroce = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroce.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCerchio = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCerchio.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerQuadrato = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerQuadrato.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerTriangolo = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerTriangolo.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerL1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerL1.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerR1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerR1.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerStart = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerStart.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)

    # img grafiche / dialoghi
    persGrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/NeilGrafMenu.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    lucy1GrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/Lucy1GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    lucy2GrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/Lucy2GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    fraMaggioreGrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf0 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf0.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf1b = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf2 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf2b = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf3 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf3.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf4 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    imgDialogoFraMaggiore = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/FratelloMaggioreDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoLucy1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/Lucy1Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoLucy2 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/Lucy2Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgFraMaggioreMenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/FratelloMaggioreMenu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgLucy1MenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Lucy1Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgLucy2MenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Lucy2Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)

    # indicatori vita
    indvita = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Indvita.png', 0, 0, True)
    fineindvita = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/FineIndVita.png', GlobalHWVar.gpx // 12, GlobalHWVar.gpy // 4, True)
    vitanemico00 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico00.png', 0, 0, True)
    vitanemico0 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico0.png', 0, 0, True)
    vitanemico1 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico1.png', 0, 0, True)
    vitanemico2 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico2.png', 0, 0, True)
    vitanemico3 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico3.png', 0, 0, True)
    vitanemico4 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico4.png', 0, 0, True)
    vitanemico5 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico5.png', 0, 0, True)
    vitanemico6 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico6.png', 0, 0, True)
    vitanemico7 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico7.png', 0, 0, True)
    vitanemico8 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico8.png', 0, 0, True)
    vitanemico9 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitanemico9.png', 0, 0, True)
    vitapersonaggio = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitapersonaggio.png', 0, 0, True)
    vitarobo = funzionePerCaricareImmagini('Risorse/Immagini/Status/Barrevita/Vitarobo.png', 0, 0, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = funzionePerCaricareImmagini("Risorse/Immagini/EquipLucy/SfondoOggetto.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False)
    sconosciutoEquipMenu = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/SconosciutoEquip.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False)
    sconosciutoOggettoMenu1 = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sconosciutoOggettoMenu2 = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    sconosciutoOggettoMenu3 = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    sconosciutoOggettoIcoMenu = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/SconosciutoIco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, False)

    # img mappe
    imgMappa1A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa1B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu1.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa2A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa2B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu2.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa3A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa3B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu3.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa4A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa4B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu4.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa5A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa5B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu5.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa6A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa6B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu6.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa7A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa7B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu7.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa8A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa8B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu8.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa9A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa9B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu9.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa10A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa10B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu10.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa11A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa11B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu11.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa12A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa12B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu12.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa13A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa13B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu13.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgMappa14A = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgMappa14B = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/MappaMenu14.png", GlobalHWVar.gpx * 50, GlobalHWVar.gpy * 35, False)
    imgOmbreggiaturaContorniMappaMenu = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/OmbreggiaturaContorniMappaMenu.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "Cinghiale", "LupoGrigio", "LupoNero", "LupoBianco", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/NemicoAvvelenato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/NemicoAppiccicato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png", GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png", GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni

    schemataDiCaricamento = loadImage("Risorse/Immagini/DecorazioniMenu/SchermataDiCaricamento.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
