# -*- coding: utf-8 -*-

import random
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.SettaggiLivelli.SetOstacoliContenutoCofanetti as SetOstacoliContenutoCofanetti
import Codice.SettaggiLivelli.SetZoneStanzeImpedimenti as SetZoneStanzeImpedimenti
import Codice.Localizzazione.LocalizInterfaccia as LI


def creaCadaveriNemici(listaNemici, stanza, avanzamentoStoria, listaPersonaggi, listaPersonaggiTotali, porte, x, y, rx, ry, casellePercorribiliPorteEscluse, carim=False, caricaTutto=False):
    # creazione personaggi-oggetto cadaveri (nel castello => solo se non ti bloccano per andare avanti)
    vatCadaveriDaCreare = []
    for nemico in listaNemici:
        if nemico.vita <= 0:
            if GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"] and GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
                listaCaselleUscitaTemp = []
                if stanza == GlobalGameVar.dictStanze["internoCastello2"]:
                    listaCaselleUscitaTemp.append([GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2])
                    listaCaselleUscitaTemp.append([GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2])
                    listaCaselleUscitaTemp.append([GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 2])
                    listaCaselleUscitaTemp.append([GlobalHWVar.gpx * 23, GlobalHWVar.gpy * 2])
                    listaCaselleUscitaTemp.append([GlobalHWVar.gpx * 24, GlobalHWVar.gpy * 2])
                    listaCaselleUscitaTemp.append([GlobalHWVar.gpx * 25, GlobalHWVar.gpy * 2])
                else:
                    if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
                        stanzaDestinazioneTemp = GlobalGameVar.dictStanze["esternoCastello5"]
                    elif stanza == GlobalGameVar.dictStanze["internoCastello9"] and ((x <= GlobalHWVar.gpx * 16 and y >= GlobalHWVar.gpy * 7) or y >= GlobalHWVar.gpy * 12):
                        stanzaDestinazioneTemp = GlobalGameVar.dictStanze["internoCastello11"]
                    elif stanza == GlobalGameVar.dictStanze["internoCastello12"]:
                        stanzaDestinazioneTemp = GlobalGameVar.dictStanze["internoCastello9"]
                    else:
                        stanzaDestinazioneTemp = stanza - 1
                    vetEntrateTemp = SetOstacoliContenutoCofanetti.getEntrateStanze(stanza, avanzamentoStoria)
                    i = 0
                    while i < len(vetEntrateTemp):
                        if vetEntrateTemp[i + 4] == stanzaDestinazioneTemp:
                            listaCaselleUscitaTemp.append([vetEntrateTemp[i], vetEntrateTemp[i + 1]])
                        i += 5
                vetNemiciSoloConXeY = []
                for personaggio in listaPersonaggi:
                    vetNemiciSoloConXeY.append(personaggio.x)
                    vetNemiciSoloConXeY.append(personaggio.y)
                vetNemiciSoloConXeY.append(nemico.x)
                vetNemiciSoloConXeY.append(nemico.y)
                for cadavere in vatCadaveriDaCreare:
                    vetNemiciSoloConXeY.append(cadavere[1])
                    vetNemiciSoloConXeY.append(cadavere[2])
                # aggiungo anche le porte che non si possono aprire
                k = 0
                while k < len(porte):
                    if stanza == porte[k] and not SetZoneStanzeImpedimenti.possibileAprirePorta(stanza, porte[k + 1], porte[k + 2], avanzamentoStoria):
                        vetNemiciSoloConXeY.append(porte[k + 1])
                        vetNemiciSoloConXeY.append(porte[k + 2])
                    k += 4
                for casellaUscita in listaCaselleUscitaTemp:
                    percorsoTrovato = GenericFunc.pathFinding(x, y, casellaUscita[0], casellaUscita[1], vetNemiciSoloConXeY, casellePercorribiliPorteEscluse)
                    if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) > 0:
                        percorsoTrovato = GenericFunc.pathFinding(rx, ry, casellaUscita[0], casellaUscita[1], vetNemiciSoloConXeY, casellePercorribiliPorteEscluse)
                        if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) > 0:
                            vatCadaveriDaCreare.append(["OggettoDictCadavereSoldatoCastello" + str(nemico.posizMorte) + "-" + str(nemico.id), nemico.x, nemico.y])
                            break
            elif not GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
                vatCadaveriDaCreare.append(["OggettoDictCadavere" + nemico.tipo + str(nemico.posizMorte) + "-" + str(nemico.id), nemico.x, nemico.y])
    for cadavere in vatCadaveriDaCreare:
        creaCadavere = True
        i = 0
        while i < len(listaPersonaggi):
            if listaPersonaggi[i].x == cadavere[1] and listaPersonaggi[i].y == cadavere[2]:
                creaCadavere = False
                break
            i += 1
        if creaCadavere:
            personaggio = PersonaggioObj.PersonaggioObj(cadavere[1], cadavere[2], "s", cadavere[0], stanza, avanzamentoStoria, [])
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            carim = True
            caricaTutto = True

    return listaPersonaggi, listaPersonaggiTotali, carim, caricaTutto


