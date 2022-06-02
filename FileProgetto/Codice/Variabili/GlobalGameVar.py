# -*- coding: utf-8 -*-

import psutil
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.SettaggiLivelli.SetAvanzamentiStanzePorteCofanetti as SetAvanzamentiStanzePorteCofanetti

# vettore statistiche per livello
def inizializzaStatistichePerLivello():
    # per ottenere le statistiche per livello
    statistichePerLivello = []
    lvTest = 1
    while lvTest <= 100:
        if lvTest == 1:
            pvtot = 15
            attVicino = 3
            attLontano = 2
            dif = 3
        elif lvTest == 2:
            pvtot = 15
            attVicino = 8
            attLontano = 6
            dif = 3
        elif lvTest == 3:
            pvtot = 15
            attVicino = 8
            attLontano = 6
            dif = 8
        else:
            pvtot = 20
            attVicino = 8
            attLontano = 6
            dif = 8
            i = 1
            while i <= 100:
                if lvTest <= i + 2:
                    # pvtot += int(i * (i * 0.05))
                    pvtot = int(i * 5)
                    break
                i += 3
            i = 2
            while i <= 100:
                if lvTest <= i + 2:
                    # attVicino += int(i * (i * 0.0515))
                    # attLontano += int(i * (i * 0.0474))
                    attVicino = 4 + int(i * 2)
                    attLontano = 3 + int(i * 1.5)
                    break
                i += 3
            i = 3
            while i <= 100:
                if lvTest <= i + 2:
                    # dif += int(i * (i * 0.0405))
                    dif = 2 + int(i * 2)
                    break
                i += 3
        statistichePerLivello.append([pvtot, attVicino, attLontano, dif])
        lvTest += 1
    # for lv in statistichePerLivello:
    #     print "statistichePerLivello.append(" + str(lv) + ")"
    # for lv in statistichePerLivello:
    #     print str(lv[0]) + ", " + str(lv[1]) + ", " + str(lv[3])
    return statistichePerLivello
statistichePerLivello = inizializzaStatistichePerLivello()
statisticheEquipaggiamento = {}
statisticheEquipaggiamento["spade"] = [0, 12, 25, 50, 100]
statisticheEquipaggiamento["archi"] = [0, 10, 20, 40, 80]
statisticheEquipaggiamento["armature"] = [0, 12, 25, 50, 100]
statisticheEquipaggiamento["scudiDif"] = [0, 6, 12, 25, 50]
statisticheEquipaggiamento["scudiPar"] = [0, 3, 8, 18, 38]
statisticheEquipaggiamento["guanti"] = [0, 20, 20, 20, 10]
statisticheEquipaggiamento["batteriaPe"] = [200, 300, 500, 900, 1500]
statisticheEquipaggiamento["batteriaDif"] = [60, 80, 120, 180, 250]
dannoAttacchiColco = {"scossa": 100, "freccia": 85, "tempesta": 70, "scossa+": 200, "freccia+": 175, "tempesta+": 150, "scossa++": 380, "freccia++": 330, "tempesta++": 280}

# vettore che conterrà tutti i dati dei salvataggi
vetDatiSalvataggi = []
# vettore che conterrà i dati di salvataggio del file gameover
vetDatiSalvataggioGameOver = []
numSalvataggioCaricato = 0

# dati tecniche di Colco [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesta++]
costoTecniche = [3, 5, 3, 3, 6, 10, 5, 10, 10, 10, 15, 10, 10, 15, 20, 20, 20, 30, 30, 60]
dannoTecniche = [dannoAttacchiColco["scossa"], 50, 0, dannoAttacchiColco["freccia"], dannoAttacchiColco["tempesta"], 0, 300, 150, dannoAttacchiColco["scossa+"], dannoAttacchiColco["freccia+"], 1, 50, 50, 1, dannoAttacchiColco["tempesta+"], 500, 1000, dannoAttacchiColco["scossa++"], dannoAttacchiColco["freccia++"], dannoAttacchiColco["tempesta++"]]
vistaRobo = 6
# costo oggetti => costoOggetti[frecce, pozione, caricabatterie, medicina, superpozione, caricabatterie migliorato, bomba, bomba veleno, esca, bomba appiccicosa, bomba potenziata, faretra1, faretra2, faretra3]
costoOggetti = [5, 20, 30, 30, 80, 100, 50, 80, 120, 150, 200, 50, 500, 5000]
# danno oggetti => dannoOggetti[bomba, bombaVeleno, esca, bombaAppiccicosa, bombaPotenziata]
dannoOggetti = [200, 100, 0, 100, 500]
# cura oggetti => curaOggetti[pozione, caricabatterie piccolo, medicina, super pozione, caricabatterie grande]
curaOggetti = [100, 250, 0, 300, 800]
# frecce trasportabili per faretra
frecceMaxPerFaretra = [3, 20, 100, 800]

