# -*- coding: utf-8 -*-

# import psutil
import os
import pygame
import datetime
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.CaricaSalvaPartita as CaricaSalvaPartita
import Codice.SettaggiLivelli.SetImgOggettiMappaPersonaggi as SetImgOggettiMappaPersonaggi
import Codice.GestioneMenu.MenuPrincipali as MenuPrincipali
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneMenu.MenuEnigmi as MenuEnigmi
import Codice.GestioneMenu.SottoMenuSalva as SottoMenuSalva
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneGrafica.EnvPrint as EnvPrint
import Codice.GestioneGrafica.Animazioni as Animazioni
import Codice.GestioneNemiciPersonaggi.MovNemiciRob as MovNemiciRob
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.FunzioniGeneriche.UtilityOstacoliContenutoCofanetti as UtilityOstacoliContenutoCofanetti
import Codice.SettaggiLivelli.SetNemiciPersonaggiEventi as SetNemiciPersonaggiEventi
import Codice.SettaggiLivelli.SetOstacoliContenutoCofanetti as SetOstacoliContenutoCofanetti
import Codice.SettaggiLivelli.SetPosizProtagonistaAudio as SetPosizProtagonistaAudio
import Codice.SettaggiLivelli.SetZoneStanzeImpedimenti as SetZoneStanzeImpedimenti
import Codice.SettaggiLivelli.SetDialoghiPersonaggi as SetDialoghiPersonaggi
import Codice.FunzioniGeneriche.FunzioniPerTest as FunzioniPerTest


