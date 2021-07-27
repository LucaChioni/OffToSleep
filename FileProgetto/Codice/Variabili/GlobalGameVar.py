# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import GlobalImgVar
import GlobalSndVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.SettaggiLivelli.SetAvanzamentiStanzePorteCofanetti as SetAvanzamentiStanzePorteCofanetti


# vettore che conterrà tutti i dati dei salvataggi
vetDatiSalvataggi = []
# vettore che conterrà i dati di salvataggio del file gameover
vetDatiSalvataggioGameOver = []
numSalvataggioCaricato = 0

# dati tecniche di Colco [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesta++]
costoTecniche = [5, 10, 10, 5, 10, 10, 1, 20, 10, 10, 15, 20, 20, 30, 20, 30, 1, 20, 20, 40]
dannoTecniche = [90, 30, 0, 70, 50, 0, 150, 120, 160, 130, 15, 10, 10, 15, 100, 250, 300, 320, 260, 200]
vistaRobo = 6
# costo oggetti => costoOggetti[frecce, pozione, caricabatterie, medicina, superpozione, caricabatterie migliorato, bomba, bomba veleno, esca, bomba appiccicosa, bomba potenziata, faretra1, faretra2, faretra3]
costoOggetti = [5, 20, 100, 30, 80, 200, 50, 80, 120, 200, 300, 50, 500, 5000]
# danno oggetti => dannoOggetti[bomba, bombaVeleno, esca, bombaAppiccicosa, bombaPotenziata]
dannoOggetti = [100, 50, 0, 50, 1000]
# frecce trasportabili per faretra
frecceMaxPerFaretra = [1, 20, 50, 90]

# dichiaro il dictionary che contiene gli avanzamenti della storia associati agli avvenimenti
dictAvanzamentoStoria = SetAvanzamentiStanzePorteCofanetti.definisciAvanzamentiStoria()
# dichiaro il dictionary che contiene le stanze associate a un nome che le descrive
dictStanze, vetStanzePacifiche = SetAvanzamentiStanzePorteCofanetti.definisciStanze()
# dichiaro i vettori di porte e cofanetti
initVetPorteGlobale = SetAvanzamentiStanzePorteCofanetti.definisciPorte(dictStanze)
initVetCofanettiGlobale = SetAvanzamentiStanzePorteCofanetti.definisciCofanetti(dictStanze)

# vita esche
vitaTotEsche = 300

# costi servizi di Rod
monetePerEntrareNellaConfraternita = 200
monetePerLasciareLaConfraternita = 1000
monetePerLaMappaDelLabirinto = 500

global imgMappaAttuale
global canzoneAttuale
global audioSottofondoAttuale
global idNemico
global listaIdNemiciUsati
global datiEnigmaBibliotecario
def inizializzaVariabiliGlobali():
    global imgMappaAttuale
    global canzoneAttuale
    global audioSottofondoAttuale
    global idNemico
    global listaIdNemiciUsati
    global datiEnigmaBibliotecario
    imgMappaAttuale = False
    canzoneAttuale = False
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
inizializzaVariabiliGlobali()

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
    while i < 10:
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
def disegnaSchermataDiCaricamento():
    global canzoneAttuale
    canzoneAttuale = "00-Menu"
    canzone = CaricaFileProgetto.loadSound("Risorse/Audio/Canzoni/" + canzoneAttuale + ".wav")
    GlobalHWVar.canaleSoundCanzone.play(canzone, -1)

    schemataDiCaricamento = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/SchermataDiCaricamento.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
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
mostraLogo()
disegnaSchermataDiCaricamento()
numImgCaricata = 0
GlobalImgVar.loadImgs(numImgCaricata, cambioRisoluzione=False)
numSndCaricato = 0
GlobalSndVar.loadSounds(numSndCaricato)
