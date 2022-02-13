# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


# dichiaro le variabili globali della funzione loadImgs
global puntatore
global puntatorevecchio
global puntatIn
global puntatOut
global puntatSfo
global puntatDif
global puntatDifPv
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
global pappagalloMenuMercante
global saraMenuMercante
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
global imgSaltaTurno
global imgSaltaTurnoCliccato
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
global imgCasellaObbiettivoAnalizzaColco
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
global impostaControllerSelect
global impostaControllerCroceDirezionale
global persGrafMenu
global sara1GrafMenu
global sara2GrafMenu
global saraSconvoltaGrafMenu
global sara3GrafMenu
global saraAssonnataPostCenaCastello
global saraAssonnataCastelloPostCenaCastello
global saraSconvoltaCastelloGrafMenu
global fraMaggioreGrafMenu
global robograf0
global robograf1
global robograf1b
global robograf2
global robograf2b
global robograf3
global robograf4
global imgDialogoFraMaggiore
global imgDialogoSara1
global imgDialogoSara2
global imgDialogoSara3
global imgDialogoSaraAssonnata
global imgDialogoSaraSconvolta
global imgDialogoSaraOcchiChiusi
global imgDialogoSaraAssonnataCastello
global imgDialogoSaraAssonnataPostCenaCastello
global imgDialogoSaraAssonnataCastelloPostCenaCastello
global imgDialogoSaraSconvoltaCastello
global imgDialogoColco
global imgFraMaggioreMenuOggetti
global imgSara1MenuOggetti
global imgSara2MenuOggetti
global imgSara3MenuOggetti
global dictImgDialoghiPersonaggiOggettoSpecifici
global dictImgPersonaggiOggettoSpecifici
global sfondoOggettoMenu
global sconosciutoEquipMenu
global sconosciutoOggettoMenu1
global sconosciutoOggettoMenu2
global sconosciutoOggettoMenu3
global sconosciutoOggettoIcoMenu
global imgOmbreggiaturaContorniMappaMenu
global dictionaryImgNemici
global dictImgCampiVisiviNemici
global dictImgNemiciDiario
global dictionaryImgPersonaggi
global dictImgPersonaggiDiario
global fraMaggioreDiario
global roboDiario
global ralloDiario
global neilSconosciutoDiario
global pappagalloDiario
global imgDanneggiamentoCausaRallo
global imgDanneggiamentoCausaColco
global persoSara1
global persoSara2
global persoSara3
global persobSara
global persoFraMaggiore
global persobFraMaggiore
global schemataDiCaricamento
global sfumaturaCaricamentoMenuPrincipale
global casellaChiara
global casellaScura
global casellaOscurata
global vetImgSpadeInGame
global vetImgArchiInGame
global vetImgArmatureInGame
global vetImgScudiInGame
global vetImgGuantiInGame
global vetImgCollaneInGame
global vetImgFaretreInGame
global vetImgArmRobInGame
global imgDiarioChiusoMenu
global imgDiarioApertoMenu
global imgBicchiereConAcqua
global imgChiaveRipostiglio
global imgChiaveStanzaCasaDavid
global imgCertificazioneResidenza
global imgImpoPietra
global imgChiaveStanzaCastello
global imgListaStrumentiStudioImpo
global imgChiaveAvamposto
global imgStrumentiDiRod
global imgChiaveUfficioNeil

numImgTotali = 1790
def caricaImmagineMostrandoAvanzamento(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True, imgImpenetrabile=False):
    global numImgCaricataTemp
    immagine = CaricaFileProgetto.loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha, imgImpenetrabile)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 0.5))
    numImgCaricataTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 30.0 / numImgTotali) * numImgCaricataTemp
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(caricamentoCompiuto), GlobalHWVar.gpy * 0.5))
    GlobalHWVar.aggiornaSchermo()
    return immagine