# dichiaro il dictionary che contiene gli avanzamenti della storia associati agli avvenimenti
dictAvanzamentoStoria = SetAvanzamentiStanzePorteCofanetti.definisciAvanzamentiStoria()
# dichiaro il dictionary che contiene le stanze associate a un nome che le descrive
dictStanze, vetStanzePacifiche = SetAvanzamentiStanzePorteCofanetti.definisciStanze()
vetStanzePacificheBackUp = vetStanzePacifiche[:]
# dichiaro i vettori di porte e cofanetti
initVetPorteGlobale = SetAvanzamentiStanzePorteCofanetti.definisciPorte(dictStanze)
initVetCofanettiGlobale = SetAvanzamentiStanzePorteCofanetti.definisciCofanetti(dictStanze)

# definisco il massimo delle monete che è possibile avere
maxMonete = 999999

# vita esche
vitaTotEsche = 200

# danno mortale (viene usato per la storia)
dannoMortale = 100000

# costi servizi di Rod
monetePerEntrareNellaConfraternita = 200
monetePerLasciareLaConfraternita = 1000
monetePerLaMappaDelLabirinto = 500
monetePerGliStumentiPerNeil = 1500

global nomiImgDaAggiornareAvanzandoStoriaAttuali
global imgDaAggiornareAvanzandoStoria
global nomePersonaggioDialoghi
global canzoneAttuale
global schemataDiCaricamento
global audioSottofondoAttuale
global idNemico
global listaIdNemiciUsati
global datiEnigmaBibliotecario
global pazzoStrabico
global volumeMusicaDimezzato
global impoPresente
global impoPietraPosseduta
global cambiataAlCastello
global armaturaIndossata
global datiAnimazioniDanniInflitti
global idDialoghiLetti
global idDialoghiLettiGameOver
def inizializzaVariabiliGlobali():
    global nomiImgDaAggiornareAvanzandoStoriaAttuali
    global imgDaAggiornareAvanzandoStoria
    global nomePersonaggioDialoghi
    global canzoneAttuale
    global schemataDiCaricamento
    global audioSottofondoAttuale
    global idNemico
    global listaIdNemiciUsati
    global datiEnigmaBibliotecario
    global pazzoStrabico
    global volumeMusicaDimezzato
    global impoPresente
    global impoPietraPosseduta
    global cambiataAlCastello
    global armaturaIndossata
    global datiAnimazioniDanniInflitti
    global idDialoghiLetti
    global idDialoghiLettiGameOver
    nomiImgDaAggiornareAvanzandoStoriaAttuali = {"imgMappaAttuale":False, "imgProtagonistaStartAttuale": False, "imgProtagonistaMenuOggettiAttuale":False, "imgProtagonistaDialogoAttuale":False}
    imgDaAggiornareAvanzandoStoria = {"imgMappa":False, "imgMappaZoom":False, "imgPersonaggioStart":False, "imgPersonaggioMenuOggetti":False, "imgPersonaggioDialoghi":False}
    nomePersonaggioDialoghi = False
    canzoneAttuale = False
    schemataDiCaricamento = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/SchermataDiCaricamento.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
    audioSottofondoAttuale = False
    # id incrementale da assegare ai nemici
    idNemico = 0
    listaIdNemiciUsati = []
    # dictionary che contiene i dati dell'enigma del bibliotecario
    datiEnigmaBibliotecario = {}
    datiEnigmaBibliotecario["reset"] = False
    datiEnigmaBibliotecario["velocità"] = 2
    datiEnigmaBibliotecario["soluzione"] = 1
    datiEnigmaBibliotecario["rispostaFalsa1"] = 1.25
    datiEnigmaBibliotecario["rispostaFalsa2"] = 0.25
    datiEnigmaBibliotecario["rispostaFalsa3"] = 1.5
    pazzoStrabico = False
    volumeMusicaDimezzato = False
    impoPresente = False
    impoPietraPosseduta = False
    # cambiataAlCastello[0] => vestiti attuali cambiataAlCastello[1] => vestiti vecchi (serve per far ricaricare le img dopo il cambio)
    cambiataAlCastello = [False, False]
    armaturaIndossata = 0
    datiAnimazioniDanniInflitti = {"dannoRallo":[False, 0, -1], "dannoImpo":[False, 0, -1], "dannoEsche":[False, 0, -1], "dannoNemico":[False, 0, -1], "tempoAnimazione":60}
    idDialoghiLetti = []
    idDialoghiLettiGameOver = []
