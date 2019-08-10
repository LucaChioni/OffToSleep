# -*- coding: utf-8 -*-

import random
from GenericFuncG2 import *


def movmostro(x, y, rx, ry, mx, my, stanza, tipo, muovimost, visto, dif, difro, par, dati, statom, vitaesca, porte, cofanetti, vetNemici):
    sposta = False
    mostro = True
    attrobo = False
    nmos = 0
    nmx = 0
    nmy = 0
    vistoesca = False
    escabersaglio = 0

    # burocrazia
    carim = False

    if visto:
        visto = False

    # caratteristiche nemici
    if tipo == "mostro":
        attlontano = True
        vistam = gpx * 5
        att = 10
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = -2
            else:
                muovimost = 0
    if tipo == "pipistrello":
        attlontano = False
        vistam = gpx * 6
        att = 5
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = 0
            else:
                muovimost = 2
    if tipo == "orco":
        attlontano = False
        vistam = gpx * 5
        att = 15
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = -3
            else:
                muovimost = -2
    if tipo == 0:
        attlontano = False
        vistam = 0
        att = 0

    # movimenti verso esche o casuali
    primaesca = True
    i = 0
    while i < len(vitaesca):
        if abs(vitaesca[i + 2] - mx) <= vistam and abs(vitaesca[i + 3] - my) <= vistam:
            if primaesca:
                distminx = vitaesca[i + 2]
                distminy = vitaesca[i + 3]
                escabersaglio = i
                vistoesca = True
                primaesca = False
            if not primaesca and (abs(vitaesca[i + 2] - mx) + abs(vitaesca[i + 3] - my) < abs(distminx - mx) + abs(distminy - my)):
                distminx = vitaesca[i + 2]
                distminy = vitaesca[i + 3]
                escabersaglio = i
            # controllo caselle che si vedono
            caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == distminx and caseattactot[j + 1] == distminy and not caseattactot[j + 2]:
                    distminx = 0
                    distminy = 0
                    escabersaglio = 0
                    vistoesca = False
                    primaesca = True
                j = j + 3
        i = i + 4
    vistoprov1 = False
    vistoprov2 = False
    if not visto and not vistoesca:
        # controllo caselle che si vedono (per controllare se vedono pers o robo)
        caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
        if abs(x - mx) <= vistam and abs(y - my) <= vistam and dati[5] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == x and caseattactot[j + 1] == y:
                    if not caseattactot[j + 2]:
                        vistoprov1 = False
                    else:
                        vistoprov1 = True
                    break
                j = j + 3
        if abs(rx - mx) <= vistam and abs(ry - my) <= vistam and dati[10] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == rx and caseattactot[j + 1] == ry:
                    if not caseattactot[j + 2]:
                        vistoprov2 = False
                    else:
                        vistoprov2 = True
                    break
                j = j + 3
            if dati[10] <= 0:
                vistoprov2 = False
        if vistoprov1 or vistoprov2:
            visto = True
        if not visto:
            nmos = random.randint(1, 4)
            sposta = True

    if (visto or vistoesca) and muovimost >= -1:
        if ((abs(rx - mx) + abs(ry - my)) < (abs(x - mx) + abs(y - my)) or not vistoprov1) and vistoprov2 and dati[10] > 0 and not vistoesca:
            x = rx
            y = ry
            attrobo = True
        if vistoesca:
            x = vitaesca[escabersaglio + 2]
            y = vitaesca[escabersaglio + 3]

        # nemici che attaccano da vicino
        if not attlontano:
            vetNemiciSoloConXeY = []
            i = 0
            while i < len(vetNemici):
                if not (vetNemici[i + 1] == mx and vetNemici[i + 2] == my):
                    vetNemiciSoloConXeY.append(vetNemici[i + 1])
                    vetNemiciSoloConXeY.append(vetNemici[i + 2])
                i += 4
            if not (x == rx and y == ry):
                vetNemiciSoloConXeY.append(rx)
                vetNemiciSoloConXeY.append(ry)
            print vetNemiciSoloConXeY
            percorsoTrovato = pathFinding(mx, my, x, y, stanza, porte, cofanetti, vetNemiciSoloConXeY)
            if percorsoTrovato:
                if len(percorsoTrovato) >= 4:
                    if percorsoTrovato[len(percorsoTrovato) - 4] != mx or percorsoTrovato[len(percorsoTrovato) - 3] != my:
                        if percorsoTrovato[len(percorsoTrovato) - 4] > mx:
                            nmos = 1
                        if percorsoTrovato[len(percorsoTrovato) - 4] < mx:
                            nmos = 2
                        if percorsoTrovato[len(percorsoTrovato) - 3] > my:
                            nmos = 3
                        if percorsoTrovato[len(percorsoTrovato) - 3] < my:
                            nmos = 4
                        sposta = True
            else:
                if abs(x - mx) > abs(y - my):
                    if mx < x:
                        nmos = 1
                    if mx > x:
                        nmos = 2
                    sposta = True
                if abs(y - my) > abs(x - mx):
                    if my < y:
                        nmos = 3
                    if my > y:
                        nmos = 4
                    sposta = True
                if (abs(x - mx) == abs(y - my)) and (x != mx) and (y != my):
                    c = random.randint(1, 2)
                    if mx < x and c == 1:
                        nmos = 1
                    if mx > x and c == 1:
                        nmos = 2
                    if my < y and c == 2:
                        nmos = 3
                    if my > y and c == 2:
                        nmos = 4
                    sposta = True
            if (x == mx + gpx and y == my) or (x == mx - gpx and y == my) or (x == mx and y == my + gpy) or (x == mx and y == my - gpy) or ((x == mx) and (y == my)):
                if vistoesca:
                    danno = att
                    if danno < 0:
                        danno = 0
                    print ("attacco vicino", tipo, "a esca", danno)
                    vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
                else:
                    if attrobo:
                        danno = att - difro
                        if danno < 0:
                            danno = 0
                        print ("attacco vicino", tipo, "a robo", danno)
                        dati[10] = dati[10] - danno
                    else:
                        danno = att - dif
                        if danno < 0:
                            danno = 0
                        if random.randint(1, 100) <= par and dati[7] > 0:
                            danno = 0
                            print ("parato:", par)
                        print ("attacco vicino", tipo, "a rallo", danno)
                        dati[5] = dati[5] - danno
                nmos = 0
                if x == mx + gpx and y == my:
                    nmos = 1
                if x == mx - gpx and y == my:
                    nmos = 2
                if x == mx and y == my + gpy:
                    nmos = 3
                if x == mx and y == my - gpy:
                    nmos = 4
                sposta = False

        # nemici che attaccano da lontano
        if attlontano:
            if vistoesca:
                danno = att
                if danno < 0:
                    danno = 0
                print ("attacco lontano", tipo, "a esca", danno)
                vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
            else:
                if attrobo:
                    danno = att - difro
                    if danno < 0:
                        danno = 0
                    print ("attacco lontano", tipo, "a robo", danno)
                    dati[10] = dati[10] - danno
                else:
                    danno = att - dif
                    if danno < 0:
                        danno = 0
                    if random.randint(1, 100) <= par and dati[7] > 0:
                        danno = 0
                        print ("parato:", par)
                    print ("attacco lontano", tipo, "a rallo", danno)
                    dati[5] = dati[5] - danno
            nmos = 0
            if abs(x - mx) > abs(y - my):
                if mx < x:
                    nmos = 1
                if mx > x:
                    nmos = 2
            if abs(y - my) > abs(x - mx):
                if my < y:
                    nmos = 3
                if my > y:
                    nmos = 4
            sposta = False

    # spostamento
    if sposta:
        if nmos == 1:
            if mx + gpx == x and my == y:
                nmx = 0
                nmy = 0
            else:
                nmx = gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if mx + gpx == vitaesca[i] and my == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 2:
            if mx - gpx == x and my == y:
                nmx = 0
                nmy = 0
            else:
                nmx = -gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if mx - gpx == vitaesca[i] and my == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 3:
            if mx == x and my + gpy == y:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = gpy
            i = 2
            while i <= len(vitaesca):
                if mx == vitaesca[i] and my + gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 4:
            if mx == x and my - gpy == y:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = -gpy
            i = 2
            while i <= len(vitaesca):
                if mx == vitaesca[i] and my - gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4

    if muovimost < -1:
        nmos = 0

    # alcuni sono inutili!!!
    mx, my, stanza, carim, muovimost, cambiosta = muri_porte(mx, my, nmx, nmy, stanza, carim, muovimost, mostro, False, porte, cofanetti)
    return mx, my, muovimost, nmos, visto, dati, vitaesca, vistam