def caricaImmagineCambioRisoluzione(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True, imgImpenetrabile=False):
    global numImgCaricataTemp
    immagine = CaricaFileProgetto.loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha, imgImpenetrabile)
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
    global puntatDifPv
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
    global pappagalloMenuMercante
    global saraMenuMercante
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
    global imgSaltaTurno
    global imgSaltaTurnoCliccato
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
    global imgCasellaObbiettivoAnalizzaColco
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
    global impostaControllerSelect
    global impostaControllerCroceDirezionale
    global persGrafMenu
    global sara1GrafMenu
    global sara2GrafMenu
    global saraSconvoltaGrafMenu
    global sara3GrafMenu
    global saraAssonnataPostCenaCastello
    global saraAssonnataCastelloPostCenaCastello
    global saraSconvoltaCastelloGrafMenu
    global fraMaggioreGrafMenu
    global robograf0
    global robograf1
    global robograf1b
    global robograf2
    global robograf2b
    global robograf3
    global robograf4
    global imgDialogoFraMaggiore
    global imgDialogoSara1
    global imgDialogoSara2
    global imgDialogoSara3
    global imgDialogoSaraAssonnata
    global imgDialogoSaraSconvolta
    global imgDialogoSaraOcchiChiusi
    global imgDialogoSaraAssonnataCastello
    global imgDialogoSaraAssonnataPostCenaCastello
    global imgDialogoSaraAssonnataCastelloPostCenaCastello
    global imgDialogoSaraSconvoltaCastello
    global imgDialogoColco
    global imgFraMaggioreMenuOggetti
    global imgSara1MenuOggetti
    global imgSara2MenuOggetti
    global imgSara3MenuOggetti
    global dictImgDialoghiPersonaggiOggettoSpecifici
    global dictImgPersonaggiOggettoSpecifici
    global sfondoOggettoMenu
    global sconosciutoEquipMenu
    global sconosciutoOggettoMenu1
    global sconosciutoOggettoMenu2
    global sconosciutoOggettoMenu3
    global sconosciutoOggettoIcoMenu
    global imgOmbreggiaturaContorniMappaMenu
    global dictionaryImgNemici
    global dictImgCampiVisiviNemici
    global dictImgNemiciDiario
    global dictionaryImgPersonaggi
    global dictImgPersonaggiDiario
    global fraMaggioreDiario
    global roboDiario
    global ralloDiario
    global neilSconosciutoDiario
    global pappagalloDiario
    global imgDanneggiamentoCausaRallo
    global imgDanneggiamentoCausaColco
    global persoSara1
    global persoSara2
    global persoSara3
    global persobSara
    global persoFraMaggiore
    global persobFraMaggiore
    global schemataDiCaricamento
    global sfumaturaCaricamentoMenuPrincipale
    global casellaChiara
    global casellaScura
    global casellaOscurata
    global vetImgSpadeInGame
    global vetImgArchiInGame
    global vetImgArmatureInGame
    global vetImgScudiInGame
    global vetImgGuantiInGame
    global vetImgCollaneInGame
    global vetImgFaretreInGame
    global vetImgArmRobInGame
    global imgDiarioChiusoMenu
    global imgDiarioApertoMenu
    global imgBicchiereConAcqua
    global imgChiaveRipostiglio
    global imgChiaveStanzaCasaDavid
    global imgCertificazioneResidenza
    global imgImpoPietra
    global imgChiaveStanzaCastello
    global imgListaStrumentiStudioImpo
    global imgChiaveAvamposto
    global imgStrumentiDiRod
    global imgChiaveUfficioNeil

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
    puntatDifPv = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/DifesaPv.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
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
    imgCasellaObbiettivoAnalizzaColco = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Puntatori/ObiettivoAnalizzaColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # immagini personaggio
    persw = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswb = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persa = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persab = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perso = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persob = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    perss = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssb = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persd = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdb = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssm = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdm = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio2mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio2movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio2movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persam = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio3mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persamb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio3movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persamb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio3movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswm = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio4mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmb1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio4movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmb2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio4movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perswmbAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio4movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persambAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio3movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    perssmbAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persdmbAttacco = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio2movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persmbDifesa = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/PersonaggiomovbDifesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persAvvele = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/PersonaggioAvvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    persoSara1 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persoSara2 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara2/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persoSara3 = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara3/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
    persobSara = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Sara1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True)
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

    # immagini equipaggiamenti
    vetImgSpadeInGame = []
    vetImgArchiInGame = []
    vetImgArmatureInGame = []
    vetImgScudiInGame = []
    vetImgGuantiInGame = []
    vetImgCollaneInGame = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        # arma
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy * 2), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx * 2, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx * 2, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy * 2), flags=pygame.SRCALPHA))
        else:
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iwMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iwMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iaMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iaMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%isMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%isMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%idMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%idMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%isAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iaAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%idAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iwAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
        vetImgSpadeInGame.append(vetAnimaTemp)
        # arco
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy * 2), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx * 2, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx * 2, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy * 2), flags=pygame.SRCALPHA))
        else:
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%isAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%iaAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%idAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%iwAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
        vetImgArchiInGame.append(vetAnimaTemp)
        # armatura
        vetAnimaTemp = []
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Armature/Armatura%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Armature/Armatura%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Armature/Armatura%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgArmatureInGame.append(vetAnimaTemp)
        # scudo
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
        else:
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%iDifesa.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgScudiInGame.append(vetAnimaTemp)
        # guanti
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
        else:
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iwMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iwMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iaMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iaMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%isMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%isMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%idMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%idMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%isAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iaAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%idAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iwAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iDifesa.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgGuantiInGame.append(vetAnimaTemp)
        # collana
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
        else:
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Collane/Collana%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Collane/Collana%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Collane/Collana%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgCollaneInGame.append(vetAnimaTemp)
        contatoreGlobale += 1
    vetImgFaretreInGame = []
    contatoreGlobale = 0
    while contatoreGlobale < 4:
        # faretra
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
            vetAnimaTemp.append(pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA))
        else:
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Faretre/Faretra%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Faretre/Faretra%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Faretre/Faretra%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Faretre/Faretra%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgFaretreInGame.append(vetAnimaTemp)
        contatoreGlobale += 1
    vetImgArmRobInGame = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        # armatura robot
        vetAnimaTemp = []
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipRobo/Batteria%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipRobo/Batteria%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipRobo/Batteria%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgArmRobInGame.append(vetAnimaTemp)
        contatoreGlobale += 1

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgDanneggiamentoCausaColco = funzionePerCaricareImmagini("Risorse/Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img menu mercante
    mercanteMenu = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Mercante/MercanteDialogo.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    pappagalloMenuMercante = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/PappagalloGrafMenuMercante.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    saraMenuMercante = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/Sara2Dialogo.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    scorriSuGiu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccato = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccatoGiu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    scorriSuGiuBloccatoSu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoSu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoDialogoMercante = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/SfondoDialogoMercante.png', GlobalHWVar.gpx * 9.5, GlobalHWVar.gpy * 4.5, False, imgImpenetrabile=True)
    faretra1Menu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Faretra1Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra2Menu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Faretra2Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra3Menu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Faretra3Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    frecciaMenu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/FrecciaMenu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)

    # sfondi
    sfondoRallo = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoRallo.png', GlobalHWVar.gpx * 6, GlobalHWVar.gpy, False, imgImpenetrabile=True)
    sfondoColco = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoColco.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy, False, imgImpenetrabile=True)
    sfondoMostro = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoNemici.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy, False, imgImpenetrabile=True)
    sfondoEsche = funzionePerCaricareImmagini('Risorse/Immagini/Status/SfondoEsche.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoStartBattaglia = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SfondoStartBattaglia.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 10, False, imgImpenetrabile=True)
    sfondoTriangolinoAltoDestra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloAltoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoAltoSinistra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoDestra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloBassoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoSinistra = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    casellaChiara = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    casellaChiara.fill((0, 0, 0, 0))
    casellaScura = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    casellaScura.fill((0, 0, 0, 10))
    casellaOscurata = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    casellaOscurata.fill((0, 0, 0, 100))

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
    sfochiaveocchio = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/SfondoOcchioChiave.png", GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, False, imgImpenetrabile=True)
    occhioape = funzionePerCaricareImmagini('Risorse/Immagini/Status/OcchioAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    occhiochiu = funzionePerCaricareImmagini('Risorse/Immagini/Status/OcchioChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    chiaveroboacc = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/ChiaveColcoAcc.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    chiaverobospe = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/ChiaveColcoSpe.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgSaltaTurno = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SaltaTurno.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgSaltaTurnoCliccato = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SaltaTurnoCliccato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # oggetti sulla schermata
    esche = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Oggetto8Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sacchettoDenaroStart = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SacchettoDenaroSinistra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaroMercante = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SacchettoDenaroDestra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart0 = funzionePerCaricareImmagini('Risorse/Immagini/EquipSara/Faretre/Faretra0Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart1 = funzionePerCaricareImmagini('Risorse/Immagini/EquipSara/Faretre/Faretra1Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart2 = funzionePerCaricareImmagini('Risorse/Immagini/EquipSara/Faretre/Faretra2Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart3 = funzionePerCaricareImmagini('Risorse/Immagini/EquipSara/Faretre/Faretra3Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaro = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SacchettoDenaroIco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgFrecciaLanciata = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/Freccia.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # cofanetti
    cofaniaper = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/CofanettoAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    cofanichiu = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/CofanettoChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfocontcof = funzionePerCaricareImmagini('Risorse/Immagini/Oggetti/SfondoContenutoCofanetto.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 3, False)

    # caselle attaccabili
    campoattaccabileRallo1 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    campoattaccabileRallo2 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False)
    campoattaccabileRallo3 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    campoattaccabileRallo4 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False)
    campoattaccabileRallo5 = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    campoattaccabileRobo = funzionePerCaricareImmagini('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRobo.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False)
    caselleattaccabiliRobo = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    caselleattaccabiliRobo.fill((0, 0, 130, 100))
    caselleattaccabilimostro = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    caselleattaccabilimostro.fill((130, 0, 0, 100))
    caselleattaccabili = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    caselleattaccabili.fill((0, 0, 0, 100))

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
        vetImgSpadeMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArchiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArmatureMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Armature/Armatura%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgScudiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgGuantiMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgCollaneMenu.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Collane/Collana%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
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
        vetImgSpadePixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArchiPixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArmaturePixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgScudiPixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgGuantiPixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgCollanePixellate.append(funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
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
    impostaControllerSelect = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerSelect.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)

    # img grafiche / dialoghi
    sfondoDialoghi = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SfondoSotto.png', GlobalHWVar.gsx, GlobalHWVar.gsy // 3, False, imgImpenetrabile=True)
    persGrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/NeilGrafMenu.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    sara1GrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/Sara1GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    sara2GrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/Sara2GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    saraSconvoltaGrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/SaraSconvoltaGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    sara3GrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/Sara3GrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    saraAssonnataPostCenaCastello = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/SaraAssonnataPostCenaCastelloGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    saraAssonnataCastelloPostCenaCastello = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/SaraAssonnataCastelloPostCenaCastelloGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    saraSconvoltaCastelloGrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/SaraSconvoltaCastelloGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    fraMaggioreGrafMenu = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf0 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf0.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf1b = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf2 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf2b = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf3 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf3.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf4 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    imgDialogoFraMaggiore = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/FratelloMaggioreDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSara1 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/Sara1Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSara2 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/Sara2Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSara3 = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/Sara3Dialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraAssonnata = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraAssonnataDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraSconvolta = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraScossaDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraOcchiChiusi = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraOcchiChiusiDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraAssonnataCastello = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraAssonnataCastelloDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraAssonnataPostCenaCastello = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraAssonnataDialogoPostCenaCastello.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraAssonnataCastelloPostCenaCastello = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraAssonnataCastelloDialogoPostCenaCastello.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoSaraSconvoltaCastello = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/SaraScossaCastelloDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgDialogoColco = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/RobotDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    imgFraMaggioreMenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/FratelloMaggioreMenu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgSara1MenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Sara1Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgSara2MenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Sara2Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    imgSara3MenuOggetti = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Sara3Menu.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True)
    dictImgDialoghiPersonaggiOggettoSpecifici = {}
    dictImgDialoghiPersonaggiOggettoSpecifici["OggettoDictCadavereSoldatoDialogo"] = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/Dialoghi/CadavereSoldatoDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    dictImgPersonaggiOggettoSpecifici = {}
    dictImgPersonaggiOggettoSpecifici["OggettoDictCadavereSoldato1"] = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Oggetti/CadavereSoldatoCastello1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    dictImgPersonaggiOggettoSpecifici["OggettoDictCadavereSoldato2"] = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Oggetti/CadavereSoldatoCastello2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    dictImgPersonaggiOggettoSpecifici["OggettoDictCadavereSoldato3"] = funzionePerCaricareImmagini('Risorse/Immagini/Personaggi/Oggetti/CadavereSoldatoCastello3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = funzionePerCaricareImmagini("Risorse/Immagini/EquipSara/SfondoOggetto.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False)
    sconosciutoEquipMenu = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/SconosciutoEquip.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False)
    sconosciutoOggettoMenu1 = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sconosciutoOggettoMenu2 = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    sconosciutoOggettoMenu3 = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    sconosciutoOggettoIcoMenu = funzionePerCaricareImmagini("Risorse/Immagini/Oggetti/SconosciutoIco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, False)

    # img personaggi
    vettoreNomiPersonaggi = ["Alieno1", "Alieno2", "AssistBiblioteca", "Bibliotecario", "CaneCasa", "FiglioUfficiale", "GuardiaCitta", "Madre", "MadreUfficiale", "Mercante", "Neil", "Padre", "PadreUfficialeCasa", "PadreUfficialeServizio", "Pazzo1", "Pazzo2", "Ragazza1", "Ragazza2", "Ragazza3", "Ragazzo1", "Ragazzo2", "Ragazzo3", "ServoArco", "ServoDavid", "ServoLancia", "ServoSpada", "FratelloMaggiore"]
    dictionaryImgPersonaggi = {}
    for nomePersonaggi in vettoreNomiPersonaggi:
        dictionaryImgPosizioni = {}
        imgW = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "W.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "A.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "S.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "D.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "WMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "WMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "AMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "AMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "SMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "SMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "DMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "DMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgDialogo = funzionePerCaricareImmagini("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "Dialogo.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, True)
        dictionaryImgPosizioni["imgDialogo"] = imgDialogo

        dictionaryImgPersonaggi[nomePersonaggi] = dictionaryImgPosizioni
    dictImgPersonaggiDiario = {}
    for nomePersonaggi in vettoreNomiPersonaggi:
        if nomePersonaggi != "AssistBiblioteca" and nomePersonaggi != "GuardiaCitta" and nomePersonaggi != "Ragazza1" and nomePersonaggi != "Ragazza2" and nomePersonaggi != "Ragazza3" and nomePersonaggi != "Ragazzo1" and nomePersonaggi != "Ragazzo2" and nomePersonaggi != "Ragazzo3" and nomePersonaggi != "ServoArco" and nomePersonaggi != "ServoDavid" and nomePersonaggi != "ServoLancia" and nomePersonaggi != "ServoSpada" and nomePersonaggi != "FratelloMaggiore":
            imgPersonaggi = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/" + nomePersonaggi + "GrafMenu.png", GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
            dictImgPersonaggiDiario[nomePersonaggi] = imgPersonaggi
    fraMaggioreDiario = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    roboDiario = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGrafMenuDiario.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    ralloDiario = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/SaraGrafMenuDiario.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    neilSconosciutoDiario = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/NeilSconosciutoGrafMenu.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    pappagalloDiario = funzionePerCaricareImmagini('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/PappagalloGrafMenu.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "LupoGrigio", "LupoBianco", "LupoNero", "Cinghiale", "Cittadino1", "Cittadino3", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
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
    dictImgCampiVisiviNemici = {}
    raggio = 2
    while raggio <= 8:
        dictImgCampiVisiviNemici[str(raggio)] = funzionePerCaricareImmagini("Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileMostro.png", (GlobalHWVar.gpx * raggio * 2) + GlobalHWVar.gpx, (GlobalHWVar.gpy * raggio * 2) + GlobalHWVar.gpy, True)
        raggio += 1
    dictImgNemiciDiario = {}
    for nomeNemico in vettoreNomiNemici:
        imgNemico = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/DisegniNemici/" + nomeNemico + "Graf.png", GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
        dictImgNemiciDiario[nomeNemico] = imgNemico

    # img menu
    schemataDiCaricamento = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/SchermataDiCaricamento.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
    sfumaturaCaricamentoMenuPrincipale = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/OmbreggiaturaCaricamentoMenuPrincipale.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
    imgOmbreggiaturaContorniMappaMenu = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Mappe/OmbreggiaturaContorniMappaMenu.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
    imgDiarioChiusoMenu = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/DiarioChiusoMenu.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgDiarioApertoMenu = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/DiarioApertoMenu.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)

    # img oggetti speciali
    imgBicchiereConAcqua = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/BicchiereConAcqua.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveRipostiglio = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveRipostiglio.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveStanzaCasaDavid = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveStanzaCasaDavid.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgCertificazioneResidenza = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/CertificazioneResidenza.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgImpoPietra = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ImpoPietra.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveStanzaCastello = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveStanzaCastello.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgListaStrumentiStudioImpo = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ListaStrumentiStudioImpo.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveAvamposto = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveAvampostoDiRod.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgStrumentiDiRod = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/StrumentiDiRod.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveUfficioNeil = funzionePerCaricareImmagini("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveUfficioNeil.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