inizializzaVariabiliGlobali()

def settaRisoluzioneOttimale():
    ramDisponibile = psutil.virtual_memory().free / 1000000.0
    print ("RAM disponibile: " + str(ramDisponibile) + " MB")
    ramNecessaria = GlobalHWVar.RAMnHD
    risoluzioneConfermata = False
    while not risoluzioneConfermata:
        if GlobalHWVar.gsx > 3840:
            ramNecessaria = GlobalHWVar.RAMUUHD
        elif 2560 < GlobalHWVar.gsx <= 3840:
            ramNecessaria = GlobalHWVar.RAMUHD
        elif 1920 < GlobalHWVar.gsx <= 2560:
            ramNecessaria = GlobalHWVar.RAMQHD
        elif 1280 < GlobalHWVar.gsx <= 1920:
            ramNecessaria = GlobalHWVar.RAMFHD
        elif 960 < GlobalHWVar.gsx <= 1280:
            ramNecessaria = GlobalHWVar.RAMHD
        elif 640 < GlobalHWVar.gsx <= 960:
            ramNecessaria = GlobalHWVar.RAMqHD
        else:
            ramNecessaria = GlobalHWVar.RAMnHD
        abbassaRisoluzione = False
        for i in range(0, 20):
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()

            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
            if (GlobalHWVar.erroreFileImpostazioni and i > 10 and GlobalHWVar.clockMenu.get_fps() < 25) or ramNecessaria > ramDisponibile:
                abbassaRisoluzione = True
        if abbassaRisoluzione:
            if len(GlobalHWVar.listaRisoluzioniDisponibili) > 1:
                if GlobalHWVar.gsx == GlobalHWVar.listaRisoluzioniDisponibili[0][0]:
                    risoluzioneConfermata = True
                else:
                    i = len(GlobalHWVar.listaRisoluzioniDisponibili) - 1
                    while i >= 0:
                        if GlobalHWVar.listaRisoluzioniDisponibili[i][0] < GlobalHWVar.gsx:
                            GlobalHWVar.gsx = GlobalHWVar.listaRisoluzioniDisponibili[i][0]
                            GlobalHWVar.gsy = GlobalHWVar.listaRisoluzioniDisponibili[i][1]
                            break
                        i -= 1
            else:
                risoluzioneConfermata = True
            GlobalHWVar.gpx = GlobalHWVar.gsx // 32
            GlobalHWVar.gpy = GlobalHWVar.gsy // 18
            opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx, GlobalHWVar.gsy), opzioni_schermo)
        else:
            risoluzioneConfermata = True
    if ramNecessaria > ramDisponibile:
        print ("RAM disponibile non sufficiente. Necessaria: " + str(ramNecessaria) + " MB")
def mostraLogo():
    effettoAvvio = CaricaFileProgetto.loadSound("Risorse/Audio/RumoriAmbiente/EffettoAvvio.wav")
    logo = CaricaFileProgetto.loadImage("Risorse/Immagini/Icone/LogoPresentazione.png", GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 12, True)
    GlobalHWVar.canaleSoundInterazioni.play(effettoAvvio)
    GlobalHWVar.disegnaImmagineSuSchermo(logo, (GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 3))

    rect = pygame.display.get_surface().get_rect()
    vetImg = []
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 250))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 200))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 150))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 100))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 60))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 20))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    i = 0
    while i <= 5:
        GlobalHWVar.disegnaImmagineSuSchermo(logo, (GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 3))
        GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
        GlobalHWVar.aggiornaSchermo()
        pygame.event.pump()
        GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
        i += 1
    GlobalHWVar.disegnaImmagineSuSchermo(logo, (GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 3))
    GlobalHWVar.aggiornaSchermo()

    i = 0
    while i < 10 or GlobalHWVar.canaleSoundInterazioni.get_busy():
        pygame.time.wait(100)
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        i += 1

    rect = pygame.display.get_surface().get_rect()
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 100))
    image = image.convert_alpha(GlobalHWVar.schermo)
    i = 0
    while i <= 5:
        GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        pygame.event.pump()
        GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
        i += 1
    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
    GlobalHWVar.aggiornaSchermo()
