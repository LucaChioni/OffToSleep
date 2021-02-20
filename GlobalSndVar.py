# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar


# dichiaro le variabili globali della funzione loadSounds
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
global audioAmbienteStradaPerCitta1_1
global audioAmbienteStradaPerCitta1_2
global audioAmbienteStradaPerCitta2_1
global audioAmbienteStradaPerCitta2_2
global audioAmbienteStradaPerCitta3_1
global audioAmbienteStradaPerCitta3_2
global canzoneEsternoCitta
global canzoneEsternoCasa
global rumoreBussareCitta
global rumoreSollevamentoPortaCitta
global canzoneCasaDavid
global audioAmbienteCasaDavid_1
global audioAmbienteCasaDavid_2
global suonoaperturaporteCasaDavid
global suonochiusuraporteCasaDavid
global rumoreDoccia

def loadSound(path):
    try:
        sound = pygame.mixer.Sound(GlobalHWVar.gamePath + path)
    except Exception:
        print ("Impossibile caricare " + path)
        sound = False

    # per poter chiudere il gioco durante il caricamento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    GlobalHWVar.listaTastiPremuti = []

    return sound

numSndTotali = 55
def caricaSuonoMostrandoAvanzamento(path):
    global numSndCaricatoTemp
    suono = loadSound(path)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscuPiuScu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 6.5, int(GlobalHWVar.gpx * 16), GlobalHWVar.gpy * 1))
    numSndCaricatoTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 15) + ((GlobalHWVar.gpx * 1.0 / numSndTotali) * numSndCaricatoTemp)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 6.5, int(caricamentoCompiuto), GlobalHWVar.gpy * 1))
    GlobalHWVar.aggiornaSchermo()
    return suono

def loadSounds(numSndCaricato):
    global numSndCaricatoTemp
    numSndCaricatoTemp = numSndCaricato

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
    global audioAmbienteStradaPerCitta1_1
    global audioAmbienteStradaPerCitta1_2
    global audioAmbienteStradaPerCitta2_1
    global audioAmbienteStradaPerCitta2_2
    global audioAmbienteStradaPerCitta3_1
    global audioAmbienteStradaPerCitta3_2
    global canzoneEsternoCitta
    global canzoneEsternoCasa
    global rumoreBussareCitta
    global rumoreSollevamentoPortaCitta
    global canzoneCasaDavid
    global audioAmbienteCasaDavid_1
    global audioAmbienteCasaDavid_2
    global suonoaperturaporteCasaDavid
    global suonochiusuraporteCasaDavid
    global rumoreDoccia

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

    # effetti speciali
    suonoaperturacofanetti = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/AperturaCofanetto.wav")
    suonoAperturaMappa = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/AperturaMappa.wav")
    rumoreScavare = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/Scavare.wav")
    rumoreBussareCitta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/BussareCittà.wav")
    rumoreSollevamentoPortaCitta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SollevamentoPortaCittà.wav")
    rumoreDoccia = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/DocciaCasaUfficiale.wav")

    # suoni apertura-chiusura porte
    suonoaperturaporteForesta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SuoniPorte/AperturaPortaForesta.wav")
    suonochiusuraporteForesta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaForesta.wav")
    suonoaperturaporteCasa = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasa.wav")
    suonochiusuraporteCasa = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasa.wav")
    suonoaperturaporteCasaDavid = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasaUfficiale.wav")
    suonochiusuraporteCasaDavid = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasaUfficiale.wav")

    # suoni sottofondi ambientali
    audioAmbienteSogno = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/Sogno.wav")
    audioAmbienteCasaInterno = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/CasaInterno.wav")
    audioAmbienteCasaEsterno = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/CasaEsterno.wav")
    audioAmbienteForesta = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/Foresta.wav")
    audioAmbienteForestaFuoco = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/ForestaFuoco.wav")
    audioAmbienteStradaPerCitta1_1 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1-1.wav")
    audioAmbienteStradaPerCitta1_2 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta1-2.wav")
    audioAmbienteStradaPerCitta2_1 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2-1.wav")
    audioAmbienteStradaPerCitta2_2 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta2-2.wav")
    audioAmbienteStradaPerCitta3_1 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3-1.wav")
    audioAmbienteStradaPerCitta3_2 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/StradaPerCitta3-2.wav")
    audioAmbienteCasaDavid_1 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/CasaUfficiale-1.wav")
    audioAmbienteCasaDavid_2 = caricaSuonoMostrandoAvanzamento("Audio/RumoriAmbiente/SottofondoPerZona/CasaUfficiale-2.wav")

    # suoni canzoni
    canzoneSogno = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/01-Sogno.wav")
    canzoneCasa = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/02-Casa.wav")
    canzoneEsternoCasa = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/03-EsternoCasaCittà.wav")
    canzoneForesta = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/04-Foresta.wav")
    canzoneEsternoCitta = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/03-EsternoCasaCittà.wav")
    canzoneCasaDavid = caricaSuonoMostrandoAvanzamento("Audio/Canzoni/05-CasaUfficiale.wav")
