# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


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
global suonoRaccoltaOggetto
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
global rumoreMovimentoNemici
global rumoreMovimentoPersonaggi
global rumoreAttaccoNemico
global rumoreLancioOggettoNemico
global rumoreMorteNemico
global rumoreDialoghiInterlocutoriN
global rumoreDialoghiInterlocutoriM
global rumoreDialoghiInterlocutoriF
global suonoAperturaMappa
global rumoreScavare
global rumoreBussareCitta
global rumoreSollevamentoPortaCitta
global suonoaperturaporteCasaDavid
global suonochiusuraporteCasaDavid
global rumoreDoccia
global rumoreChiusuraPortaCitta
global rumoreLancioPallaBibliotecario
global rumoreRitornoPallaBibliotecario
global rumoreAppoggioStrumentoEnigmi
global rumoreScorrimentoMatitaEnigmi
global rumoreScorrimentoGommaEnigmi
global rumoreCancellaTuttoEnigmi
global suonoaperturaporteSelva
global suonochiusuraporteSelva
global rumoreAperturaCancelloCastello
global rumorePortoniCambioStanza
global suonoaperturaporteCastello
global suonochiusuraporteCastello
global rumoreMovimentoVestiti
global rumoreCucchiaioSuPiatto
global rumoreBussarePortaUfficioNeil
global rumorePianoAscensoreCastello
global rumoreBattitoCardiaco
global rumoreAttimoPericoloso
global rumoreVomito
global rumoreMelodiaFantasticare
global suonoaperturaportePalazzoDiRod
global suonochiusuraportePalazzoDiRod
global rumoreLevaTunnelDiRod
global rumoreTuffoLago
global rumoreSbloccoPorta