def disegnaSchermataSelezioneLingua():
    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
    sndSpostapun = CaricaFileProgetto.loadSound("Risorse/Audio/RumoriPuntatore/SpostaPun.wav")
    sndSelezione = CaricaFileProgetto.loadSound("Risorse/Audio/RumoriPuntatore/Selezione.wav")
    sndSelimp = CaricaFileProgetto.loadSound("Risorse/Audio/RumoriPuntatore/SelImp.wav")
    puntatore = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/Puntatori/Puntatore.png", GlobalHWVar.gpx // 2, GlobalHWVar.gpy // 2, True, True)

    stringaTitolo = "Choose language"
    carattere = pygame.font.Font(GlobalHWVar.fontUtilizzato, GlobalHWVar.gpx * 200 // 60)
    testo = carattere.render(stringaTitolo, True, GlobalHWVar.grigiochi)
    GlobalHWVar.disegnaImmagineSuSchermo(testo, (GlobalHWVar.gpx * 1.6, GlobalHWVar.gpy * 2))
    carattere = pygame.font.Font(GlobalHWVar.fontUtilizzato, GlobalHWVar.gpx * 100 // 60)
    testo1 = carattere.render("English", True, GlobalHWVar.grigiochi)
    GlobalHWVar.disegnaImmagineSuSchermo(testo1, (GlobalHWVar.gpx * 2.6, GlobalHWVar.gpy * 8))
    testo2 = carattere.render("Italiano", True, GlobalHWVar.grigiochi)
    GlobalHWVar.disegnaImmagineSuSchermo(testo2, (GlobalHWVar.gpx * 2.6, GlobalHWVar.gpy * 11))
    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
    screen = GlobalHWVar.schermo.copy().convert()

    rect = pygame.display.get_surface().get_rect()
    vetImg = []
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 250))
    vetImg.append(imgOscuramento.convert_alpha(GlobalHWVar.schermo))
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 200))
    vetImg.append(imgOscuramento.convert_alpha(GlobalHWVar.schermo))
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 150))
    vetImg.append(imgOscuramento.convert_alpha(GlobalHWVar.schermo))
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 100))
    vetImg.append(imgOscuramento.convert_alpha(GlobalHWVar.schermo))
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 60))
    vetImg.append(imgOscuramento.convert_alpha(GlobalHWVar.schermo))
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 20))
    vetImg.append(imgOscuramento.convert_alpha(GlobalHWVar.schermo))
    i = 0
    while i <= 5:
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
        GlobalHWVar.aggiornaSchermo()
        pygame.event.pump()
        GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
        i += 1
    GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
    GlobalHWVar.aggiornaSchermo()

    xp = GlobalHWVar.gpx * 1.5
    yp = GlobalHWVar.gpy * 8.8
    GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
    GlobalHWVar.aggiornaSchermo()

    risposta = False
    bottoneDown = False
    voceMarcata = 1
    while not risposta:
        aggiornaSchermo = False

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 1.5 <= xMouse <= GlobalHWVar.gsx // 32 * 9:
                if GlobalHWVar.gsy // 18 * 7.8 <= yMouse <= GlobalHWVar.gsy // 18 * 10.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    yp = GlobalHWVar.gpy * 8.8
                elif GlobalHWVar.gsy // 18 * 10.5 <= yMouse <= GlobalHWVar.gsy // 18 * 13.2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    yp = GlobalHWVar.gpy * 11.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(sndSpostapun)
                aggiornaSchermo = True

        # gestione degli input
        bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu" or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu":
            GlobalHWVar.canaleSoundPuntatoreSposta.play(sndSpostapun)
            aggiornaSchermo = True
            bottoneDown = False
            if voceMarcata == 1:
                voceMarcata = 2
                yp = GlobalHWVar.gpy * 11.8
            elif voceMarcata == 2:
                voceMarcata = 1
                yp = GlobalHWVar.gpy * 8.8
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(sndSelezione)
            risposta = True
            bottoneDown = False
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(sndSelimp)
            bottoneDown = False

        if aggiornaSchermo:
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1.3, GlobalHWVar.gpx * 25, GlobalHWVar.gpy * 5.4))
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, GlobalHWVar.gpx * 1.5, GlobalHWVar.gpy * 8.2))
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
            if voceMarcata == 1:
                stringaTitolo = "Choose language"
            else:
                stringaTitolo = "Seleziona lingua"
            carattere = pygame.font.Font(GlobalHWVar.fontUtilizzato, GlobalHWVar.gpx * 200 // 60)
            testo = carattere.render(stringaTitolo, True, GlobalHWVar.grigiochi)
            GlobalHWVar.disegnaImmagineSuSchermo(testo, (GlobalHWVar.gpx * 1.6, GlobalHWVar.gpy * 2))
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    rect = pygame.display.get_surface().get_rect()
    imgOscuramento = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    imgOscuramento.fill((0, 0, 0, 100))
    imgOscuramento = imgOscuramento.convert_alpha(GlobalHWVar.schermo)
    i = 0
    while i <= 5:
        GlobalHWVar.disegnaImmagineSuSchermo(imgOscuramento, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
        i += 1
    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
    GlobalHWVar.aggiornaSchermo()

    if voceMarcata == 2:
        GlobalHWVar.linguaImpostata = "ita"
    elif voceMarcata == 1:
        GlobalHWVar.linguaImpostata = "eng"
    # inizializzo il file di impostazioni
    scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Impostazioni/Impostazioni.txt", "w")
    if GlobalHWVar.linguaImpostata == "ita":
        scrivi.write("0_")
    elif GlobalHWVar.linguaImpostata == "eng":
        scrivi.write("1_")
    scrivi.write(str(int(GlobalHWVar.volumeEffetti * 10)) + "_")
    scrivi.write(str(int(GlobalHWVar.volumeCanzoni * 10)) + "_")
    scrivi.write(str(GlobalHWVar.modalitaSchermo) + "_")
    scrivi.write(str(GlobalHWVar.gsx) + "_")
    scrivi.write(str(GlobalHWVar.gsy) + "_")
    scrivi.close()
def disegnaSchermataDiCaricamento():
    global schemataDiCaricamento
    global canzoneAttuale
    canzoneAttuale = "00-Menu"
    canzone = CaricaFileProgetto.loadSound("Risorse/Audio/Canzoni/" + canzoneAttuale + ".wav")

    sfumaturaCaricamentoMenuPrincipale = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/OmbreggiaturaCaricamentoMenuPrincipale.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
    GlobalHWVar.disegnaImmagineSuSchermo(schemataDiCaricamento, (0, 0))
    GlobalHWVar.disegnaImmagineSuSchermo(sfumaturaCaricamentoMenuPrincipale, (0, 0))
    carattere = pygame.font.Font(GlobalHWVar.fontUtilizzato, GlobalHWVar.gpx * 70 // 60)
    testo = carattere.render("Caricamento...", True, GlobalHWVar.grigiochi)
    GlobalHWVar.disegnaImmagineSuSchermo(testo, (GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 15.5))
    carattere = pygame.font.Font(GlobalHWVar.fontUtilizzato, GlobalHWVar.gpx * 200 // 60)
    testo1 = carattere.render("Off", True, GlobalHWVar.grigiochi)
    testo2 = carattere.render("To", True, GlobalHWVar.grigiochi)
    testo3 = carattere.render("Sleep", True, GlobalHWVar.grigiochi)
    GlobalHWVar.disegnaImmagineSuSchermo(testo1, (GlobalHWVar.gsx // 32 * 1.6, GlobalHWVar.gsy // 18 * 1.5))
    GlobalHWVar.disegnaImmagineSuSchermo(testo2, (GlobalHWVar.gsx // 32 * 1.6, GlobalHWVar.gsy // 18 * 4.5))
    GlobalHWVar.disegnaImmagineSuSchermo(testo3, (GlobalHWVar.gsx // 32 * 1.6, GlobalHWVar.gsy // 18 * 7.5))
    GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 1.5)), (int(GlobalHWVar.gpx * 1.5) - 1, int(GlobalHWVar.gpy * 14)), 2)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 0.5))
    screen = GlobalHWVar.schermo.copy().convert()

    rect = pygame.display.get_surface().get_rect()
    vetImg = []
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 250))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 200))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 150))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 100))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 60))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    image.fill((0, 0, 0, 20))
    vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
    i = 0
    while i <= 5:
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
        GlobalHWVar.aggiornaSchermo()
        pygame.event.pump()
        GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
        i += 1
    GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
    GlobalHWVar.aggiornaSchermo()

    GlobalHWVar.canaleSoundCanzone.play(canzone, -1)

settaRisoluzioneOttimale()
mostraLogo()
if GlobalHWVar.erroreFileImpostazioni:
    disegnaSchermataSelezioneLingua()
disegnaSchermataDiCaricamento()
numImgCaricata = 0
GlobalImgVar.loadImgs(numImgCaricata, cambioRisoluzione=False)
numSndCaricato = 0
GlobalSndVar.loadSounds(numSndCaricato)
