# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.Variabili.ImageClass as ImageClass


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
global sfondoLogoInterazioneNonAttivo
global sfondoLogoInterazioneAttivo
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
global imgModInterazione
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
global impostaControllerCroceDirezionale_su
global impostaControllerCroceDirezionale_giu
global impostaControllerCroceDirezionale_destra
global impostaControllerCroceDirezionale_sinistra
global impostazioniTastiera
global robograf1
global robograf2
global robograf2b
global robograf4
global imgDialogoColco
global dictImgDialoghiPersonaggiOggettoSpecifici
global dictImgPersonaggiOggettoSpecifici
global sfondoOggettoMenu
global sconosciutoEquipMenu
global sconosciutoOggettoMenu1
global sconosciutoOggettoMenu2
global sconosciutoOggettoMenu3
global sconosciutoOggettoIcoMenu
global imgOmbreggiaturaContorniMappaMenu
global vettoreNomiNemici
global dictionaryImgNemici
global dictImgCampiVisiviNemici
global dictImgNemiciDiario
global dictionaryImgPersonaggi
global dictImgPersonaggiDiario
global fraMaggioreDiario
global roboDiario
global imgProtagonistaDiario
global neilSconosciutoDiario
global pappagalloDiario
global imgDanneggiamentoCausaRallo
global imgDanneggiamentoCausaColco
global persoSara1
global persoSara2
global persoSara3
global persoSara4
global persoSara5
global persoSara6
global persobSara
global persobSara5
global persoFraMaggiore
global persobFraMaggiore
global persoRod
global persobRod
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
global imgEvidenziaInterzaione
global imgEvidenziaInterzaioneCompiuta
global imgEvidenziaUsciteStanzaSu
global imgEvidenziaUsciteStanzaGiu
global imgEvidenziaUsciteStanzaDestra
global imgEvidenziaUsciteStanzaSinistra
global imgEvidenziaUsciteStanzaSuBloccate
global imgEvidenziaUsciteStanzaGiuBloccate
global imgEvidenziaUsciteStanzaDestraBloccate
global imgEvidenziaUsciteStanzaSinistraBloccate
global imgChiaveSeminterratoPalazzoRod
global imgBacchePv