numSndTotali = 82
def caricaSuonoMostrandoAvanzamento(path):
    global numSndCaricatoTemp
    suono = CaricaFileProgetto.loadSound(path)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(GlobalHWVar.gpx * 31), GlobalHWVar.gpy * 0.5))
    numSndCaricatoTemp += 1
    caricamentoCompiuto = (GlobalHWVar.gpx * 30) + ((GlobalHWVar.gpx * 1.0 / numSndTotali) * numSndCaricatoTemp)
    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 0.5), GlobalHWVar.gpy * 17, int(caricamentoCompiuto), GlobalHWVar.gpy * 0.5))
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
    global suonoRaccoltaOggetto
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
    global rumoreMovimentoNemici
    global rumoreMovimentoPersonaggi
    global rumoreAttaccoNemico
    global rumoreLancioOggettoNemico
    global rumoreMorteNemico
    global rumoreDialoghiInterlocutoriN
    global rumoreDialoghiInterlocutoriM
    global rumoreDialoghiInterlocutoriF
    global suonoAperturaMappa
    global rumoreScavare
    global rumoreBussareCitta
    global rumoreSollevamentoPortaCitta
    global suonoaperturaporteCasaDavid
    global suonochiusuraporteCasaDavid
    global rumoreDoccia
    global rumoreChiusuraPortaCitta
    global rumoreLancioPallaBibliotecario
    global rumoreRitornoPallaBibliotecario
    global rumoreAppoggioStrumentoEnigmi
    global rumoreScorrimentoMatitaEnigmi
    global rumoreScorrimentoGommaEnigmi
    global rumoreCancellaTuttoEnigmi
    global suonoaperturaporteSelva
    global suonochiusuraporteSelva
    global rumoreAperturaCancelloCastello
    global rumorePortoniCambioStanza
    global suonoaperturaporteCastello
    global suonochiusuraporteCastello
    global rumoreMovimentoVestiti
    global rumoreCucchiaioSuPiatto
    global rumoreBussarePortaUfficioNeil
    global rumorePianoAscensoreCastello
    global rumoreBattitoCardiaco
    global rumoreAttimoPericoloso
    global rumoreVomito
    global rumoreMelodiaFantasticare
    global suonoaperturaportePalazzoDiRod
    global suonochiusuraportePalazzoDiRod
    global rumoreLevaTunnelDiRod
    global rumoreTuffoLago
    global rumoreSbloccoPorta

    # suoni puntatore
    selsta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelSta.wav")
    selind = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelInd.wav")
    spostapun = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SpostaPun.wav")
    selimp = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelImp.wav")
    selezione = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/Selezione.wav")
    spostaPunBattaglia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SpostaPunBattaglia.wav")
    selObbiettivo = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPuntatore/SelObbiettivo.wav")

    # suoni personaggio
    rumoreAttaccoSpada = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/AttaccoSpada.wav")
    rumoreLancioFreccia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/LancioFreccia.wav")
    rumoreAttaccoArco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/AttaccoArco.wav")
    rumoreParata = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/ParataConScudo.wav")
    rumorecamminata = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/Camminata.wav")
    rumorelevelup = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/Levelup.wav")
    rumoreMorte = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriPersonaggio/Morte.wav")

    # suoni robo
    rumoreCamminataColco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Camminata.wav")
    rumoreScossaFreccia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/ScossaFreccia.wav")
    rumoreTempestaElettrica = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/TempestaElettrica.wav")
    rumoreCuraRobo = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Cura.wav")
    rumoreAntidoto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Antidoto.wav")
    rumoreAttPDifP = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/AttPDifP.wav")
    rumoreAutoricarica = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Autoricarica.wav")
    rumoreRaffreddamento = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/Raffreddamento.wav")
    rumoreVelocizzaEfficienza = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriColco/VelocizzaEfficienza.wav")

    # suono oggetti
    suonoTeleColco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/TeleColco.wav")
    suonoLancioOggetti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/LancioOggetti.wav")
    suonoUsoPozione = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Pozione.wav")
    suonoUsoCaricabatterie = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Caricabatterie.wav")
    suonoUsoMedicina = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Medicina.wav")
    suonoUsoBomba = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Bomba.wav")
    suonoUsoBombaVeleno = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/BombaVeleno.wav")
    suonoUsoEsca = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/Esca.wav")
    suonoUsoBombaAppiccicosa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/BombaAppiccicosa.wav")
    suonoUsoBombaPotenziata = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriOggetti/BombaPotenziata.wav")

    # suoni nemici - personaggi
    rumoreMovimentoNemici = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MovimentoNemici.wav")
    rumoreMovimentoPersonaggi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MovimentoPersonaggi.wav")
    rumoreAttaccoNemico = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/AttaccoVicinoNemico.wav")
    rumoreLancioOggettoNemico = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/AttaccoLontanoNemico.wav")
    rumoreMorteNemico = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriNemiciPersonaggi/MorteNemico.wav")

    # suono dialoghi
    rumoreDialoghiInterlocutoriM = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriDialoghi/DialoghiInterlocutoriM.wav")
    rumoreDialoghiInterlocutoriN = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriDialoghi/DialoghiInterlocutoriN.wav")
    rumoreDialoghiInterlocutoriF = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriDialoghi/DialoghiInterlocutoriF.wav")

    # effetti speciali generici
    suonoRaccoltaOggetto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/RaccoltaOggetto.wav")
    suonoRaccoltaMonete = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/RaccoltaMonete.wav")
    rumoreAcquisto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Acquisto.wav")
    suonoaperturacofanetti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/AperturaCofanetto.wav")
    suonoAperturaMappa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/AperturaMappa.wav")
    rumorePianoAscensoreCastello = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/PianoAscensoreCastello.wav")

    # effetti speciali enigmi
    rumoreLancioPallaBibliotecario = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Enigmi/LancioPallaBibliotecario.wav")
    rumoreRitornoPallaBibliotecario = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Enigmi/RitornoPallaBibliotecario.wav")
    rumoreAppoggioStrumentoEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Enigmi/AppaggioMatitaEnigmi.wav")
    rumoreScorrimentoMatitaEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Enigmi/ScorrimentoMatitaEnigmi.wav")
    rumoreScorrimentoGommaEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Enigmi/ScorrimentoGommaEnigmi.wav")
    rumoreCancellaTuttoEnigmi = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Enigmi/CancellaTuttoEnigmi.wav")

    # effetti speciali eventi
    rumoreScavare = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/Scavare.wav")
    rumoreBussareCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/BussareCittà.wav")
    rumoreSollevamentoPortaCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/SollevamentoPortaCittà.wav")
    rumoreChiusuraPortaCitta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/AbbassamentoPortaCittà.wav")
    rumoreDoccia = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/DocciaCasaUfficiale.wav")
    rumoreMovimentoVestiti = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/MovimentoVestiti.wav")
    rumoreCucchiaioSuPiatto = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/CucchiaioSuPiatto.wav")
    rumoreAperturaCancelloCastello = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/AperturaCancelloCastello.wav")
    rumoreBussarePortaUfficioNeil = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/BussarePortaUfficioNeil.wav")
    rumoreBattitoCardiaco = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/BattitoCardiaco.wav")
    rumoreAttimoPericoloso = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/AttimoPericoloso.wav")
    rumoreVomito = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/Vomito.wav")
    rumoreMelodiaFantasticare = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/MelodiaFantasticare.wav")
    rumoreLevaTunnelDiRod = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/LevaSbarreGrotta.wav")
    rumoreTuffoLago = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/TuffoLago.wav")
    rumoreSbloccoPorta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/Eventi/SbloccoPorta.wav")

    # suoni apertura-chiusura porte
    rumorePortoniCambioStanza = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/PortoniCambioStanza.wav")
    suonoaperturaporteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaForesta.wav")
    suonochiusuraporteForesta = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaForesta.wav")
    suonoaperturaporteCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasa.wav")
    suonochiusuraporteCasa = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasa.wav")
    suonoaperturaporteCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCasaUfficiale.wav")
    suonochiusuraporteCasaDavid = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCasaUfficiale.wav")
    suonoaperturaporteSelva = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaSelva.wav")
    suonochiusuraporteSelva = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaSelva.wav")
    suonoaperturaporteCastello = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaCastello.wav")
    suonochiusuraporteCastello = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaCastello.wav")
    suonoaperturaportePalazzoDiRod = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/AperturaPortaPalazzoDiRod.wav")
    suonochiusuraportePalazzoDiRod = caricaSuonoMostrandoAvanzamento("Risorse/Audio/RumoriAmbiente/SuoniPorte/ChiusuraPortaPalazzoDiRod.wav")