def gameloop():
    # p = psutil.Process()
    # maxMemoryUsage = 0
    caricaSalvataggio = False
    inizio = True
    gameover = False
    # inizializzo tutte le variabili
    if True:
        casellaVuotaPreset = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)

        listaNemiciSotterrati = []
        avanzaManualmentePercorsoDaEseguire = False
        evitaAggiornamentoStatoInizioTurno = True
        cambiatoRisoluzione = False
        riavviaAudioMusica = False
        riavviaAudioAmbiente = False
        canzone = False
        listaSottofondoAmbientale = []
        evitaAvanzamentoTurno = False
        caseattactotRallo = []
        posizioneRalloAggiornamentoCaseAttac = [0, 0]
        saltaTurno = False
        movimentoDaCompiere = False
        percorsoDaEseguire = []
        nonMostrarePersonaggio = False
        avanzaIlTurnoSenzaMuoverti = False
        evitaTurnoDiColco = False
        aggiornaImgEquip = True
        refreshSchermo = True
        impossibileAprirePorta = False
        stanzaCambiata = False
        uscitoDaMenu = 0
        # rumore porte (dipende dalla stanza)
        rumoreAperturaPorte = 0
        rumoreChiusuraPorte = 0
        animaOggetto = [False, 0, 0]
        raffreddamento = False
        ricarica1 = False
        ricarica2 = False
        nemicoInquadrato = False
        spingiColco = False
        apriChiudiPorta = [False, 0, 0]
        apriCofanetto = [False, 0, 0]
        interagisciConPersonaggio = False
        oggettoRicevuto = False
        visualizzaMenuMercante = False
        stanzaVecchia = 0
        tesoro = -1
        apriocchio = False
        sposta = False
        bottoneDown = False
        startf = False
        aumentoliv = 0
        primopasso = True
        xesca = 0
        yesca = 0
        creaesca = False
        attacco = 0
        difesa = 0
        nx = 0
        ny = 0

        dati = []
        tutteporte = []
        tutticofanetti = []
        listaNemiciTotali = []
        vettoreEsche = []
        vettoreDenaroTotale = []
        vettoreDenaroStanza = []
        stanzeGiaVisitate = []
        listaPersonaggiTotali = []
        listaAvanzamentoDialoghi = []
        oggettiRimastiAHans = []
        ultimoObbiettivoColco = []
        obbiettivoCasualeColco = False

        # controlla se devi cambiare personaggio giocabile
        personaggioDaUsare = "Sara1"
        personaggioUsato = personaggioDaUsare
        pers = casellaVuotaPreset
        robot = casellaVuotaPreset

        # vettore porte -> porte[stanza, x, y, True/False, ...]
        porte = []
        # vettore cofanetti -> cofanetti[stanza, x, y, True/False, ...]
        cofanetti = []

        x = 0
        y = 0
        vx = x
        vy = y
        # 1->d , 2->a , 3->w , 4->s
        npers = 1
        rx = 0
        ry = 0
        vrx = rx
        vry = ry
        chiamarob = False
        caselleAttaccabiliColco = []
        posizioneColcoAggiornamentoCaseAttac = [rx, ry]
        raffredda = 0
        autoRic1 = 0
        autoRic2 = 0
        # 1->d , 2->a , 3->s , 4->w
        nrob = 3
        mosseRimasteRob = 0
        morterob = False

        listaPersonaggi = []
        listaNemici = []

        carim = True
        cambiosta = True
        impossibileCliccarePulsanti = True

        # stanza
        imgSfondoStanza = casellaVuotaPreset
        portaVert = False
        portaOriz = False
        imgNemicoSotterrato = casellaVuotaPreset

        caseviste = []
        casevisteDaRallo = []
        casevisteEntrateIncluse = []
        caselleNonVisibili = []
        casellePercorribili = []
        casellePercorribiliPorteEscluse = []
        entrateStanza = []

        vettoreImgCaselle = []

        # arma
        armaw = casellaVuotaPreset
        armawMov1 = casellaVuotaPreset
        armawMov2 = casellaVuotaPreset
        armaa = casellaVuotaPreset
        armaaMov1 = casellaVuotaPreset
        armaaMov2 = casellaVuotaPreset
        armas = casellaVuotaPreset
        armasMov1 = casellaVuotaPreset
        armasMov2 = casellaVuotaPreset
        armad = casellaVuotaPreset
        armadMov1 = casellaVuotaPreset
        armadMov2 = casellaVuotaPreset
        armasAttacco = casellaVuotaPreset
        armaaAttacco = casellaVuotaPreset
        armadAttacco = casellaVuotaPreset
        armawAttacco = casellaVuotaPreset
        # arco
        arcow = casellaVuotaPreset
        arcoa = casellaVuotaPreset
        arcos = casellaVuotaPreset
        arcod = casellaVuotaPreset
        arcosAttacco = casellaVuotaPreset
        arcoaAttacco = casellaVuotaPreset
        arcodAttacco = casellaVuotaPreset
        arcowAttacco = casellaVuotaPreset
        # faretra
        faretraw = casellaVuotaPreset
        faretraa = casellaVuotaPreset
        faretras = casellaVuotaPreset
        faretrad = casellaVuotaPreset
        # armatura
        armaturaw = casellaVuotaPreset
        armaturaa = casellaVuotaPreset
        armaturas = casellaVuotaPreset
        armaturad = casellaVuotaPreset
        # scudo
        scudow = casellaVuotaPreset
        scudoa = casellaVuotaPreset
        scudos = casellaVuotaPreset
        scudod = casellaVuotaPreset
        scudoDifesa = casellaVuotaPreset
        # guanti
        guantiw = casellaVuotaPreset
        guantiwMov1 = casellaVuotaPreset
        guantiwMov2 = casellaVuotaPreset
        guantia = casellaVuotaPreset
        guantiaMov1 = casellaVuotaPreset
        guantiaMov2 = casellaVuotaPreset
        guantis = casellaVuotaPreset
        guantisMov1 = casellaVuotaPreset
        guantisMov2 = casellaVuotaPreset
        guantid = casellaVuotaPreset
        guantidMov1 = casellaVuotaPreset
        guantidMov2 = casellaVuotaPreset
        guantisAttacco = casellaVuotaPreset
        guantiaAttacco = casellaVuotaPreset
        guantidAttacco = casellaVuotaPreset
        guantiwAttacco = casellaVuotaPreset
        guantiDifesa = casellaVuotaPreset
        # collana
        collanaw = casellaVuotaPreset
        collanaa = casellaVuotaPreset
        collanas = casellaVuotaPreset
        collanad = casellaVuotaPreset
        # armatura robot
        armrobw = casellaVuotaPreset
        armroba = casellaVuotaPreset
        armrobs = casellaVuotaPreset
        armrobd = casellaVuotaPreset

        arma = casellaVuotaPreset
        armaMov1 = casellaVuotaPreset
        armaMov2 = casellaVuotaPreset
        armaAttacco = casellaVuotaPreset
        armatura = casellaVuotaPreset
        scudo = casellaVuotaPreset
        arco = casellaVuotaPreset
        faretra = casellaVuotaPreset
        arcoAttacco = casellaVuotaPreset
        guanti = casellaVuotaPreset
        guantiMov1 = casellaVuotaPreset
        guantiMov2 = casellaVuotaPreset
        guantiAttacco = casellaVuotaPreset
        collana = casellaVuotaPreset
        armrob = casellaVuotaPreset

        statoRalloInizioTurno = [0, 0, 0, 0]
        pvtot = 0
        statoColcoInizioTurno = [0, 0, 0, 0]
        entot = 0
        statoEscheInizioTurno = []

        caricaTutto = True

    while True:
        # memoriaUsata = p.memory_info().rss / 1000000.0
        # if memoriaUsata > maxMemoryUsage:
        #     maxMemoryUsage = memoriaUsata
        #     print (u"Max RAM necessitata: " + str(maxMemoryUsage) + " MB")

        if inizio:
            listaNemiciSotterrati = []
            cambiatoRisoluzione = False
            if not gameover:
                riavviaAudioMusica = False
                riavviaAudioAmbiente = False
                canzone = False
                listaSottofondoAmbientale = []
            avanzaManualmentePercorsoDaEseguire = False
            evitaAvanzamentoTurno = False
            caseattactotRallo = []
            posizioneRalloAggiornamentoCaseAttac = [0, 0]
            saltaTurno = False
            movimentoDaCompiere = False
            percorsoDaEseguire = []
            nonMostrarePersonaggio = False
            avanzaIlTurnoSenzaMuoverti = False
            evitaTurnoDiColco = False
            aggiornaImgEquip = True
            refreshSchermo = True
            impossibileAprirePorta = False
            stanzaCambiata = False
            uscitoDaMenu = 0
            # rumore porte (dipende dalla stanza)
            rumoreAperturaPorte = 0
            rumoreChiusuraPorte = 0
            animaOggetto = [False, 0, 0]
            raffreddamento = False
            ricarica1 = False
            ricarica2 = False
            nemicoInquadrato = False
            spingiColco = False
            apriChiudiPorta = [False, 0, 0]
            apriCofanetto = [False, 0, 0]
            interagisciConPersonaggio = False
            oggettoRicevuto = False
            visualizzaMenuMercante = False
            stanzaVecchia = 0
            tesoro = -1
            apriocchio = False
            sposta = False
            bottoneDown = False
            startf = False
            aumentoliv = 0
            primopasso = True
            xesca = 0
            yesca = 0
            creaesca = False
            attacco = 0
            difesa = 0
            nx = 0
            ny = 0

            dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaroTotale, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco = MenuPrincipali.menu(caricaSalvataggio, gameover)
            # print ("Salvataggio: " + str(GlobalGameVar.numSalvataggioCaricato))

            # decido dove ripartire per il prossimo salvataggio
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["oltreFinale"]:
                GlobalGameVar.partitaAppenaAvviataPostFinale = True
                if dati[0] == GlobalGameVar.dictAvanzamentoStoria["oltreFinale"] or dati[0] == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCittà"]:
                    dati[0] = GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCasa"]
                    dati[1] = GlobalGameVar.dictStanze["casaHansSara1"]
                    dati[2] = GlobalHWVar.gpx * 6
                    dati[3] = GlobalHWVar.gpx * 13
                    # npers: 1=d, 2=a, 3=w, 4=s
                    dati[140] = 2
                    nonMostrarePersonaggio = True
                elif dati[0] == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCasa"]:
                    dati[0] = GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCalcolatore"]
                    dati[1] = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                    dati[2] = GlobalHWVar.gpx * 15
                    dati[3] = GlobalHWVar.gpx * 7
                    # npers: 1=d, 2=a, 3=w, 4=s
                    dati[140] = 4
                    nonMostrarePersonaggio = True
                elif dati[0] == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCalcolatore"]:
                    dati[0] = GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaSpecchio"]
                    dati[1] = GlobalGameVar.dictStanze["internoCastello21"]
                    dati[2] = GlobalHWVar.gpx * 27
                    dati[3] = GlobalHWVar.gpx * 8
                    # npers: 1=d, 2=a, 3=w, 4=s
                    dati[140] = 1
                elif dati[0] == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaSpecchio"]:
                    dati[0] = GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaRod"]
                    dati[1] = GlobalGameVar.dictStanze["palazzoDiRod3"]
                    dati[2] = GlobalHWVar.gpx * 25
                    dati[3] = GlobalHWVar.gpx * 5
                    # npers: 1=d, 2=a, 3=w, 4=s
                    dati[140] = 1
                elif dati[0] == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaRod"]:
                    dati[0] = GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCittà"]
                    dati[1] = GlobalGameVar.dictStanze["stradaPerCittà3"]
                    dati[2] = GlobalHWVar.gpx * 14
                    dati[3] = GlobalHWVar.gpx * 13
                    # npers: 1=d, 2=a, 3=w, 4=s
                    dati[140] = 4
                datiAttualiTotali = [dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaroTotale, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco]
                CaricaSalvaPartita.salvataggio(GlobalGameVar.numSalvataggioCaricato, datiAttualiTotali, datiAttualiTotali[:])

            # se è nuova partita => mostro schemata con citazione e imposto il tempo d'inizio di gioco
            if GlobalGameVar.numSalvataggioCaricato == 0 and not gameover:
                FunzioniGraficheGeneriche.mostraSchermataCitazione()
                GlobalHWVar.tempoInizioPartita = datetime.datetime.now()

            gameover = False
            # controlla se devi cambiare personaggio giocabile
            personaggioDaUsare = SetImgOggettiMappaPersonaggi.cambiaProtagonista(dati[0])
            personaggioUsato = personaggioDaUsare
            caricaSalvataggio = False
            pers = GlobalImgVar.perss
            robot = GlobalImgVar.robos

            # vettore porte -> porte[stanza, x, y, True/False, ...]
            porte = []
            # vettore cofanetti -> cofanetti[stanza, x, y, True/False, ...]
            cofanetti = []

            x = dati[2]
            y = dati[3]
            vx = x
            vy = y
            # 1->d , 2->a , 3->w , 4->s
            npers = dati[140]
            rx = dati[134]
            ry = dati[135]
            vrx = rx
            vry = ry
            chiamarob = dati[142]
            caselleAttaccabiliColco = []
            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            raffredda = dati[136]
            autoRic1 = dati[137]
            autoRic2 = dati[138]
            # 1->d , 2->a , 3->s , 4->w
            nrob = dati[141]
            mosseRimasteRob = dati[139]
            if dati[10] > 0:
                morterob = False
            else:
                morterob = True
            GlobalGameVar.pazzoStrabico = dati[143]
            GlobalGameVar.cambiataAlCastello[0] = dati[144]
            GlobalGameVar.cambiataAlCastello[1] = dati[144]

            listaPersonaggi = []
            listaNemici = []

            SetPosizProtagonistaAudio.decidiSeDimezzareVolumeMusica(dati[0])

            statoRalloInizioTurno = []
            statoRalloInizioTurno.append(dati[5])
            statoRalloInizioTurno.append(dati[121])
            statoRalloInizioTurno.append(dati[123])
            statoRalloInizioTurno.append(dati[124])
            statoColcoInizioTurno = []
            statoColcoInizioTurno.append(dati[10])
            statoColcoInizioTurno.append(dati[122])
            statoColcoInizioTurno.append(dati[125])
            statoColcoInizioTurno.append(dati[126])

            carim = True
            cambiosta = True
            impossibileCliccarePulsanti = True

        # caricare gli oggetti
        if carim:
            evitaAggiornamentoStatoInizioTurno = True
            # aggiorno presenza di Impo
            SetZoneStanzeImpedimenti.settaPresenzaDiColco(dati[0])

            # aggiorno le img del personaggio giocabile
            personaggioDaUsare = SetImgOggettiMappaPersonaggi.cambiaProtagonista(dati[0], personaggioUsato)
            if personaggioDaUsare != personaggioUsato:
                personaggioUsato = personaggioDaUsare
                npers = 4

            if cambiosta or cambiatoRisoluzione:
                listaNemiciSotterrati = []
                posizioneRalloAggiornamentoCaseAttac = [0, 0]
                if not inizio and not cambiatoRisoluzione:
                    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)

                # carica i cofanetti nella stanza (svuoto e riempio il vettore)
                i = 0
                while i < len(cofanetti):
                    del cofanetti[i + 3]
                    del cofanetti[i + 2]
                    del cofanetti[i + 1]
                    del cofanetti[i]
                i = 0
                while i < len(tutticofanetti):
                    if tutticofanetti[i] == dati[1]:
                        cofanetti.append(tutticofanetti[i])
                        cofanetti.append(tutticofanetti[i + 1])
                        cofanetti.append(tutticofanetti[i + 2])
                        cofanetti.append(tutticofanetti[i + 3])
                    i = i + 4
                # carica le porte nella stanza (svuoto e riempio il vettore)
                i = 0
                while i < len(porte):
                    del porte[i + 3]
                    del porte[i + 2]
                    del porte[i + 1]
                    del porte[i]
                i = 0
                while i < len(tutteporte):
                    if tutteporte[i] == dati[1]:
                        porte.append(tutteporte[i])
                        porte.append(tutteporte[i + 1])
                        porte.append(tutteporte[i + 2])
                        porte.append(tutteporte[i + 3])
                    i += 4
                vettoreDenaroStanza = []
                i = 0
                while i < len(vettoreDenaroTotale):
                    if vettoreDenaroTotale[i + 3] == dati[1]:
                        vettoreDenaroStanza.append(vettoreDenaroTotale[i])
                        vettoreDenaroStanza.append(vettoreDenaroTotale[i + 1])
                        vettoreDenaroStanza.append(vettoreDenaroTotale[i + 2])
                    i += 4

                # decido se rendere le porte e i cofanetti non interagibili
                porte = SetZoneStanzeImpedimenti.decidiInteragibilitaPorte(dati[0], porte)
                cofanetti = SetZoneStanzeImpedimenti.decidiInteragibilitaCofanetti(dati[0], dati[1], cofanetti)

                if cambiosta:
                    # resetto l'animazione del valore dei danni
                    GlobalGameVar.datiAnimazioniDanniInflitti["dannoRallo"] = [False, 0, -1]
                    GlobalGameVar.datiAnimazioniDanniInflitti["dannoImpo"] = [False, 0, -1]
                    GlobalGameVar.datiAnimazioniDanniInflitti["dannoEsche"] = [False, 0, -1]
                    GlobalGameVar.datiAnimazioniDanniInflitti["dannoNemico"] = [False, 0, -1]

                    # necessario ridefinire le stanze pacifiche in caso di carica partita nel castello (inizialmente quelle stanze sono pacifiche)
                    SetZoneStanzeImpedimenti.modificaStanzePacifiche(dati[0])

                    SetZoneStanzeImpedimenti.scriviNomeZona(dati[1], stanzaVecchia, attesa=False)
                    stoppaMusica = SetPosizProtagonistaAudio.decidiSeStoppareMusica(dati[1], dati[0])
                    stoppaAudioAmbientale = SetPosizProtagonistaAudio.decidiSeStoppareAudioAmbientale(dati[1], dati[0])
                    SetPosizProtagonistaAudio.riproduciAudioSpeciali(dati[0])

                    canzoneCambiata = False
                    sottofondoAmbientaleCambiato = False
                    # mi posiziono e setto canzone, sottofondo ambientale e rumore porte
                    x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, listaSottofondoAmbientale, bottoneDown, dati[0], mantieniPosizioneImpo = SetPosizProtagonistaAudio.settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, dati[1], stanzaVecchia, canzone, listaSottofondoAmbientale, inizio, dati[0], bottoneDown)
                    if not inizio:
                        vx = x
                        vy = y
                        if GlobalGameVar.impoPresente and not mantieniPosizioneImpo:
                            rx = x
                            ry = y
                            vrx = x
                            vry = y
                            # nrob: 1=d, 2=a, 3=s, 4=w
                            if npers == 1:
                                nrob = 1
                            if npers == 2:
                                nrob = 2
                            if npers == 3:
                                nrob = 4
                            if npers == 4:
                                nrob = 3
                    if not GlobalGameVar.impoPresente:
                        rx = GlobalHWVar.gsx
                        ry = GlobalHWVar.gsy
                        vrx = rx
                        vry = ry

                    # aggiorno presenza di Impo (perché altrimenti non riappare subito dopo che entri in internoCastello21 prima dell'operazione per bloccare il tempo)
                    if dati[0] == GlobalGameVar.dictAvanzamentoStoria["riapparsoImpoInternoCastello20PostRianimazione"]:
                        SetZoneStanzeImpedimenti.settaPresenzaDiColco(dati[0])
                        rx = GlobalHWVar.gpx * 15
                        ry = GlobalHWVar.gpy * 13
                        dati[10] = 0
                        dati[122] = 0
                        dati[125] = 0
                        dati[126] = 0

                    if stoppaMusica and GlobalHWVar.canaleSoundCanzone.get_busy():
                        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
                        GlobalHWVar.canaleSoundCanzone.stop()
                    if stoppaAudioAmbientale and GlobalHWVar.canaliSoundSottofondoAmbientale.getBusy():
                        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [0], False)
                        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
                    if riavviaAudioMusica:
                        canzoneCambiata = True
                    if riavviaAudioAmbiente:
                        sottofondoAmbientaleCambiato = True
                    riavviaAudioMusica = False
                    riavviaAudioAmbiente = False
                    if canzoneCambiata or sottofondoAmbientaleCambiato:
                        canaliDaMutare = []
                        volumiAzzerati = []
                        posizioneCanaleMusica = -1
                        if canzoneCambiata:
                            canaliDaMutare.append(GlobalHWVar.canaleSoundCanzone)
                            volumiAzzerati.append(0)
                            posizioneCanaleMusica = 0
                        if sottofondoAmbientaleCambiato:
                            canaliDaMutare.append(GlobalHWVar.canaliSoundSottofondoAmbientale)
                            volumiAzzerati.append(0)
                        GenericFunc.cambiaVolumeCanaliAudio(canaliDaMutare, volumiAzzerati, False, posizioneCanaleMusica=posizioneCanaleMusica)
                        if canzoneCambiata:
                            GlobalHWVar.canaleSoundCanzone.stop()
                            if canzone and not stoppaMusica:
                                GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
                        if sottofondoAmbientaleCambiato:
                            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
                            if len(listaSottofondoAmbientale) > 0 and not stoppaAudioAmbientale:
                                GlobalHWVar.canaliSoundSottofondoAmbientale.riproduci(listaSottofondoAmbientale)
                        canaliDaRiavviare = []
                        volumiRiattivati = []
                        posizioneCanaleMusica = -1
                        if canzoneCambiata:
                            canaliDaRiavviare.append(GlobalHWVar.canaleSoundCanzone)
                            volumiRiattivati.append(GlobalHWVar.volumeCanzoni)
                            posizioneCanaleMusica = 0
                        if sottofondoAmbientaleCambiato:
                            canaliDaRiavviare.append(GlobalHWVar.canaliSoundSottofondoAmbientale)
                            volumiRiattivati.append(GlobalHWVar.volumeEffetti)
                        GenericFunc.cambiaVolumeCanaliAudio(canaliDaRiavviare, volumiRiattivati, False, posizioneCanaleMusica=posizioneCanaleMusica)

                    SetZoneStanzeImpedimenti.scriviNomeZona(dati[1], stanzaVecchia, attesa=True)
                    SetZoneStanzeImpedimenti.mostraTempoPassato(dati[0], dati[1], stanzaVecchia)

                    # resetto obiettivo Colco
                    if not inizio:
                        ultimoObbiettivoColco = []
                        obbiettivoCasualeColco = False

                    # carico nemici e personaggi nella stanza
                    listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi = SetNemiciPersonaggiEventi.caricaNemiciEPersonaggi(dati[0], dati[1], stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi, listaPersonaggi, cofanetti)
                    stanzaVecchia = dati[1]
                    # metto i nemici nella posizione originale se sono nella nostra stessa casella
                    for nemico in listaNemici:
                        if nemico.x == x and nemico.y == y:
                            nemico.x, nemico.y = nemico.posizioneOriginale
                            nemico.vx, nemico.vy = nemico.posizioneOriginale
                            # controllo se nella casella originale c'è un altro nemico
                            nemicoAppenaSpostato = nemico
                            nemiciSovrappostiRisolti = False
                            while not nemiciSovrappostiRisolti:
                                nemiciSovrappostiRisolti = True
                                for nemicoDaControllare in listaNemici:
                                    if nemicoAppenaSpostato.id != nemicoDaControllare.id and nemicoAppenaSpostato.x == nemicoDaControllare.x and nemicoAppenaSpostato.y == nemicoDaControllare.y:
                                        nemiciSovrappostiRisolti = False
                                        nemicoDaControllare.x, nemicoDaControllare.y = nemicoDaControllare.posizioneOriginale
                                        nemicoDaControllare.vx, nemicoDaControllare.vy = nemicoDaControllare.posizioneOriginale
                                        nemicoAppenaSpostato = nemicoDaControllare
                                        break
                            break
                    # elimino i personaggi se sono nella nostra stessa casella
                    for personaggio in listaPersonaggi:
                        if personaggio.x == x and personaggio.y == y:
                            listaPersonaggi.remove(personaggio)
                            if personaggio in listaPersonaggiTotali:
                                listaPersonaggiTotali.remove(personaggio)

                    if not inizio:
                        mosseRimasteRob = 0
                    nemicoInquadrato = False

                    # elimino tutte le esche
                    if not inizio:
                        vettoreEsche = []

                    stanzaCambiata = True

                    if dati[1] in GlobalGameVar.vetStanzePacifiche:
                        vettoreDenaroTotale = []
                        vettoreDenaroStanza = []
                        dati[2] = x
                        dati[3] = y
                        dati[140] = npers
                        dati[134] = rx
                        dati[135] = ry
                        # 1->d , 2->a , 3->s , 4->w
                        if robot == GlobalImgVar.robod:
                            dati[141] = 1
                        elif robot == GlobalImgVar.roboa:
                            dati[141] = 2
                        elif robot == GlobalImgVar.robos:
                            dati[141] = 3
                        elif robot == GlobalImgVar.robow:
                            dati[141] = 4
                        dati[142] = chiamarob
                        dati[139] = mosseRimasteRob
                        dati[136] = raffredda
                        dati[137] = autoRic1
                        dati[138] = autoRic2
                        dati[143] = GlobalGameVar.pazzoStrabico
                        dati[144] = GlobalGameVar.cambiataAlCastello[0]
                        GlobalGameVar.vetDatiSalvataggioGameOver = [dati[:], tutteporte[:], tutticofanetti[:], GenericFunc.copiaListaDiOggettiConImmagini(listaNemiciTotali, True), vettoreEsche[:], vettoreDenaroTotale[:], stanzeGiaVisitate[:], GenericFunc.copiaListaDiOggettiConImmagini(listaPersonaggiTotali, False, dati[0]), listaAvanzamentoDialoghi[:], oggettiRimastiAHans[:], ultimoObbiettivoColco[:], GenericFunc.copiaNemico(obbiettivoCasualeColco)]
                        GlobalGameVar.idDialoghiLettiGameOver = GlobalGameVar.idDialoghiLetti[:]

                if cambiatoRisoluzione:
                    vx = x
                    vy = y
                    vrx = rx
                    vry = ry
                    if obbiettivoCasualeColco:
                        obbiettivoCasualeColco.caricaImg()
                        obbiettivoCasualeColco.girati(obbiettivoCasualeColco.direzione)
                    for nemico in listaNemiciTotali:
                        nemico.caricaImg()
                        nemico.girati(nemico.direzione)
                    for personaggio in listaPersonaggiTotali:
                        if personaggio.tipo.startswith("Oggetto"):
                            personaggio.caricaImgOggetto()
                            personaggio.aggiornaImgOggetto(dati[0])
                        else:
                            if personaggio.tipo in GlobalImgVar.vettoreNomiNemici and personaggio.tipo != "ServoLancia" and personaggio.tipo != "ServoSpada" and personaggio.tipo != "ServoArco":
                                personaggio.caricaImgNemico()
                            else:
                                personaggio.caricaImgPersonaggio()
                            personaggio.girati(personaggio.direzione)
                    if GlobalGameVar.vetDatiSalvataggioGameOver[11]:
                        GlobalGameVar.vetDatiSalvataggioGameOver[11].caricaImg()
                        GlobalGameVar.vetDatiSalvataggioGameOver[11].girati(GlobalGameVar.vetDatiSalvataggioGameOver[11].direzione)
                    for nemico in GlobalGameVar.vetDatiSalvataggioGameOver[3]:
                        nemico.caricaImg()
                        nemico.girati(nemico.direzione)
                    for personaggio in GlobalGameVar.vetDatiSalvataggioGameOver[7]:
                        if personaggio.tipo.startswith("Oggetto"):
                            personaggio.caricaImgOggetto()
                            personaggio.aggiornaImgOggetto(dati[0])
                        else:
                            if personaggio.tipo in GlobalImgVar.vettoreNomiNemici and personaggio.tipo != "ServoLancia" and personaggio.tipo != "ServoSpada" and personaggio.tipo != "ServoArco":
                                personaggio.caricaImgNemico()
                            else:
                                personaggio.caricaImgPersonaggio()
                            personaggio.girati(personaggio.direzione)

                # stanza
                nomeStanza = SetZoneStanzeImpedimenti.settaNomeImgStanza(dati[0], dati[1], listaAvanzamentoDialoghi)
                imgSfondoStanza = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/" + nomeStanza + ".png", GlobalHWVar.gsx, GlobalHWVar.gsy, False, canale_alpha=False)
                if os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaVerticale.png") and os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaOrizzontale.png"):
                    portaVert = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaVerticale.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                    portaOriz = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/PortaOrizzontale.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                else:
                    portaVert = False
                    portaOriz = False
                if os.path.exists(GlobalHWVar.gamePath + "Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/CadavereSotterrato.png"):
                    imgNemicoSotterrato = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(dati[1]) + "/CadavereSotterrato.png", GlobalHWVar.gpx, GlobalHWVar.gpy, True)
                else:
                    imgNemicoSotterrato = casellaVuotaPreset

                # fermare la camminata dopo il cambio stanza
                bottoneDown = False

                caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili, casellePercorribiliPorteEscluse = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                entrateStanza = SetOstacoliContenutoCofanetti.getEntrateStanze(dati[1], dati[0])

                vettoreImgCaselle = []
                i = 0
                while i < len(caseviste):
                    vettoreImgCaselle.append(caseviste[i])
                    vettoreImgCaselle.append(caseviste[i + 1])
                    vettoreImgCaselle.append(imgSfondoStanza.subsurface(pygame.Rect(caseviste[i], caseviste[i + 1], GlobalHWVar.gpx, GlobalHWVar.gpy)).convert())
                    i += 3

                impossibileCliccarePulsanti = True

            GlobalGameVar.armaturaIndossata = dati[8]
            if aggiornaImgEquip or cambiatoRisoluzione:
                # arma
                armaw = GlobalImgVar.vetImgSpadeInGame[dati[6]][0]
                armawMov1 = GlobalImgVar.vetImgSpadeInGame[dati[6]][1]
                armawMov2 = GlobalImgVar.vetImgSpadeInGame[dati[6]][2]
                armaa = GlobalImgVar.vetImgSpadeInGame[dati[6]][3]
                armaaMov1 = GlobalImgVar.vetImgSpadeInGame[dati[6]][4]
                armaaMov2 = GlobalImgVar.vetImgSpadeInGame[dati[6]][5]
                armas = GlobalImgVar.vetImgSpadeInGame[dati[6]][6]
                armasMov1 = GlobalImgVar.vetImgSpadeInGame[dati[6]][7]
                armasMov2 = GlobalImgVar.vetImgSpadeInGame[dati[6]][8]
                armad = GlobalImgVar.vetImgSpadeInGame[dati[6]][9]
                armadMov1 = GlobalImgVar.vetImgSpadeInGame[dati[6]][10]
                armadMov2 = GlobalImgVar.vetImgSpadeInGame[dati[6]][11]
                armasAttacco = GlobalImgVar.vetImgSpadeInGame[dati[6]][12]
                armaaAttacco = GlobalImgVar.vetImgSpadeInGame[dati[6]][13]
                armadAttacco = GlobalImgVar.vetImgSpadeInGame[dati[6]][14]
                armawAttacco = GlobalImgVar.vetImgSpadeInGame[dati[6]][15]
                # arco
                arcow = GlobalImgVar.vetImgArchiInGame[dati[128]][0]
                arcoa = GlobalImgVar.vetImgArchiInGame[dati[128]][1]
                arcos = GlobalImgVar.vetImgArchiInGame[dati[128]][2]
                arcod = GlobalImgVar.vetImgArchiInGame[dati[128]][3]
                arcosAttacco = GlobalImgVar.vetImgArchiInGame[dati[128]][4]
                arcoaAttacco = GlobalImgVar.vetImgArchiInGame[dati[128]][5]
                arcodAttacco = GlobalImgVar.vetImgArchiInGame[dati[128]][6]
                arcowAttacco = GlobalImgVar.vetImgArchiInGame[dati[128]][7]
                # faretra
                faretraw = GlobalImgVar.vetImgFaretreInGame[dati[133]][0]
                faretraa = GlobalImgVar.vetImgFaretreInGame[dati[133]][1]
                faretras = GlobalImgVar.vetImgFaretreInGame[dati[133]][2]
                faretrad = GlobalImgVar.vetImgFaretreInGame[dati[133]][3]
                # armatura
                if dati[0] > GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"] and dati[8] == 0:
                    armaturaw = casellaVuotaPreset
                    armaturaa = casellaVuotaPreset
                    armaturas = casellaVuotaPreset
                    armaturad = casellaVuotaPreset
                else:
                    armaturaw = GlobalImgVar.vetImgArmatureInGame[dati[8]][0]
                    armaturaa = GlobalImgVar.vetImgArmatureInGame[dati[8]][1]
                    armaturas = GlobalImgVar.vetImgArmatureInGame[dati[8]][2]
                    armaturad = GlobalImgVar.vetImgArmatureInGame[dati[8]][3]
                # scudo
                scudow = GlobalImgVar.vetImgScudiInGame[dati[7]][0]
                scudoa = GlobalImgVar.vetImgScudiInGame[dati[7]][1]
                scudos = GlobalImgVar.vetImgScudiInGame[dati[7]][2]
                scudod = GlobalImgVar.vetImgScudiInGame[dati[7]][3]
                scudoDifesa = GlobalImgVar.vetImgScudiInGame[dati[7]][4]
                # guanti
                guantiw = GlobalImgVar.vetImgGuantiInGame[dati[129]][0]
                guantiwMov1 = GlobalImgVar.vetImgGuantiInGame[dati[129]][1]
                guantiwMov2 = GlobalImgVar.vetImgGuantiInGame[dati[129]][2]
                guantia = GlobalImgVar.vetImgGuantiInGame[dati[129]][3]
                guantiaMov1 = GlobalImgVar.vetImgGuantiInGame[dati[129]][4]
                guantiaMov2 = GlobalImgVar.vetImgGuantiInGame[dati[129]][5]
                guantis = GlobalImgVar.vetImgGuantiInGame[dati[129]][6]
                guantisMov1 = GlobalImgVar.vetImgGuantiInGame[dati[129]][7]
                guantisMov2 = GlobalImgVar.vetImgGuantiInGame[dati[129]][8]
                guantid = GlobalImgVar.vetImgGuantiInGame[dati[129]][9]
                guantidMov1 = GlobalImgVar.vetImgGuantiInGame[dati[129]][10]
                guantidMov2 = GlobalImgVar.vetImgGuantiInGame[dati[129]][11]
                guantisAttacco = GlobalImgVar.vetImgGuantiInGame[dati[129]][12]
                guantiaAttacco = GlobalImgVar.vetImgGuantiInGame[dati[129]][13]
                guantidAttacco = GlobalImgVar.vetImgGuantiInGame[dati[129]][14]
                guantiwAttacco = GlobalImgVar.vetImgGuantiInGame[dati[129]][15]
                guantiDifesa = GlobalImgVar.vetImgGuantiInGame[dati[129]][16]
                # collana
                collanaw = GlobalImgVar.vetImgCollaneInGame[dati[130]][0]
                collanaa = GlobalImgVar.vetImgCollaneInGame[dati[130]][1]
                collanas = GlobalImgVar.vetImgCollaneInGame[dati[130]][2]
                collanad = GlobalImgVar.vetImgCollaneInGame[dati[130]][3]
                # armatura robot
                armrobw = GlobalImgVar.vetImgArmRobInGame[dati[9]][0]
                armroba = GlobalImgVar.vetImgArmRobInGame[dati[9]][1]
                armrobs = GlobalImgVar.vetImgArmRobInGame[dati[9]][2]
                armrobd = GlobalImgVar.vetImgArmRobInGame[dati[9]][3]

            if npers == 3:
                pers = GlobalImgVar.persw
                arma = armaw
                armaMov1 = armawMov1
                armaMov2 = armawMov2
                armaAttacco = armawAttacco
                armatura = armaturaw
                scudo = scudow
                arco = arcow
                faretra = faretraw
                arcoAttacco = arcowAttacco
                guanti = guantiw
                guantiMov1 = guantiwMov1
                guantiMov2 = guantiwMov2
                guantiAttacco = guantiwAttacco
                collana = collanaw
            if npers == 2:
                pers = GlobalImgVar.persa
                arma = armaa
                armaMov1 = armaaMov1
                armaMov2 = armaaMov2
                armaAttacco = armaaAttacco
                armatura = armaturaa
                scudo = scudoa
                arco = arcoa
                faretra = faretraa
                arcoAttacco = arcoaAttacco
                guanti = guantia
                guantiMov1 = guantiaMov1
                guantiMov2 = guantiaMov2
                guantiAttacco = guantiaAttacco
                collana = collanaa
            if npers == 4:
                pers = GlobalImgVar.perss
                arma = armas
                armaMov1 = armasMov1
                armaMov2 = armasMov2
                armaAttacco = armasAttacco
                armatura = armaturas
                scudo = scudos
                arco = arcos
                faretra = faretras
                arcoAttacco = arcosAttacco
                guanti = guantis
                guantiMov1 = guantisMov1
                guantiMov2 = guantisMov2
                guantiAttacco = guantisAttacco
                collana = collanas
            if npers == 1:
                pers = GlobalImgVar.persd
                arma = armad
                armaMov1 = armadMov1
                armaMov2 = armadMov2
                armaAttacco = armadAttacco
                armatura = armaturad
                scudo = scudod
                arco = arcod
                faretra = faretrad
                arcoAttacco = arcodAttacco
                guanti = guantid
                guantiMov1 = guantidMov1
                guantiMov2 = guantidMov2
                guantiAttacco = guantidAttacco
                collana = collanad
            if nrob != 0:
                if nrob == 1:
                    robot = GlobalImgVar.robod
                    armrob = armrobd
                if nrob == 2:
                    robot = GlobalImgVar.roboa
                    armrob = armroba
                if nrob == 3:
                    robot = GlobalImgVar.robos
                    armrob = armrobs
                if nrob == 4:
                    robot = GlobalImgVar.robow
                    armrob = armrobw

            # aggiorno inCasellaVista di nemici e personaggi
            listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caselleNonVisibili, listaNemici, listaPersonaggi)
            # aggiorno il campo attaccabile di colco
            if GlobalGameVar.impoPresente and rx == GlobalHWVar.gsx and ry == GlobalHWVar.gsy:
                rx = x
                ry = y
                vrx = rx
                vry = ry
            if GlobalGameVar.impoPresente:
                caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            # faccio il primo aggiornamento delle caselle attaccabili dei nemici (lo faccio perché queste caselle non vengono aggiornate finché il nemico non si sposta almeno una volta)
            for nemico in listaNemici:
                if inizio:
                    nemico.settaObbiettivoDalSalvataggio(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, listaNemici, listaPersonaggi, dati, caseviste)
                if nemico.vita > 0 and nemico.inCasellaVista:
                    nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=True)

            # aggiorno dialoghi/img dei personaggi
            for personaggio in listaPersonaggi:
                personaggio.aggiornaDialogo(dati[0], dati[131])
                if personaggio.tipo.startswith("Oggetto"):
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            # aggiorna img mappa, protagonista
            SetImgOggettiMappaPersonaggi.settaImgMappa(dati[0])
            SetImgOggettiMappaPersonaggi.setImgMenuStartProtagonista(dati[0])
            SetImgOggettiMappaPersonaggi.setImgMenuOggettiProtagonista(dati[0])
            SetImgOggettiMappaPersonaggi.setImgDialogoProtagonista(dati[0])

            caricaTutto = True
            cambiosta = False
            carim = False
            aggiornaImgEquip = False
            cambiatoRisoluzione = False

        if inizio:
            if npers != 1 and npers != 2 and npers != 3 and npers != 4:
                arma = armas
                armaMov1 = armasMov1
                armaMov2 = armasMov2
                armaAttacco = armasAttacco
                armatura = armaturas
                scudo = scudos
                arco = arcos
                faretra = faretras
                arcoAttacco = arcosAttacco
                guanti = guantis
                guantiMov1 = guantisMov1
                guantiMov2 = guantisMov2
                guantiAttacco = guantisAttacco
                collana = collanas
            if nrob == 0:
                robot = GlobalImgVar.robos
                armrob = armrobs
            inizio = False

        inquadratoQualcosa = False
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            # controlle se il cursore è sul pers in basso a sinistra / nemico in alto a sinistra / telecolco / salta turno / personaggio / porta / cofanetto / casella vista
            if GlobalHWVar.gsy // 18 * 17 <= yMouse <= GlobalHWVar.gsy and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 8:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "start"
            elif ((type(nemicoInquadrato) is str and nemicoInquadrato == "Colco") or (not nemicoInquadrato and GlobalGameVar.impoPresente)) and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 6:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 3:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif nemicoInquadrato and not type(nemicoInquadrato) is str and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif not nemicoInquadrato and not GlobalGameVar.impoPresente and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 0 <= xMouse <= GlobalHWVar.gsx // 32 * 1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "battaglia"
            elif GlobalGameVar.impoPresente and GlobalGameVar.impoPietraPosseduta and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 28.6 <= xMouse <= GlobalHWVar.gsx // 32 * 29.8:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "telecolco"
            elif 0 <= yMouse <= GlobalHWVar.gsy // 18 * 1 and GlobalHWVar.gsx // 32 * 30.8 <= xMouse <= GlobalHWVar.gsx:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                inquadratoQualcosa = "saltaTurno"
            else:
                if not inquadratoQualcosa:
                    i = 0
                    for personaggio in listaPersonaggi:
                        if personaggio.x <= xMouse <= personaggio.x + GlobalHWVar.gpx and personaggio.y <= yMouse <= personaggio.y + GlobalHWVar.gpy:
                            if (personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy):
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "personaggio:" + str(i)
                            break
                        i += 1
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(porte):
                        if porte[i + 1] <= xMouse <= porte[i + 1] + GlobalHWVar.gpx and porte[i + 2] <= yMouse <= porte[i + 2] + GlobalHWVar.gpy and not porte[i + 3]:
                            if ((porte[i + 1] == x + GlobalHWVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x - GlobalHWVar.gpx and porte[i + 2] == y) or (porte[i + 1] == x and porte[i + 2] == y + GlobalHWVar.gpy) or (porte[i + 1] == x and porte[i + 2] == y - GlobalHWVar.gpy)) and not porte[i + 3]:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "porta:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i + 1] <= xMouse <= cofanetti[i + 1] + GlobalHWVar.gpx and cofanetti[i + 2] <= yMouse <= cofanetti[i + 2] + GlobalHWVar.gpy and not cofanetti[i + 3]:
                            if ((cofanetti[i + 1] == x + GlobalHWVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x - GlobalHWVar.gpx and cofanetti[i + 2] == y) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalHWVar.gpy) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalHWVar.gpy)) and not cofanetti[i + 3]:
                                if GlobalHWVar.mouseBloccato:
                                    GlobalHWVar.configuraCursore(False)
                                inquadratoQualcosa = "cofanetto:" + str(i)
                            break
                        i += 4
                if not inquadratoQualcosa:
                    i = 0
                    while i < len(casevisteEntrateIncluse):
                        if xMouse < GlobalHWVar.gpx or xMouse > GlobalHWVar.gpx * 31 or yMouse < GlobalHWVar.gpy or yMouse > GlobalHWVar.gpy * 17:
                            if casevisteEntrateIncluse[i + 2] and (casevisteEntrateIncluse[i] == GlobalHWVar.gpx or casevisteEntrateIncluse[i] == GlobalHWVar.gpx * 30 or casevisteEntrateIncluse[i + 1] == GlobalHWVar.gpy or casevisteEntrateIncluse[i + 1] == GlobalHWVar.gpy * 16):
                                if (casevisteEntrateIncluse[i] <= xMouse + GlobalHWVar.gpx <= casevisteEntrateIncluse[i] + GlobalHWVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse <= casevisteEntrateIncluse[i + 1] + GlobalHWVar.gpy) or (casevisteEntrateIncluse[i] <= xMouse - GlobalHWVar.gpx <= casevisteEntrateIncluse[i] + GlobalHWVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse <= casevisteEntrateIncluse[i + 1] + GlobalHWVar.gpy) or (casevisteEntrateIncluse[i] <= xMouse <= casevisteEntrateIncluse[i] + GlobalHWVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse + GlobalHWVar.gpy <= casevisteEntrateIncluse[i + 1] + GlobalHWVar.gpy) or (casevisteEntrateIncluse[i] <= xMouse <= casevisteEntrateIncluse[i] + GlobalHWVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse - GlobalHWVar.gpy <= casevisteEntrateIncluse[i + 1] + GlobalHWVar.gpy):
                                    if GlobalHWVar.mouseBloccato:
                                        GlobalHWVar.configuraCursore(False)
                                    inquadratoQualcosa = "movimento:" + str(casevisteEntrateIncluse[i]) + ":" + str(casevisteEntrateIncluse[i + 1])
                                    break
                        elif casevisteEntrateIncluse[i] <= xMouse <= casevisteEntrateIncluse[i] + GlobalHWVar.gpx and casevisteEntrateIncluse[i + 1] <= yMouse <= casevisteEntrateIncluse[i + 1] + GlobalHWVar.gpy:
                            if casevisteEntrateIncluse[i + 2]:
                                casellaOccupata = False
                                for personaggio in listaPersonaggi:
                                    if casevisteEntrateIncluse[i] == personaggio.x and casevisteEntrateIncluse[i + 1] == personaggio.y:
                                        casellaOccupata = True
                                        break
                                for nemico in listaNemici:
                                    if casevisteEntrateIncluse[i] == nemico.x and casevisteEntrateIncluse[i + 1] == nemico.y:
                                        casellaOccupata = True
                                        break
                                if not casellaOccupata:
                                    if GlobalHWVar.mouseBloccato:
                                        GlobalHWVar.configuraCursore(False)
                                    inquadratoQualcosa = "movimento:" + str(casevisteEntrateIncluse[i]) + ":" + str(casevisteEntrateIncluse[i + 1])
                            break
                        i += 3
        if not inquadratoQualcosa and GlobalHWVar.mouseVisibile:
            if not GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(True)

        # controllo se ci sono nemici in movimento per decidere se fare altre animazioni o no
        nemiciInMovimento = False
        for nemico in listaNemici:
            if nemico.mosseRimaste > 0:
                nemiciInMovimento = True
                break

        if saltaTurno and mosseRimasteRob <= 0 and not nemiciInMovimento:
            saltaTurno = False
            refreshSchermo = True

        # gestione degli input
        if not impossibileCliccarePulsanti and not avanzaIlTurnoSenzaMuoverti and mosseRimasteRob <= 0 and not nemiciInMovimento and not startf and not oggettoRicevuto and len(percorsoDaEseguire) == 0 and not uscitoDaMenu > 0 and not evitaAvanzamentoTurno:
            bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
        elif startf or oggettoRicevuto or impossibileCliccarePulsanti or avanzaIlTurnoSenzaMuoverti or uscitoDaMenu > 0 or evitaAvanzamentoTurno:
            bottoneDown = False
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        elif len(percorsoDaEseguire) > 0 and mosseRimasteRob <= 0 and not nemiciInMovimento:
            bottoneDown, inutile = GestioneInput.getInput(bottoneDown, False)
            if avanzaManualmentePercorsoDaEseguire:
                if (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato and (inquadratoQualcosa.startswith("movimento") or inquadratoQualcosa.startswith("personaggio") or inquadratoQualcosa.startswith("porta") or inquadratoQualcosa.startswith("cofanetto") or inquadratoQualcosa == "saltaTurno")) or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padSu" or bottoneDown == "padSinistra" or bottoneDown == "padGiu" or bottoneDown == "padDestra" or bottoneDown == pygame.K_0 or bottoneDown == pygame.K_KP0 or bottoneDown == "padSelect" or bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce":
                    movimentoDaCompiere = percorsoDaEseguire.pop(0)
                elif bottoneDown:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            else:
                movimentoDaCompiere = percorsoDaEseguire.pop(0)
            bottoneDown = False
            if len(percorsoDaEseguire) <= 0:
                avanzaManualmentePercorsoDaEseguire = False
        if (not bottoneDown and not movimentoDaCompiere) or GlobalHWVar.aggiornaInterfacciaPerCambioInputMainFunc:
            bottoneDown = False
            GlobalHWVar.aggiornaInterfacciaPerCambioInputMainFunc = False
            GlobalHWVar.canaleSoundPassiRallo.stop()
            nx = 0
            ny = 0
        movimentoPerMouse = False
        if mosseRimasteRob <= 0 and not nemiciInMovimento:
            # salta il turno
            if bottoneDown == pygame.K_0 or bottoneDown == pygame.K_KP0 or bottoneDown == "padSelect" or movimentoDaCompiere == "saltaTurno":
                if not movimentoDaCompiere == "saltaTurno":
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostaPunBattaglia)
                sposta = True
                saltaTurno = True

            # movimenti personaggio
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu" or movimentoDaCompiere == "w":
                refreshSchermo = True
                npers = 3
                pers = GlobalImgVar.persw
                arma = armaw
                armaMov1 = armawMov1
                armaMov2 = armawMov2
                armaAttacco = armawAttacco
                armatura = armaturaw
                scudo = scudow
                arco = arcow
                faretra = faretraw
                arcoAttacco = arcowAttacco
                guanti = guantiw
                guantiMov1 = guantiwMov1
                guantiMov2 = guantiwMov2
                guantiAttacco = guantiwAttacco
                collana = collanaw
                ny = -GlobalHWVar.gpy
                nx = 0
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["A"] or bottoneDown == "padSinistra" or movimentoDaCompiere == "a":
                refreshSchermo = True
                npers = 2
                pers = GlobalImgVar.persa
                arma = armaa
                armaMov1 = armaaMov1
                armaMov2 = armaaMov2
                armaAttacco = armaaAttacco
                armatura = armaturaa
                scudo = scudoa
                arco = arcoa
                faretra = faretraa
                arcoAttacco = arcoaAttacco
                guanti = guantia
                guantiMov1 = guantiaMov1
                guantiMov2 = guantiaMov2
                guantiAttacco = guantiaAttacco
                collana = collanaa
                nx = -GlobalHWVar.gpx
                ny = 0
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu" or movimentoDaCompiere == "s":
                refreshSchermo = True
                npers = 4
                pers = GlobalImgVar.perss
                arma = armas
                armaMov1 = armasMov1
                armaMov2 = armasMov2
                armaAttacco = armasAttacco
                armatura = armaturas
                scudo = scudos
                arco = arcos
                faretra = faretras
                arcoAttacco = arcosAttacco
                guanti = guantis
                guantiMov1 = guantisMov1
                guantiMov2 = guantisMov2
                guantiAttacco = guantisAttacco
                collana = collanas
                ny = GlobalHWVar.gpy
                nx = 0
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["D"] or bottoneDown == "padDestra" or movimentoDaCompiere == "d":
                refreshSchermo = True
                npers = 1
                pers = GlobalImgVar.persd
                arma = armad
                armaMov1 = armadMov1
                armaMov2 = armadMov2
                armaAttacco = armadAttacco
                armatura = armaturad
                scudo = scudod
                arco = arcod
                faretra = faretrad
                arcoAttacco = arcodAttacco
                guanti = guantid
                guantiMov1 = guantidMov1
                guantiMov2 = guantidMov2
                guantiAttacco = guantidAttacco
                collana = collanad
                nx = GlobalHWVar.gpx
                ny = 0
            # vado in mod. interazione
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["E"] or bottoneDown == "padQuadrato":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                attacco = 1
                bottoneDown = False
            # tolgo l'obiettivo se presente
            if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "padCerchio":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                if nemicoInquadrato:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    nemicoInquadrato = False
                    caricaTutto = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            # attivo / disattivo gambit di Colco
            if bottoneDown == pygame.K_LSHIFT or bottoneDown == pygame.K_RSHIFT or bottoneDown == "padTriangolo":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                if GlobalGameVar.impoPresente and GlobalGameVar.impoPietraPosseduta:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                    refreshSchermo = True
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        ultimoObbiettivoColco.append("spostamento")
                        chiamarob = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            # scorro la selezione dell'obiettivo
            if bottoneDown == pygame.K_3 or bottoneDown == pygame.K_KP3 or bottoneDown == "padR1":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                listaNemiciVisti = []
                for nemico in listaNemici:
                    if nemico.inCasellaVista:
                        listaNemiciVisti.append(nemico)
                listaEscheViste = []
                i = 0
                while i < len(vettoreEsche):
                    j = 0
                    while j < len(caseviste):
                        if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                            listaEscheViste.append(vettoreEsche[i])
                            listaEscheViste.append(vettoreEsche[i + 1])
                            listaEscheViste.append(vettoreEsche[i + 2])
                            listaEscheViste.append(vettoreEsche[i + 3])
                        j += 3
                    i += 4
                trovatoNemicoDaInquadrare, nemicoInquadrato = GenericFunc.scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, True)
                if trovatoNemicoDaInquadrare:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                caricaTutto = True
                bottoneDown = False
            if bottoneDown == pygame.K_2 or bottoneDown == pygame.K_KP2 or bottoneDown == "padL1":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                listaNemiciVisti = []
                for nemico in listaNemici:
                    if nemico.inCasellaVista:
                        listaNemiciVisti.append(nemico)
                listaEscheViste = []
                i = 0
                while i < len(vettoreEsche):
                    j = 0
                    while j < len(caseviste):
                        if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and caseviste[j + 2]:
                            listaEscheViste.append(vettoreEsche[i])
                            listaEscheViste.append(vettoreEsche[i + 1])
                            listaEscheViste.append(vettoreEsche[i + 2])
                            listaEscheViste.append(vettoreEsche[i + 3])
                        j += 3
                    i += 4
                trovatoNemicoDaInquadrare, nemicoInquadrato = GenericFunc.scorriObbiettiviInquadrati(dati[0], nemicoInquadrato, listaNemiciVisti, listaEscheViste, False)
                if trovatoNemicoDaInquadrare:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selObbiettivo)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                caricaTutto = True
                bottoneDown = False
            # interagisco
            if bottoneDown == pygame.K_SPACE or bottoneDown == "padCroce":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                interazioneEseguita = False
                nx = 0
                ny = 0
                # apertura porte
                k = 0
                while k < len(porte):
                    if porte[k] == dati[1] and not porte[k + 3] and ((porte[k + 1] == x + GlobalHWVar.gpx and porte[k + 2] == y and npers == 1) or (porte[k + 1] == x - GlobalHWVar.gpx and porte[k + 2] == y and npers == 2) or (porte[k + 1] == x and porte[k + 2] == y + GlobalHWVar.gpy and npers == 4) or (porte[k + 1] == x and porte[k + 2] == y - GlobalHWVar.gpy and npers == 3)):
                        if SetZoneStanzeImpedimenti.possibileAprirePorta(dati[1], porte[k + 1], porte[k + 2], dati[0]):
                            posizioneRalloAggiornamentoCaseAttac = [0, 0]
                            sposta = True
                            GlobalHWVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                            porte[k + 3] = True
                            caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili, casellePercorribiliPorteEscluse = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                            caricaTutto = True
                            # aggiornare vettore tutteporte
                            j = 0
                            while j < len(tutteporte):
                                if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                    tutteporte[j + 3] = True
                                    break
                                j = j + 4
                            # aggiorno inCasellaVista di nemici e personaggi
                            listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caselleNonVisibili, listaNemici, listaPersonaggi)
                            # aggiorno il campo attaccabile di colco
                            if GlobalGameVar.impoPresente:
                                caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                                posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                            # aggiorno la vista dei nemici
                            for nemico in listaNemici:
                                if nemico.vita > 0 and nemico.inCasellaVista:
                                    nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=True)
                        else:
                            caricaTutto = True
                            impossibileAprirePorta = True
                        interazioneEseguita = True
                        break
                    k = k + 4
                # apertura cofanetti
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and ((cofanetti[i + 1] == x + GlobalHWVar.gpx and cofanetti[i + 2] == y and npers == 1) or (cofanetti[i + 1] == x - GlobalHWVar.gpx and cofanetti[i + 2] == y and npers == 2) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + GlobalHWVar.gpy and npers == 4) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - GlobalHWVar.gpy and npers == 3)) and not cofanetti[i + 3]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturacofanetti)
                        sposta = True
                        dati, tesoro, dati[0] = SetOstacoliContenutoCofanetti.aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                        if tesoro == -2 or tesoro == -1 or tesoro > 0:
                            cofanetti[i + 3] = True
                        caricaTutto = True
                        # aggiornare vettore tutticofanetti
                        j = 0
                        while j < len(tutticofanetti):
                            if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                                if tesoro == -2 or tesoro == -1 or tesoro > 0:
                                    tutticofanetti[j + 3] = True
                            j = j + 4
                    i = i + 4
                # interazioni con altri personaggi
                for personaggio in listaPersonaggi:
                    if (personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy and npers == 3):
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        if dati[0] < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                            if npers == 1:
                                personaggio.girati("a", perDialogo=True)
                            elif npers == 2:
                                personaggio.girati("d", perDialogo=True)
                            elif npers == 3:
                                personaggio.girati("s", perDialogo=True)
                            elif npers == 4:
                                personaggio.girati("w", perDialogo=True)
                        EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)
                        if personaggio.oggettoEnigma:
                            dati[0] = MenuEnigmi.mostraEnigma(personaggio.tipo, dati[0])
                        else:
                            dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi, canzone)
                        sposta = False
                        interazioneEseguita = True
                        caricaTutto = True
                if not sposta and not interazioneEseguita:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
            # apro il menu
            if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                startf = True
                bottoneDown = False
            # comandi mouse
            if bottoneDown == "mouseDestro":
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                if inquadratoQualcosa == "battaglia" and nemicoInquadrato:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    nemicoInquadrato = False
                    caricaTutto = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                    attacco = 1
                bottoneDown = False
            if bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato:
                if inquadratoQualcosa == "saltaTurno":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostaPunBattaglia)
                    sposta = True
                    saltaTurno = True
                elif inquadratoQualcosa == "start":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    startf = True
                    bottoneDown = False
                elif inquadratoQualcosa == "battaglia":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostaPunBattaglia)
                    attacco = 1
                    bottoneDown = False
                elif inquadratoQualcosa == "telecolco":
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                    refreshSchermo = True
                    if chiamarob:
                        chiamarob = False
                    else:
                        ultimoObbiettivoColco = []
                        ultimoObbiettivoColco.append("Telecomando")
                        ultimoObbiettivoColco.append(x)
                        ultimoObbiettivoColco.append(y)
                        ultimoObbiettivoColco.append("spostamento")
                        chiamarob = True
                    bottoneDown = False
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("porta"):
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizPortaInVettore = int(inquadratoQualcosaList[1])
                    if SetZoneStanzeImpedimenti.possibileAprirePorta(dati[1], porte[posizPortaInVettore + 1], porte[posizPortaInVettore + 2], dati[0]):
                        posizioneRalloAggiornamentoCaseAttac = [0, 0]
                        sposta = True
                        GlobalHWVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                        porte[posizPortaInVettore + 3] = True
                        caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili, casellePercorribiliPorteEscluse = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                        caricaTutto = True
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[posizPortaInVettore] and tutteporte[j + 1] == porte[posizPortaInVettore + 1] and tutteporte[j + 2] == porte[posizPortaInVettore + 2]:
                                tutteporte[j + 3] = True
                                break
                            j += 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caselleNonVisibili, listaNemici, listaPersonaggi)
                        # aggiorno il campo attaccabile di colco
                        if GlobalGameVar.impoPresente:
                            caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                        # aggiorno la vista dei nemici
                        for nemico in listaNemici:
                            if nemico.vita > 0 and nemico.inCasellaVista:
                                nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=True)
                    else:
                        impossibileAprirePorta = True
                        caricaTutto = True
                    # giro il pers verso la porta
                    if porte[posizPortaInVettore + 1] == x + GlobalHWVar.gpx and porte[posizPortaInVettore + 2] == y:
                        npers = 1
                    if porte[posizPortaInVettore + 1] == x - GlobalHWVar.gpx and porte[posizPortaInVettore + 2] == y:
                        npers = 2
                    if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y + GlobalHWVar.gpy:
                        npers = 4
                    if porte[posizPortaInVettore + 1] == x and porte[posizPortaInVettore + 2] == y - GlobalHWVar.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("cofanetto"):
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizCofanettoInVettore = int(inquadratoQualcosaList[1])
                    sposta = True
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturacofanetti)
                    dati, tesoro, dati[0] = SetOstacoliContenutoCofanetti.aperturacofanetto(cofanetti[posizCofanettoInVettore], cofanetti[posizCofanettoInVettore + 1], cofanetti[posizCofanettoInVettore + 2], dati)
                    if tesoro == -2 or tesoro == -1 or tesoro > 0:
                        cofanetti[posizCofanettoInVettore + 3] = True
                    caricaTutto = True
                    # aggiornare vettore tutticofanetti
                    j = 0
                    while j < len(tutticofanetti):
                        if tutticofanetti[j] == cofanetti[posizCofanettoInVettore] and tutticofanetti[j + 1] == cofanetti[posizCofanettoInVettore + 1] and tutticofanetti[j + 2] == cofanetti[posizCofanettoInVettore + 2]:
                            if tesoro == -2 or tesoro == -1 or tesoro > 0:
                                tutticofanetti[j + 3] = True
                        j += 4
                    # giro il pers verso il cofanetto
                    if cofanetti[posizCofanettoInVettore + 1] == x + GlobalHWVar.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                        npers = 1
                    if cofanetti[posizCofanettoInVettore + 1] == x - GlobalHWVar.gpx and cofanetti[posizCofanettoInVettore + 2] == y:
                        npers = 2
                    if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y + GlobalHWVar.gpy:
                        npers = 4
                    if cofanetti[posizCofanettoInVettore + 1] == x and cofanetti[posizCofanettoInVettore + 2] == y - GlobalHWVar.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                    bottoneDown = False
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("personaggio"):
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                    nx = 0
                    ny = 0
                    inquadratoQualcosaList = inquadratoQualcosa.split(":")
                    posizPersonaggioInVettore = int(inquadratoQualcosaList[1])
                    personaggio = listaPersonaggi[posizPersonaggioInVettore]
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    # giro Rallo verso il personaggio e viceversa
                    if personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y:
                        npers = 1
                    if personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y:
                        npers = 2
                    if personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy:
                        npers = 4
                    if personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy:
                        npers = 3
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                    if dati[0] < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                        if npers == 1:
                            personaggio.girati("a", perDialogo=True)
                        elif npers == 2:
                            personaggio.girati("d", perDialogo=True)
                        elif npers == 3:
                            personaggio.girati("s", perDialogo=True)
                        elif npers == 4:
                            personaggio.girati("w", perDialogo=True)
                    EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)
                    if personaggio.oggettoEnigma:
                        dati[0] = MenuEnigmi.mostraEnigma(personaggio.tipo, dati[0])
                    else:
                        dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi, canzone)
                    sposta = False
                    caricaTutto = True
                    bottoneDown = False
                elif inquadratoQualcosa and inquadratoQualcosa.startswith("movimento"):
                    movimentoPerMouse = True
            elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
                GlobalHWVar.canaleSoundPassiRallo.stop()
                nx = 0
                ny = 0
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False

        impossibileCliccarePulsanti = False
        if avanzaIlTurnoSenzaMuoverti and not evitaAvanzamentoTurno:
            sposta = True
        avanzaIlTurnoSenzaMuoverti = False
        evitaAvanzamentoTurno = False
        # statistiche personaggio e robo
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)

        # decido quando si deve dimezzare il volume della musica
        SetPosizProtagonistaAudio.decidiSeDimezzareVolumeMusica(dati[0])
        # decido quando togliere il volume dei passi e degli attacchi
        SetPosizProtagonistaAudio.decidiSeRiprodurreSuoniPassiAttacchi(dati[0])
        # decido se riavviare il sottofono ambientale
        SetPosizProtagonistaAudio.decidiSeRiavviareSottofondoAmbientale(dati[0], listaSottofondoAmbientale)

        # resetta stati/pv al cambio personaggio
        if dati[0] == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] or dati[0] == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or dati[0] == GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] or dati[0] == GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"]:
            dati[5] = pvtot
            dati[121] = False

        # ripristina vita e status dopo lv up
        if aumentoliv != 0:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = 0

        # movimento col mouse
        if inquadratoQualcosa and inquadratoQualcosa.startswith("movimento") and movimentoPerMouse and mosseRimasteRob <= 0 and not nemiciInMovimento and not startf and dati[5] > 0:
            nx = 0
            ny = 0
            vetNemiciSoloConXeY = []
            for nemico in listaNemici:
                vetNemiciSoloConXeY.append(nemico.x)
                vetNemiciSoloConXeY.append(nemico.y)
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            inquadratoQualcosaList = inquadratoQualcosa.split(":")
            xObbiettivo = int(inquadratoQualcosaList[1])
            yObbiettivo = int(inquadratoQualcosaList[2])
            bloccato = False
            i = 0
            while i < len(vetNemiciSoloConXeY):
                if xObbiettivo == vetNemiciSoloConXeY[i] and yObbiettivo == vetNemiciSoloConXeY[i + 1]:
                    bloccato = True
                    break
                i += 2
            if not bloccato and not (x == xObbiettivo and y == yObbiettivo):
                if abs(xObbiettivo - x) == GlobalHWVar.gpx and abs(yObbiettivo - y) == 0:
                    if x < xObbiettivo:
                        npers = 1
                    if x > xObbiettivo:
                        npers = 2
                    sposta = True
                elif abs(yObbiettivo - y) == GlobalHWVar.gpy and abs(xObbiettivo - x) == 0:
                    if y < yObbiettivo:
                        npers = 4
                    if y > yObbiettivo:
                        npers = 3
                    sposta = True
                else:
                    percorsoTrovato = GenericFunc.pathFinding(x, y, xObbiettivo, yObbiettivo, vetNemiciSoloConXeY, casevisteEntrateIncluse)
                    if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != x or percorsoTrovato[len(percorsoTrovato) - 3] != y):
                        if percorsoTrovato[len(percorsoTrovato) - 4] > x:
                            npers = 1
                        if percorsoTrovato[len(percorsoTrovato) - 4] < x:
                            npers = 2
                        if percorsoTrovato[len(percorsoTrovato) - 3] > y:
                            npers = 4
                        if percorsoTrovato[len(percorsoTrovato) - 3] < y:
                            npers = 3
                        sposta = True
                    else:
                        # print ("Percorso Rallo verso cursore non trovato")
                        bottoneDown = False
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # cambiare posizione
                if sposta:
                    if npers == 3:
                        ny = -GlobalHWVar.gpy
                        nx = 0
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        ny = 0
                        nx = -GlobalHWVar.gpx
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        ny = GlobalHWVar.gpy
                        nx = 0
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        ny = 0
                        nx = GlobalHWVar.gpx
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
            if nx == 0 and ny == 0:
                GlobalHWVar.canaleSoundPassiRallo.stop()

        # setto stato personaggi all'inizio del turno
        if not evitaAggiornamentoStatoInizioTurno:
            for nemico in listaNemici:
                nemico.statoInizioTurno = []
                nemico.statoInizioTurno.append(nemico.vita)
                nemico.statoInizioTurno.append(nemico.avvelenato)
                nemico.statoInizioTurno.append(nemico.appiccicato)
            statoRalloInizioTurno = []
            statoRalloInizioTurno.append(dati[5])
            statoRalloInizioTurno.append(dati[121])
            statoRalloInizioTurno.append(dati[123])
            statoRalloInizioTurno.append(dati[124])
            statoColcoInizioTurno = []
            statoColcoInizioTurno.append(dati[10])
            statoColcoInizioTurno.append(dati[122])
            statoColcoInizioTurno.append(dati[125])
            statoColcoInizioTurno.append(dati[126])
            statoEscheInizioTurno = []
            i = 0
            while i < len(vettoreEsche):
                statoEscheInizioTurno.append("Esca" + str(vettoreEsche[i]))
                statoEscheInizioTurno.append(vettoreEsche[i + 1])
                i += 4
        evitaAggiornamentoStatoInizioTurno = False

        # menu start
        if startf and attacco != 1 and dati[5] > 0:
            possibileAprireMenu = SetZoneStanzeImpedimenti.decidiSePoterAprireMenu(dati[0])
            if possibileAprireMenu:
                if not (GlobalGameVar.dictStanze["labirinto1"] <= dati[1] <= GlobalGameVar.dictStanze["labirinto23"]):
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selsta)
                refreshSchermo = True
                dati[2] = x
                dati[3] = y
                dati[140] = npers
                dati[134] = rx
                dati[135] = ry
                # 1->d , 2->a , 3->s , 4->w
                if robot == GlobalImgVar.robod:
                    dati[141] = 1
                elif robot == GlobalImgVar.roboa:
                    dati[141] = 2
                elif robot == GlobalImgVar.robos:
                    dati[141] = 3
                elif robot == GlobalImgVar.robow:
                    dati[141] = 4
                elif robot == GlobalImgVar.robomo:
                    dati[141] = 0
                dati[142] = chiamarob
                dati[139] = mosseRimasteRob
                dati[136] = raffredda
                dati[137] = autoRic1
                dati[138] = autoRic2
                dati[143] = GlobalGameVar.pazzoStrabico
                dati[144] = GlobalGameVar.cambiataAlCastello[0]
                # se c'è un nemico in caselleViste di Rallo => apri il menu di battaglia
                nemicoInCasellaVista = False
                colcoInCasellaVista = False
                i = 0
                while i < len(casevisteDaRallo):
                    for nemico in listaNemici:
                        if nemico.x == casevisteDaRallo[i] and nemico.y == casevisteDaRallo[i + 1] and casevisteDaRallo[i + 2]:
                            nemicoInCasellaVista = True
                            break
                    if rx == casevisteDaRallo[i] and ry == casevisteDaRallo[i + 1] and casevisteDaRallo[i + 2]:
                        colcoInCasellaVista = True
                    i += 3
                if not nemicoInCasellaVista:
                    aggiornaImgEquip = True
                    dati, inizio, attacco, caricaSalvataggio, cambiatoRisoluzione = MenuPrincipali.start(dati, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaroTotale, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco, colcoInCasellaVista)
                    if caricaSalvataggio:
                        inizio = True
                    if attacco == 0:
                        uscitoDaMenu = 2
                    if not inizio:
                        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=3)
                    # aggiorno lo stato di Rallo e Colco all'inizio del turno (altrimenti ci sono bug nell'aggiornare i PV e i PE)
                    statoRalloInizioTurno = []
                    statoRalloInizioTurno.append(dati[5])
                    statoRalloInizioTurno.append(dati[121])
                    statoRalloInizioTurno.append(dati[123])
                    statoRalloInizioTurno.append(dati[124])
                    statoColcoInizioTurno = []
                    statoColcoInizioTurno.append(dati[10])
                    statoColcoInizioTurno.append(dati[122])
                    statoColcoInizioTurno.append(dati[125])
                    statoColcoInizioTurno.append(dati[126])
                else:
                    dati, attacco, sposta, animaOggetto, npers, inizio, cambiatoRisoluzione = MenuPrincipali.startBattaglia(dati, animaOggetto, x, y, npers, rx, ry, inizio, tutteporte, tutticofanetti, listaNemiciTotali, vettoreEsche, vettoreDenaroTotale, listaPersonaggiTotali, ultimoObbiettivoColco, obbiettivoCasualeColco)
                    # cambiare posizione dopo l'uso di caricabatterie
                    if npers == 3:
                        pers = GlobalImgVar.persw
                        arma = armaw
                        armaMov1 = armawMov1
                        armaMov2 = armawMov2
                        armaAttacco = armawAttacco
                        armatura = armaturaw
                        scudo = scudow
                        arco = arcow
                        faretra = faretraw
                        arcoAttacco = arcowAttacco
                        guanti = guantiw
                        guantiMov1 = guantiwMov1
                        guantiMov2 = guantiwMov2
                        guantiAttacco = guantiwAttacco
                        collana = collanaw
                    if npers == 2:
                        pers = GlobalImgVar.persa
                        arma = armaa
                        armaMov1 = armaaMov1
                        armaMov2 = armaaMov2
                        armaAttacco = armaaAttacco
                        armatura = armaturaa
                        scudo = scudoa
                        arco = arcoa
                        faretra = faretraa
                        arcoAttacco = arcoaAttacco
                        guanti = guantia
                        guantiMov1 = guantiaMov1
                        guantiMov2 = guantiaMov2
                        guantiAttacco = guantiaAttacco
                        collana = collanaa
                    if npers == 4:
                        pers = GlobalImgVar.perss
                        arma = armas
                        armaMov1 = armasMov1
                        armaMov2 = armasMov2
                        armaAttacco = armasAttacco
                        armatura = armaturas
                        scudo = scudos
                        arco = arcos
                        faretra = faretras
                        arcoAttacco = arcosAttacco
                        guanti = guantis
                        guantiMov1 = guantisMov1
                        guantiMov2 = guantisMov2
                        guantiAttacco = guantisAttacco
                        collana = collanas
                    if npers == 1:
                        pers = GlobalImgVar.persd
                        arma = armad
                        armaMov1 = armadMov1
                        armaMov2 = armadMov2
                        armaAttacco = armadAttacco
                        armatura = armaturad
                        scudo = scudod
                        arco = arcod
                        faretra = faretrad
                        arcoAttacco = arcodAttacco
                        guanti = guantid
                        guantiMov1 = guantidMov1
                        guantiMov2 = guantidMov2
                        guantiAttacco = guantidAttacco
                        collana = collanad
                    caricaTutto = True
                x = dati[2]
                y = dati[3]
                rx = dati[134]
                ry = dati[135]
                nrob = dati[141]

                # se robo è morto e non lo è più quando esci dal menu rimetti le img giuste del robo
                if morterob and dati[10] > 0:
                    robot = GlobalImgVar.robos
                    armrob = armrobs

                impossibileCliccarePulsanti = True
                carim = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            startf = False

        # per animazione valori cura
        # attaccoDiRallo [obiettivo, danno, status(avvelena, appiccica) ... => per ogni nemico colpito]
        attaccoDiRallo = []
        if statoRalloInizioTurno[0] != dati[5]:
            attaccoDiRallo.append("Rallo")
            attaccoDiRallo.append(dati[5] - statoRalloInizioTurno[0])
            attaccoDiRallo.append("")
        if statoColcoInizioTurno[0] != dati[10]:
            attaccoDiRallo.append("Colco")
            attaccoDiRallo.append(dati[10] - statoColcoInizioTurno[0])
            attaccoDiRallo.append("")

        # morte tua e di robo
        inizio, gameover, riavviaAudioMusica, riavviaAudioAmbiente = FunzioniGraficheGeneriche.controllaMorteRallo(dati[5], pvtot, dati[132], dati[121], dati[123], dati[124], inizio, gameover, riavviaAudioMusica, riavviaAudioAmbiente, dati[0])
        morterob, dati, mosseRimasteRob, ultimoObbiettivoColco = GenericFunc.controllaMorteColco(dati, mosseRimasteRob, ultimoObbiettivoColco)

        # decido se cambiare le stanze pacifiche a seconda dell'avanzamento nella storia
        SetZoneStanzeImpedimenti.modificaStanzePacifiche(dati[0])
        # decido se far avanzare dei dialoghi specifici (in base all'avanzamentoDialoghi di altri personaggi)
        listaAvanzamentoDialoghi, listaPersonaggiTotali = SetDialoghiPersonaggi.avanzaDialoghiSpecifici(dati[0], dati[1], listaAvanzamentoDialoghi, listaPersonaggiTotali)

        # aggiorna img mappa, protagonista
        SetImgOggettiMappaPersonaggi.settaImgMappa(dati[0])
        SetImgOggettiMappaPersonaggi.setImgMenuStartProtagonista(dati[0])
        SetImgOggettiMappaPersonaggi.setImgMenuOggettiProtagonista(dati[0])
        SetImgOggettiMappaPersonaggi.setImgDialogoProtagonista(dati[0])

        if not inizio and not cambiatoRisoluzione and not carim:
            # faccio animazione di quando ricevo un oggetto speciale
            if oggettoRicevuto:
                EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)
                FunzioniGraficheGeneriche.animaOggettoSpecialeRicevuto(oggettoRicevuto)
                oggettoRicevuto = False
                caricaTutto = True

            # movimento-azioni personaggio
            if (nx != 0 or ny != 0) and not nemiciInMovimento and mosseRimasteRob <= 0:
                vx = x
                vy = y
                stanzaVecchia = dati[1]
                x, y, dati[1], carim, cambiosta = SetOstacoliContenutoCofanetti.controlloOstacoli(x, y, nx, ny, dati[1], carim, porte, cofanetti, dati[0])

                sovrapposto = False
                for nemico in listaNemici:
                    if nemico.x == x and nemico.y == y:
                        sovrapposto = True
                        break
                for personaggio in listaPersonaggi:
                    if personaggio.x == x and personaggio.y == y:
                        sovrapposto = True
                        break
                if sovrapposto:
                    x = vx
                    y = vy
                if x == rx and y == ry and not sovrapposto:
                    spingiColco = True
                if not (vx == x and vy == y):
                    sposta = True
                else:
                    GlobalHWVar.canaleSoundPassiRallo.stop()
            # gestione attacchi
            attaccoADistanza = False
            if attacco != 0:
                sposta, creaesca, xesca, yesca, npers, nrob, dati[5], dati[121], dati[10], difesa, apriChiudiPorta, apriCofanetto, listaNemici, attacco, attaccoADistanza, nemicoInquadrato, attaccoDiRallo, chiamarob, ultimoObbiettivoColco, animaOggetto, interagisciConPersonaggio, startf, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, saltaTurno, caseattactotRallo, posizioneRalloAggiornamentoCaseAttac = EnvPrint.attacca(dati, x, y, vx, vy, npers, nrob, rx, ry, obbiettivoCasualeColco, pers, dati[5], pvtot, dif, dati[121], dati[130], dati[123], dati[124], dati[10], entot, difro, dati[122], dati[125], dati[126], imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, attVicino, attLontano, attacco, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, vettoreDenaroStanza, dati[132], nemicoInquadrato, raffredda, autoRic1, autoRic2, ultimoObbiettivoColco, animaOggetto, listaPersonaggi, startf, dati[0], casellePercorribili, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, mosseRimasteRob, nonMostrarePersonaggio, saltaTurno, caseattactotRallo, posizioneRalloAggiornamentoCaseAttac, caselleNonVisibili, casellePercorribiliPorteEscluse, listaNemiciSotterrati, imgNemicoSotterrato)
                # creo cadaveri nemici
                listaPersonaggi, listaPersonaggiTotali, carim, caricaTutto = MovNemiciRob.creaCadaveriNemici(listaNemici, dati[1], dati[0], listaPersonaggi, listaPersonaggiTotali, porte, x, y, rx, ry, casellePercorribiliPorteEscluse, carim, caricaTutto)

                refreshSchermo = True
                caricaTutto = True
                # cancello apertura porta se non si può aprire
                if apriChiudiPorta[0] and not SetZoneStanzeImpedimenti.possibileAprirePorta(dati[1], apriChiudiPorta[1], apriChiudiPorta[2], dati[0]):
                    apriChiudiPorta = [False, 0, 0]
                    sposta = False
                    impossibileAprirePorta = True
                # tolgo una freccia se uso l'attacco a distanza
                if attaccoADistanza:
                    dati[132] -= 1
                # cambiare posizione dopo l'attacco
                if npers == 3:
                    pers = GlobalImgVar.persw
                    arma = armaw
                    armaMov1 = armawMov1
                    armaMov2 = armawMov2
                    armaAttacco = armawAttacco
                    armatura = armaturaw
                    scudo = scudow
                    arco = arcow
                    faretra = faretraw
                    arcoAttacco = arcowAttacco
                    guanti = guantiw
                    guantiMov1 = guantiwMov1
                    guantiMov2 = guantiwMov2
                    guantiAttacco = guantiwAttacco
                    collana = collanaw
                if npers == 2:
                    pers = GlobalImgVar.persa
                    arma = armaa
                    armaMov1 = armaaMov1
                    armaMov2 = armaaMov2
                    armaAttacco = armaaAttacco
                    armatura = armaturaa
                    scudo = scudoa
                    arco = arcoa
                    faretra = faretraa
                    arcoAttacco = arcoaAttacco
                    guanti = guantia
                    guantiMov1 = guantiaMov1
                    guantiMov2 = guantiaMov2
                    guantiAttacco = guantiaAttacco
                    collana = collanaa
                if npers == 4:
                    pers = GlobalImgVar.perss
                    arma = armas
                    armaMov1 = armasMov1
                    armaMov2 = armasMov2
                    armaAttacco = armasAttacco
                    armatura = armaturas
                    scudo = scudos
                    arco = arcos
                    faretra = faretras
                    arcoAttacco = arcosAttacco
                    guanti = guantis
                    guantiMov1 = guantisMov1
                    guantiMov2 = guantisMov2
                    guantiAttacco = guantisAttacco
                    collana = collanas
                if npers == 1:
                    pers = GlobalImgVar.persd
                    arma = armad
                    armaMov1 = armadMov1
                    armaMov2 = armadMov2
                    armaAttacco = armadAttacco
                    armatura = armaturad
                    scudo = scudod
                    arco = arcod
                    faretra = faretrad
                    arcoAttacco = arcodAttacco
                    guanti = guantid
                    guantiMov1 = guantidMov1
                    guantiMov2 = guantidMov2
                    guantiAttacco = guantidAttacco
                    collana = collanad
                # decrementa oggetto utilizzato
                usandoRod = False
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    usandoRod = True
                if sposta and not usandoRod:
                    # bomba attacco = 2
                    if attacco == 2:
                        dati[36] -= 1
                    # bomba veleno attacco = 3
                    if attacco == 3:
                        dati[37] -= 1
                    # esca attacco = 4
                    if attacco == 4:
                        dati[38] -= 1
                    # bomba appiccicosa attacco = 5
                    if attacco == 5:
                        dati[39] -= 1
                    # bomba potenziata attacco = 6
                    if attacco == 6:
                        dati[40] -= 1
            # gestione difesa
            if (not sposta and difesa == 1 and mosseRimasteRob <= 0 and not nemiciInMovimento) or (sposta and difesa == 1):
                difesa = 0
                refreshSchermo = True
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)
            if difesa == 2 and not sposta:
                if dati[1] in GlobalGameVar.vetStanzePacifiche and dati[5] < pvtot:
                    dati[5] = pvtot
                    difesa = 0
                    FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=1)
                    riavviaMusicaPostDifesa = False
                    if GlobalHWVar.canaleSoundCanzone.get_busy():
                        riavviaMusicaPostDifesa = True
                    riavviaAudioAmbientePostDifesa = False
                    if GlobalHWVar.canaliSoundSottofondoAmbientale.getBusy():
                        riavviaAudioAmbientePostDifesa = True
                    GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [0, 0], False, posizioneCanaleMusica=0)
                    if riavviaMusicaPostDifesa:
                        GlobalHWVar.canaleSoundCanzone.stop()
                        if canzone:
                            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
                    if riavviaAudioAmbientePostDifesa:
                        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
                        if len(listaSottofondoAmbientale) > 0:
                            GlobalHWVar.canaliSoundSottofondoAmbientale.riproduci(listaSottofondoAmbientale)
                    GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeCanzoni, GlobalHWVar.volumeEffetti], False, posizioneCanaleMusica=0)
                    caricaTutto = True
                    uscitoDaMenu = 2
                else:
                    difesa = 1
                    sposta = True
            # gestione att+ e dif+
            if dati[123] > 0 and sposta:
                dati[123] = dati[123] - 1
            if dati[124] > 0 and sposta:
                dati[124] = dati[124] - 1
            # effetto collana rigenerante
            animaCuraCollana = -1
            if dati[130] == 1 and sposta:
                if dati[5] + 1 > pvtot:
                    animaCuraCollana = 0
                else:
                    animaCuraCollana = 1
                statoRalloInizioTurno[0] += animaCuraCollana
                dati[5] += 1
                if dati[5] > pvtot:
                    dati[5] = pvtot
            # apertura/chiusura porte
            if apriChiudiPorta[0]:
                k = 0
                while k < len(porte):
                    if porte[k] == dati[1] and porte[k + 1] == apriChiudiPorta[1] and porte[k + 2] == apriChiudiPorta[2]:
                        posizioneRalloAggiornamentoCaseAttac = [0, 0]
                        if porte[k + 3]:
                            GlobalHWVar.canaleSoundInterazioni.play(rumoreChiusuraPorte)
                            porte[k + 3] = False
                        else:
                            GlobalHWVar.canaleSoundInterazioni.play(rumoreAperturaPorte)
                            porte[k + 3] = True
                        caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili, casellePercorribiliPorteEscluse = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])
                        # aggiornare vettore tutteporte
                        j = 0
                        while j < len(tutteporte):
                            if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                tutteporte[j + 3] = porte[k + 3]
                                break
                            j = j + 4
                        # aggiorno inCasellaVista di nemici e personaggi
                        listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caselleNonVisibili, listaNemici, listaPersonaggi)
                        # aggiorno il campo attaccabile di colco
                        if GlobalGameVar.impoPresente:
                            caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                        # aggiorno la vista dei nemici
                        for nemico in listaNemici:
                            if nemico.vita > 0 and nemico.inCasellaVista:
                                nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=True)
                        break
                    k = k + 4
                apriChiudiPorta = [False, 0, 0]
                # controllo se devo deselezionare il nemico/esca inquadrato
                if not type(nemicoInquadrato) is str and nemicoInquadrato:
                    i = 0
                    while i < len(caseviste):
                        if not caseviste[i + 2] and caseviste[i] == nemicoInquadrato.x and caseviste[i + 1] == nemicoInquadrato.y:
                            nemicoInquadrato = False
                            break
                        i += 3
                # vita esche selezionate
                elif type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca"):
                    idEscaInquadrata = int(nemicoInquadrato[4:])
                    i = 0
                    while i < len(vettoreEsche):
                        if idEscaInquadrata == vettoreEsche[i]:
                            j = 0
                            while j < len(caseviste):
                                if caseviste[j] == vettoreEsche[i + 2] and caseviste[j + 1] == vettoreEsche[i + 3] and not caseviste[j + 2]:
                                    nemicoInquadrato = False
                                j += 3
                            break
                        i += 4
            # interazioni con altri personaggi
            if interagisciConPersonaggio:
                for personaggio in listaPersonaggi:
                    if (personaggio.x == x + GlobalHWVar.gpx and personaggio.y == y and npers == 1) or (personaggio.x == x - GlobalHWVar.gpx and personaggio.y == y and npers == 2) or (personaggio.x == x and personaggio.y == y + GlobalHWVar.gpy and npers == 4) or (personaggio.x == x and personaggio.y == y - GlobalHWVar.gpy and npers == 3):
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        if dati[0] < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                            if npers == 1:
                                personaggio.girati("a", perDialogo=True)
                            elif npers == 2:
                                personaggio.girati("d", perDialogo=True)
                            elif npers == 3:
                                personaggio.girati("s", perDialogo=True)
                            elif npers == 4:
                                personaggio.girati("w", perDialogo=True)
                        # aggiorno lo schermo (serve per girare i pers uno verso l'altro e per togliere il campo visivo dell'obiettivo selezionato)
                        EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)
                        if personaggio.oggettoEnigma:
                            dati[0] = MenuEnigmi.mostraEnigma(personaggio.tipo, dati[0])
                        else:
                            dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi, canzone)
                        sposta = False
                        caricaTutto = True
                interagisciConPersonaggio = False
            # menu mercante
            if visualizzaMenuMercante:
                dati = MenuDialoghi.menuMercante(dati)
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=3)
                visualizzaMenuMercante = False
                uscitoDaMenu = 2
                aggiornaImgEquip = True
                carim = True
            # apertura cofanetti
            if apriCofanetto[0]:
                i = 0
                while i < len(cofanetti):
                    if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturacofanetti)
                        dati, tesoro, dati[0] = SetOstacoliContenutoCofanetti.aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                        if tesoro == -2 or tesoro == -1 or tesoro > 0:
                            cofanetti[i + 3] = True
                        # aggiornare vettore tutticofanetti
                        j = 0
                        while j < len(tutticofanetti):
                            if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                                if tesoro == -2 or tesoro == -1 or tesoro > 0:
                                    tutticofanetti[j + 3] = True
                            j = j + 4
                    i = i + 4
                apriCofanetto = [False, 0, 0]
            # scambia posizione con Colco
            if spingiColco:
                rx = vx
                ry = vy
                # nrob: 1=d, 2=a, 3=s, 4=w
                if rx > vrx:
                    nrob = 1
                elif rx < vrx:
                    nrob = 2
                elif ry > vry:
                    nrob = 3
                elif ry < vry:
                    nrob = 4
                if nrob != 0:
                    if nrob == 1:
                        robot = GlobalImgVar.robod
                        armrob = armrobd
                    if nrob == 2:
                        robot = GlobalImgVar.roboa
                        armrob = armroba
                    if nrob == 3:
                        robot = GlobalImgVar.robos
                        armrob = armrobs
                    if nrob == 4:
                        robot = GlobalImgVar.robow
                        armrob = armrobw
                vrx = rx
                vry = ry
                if not chiamarob:
                    caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                    posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                spingiColco = False
            # aggiorna la posizione del telecolco se è attivo
            if chiamarob:
                ultimoObbiettivoColco = []
                ultimoObbiettivoColco.append("Telecomando")
                ultimoObbiettivoColco.append(x)
                ultimoObbiettivoColco.append(y)
                ultimoObbiettivoColco.append("spostamento")

            # impedisce di andare avanti quando si vuole andare in una zona non ancora sbloccata (usato anche per gli eventi)
            if dati[6] != 0 or dati[128] != 0 or dati[8] != 0 or dati[7] != 0:
                equipaggiamentoIndossato = True
            else:
                equipaggiamentoIndossato = False
            if cambiosta and SetZoneStanzeImpedimenti.nonPuoiProcedere(dati[0], stanzaVecchia, dati[1], equipaggiamentoIndossato, listaAvanzamentoDialoghi):
                cambiosta = False
                dati[1] = stanzaVecchia
                xPrimaDiCambioStanza = x
                yPrimaDiCambioStanza = y
                x = vx
                y = vy
                sposta = False
                caricaTutto = True
                bottoneDown = False

                EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)
                personaggio = PersonaggioObj.PersonaggioObj(xPrimaDiCambioStanza, yPrimaDiCambioStanza, False, "Nessuno-0", dati[1], dati[0], False)
                if personaggio.oggettoEnigma:
                    dati[0] = MenuEnigmi.mostraEnigma(personaggio.tipo, dati[0])
                else:
                    dati[0], oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(dati[0], personaggio, listaAvanzamentoDialoghi, canzone)

            # lancio esche
            if creaesca:
                contaesca = 0
                if len(vettoreEsche) > 0:
                    contaesca = vettoreEsche[len(vettoreEsche) - 4] + 1
                # id, vita, xesca, yesca
                vettoreEsche.append(contaesca)
                vettoreEsche.append(GlobalGameVar.vitaTotEsche)
                vettoreEsche.append(xesca)
                vettoreEsche.append(yesca)
                creaesca = False
            # riprendere le esche
            i = 1
            while i < len(vettoreEsche):
                if vettoreEsche[i + 1] == x and vettoreEsche[i + 2] == y:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
                    # tolgo la selezione dell'esca ripresa
                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vettoreEsche[i - 1]:
                        nemicoInquadrato = False
                        caricaTutto = True
                    del vettoreEsche[i + 2]
                    del vettoreEsche[i + 1]
                    del vettoreEsche[i]
                    del vettoreEsche[i - 1]
                    if not GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dati[38] += 1
                i += 4
            i = 0
            while i < len(vettoreEsche):
                if not vettoreEsche[i + 1] in statoEscheInizioTurno:
                    statoEscheInizioTurno.append("Esca" + str(vettoreEsche[i]))
                    statoEscheInizioTurno.append(vettoreEsche[i + 1])
                i += 4

            # cancello ultimoObbiettivoColco se il nemico è morto
            if len(ultimoObbiettivoColco) > 0 and ultimoObbiettivoColco[0].startswith("Nemico"):
                for nemico in listaNemici:
                    if nemico.vita <= 0 and (int(ultimoObbiettivoColco[0].split("-")[1]) == nemico.id or (ultimoObbiettivoColco[1] == nemico.x and ultimoObbiettivoColco[2] == nemico.y)):
                        ultimoObbiettivoColco = []
                        break
            # movimento-azioni robo
            azioneRobEseguita = False
            if GlobalGameVar.impoPresente and dati[122] > 0 and (dati[125] > 0 or dati[126] > 0):
                # se surriscaldato toglie vel+ e efficienza
                dati[125] = 0
                dati[126] = 0
                refreshSchermo = True
            if GlobalGameVar.impoPresente and sposta and mosseRimasteRob == 0 and not morterob and not evitaTurnoDiColco:
                if dati[125] > 0:
                    mosseRimasteRob = 2
                else:
                    mosseRimasteRob = 1
            # attaccoDiColco [obiettivo, danno, status (antidoto, attP, difP, velocizza, efficienza) ... => per ogni nemico colpito (non raffredda perché deve rimanere per più turni)]
            attaccoDiColco = []
            tecnicaUsata = False
            listaNemiciAttaccatiADistanzaRobo = False
            # decremento di surriscalda, raffreddamento, auto-ricarica, auto-ricarica+ / effetto di raffreddamento, auto-ricarica, auto-ricarica+
            if GlobalGameVar.impoPresente:
                raffreddamento = False
                ricarica1 = False
                ricarica2 = False
                if raffredda == 0:
                    raffredda -= 1
                    refreshSchermo = True
                if autoRic1 == 0:
                    autoRic1 -= 1
                    refreshSchermo = True
                if autoRic2 == 0:
                    autoRic2 -= 1
                    refreshSchermo = True
                if sposta:
                    # surriscalda
                    if dati[122] > 0:
                        dati[122] -= 1
                    # raffred
                    if raffredda >= 0:
                        raffredda -= 1
                    if raffredda == 0:
                        dati[122] = 0
                    # autoric
                    if autoRic1 >= 0:
                        autoRic1 -= 1
                    if autoRic1 == 0:
                        qtaRicarica = GlobalGameVar.dannoTecniche[6]
                        dati[10] += GlobalGameVar.dannoTecniche[6]
                        if dati[10] > entot:
                            qtaRicarica = GlobalGameVar.dannoTecniche[6] - (dati[10] - entot)
                            dati[10] = entot
                        attaccoDiColco.append("Colco")
                        attaccoDiColco.append(qtaRicarica)
                        attaccoDiColco.append("")
                        tecnicaUsata = "conclusioneRicarica"
                        dati[122] = GlobalGameVar.durataSurriscaldamento
                    # autoric+
                    if autoRic2 >= 0:
                        autoRic2 -= 1
                    if autoRic2 == 0:
                        qtaRicarica = GlobalGameVar.dannoTecniche[16]
                        dati[10] += GlobalGameVar.dannoTecniche[16]
                        if dati[10] > entot:
                            qtaRicarica = GlobalGameVar.dannoTecniche[16] - (dati[10] - entot)
                            dati[10] = entot
                        attaccoDiColco.append("Colco")
                        attaccoDiColco.append(qtaRicarica)
                        attaccoDiColco.append("")
                        tecnicaUsata = "conclusioneRicarica+"
                        dati[122] = GlobalGameVar.durataSurriscaldamento
            if GlobalGameVar.impoPresente and mosseRimasteRob > 0 and not morterob and not cambiosta and not evitaTurnoDiColco:
                vrx = rx
                vry = ry

                # movimento - gambit
                if raffredda < 0 and autoRic1 < 0 and autoRic2 < 0:
                    rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneRobEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche = MovNemiciRob.movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco=False)
                    # creo cadaveri nemici
                    listaPersonaggi, listaPersonaggiTotali, carim, caricaTutto = MovNemiciRob.creaCadaveriNemici(listaNemici, dati[1], dati[0], listaPersonaggi, listaPersonaggiTotali, porte, x, y, rx, ry, casellePercorribiliPorteEscluse, carim, caricaTutto)

                if dati[122] > 0 or raffreddamento or ricarica1 or ricarica2:
                    mosseRimasteRob -= 2
                else:
                    mosseRimasteRob -= 1
                if raffreddamento:
                    raffredda = 1
                if ricarica1:
                    autoRic1 = 1
                if ricarica2:
                    autoRic2 = 1

                sovrapposto = False
                for nemico in listaNemici:
                    if nemico.x == rx and nemico.y == ry and nemico.vita > 0:
                        sovrapposto = True
                        break
                if sovrapposto:
                    rx = vrx
                    ry = vry
                    nrob = 0
                    azioneRobEseguita = False
                if nrob != 0:
                    if nrob == 1:
                        robot = GlobalImgVar.robod
                        armrob = armrobd
                    if nrob == 2:
                        robot = GlobalImgVar.roboa
                        armrob = armroba
                    if nrob == 3:
                        robot = GlobalImgVar.robos
                        armrob = armrobs
                    if nrob == 4:
                        robot = GlobalImgVar.robow
                        armrob = armrobw
                if (rx != vrx or ry != vry) and not chiamarob:
                    caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                    posizioneColcoAggiornamentoCaseAttac = [rx, ry]
            elif GlobalGameVar.impoPresente and sposta and mosseRimasteRob < 0 and not morterob:
                mosseRimasteRob += 1
            if GlobalGameVar.impoPresente and morterob:
                robot = GlobalImgVar.robomo
                armrob = GlobalImgVar.armrobmo
            if not GlobalGameVar.impoPresente:
                rx = GlobalHWVar.gsx
                ry = GlobalHWVar.gsy
                vrx = rx
                vry = ry
            evitaTurnoDiColco = False

            # aggiorna vista dei mostri (per mettere l'occhio se ti vedono) e aggiorno xPosizioneUltimoBersaglio e yPosizioneUltimoBersaglio se ci sono attacchi a distanza
            apriocchio = False
            for nemico in listaNemici:
                if nemico.vita > 0 and nemico.inCasellaVista:
                    nemico.aggiornaBersaglioAttacchiDistanti(x, y, rx, ry, attaccoADistanza, listaNemiciAttaccatiADistanzaRobo)
                    nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste)
                    if nemico.visto:
                        apriocchio = True
                else:
                    nemico.visto = False
            # movimento-azioni mostri
            impossibileParare = SetZoneStanzeImpedimenti.decidiSePoterParare(dati[0])
            if len(listaNemici) > 0 and not cambiosta:
                for nemico in listaNemici:
                    if nemico.vita > 0 and nemico.inCasellaVista and dati[5] > 0:
                        if sposta and nemico.mosseRimaste == 0:
                            nemico.resettaMosseRimaste()
                        if nemico.mosseRimaste > 0:
                            vetDatiNemici = []
                            for nemicoTemp in listaNemici:
                                if nemicoTemp.vita > 0:
                                    vetDatiNemici.append(nemicoTemp.vita)
                                    vetDatiNemici.append(nemicoTemp.x)
                                    vetDatiNemici.append(nemicoTemp.y)
                                    vetDatiNemici.append(nemicoTemp.vitaTotale)
                            # trovo l'obiettivo
                            nemico.settaObbiettivo(x, y, rx, ry, dati, vettoreDenaroStanza, vettoreEsche, listaPersonaggi, listaNemici, porte, caseviste)
                            nemico.vx = nemico.x
                            nemico.vy = nemico.y
                            nemico, direzioneMostro, dati, vettoreEsche = MovNemiciRob.movmostro(x, y, rx, ry, morterob, nemico, dif, difro, par, dati, vettoreEsche, vetDatiNemici, listaPersonaggi, caseviste, impossibileParare)
                            if direzioneMostro == 1:
                                nemico.girati("d")
                            elif direzioneMostro == 2:
                                nemico.girati("a")
                            elif direzioneMostro == 3:
                                nemico.girati("s")
                            elif direzioneMostro == 4:
                                nemico.girati("w")
                            i = 0
                            while i < len(vetDatiNemici):
                                if nemico.x == vetDatiNemici[i + 1] and nemico.y == vetDatiNemici[i + 2]:
                                    nemico.x = nemico.vx
                                    nemico.y = nemico.vy
                                    nemico.animaSpostamento = False
                                    break
                                i += 4
                            for personaggio in listaPersonaggi:
                                if nemico.x == personaggio.x and nemico.y == personaggio.y:
                                    nemico.x = nemico.vx
                                    nemico.y = nemico.vy
                                    nemico.animaSpostamento = False
                                    break
                            if (nemico.x == x and nemico.y == y) or (nemico.x == rx and nemico.y == ry):
                                nemico.x = nemico.vx
                                nemico.y = nemico.vy
                                nemico.animaSpostamento = False
                            # raccolta delle esche da parte dei nemici
                            i = 1
                            while i < len(vettoreEsche):
                                if vettoreEsche[i + 1] == nemico.x and vettoreEsche[i + 2] == nemico.y:
                                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
                                    # tolgo la selezione dell'esca sparita
                                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vettoreEsche[i - 1]:
                                        nemicoInquadrato = False
                                        caricaTutto = True
                                    del vettoreEsche[i + 2]
                                    del vettoreEsche[i + 1]
                                    del vettoreEsche[i]
                                    del vettoreEsche[i - 1]
                                i += 4
                            if nemico.animaSpostamento or (len(nemico.percorso) > 0 and (nemico.percorso[nemico.numeroMovimento] == "" or nemico.percorso[nemico.numeroMovimento].endswith("Gira"))):
                                if nemico.numeroMovimento < len(nemico.percorso) - 1:
                                    nemico.numeroMovimento += 1
                                else:
                                    nemico.numeroMovimento = 0
                            if nemico.vx != nemico.x or nemico.vy != nemico.y:
                                nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste)
                            nemico.compiMossa()
                        elif sposta and nemico.mosseRimaste < 0:
                            nemico.mosseRimaste += 1
                    elif nemico.vita <= 0:
                        dati[127] += nemico.esp
                        # metto il suo denaro nella casella in cui è morto (vettore => qta, x, y)
                        denaroDroppato = nemico.denaro
                        # effetto portafortuna
                        if dati[130] == 3:
                            denaroDroppato += int(nemico.denaro * 1.5)
                        if denaroDroppato > 0:
                            vettoreDenaroTotale.append(denaroDroppato)
                            vettoreDenaroTotale.append(nemico.x)
                            vettoreDenaroTotale.append(nemico.y)
                            vettoreDenaroTotale.append(dati[1])
                            vettoreDenaroStanza.append(denaroDroppato)
                            vettoreDenaroStanza.append(nemico.x)
                            vettoreDenaroStanza.append(nemico.y)
                        nemico.morto = True
                        nemico.animaMorte = True

            # effetto veleno su Rallo + veleno su nemici + surriscaldamento su impo -> vengono fatti alla fine del turno per farli combaciare con le animazioni
            animaEffettoVeleno = -1
            if dati[121] and sposta and dati[5] > 0:
                if dati[5] - 2 > 0:
                    animaEffettoVeleno = 2
                elif dati[5] - 1 > 0:
                    animaEffettoVeleno = 1
                else:
                    animaEffettoVeleno = 0
                dati[5] -= 2
                if dati[5] <= 0:
                    dati[5] = 1
            animaEffettoSurriscaldamento = -1
            if GlobalGameVar.impoPresente and sposta and dati[122] > 0 and dati[10] > 0:
                animaEffettoSurriscaldamento = 1
                dati[10] -= 1
            animaEffettoVelenoNemico = []
            for nemico in listaNemici:
                if nemico.avvelenato and sposta and nemico.vita > 0 and not cambiosta:
                    animaEffettoVelenoNemico.append(nemico.id)
                    if nemico.vita - 3 > 0:
                        animaEffettoVelenoNemico.append(3)
                    elif nemico.vita - 2 > 0:
                        animaEffettoVelenoNemico.append(2)
                    elif nemico.vita - 1 > 0:
                        animaEffettoVelenoNemico.append(1)
                    else:
                        animaEffettoVelenoNemico.append(0)
                    nemico.vita -= 3
                    if nemico.vita <= 0:
                        nemico.vita = 1

            # movimento personaggi che sono in una casella vista
            if sposta:
                for personaggio in listaPersonaggi:
                    if personaggio.inCasellaVista and not personaggio.mantieniSempreASchermo:
                        personaggio.spostati(x, y, rx, ry, listaNemici, listaPersonaggi, caseviste)

            # aumentare di livello
            while dati[127] >= esptot and dati[4] < 100:
                dati[4] += 1
                dati[127] -= esptot
                aumentoliv += 1
                esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)
                impossibileCliccarePulsanti = True

            # aggiorna i dialoghi e le img di tutti i personaggi in base all'avanzamento nella storia
            for personaggio in listaPersonaggi:
                if personaggio.tipo.startswith("Oggetto"):
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            # fai tutte le animazioni del turno e disegni gli sfondi e personaggi
            if caricaTutto:
                refreshSchermo = True
                if aumentoliv != 0:
                    pvtot = GenericFunc.getVitaTotRallo(dati[4] - aumentoliv, dati[129])
                EnvPrint.disegnaAmbiente(x, y, npers, statoRalloInizioTurno[0], pvtot, statoRalloInizioTurno[1], statoRalloInizioTurno[2], statoRalloInizioTurno[3], statoColcoInizioTurno[0], entot, statoColcoInizioTurno[1], statoColcoInizioTurno[2], statoColcoInizioTurno[3], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, True, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)
                caricaTutto = False
            if (azioneRobEseguita or nemiciInMovimento or sposta) and not uscitoDaMenu > 0 and not stanzaCambiata:
                primopasso, caricaTutto, tesoro, bottoneDown, movimentoPerMouse, robot, armrob = Animazioni.anima(sposta, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, scudo, armatura, arma, armaMov1, armaMov2, armaAttacco, scudoDifesa, arco, faretra, arcoAttacco, guanti, guantiMov1, guantiMov2, guantiAttacco, guantiDifesa, collana, armas, armaturas, arcos, faretras, collanas, armrob, armrobs, dati, attacco, difesa, bottoneDown, tesoro, aumentoliv, caricaTutto, listaNemici, vettoreEsche, vettoreDenaroStanza, attaccoADistanza, caseviste, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, nemicoInquadrato, attaccoDiRallo, attaccoDiColco, statoRalloInizioTurno, statoColcoInizioTurno, statoEscheInizioTurno, raffreddamento, ricarica1, ricarica2, raffredda, autoRic1, autoRic2, animaOggetto, listaPersonaggi, apriocchio, chiamarob, movimentoPerMouse, vettoreImgCaselle, nonMostrarePersonaggio, saltaTurno, stanzaVecchia, animaCuraCollana, animaEffettoVeleno, animaEffettoVelenoNemico, animaEffettoSurriscaldamento, listaNemiciSotterrati, imgNemicoSotterrato)
            if not carim and (refreshSchermo or azioneRobEseguita or nemiciInMovimento or sposta):
                refreshSchermo = False
                apriocchio = False
                for nemico in listaNemici:
                    if nemico.vita > 0 and nemico.visto:
                        apriocchio = True
                        break
                pvtot = GenericFunc.getVitaTotRallo(dati[4], dati[129])
                EnvPrint.disegnaAmbiente(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers, imgSfondoStanza, portaVert, portaOriz, arma, armatura, scudo, arco, faretra, guanti, collana, robot, armrob, armrobs, vettoreEsche, porte, cofanetti, caseviste, apriocchio, chiamarob, listaNemici, caricaTutto, vettoreDenaroStanza, dati[132], nemicoInquadrato, statoEscheInizioTurno, raffredda, autoRic1, autoRic2, raffreddamento, ricarica1, ricarica2, listaPersonaggi, False, stanzaCambiata, uscitoDaMenu, casellePercorribili, vettoreImgCaselle, entrateStanza, caselleNonVisibili, dati[0], nonMostrarePersonaggio, saltaTurno, casellePercorribiliPorteEscluse, difesa, arcos, faretras, armaturas, collanas, armas, guantiDifesa, scudoDifesa, listaNemiciSotterrati, imgNemicoSotterrato)

            if GlobalHWVar.testOstacoliAttivi:
                FunzioniPerTest.testOstacoli(x, y, rx, ry, dati[1], porte, cofanetti, dati[0], entrateStanza)

            # gestisce eventi speciali come i dialoghi del tutorial o dialoghi con nessuno
            if not carim:
                porteTemp = porte[:]
                if movimentoDaCompiere and len(percorsoDaEseguire) == 0:
                    GlobalHWVar.canaleSoundPassiRallo.stop()
                x, y, rx, ry, nrob, dati[0], cambiosta, dati[1], npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, dati[131], percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, evitaAvanzamentoTurno, avanzaManualmentePercorsoDaEseguire, listaNemiciSotterrati = SetNemiciPersonaggiEventi.gestisciEventiStoria(dati[0], dati[1], npers, x, y, rx, ry, nrob, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, canzone, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, dati[131], percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire, listaNemiciSotterrati)
                impossibileAprirePorta = False
                if caricaTutto:
                    impossibileCliccarePulsanti = True
                if porteTemp != porte:
                    posizioneRalloAggiornamentoCaseAttac = [0, 0]
                    # aggiorno inCasellaVista di nemici e personaggi
                    listaNemici, listaPersonaggi = GenericFunc.aggiornaInCasellaVistaDiNemiciEPersonaggi(caselleNonVisibili, listaNemici, listaPersonaggi)
                    # aggiorno il campo attaccabile di colco
                    if GlobalGameVar.impoPresente:
                        caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
                        posizioneColcoAggiornamentoCaseAttac = [rx, ry]
                    # aggiorno la vista dei nemici
                    for nemico in listaNemici:
                        if nemico.vita > 0 and nemico.inCasellaVista:
                            nemico.aggiornaVista(x, y, rx, ry, vettoreEsche, vettoreDenaroStanza, dati, caseviste, forzaAggiornamentoCaselleAttaccabili=True)
                    caseviste, casevisteDaRallo, casevisteEntrateIncluse, caselleNonVisibili, casellePercorribili, casellePercorribiliPorteEscluse = GenericFunc.creaTuttiIVettoriPerLeCaselleViste(x, y, rx, ry, dati[1], porte, cofanetti, dati[0])

            # tolgo le esche sovrapposte a eventuali personaggi o nemici creati negli eventi
            i = 0
            while i < len(vettoreEsche):
                escaCancellata = False
                for personaggio in listaPersonaggi:
                    if vettoreEsche[i + 2] == personaggio.x and vettoreEsche[i + 3] == personaggio.y:
                        del vettoreEsche[i + 3]
                        del vettoreEsche[i + 2]
                        del vettoreEsche[i + 1]
                        del vettoreEsche[i]
                        escaCancellata = True
                        break
                if not escaCancellata:
                    for nemico in listaNemici:
                        if vettoreEsche[i + 2] == nemico.x and vettoreEsche[i + 3] == nemico.y:
                            del vettoreEsche[i + 3]
                            del vettoreEsche[i + 2]
                            del vettoreEsche[i + 1]
                            del vettoreEsche[i]
                            escaCancellata = True
                            break
                if not escaCancellata:
                    i += 4

            # creo cadaveri nemici nel caso non siano morti per azioni di Rallo o di Colco (non dovrebbero esserci altre cause, ma magari non hai tenuto conto di qualcosa, eh?! O magari metterai qualcos'altro in futuro...)
            listaPersonaggi, listaPersonaggiTotali, carim, caricaTutto = MovNemiciRob.creaCadaveriNemici(listaNemici, dati[1], dati[0], listaPersonaggi, listaPersonaggiTotali, porte, x, y, rx, ry, casellePercorribiliPorteEscluse, carim, caricaTutto)
            # cancella definitivamente i mostri morti e resetta vx/vy/anima
            i = len(listaNemici) - 1
            while i >= 0:
                nemico = listaNemici[i]
                nemico.vx = nemico.x
                nemico.vy = nemico.y
                nemico.animaSpostamento = False
                nemico.animaAttacco = False
                nemico.animaMorte = False
                nemico.animaDanneggiamento = []
                nemico.bersaglioColpito = []
                nemico.ralloParato = False
                if not type(nemicoInquadrato) is str and nemicoInquadrato and nemicoInquadrato.morto:
                    nemicoInquadrato = False
                    caricaTutto = True
                if nemico.morto:
                    listaNemici.remove(nemico)
                    listaNemiciTotali.remove(nemico)
                i -= 1
            # morte esche
            i = 1
            while i < len(vettoreEsche):
                if vettoreEsche[i] <= 0:
                    # tolgo la selezione dell'esca morta
                    if type(nemicoInquadrato) is str and nemicoInquadrato.startswith("Esca") and int(nemicoInquadrato[4:]) == vettoreEsche[i - 1]:
                        nemicoInquadrato = False
                        caricaTutto = True
                    del vettoreEsche[i + 2]
                    del vettoreEsche[i + 1]
                    del vettoreEsche[i]
                    del vettoreEsche[i - 1]
                else:
                    i += 4

            # aggiorna i dialoghi e le img di tutti i personaggi in base all'avanzamento nella storia e resetta vx/vy/anima
            for personaggio in listaPersonaggi:
                personaggio.vx = personaggio.x
                personaggio.vy = personaggio.y
                personaggio.animaSpostamento = False
                # aggiorno il dialogo in caso di oggetto-personaggi che sono in più di una casella
                if personaggio.tipo.startswith("Oggetto"):
                    i = 0
                    while i < len(listaAvanzamentoDialoghi):
                        if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                            if personaggio.avanzamentoDialogo != listaAvanzamentoDialoghi[i + 1]:
                                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                            break
                        i += 2
                personaggio.aggiornaDialogo(dati[0], dati[131])
                if personaggio.tipo.startswith("Oggetto"):
                    imgAggiornata = personaggio.aggiornaImgOggetto(dati[0])
                    if imgAggiornata:
                        refreshSchermo = True

            # prendere il denaro da terra
            i = 0
            while i < len(vettoreDenaroTotale):
                denaroPreso = False
                if vettoreDenaroTotale[i + 3] == dati[1]:
                    if vettoreDenaroTotale[i + 1] == x and vettoreDenaroTotale[i + 2] == y:
                        dati = UtilityOstacoliContenutoCofanetti.ottieniMonete(dati, vettoreDenaroTotale[i])
                        j = 0
                        while j < len(vettoreDenaroStanza):
                            if vettoreDenaroStanza[j + 1] == vettoreDenaroTotale[i + 1] and vettoreDenaroStanza[j + 2] == vettoreDenaroTotale[i + 2]:
                                del vettoreDenaroStanza[j + 2]
                                del vettoreDenaroStanza[j + 1]
                                del vettoreDenaroStanza[j]
                                break
                            j += 3
                        del vettoreDenaroTotale[i + 3]
                        del vettoreDenaroTotale[i + 2]
                        del vettoreDenaroTotale[i + 1]
                        del vettoreDenaroTotale[i]
                        denaroPreso = True
                    if not denaroPreso:
                        for nemico in listaNemici:
                            if vettoreDenaroTotale[i + 1] == nemico.x and vettoreDenaroTotale[i + 2] == nemico.y:
                                nemico.denaro += vettoreDenaroTotale[i]
                                j = 0
                                while j < len(vettoreDenaroStanza):
                                    if vettoreDenaroStanza[j + 1] == vettoreDenaroTotale[i + 1] and vettoreDenaroStanza[j + 2] == vettoreDenaroTotale[i + 2]:
                                        del vettoreDenaroStanza[j + 2]
                                        del vettoreDenaroStanza[j + 1]
                                        del vettoreDenaroStanza[j]
                                        break
                                    j += 3
                                del vettoreDenaroTotale[i + 3]
                                del vettoreDenaroTotale[i + 2]
                                del vettoreDenaroTotale[i + 1]
                                del vettoreDenaroTotale[i]
                                refreshSchermo = True
                                denaroPreso = True
                                break
                if not denaroPreso:
                    i += 4

            # tolgo animazione valore danni dopo il tempo limite
            FunzioniGraficheGeneriche.aggiornaBarreStatusPerValoriDanniCureScaduti(dati, pvtot, nemicoInquadrato, entot, vettoreEsche, sposta)

            # aggiorno la presenza di Impo
            SetZoneStanzeImpedimenti.settaPresenzaDiColco(dati[0])

            movimentoDaCompiere = False
            vx = x
            vy = y
            vrx = rx
            vry = ry
            attacco = 0
            animaOggetto = [False, 0, 0]
            stanzaCambiata = False
            uscitoDaMenu -= 1
            sposta = False

        if inizio:
            if not caricaSalvataggio:
                FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
            GlobalHWVar.canaleSoundPuntatoreSposta.stop()
            GlobalHWVar.canaleSoundPuntatoreSeleziona.stop()
            GlobalHWVar.canaleSoundPassiRallo.stop()
            GlobalHWVar.canaleSoundPassiColco.stop()
            GlobalHWVar.canaleSoundPassiNemici.stop()
            GlobalHWVar.canaleSoundPassiPersonaggi.stop()
            GlobalHWVar.canaleSoundMorteNemici.stop()
            GlobalHWVar.canaleSoundLvUp.stop()
            GlobalHWVar.canaleSoundInterazioni.stop()
            GlobalHWVar.canaleSoundAttacco.stop()
            GlobalHWVar.canaleSoundMelodieEventi.stop()
            GlobalHWVar.canaleSoundBattitoCardiaco.stop()
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone, GlobalHWVar.canaliSoundSottofondoAmbientale], [0, 0], False, posizioneCanaleMusica=0)
            GlobalHWVar.canaleSoundCanzone.stop()
            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
            GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
        elif cambiatoRisoluzione:
            # controlla se devi cambiare personaggio giocabile
            personaggioDaUsare = SetImgOggettiMappaPersonaggi.cambiaProtagonista(dati[0])
            personaggioUsato = personaggioDaUsare

        if dati[0] == GlobalGameVar.dictAvanzamentoStoria["fine"]:
            dati[0] += 1
            # tolgo l'equipaggiamento (spada, scudo, armatura, arco, guanti e collana)
            dati[6] = 0
            dati[7] = 0
            dati[8] = 0
            dati[128] = 0
            dati[129] = 0
            dati[130] = 0
            # aggiorno il vettore "dati"
            dati[2] = x
            dati[3] = y
            dati[140] = npers
            dati[134] = rx
            dati[135] = ry
            if robot == GlobalImgVar.robod:
                dati[141] = 1
            elif robot == GlobalImgVar.roboa:
                dati[141] = 2
            elif robot == GlobalImgVar.robos:
                dati[141] = 3
            elif robot == GlobalImgVar.robow:
                dati[141] = 4
            elif robot == GlobalImgVar.robomo:
                dati[141] = 0
            dati[142] = chiamarob
            dati[139] = mosseRimasteRob
            dati[136] = raffredda
            dati[137] = autoRic1
            dati[138] = autoRic2
            dati[143] = GlobalGameVar.pazzoStrabico
            dati[144] = GlobalGameVar.cambiataAlCastello[0]
            SottoMenuSalva.scegli_sal(True, len(dati), len(tutteporte), len(tutticofanetti), tutteporte, tutticofanetti, vettoreEsche, vettoreDenaroTotale, dati, listaNemiciTotali, stanzeGiaVisitate, listaPersonaggiTotali, listaAvanzamentoDialoghi, oggettiRimastiAHans, ultimoObbiettivoColco, obbiettivoCasualeColco, fineDelGioco=True)
            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
            i = 0
            while i < 30:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            inizio = True
        GlobalGameVar.partitaAppenaAvviataPostFinale = False

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMainLoop.tick(GlobalHWVar.fpsMainLoop)

gameloop()