def movmostro(x, y, rx, ry, morterob, nemico, dif, difro, par, dati, vettoreEsche, vetNemici, listaPersonaggi, caseviste, impossibileParare):
    sposta = False
    attacca = False
    nmos = 0
    nmx = 0
    nmy = 0
    avvelena = nemico.velenoso
    surriscalda = nemico.surriscaldante

    if nemico.obbiettivo[0] == "Esca" or nemico.obbiettivo[0] == "Colco" or nemico.obbiettivo[0] == "Rallo":
        nemico.triggerato = True
        # nemici che attaccano da vicino
        if not nemico.attaccaDaLontano:
            if (nemico.obbiettivo[1] == nemico.x + GlobalHWVar.gpx and nemico.obbiettivo[2] == nemico.y) or (nemico.obbiettivo[1] == nemico.x - GlobalHWVar.gpx and nemico.obbiettivo[2] == nemico.y) or (nemico.obbiettivo[1] == nemico.x and nemico.obbiettivo[2] == nemico.y + GlobalHWVar.gpy) or (nemico.obbiettivo[1] == nemico.x and nemico.obbiettivo[2] == nemico.y - GlobalHWVar.gpy) or (nemico.obbiettivo[1] == nemico.x and nemico.obbiettivo[2] == nemico.y):
                if nemico.obbiettivo[0] == "Esca":
                    danno = nemico.attacco
                    if danno < 0:
                        danno = 0
                    escabersaglio = -1
                    i = 0
                    while i < len(vettoreEsche):
                        if nemico.obbiettivo[1] == vettoreEsche[i + 2] and nemico.obbiettivo[2] == vettoreEsche[i + 3]:
                            escabersaglio = i
                            break
                        i += 4
                    if escabersaglio != -1:
                        nemico.bersaglioColpito.append("Esca" + str(vettoreEsche[escabersaglio]))
                        nemico.bersaglioColpito.append(-danno)
                        nemico.bersaglioColpito.append("")
                        if vettoreEsche[escabersaglio + 1] - danno <= 0:
                            nemico.bersaglioColpito.append(True)
                        else:
                            nemico.bersaglioColpito.append(False)
                        # print ("attacco vicino", nemico.tipo, "a esca", danno)
                        vettoreEsche[escabersaglio + 1] = vettoreEsche[escabersaglio + 1] - danno
                elif nemico.obbiettivo[0] == "Colco":
                    danno = GenericFunc.calcoloDanni(nemico.attacco, difro)
                    nemico.bersaglioColpito.append("Colco")
                    nemico.bersaglioColpito.append(-danno)
                    if surriscalda:
                        dati[122] = GlobalGameVar.durataSurriscaldamento
                        nemico.bersaglioColpito.append("surriscalda")
                    else:
                        nemico.bersaglioColpito.append("")
                    if dati[10] - danno <= 0:
                        nemico.bersaglioColpito.append(True)
                    else:
                        nemico.bersaglioColpito.append(False)
                    # print ("attacco vicino", nemico.tipo, "a robo", danno)
                    dati[10] = dati[10] - danno
                elif nemico.obbiettivo[0] == "Rallo":
                    danno = GenericFunc.calcoloDanni(nemico.attacco, dif)
                    if random.randint(1, 100) <= par and not impossibileParare:
                        danno = 0
                        avvelena = False
                        nemico.ralloParato = True
                        # print ("parato:", par)
                    nemico.bersaglioColpito.append("Rallo")
                    nemico.bersaglioColpito.append(-danno)
                    if avvelena and not dati[130] == 2:
                        dati[121] = True
                        nemico.bersaglioColpito.append("avvelena")
                    else:
                        nemico.bersaglioColpito.append("")
                    if dati[5] - danno <= 0:
                        nemico.bersaglioColpito.append(True)
                    else:
                        nemico.bersaglioColpito.append(False)
                    # print ("attacco vicino", nemico.tipo, "a rallo", danno)
                    dati[5] = dati[5] - danno
                nmos = 0
                if nemico.obbiettivo[1] == nemico.x + GlobalHWVar.gpx and nemico.obbiettivo[2] == nemico.y:
                    nmos = 1
                if nemico.obbiettivo[1] == nemico.x - GlobalHWVar.gpx and nemico.obbiettivo[2] == nemico.y:
                    nmos = 2
                if nemico.obbiettivo[1] == nemico.x and nemico.obbiettivo[2] == nemico.y + GlobalHWVar.gpy:
                    nmos = 3
                if nemico.obbiettivo[1] == nemico.x and nemico.obbiettivo[2] == nemico.y - GlobalHWVar.gpy:
                    nmos = 4
                attacca = True
                sposta = False
            else:
                percorsoTrovato = nemico.obbiettivo[3]
                if percorsoTrovato and not percorsoTrovato == "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y):
                    if percorsoTrovato[len(percorsoTrovato) - 4] > nemico.x:
                        nmos = 1
                    if percorsoTrovato[len(percorsoTrovato) - 4] < nemico.x:
                        nmos = 2
                    if percorsoTrovato[len(percorsoTrovato) - 3] > nemico.y:
                        nmos = 3
                    if percorsoTrovato[len(percorsoTrovato) - 3] < nemico.y:
                        nmos = 4
                    sposta = True
                else:
                    # print ("Percorso nemico verso obiettivo non trovato")
                    # ricalcolo togliendo i nemici e i personaggi dagli ostacoli
                    vetNemiciSoloConXeY = []
                    if dati[10] <= 0:
                        vetNemiciSoloConXeY.append(rx)
                        vetNemiciSoloConXeY.append(ry)
                    percorsoTrovato = GenericFunc.pathFinding(nemico.x, nemico.y, nemico.obbiettivo[1], nemico.obbiettivo[2], vetNemiciSoloConXeY, caseviste)
                    if percorsoTrovato and not percorsoTrovato == "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y):
                        if percorsoTrovato[len(percorsoTrovato) - 4] > nemico.x:
                            nmos = 1
                        if percorsoTrovato[len(percorsoTrovato) - 4] < nemico.x:
                            nmos = 2
                        if percorsoTrovato[len(percorsoTrovato) - 3] > nemico.y:
                            nmos = 3
                        if percorsoTrovato[len(percorsoTrovato) - 3] < nemico.y:
                            nmos = 4
                        sposta = True
                    else:
                        # print ("Percorso nemico verso obiettivo non trovato (senza nemici e personaggi come ostacoli)")
                        if abs(nemico.obbiettivo[1] - nemico.x) > abs(nemico.obbiettivo[2] - nemico.y):
                            if nemico.x < nemico.obbiettivo[1]:
                                nmos = 1
                            if nemico.x > nemico.obbiettivo[1]:
                                nmos = 2
                            sposta = True
                        elif abs(nemico.obbiettivo[2] - nemico.y) > abs(nemico.obbiettivo[1] - nemico.x):
                            if nemico.y < nemico.obbiettivo[2]:
                                nmos = 3
                            if nemico.y > nemico.obbiettivo[2]:
                                nmos = 4
                            sposta = True
                        elif (abs(nemico.obbiettivo[1] - nemico.x) == abs(nemico.obbiettivo[2] - nemico.y)) and (nemico.obbiettivo[1] != nemico.x) and (nemico.obbiettivo[2] != nemico.y):
                            c = random.randint(1, 2)
                            if nemico.x < nemico.obbiettivo[1] and c == 1:
                                nmos = 1
                            if nemico.x > nemico.obbiettivo[1] and c == 1:
                                nmos = 2
                            if nemico.y < nemico.obbiettivo[2] and c == 2:
                                nmos = 3
                            if nemico.y > nemico.obbiettivo[2] and c == 2:
                                nmos = 4
                            sposta = True
        # nemici che attaccano da lontano
        elif nemico.attaccaDaLontano:
            if nemico.obbiettivo[0] == "Esca":
                danno = nemico.attacco
                if danno < 0:
                    danno = 0
                escabersaglio = -1
                i = 0
                while i < len(vettoreEsche):
                    if nemico.obbiettivo[1] == vettoreEsche[i + 2] and nemico.obbiettivo[2] == vettoreEsche[i + 3]:
                        escabersaglio = i
                        break
                    i += 4
                if escabersaglio != -1:
                    nemico.bersaglioColpito.append("Esca" + str(vettoreEsche[escabersaglio]))
                    nemico.bersaglioColpito.append(-danno)
                    nemico.bersaglioColpito.append("")
                    if vettoreEsche[escabersaglio + 1] - danno <= 0:
                        nemico.bersaglioColpito.append(True)
                    else:
                        nemico.bersaglioColpito.append(False)
                    # print ("attacco lontano", nemico.tipo, "a esca", danno)
                    vettoreEsche[escabersaglio + 1] = vettoreEsche[escabersaglio + 1] - danno
                nmos = 0
                if abs(nemico.obbiettivo[1] - nemico.x) > abs(nemico.obbiettivo[2] - nemico.y):
                    if nemico.x < nemico.obbiettivo[1]:
                        nmos = 1
                    if nemico.x > nemico.obbiettivo[1]:
                        nmos = 2
                if abs(nemico.obbiettivo[2] - nemico.y) > abs(nemico.obbiettivo[1] - nemico.x):
                    if nemico.y < nemico.obbiettivo[2]:
                        nmos = 3
                    if nemico.y > nemico.obbiettivo[2]:
                        nmos = 4
                if (abs(nemico.obbiettivo[1] - nemico.x) == abs(nemico.obbiettivo[2] - nemico.y)) and (nemico.obbiettivo[1] != nemico.x) and (nemico.obbiettivo[2] != nemico.y):
                    c = random.randint(1, 2)
                    if nemico.x < nemico.obbiettivo[1] and c == 1:
                        nmos = 1
                    if nemico.x > nemico.obbiettivo[1] and c == 1:
                        nmos = 2
                    if nemico.y < nemico.obbiettivo[2] and c == 2:
                        nmos = 3
                    if nemico.y > nemico.obbiettivo[2] and c == 2:
                        nmos = 4
                attacca = True
                sposta = False
            else:
                ralloVicino = False
                colcoVicino = False
                if (abs(x - nemico.x) == GlobalHWVar.gpx and abs(y - nemico.y) == 0) or (abs(x - nemico.x) == 0 and abs(y - nemico.y) == GlobalHWVar.gpy):
                    ralloVicino = True
                if not morterob and ((abs(rx - nemico.x) == GlobalHWVar.gpx and abs(ry - nemico.y) == 0) or (abs(rx - nemico.x) == 0 and abs(ry - nemico.y) == GlobalHWVar.gpy)):
                    colcoVicino = True
                if ralloVicino or colcoVicino:
                    # nmos: 1=d, 2=a, 3=s, 4=w
                    casellaDaControllarePrima = 0
                    if ralloVicino and colcoVicino:
                        nmosPossibili = []
                        nmxProbabile = GlobalHWVar.gpx
                        nmyProbabile = 0
                        mxProbabile = nemico.x
                        myProbabile = nemico.y
                        i = 0
                        while i < len(caseviste):
                            if caseviste[i] == nemico.x + nmxProbabile and caseviste[i + 1] == nemico.y + nmyProbabile:
                                if caseviste[i + 2]:
                                    mxProbabile = nemico.x + nmxProbabile
                                    myProbabile = nemico.y + nmyProbabile
                                break
                            i += 3
                        casellaOccupata = False
                        if (abs(x - mxProbabile) == GlobalHWVar.gpx and abs(y - myProbabile) == 0) or (abs(x - mxProbabile) == 0 and abs(y - myProbabile) == GlobalHWVar.gpy) or (x == mxProbabile and y == myProbabile):
                            casellaOccupata = True
                        if (not morterob and ((abs(rx - mxProbabile) == GlobalHWVar.gpx and abs(ry - myProbabile) == 0) or (abs(rx - mxProbabile) == 0 and abs(ry - myProbabile) == GlobalHWVar.gpy))) or (rx == mxProbabile and ry == myProbabile):
                            casellaOccupata = True
                        i = 0
                        while i < len(vetNemici):
                            if vetNemici[i + 1] == mxProbabile and vetNemici[i + 2] == myProbabile:
                                casellaOccupata = True
                                break
                            i += 4
                        for personaggio in listaPersonaggi:
                            if personaggio.x == mxProbabile and personaggio.y == myProbabile:
                                casellaOccupata = True
                                break
                        if not casellaOccupata:
                            nmosPossibili.append(1)
                        nmxProbabile = -GlobalHWVar.gpx
                        nmyProbabile = 0
                        mxProbabile = nemico.x
                        myProbabile = nemico.y
                        i = 0
                        while i < len(caseviste):
                            if caseviste[i] == nemico.x + nmxProbabile and caseviste[i + 1] == nemico.y + nmyProbabile:
                                if caseviste[i + 2]:
                                    mxProbabile = nemico.x + nmxProbabile
                                    myProbabile = nemico.y + nmyProbabile
                                break
                            i += 3
                        casellaOccupata = False
                        if (abs(x - mxProbabile) == GlobalHWVar.gpx and abs(y - myProbabile) == 0) or (abs(x - mxProbabile) == 0 and abs(y - myProbabile) == GlobalHWVar.gpy) or (x == mxProbabile and y == myProbabile):
                            casellaOccupata = True
                        if (not morterob and ((abs(rx - mxProbabile) == GlobalHWVar.gpx and abs(ry - myProbabile) == 0) or (abs(rx - mxProbabile) == 0 and abs(ry - myProbabile) == GlobalHWVar.gpy))) or (rx == mxProbabile and ry == myProbabile):
                            casellaOccupata = True
                        i = 0
                        while i < len(vetNemici):
                            if vetNemici[i + 1] == mxProbabile and vetNemici[i + 2] == myProbabile:
                                casellaOccupata = True
                                break
                            i += 4
                        for personaggio in listaPersonaggi:
                            if personaggio.x == mxProbabile and personaggio.y == myProbabile:
                                casellaOccupata = True
                                break
                        if not casellaOccupata:
                            nmosPossibili.append(2)
                        nmxProbabile = 0
                        nmyProbabile = GlobalHWVar.gpy
                        mxProbabile = nemico.x
                        myProbabile = nemico.y
                        i = 0
                        while i < len(caseviste):
                            if caseviste[i] == nemico.x + nmxProbabile and caseviste[i + 1] == nemico.y + nmyProbabile:
                                if caseviste[i + 2]:
                                    mxProbabile = nemico.x + nmxProbabile
                                    myProbabile = nemico.y + nmyProbabile
                                break
                            i += 3
                        casellaOccupata = False
                        if (abs(x - mxProbabile) == GlobalHWVar.gpx and abs(y - myProbabile) == 0) or (abs(x - mxProbabile) == 0 and abs(y - myProbabile) == GlobalHWVar.gpy) or (x == mxProbabile and y == myProbabile):
                            casellaOccupata = True
                        if (not morterob and ((abs(rx - mxProbabile) == GlobalHWVar.gpx and abs(ry - myProbabile) == 0) or (abs(rx - mxProbabile) == 0 and abs(ry - myProbabile) == GlobalHWVar.gpy))) or (rx == mxProbabile and ry == myProbabile):
                            casellaOccupata = True
                        i = 0
                        while i < len(vetNemici):
                            if vetNemici[i + 1] == mxProbabile and vetNemici[i + 2] == myProbabile:
                                casellaOccupata = True
                                break
                            i += 4
                        for personaggio in listaPersonaggi:
                            if personaggio.x == mxProbabile and personaggio.y == myProbabile:
                                casellaOccupata = True
                                break
                        if not casellaOccupata:
                            nmosPossibili.append(3)
                        nmxProbabile = 0
                        nmyProbabile = -GlobalHWVar.gpy
                        mxProbabile = nemico.x
                        myProbabile = nemico.y
                        i = 0
                        while i < len(caseviste):
                            if caseviste[i] == nemico.x + nmxProbabile and caseviste[i + 1] == nemico.y + nmyProbabile:
                                if caseviste[i + 2]:
                                    mxProbabile = nemico.x + nmxProbabile
                                    myProbabile = nemico.y + nmyProbabile
                                break
                            i += 3
                        casellaOccupata = False
                        if (abs(x - mxProbabile) == GlobalHWVar.gpx and abs(y - myProbabile) == 0) or (abs(x - mxProbabile) == 0 and abs(y - myProbabile) == GlobalHWVar.gpy) or (x == mxProbabile and y == myProbabile):
                            casellaOccupata = True
                        if (not morterob and ((abs(rx - mxProbabile) == GlobalHWVar.gpx and abs(ry - myProbabile) == 0) or (abs(rx - mxProbabile) == 0 and abs(ry - myProbabile) == GlobalHWVar.gpy))) or (rx == mxProbabile and ry == myProbabile):
                            casellaOccupata = True
                        i = 0
                        while i < len(vetNemici):
                            if vetNemici[i + 1] == mxProbabile and vetNemici[i + 2] == myProbabile:
                                casellaOccupata = True
                                break
                            i += 4
                        for personaggio in listaPersonaggi:
                            if personaggio.x == mxProbabile and personaggio.y == myProbabile:
                                casellaOccupata = True
                                break
                        if not casellaOccupata:
                            nmosPossibili.append(4)

                        if len(nmosPossibili) > 0:
                            nmosScelta = random.randint(1, len(nmosPossibili)) - 1
                            nmos = nmosPossibili[nmosScelta]
                            sposta = True
                    else:
                        if ralloVicino:
                            if nemico.x - GlobalHWVar.gpx == x and nemico.y == y:
                                casellaDaControllarePrima = 1
                            elif nemico.x + GlobalHWVar.gpx == x and nemico.y == y:
                                casellaDaControllarePrima = 2
                            elif nemico.x == x and nemico.y - GlobalHWVar.gpy == y:
                                casellaDaControllarePrima = 3
                            elif nemico.x == x and nemico.y + GlobalHWVar.gpy == y:
                                casellaDaControllarePrima = 4
                        elif colcoVicino:
                            if nemico.x - GlobalHWVar.gpx == rx and nemico.y == ry:
                                casellaDaControllarePrima = 1
                            elif nemico.x + GlobalHWVar.gpx == rx and nemico.y == ry:
                                casellaDaControllarePrima = 2
                            elif nemico.x == rx and nemico.y - GlobalHWVar.gpy == ry:
                                casellaDaControllarePrima = 3
                            elif nemico.x == rx and nemico.y + GlobalHWVar.gpy == ry:
                                casellaDaControllarePrima = 4

                        ordineCaselleDaControllare = []
                        ordineCaselleDaControllare.append(casellaDaControllarePrima)
                        caselleDaControllare = [1, 2, 3, 4]
                        caselleDaControllare.remove(casellaDaControllarePrima)
                        i = 0
                        while i < 3:
                            ordineCaselleDaControllare.append(caselleDaControllare.pop(random.randint(0, len(caselleDaControllare) - 1)))
                            i += 1

                        for i in ordineCaselleDaControllare:
                            nmxProbabile = 0
                            nmyProbabile = 0
                            if i == 1:
                                nmxProbabile = GlobalHWVar.gpx
                                nmyProbabile = 0
                            elif i == 2:
                                nmxProbabile = -GlobalHWVar.gpx
                                nmyProbabile = 0
                            elif i == 3:
                                nmxProbabile = 0
                                nmyProbabile = GlobalHWVar.gpy
                            elif i == 4:
                                nmxProbabile = 0
                                nmyProbabile = -GlobalHWVar.gpy
                            mxProbabile = nemico.x
                            myProbabile = nemico.y
                            j = 0
                            while j < len(caseviste):
                                if caseviste[j] == nemico.x + nmxProbabile and caseviste[j + 1] == nemico.y + nmyProbabile:
                                    if caseviste[j + 2]:
                                        mxProbabile = nemico.x + nmxProbabile
                                        myProbabile = nemico.y + nmyProbabile
                                    break
                                j += 3
                            casellaOccupata = False
                            if (abs(x - mxProbabile) == GlobalHWVar.gpx and abs(y - myProbabile) == 0) or (abs(x - mxProbabile) == 0 and abs(y - myProbabile) == GlobalHWVar.gpy) or (x == mxProbabile and y == myProbabile):
                                casellaOccupata = True
                            if (not morterob and ((abs(rx - mxProbabile) == GlobalHWVar.gpx and abs(ry - myProbabile) == 0) or (abs(rx - mxProbabile) == 0 and abs(ry - myProbabile) == GlobalHWVar.gpy))) or (rx == mxProbabile and ry == myProbabile):
                                casellaOccupata = True
                            j = 0
                            while j < len(vetNemici):
                                if vetNemici[j + 1] == mxProbabile and vetNemici[j + 2] == myProbabile:
                                    casellaOccupata = True
                                    break
                                j += 4
                            for personaggio in listaPersonaggi:
                                if personaggio.x == mxProbabile and personaggio.y == myProbabile:
                                    casellaOccupata = True
                                    break
                            if not casellaOccupata:
                                nmos = i
                                sposta = True
                                break

                if not sposta:
                    if nemico.obbiettivo[0] == "Colco":
                        danno = GenericFunc.calcoloDanni(nemico.attacco, difro)
                        nemico.bersaglioColpito.append("Colco")
                        nemico.bersaglioColpito.append(-danno)
                        if surriscalda:
                            dati[122] = GlobalGameVar.durataSurriscaldamento
                            nemico.bersaglioColpito.append("surriscalda")
                        else:
                            nemico.bersaglioColpito.append("")
                        if dati[10] - danno <= 0:
                            nemico.bersaglioColpito.append(True)
                        else:
                            nemico.bersaglioColpito.append(False)
                        # print ("attacco lontano", nemico.tipo, "a robo", danno)
                        dati[10] = dati[10] - danno
                    elif nemico.obbiettivo[0] == "Rallo":
                        danno = GenericFunc.calcoloDanni(nemico.attacco, dif)
                        if random.randint(1, 100) <= par and not impossibileParare:
                            danno = 0
                            avvelena = False
                            nemico.ralloParato = True
                            # print ("parato:", par)
                        nemico.bersaglioColpito.append("Rallo")
                        nemico.bersaglioColpito.append(-danno)
                        if avvelena and not dati[130] == 2:
                            dati[121] = True
                            nemico.bersaglioColpito.append("avvelena")
                        else:
                            nemico.bersaglioColpito.append("")
                        if dati[5] - danno <= 0:
                            nemico.bersaglioColpito.append(True)
                        else:
                            nemico.bersaglioColpito.append(False)
                        # print ("attacco lontano", nemico.tipo, "a rallo", danno)
                        dati[5] = dati[5] - danno
                    nmos = 0
                    if abs(nemico.obbiettivo[1] - nemico.x) > abs(nemico.obbiettivo[2] - nemico.y):
                        if nemico.x < nemico.obbiettivo[1]:
                            nmos = 1
                        if nemico.x > nemico.obbiettivo[1]:
                            nmos = 2
                    if abs(nemico.obbiettivo[2] - nemico.y) > abs(nemico.obbiettivo[1] - nemico.x):
                        if nemico.y < nemico.obbiettivo[2]:
                            nmos = 3
                        if nemico.y > nemico.obbiettivo[2]:
                            nmos = 4
                    if (abs(nemico.obbiettivo[1] - nemico.x) == abs(nemico.obbiettivo[2] - nemico.y)) and (nemico.obbiettivo[1] != nemico.x) and (nemico.obbiettivo[2] != nemico.y):
                        c = random.randint(1, 2)
                        if nemico.x < nemico.obbiettivo[1] and c == 1:
                            nmos = 1
                        if nemico.x > nemico.obbiettivo[1] and c == 1:
                            nmos = 2
                        if nemico.y < nemico.obbiettivo[2] and c == 2:
                            nmos = 3
                        if nemico.y > nemico.obbiettivo[2] and c == 2:
                            nmos = 4
                    attacca = True
                    sposta = False
    elif nemico.obbiettivo[0] == "Monete":
        nemico.triggerato = True
        percorsoTrovato = nemico.obbiettivo[3]
        if percorsoTrovato and not percorsoTrovato == "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y):
            if percorsoTrovato[len(percorsoTrovato) - 4] > nemico.x:
                nmos = 1
            if percorsoTrovato[len(percorsoTrovato) - 4] < nemico.x:
                nmos = 2
            if percorsoTrovato[len(percorsoTrovato) - 3] > nemico.y:
                nmos = 3
            if percorsoTrovato[len(percorsoTrovato) - 3] < nemico.y:
                nmos = 4
            sposta = True
        else:
            # print ("Percorso nemico verso monete non trovato")
            # ricalcolo togliendo i nemici e i personaggi dagli ostacoli
            vetNemiciSoloConXeY = []
            if dati[10] <= 0:
                vetNemiciSoloConXeY.append(rx)
                vetNemiciSoloConXeY.append(ry)
            percorsoTrovato = GenericFunc.pathFinding(nemico.x, nemico.y, nemico.obbiettivo[1], nemico.obbiettivo[2], vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato and not percorsoTrovato == "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y):
                if percorsoTrovato[len(percorsoTrovato) - 4] > nemico.x:
                    nmos = 1
                if percorsoTrovato[len(percorsoTrovato) - 4] < nemico.x:
                    nmos = 2
                if percorsoTrovato[len(percorsoTrovato) - 3] > nemico.y:
                    nmos = 3
                if percorsoTrovato[len(percorsoTrovato) - 3] < nemico.y:
                    nmos = 4
                sposta = True
            else:
                # print ("Percorso nemico verso monete non trovato (senza nemici e personaggi come ostacoli)")
                if abs(nemico.obbiettivo[1] - nemico.x) > abs(nemico.obbiettivo[2] - nemico.y):
                    if nemico.x < nemico.obbiettivo[1]:
                        nmos = 1
                    if nemico.x > nemico.obbiettivo[1]:
                        nmos = 2
                    sposta = True
                elif abs(nemico.obbiettivo[2] - nemico.y) > abs(nemico.obbiettivo[1] - nemico.x):
                    if nemico.y < nemico.obbiettivo[2]:
                        nmos = 3
                    if nemico.y > nemico.obbiettivo[2]:
                        nmos = 4
                    sposta = True
                elif (abs(nemico.obbiettivo[1] - nemico.x) == abs(nemico.obbiettivo[2] - nemico.y)) and (nemico.obbiettivo[1] != nemico.x) and (nemico.obbiettivo[2] != nemico.y):
                    c = random.randint(1, 2)
                    if nemico.x < nemico.obbiettivo[1] and c == 1:
                        nmos = 1
                    if nemico.x > nemico.obbiettivo[1] and c == 1:
                        nmos = 2
                    if nemico.y < nemico.obbiettivo[2] and c == 2:
                        nmos = 3
                    if nemico.y > nemico.obbiettivo[2] and c == 2:
                        nmos = 4
                    sposta = True
    elif nemico.xPosizioneUltimoBersaglio and nemico.yPosizioneUltimoBersaglio:
        nemico.triggerato = True
        if (nemico.xPosizioneUltimoBersaglio == nemico.x + GlobalHWVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y) or (nemico.xPosizioneUltimoBersaglio == nemico.x - GlobalHWVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y) or (nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y + GlobalHWVar.gpy) or (nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y - GlobalHWVar.gpy):
            if nemico.xPosizioneUltimoBersaglio == nemico.x + GlobalHWVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y:
                nmos = 1
            if nemico.xPosizioneUltimoBersaglio == nemico.x - GlobalHWVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y:
                nmos = 2
            if nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y + GlobalHWVar.gpy:
                nmos = 3
            if nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y - GlobalHWVar.gpy:
                nmos = 4
            nemico.obbiettivo = ["", 0, 0, []]
            sposta = True
        else:
            vetNemiciSoloConXeY = []
            if dati[10] <= 0:
                vetNemiciSoloConXeY.append(rx)
                vetNemiciSoloConXeY.append(ry)
            i = 0
            while i < len(vetNemici):
                if not (vetNemici[i + 1] == nemico.x and vetNemici[i + 2] == nemico.y):
                    vetNemiciSoloConXeY.append(vetNemici[i + 1])
                    vetNemiciSoloConXeY.append(vetNemici[i + 2])
                i += 4
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            percorsoTrovato = GenericFunc.pathFinding(nemico.x, nemico.y, nemico.xPosizioneUltimoBersaglio, nemico.yPosizioneUltimoBersaglio, vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato and not percorsoTrovato == "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y):
                if percorsoTrovato[len(percorsoTrovato) - 4] > nemico.x:
                    nmos = 1
                if percorsoTrovato[len(percorsoTrovato) - 4] < nemico.x:
                    nmos = 2
                if percorsoTrovato[len(percorsoTrovato) - 3] > nemico.y:
                    nmos = 3
                if percorsoTrovato[len(percorsoTrovato) - 3] < nemico.y:
                    nmos = 4
                sposta = True
            else:
                # print ("Percorso nemico verso ultimo bersaglio non trovato")
                # ricalcolo togliendo i nemici e i personaggi dagli ostacoli
                vetNemiciSoloConXeY = []
                if dati[10] <= 0:
                    vetNemiciSoloConXeY.append(rx)
                    vetNemiciSoloConXeY.append(ry)
                percorsoTrovato = GenericFunc.pathFinding(nemico.x, nemico.y, nemico.xPosizioneUltimoBersaglio, nemico.yPosizioneUltimoBersaglio, vetNemiciSoloConXeY, caseviste)
                if percorsoTrovato and not percorsoTrovato == "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y):
                    if percorsoTrovato[len(percorsoTrovato) - 4] > nemico.x:
                        nmos = 1
                    if percorsoTrovato[len(percorsoTrovato) - 4] < nemico.x:
                        nmos = 2
                    if percorsoTrovato[len(percorsoTrovato) - 3] > nemico.y:
                        nmos = 3
                    if percorsoTrovato[len(percorsoTrovato) - 3] < nemico.y:
                        nmos = 4
                    sposta = True
                else:
                    # print ("Percorso nemico verso ultimo bersaglio non trovato (senza nemici e personaggi come ostacoli)")
                    if abs(nemico.xPosizioneUltimoBersaglio - nemico.x) > abs(nemico.yPosizioneUltimoBersaglio - nemico.y):
                        if nemico.x < nemico.xPosizioneUltimoBersaglio:
                            nmos = 1
                        if nemico.x > nemico.xPosizioneUltimoBersaglio:
                            nmos = 2
                        sposta = True
                    elif abs(nemico.yPosizioneUltimoBersaglio - nemico.y) > abs(nemico.xPosizioneUltimoBersaglio - nemico.x):
                        if nemico.y < nemico.yPosizioneUltimoBersaglio:
                            nmos = 3
                        if nemico.y > nemico.yPosizioneUltimoBersaglio:
                            nmos = 4
                        sposta = True
                    elif (abs(nemico.xPosizioneUltimoBersaglio - nemico.x) == abs(nemico.yPosizioneUltimoBersaglio - nemico.y)) and (nemico.xPosizioneUltimoBersaglio != nemico.x) and (nemico.yPosizioneUltimoBersaglio != nemico.y):
                        c = random.randint(1, 2)
                        if nemico.x < nemico.xPosizioneUltimoBersaglio and c == 1:
                            nmos = 1
                        if nemico.x > nemico.xPosizioneUltimoBersaglio and c == 1:
                            nmos = 2
                        if nemico.y < nemico.yPosizioneUltimoBersaglio and c == 2:
                            nmos = 3
                        if nemico.y > nemico.yPosizioneUltimoBersaglio and c == 2:
                            nmos = 4
                        sposta = True
    else:
        nemico.obbiettivo = ["", 0, 0, []]
        if nemico.triggerato:
            nmos = random.randint(0, 4)
        else:
            if len(nemico.percorso) > 0:
                direzione = nemico.percorso[nemico.numeroMovimento]
            else:
                direzione = ""
            if direzione == "w":
                nmos = 4
            elif direzione == "a":
                nmos = 2
            elif direzione == "s":
                nmos = 3
            elif direzione == "d":
                nmos = 1
            elif direzione.endswith("Gira"):
                nemico.girati(direzione[0])
                nmos = 0
            else:
                nmos = 0
        sposta = True

    # spostamento
    if sposta:
        # 1=d, 2=a, 3=s, 4=w
        if nmos == 1:
            if nemico.obbiettivo[0] != "Monete" and nemico.x + GlobalHWVar.gpx == nemico.obbiettivo[1] and nemico.y == nemico.obbiettivo[2]:
                nmx = 0
                nmy = 0
            else:
                nmx = GlobalHWVar.gpx
                nmy = 0
        if nmos == 2:
            if nemico.obbiettivo[0] != "Monete" and nemico.x - GlobalHWVar.gpx == nemico.obbiettivo[1] and nemico.y == nemico.obbiettivo[2]:
                nmx = 0
                nmy = 0
            else:
                nmx = -GlobalHWVar.gpx
                nmy = 0
        if nmos == 3:
            if nemico.obbiettivo[0] != "Monete" and nemico.x == nemico.obbiettivo[1] and nemico.y + GlobalHWVar.gpy == nemico.obbiettivo[2]:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = GlobalHWVar.gpy
        if nmos == 4:
            if nemico.obbiettivo[0] != "Monete" and nemico.x == nemico.obbiettivo[1] and nemico.y - GlobalHWVar.gpy == nemico.obbiettivo[2]:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = -GlobalHWVar.gpy
        if not nemico.ignoraEsche:
            i = 2
            while i <= len(vettoreEsche):
                if nemico.x + nmx == vettoreEsche[i] and nemico.y + nmy == vettoreEsche[i + 1]:
                    nmx = 0
                    nmy = 0
                    break
                i += 4

    i = 0
    while i < len(caseviste):
        if caseviste[i] == nemico.x + nmx and caseviste[i + 1] == nemico.y + nmy:
            if caseviste[i + 2]:
                nemico.x += nmx
                nemico.y += nmy
            break
        i += 3

    if sposta and (nemico.x != nemico.vx or nemico.y != nemico.vy):
        nemico.animaSpostamento = True
    if attacca:
        nemico.animaAttacco = True
    return nemico, nmos, dati, vettoreEsche


def eseguiAzione(rx, ry, nemicoBersaglio, azione, suAlleato, nemiciVistiDaColco, dati, caselleVisteDaColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, listaNemici, caseviste, pathToRallo, pathToNemico):
    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)
    if dati[126] > 0:
        costoTecnicaUsata = GlobalGameVar.costoTecniche[azione - 1] // 2
    else:
        costoTecnicaUsata = GlobalGameVar.costoTecniche[azione - 1]
    raffreddamento = False
    ricarica1 = False
    ricarica2 = False
    azioneEseguita = False
    nrob = 0
    sposta = False

    if azione == 6 or azione == 7 or azione == 11 or azione == 14 or azione == 17:
        if dati[10] > costoTecnicaUsata and not (dati[122] > 0 and (azione == 11 or azione == 14)):
            azioneEseguita = True
            attaccoDiColco.append("Colco")
            attaccoDiColco.append(-costoTecnicaUsata)
            attaccoDiColco.append("")
            dati[10] -= costoTecnicaUsata
            attaccoDiColco.append("Colco")
            attaccoDiColco.append(0)
        # raffred
        if azione == 6 and azioneEseguita:
            raffreddamento = True
            attaccoDiColco.append("raffredda")
        # ricarica
        if azione == 7 and azioneEseguita:
            ricarica1 = True
            attaccoDiColco.append("")
        # velocizza
        if azione == 11 and azioneEseguita and dati[122] <= 0:
            dati[125] = GlobalGameVar.dannoTecniche[azione - 1]
            attaccoDiColco.append("velocizza")
        # efficienza
        if azione == 14 and azioneEseguita and dati[122] <= 0:
            dati[126] = GlobalGameVar.dannoTecniche[azione - 1]
            attaccoDiColco.append("efficienza")
        # ricarica+
        if azione == 17 and azioneEseguita:
            ricarica2 = True
            attaccoDiColco.append("")
        if not suAlleato:
            return azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, listaNemici
        else:
            return azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, listaNemici
    elif not suAlleato:
        mostroAccanto = False
        mostroVisto = True
        if (rx == nemicoBersaglio.x and ry == nemicoBersaglio.y) or (rx + GlobalHWVar.gpx == nemicoBersaglio.x and ry == nemicoBersaglio.y) or (rx - GlobalHWVar.gpx == nemicoBersaglio.x and ry == nemicoBersaglio.y) or (rx == nemicoBersaglio.x and ry + GlobalHWVar.gpy == nemicoBersaglio.y) or (rx == nemicoBersaglio.x and ry - GlobalHWVar.gpy == nemicoBersaglio.y):
            mostroAccanto = True
            mostroVisto = True
        if mostroAccanto and (azione == 1 or azione == 2 or azione == 3 or azione == 8 or azione == 9 or azione == 12 or azione == 13 or azione == 16 or azione == 18):
            if dati[10] > costoTecnicaUsata:
                azioneEseguita = True
                attaccoDiColco.append("Colco")
                attaccoDiColco.append(-costoTecnicaUsata)
                attaccoDiColco.append("")
                dati[10] -= costoTecnicaUsata
            # scossa
            if azione == 1 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = GenericFunc.calcoloDanni(danno, nemicoBersaglio.difesa)
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # cura
            if azione == 2 and azioneEseguita:
                pvGuadagnati = GlobalGameVar.dannoTecniche[azione - 1]
                if pvGuadagnati + nemicoBersaglio.vita > nemicoBersaglio.vitaTotale:
                    pvGuadagnati = nemicoBersaglio.vitaTotale - nemicoBersaglio.vita
                nemicoBersaglio.vita += pvGuadagnati
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(pvGuadagnati)
                attaccoDiColco.append("")
            # antidoto
            if azione == 3 and azioneEseguita:
                nemicoBersaglio.avvelenato = False
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(0)
                attaccoDiColco.append("antidoto")
            # cura+
            if azione == 8 and azioneEseguita:
                pvGuadagnati = GlobalGameVar.dannoTecniche[azione - 1]
                if pvGuadagnati + nemicoBersaglio.vita > nemicoBersaglio.vitaTotale:
                    pvGuadagnati = nemicoBersaglio.vitaTotale - nemicoBersaglio.vita
                nemicoBersaglio.vita += pvGuadagnati
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(pvGuadagnati)
                attaccoDiColco.append("")
            # scossa+
            if azione == 9 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = GenericFunc.calcoloDanni(danno, nemicoBersaglio.difesa)
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # attP
            if azione == 12 and azioneEseguita:
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(0)
                attaccoDiColco.append("")
            # difP
            if azione == 13 and azioneEseguita:
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(0)
                attaccoDiColco.append("")
            # cura++
            if azione == 16 and azioneEseguita:
                pvGuadagnati = GlobalGameVar.dannoTecniche[azione - 1]
                if pvGuadagnati + nemicoBersaglio.vita > nemicoBersaglio.vitaTotale:
                    pvGuadagnati = nemicoBersaglio.vitaTotale - nemicoBersaglio.vita
                nemicoBersaglio.vita += pvGuadagnati
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(pvGuadagnati)
                attaccoDiColco.append("")
            # scossa++
            if azione == 18 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = GenericFunc.calcoloDanni(danno, nemicoBersaglio.difesa)
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # giro Colco verso l'obiettivo
            if azioneEseguita:
                if abs(nemicoBersaglio.x - rx) > abs(nemicoBersaglio.y - ry):
                    if rx < nemicoBersaglio.x:
                        nrob = 1
                    if rx > nemicoBersaglio.x:
                        nrob = 2
                if abs(nemicoBersaglio.y - ry) > abs(nemicoBersaglio.x - rx):
                    if ry < nemicoBersaglio.y:
                        nrob = 3
                    if ry > nemicoBersaglio.y:
                        nrob = 4
                if (abs(nemicoBersaglio.x - rx) == abs(nemicoBersaglio.y - ry)) and (nemicoBersaglio.x != rx) and (nemicoBersaglio.y != ry):
                    c = random.randint(1, 2)
                    if rx < nemicoBersaglio.x and c == 1:
                        nrob = 1
                    if rx > nemicoBersaglio.x and c == 1:
                        nrob = 2
                    if ry < nemicoBersaglio.y and c == 2:
                        nrob = 3
                    if ry > nemicoBersaglio.y and c == 2:
                        nrob = 4
        elif mostroVisto and (azione == 4 or azione == 5 or azione == 10 or azione == 15 or azione == 19 or azione == 20):
            if dati[10] > costoTecnicaUsata:
                azioneEseguita = True
                attaccoDiColco.append("Colco")
                attaccoDiColco.append(-costoTecnicaUsata)
                attaccoDiColco.append("")
                dati[10] -= costoTecnicaUsata
            # freccia
            if azione == 4 and azioneEseguita:
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    attaccoDiColco.append(nemico)
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
            # tempesta
            if azione == 5 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if abs(rx - x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                i = 0
                while i < len(caseviste):
                    k = 0
                    while k < len(vettoreEsche):
                        if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                            if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                if vettoreEsche[k + 1] <= 0:
                                    vettoreEsche[k + 1] = 0
                                    attaccoDiColco.append("morte")
                                else:
                                    attaccoDiColco.append("")
                            break
                        k += 4
                    i += 3
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str:
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # freccia+
            if azione == 10 and azioneEseguita:
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    attaccoDiColco.append(nemico)
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
            # tempesta+
            if azione == 15 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if abs(rx - x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                i = 0
                while i < len(caseviste):
                    k = 0
                    while k < len(vettoreEsche):
                        if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                            if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                if vettoreEsche[k + 1] <= 0:
                                    vettoreEsche[k + 1] = 0
                                    attaccoDiColco.append("morte")
                                else:
                                    attaccoDiColco.append("")
                            break
                        k += 4
                    i += 3
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str:
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # freccia++
            if azione == 19 and azioneEseguita:
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    attaccoDiColco.append(nemico)
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
            # tempesta++
            if azione == 20 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if abs(rx - x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                i = 0
                while i < len(caseviste):
                    k = 0
                    while k < len(vettoreEsche):
                        if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                            if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                if vettoreEsche[k + 1] <= 0:
                                    vettoreEsche[k + 1] = 0
                                    attaccoDiColco.append("morte")
                                else:
                                    attaccoDiColco.append("")
                            break
                        k += 4
                    i += 3
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str:
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # giro Colco verso l'obiettivo
            if azioneEseguita:
                if abs(nemicoBersaglio.x - rx) > abs(nemicoBersaglio.y - ry):
                    if rx < nemicoBersaglio.x:
                        nrob = 1
                    if rx > nemicoBersaglio.x:
                        nrob = 2
                if abs(nemicoBersaglio.y - ry) > abs(nemicoBersaglio.x - rx):
                    if ry < nemicoBersaglio.y:
                        nrob = 3
                    if ry > nemicoBersaglio.y:
                        nrob = 4
                if (abs(nemicoBersaglio.x - rx) == abs(nemicoBersaglio.y - ry)) and (nemicoBersaglio.x != rx) and (nemicoBersaglio.y != ry):
                    c = random.randint(1, 2)
                    if rx < nemicoBersaglio.x and c == 1:
                        nrob = 1
                    if rx > nemicoBersaglio.x and c == 1:
                        nrob = 2
                    if ry < nemicoBersaglio.y and c == 2:
                        nrob = 3
                    if ry > nemicoBersaglio.y and c == 2:
                        nrob = 4
        elif mostroVisto and not azioneEseguita:
            percorsoTrovato = pathToNemico
            if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry):
                azioneEseguita = True
                if percorsoTrovato[len(percorsoTrovato) - 4] > rx:
                    nrob = 1
                if percorsoTrovato[len(percorsoTrovato) - 4] < rx:
                    nrob = 2
                if percorsoTrovato[len(percorsoTrovato) - 3] > ry:
                    nrob = 3
                if percorsoTrovato[len(percorsoTrovato) - 3] < ry:
                    nrob = 4
                sposta = True
            # else:
                # print ("Percorso Colco verso obiettivo 1 non trovato")

        # effetto assorbilampo
        if dati[130] == 4:
            i = 0
            while i < len(attaccoDiColco):
                if attaccoDiColco[i] == "Rallo" and attaccoDiColco[i + 1] < 0:
                    attaccoDiColco[i + 1] = 0
                i += 3
        # danno a rallo
        i = 0
        while i < len(attaccoDiColco):
            if attaccoDiColco[i] == "Rallo":
                dati[5] += attaccoDiColco[i + 1]
                if dati[5] < 0:
                    dati[5] = 0
            i += 3

        return azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, listaNemici
    else:
        ralloAccanto = False
        ralloVisto = False
        if (rx == x and ry == y) or (rx + GlobalHWVar.gpx == x and ry == y) or (rx - GlobalHWVar.gpx == x and ry == y) or (rx == x and ry + GlobalHWVar.gpy == y) or (rx == x and ry - GlobalHWVar.gpy == y):
            ralloAccanto = True
            ralloVisto = True
        else:
            i = 0
            while i < len(caselleVisteDaColco):
                if caselleVisteDaColco[i] == x and caselleVisteDaColco[i + 1] == y and caselleVisteDaColco[i + 2]:
                    ralloVisto = True
                    break
                i += 3
        if suAlleato == 1:
            if azione == 1 or azione == 2 or azione == 3 or azione == 8 or azione == 9 or azione == 12 or azione == 13 or azione == 16 or azione == 18:
                if ralloAccanto:
                    if dati[10] > costoTecnicaUsata and not (azione == 12 and dati[123] > 0) and not (azione == 13 and dati[124] > 0):
                        azioneEseguita = True
                        attaccoDiColco.append("Colco")
                        attaccoDiColco.append(-costoTecnicaUsata)
                        attaccoDiColco.append("")
                        dati[10] -= costoTecnicaUsata
                    # scossa
                    if azione == 1 and azioneEseguita:
                        dannoEffettivo = GenericFunc.calcoloDanni(GlobalGameVar.dannoTecniche[azione - 1], dif)
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                    # cura
                    if azione == 2 and azioneEseguita:
                        pvGuadagnati = GlobalGameVar.dannoTecniche[azione - 1]
                        if pvGuadagnati + dati[5] > pvtot:
                            pvGuadagnati = pvtot - dati[5]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(pvGuadagnati)
                        attaccoDiColco.append("")
                    # antidoto
                    if azione == 3 and azioneEseguita:
                        dati[121] = False
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(0)
                        attaccoDiColco.append("antidoto")
                    # cura+
                    if azione == 8 and azioneEseguita:
                        pvGuadagnati = GlobalGameVar.dannoTecniche[azione - 1]
                        if pvGuadagnati + dati[5] > pvtot:
                            pvGuadagnati = pvtot - dati[5]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(pvGuadagnati)
                        attaccoDiColco.append("")
                    # scossa+
                    if azione == 9 and azioneEseguita:
                        dannoEffettivo = GenericFunc.calcoloDanni(GlobalGameVar.dannoTecniche[azione - 1], dif)
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                    # attP
                    if azione == 12 and azioneEseguita and dati[123] <= 0:
                        dati[123] = GlobalGameVar.dannoTecniche[azione - 1]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(0)
                        attaccoDiColco.append("attP")
                    # difP
                    if azione == 13 and azioneEseguita and dati[124] <= 0:
                        dati[124] = GlobalGameVar.dannoTecniche[azione - 1]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(0)
                        attaccoDiColco.append("difP")
                    # cura++
                    if azione == 16 and azioneEseguita:
                        pvGuadagnati = GlobalGameVar.dannoTecniche[azione - 1]
                        if pvGuadagnati + dati[5] > pvtot:
                            pvGuadagnati = pvtot - dati[5]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(pvGuadagnati)
                        attaccoDiColco.append("")
                    # scossa++
                    if azione == 18 and azioneEseguita:
                        dannoEffettivo = GenericFunc.calcoloDanni(GlobalGameVar.dannoTecniche[azione - 1], dif)
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                    # giro Colco verso l'obiettivo
                    if azioneEseguita:
                        if abs(x - rx) > abs(y - ry):
                            if rx < x:
                                nrob = 1
                            if rx > x:
                                nrob = 2
                        if abs(y - ry) > abs(x - rx):
                            if ry < y:
                                nrob = 3
                            if ry > y:
                                nrob = 4
                        if (abs(x - rx) == abs(y - ry)) and (x != rx) and (y != ry):
                            c = random.randint(1, 2)
                            if rx < x and c == 1:
                                nrob = 1
                            if rx > x and c == 1:
                                nrob = 2
                            if ry < y and c == 2:
                                nrob = 3
                            if ry > y and c == 2:
                                nrob = 4
            elif ralloVisto:
                if dati[10] > costoTecnicaUsata:
                    azioneEseguita = True
                    attaccoDiColco.append("Colco")
                    attaccoDiColco.append(-costoTecnicaUsata)
                    attaccoDiColco.append("")
                    dati[10] -= costoTecnicaUsata
                # freccia
                if azione == 4 and azioneEseguita:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(GlobalGameVar.dannoTecniche[azione - 1], dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                # tempesta
                if azione == 5 and azioneEseguita:
                    danno = GlobalGameVar.dannoTecniche[azione - 1]
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                    i = 0
                    while i < len(caseviste):
                        k = 0
                        while k < len(vettoreEsche):
                            if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                                if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                    listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                    vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                    attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                    attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                    if vettoreEsche[k + 1] <= 0:
                                        vettoreEsche[k + 1] = 0
                                        attaccoDiColco.append("morte")
                                    else:
                                        attaccoDiColco.append("")
                                break
                            k += 4
                        i += 3
                    for nemico in listaNemici:
                        if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                            listaNemiciAttaccatiADistanzaRobo.append(nemico)
                            nemico.danneggia(danno, "Colco")
                    for nemico in nemiciVistiDaColco:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                    for nemico in listaNemiciAttaccatiADistanzaRobo:
                        if type(nemico) is not str:
                            attaccoDiColco.append(nemico)
                            dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                            attaccoDiColco.append(-dannoEffettivo)
                            attaccoDiColco.append("")
                # freccia+
                if azione == 10 and azioneEseguita:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(GlobalGameVar.dannoTecniche[azione - 1], dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                # tempesta+
                if azione == 15 and azioneEseguita:
                    danno = GlobalGameVar.dannoTecniche[azione - 1]
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                    i = 0
                    while i < len(caseviste):
                        k = 0
                        while k < len(vettoreEsche):
                            if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                                if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                    listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                    vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                    attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                    attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                    if vettoreEsche[k + 1] <= 0:
                                        vettoreEsche[k + 1] = 0
                                        attaccoDiColco.append("morte")
                                    else:
                                        attaccoDiColco.append("")
                                break
                            k += 4
                        i += 3
                    for nemico in listaNemici:
                        if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                            listaNemiciAttaccatiADistanzaRobo.append(nemico)
                            nemico.danneggia(danno, "Colco")
                    for nemico in nemiciVistiDaColco:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                    for nemico in listaNemiciAttaccatiADistanzaRobo:
                        if type(nemico) is not str:
                            attaccoDiColco.append(nemico)
                            dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                            attaccoDiColco.append(-dannoEffettivo)
                            attaccoDiColco.append("")
                # freccia++
                if azione == 19 and azioneEseguita:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(GlobalGameVar.dannoTecniche[azione - 1], dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                # tempesta++
                if azione == 20 and azioneEseguita:
                    danno = GlobalGameVar.dannoTecniche[azione - 1]
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                    i = 0
                    while i < len(caseviste):
                        k = 0
                        while k < len(vettoreEsche):
                            if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                                if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                    listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                    vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                    attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                    attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                    if vettoreEsche[k + 1] <= 0:
                                        vettoreEsche[k + 1] = 0
                                        attaccoDiColco.append("morte")
                                    else:
                                        attaccoDiColco.append("")
                                break
                            k += 4
                        i += 3
                    for nemico in listaNemici:
                        if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                            listaNemiciAttaccatiADistanzaRobo.append(nemico)
                            nemico.danneggia(danno, "Colco")
                    for nemico in nemiciVistiDaColco:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                    for nemico in listaNemiciAttaccatiADistanzaRobo:
                        if type(nemico) is not str:
                            attaccoDiColco.append(nemico)
                            dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                            attaccoDiColco.append(-dannoEffettivo)
                            attaccoDiColco.append("")
                # giro Colco verso l'obiettivo
                if azioneEseguita:
                    if abs(x - rx) > abs(y - ry):
                        if rx < x:
                            nrob = 1
                        if rx > x:
                            nrob = 2
                    if abs(y - ry) > abs(x - rx):
                        if ry < y:
                            nrob = 3
                        if ry > y:
                            nrob = 4
                    if (abs(x - rx) == abs(y - ry)) and (x != rx) and (y != ry):
                        c = random.randint(1, 2)
                        if rx < x and c == 1:
                            nrob = 1
                        if rx > x and c == 1:
                            nrob = 2
                        if ry < y and c == 2:
                            nrob = 3
                        if ry > y and c == 2:
                            nrob = 4
            if not (ralloAccanto and (azione == 1 or azione == 2 or azione == 3 or azione == 8 or azione == 9 or azione == 12 or azione == 13 or azione == 16 or azione == 18)) and not (ralloVisto and (azione == 4 or azione == 5 or azione == 10 or azione == 15 or azione == 19 or azione == 20)):
                if (vx == rx + GlobalHWVar.gpx and vy == ry) or (vx == rx - GlobalHWVar.gpx and vy == ry) or (vx == rx and vy == ry + GlobalHWVar.gpy) or (vx == rx and vy == ry - GlobalHWVar.gpy):
                    azioneEseguita = True
                    if vx == rx + GlobalHWVar.gpx and vy == ry:
                        nrob = 1
                    elif vx == rx - GlobalHWVar.gpx and vy == ry:
                        nrob = 2
                    elif vy == ry + GlobalHWVar.gpy and vx == rx:
                        nrob = 3
                    elif vy == ry - GlobalHWVar.gpy and vx == rx:
                        nrob = 4
                    sposta = True
                else:
                    percorsoTrovato = pathToRallo
                    if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry):
                        azioneEseguita = True
                        if percorsoTrovato[len(percorsoTrovato) - 4] > rx:
                            nrob = 1
                        if percorsoTrovato[len(percorsoTrovato) - 4] < rx:
                            nrob = 2
                        if percorsoTrovato[len(percorsoTrovato) - 3] > ry:
                            nrob = 3
                        if percorsoTrovato[len(percorsoTrovato) - 3] < ry:
                            nrob = 4
                        sposta = True
                    # else:
                        # print ("Percorso Colco verso obiettivo 2 non trovato")
        if suAlleato == 2:
            if dati[10] > costoTecnicaUsata:
                azioneEseguita = True
                attaccoDiColco.append("Colco")
                attaccoDiColco.append(-costoTecnicaUsata)
                attaccoDiColco.append("")
                dati[10] -= costoTecnicaUsata
                if azione != 5 and azione != 15 and azione != 20:
                    attaccoDiColco.append("Colco")
                    attaccoDiColco.append(0)
                    attaccoDiColco.append("")
            # tempesta
            if azione == 5 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if abs(rx - x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                i = 0
                while i < len(caseviste):
                    k = 0
                    while k < len(vettoreEsche):
                        if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                            if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                if vettoreEsche[k + 1] <= 0:
                                    vettoreEsche[k + 1] = 0
                                    attaccoDiColco.append("morte")
                                else:
                                    attaccoDiColco.append("")
                            break
                        k += 4
                    i += 3
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str:
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # tempesta+
            if azione == 15 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if abs(rx - x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                i = 0
                while i < len(caseviste):
                    k = 0
                    while k < len(vettoreEsche):
                        if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                            if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                if vettoreEsche[k + 1] <= 0:
                                    vettoreEsche[k + 1] = 0
                                    attaccoDiColco.append("morte")
                                else:
                                    attaccoDiColco.append("")
                            break
                        k += 4
                    i += 3
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str:
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # tempesa++
            if azione == 20 and azioneEseguita:
                danno = GlobalGameVar.dannoTecniche[azione - 1]
                if abs(rx - x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    dannoEffettivo = GenericFunc.calcoloDanni(danno, dif)
                    attaccoDiColco.append("Rallo")
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                i = 0
                while i < len(caseviste):
                    k = 0
                    while k < len(vettoreEsche):
                        if vettoreEsche[k + 1] > 0 and caseviste[i] == vettoreEsche[k + 2] and caseviste[i + 1] == vettoreEsche[k + 3]:
                            if caseviste[i + 2] and abs(rx - vettoreEsche[k + 2]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - vettoreEsche[k + 3]) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                                listaNemiciAttaccatiADistanzaRobo.append("Esca:" + str(vettoreEsche[k]))
                                vettoreEsche[k + 1] -= GlobalGameVar.dannoTecniche[azione - 1]
                                attaccoDiColco.append("Esca:" + str(vettoreEsche[k]))
                                attaccoDiColco.append(-GlobalGameVar.dannoTecniche[azione - 1])
                                if vettoreEsche[k + 1] <= 0:
                                    vettoreEsche[k + 1] = 0
                                    attaccoDiColco.append("morte")
                                else:
                                    attaccoDiColco.append("")
                            break
                        k += 4
                    i += 3
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and abs(rx - nemico.x) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpx and abs(ry - nemico.y) <= GlobalGameVar.vistaRobo * GlobalHWVar.gpy:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if type(nemico) is not str:
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = GenericFunc.calcoloDanni(danno, nemico.difesa)
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")

        # effetto assorbilampo
        if dati[130] == 4:
            i = 0
            while i < len(attaccoDiColco):
                if attaccoDiColco[i] == "Rallo" and attaccoDiColco[i + 1] < 0:
                    attaccoDiColco[i + 1] = 0
                i += 3
        # danno a rallo
        i = 0
        while i < len(attaccoDiColco):
            if attaccoDiColco[i] == "Rallo":
                dati[5] += attaccoDiColco[i + 1]
                if dati[5] < 0:
                    dati[5] = 0
            i += 3

        return azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, listaNemici


def creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, xNemicoDaEscludere, yNemicoDaEscludere):
    vetNemiciSoloConXeY = []
    # non metto Rallo tra gli ostacoli se ?? nella stessa casella di Colco
    if not (rx == x and ry == y):
        vetNemiciSoloConXeY.append(x)
        vetNemiciSoloConXeY.append(y)
    for nemico in listaNemici:
        if nemico.inCasellaVista and nemico.vita > 0 and not (nemico.x == xNemicoDaEscludere and nemico.y == yNemicoDaEscludere):
            vetNemiciSoloConXeY.append(nemico.x)
            vetNemiciSoloConXeY.append(nemico.y)
    for personaggio in listaPersonaggi:
        vetNemiciSoloConXeY.append(personaggio.x)
        vetNemiciSoloConXeY.append(personaggio.y)
    i = 0
    while i < len(vettoreEsche):
        if vettoreEsche[i + 1] > 0:
            vetNemiciSoloConXeY.append(vettoreEsche[i + 2])
            vetNemiciSoloConXeY.append(vettoreEsche[i + 3])
        i += 4
    return vetNemiciSoloConXeY


def movrobo(x, y, vx, vy, rx, ry, chiamarob, dati, porte, listaNemici, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche, analizzaColco):
    nrx = 0
    nry = 0
    raffreddamento = False
    ricarica1 = False
    ricarica2 = False
    listaNemiciAttaccatiADistanzaRobo = []
    tecnicaUsata = False
    attaccoDiColco = []
    nemiciVistiDaColco = []
    nemiciNonVistiDaColco = []
    ralloVisto = False
    vrx = rx
    vry = ry

    # vettorePrevisione contiene tutte le azioni possibili con il relativo motivo per cui non ?? stato possibile eseguirle
    vettorePrevisione = [["telecolco", ""], [1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [8, ""], [9, ""], [10, ""], ["ultimoObbiettivo", ""]]
    previsionePosizioneObbiettivo = []

    # vetDatiNemici = [vita, x, y, vitaTot, stato]
    nrob = 0
    sposta = False
    # movimento robot
    if chiamarob:
        if dati[10] <= 0:
            i = 0
            while i < len(vettorePrevisione):
                vettorePrevisione[i][1] = LI.ENERGIA_INSUFFICIENTE[GlobalHWVar.linguaImpostata]
                i += 1
        else:
            previsionePosizioneObbiettivo.append([x, y])
        azioneEseguita = False
        if (vx == rx + GlobalHWVar.gpx and vy == ry) or (vx == rx - GlobalHWVar.gpx and vy == ry) or (vx == rx and vy == ry + GlobalHWVar.gpy) or (vx == rx and vy == ry - GlobalHWVar.gpy):
            if not (x == vx and y == vy):
                if vx == rx + GlobalHWVar.gpx and vy == ry:
                    nrob = 1
                elif vx == rx - GlobalHWVar.gpx and vy == ry:
                    nrob = 2
                elif vy == ry + GlobalHWVar.gpy and vx == rx:
                    nrob = 3
                elif vy == ry - GlobalHWVar.gpy and vx == rx:
                    nrob = 4
                sposta = True
                azioneEseguita = True
        elif not (vx == rx and vy == ry):
            vetNemiciSoloConXeY = []
            for nemico in listaNemici:
                if nemico.inCasellaVista and nemico.vita > 0:
                    vetNemiciSoloConXeY.append(nemico.x)
                    vetNemiciSoloConXeY.append(nemico.y)
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            i = 0
            while i < len(vettoreEsche):
                if vettoreEsche[i + 1] > 0:
                    vetNemiciSoloConXeY.append(vettoreEsche[i + 2])
                    vetNemiciSoloConXeY.append(vettoreEsche[i + 3])
                i += 4
            percorsoTrovato = GenericFunc.pathFinding(rx, ry, x, y, vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry):
                azioneEseguita = True
                if percorsoTrovato[len(percorsoTrovato) - 4] > rx:
                    nrob = 1
                if percorsoTrovato[len(percorsoTrovato) - 4] < rx:
                    nrob = 2
                if percorsoTrovato[len(percorsoTrovato) - 3] > ry:
                    nrob = 3
                if percorsoTrovato[len(percorsoTrovato) - 3] < ry:
                    nrob = 4
                sposta = True
            # else:
                # print ("Percorso Colco verso ImpoPietra non trovato")
        if azioneEseguita and sposta:
            tecnicaUsata = "spostamento"
            ultimoObbiettivoColco = ["Telecomando", x, y, "spostamento"]
        else:
            ultimoObbiettivoColco = []
    else:
        vettorePrevisione[0][1] = LI.IMPOPIETRA_SPENTA[GlobalHWVar.linguaImpostata]
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, difesa)

        if GlobalGameVar.impoPresente and (posizioneColcoAggiornamentoCaseAttac[0] != rx or posizioneColcoAggiornamentoCaseAttac[1] != ry):
            caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
            posizioneColcoAggiornamentoCaseAttac = [rx, ry]
        # trovo il path verso Rallo
        vetNemiciSoloConXeY = []
        for nemico in listaNemici:
            if nemico.inCasellaVista and nemico.vita > 0:
                vetNemiciSoloConXeY.append(nemico.x)
                vetNemiciSoloConXeY.append(nemico.y)
        for personaggio in listaPersonaggi:
            vetNemiciSoloConXeY.append(personaggio.x)
            vetNemiciSoloConXeY.append(personaggio.y)
        i = 0
        while i < len(vettoreEsche):
            if vettoreEsche[i + 1] > 0:
                vetNemiciSoloConXeY.append(vettoreEsche[i + 2])
                vetNemiciSoloConXeY.append(vettoreEsche[i + 3])
            i += 4
        pathToRallo = GenericFunc.pathFinding(rx, ry, x, y, vetNemiciSoloConXeY, caseviste)
        # trovo i nemici/Rallo visti
        if rx == x and ry == y:
            ralloVisto = True
        k = 0
        while k < len(caselleAttaccabiliColco):
            if caselleAttaccabiliColco[k + 2]:
                if caselleAttaccabiliColco[k] == x and caselleAttaccabiliColco[k + 1] == y:
                    ralloVisto = True
                for nemico in listaNemici:
                    if caselleAttaccabiliColco[k] == nemico.x and caselleAttaccabiliColco[k + 1] == nemico.y and nemico.vita > 0:
                        nemiciVistiDaColco.append(nemico)
                        break
            k += 3
        # trovo i nemici non visti
        for nemico in listaNemici:
            if nemico.vita > 0 and not nemico in nemiciVistiDaColco:
                nemiciNonVistiDaColco.append(nemico)

        # dati: tecniche(11-30) / condizioni(81-100) / gambit(101-120) / pvRallo(5) / veleno(121) / attP(123) / difP(124) / peColco(10) / surriscalda(122) / velP(125) / efficienza(126)
        # in gambit: prime 10 -> condizioni, ultime 10 -> tecniche
        # condizioni = intero da 1 a 20: pvR<80, pvR<50, pvR<30, velenoR, surrisC, peC<80, peC<50, peC<30, sempreR, sempreC, nemicoCasuale, nemicoVicino, nemicoLontano, pvN<80, pvN<50, pvN<30, nemico-pv, numN>1, numN>4, numN>7
        # tecniche = intero da 1 a 20: scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesta++

        # controllo se la condizione ?? rispettata
        azioneEseguita = False
        i = 101
        while i <= 110 and not azioneEseguita:
            if dati[126] > 0:
                costoTecnicaUsata = GlobalGameVar.costoTecniche[dati[i + 10] - 1] // 2
            else:
                costoTecnicaUsata = GlobalGameVar.costoTecniche[dati[i + 10] - 1]
            rigaGambitAttuale = i - 100
            if dati[i] <= 0 or dati[i + 10] <= 0:
                vettorePrevisione[rigaGambitAttuale][1] = LI.CEL_DI_MEM_INC[GlobalHWVar.linguaImpostata]
            elif dati[10] > costoTecnicaUsata:
                if not (dati[122] > 0 and (dati[i + 10] == 11 or dati[i + 10] == 14)):
                    pathToNemico = []
                    # tecnicaRavvicinata ?? True quando la tecnica pu?? essere usata solo accanto al bersaglio, altrimenti ?? False
                    if dati[i + 10] == 1 or dati[i + 10] == 2 or dati[i + 10] == 3 or dati[i + 10] == 8 or dati[i + 10] == 9 or dati[i + 10] == 12 or dati[i + 10] == 13 or dati[i + 10] == 16 or dati[i + 10] == 18:
                        tecnicaRavvicinata = True
                    else:
                        tecnicaRavvicinata = False
                    if dati[i + 10] == 5 or dati[i + 10] == 15 or dati[i + 10] == 20:
                        tecnicaABersaglioSingolo = False
                    else:
                        tecnicaABersaglioSingolo = True

                    # azioni su alleati
                    # pv rallo < 80
                    if dati[i] == 1:
                        if dati[5] < pvtot / float(100) * 80 and ((not tecnicaRavvicinata and ralloVisto) or (tecnicaRavvicinata and ralloVisto and pathToRallo)):
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Rallo", x, y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        elif not dati[5] < pvtot / float(100) * 80:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                        elif not ralloVisto:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.POS_OBI_SCO[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                    # pv rallo < 50
                    if dati[i] == 2:
                        if dati[5] < pvtot / float(100) * 50 and ((not tecnicaRavvicinata and ralloVisto) or (tecnicaRavvicinata and ralloVisto and pathToRallo)):
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Rallo", x, y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        elif not dati[5] < pvtot / float(100) * 50:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                        elif not ralloVisto:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.POS_OBI_SCO[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                    # pv rallo < 30
                    if dati[i] == 3:
                        if dati[5] < pvtot / float(100) * 30 and ((not tecnicaRavvicinata and ralloVisto) or (tecnicaRavvicinata and ralloVisto and pathToRallo)):
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Rallo", x, y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        elif not dati[5] < pvtot / float(100) * 30:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                        elif not ralloVisto:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.POS_OBI_SCO[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                    # rallo avvelenato
                    if dati[i] == 4:
                        if dati[121] and ((not tecnicaRavvicinata and ralloVisto) or (tecnicaRavvicinata and ralloVisto and pathToRallo)):
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Rallo", x, y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        elif not dati[121]:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                        elif not ralloVisto:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.POS_OBI_SCO[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                    # colco surriscaldato
                    if dati[i] == 5:
                        if dati[122] > 0:
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Colco", rx, ry, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # pe colco < 80
                    if dati[i] == 6:
                        if dati[10] < entot / float(100) * 80:
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Colco", rx, ry, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # pe colco < 50
                    if dati[i] == 7:
                        if dati[10] < entot / float(100) * 50:
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Colco", rx, ry, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # pe colco < 30
                    if dati[i] == 8:
                        if dati[10] < entot / float(100) * 30:
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Colco", rx, ry, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # sempre rallo
                    if dati[i] == 9:
                        if not (dati[i + 10] == 12 and dati[123] > 0) and not (dati[i + 10] == 13 and dati[124] > 0) and ((not tecnicaRavvicinata and ralloVisto) or (tecnicaRavvicinata and ralloVisto and pathToRallo)):
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Rallo", x, y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        elif (dati[i + 10] == 12 and dati[123] > 0) or (dati[i + 10] == 13 and dati[124] > 0):
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                        elif not ralloVisto:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.POS_OBI_SCO[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                    # sempre colco
                    if dati[i] == 10:
                        if not (dati[i + 10] == 11 and dati[125] > 0) and not (dati[i + 10] == 14 and dati[126] > 0):
                            azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            if azioneEseguita:
                                ultimoObbiettivoColco = ["Colco", rx, ry, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]

                    # azioni su nemici
                    nemicoBersaglio = False
                    # nemico a caso
                    if dati[i] == 11:
                        obiettivoGiaConosciuto = False
                        pathToNemico = []
                        if obbiettivoCasualeColco and obbiettivoCasualeColco in nemiciVistiDaColco:
                            if tecnicaRavvicinata:
                                vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, obbiettivoCasualeColco.x, obbiettivoCasualeColco.y)
                                pathToNemico = GenericFunc.pathFinding(rx, ry, obbiettivoCasualeColco.x, obbiettivoCasualeColco.y, vetNemiciSoloConXeY, caseviste)
                                if pathToNemico and len(pathToNemico) > 0:
                                    obiettivoGiaConosciuto = True
                                    nemicoBersaglio = obbiettivoCasualeColco
                                    vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemicoBersaglio.x, nemicoBersaglio.y)
                                    pathToNemico = GenericFunc.pathFinding(rx, ry, nemicoBersaglio.x, nemicoBersaglio.y, vetNemiciSoloConXeY, caseviste)
                            else:
                                obiettivoGiaConosciuto = True
                                nemicoBersaglio = obbiettivoCasualeColco
                                vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemicoBersaglio.x, nemicoBersaglio.y)
                                pathToNemico = GenericFunc.pathFinding(rx, ry, nemicoBersaglio.x, nemicoBersaglio.y, vetNemiciSoloConXeY, caseviste)
                        if not nemicoBersaglio and len(nemiciVistiDaColco) > 0:
                            # non uso il deepcopy perch?? mi serve che gli oggetti siano gli stessi
                            listaNemiciProvvisoria = nemiciVistiDaColco[:]
                            trovatoNemicoCasuale = False
                            while len(listaNemiciProvvisoria) > 0 and not trovatoNemicoCasuale:
                                numeroNemico = random.randint(0, (len(listaNemiciProvvisoria) - 1))
                                nemicoBersaglio = listaNemiciProvvisoria[numeroNemico]
                                del listaNemiciProvvisoria[numeroNemico]
                                if tecnicaRavvicinata:
                                    vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemicoBersaglio.x, nemicoBersaglio.y)
                                    pathToNemico = GenericFunc.pathFinding(rx, ry, nemicoBersaglio.x, nemicoBersaglio.y, vetNemiciSoloConXeY, caseviste)
                                if pathToNemico or not tecnicaRavvicinata:
                                    trovatoNemicoCasuale = True
                            if not trovatoNemicoCasuale:
                                nemicoBersaglio = False
                            obbiettivoCasualeColco = nemicoBersaglio
                        if not nemicoBersaglio:
                            obbiettivoCasualeColco = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                if obiettivoGiaConosciuto:
                                    previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                                else:
                                    for nemico in nemiciVistiDaColco:
                                        previsionePosizioneObbiettivo.append([nemico.x, nemico.y])
                            else:
                                ultimoObbiettivoColco = []
                            if len(attaccoDiColco) > 0 and not analizzaColco:
                                obbiettivoCasualeColco = False
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # nemico vicino
                    if dati[i] == 12:
                        for nemico in nemiciVistiDaColco:
                            if (abs(nemico.x - rx) == GlobalHWVar.gpx and abs(nemico.y - ry) == 0) or (abs(nemico.x - rx) == 0 and abs(nemico.y - ry) == GlobalHWVar.gpy):
                                nemicoBersaglio = nemico
                                break
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                            else:
                                ultimoObbiettivoColco = []
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # nemico lontano
                    if dati[i] == 13:
                        distMin = False
                        distanzaDaNemico = -1
                        pathToNemico = []
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if not ((abs(nemico.x - rx) == GlobalHWVar.gpx and abs(nemico.y - ry) == 0) or (abs(nemico.x - rx) == 0 and abs(nemico.y - ry) == GlobalHWVar.gpy)):
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                        if tecnicaRavvicinata and not pathToNemico:
                            nemicoBersaglio = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                            else:
                                ultimoObbiettivoColco = []
                        else:
                            if distMin and tecnicaRavvicinata and (not pathToNemico or len(pathToNemico) == 0):
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # nemico pv < 80
                    if dati[i] == 14:
                        distMin = False
                        distanzaDaNemico = -1
                        pathToNemico = []
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if nemico.vita < nemico.vitaTotale / float(100) * 80:
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                        if tecnicaRavvicinata and not pathToNemico:
                            nemicoBersaglio = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                            else:
                                ultimoObbiettivoColco = []
                        else:
                            if distMin and tecnicaRavvicinata and (not pathToNemico or len(pathToNemico) == 0):
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # nemico pv < 50
                    if dati[i] == 15:
                        distMin = False
                        distanzaDaNemico = -1
                        pathToNemico = []
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if nemico.vita < nemico.vitaTotale / float(100) * 50:
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                        if tecnicaRavvicinata and not pathToNemico:
                            nemicoBersaglio = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                            else:
                                ultimoObbiettivoColco = []
                        else:
                            if distMin and tecnicaRavvicinata and (not pathToNemico or len(pathToNemico) == 0):
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # nemico pv < 30
                    if dati[i] == 16:
                        distMin = False
                        distanzaDaNemico = -1
                        pathToNemico = []
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if nemico.vita < nemico.vitaTotale / float(100) * 30:
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                        if tecnicaRavvicinata and not pathToNemico:
                            nemicoBersaglio = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                            else:
                                ultimoObbiettivoColco = []
                        else:
                            if distMin and tecnicaRavvicinata and (not pathToNemico or len(pathToNemico) == 0):
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # nemico con meno pv
                    if dati[i] == 17:
                        distMin = False
                        distanzaDaNemico = -1
                        pathToNemico = []
                        pvMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if primoMostro:
                                if tecnicaRavvicinata:
                                    vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                    pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if pathToNemico and len(pathToNemico) > 0:
                                        distanzaDaNemico = len(pathToNemico) / 2
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                pvMin = nemico.vita
                                nemicoBersaglio = nemico
                                primoMostro = False
                            elif pvMin and nemico.vita <= pvMin:
                                pathToNemicoTemp = False
                                if tecnicaRavvicinata:
                                    vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                    pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                if nemico.vita < pvMin or (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and (nemico.vita == pvMin and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin)):
                                    if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                        pathToNemico = pathToNemicoTemp
                                        distanzaDaNemico = len(pathToNemico) / 2
                                    else:
                                        pathToNemico = False
                                        distanzaDaNemico = -1
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    pvMin = nemico.vita
                                    nemicoBersaglio = nemico
                        if tecnicaRavvicinata and not pathToNemico:
                            nemicoBersaglio = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            if nemicoBersaglio.vita > 0 or analizzaColco:
                                ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                            else:
                                ultimoObbiettivoColco = []
                        else:
                            if distMin and tecnicaRavvicinata and (not pathToNemico or len(pathToNemico) == 0):
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # numero nemici > 1
                    if dati[i] == 18:
                        if len(nemiciVistiDaColco) > 1:
                            distMin = False
                            distanzaDaNemico = -1
                            pathToNemico = []
                            primoMostro = True
                            for nemico in nemiciVistiDaColco:
                                if not tecnicaABersaglioSingolo:
                                    previsionePosizioneObbiettivo.append([nemico.x, nemico.y])
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                            if tecnicaRavvicinata and not pathToNemico:
                                nemicoBersaglio = False
                            if nemicoBersaglio:
                                if tecnicaABersaglioSingolo:
                                    previsionePosizioneObbiettivo.append([nemicoBersaglio.x, nemicoBersaglio.y])
                                nemiciVistiDaColco.remove(nemicoBersaglio)
                                azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                                nemiciVistiDaColco.append(nemicoBersaglio)
                                if nemicoBersaglio.vita > 0 or analizzaColco:
                                    ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                else:
                                    ultimoObbiettivoColco = []
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # numero nemici > 2
                    if dati[i] == 19:
                        if len(nemiciVistiDaColco) > 2:
                            distMin = False
                            distanzaDaNemico = -1
                            pathToNemico = []
                            primoMostro = True
                            for nemico in nemiciVistiDaColco:
                                if not tecnicaABersaglioSingolo:
                                    previsionePosizioneObbiettivo.append([nemico.x, nemico.y])
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                            if tecnicaRavvicinata and not pathToNemico:
                                nemicoBersaglio = False
                            if nemicoBersaglio:
                                if tecnicaABersaglioSingolo:
                                    previsionePosizioneObbiettivo.append([nemicoBersaglio.x, nemicoBersaglio.y])
                                nemiciVistiDaColco.remove(nemicoBersaglio)
                                azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                                nemiciVistiDaColco.append(nemicoBersaglio)
                                if nemicoBersaglio.vita > 0 or analizzaColco:
                                    ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                else:
                                    ultimoObbiettivoColco = []
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]
                    # numero nemici > 3
                    if dati[i] == 20:
                        if len(nemiciVistiDaColco) > 3:
                            distMin = False
                            distanzaDaNemico = -1
                            pathToNemico = []
                            primoMostro = True
                            for nemico in nemiciVistiDaColco:
                                if not tecnicaABersaglioSingolo:
                                    previsionePosizioneObbiettivo.append([nemico.x, nemico.y])
                                if primoMostro:
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemico = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                        if pathToNemico and len(pathToNemico) > 0:
                                            distanzaDaNemico = len(pathToNemico) / 2
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                else:
                                    pathToNemicoTemp = False
                                    if tecnicaRavvicinata:
                                        vetNemiciSoloConXeY = creaVetOstacoliPerColco(x, y, rx, ry, listaNemici, listaPersonaggi, vettoreEsche, nemico.x, nemico.y)
                                        pathToNemicoTemp = GenericFunc.pathFinding(rx, ry, nemico.x, nemico.y, vetNemiciSoloConXeY, caseviste)
                                    if (tecnicaRavvicinata and pathToNemicoTemp and (len(pathToNemicoTemp) / 2 < distanzaDaNemico or distanzaDaNemico == -1)) or (((tecnicaRavvicinata and not pathToNemicoTemp and distanzaDaNemico == -1) or not tecnicaRavvicinata) and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                        if pathToNemicoTemp and len(pathToNemicoTemp) > 0:
                                            pathToNemico = pathToNemicoTemp
                                            distanzaDaNemico = len(pathToNemico) / 2
                                        distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                        nemicoBersaglio = nemico
                            if tecnicaRavvicinata and not pathToNemico:
                                nemicoBersaglio = False
                            if nemicoBersaglio:
                                if tecnicaABersaglioSingolo:
                                    previsionePosizioneObbiettivo.append([nemicoBersaglio.x, nemicoBersaglio.y])
                                nemiciVistiDaColco.remove(nemicoBersaglio)
                                azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabiliColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, vettoreEsche, nemiciNonVistiDaColco, caseviste, pathToRallo, pathToNemico)
                                nemiciVistiDaColco.append(nemicoBersaglio)
                                if nemicoBersaglio.vita > 0 or analizzaColco:
                                    ultimoObbiettivoColco = ["Nemico-" + str(nemicoBersaglio.id), nemicoBersaglio.x, nemicoBersaglio.y, str(dati[i + 10])]
                                else:
                                    ultimoObbiettivoColco = []
                            else:
                                vettorePrevisione[rigaGambitAttuale][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
                        else:
                            vettorePrevisione[rigaGambitAttuale][1] = LI.CON_NON_RIS[GlobalHWVar.linguaImpostata]

                    # nel caso in cui viene fatta un'azione e non c'?? un target specifico resetto ultimoObbiettivoColco
                    if azioneEseguita and dati[i] >= 11 and not nemicoBersaglio:
                        ultimoObbiettivoColco = []

                    # tecniche = scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesta++
                    if azioneEseguita and sposta:
                        tecnicaUsata = "spostamento"
                    elif azioneEseguita:
                        if dati[i + 10] == 1:
                            tecnicaUsata = "scossa"
                        if dati[i + 10] == 2:
                            tecnicaUsata = "cura"
                        if dati[i + 10] == 3:
                            tecnicaUsata = "antidoto"
                        if dati[i + 10] == 4:
                            tecnicaUsata = "freccia"
                        if dati[i + 10] == 5:
                            tecnicaUsata = "tempesta"
                        if dati[i + 10] == 6:
                            tecnicaUsata = "raffred"
                        if dati[i + 10] == 7:
                            tecnicaUsata = "ricarica"
                        if dati[i + 10] == 8:
                            tecnicaUsata = "cura+"
                        if dati[i + 10] == 9:
                            tecnicaUsata = "scossa+"
                        if dati[i + 10] == 10:
                            tecnicaUsata = "freccia+"
                        if dati[i + 10] == 11:
                            tecnicaUsata = "velocizza"
                        if dati[i + 10] == 12:
                            tecnicaUsata = "attP"
                        if dati[i + 10] == 13:
                            tecnicaUsata = "difP"
                        if dati[i + 10] == 14:
                            tecnicaUsata = "efficienza"
                        if dati[i + 10] == 15:
                            tecnicaUsata = "tempesta+"
                        if dati[i + 10] == 16:
                            tecnicaUsata = "cura++"
                        if dati[i + 10] == 17:
                            tecnicaUsata = "ricarica+"
                        if dati[i + 10] == 18:
                            tecnicaUsata = "scossa++"
                        if dati[i + 10] == 19:
                            tecnicaUsata = "freccia++"
                        if dati[i + 10] == 20:
                            tecnicaUsata = "tempesta++"
                else:
                    vettorePrevisione[rigaGambitAttuale][1] = LI.AZI_IMP_CON_SUR[GlobalHWVar.linguaImpostata]
            else:
                vettorePrevisione[rigaGambitAttuale][1] = LI.ENERGIA_INSUFFICIENTE[GlobalHWVar.linguaImpostata]

            i += 1

        # prima di andare all'ultimoObbiettivoColco controllo se Colco ha abbastanza energia per fare l'azione che deve fare quando raggiunge ultimoObbiettivoColco
        if not azioneEseguita and len(ultimoObbiettivoColco) > 0 and ultimoObbiettivoColco[3] != "spostamento":
            if dati[126] > 0:
                costoTecnicaUsata = GlobalGameVar.costoTecniche[int(ultimoObbiettivoColco[3]) - 1] // 2
            else:
                costoTecnicaUsata = GlobalGameVar.costoTecniche[int(ultimoObbiettivoColco[3]) - 1]
            if not dati[10] > costoTecnicaUsata:
                ultimoObbiettivoColco = []
        if not azioneEseguita and len(ultimoObbiettivoColco) > 0:
            vetNemiciSoloConXeY = []
            if ultimoObbiettivoColco[0] == "Telecomando" or ultimoObbiettivoColco[0] == "Rallo":
                if not (ultimoObbiettivoColco[1] == x and ultimoObbiettivoColco[2] == y):
                    vetNemiciSoloConXeY.append(x)
                    vetNemiciSoloConXeY.append(y)
            else:
                vetNemiciSoloConXeY.append(x)
                vetNemiciSoloConXeY.append(y)
            for nemico in listaNemici:
                if nemico.inCasellaVista and nemico.vita > 0 and not (ultimoObbiettivoColco[1] == nemico.x and ultimoObbiettivoColco[2] == nemico.y):
                    vetNemiciSoloConXeY.append(nemico.x)
                    vetNemiciSoloConXeY.append(nemico.y)
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            i = 0
            while i < len(vettoreEsche):
                if vettoreEsche[i + 1] > 0:
                    vetNemiciSoloConXeY.append(vettoreEsche[i + 2])
                    vetNemiciSoloConXeY.append(vettoreEsche[i + 3])
                i += 4

            if (abs(rx - ultimoObbiettivoColco[1]) == GlobalHWVar.gpx and abs(ry - ultimoObbiettivoColco[2]) == 0) or (abs(rx - ultimoObbiettivoColco[1]) == 0 and abs(ry - ultimoObbiettivoColco[2]) == GlobalHWVar.gpy):
                posizioneOstacolata = False
                if ultimoObbiettivoColco[1] == x and ultimoObbiettivoColco[2] == y:
                    posizioneOstacolata = True
                for nemico in listaNemici:
                    if nemico.inCasellaVista and nemico.vita > 0 and ultimoObbiettivoColco[1] == nemico.x and ultimoObbiettivoColco[2] == nemico.y:
                        posizioneOstacolata = True
                        break
                for personaggio in listaPersonaggi:
                    if ultimoObbiettivoColco[1] == personaggio.x and ultimoObbiettivoColco[2] == personaggio.y:
                        posizioneOstacolata = True
                        break
                # per evitare di non mostrare l'intento di Colco nella schermata di previsione (altrimenti l'obiettivo verrebbe mostrato sempre tranne quando gli ?? accanto)
                if analizzaColco:
                    posizioneOstacolata = False
                i = 0
                while i < len(porte):
                    if ultimoObbiettivoColco[1] == porte[i + 1] and ultimoObbiettivoColco[2] == porte[i + 2]:
                        if not porte[i + 3]:
                            posizioneOstacolata = True
                        break
                    i += 4
                if not posizioneOstacolata:
                    if rx + GlobalHWVar.gpx == ultimoObbiettivoColco[1] and ry == ultimoObbiettivoColco[2]:
                        nrob = 1
                    if rx - GlobalHWVar.gpx == ultimoObbiettivoColco[1] and ry == ultimoObbiettivoColco[2]:
                        nrob = 2
                    if rx == ultimoObbiettivoColco[1] and ry + GlobalHWVar.gpy == ultimoObbiettivoColco[2]:
                        nrob = 3
                    if rx == ultimoObbiettivoColco[1] and ry - GlobalHWVar.gpy == ultimoObbiettivoColco[2]:
                        nrob = 4
                    sposta = True
                    azioneEseguita = True
            elif not (ultimoObbiettivoColco[1] == rx and ultimoObbiettivoColco[2] == ry):
                percorsoTrovato = GenericFunc.pathFinding(rx, ry, ultimoObbiettivoColco[1], ultimoObbiettivoColco[2], vetNemiciSoloConXeY, caseviste)
                if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry):
                    azioneEseguita = True
                    if percorsoTrovato[len(percorsoTrovato) - 4] > rx:
                        nrob = 1
                    if percorsoTrovato[len(percorsoTrovato) - 4] < rx:
                        nrob = 2
                    if percorsoTrovato[len(percorsoTrovato) - 3] > ry:
                        nrob = 3
                    if percorsoTrovato[len(percorsoTrovato) - 3] < ry:
                        nrob = 4
                    sposta = True
                # else:
                #     print ("Percorso Colco verso ultimo obiettivo non trovato")
            else:
                ultimoObbiettivoColco = []
            if azioneEseguita and sposta:
                if dati[10] <= 0:
                    vettorePrevisione[11][1] = LI.ENERGIA_INSUFFICIENTE[GlobalHWVar.linguaImpostata]
                else:
                    previsionePosizioneObbiettivo.append([ultimoObbiettivoColco[1], ultimoObbiettivoColco[2]])
                tecnicaUsata = "spostamento"
            else:
                if dati[10] <= 0:
                    vettorePrevisione[11][1] = LI.ENERGIA_INSUFFICIENTE[GlobalHWVar.linguaImpostata]
                else:
                    vettorePrevisione[11][1] = LI.OBIETTIVO_IRRAGGIUNGIBILE[GlobalHWVar.linguaImpostata]
        elif not azioneEseguita:
            if dati[10] <= 0:
                vettorePrevisione[11][1] = LI.ENERGIA_INSUFFICIENTE[GlobalHWVar.linguaImpostata]
            else:
                vettorePrevisione[11][1] = LI.NES_OBI_IN_MEM[GlobalHWVar.linguaImpostata]

    # cancello ultimoObbiettivoColco se ho appena compiuto la tecnica (altrimenti andrebbe sopra la casella dell'ultimoObbiettivoColco inutilmente)
    if tecnicaUsata and tecnicaUsata != "spostamento":
        ultimoObbiettivoColco = []

    if len(listaNemiciAttaccatiADistanzaRobo) == 0:
        listaNemiciAttaccatiADistanzaRobo = False

    # spostamento
    if sposta:
        if nrob == 1:
            if rx + GlobalHWVar.gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = GlobalHWVar.gpx
                nry = 0
        if nrob == 2:
            if rx - GlobalHWVar.gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = -GlobalHWVar.gpx
                nry = 0
        if nrob == 3:
            if rx == x and ry + GlobalHWVar.gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = GlobalHWVar.gpy
        if nrob == 4:
            if rx == x and ry - GlobalHWVar.gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = -GlobalHWVar.gpy
    if len(ultimoObbiettivoColco) > 0 and rx + nrx == ultimoObbiettivoColco[1] and ry + nry == ultimoObbiettivoColco[2]:
        ultimoObbiettivoColco = []

    i = 0
    while i < len(caseviste):
        if caseviste[i] == rx + nrx and caseviste[i + 1] == ry + nry:
            if caseviste[i + 2]:
                rx += nrx
                ry += nry
            break
        i += 3

    # aggiorno l'obiettivo se sta cercando Rallo (potrebbe vederlo prima che si muova di nuovo nel prossimo turno)
    if len(ultimoObbiettivoColco) > 0 and ultimoObbiettivoColco[0] == "Rallo" and not ralloVisto and not (rx == vrx and ry == vry):
        tecnicaDaUsareSuRallo = ultimoObbiettivoColco[3]
        # non segno caselleAttaccabiliColco come aggiornato perch?? si devono ancora muovere i nemici
        caselleAttaccabiliColco = GenericFunc.trovacasattaccabili(rx, ry, GlobalGameVar.vistaRobo * GlobalHWVar.gpx, caseviste)
        k = 0
        while k < len(caselleAttaccabiliColco):
            if caselleAttaccabiliColco[k + 2]:
                if caselleAttaccabiliColco[k] == x and caselleAttaccabiliColco[k + 1] == y:
                    ultimoObbiettivoColco = ["Rallo", x, y, tecnicaDaUsareSuRallo]
            k += 3

    if analizzaColco:
        return vettorePrevisione, previsionePosizioneObbiettivo
    else:
        return rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco, caselleAttaccabiliColco, posizioneColcoAggiornamentoCaseAttac, vettoreEsche