def eseguiAzione(rx, ry, pvm, xBersaglio, yBersaglio, azione, suAlleato, nemiciVistiDaColco, dati, caselleVisteDaColco, stanza, porte, cofanetti):
    print "gambit robo"
    vetNemiciSoloConXeY = []
    i = 0
    while i < len(nemiciVistiDaColco):
        vetNemiciSoloConXeY.append(nemiciVistiDaColco[i + 2])
        vetNemiciSoloConXeY.append(nemiciVistiDaColco[i + 3])
        i += 4
    if not suAlleato:
        if pvm == -1 and xBersaglio == -1 and yBersaglio == -1:
            i = 0
            while i < len(nemiciVistiDaColco):
                nemiciVistiDaColco[i + 1] = 0
                i += 4
            return True, pvm, nemiciVistiDaColco
        else:
            pvm = 0
            return True, pvm, nemiciVistiDaColco
    else:
        if suAlleato == 1:
            ralloVisto = False
            vistaRobo = gpx * 6
            i = 0
            while i < len(caselleVisteDaColco):
                if caselleVisteDaColco[i] == xBersaglio and caselleVisteDaColco[i + 1] == yBersaglio and abs(rx - xBersaglio) <= vistaRobo and abs(ry - yBersaglio) <= vistaRobo and caselleVisteDaColco[i + 2]:
                    ralloVisto = True
                i += 3
            if ralloVisto:
                # scossa
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # cura
                if azione == 2 and dati[10] >= costoTecniche[azione]:
                    dati[5] += dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # antidoto
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # freccia
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # tempesta
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # raffred
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # ricarica
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # cura+
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # scossa+
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # freccia+
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # velocizza
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # attP
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # difP
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # efficienza
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # tempesta+
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # cura++
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # ricarica+
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # scossa++
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # freccia++
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
                # tempesa++
                if azione == 1 and dati[10] >= costoTecniche[azione]:
                    dati[5] -= dannoTecniche[azione]
                    if dati[5] < 0:
                        dati[5] = 0
                    if dati[126] > 0:
                        dati[10] -= costoTecniche[azione] // 2
                    else:
                        dati[10] -= costoTecniche[azione]
                    return True
            else:
                percorsoTrovato = pathFinding(rx, ry, xBersaglio, yBersaglio, stanza, porte, cofanetti, vetNemiciSoloConXeY)
                if not percorsoTrovato:
                    return False
                #else:

        if suAlleato == 2:
            if azione == 1 and dati[10] >= costoTecniche[azione]:
                if dati[126] > 0:
                    dati[10] -= 2
                else:
                    dati[10] -= 5
                return True