numImgTotali = 267
def caricaImmagineMostrandoAvanzamento(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True, imgImpenetrabile=False):
    global numImgCaricataTemp
    immagine = CaricaFileProgetto.loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha, imgImpenetrabile)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 0.5))
    numImgCaricataTemp += 1
    # print(numImgCaricataTemp)
    caricamentoCompiuto = (GlobalHWVar.gpx * 20.0 / numImgTotali) * numImgCaricataTemp
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
    global sfondoLogoInterazioneNonAttivo
    global sfondoLogoInterazioneAttivo
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
    global imgModInterazione
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
    global impostaControllerCroceDirezionale_su
    global impostaControllerCroceDirezionale_giu
    global impostaControllerCroceDirezionale_destra
    global impostaControllerCroceDirezionale_sinistra
    global impostazioniTastiera
    global robograf1
    global robograf2
    global robograf2b
    global robograf4
    global imgDialogoColco
    global dictImgDialoghiPersonaggiOggettoSpecifici
    global dictImgPersonaggiOggettoSpecifici
    global sfondoOggettoMenu
    global sconosciutoEquipMenu
    global sconosciutoOggettoMenu1
    global sconosciutoOggettoMenu2
    global sconosciutoOggettoMenu3
    global sconosciutoOggettoIcoMenu
    global imgOmbreggiaturaContorniMappaMenu
    global vettoreNomiNemici
    global dictionaryImgNemici
    global dictImgCampiVisiviNemici
    global dictImgNemiciDiario
    global dictionaryImgPersonaggi
    global dictImgPersonaggiDiario
    global fraMaggioreDiario
    global roboDiario
    global imgProtagonistaDiario
    global neilSconosciutoDiario
    global pappagalloDiario
    global imgDanneggiamentoCausaRallo
    global imgDanneggiamentoCausaColco
    global persoSara1
    global persoSara2
    global persoSara3
    global persoSara4
    global persoSara5
    global persoSara6
    global persobSara
    global persobSara5
    global persoFraMaggiore
    global persobFraMaggiore
    global persoRod
    global persobRod
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
    global imgEvidenziaInterzaione
    global imgEvidenziaInterzaioneCompiuta
    global imgEvidenziaUsciteStanzaSu
    global imgEvidenziaUsciteStanzaGiu
    global imgEvidenziaUsciteStanzaDestra
    global imgEvidenziaUsciteStanzaSinistra
    global imgEvidenziaUsciteStanzaSuBloccate
    global imgEvidenziaUsciteStanzaGiuBloccate
    global imgEvidenziaUsciteStanzaDestraBloccate
    global imgEvidenziaUsciteStanzaSinistraBloccate
    global imgChiaveSeminterratoPalazzoRod
    global imgBacchePv

    if cambioRisoluzione:
        funzionePerCaricareImmagini = caricaImmagineCambioRisoluzione
    else:
        funzionePerCaricareImmagini = caricaImmagineMostrandoAvanzamento

    # puntatore
    puntatore = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/Puntatore.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True, forceLoad=funzionePerCaricareImmagini)
    puntatorevecchio = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/Puntatorevecchio.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True, forceLoad=funzionePerCaricareImmagini)
    puntatIn = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Puntatori/InquadraCVin.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatOut = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Puntatori/InquadraCVout.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatSfo = ImageClass.ImageClass('Risorse/Immagini/Oggetti/sfondoOggettoLanciato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatDif = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Difesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatDifPv = ImageClass.ImageClass('Risorse/Immagini/Oggetti/DifesaPv.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatAtt = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Attacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatArc = ImageClass.ImageClass('Risorse/Immagini/Oggetti/AttaccoDistanza.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatPor = ImageClass.ImageClass('Risorse/Immagini/Oggetti/ApriChiudiPorta.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatCof = ImageClass.ImageClass('Risorse/Immagini/Oggetti/ApriCofanetto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatAnalisi = ImageClass.ImageClass('Risorse/Immagini/Oggetti/AnalizzaColco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatBom = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Oggetto6Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatBoV = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Oggetto7Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatEsc = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Oggetto8Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatBoA = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Oggetto9Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatBoP = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Oggetto10Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    scorriSu = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriOggettiSu.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    scorriGiu = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriOggettiGiu.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatDialoghi = ImageClass.ImageClass('Risorse/Immagini/Oggetti/IcoDialogo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatoreInquadraNemici = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/InquadraNemicoSelezionato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatoreImpostazioniDestra = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestra.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatoreImpostazioniSinistra = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistra.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatoreImpostazioniDestraBloccato = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniDestraBloccato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    puntatoreImpostazioniSinistraBloccato = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriImpostazioniSinistraBloccato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgCasellaObbiettivoAnalizzaColco = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Puntatori/ObiettivoAnalizzaColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    # immagini personaggio
    persw = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perswb = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persa = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persab = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perso = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persob = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    perss = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perssb = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persd = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persdb = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perssm = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perssmb1 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perssmb2 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persdm = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio2mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persdmb1 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio2movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persdmb2 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio2movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persam = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio3mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persamb1 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio3movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persamb2 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio3movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perswm = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio4mov.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perswmb1 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio4movb1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perswmb2 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio4movb2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perswmbAttacco = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio4movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persambAttacco = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio3movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    perssmbAttacco = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persdmbAttacco = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio2movbAttacco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persmbDifesa = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/PersonaggiomovbDifesa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persAvvele = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/PersonaggioAvvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    persoSara1 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoSara2 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara2/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoSara3 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara3/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoSara4 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara4/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoSara5 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoSara6 = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Sara6Menu.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persobSara = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara1/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persobSara5 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoFraMaggiore = ImageClass.ImageClass('Risorse/Immagini/Personaggi/FratelloMaggiore/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persobFraMaggiore = ImageClass.ImageClass('Risorse/Immagini/Personaggi/FratelloMaggiore/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persoRod = ImageClass.ImageClass('Risorse/Immagini/Personaggi/RodGiocabile/Personaggio1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    persobRod = ImageClass.ImageClass('Risorse/Immagini/Personaggi/RodGiocabile/Personaggio1b.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)

    # immagini robot
    robow = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    roboa = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    roboo1 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    roboo2 = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True, forceLoad=funzionePerCaricareImmagini)
    robos = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    robod = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    robomo = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot0.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    robodp = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot2p.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    roboap = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/Robot3p.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    armrobmo = ImageClass.ImageClass('Risorse/Immagini/EquipRobo/Batteria00.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    roboSurrisc = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Colco/RobotSurriscaldato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    casellaVuotaPreset = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
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
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
        else:
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iwMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iwMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iaMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iaMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%isMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%isMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%idMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%idMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%isAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iaAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%idAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iwAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
        vetImgSpadeInGame.append(vetAnimaTemp)
        # arco
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
        else:
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%isAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%iaAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%idAttacco.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%iwAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True))
        vetImgArchiInGame.append(vetAnimaTemp)
        # armatura
        vetAnimaTemp = []
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Armature/Armatura%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Armature/Armatura%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Armature/Armatura%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgArmatureInGame.append(vetAnimaTemp)
        # scudo
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
        else:
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%iDifesa.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgScudiInGame.append(vetAnimaTemp)
        # guanti
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
        else:
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iwMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iwMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iaMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iaMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%isMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%isMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%idMov1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%idMov2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%isAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iaAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%idAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iwAttacco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iDifesa.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgGuantiInGame.append(vetAnimaTemp)
        # collana
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
        else:
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Collane/Collana%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Collane/Collana%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Collane/Collana%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgCollaneInGame.append(vetAnimaTemp)
        contatoreGlobale += 1
    vetImgFaretreInGame = []
    contatoreGlobale = 0
    while contatoreGlobale < 4:
        # faretra
        vetAnimaTemp = []
        if contatoreGlobale == 0:
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
            vetAnimaTemp.append(casellaVuotaPreset)
        else:
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Faretre/Faretra%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Faretre/Faretra%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Faretre/Faretra%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
            vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Faretre/Faretra%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgFaretreInGame.append(vetAnimaTemp)
        contatoreGlobale += 1
    vetImgArmRobInGame = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        # armatura robot
        vetAnimaTemp = []
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipRobo/Batteria%iw.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipRobo/Batteria%ia.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetAnimaTemp.append(ImageClass.ImageClass("Risorse/Immagini/EquipRobo/Batteria%id.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
        vetImgArmRobInGame.append(vetAnimaTemp)
        contatoreGlobale += 1

    # img danneggiamento personaggio e Colco
    imgDanneggiamentoCausaRallo = ImageClass.ImageClass("Risorse/Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgDanneggiamentoCausaColco = ImageClass.ImageClass("Risorse/Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    # img menu mercante
    mercanteMenu = ImageClass.ImageClass('Risorse/Immagini/Personaggi/Mercante/MercanteDialogo.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    pappagalloMenuMercante = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Dialoghi/PappagalloGrafMenuMercante.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    saraMenuMercante = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Dialoghi/Sara4Dialogo.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    scorriSuGiu = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    scorriSuGiuBloccato = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    scorriSuGiuBloccatoGiu = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    scorriSuGiuBloccatoSu = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Puntatori/ScorriSuGiuBloccatoSu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    sfondoDialogoMercante = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/SfondoDialogoMercante.png', GlobalHWVar.gpx * 9.5, GlobalHWVar.gpy * 4.5, False, imgImpenetrabile=True)
    faretra1Menu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Faretra1Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra2Menu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Faretra2Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    faretra3Menu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Faretra3Menu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)
    frecciaMenu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/FrecciaMenu.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False)

    # sfondi
    sfondoRallo = ImageClass.ImageClass('Risorse/Immagini/Status/SfondoRallo.png', GlobalHWVar.gpx * 8, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoColco = ImageClass.ImageClass('Risorse/Immagini/Status/SfondoColco.png', GlobalHWVar.gpx * 6, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoMostro = ImageClass.ImageClass('Risorse/Immagini/Status/SfondoNemici.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoEsche = ImageClass.ImageClass('Risorse/Immagini/Status/SfondoEsche.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoLogoInterazioneNonAttivo = ImageClass.ImageClass('Risorse/Immagini/Status/SfondoLogoInterazioneNonAttivo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoLogoInterazioneAttivo = ImageClass.ImageClass('Risorse/Immagini/Status/SfondoLogoInterazioneAttivo.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, imgImpenetrabile=True)
    sfondoStartBattaglia = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SfondoStartBattaglia.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 10, False, imgImpenetrabile=True)
    sfondoTriangolinoAltoDestra = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/TriangoloAltoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoAltoSinistra = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/TriangoloAltoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoDestra = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/TriangoloBassoDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    sfondoTriangolinoBassoSinistra = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/TriangoloBassoSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    casellaChiara = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    casellaChiara.fill((0, 0, 0, 0))
    casellaScura = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    casellaScura.fill((0, 0, 0, 10))
    casellaOscurata = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    casellaOscurata.fill((0, 0, 0, 100))

    # status
    appiccicoso = ImageClass.ImageClass('Risorse/Immagini/Status/Appiccicoso.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    avvelenatoMenu = ImageClass.ImageClass('Risorse/Immagini/Status/Avvelenato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    avvelenato = ImageClass.ImageClass('Risorse/Immagini/Status/Avvelenato.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    surriscaldatoMenu = ImageClass.ImageClass('Risorse/Immagini/Status/Surriscaldato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    surriscaldato = ImageClass.ImageClass('Risorse/Immagini/Status/Surriscaldato.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    attaccopiuMenu = ImageClass.ImageClass('Risorse/Immagini/Status/Attaccopiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    attaccopiu = ImageClass.ImageClass('Risorse/Immagini/Status/Attaccopiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    difesapiuMenu = ImageClass.ImageClass('Risorse/Immagini/Status/Difesapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    difesapiu = ImageClass.ImageClass('Risorse/Immagini/Status/Difesapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    velocitapiuMenu = ImageClass.ImageClass('Risorse/Immagini/Status/Velocitapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    velocitapiu = ImageClass.ImageClass('Risorse/Immagini/Status/Velocitapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    efficienzapiuMenu = ImageClass.ImageClass('Risorse/Immagini/Status/Efficienzapiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    efficienzapiu = ImageClass.ImageClass('Risorse/Immagini/Status/Efficienzapiu.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)
    imgNumFrecce = ImageClass.ImageClass('Risorse/Immagini/Status/NumFrecce.png', GlobalHWVar.gpx * 3 // 4, GlobalHWVar.gpy * 3 // 4, True, forceLoad=funzionePerCaricareImmagini)

    # menu alto destra
    sfochiaveocchio = ImageClass.ImageClass("Risorse/Immagini/Oggetti/SfondoOcchioChiave.png", GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, False, imgImpenetrabile=True)
    occhioape = ImageClass.ImageClass('Risorse/Immagini/Status/OcchioAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    occhiochiu = ImageClass.ImageClass('Risorse/Immagini/Status/OcchioChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    chiaveroboacc = ImageClass.ImageClass('Risorse/Immagini/Oggetti/ChiaveColcoAcc.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    chiaverobospe = ImageClass.ImageClass('Risorse/Immagini/Oggetti/ChiaveColcoSpe.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgSaltaTurno = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SaltaTurno.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgSaltaTurnoCliccato = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SaltaTurnoCliccato.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
    imgModInterazione = ImageClass.ImageClass('Risorse/Immagini/Oggetti/LogoInterazione.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # oggetti sulla schermata
    esche = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Oggetto8Ico.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    sacchettoDenaroStart = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SacchettoDenaroSinistra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaroMercante = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SacchettoDenaroDestra.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart0 = ImageClass.ImageClass('Risorse/Immagini/EquipSara/Faretre/Faretra0Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart1 = ImageClass.ImageClass('Risorse/Immagini/EquipSara/Faretre/Faretra1Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart2 = ImageClass.ImageClass('Risorse/Immagini/EquipSara/Faretre/Faretra2Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    faretraFrecceStart3 = ImageClass.ImageClass('Risorse/Immagini/EquipSara/Faretre/Faretra3Menu.png', GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False)
    sacchettoDenaro = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SacchettoDenaroIco.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgFrecciaLanciata = ImageClass.ImageClass('Risorse/Immagini/Oggetti/Freccia.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaInterzaione = ImageClass.ImageClass('Risorse/Immagini/Oggetti/InterazioneDisponibile.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaInterzaioneCompiuta = ImageClass.ImageClass('Risorse/Immagini/Oggetti/InterazioneEffettuata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaSu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaSu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaGiu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaGiu.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaDestra = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaDestra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaSinistra = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaSinistra.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaSuBloccate = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaSuBloccata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaGiuBloccate = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaGiuBloccata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaDestraBloccate = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaDestraBloccata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgEvidenziaUsciteStanzaSinistraBloccate = ImageClass.ImageClass('Risorse/Immagini/Oggetti/UscitaStanzaSinistraBloccata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgBacchePv = ImageClass.ImageClass('Risorse/Immagini/Oggetti/BacchePv.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    # cofanetti
    cofaniaper = ImageClass.ImageClass('Risorse/Immagini/Oggetti/CofanettoAperto.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    cofanichiu = ImageClass.ImageClass('Risorse/Immagini/Oggetti/CofanettoChiuso.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    sfocontcof = ImageClass.ImageClass('Risorse/Immagini/Oggetti/SfondoContenutoCofanetto.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 3, False)

    # caselle attaccabili
    campoattaccabileRallo1 = ImageClass.ImageClass('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False, forceLoad=funzionePerCaricareImmagini)
    campoattaccabileRallo2 = ImageClass.ImageClass('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False, forceLoad=funzionePerCaricareImmagini)
    campoattaccabileRallo3 = ImageClass.ImageClass('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False, forceLoad=funzionePerCaricareImmagini)
    campoattaccabileRallo4 = ImageClass.ImageClass('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 11, False, forceLoad=funzionePerCaricareImmagini)
    campoattaccabileRallo5 = ImageClass.ImageClass('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRallo.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False, forceLoad=funzionePerCaricareImmagini)
    campoattaccabileRobo = ImageClass.ImageClass('Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileRobo.png', GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, False, forceLoad=funzionePerCaricareImmagini)
    caselleattaccabiliRobo = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    caselleattaccabiliRobo.fill((0, 0, 130, 100))
    caselleattaccabilimostro = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    caselleattaccabilimostro.fill((130, 0, 0, 100))
    caselleattaccabili = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
    caselleattaccabili.fill((0, 0, 0, 100))

    # aumento livello
    saliliv = ImageClass.ImageClass('Risorse/Immagini/Status/Levelup/Saliliv.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    saliliv1 = ImageClass.ImageClass('Risorse/Immagini/Status/Levelup/Saliliv1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    saliliv2 = ImageClass.ImageClass('Risorse/Immagini/Status/Levelup/Saliliv2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    # img equipaggiamento, condizioni, tecniche, oggetti
    vetImgSpadeMenu = []
    vetImgArchiMenu = []
    vetImgArmatureMenu = []
    vetImgScudiMenu = []
    vetImgGuantiMenu = []
    vetImgCollaneMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgSpadeMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArchiMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgArmatureMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Armature/Armatura%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgScudiMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgGuantiMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        vetImgCollaneMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Collane/Collana%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        contatoreGlobale += 1
    imgGambitSconosciuta = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/GrafGambit/Sconosciuto.png', GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False)
    vetImgCondizioniMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgCondizioniMenu.append(ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/GrafGambit/GrafCondizioni/Condizione%i.png" % contatoreGlobale, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False))
        contatoreGlobale += 1
    vetImgTecnicheMenu = []
    contatoreGlobale = 0
    while contatoreGlobale <= 20:
        vetImgTecnicheMenu.append(ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/GrafGambit/GrafTecniche/Tecnica%i.png" % contatoreGlobale, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 9, False))
        contatoreGlobale += 1
    vetImgBatterieMenu = []
    vetIcoBatterieMenu = []
    contatoreGlobale = 0
    while contatoreGlobale < 5:
        vetImgBatterieMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetIcoBatterieMenu.append(ImageClass.ImageClass("Risorse/Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False))
        contatoreGlobale += 1
    vetImgOggettiMenu = []
    vetImgOggettiMercante = []
    vetImgOggettiStart = []
    vetIcoOggettiMenu = []
    contatoreGlobale = 1
    while contatoreGlobale <= 10:
        vetImgOggettiMenu.append(ImageClass.ImageClass("Risorse/Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False))
        vetImgOggettiMercante.append(ImageClass.ImageClass("Risorse/Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False))
        vetImgOggettiStart.append(ImageClass.ImageClass("Risorse/Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False))
        vetIcoOggettiMenu.append(ImageClass.ImageClass("Risorse/Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True))
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
        vetImgSpadePixellate.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Spade/Spada%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArchiPixellate.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Archi/Arco%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgArmaturePixellate.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Armature/Armatura%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgScudiPixellate.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Scudi/Scudo%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgGuantiPixellate.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Guanti/Guanti%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        vetImgCollanePixellate.append(ImageClass.ImageClass("Risorse/Immagini/EquipSara/Collane/Collana%is.png" % contatoreGlobale, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True))
        contatoreGlobale += 1

    # img animazioni oggetti
    imgAnimaBomba = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/Bomba.png', GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaBombaVeleno = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/BombaVeleno.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaBombaAppiccicosa = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/BombaAppiccicosa.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaBombaPotenziata = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/BombaPotenziata.png', GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaPozione1 = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/Pozione1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaPozione2 = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/Pozione2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaMedicina1 = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/Medicina1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaMedicina2 = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/Medicina2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgAnimaCaricabatterie = ImageClass.ImageClass('Risorse/Immagini/AnimazioniOggetti/Caricabatterie.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    # img animazioni tecniche
    imgDanneggiamentoColco = ImageClass.ImageClass('Risorse/Immagini/AnimazioniTecniche/Danneggiamento.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    vetAnimazioniTecniche = []
    nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
    for contatoreGlobale in nomiTecniche:
        vetAnimazioniTecniche.append(contatoreGlobale)
        vetAnimaImgTecniche = []
        if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
            if contatoreGlobale.startswith("freccia"):
                contatoreGlobale = "freccia"
            img1 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True, forceLoad=funzionePerCaricareImmagini)
            img2 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
            img2 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True, forceLoad=funzionePerCaricareImmagini)
            img2 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            img1 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
            img2 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
            imgSelf = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%sAnimaSelf.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(imgSelf)
        elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
            img1 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale, GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(img1)
        elif contatoreGlobale.startswith("tempesta"):
            img1 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, True, forceLoad=funzionePerCaricareImmagini)
            img2 = ImageClass.ImageClass("Risorse/Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 13, True, forceLoad=funzionePerCaricareImmagini)
            vetAnimaImgTecniche.append(img1)
            vetAnimaImgTecniche.append(img2)
        vetAnimazioniTecniche.append(vetAnimaImgTecniche)
    imgFrecciaEletttricaLanciata = ImageClass.ImageClass('Risorse/Immagini/AnimazioniTecniche/FrecciaLanciata.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgFrecciaEletttricaLanciataP = ImageClass.ImageClass('Risorse/Immagini/AnimazioniTecniche/FrecciaLanciata+.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
    imgFrecciaEletttricaLanciataPP = ImageClass.ImageClass('Risorse/Immagini/AnimazioniTecniche/FrecciaLanciata++.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)

    # img tutorial
    tutorialTastieraInGioco = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/TastieraInGioco.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialTastieraInMenu = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/TastieraInMenu.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialMouse = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/Mouse.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialControllerInGioco = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ControllerInGioco.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    tutorialControllerInMenu = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ControllerInMenu.png', GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11, False)
    impostazioniController = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoController.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroce = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroce.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCerchio = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCerchio.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerQuadrato = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerQuadrato.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerTriangolo = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerTriangolo.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerL1 = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerL1.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerR1 = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerR1.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerStart = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerStart.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerSelect = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerSelect.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale_su = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale_su.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale_giu = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale_giu.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale_destra = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale_destra.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostaControllerCroceDirezionale_sinistra = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoControllerCroceDirezionale_sinistra.png', GlobalHWVar.gpx * 14, GlobalHWVar.gpy * 14, False)
    impostazioniTastiera = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Tutorial/ImpoTastiera.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 16, False)

    # img grafiche / dialoghi
    sfondoDialoghi = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Dialoghi/SfondoSotto.png', GlobalHWVar.gsx, GlobalHWVar.gsy // 3, False, imgImpenetrabile=True)
    robograf1 = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf1.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf2 = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    robograf2b = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf2.png', GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    robograf4 = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGraf4.png', GlobalHWVar.gpx * 18, GlobalHWVar.gpy * 18, False)
    imgDialogoColco = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/Dialoghi/RobotDialogo.png', GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
    dictImgDialoghiPersonaggiOggettoSpecifici = {}
    dictImgPersonaggiOggettoSpecifici = {}
    dictImgPersonaggiOggettoSpecifici["OggettoDictCofanettoAperto"] = cofaniaper
    dictImgPersonaggiOggettoSpecifici["OggettoDictCofanettoChiuso"] = cofanichiu
    vettoreNomiCadaveriNemici = ["CadavereSoldatoCastello", "CadavereOrco", "CadaverePipistrello", "CadavereTartarugaVerde", "CadavereTartarugaMarrone", "CadavereLupoGrigio", "CadavereLupoBianco", "CadavereLupoNero", "CadavereCinghiale", "CadavereCittadino1", "CadavereCittadino3", "CadavereSerpeVerde", "CadavereSerpeArancio", "CadavereScorpione", "CadavereRagnoNero", "CadavereRagnoRosso", "CadavereGufoMarrone", "CadavereGufoBianco", "CadavereFalco", "CadavereAquila", "CadavereStruzzo", "CadavereCasuario", "CadavereRoboLeggero", "CadavereRoboVolante", "CadavereRoboPesante", "CadavereRoboPesanteVolante", "CadavereRoboTorre"]
    for nomeCadavereNemico in vettoreNomiCadaveriNemici:
        dictImgDialoghiPersonaggiOggettoSpecifici["OggettoDict" + nomeCadavereNemico + "Dialogo"] = ImageClass.ImageClass("Risorse/Immagini/Personaggi/Oggetti/" + nomeCadavereNemico + "/" + nomeCadavereNemico + "Dialogo.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
        dictImgPersonaggiOggettoSpecifici["OggettoDict" + nomeCadavereNemico + "1"] = ImageClass.ImageClass("Risorse/Immagini/Personaggi/Oggetti/" + nomeCadavereNemico + "/" + nomeCadavereNemico + "1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictImgPersonaggiOggettoSpecifici["OggettoDict" + nomeCadavereNemico + "2"] = ImageClass.ImageClass("Risorse/Immagini/Personaggi/Oggetti/" + nomeCadavereNemico + "/" + nomeCadavereNemico + "2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictImgPersonaggiOggettoSpecifici["OggettoDict" + nomeCadavereNemico + "3"] = ImageClass.ImageClass("Risorse/Immagini/Personaggi/Oggetti/" + nomeCadavereNemico + "/" + nomeCadavereNemico + "3.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)

    # img equipaggiamento, condizioni, tecniche, oggetti
    sfondoOggettoMenu = ImageClass.ImageClass("Risorse/Immagini/EquipSara/SfondoOggetto.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False, forceLoad=funzionePerCaricareImmagini)
    sconosciutoEquipMenu = ImageClass.ImageClass("Risorse/Immagini/Oggetti/SconosciutoEquip.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, False, forceLoad=funzionePerCaricareImmagini)
    sconosciutoOggettoMenu1 = ImageClass.ImageClass("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 4, False, forceLoad=funzionePerCaricareImmagini)
    sconosciutoOggettoMenu2 = ImageClass.ImageClass("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 8, False, forceLoad=funzionePerCaricareImmagini)
    sconosciutoOggettoMenu3 = ImageClass.ImageClass("Risorse/Immagini/Oggetti/Sconosciuto.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False, forceLoad=funzionePerCaricareImmagini)
    sconosciutoOggettoIcoMenu = ImageClass.ImageClass("Risorse/Immagini/Oggetti/SconosciutoIco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, False, forceLoad=funzionePerCaricareImmagini)

    # img personaggi
    vettoreNomiPersonaggi = ["AssistBiblioteca", "Bambino1", "Bambino2", "Bibliotecario", "BibliotecarioOperato", "CaneCasa", "Costruttore", "FiglioUfficiale", "GuardiaCitta", "Madre", "MadreUfficiale", "Mercante", "MercanteFuturo", "Neil", "Padre", "PadreUfficialeCasa", "PadreUfficialeServizio", "Pazzo1", "Pazzo2", "Ragazza1", "Ragazza2", "Ragazza3", "Ragazzo1", "Ragazzo2", "Ragazzo3", "ServoArco", "ServoDavid", "ServoLancia", "ServoSpada", "FratelloMaggiore", "SaraArmaturaPelle"]
    dictionaryImgPersonaggi = {}
    for nomePersonaggi in vettoreNomiPersonaggi:
        dictionaryImgPosizioni = {}
        imgW = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "W.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "A.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "S.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "D.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "WMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "WMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "AMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "AMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "SMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "SMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "DMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "DMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgDialogo = ImageClass.ImageClass("Risorse/Immagini/Personaggi/" + nomePersonaggi + "/" + nomePersonaggi + "Dialogo.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, True)
        dictionaryImgPosizioni["imgDialogo"] = imgDialogo

        dictionaryImgPersonaggi[nomePersonaggi] = dictionaryImgPosizioni
    dictImgPersonaggiDiario = {}
    for nomePersonaggi in vettoreNomiPersonaggi:
        if nomePersonaggi != "AssistBiblioteca" and nomePersonaggi != "GuardiaCitta" and nomePersonaggi != "Ragazza1" and nomePersonaggi != "Ragazza2" and nomePersonaggi != "Ragazza3" and nomePersonaggi != "Ragazzo1" and nomePersonaggi != "Ragazzo2" and nomePersonaggi != "Ragazzo3" and nomePersonaggi != "ServoArco" and nomePersonaggi != "ServoDavid" and nomePersonaggi != "ServoLancia" and nomePersonaggi != "ServoSpada" and nomePersonaggi != "FratelloMaggiore" and nomePersonaggi != "BibliotecarioOperato" and nomePersonaggi != "MercanteFuturo" and nomePersonaggi != "Bambino1" and nomePersonaggi != "Bambino2" and nomePersonaggi != "SaraArmaturaPelle":
            imgPersonaggi = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/" + nomePersonaggi + "GrafMenu.png", GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
            dictImgPersonaggiDiario[nomePersonaggi] = imgPersonaggi
    fraMaggioreDiario = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/FratelloMaggioreGrafMenu.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    roboDiario = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/RobotGrafMenuDiario.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    imgProtagonistaDiario = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/SaraGrafMenuDiario.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    neilSconosciutoDiario = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/NeilSconosciutoGrafMenu.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
    pappagalloDiario = ImageClass.ImageClass('Risorse/Immagini/DecorazioniMenu/DisegniPersonaggi/PappagalloGrafMenu.png', GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)

    # img nemici
    vettoreNomiNemici = ["Orco", "Pipistrello", "TartarugaVerde", "TartarugaMarrone", "LupoGrigio", "LupoBianco", "LupoNero", "Cinghiale", "Cittadino1", "Cittadino3", "SerpeVerde", "SerpeArancio", "Scorpione", "RagnoNero", "RagnoRosso", "ServoSpada", "ServoArco", "ServoLancia", "GufoMarrone", "GufoBianco", "Falco", "Aquila", "Struzzo", "Casuario", "RoboLeggero", "RoboVolante", "RoboPesante", "RoboPesanteVolante", "RoboTorre"]
    dictionaryImgNemici = {}
    for nomeNemico in vettoreNomiNemici:
        dictionaryImgPosizioni = {}

        imgW = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "w.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgW"] = imgW
        imgA = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "a.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgA"] = imgA
        imgS = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "s.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgS"] = imgS
        imgD = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "d.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgD"] = imgD
        imgWMov1 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov1"] = imgWMov1
        imgWMov2 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgWMov2"] = imgWMov2
        imgAMov1 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov1"] = imgAMov1
        imgAMov2 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAMov2"] = imgAMov2
        imgSMov1 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov1"] = imgSMov1
        imgSMov2 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgSMov2"] = imgSMov2
        imgDMov1 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov1.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov1"] = imgDMov1
        imgDMov2 = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dMov2.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDMov2"] = imgDMov2
        imgAvvelenamento = ImageClass.ImageClass("Risorse/Immagini/Nemici/NemicoAvvelenato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAvvelenamento"] = imgAvvelenamento
        imgAppiccicato = ImageClass.ImageClass("Risorse/Immagini/Nemici/NemicoAppiccicato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAppiccicato"] = imgAppiccicato
        imgAttaccoW = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "wAttacco.png", GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoW"] = imgAttaccoW
        imgAttaccoA = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "aAttacco.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAttaccoA"] = imgAttaccoA
        imgAttaccoS = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "sAttacco.png", GlobalHWVar.gpx, GlobalHWVar.gpy * 2, True)
        dictionaryImgPosizioni["imgAttaccoS"] = imgAttaccoS
        imgAttaccoD = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "dAttacco.png", GlobalHWVar.gpx * 2, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgAttaccoD"] = imgAttaccoD
        imgOggettoLanciato = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/OggettoLanciato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgOggettoLanciato"] = imgOggettoLanciato
        imgDanneggiamentoOggettoLanciato = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/DanneggiamentoOggettoLanciato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoOggettoLanciato"] = imgDanneggiamentoOggettoLanciato
        imgDanneggiamentoRalloNemico = ImageClass.ImageClass("Risorse/Immagini/Nemici/DannoRallo.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoRalloNemico"] = imgDanneggiamentoRalloNemico
        imgDanneggiamentoColcoNemico = ImageClass.ImageClass("Risorse/Immagini/Nemici/DannoColco.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        dictionaryImgPosizioni["imgDanneggiamentoColcoNemico"] = imgDanneggiamentoColcoNemico
        if nomeNemico == "Orco" or nomeNemico == "Pipistrello" or nomeNemico == "Cinghiale" or nomeNemico == "Cittadino1" or nomeNemico == "Cittadino3" or nomeNemico == "Scorpione" or nomeNemico == "ServoSpada" or nomeNemico == "ServoArco" or nomeNemico == "ServoLancia" or nomeNemico == "Aquila":
            imgDialogo = casellaVuotaPreset
        else:
            imgDialogo = ImageClass.ImageClass("Risorse/Immagini/Nemici/" + nomeNemico + "/" + nomeNemico + "Dialogo.png", GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 12, False)
        dictionaryImgPosizioni["imgDialogo"] = imgDialogo

        dictionaryImgNemici[nomeNemico] = dictionaryImgPosizioni
    dictImgCampiVisiviNemici = {}
    raggio = 2
    while raggio <= 8:
        dictImgCampiVisiviNemici[str(raggio)] = ImageClass.ImageClass("Risorse/Immagini/Status/Campiattaccabili/CampoattaccabileMostro.png", (GlobalHWVar.gpx * raggio * 2) + GlobalHWVar.gpx, (GlobalHWVar.gpy * raggio * 2) + GlobalHWVar.gpy, True, forceLoad=funzionePerCaricareImmagini)
        raggio += 1
    dictImgNemiciDiario = {}
    for nomeNemico in vettoreNomiNemici:
        imgNemico = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/DisegniNemici/" + nomeNemico + "Graf.png", GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 9, False)
        dictImgNemiciDiario[nomeNemico] = imgNemico

    # img menu
    imgOmbreggiaturaContorniMappaMenu = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Mappe/OmbreggiaturaContorniMappaMenu.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
    imgDiarioChiusoMenu = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/DiarioChiusoMenu.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)
    imgDiarioApertoMenu = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/DiarioApertoMenu.png", GlobalHWVar.gpx * 22, GlobalHWVar.gpy * 15, False)

    # img oggetti speciali
    imgBicchiereConAcqua = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/BicchiereConAcqua.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveRipostiglio = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveRipostiglio.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveStanzaCasaDavid = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveStanzaCasaDavid.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgCertificazioneResidenza = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/CertificazioneResidenza.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgImpoPietra = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ImpoPietra.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveStanzaCastello = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveStanzaCastello.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgListaStrumentiStudioImpo = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ListaStrumentiStudioImpo.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveAvamposto = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveAvampostoDiRod.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgStrumentiDiRod = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/StrumentiDiRod.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveUfficioNeil = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveUfficioNeil.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
    imgChiaveSeminterratoPalazzoRod = ImageClass.ImageClass("Risorse/Immagini/DecorazioniMenu/Diario/OggettiSpeciali/ChiaveSeminterratoPalazzoDiRod.png", GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 10, False)