def movrobo(x, y, vx, vy, rx, ry, stanza, muovirob, chiamarob, dati, porte, cofanetti, vetDatiNemici, nmost):
    robo = True
    nrx = 0
    nry = 0

    # burocrazia
    carim = False

    # trova i nemici visti
    nemiciVistiDaColco = []
    vistaRobo = gpx * 6
    caselleAttaccabili = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
    k = 0
    while k < len(caselleAttaccabili):
        if caselleAttaccabili[k + 2]:
            j = 0
            while j < len(vetDatiNemici):
                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[
                    j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(
                        ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                    # in caselleAttaccabili si ripetono le caselle che hanno stessa x o stessa y della casella di riferimento (che è quella dove sta Colco)
                    giaVisitata = False
                    i = 0
                    while i < len(nemiciVistiDaColco):
                        if nemiciVistiDaColco[i + 2] == vetDatiNemici[j + 1] and nemiciVistiDaColco[i + 3] == \
                                vetDatiNemici[j + 2]:
                            giaVisitata = True
                            break
                        i += 4
                    if not giaVisitata:
                        nemiciVistiDaColco.append(j)
                        nemiciVistiDaColco.append(vetDatiNemici[j])
                        nemiciVistiDaColco.append(vetDatiNemici[j + 1])
                        nemiciVistiDaColco.append(vetDatiNemici[j + 2])
                    break
                j += 4
        k += 3

    nrob = 0
    sposta = False
    # movimento robot
    if chiamarob:
        if abs(rx - x) == gpx and abs(ry - y) == gpy:
            if vx == rx + gpx:
                nrob = 1
            if vx == rx - gpx:
                nrob = 2
            if vy == ry + gpy:
                nrob = 3
            if vy == ry - gpy:
                nrob = 4
            sposta = True
        else:
            vetNemiciSoloConXeY = []
            i = 0
            while i < len(nemiciVistiDaColco):
                vetNemiciSoloConXeY.append(nemiciVistiDaColco[i + 2])
                vetNemiciSoloConXeY.append(nemiciVistiDaColco[i + 3])
                i += 4
            percorsoTrovato = pathFinding(rx, ry, x, y, stanza, porte, cofanetti, vetNemiciSoloConXeY)
            if percorsoTrovato:
                if len(percorsoTrovato) >= 4:
                    if percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry:
                        if percorsoTrovato[len(percorsoTrovato) - 4] > rx:
                            nrob = 1
                        if percorsoTrovato[len(percorsoTrovato) - 4] < rx:
                            nrob = 2
                        if percorsoTrovato[len(percorsoTrovato) - 3] > ry:
                            nrob = 3
                        if percorsoTrovato[len(percorsoTrovato) - 3] < ry:
                            nrob = 4
                        sposta = True
    elif muovirob >= -1:
        esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati)

        """dati: tecniche(11-30) / condizioni(81-100) / gambit(101-120) / pvRallo(5) / veleno(121) / attP(123) / difP(124) / peColco(10) / surriscalda(122) / velP(125) / efficienza(126)
        in gambit: prime 10 -> condizioni, ultime 10 -> tecniche
                   condizioni = intero da 1 a 20: pvR<80, pvR<50, pvR<30, velenoR, surrisC, peC<80, peC<50, peC<30, sempreR, sempreC, nemico+vicinoR, nemicoVicino, nemicoLontano, pvN<80, pvN<50, pvN<30, nemico-pv, numN>1, numN>4, numN>7
                   tecniche = intero da 1 a 20: scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesa++"""

        # controllo se la condizione è rispettata
        azioneEseguita = False
        i = 101
        while i <= 110 and not azioneEseguita:
            # azioni su alleati
            # pv rallo < 80
            if dati[i] == 1:
                if dati[5] < pvtot / float(100) * 80 and dati[5] >= 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[5], x, y, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # pv rallo < 50
            if dati[i] == 2:
                if dati[5] < pvtot / float(100) * 50 and dati[5] > 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[5], x, y, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # pv rallo < 30
            if dati[i] == 3:
                if dati[5] < pvtot / float(100) * 30 and dati[5] > 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[5], x, y, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # rallo avvelenato
            if dati[i] == 4:
                if dati[121]:
                    azioneEseguita = eseguiAzione(rx, ry, dati[5], x, y, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # colco surriscaldato
            if dati[i] == 5:
                if dati[122] > 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[10], rx, ry, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # pe colco < 80
            if dati[i] == 6:
                if dati[10] < entot / float(100) * 80 and dati[10] > 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[10], rx, ry, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # pe colco < 50
            if dati[i] == 7:
                if dati[10] < entot / float(100) * 50 and dati[10] > 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[10], rx, ry, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # pe colco < 30
            if dati[i] == 8:
                if dati[10] < entot / float(100) * 30 and dati[10] > 0:
                    azioneEseguita = eseguiAzione(rx, ry, dati[10], rx, ry, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # sempre rallo
            if dati[i] == 9:
                if (dati[i + 10] != 12 and dati[i + 10] != 13) or (dati[i + 10] == 12 and dati[123] == 0) or (dati[i + 10] == 13 and dati[124] == 0):
                    azioneEseguita = eseguiAzione(rx, ry, dati[10], x, y, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # sempre colco
            if dati[i] == 10:
                if (dati[i + 10] != 11 and dati[i + 10] != 14) or (dati[i + 10] == 11 and dati[125] == 0) or (dati[i + 10] == 14 and dati[126] == 0):
                    azioneEseguita = eseguiAzione(rx, ry, dati[10], rx, ry, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
            # azioni su nemici
            if nmost > 0:
                numeroNemico = 0
                pvm = 0
                mx = 0
                my = 0
                # nemico a caso
                if dati[i] == 11:
                    # nemiciPossibili conterrà [numeroNemico, pvm, mx, my] per ogni nemico visto da Colco (serve per scegliere il nemico casuale)
                    nemiciPossibili = []
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                                    nemiciPossibili.append(j)
                                    nemiciPossibili.append(vetDatiNemici[j])
                                    nemiciPossibili.append(vetDatiNemici[j + 1])
                                    nemiciPossibili.append(vetDatiNemici[j + 2])
                                    break
                                j += 4
                        k += 3
                    if len(nemiciPossibili) > 0:
                        nemicoScelto = random.randint(0, (len(nemiciPossibili) // 4) - 1) * 4
                        numeroNemico = nemiciPossibili[nemicoScelto]
                        pvm = nemiciPossibili[nemicoScelto + 1]
                        mx = nemiciPossibili[nemicoScelto + 2]
                        my = nemiciPossibili[nemicoScelto + 3]
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # nemico vicino
                if dati[i] == 12:
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(vetDatiNemici[j + 1] - rx) <= (gpx * 2) and abs(vetDatiNemici[j + 2] - ry) <= (gpy * 2) and vetDatiNemici[j] > 0:
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # nemico lontano
                if dati[i] == 13:
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and (abs(vetDatiNemici[j + 1] - rx) >= (gpx * 3) or abs(vetDatiNemici[j + 2] - ry) >= (gpy * 3)) and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # nemico pv < 80
                if dati[i] == 14:
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0 and vetDatiNemici[j] < vetDatiNemici[j + 3] / float(100) * 80:
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # nemico pv < 50
                if dati[i] == 15:
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0 and vetDatiNemici[j] < vetDatiNemici[j + 3] / float(100) * 50:
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # nemico pv < 30
                if dati[i] == 16:
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0 and vetDatiNemici[j] < vetDatiNemici[j + 3] / float(100) * 30:
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # nemico con meno pv
                if dati[i] == 17:
                    pvMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                                    if primoMostro:
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        pvMin = pvm
                                        primoMostro = False
                                    elif vetDatiNemici[j] < pvMin:
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        pvMin = pvm
                                    break
                                j += 4
                        k += 3
                    if mx != 0 and my != 0:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # numero nemici > 1
                if dati[i] == 18:
                    numeroNemici = 0
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                                    numeroNemici += 1
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if numeroNemici > 1:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # numero nemici > 4
                if dati[i] == 19:
                    numeroNemici = 0
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                                    numeroNemici += 1
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if numeroNemici > 4:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
                # numero nemici > 7
                if dati[i] == 20:
                    numeroNemici = 0
                    distMin = -1
                    primoMostro = True
                    k = 0
                    while k < len(caselleAttaccabili):
                        if caselleAttaccabili[k + 2]:
                            j = 0
                            while j < len(vetDatiNemici):
                                if caselleAttaccabili[k] == vetDatiNemici[j + 1] and caselleAttaccabili[k + 1] == vetDatiNemici[j + 2] and abs(rx - vetDatiNemici[j + 1]) <= vistaRobo and abs(ry - vetDatiNemici[j + 2]) <= vistaRobo and vetDatiNemici[j] > 0:
                                    numeroNemici += 1
                                    if primoMostro:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                        primoMostro = False
                                    elif abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry) < distMin:
                                        distMin = abs(vetDatiNemici[j + 1] - rx) + abs(vetDatiNemici[j + 2] - ry)
                                        numeroNemico = j
                                        pvm = vetDatiNemici[j]
                                        mx = vetDatiNemici[j + 1]
                                        my = vetDatiNemici[j + 2]
                                    break
                                j += 4
                        k += 3
                    if numeroNemici > 7:
                        azioneEseguita, pvm, nemiciVistiDaColco = eseguiAzione(rx, ry, pvm, mx, my, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, stanza, porte, cofanetti)
                        vetDatiNemici[numeroNemico] = pvm
                        k = 0
                        while k < len(vetDatiNemici):
                            j = 0
                            while j < len(nemiciVistiDaColco):
                                if k == nemiciVistiDaColco[j]:
                                    vetDatiNemici[k] = nemiciVistiDaColco[j + 1]
                                    vetDatiNemici[k + 1] = nemiciVistiDaColco[j + 2]
                                    vetDatiNemici[k + 2] = nemiciVistiDaColco[j + 3]
                                j += 4
                            k += 4
            i += 1

    # spostamento
    if sposta:
        if nrob == 1:
            if rx + gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = gpx
                nry = 0
        if nrob == 2:
            if rx - gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = -gpx
                nry = 0
        if nrob == 3:
            if rx == x and ry + gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = gpy
        if nrob == 4:
            if rx == x and ry - gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = -gpy

    # alcuni sono inutili!!!
    rx, ry, stanza, carim, muovirob, cambiosta = muri_porte(rx, ry, nrx, nry, stanza, carim, muovirob, False, robo, porte, cofanetti)
    return rx, ry, muovirob, nrob, dati, vetDatiNemici
