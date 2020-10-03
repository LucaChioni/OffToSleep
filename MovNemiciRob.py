# -*- coding: utf-8 -*-

from GenericFuncA import *


def movmostro(x, y, rx, ry, nemico, stanza, dif, difro, par, dati, vitaesca, porte, cofanetti, vetNemici, vistoRallo, vistoRob, vistoesca, escabersaglio, vistoDenaro, xDenaro, yDenaro, attrobo, listaPersonaggi, caseviste):
    sposta = False
    attacca = False
    nmos = 0
    nmx = 0
    nmy = 0
    avvelena = nemico.velenoso
    surriscalda = nemico.surriscaldante

    # burocrazia
    carim = False

    if vistoRallo or vistoRob or vistoesca:
        nemico.triggerato = True
        # andare verso il sacchetto di denaro
        if nemico.xObbiettivo == xDenaro and nemico.yObbiettivo == yDenaro:
            vetNemiciSoloConXeY = []
            vetNemiciSoloConXeY.append(x)
            vetNemiciSoloConXeY.append(y)
            vetNemiciSoloConXeY.append(rx)
            vetNemiciSoloConXeY.append(ry)
            i = 0
            while i < len(vetNemici):
                if not (vetNemici[i + 1] == nemico.x and vetNemici[i + 2] == nemico.y):
                    vetNemiciSoloConXeY.append(vetNemici[i + 1])
                    vetNemiciSoloConXeY.append(vetNemici[i + 2])
                i += 4
            for personaggio in listaPersonaggi:
                if not personaggio.mantieniSempreASchermo:
                    vetNemiciSoloConXeY.append(personaggio.x)
                    vetNemiciSoloConXeY.append(personaggio.y)
            percorsoTrovato = pathFinding(nemico.x, nemico.y, nemico.xObbiettivo, nemico.yObbiettivo, vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato:
                if len(percorsoTrovato) >= 4:
                    if percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y:
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
                if abs(nemico.xObbiettivo - nemico.x) > abs(nemico.yObbiettivo - nemico.y):
                    if nemico.x < nemico.xObbiettivo:
                        nmos = 1
                    if nemico.x > nemico.xObbiettivo:
                        nmos = 2
                    sposta = True
                if abs(nemico.yObbiettivo - nemico.y) > abs(nemico.xObbiettivo - nemico.x):
                    if nemico.y < nemico.yObbiettivo:
                        nmos = 3
                    if nemico.y > nemico.yObbiettivo:
                        nmos = 4
                    sposta = True
                if (abs(nemico.xObbiettivo - nemico.x) == abs(nemico.yObbiettivo - nemico.y)) and (nemico.xObbiettivo != nemico.x) and (nemico.yObbiettivo != nemico.y):
                    c = random.randint(1, 2)
                    if nemico.x < nemico.xObbiettivo and c == 1:
                        nmos = 1
                    if nemico.x > nemico.xObbiettivo and c == 1:
                        nmos = 2
                    if nemico.y < nemico.yObbiettivo and c == 2:
                        nmos = 3
                    if nemico.y > nemico.yObbiettivo and c == 2:
                        nmos = 4
                    sposta = True
            if abs(nemico.xObbiettivo - nemico.x) == GlobalVar.gpx and abs(nemico.yObbiettivo - nemico.y) == 0:
                if nemico.x < nemico.xObbiettivo:
                    nmos = 1
                if nemico.x > nemico.xObbiettivo:
                    nmos = 2
                sposta = True
                nemico.xObbiettivo = False
                nemico.yObbiettivo = False
            if abs(nemico.yObbiettivo - nemico.y) == GlobalVar.gpy and abs(nemico.xObbiettivo - nemico.x) == 0:
                if nemico.y < nemico.yObbiettivo:
                    nmos = 3
                if nemico.y > nemico.yObbiettivo:
                    nmos = 4
                sposta = True
                nemico.xObbiettivo = False
                nemico.yObbiettivo = False

        # nemici che attaccano da vicino
        elif not nemico.attaccaDaLontano:
            if (nemico.xObbiettivo == nemico.x + GlobalVar.gpx and nemico.yObbiettivo == nemico.y) or (nemico.xObbiettivo == nemico.x - GlobalVar.gpx and nemico.yObbiettivo == nemico.y) or (nemico.xObbiettivo == nemico.x and nemico.yObbiettivo == nemico.y + GlobalVar.gpy) or (nemico.xObbiettivo == nemico.x and nemico.yObbiettivo == nemico.y - GlobalVar.gpy) or (nemico.xObbiettivo == nemico.x and nemico.yObbiettivo == nemico.y):
                if vistoesca:
                    danno = nemico.attacco
                    if danno < 0:
                        danno = 0
                    print ("attacco vicino", nemico.tipo, "a esca", danno)
                    nemico.bersaglioColpito.append("Esca" + str(vitaesca[escabersaglio]))
                    nemico.bersaglioColpito.append(-danno)
                    nemico.bersaglioColpito.append("")
                    vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
                else:
                    if attrobo:
                        danno = nemico.attacco - difro
                        if danno < 0:
                            danno = 0
                        nemico.bersaglioColpito.append("Colco")
                        nemico.bersaglioColpito.append(-danno)
                        if surriscalda:
                            dati[122] = 10
                            nemico.bersaglioColpito.append("surriscalda")
                        else:
                            nemico.bersaglioColpito.append("")
                        print ("attacco vicino", nemico.tipo, "a robo", danno)
                        dati[10] = dati[10] - danno
                    else:
                        danno = nemico.attacco - dif
                        if danno < 0:
                            danno = 0
                        if random.randint(1, 100) <= par:
                            danno = 0
                            avvelena = False
                            nemico.ralloParato = True
                            print ("parato:", par)
                        nemico.bersaglioColpito.append("Rallo")
                        nemico.bersaglioColpito.append(-danno)
                        if avvelena and not dati[130] == 1:
                            dati[121] = True
                            nemico.bersaglioColpito.append("avvelena")
                        else:
                            nemico.bersaglioColpito.append("")
                        print ("attacco vicino", nemico.tipo, "a rallo", danno)
                        dati[5] = dati[5] - danno
                nmos = 0
                if nemico.xObbiettivo == nemico.x + GlobalVar.gpx and nemico.yObbiettivo == nemico.y:
                    nmos = 1
                if nemico.xObbiettivo == nemico.x - GlobalVar.gpx and nemico.yObbiettivo == nemico.y:
                    nmos = 2
                if nemico.xObbiettivo == nemico.x and nemico.yObbiettivo == nemico.y + GlobalVar.gpy:
                    nmos = 3
                if nemico.xObbiettivo == nemico.x and nemico.yObbiettivo == nemico.y - GlobalVar.gpy:
                    nmos = 4
                attacca = True
                sposta = False
            else:
                vetNemiciSoloConXeY = []
                i = 0
                while i < len(vetNemici):
                    if not (vetNemici[i + 1] == nemico.x and vetNemici[i + 2] == nemico.y):
                        vetNemiciSoloConXeY.append(vetNemici[i + 1])
                        vetNemiciSoloConXeY.append(vetNemici[i + 2])
                    i += 4
                if not (nemico.xObbiettivo == x and nemico.yObbiettivo == y):
                    vetNemiciSoloConXeY.append(x)
                    vetNemiciSoloConXeY.append(y)
                if not (nemico.xObbiettivo == rx and nemico.yObbiettivo == ry):
                    vetNemiciSoloConXeY.append(rx)
                    vetNemiciSoloConXeY.append(ry)
                for personaggio in listaPersonaggi:
                    if not personaggio.mantieniSempreASchermo:
                        vetNemiciSoloConXeY.append(personaggio.x)
                        vetNemiciSoloConXeY.append(personaggio.y)
                percorsoTrovato = pathFinding(nemico.x, nemico.y, nemico.xObbiettivo, nemico.yObbiettivo, vetNemiciSoloConXeY, caseviste)
                if percorsoTrovato:
                    if len(percorsoTrovato) >= 4:
                        if percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y:
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
                    if abs(nemico.xObbiettivo - nemico.x) > abs(nemico.yObbiettivo - nemico.y):
                        if nemico.x < nemico.xObbiettivo:
                            nmos = 1
                        if nemico.x > nemico.xObbiettivo:
                            nmos = 2
                        sposta = True
                    if abs(nemico.yObbiettivo - nemico.y) > abs(nemico.xObbiettivo - nemico.x):
                        if nemico.y < nemico.yObbiettivo:
                            nmos = 3
                        if nemico.y > nemico.yObbiettivo:
                            nmos = 4
                        sposta = True
                    if (abs(nemico.xObbiettivo - nemico.x) == abs(nemico.yObbiettivo - nemico.y)) and (nemico.xObbiettivo != nemico.x) and (nemico.yObbiettivo != nemico.y):
                        c = random.randint(1, 2)
                        if nemico.x < nemico.xObbiettivo and c == 1:
                            nmos = 1
                        if nemico.x > nemico.xObbiettivo and c == 1:
                            nmos = 2
                        if nemico.y < nemico.yObbiettivo and c == 2:
                            nmos = 3
                        if nemico.y > nemico.yObbiettivo and c == 2:
                            nmos = 4
                        sposta = True

        # nemici che attaccano da lontano
        elif nemico.attaccaDaLontano:
            if vistoesca:
                danno = nemico.attacco
                if danno < 0:
                    danno = 0
                nemico.bersaglioColpito.append("Esca" + str(vitaesca[escabersaglio]))
                nemico.bersaglioColpito.append(-danno)
                nemico.bersaglioColpito.append("")
                print ("attacco lontano", nemico.tipo, "a esca", danno)
                vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
                nmos = 0
                if abs(nemico.xObbiettivo - nemico.x) > abs(nemico.yObbiettivo - nemico.y):
                    if nemico.x < nemico.xObbiettivo:
                        nmos = 1
                    if nemico.x > nemico.xObbiettivo:
                        nmos = 2
                if abs(nemico.yObbiettivo - nemico.y) > abs(nemico.xObbiettivo - nemico.x):
                    if nemico.y < nemico.yObbiettivo:
                        nmos = 3
                    if nemico.y > nemico.yObbiettivo:
                        nmos = 4
                if (abs(nemico.xObbiettivo - nemico.x) == abs(nemico.yObbiettivo - nemico.y)) and (nemico.xObbiettivo != nemico.x) and (nemico.yObbiettivo != nemico.y):
                    c = random.randint(1, 2)
                    if nemico.x < nemico.xObbiettivo and c == 1:
                        nmos = 1
                    if nemico.x > nemico.xObbiettivo and c == 1:
                        nmos = 2
                    if nemico.y < nemico.yObbiettivo and c == 2:
                        nmos = 3
                    if nemico.y > nemico.yObbiettivo and c == 2:
                        nmos = 4
                attacca = True
                sposta = False
            else:
                if (x == nemico.x + GlobalVar.gpx and y == nemico.y) or (x == nemico.x - GlobalVar.gpx and y == nemico.y) or (x == nemico.x and y == nemico.y + GlobalVar.gpy) or (x == nemico.x and y == nemico.y - GlobalVar.gpy) or (rx == nemico.x + GlobalVar.gpx and ry == nemico.y) or (rx == nemico.x - GlobalVar.gpx and ry == nemico.y) or (rx == nemico.x and ry == nemico.y + GlobalVar.gpy) or (rx == nemico.x and ry == nemico.y - GlobalVar.gpy):
                    # nmos: 1=d, 2=a, 3=s, 4=w
                    xRalloVicino = 0
                    yRalloVicino = 0
                    xColcoVicino = 0
                    yColcoVicino = 0
                    casellaDaControllarePrima = 0
                    if (x == nemico.x + GlobalVar.gpx and y == nemico.y) or (x == nemico.x - GlobalVar.gpx and y == nemico.y) or (x == nemico.x and y == nemico.y + GlobalVar.gpy) or (x == nemico.x and y == nemico.y - GlobalVar.gpy):
                        xRalloVicino = x
                        yRalloVicino = y
                    if (rx == nemico.x + GlobalVar.gpx and ry == nemico.y) or (rx == nemico.x - GlobalVar.gpx and ry == nemico.y) or (rx == nemico.x and ry == nemico.y + GlobalVar.gpy) or (rx == nemico.x and ry == nemico.y - GlobalVar.gpy):
                        xColcoVicino = rx
                        yColcoVicino = ry
                    if xRalloVicino != 0 and yRalloVicino != 0 and xColcoVicino != 0 and yColcoVicino != 0:
                        casellaTrovata = False
                        nmxProbabile = GlobalVar.gpx
                        nmyProbabile = 0
                        mxProbabile, myProbabile, inutile, inutile, inutile = muri_porte(nemico.x, nemico.y, nmxProbabile, nmyProbabile, stanza, carim, True, False, porte, cofanetti, listaPersonaggi)
                        if not ((x == mxProbabile + GlobalVar.gpx and y == myProbabile) or (x == mxProbabile - GlobalVar.gpx and y == myProbabile) or (x == mxProbabile and y == myProbabile + GlobalVar.gpy) or (x == mxProbabile and y == myProbabile - GlobalVar.gpy) or (x == mxProbabile and y == myProbabile) or (rx == mxProbabile + GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile - GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile and ry == myProbabile + GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile - GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile)):
                            if casellaTrovata:
                                if random.randint(0, 1) == 0:
                                    nmos = 1
                                    sposta = True
                            else:
                                nmos = 1
                                sposta = True
                                casellaTrovata = True
                        nmxProbabile = -GlobalVar.gpx
                        nmyProbabile = 0
                        mxProbabile, myProbabile, inutile, inutile, inutile = muri_porte(nemico.x, nemico.y, nmxProbabile, nmyProbabile, stanza, carim, True, False, porte, cofanetti, listaPersonaggi)
                        if not ((x == mxProbabile + GlobalVar.gpx and y == myProbabile) or (x == mxProbabile - GlobalVar.gpx and y == myProbabile) or (x == mxProbabile and y == myProbabile + GlobalVar.gpy) or (x == mxProbabile and y == myProbabile - GlobalVar.gpy) or (x == mxProbabile and y == myProbabile) or (rx == mxProbabile + GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile - GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile and ry == myProbabile + GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile - GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile)):
                            if casellaTrovata:
                                if random.randint(0, 1) == 0:
                                    nmos = 2
                                    sposta = True
                            else:
                                nmos = 2
                                sposta = True
                                casellaTrovata = True
                        nmxProbabile = 0
                        nmyProbabile = GlobalVar.gpy
                        mxProbabile, myProbabile, inutile, inutile, inutile = muri_porte(nemico.x, nemico.y, nmxProbabile, nmyProbabile, stanza, carim, True, False, porte, cofanetti, listaPersonaggi)
                        if not ((x == mxProbabile + GlobalVar.gpx and y == myProbabile) or (x == mxProbabile - GlobalVar.gpx and y == myProbabile) or (x == mxProbabile and y == myProbabile + GlobalVar.gpy) or (x == mxProbabile and y == myProbabile - GlobalVar.gpy) or (x == mxProbabile and y == myProbabile) or (rx == mxProbabile + GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile - GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile and ry == myProbabile + GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile - GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile)):
                            if casellaTrovata:
                                if random.randint(0, 1) == 0:
                                    nmos = 3
                                    sposta = True
                            else:
                                nmos = 3
                                sposta = True
                                casellaTrovata = True
                        nmxProbabile = 0
                        nmyProbabile = -GlobalVar.gpy
                        mxProbabile, myProbabile, inutile, inutile, inutile = muri_porte(nemico.x, nemico.y, nmxProbabile, nmyProbabile, stanza, carim, True, False, porte, cofanetti, listaPersonaggi)
                        if not ((x == mxProbabile + GlobalVar.gpx and y == myProbabile) or (x == mxProbabile - GlobalVar.gpx and y == myProbabile) or (x == mxProbabile and y == myProbabile + GlobalVar.gpy) or (x == mxProbabile and y == myProbabile - GlobalVar.gpy) or (x == mxProbabile and y == myProbabile) or (rx == mxProbabile + GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile - GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile and ry == myProbabile + GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile - GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile)):
                            if casellaTrovata:
                                if random.randint(0, 1) == 0:
                                    nmos = 4
                                    sposta = True
                            else:
                                nmos = 4
                                sposta = True
                    else:
                        if xRalloVicino != 0 and yRalloVicino != 0:
                            if nemico.x - GlobalVar.gpx == xRalloVicino and nemico.y == yRalloVicino:
                                casellaDaControllarePrima = 1
                            elif nemico.x + GlobalVar.gpx == xRalloVicino and nemico.y == yRalloVicino:
                                casellaDaControllarePrima = 2
                            elif nemico.x == xRalloVicino and nemico.y - GlobalVar.gpy == yRalloVicino:
                                casellaDaControllarePrima = 3
                            elif nemico.x == xRalloVicino and nemico.y + GlobalVar.gpy == yRalloVicino:
                                casellaDaControllarePrima = 4
                        elif xColcoVicino != 0 and yColcoVicino != 0:
                            if nemico.x - GlobalVar.gpx == xColcoVicino and nemico.y == yColcoVicino:
                                casellaDaControllarePrima = 1
                            elif nemico.x + GlobalVar.gpx == xColcoVicino and nemico.y == yColcoVicino:
                                casellaDaControllarePrima = 2
                            elif nemico.x == xColcoVicino and nemico.y - GlobalVar.gpy == yColcoVicino:
                                casellaDaControllarePrima = 3
                            elif nemico.x == xColcoVicino and nemico.y + GlobalVar.gpy == yColcoVicino:
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
                                nmxProbabile = GlobalVar.gpx
                                nmyProbabile = 0
                            elif i == 2:
                                nmxProbabile = -GlobalVar.gpx
                                nmyProbabile = 0
                            elif i == 3:
                                nmxProbabile = 0
                                nmyProbabile = GlobalVar.gpy
                            elif i == 4:
                                nmxProbabile = 0
                                nmyProbabile = -GlobalVar.gpy
                            mxProbabile, myProbabile, inutile, inutile, inutile = muri_porte(nemico.x, nemico.y, nmxProbabile, nmyProbabile, stanza, carim, True, False, porte, cofanetti, listaPersonaggi)
                            if not ((x == mxProbabile + GlobalVar.gpx and y == myProbabile) or (x == mxProbabile - GlobalVar.gpx and y == myProbabile) or (x == mxProbabile and y == myProbabile + GlobalVar.gpy) or (x == mxProbabile and y == myProbabile - GlobalVar.gpy) or (x == mxProbabile and y == myProbabile) or (rx == mxProbabile + GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile - GlobalVar.gpx and ry == myProbabile) or (rx == mxProbabile and ry == myProbabile + GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile - GlobalVar.gpy) or (rx == mxProbabile and ry == myProbabile)):
                                nmos = i
                                sposta = True
                                break

                if not sposta:
                    if attrobo:
                        danno = nemico.attacco - difro
                        if danno < 0:
                            danno = 0
                        nemico.bersaglioColpito.append("Colco")
                        nemico.bersaglioColpito.append(-danno)
                        if surriscalda:
                            dati[122] = 10
                            nemico.bersaglioColpito.append("surriscalda")
                        else:
                            nemico.bersaglioColpito.append("")
                        print ("attacco lontano", nemico.tipo, "a robo", danno)
                        dati[10] = dati[10] - danno
                    else:
                        danno = nemico.attacco - dif
                        if danno < 0:
                            danno = 0
                        if random.randint(1, 100) <= par:
                            danno = 0
                            avvelena = False
                            nemico.ralloParato = True
                            print ("parato:", par)
                        nemico.bersaglioColpito.append("Rallo")
                        nemico.bersaglioColpito.append(-danno)
                        if avvelena and not dati[130] == 1:
                            dati[121] = True
                            nemico.bersaglioColpito.append("avvelena")
                        else:
                            nemico.bersaglioColpito.append("")
                        print ("attacco lontano", nemico.tipo, "a rallo", danno)
                        dati[5] = dati[5] - danno
                    nmos = 0
                    if abs(nemico.xObbiettivo - nemico.x) > abs(nemico.yObbiettivo - nemico.y):
                        if nemico.x < nemico.xObbiettivo:
                            nmos = 1
                        if nemico.x > nemico.xObbiettivo:
                            nmos = 2
                    if abs(nemico.yObbiettivo - nemico.y) > abs(nemico.xObbiettivo - nemico.x):
                        if nemico.y < nemico.yObbiettivo:
                            nmos = 3
                        if nemico.y > nemico.yObbiettivo:
                            nmos = 4
                    if (abs(nemico.xObbiettivo - nemico.x) == abs(nemico.yObbiettivo - nemico.y)) and (nemico.xObbiettivo != nemico.x) and (nemico.yObbiettivo != nemico.y):
                        c = random.randint(1, 2)
                        if nemico.x < nemico.xObbiettivo and c == 1:
                            nmos = 1
                        if nemico.x > nemico.xObbiettivo and c == 1:
                            nmos = 2
                        if nemico.y < nemico.yObbiettivo and c == 2:
                            nmos = 3
                        if nemico.y > nemico.yObbiettivo and c == 2:
                            nmos = 4
                    attacca = True
                    sposta = False
    elif vistoDenaro:
        nemico.triggerato = True
        nemico.xObbiettivo = xDenaro
        nemico.yObbiettivo = yDenaro
        vetNemiciSoloConXeY = []
        i = 0
        while i < len(vetNemici):
            if not (vetNemici[i + 1] == nemico.x and vetNemici[i + 2] == nemico.y):
                vetNemiciSoloConXeY.append(vetNemici[i + 1])
                vetNemiciSoloConXeY.append(vetNemici[i + 2])
            i += 4
        for personaggio in listaPersonaggi:
            if not personaggio.mantieniSempreASchermo:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
        percorsoTrovato = pathFinding(nemico.x, nemico.y, nemico.xObbiettivo, nemico.yObbiettivo, vetNemiciSoloConXeY, caseviste)
        if percorsoTrovato:
            if len(percorsoTrovato) >= 4:
                if percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y:
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
            if abs(nemico.xObbiettivo - nemico.x) > abs(nemico.yObbiettivo - nemico.y):
                if nemico.x < nemico.xObbiettivo:
                    nmos = 1
                if nemico.x > nemico.xObbiettivo:
                    nmos = 2
                sposta = True
            if abs(nemico.yObbiettivo - nemico.y) > abs(nemico.xObbiettivo - nemico.x):
                if nemico.y < nemico.yObbiettivo:
                    nmos = 3
                if nemico.y > nemico.yObbiettivo:
                    nmos = 4
                sposta = True
            if (abs(nemico.xObbiettivo - nemico.x) == abs(nemico.yObbiettivo - nemico.y)) and (nemico.xObbiettivo != nemico.x) and (nemico.yObbiettivo != nemico.y):
                c = random.randint(1, 2)
                if nemico.x < nemico.xObbiettivo and c == 1:
                    nmos = 1
                if nemico.x > nemico.xObbiettivo and c == 1:
                    nmos = 2
                if nemico.y < nemico.yObbiettivo and c == 2:
                    nmos = 3
                if nemico.y > nemico.yObbiettivo and c == 2:
                    nmos = 4
                sposta = True
        if abs(nemico.xObbiettivo - nemico.x) == GlobalVar.gpx and abs(nemico.yObbiettivo - nemico.y) == 0:
            if nemico.x < nemico.xObbiettivo:
                nmos = 1
            if nemico.x > nemico.xObbiettivo:
                nmos = 2
            sposta = True
            nemico.xObbiettivo = False
            nemico.yObbiettivo = False
        if abs(nemico.yObbiettivo - nemico.y) == GlobalVar.gpy and abs(nemico.xObbiettivo - nemico.x) == 0:
            if nemico.y < nemico.yObbiettivo:
                nmos = 3
            if nemico.y > nemico.yObbiettivo:
                nmos = 4
            sposta = True
            nemico.xObbiettivo = False
            nemico.yObbiettivo = False
    elif nemico.xPosizioneUltimoBersaglio and nemico.yPosizioneUltimoBersaglio:
        nemico.triggerato = True
        if (nemico.xPosizioneUltimoBersaglio == nemico.x + GlobalVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y) or (nemico.xPosizioneUltimoBersaglio == nemico.x - GlobalVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y) or (nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y + GlobalVar.gpy) or (nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y - GlobalVar.gpy):
            if nemico.xPosizioneUltimoBersaglio == nemico.x + GlobalVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y:
                nmos = 1
            if nemico.xPosizioneUltimoBersaglio == nemico.x - GlobalVar.gpx and nemico.yPosizioneUltimoBersaglio == nemico.y:
                nmos = 2
            if nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y + GlobalVar.gpy:
                nmos = 3
            if nemico.xPosizioneUltimoBersaglio == nemico.x and nemico.yPosizioneUltimoBersaglio == nemico.y - GlobalVar.gpy:
                nmos = 4
            nemico.xObbiettivo = False
            nemico.yObbiettivo = False
            sposta = True
        else:
            vetNemiciSoloConXeY = []
            i = 0
            while i < len(vetNemici):
                if not (vetNemici[i + 1] == nemico.x and vetNemici[i + 2] == nemico.y):
                    vetNemiciSoloConXeY.append(vetNemici[i + 1])
                    vetNemiciSoloConXeY.append(vetNemici[i + 2])
                i += 4
            for personaggio in listaPersonaggi:
                if not personaggio.mantieniSempreASchermo:
                    vetNemiciSoloConXeY.append(personaggio.x)
                    vetNemiciSoloConXeY.append(personaggio.y)
            percorsoTrovato = pathFinding(nemico.x, nemico.y, nemico.xPosizioneUltimoBersaglio, nemico.yPosizioneUltimoBersaglio, vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato and not percorsoTrovato == "arrivato":
                if len(percorsoTrovato) >= 4:
                    if percorsoTrovato[len(percorsoTrovato) - 4] != nemico.x or percorsoTrovato[len(percorsoTrovato) - 3] != nemico.y:
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
                nemico.xPosizioneUltimoBersaglio = False
                nemico.yPosizioneUltimoBersaglio = False
                nemico.xObbiettivo = False
                nemico.yObbiettivo = False
                if nemico.triggerato:
                    nmos = random.randint(1, 4)
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
                    else:
                        nmos = 0
                sposta = True
    else:
        nemico.xObbiettivo = False
        nemico.yObbiettivo = False
        if nemico.triggerato:
            nmos = random.randint(1, 4)
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
            else:
                nmos = 0
        sposta = True

    # spostamento
    if sposta:
        # 1=d, 2=a, 3=s, 4=w
        if nmos == 1:
            if nemico.x + GlobalVar.gpx == nemico.xObbiettivo and nemico.y == nemico.yObbiettivo:
                nmx = 0
                nmy = 0
            else:
                nmx = GlobalVar.gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if nemico.x + GlobalVar.gpx == vitaesca[i] and nemico.y == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 2:
            if nemico.x - GlobalVar.gpx == nemico.xObbiettivo and nemico.y == nemico.yObbiettivo:
                nmx = 0
                nmy = 0
            else:
                nmx = -GlobalVar.gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if nemico.x - GlobalVar.gpx == vitaesca[i] and nemico.y == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 3:
            if nemico.x == nemico.xObbiettivo and nemico.y + GlobalVar.gpy == nemico.yObbiettivo:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = GlobalVar.gpy
            i = 2
            while i <= len(vitaesca):
                if nemico.x == vitaesca[i] and nemico.y + GlobalVar.gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 4:
            if nemico.x == nemico.xObbiettivo and nemico.y - GlobalVar.gpy == nemico.yObbiettivo:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = -GlobalVar.gpy
            i = 2
            while i <= len(vitaesca):
                if nemico.x == vitaesca[i] and nemico.y - GlobalVar.gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4

    # alcuni sono inutili!!!
    nemico.x, nemico.y, stanza, carim, cambiosta = muri_porte(nemico.x, nemico.y, nmx, nmy, stanza, carim, True, False, porte, cofanetti, listaPersonaggi)

    if sposta and (nemico.x != nemico.vx or nemico.y != nemico.vy):
        nemico.animaSpostamento = True
    if attacca:
        nemico.animaAttacco = True
    if vistoRallo or vistoRob:
        nemico.visto = True
    return nemico, nmos, dati, vitaesca


def eseguiAzione(rx, ry, nemicoBersaglio, azione, suAlleato, nemiciVistiDaColco, dati, caselleVisteDaColco, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste):
    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)
    if dati[126] > 0:
        costoTecnicaUsata = GlobalVar.costoTecniche[azione - 1] // 2
    else:
        costoTecnicaUsata = GlobalVar.costoTecniche[azione - 1]
    raffreddamento = False
    ricarica1 = False
    ricarica2 = False
    azioneEseguita = False
    nrob = 0
    sposta = False
    vetNemiciSoloConXeY = []
    if not suAlleato:
        vetNemiciSoloConXeY.append(x)
        vetNemiciSoloConXeY.append(y)
    for nemico in nemiciVistiDaColco:
        vetNemiciSoloConXeY.append(nemico.x)
        vetNemiciSoloConXeY.append(nemico.y)
    for personaggio in listaPersonaggi:
        if not personaggio.mantieniSempreASchermo:
            vetNemiciSoloConXeY.append(personaggio.x)
            vetNemiciSoloConXeY.append(personaggio.y)

    if azione == 6 or azione == 7 or azione == 11 or azione == 14 or azione == 17:
        if dati[10] >= costoTecnicaUsata and not (dati[122] > 0 and (azione == 11 or azione == 14)):
            azioneEseguita = True
            attaccoDiColco.append("Colco")
            attaccoDiColco.append(-costoTecnicaUsata)
            attaccoDiColco.append("")
            dati[10] -= costoTecnicaUsata
            attaccoDiColco.append("Colco")
            attaccoDiColco.append(0)
        # raffred
        if azione == 6 and dati[10] >= costoTecnicaUsata:
            raffreddamento = True
            attaccoDiColco.append("raffredda")
        # ricarica
        if azione == 7 and dati[10] >= costoTecnicaUsata:
            ricarica1 = True
            attaccoDiColco.append("")
        # velocizza
        if azione == 11 and dati[10] >= costoTecnicaUsata and dati[122] <= 0:
            dati[125] = GlobalVar.dannoTecniche[azione - 1]
            attaccoDiColco.append("velocizza")
        # efficienza
        if azione == 14 and dati[10] >= costoTecnicaUsata and dati[122] <= 0:
            dati[126] = GlobalVar.dannoTecniche[azione - 1]
            attaccoDiColco.append("efficienza")
        # ricarica+
        if azione == 17 and dati[10] >= costoTecnicaUsata:
            ricarica2 = True
            attaccoDiColco.append("")
        if not suAlleato:
            return azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco
        else:
            return azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco
    elif not suAlleato:
        ralloVisto = False
        i = 0
        while i < len(caselleVisteDaColco):
            if caselleVisteDaColco[i] == x and caselleVisteDaColco[i + 1] == y and caselleVisteDaColco[i + 2]:
                ralloVisto = True
                break
            i += 3
        mostroAccanto = False
        mostroVisto = True
        if (rx == nemicoBersaglio.x and ry == nemicoBersaglio.y) or (rx + GlobalVar.gpx == nemicoBersaglio.x and ry == nemicoBersaglio.y) or (rx - GlobalVar.gpx == nemicoBersaglio.x and ry == nemicoBersaglio.y) or (rx == nemicoBersaglio.x and ry + GlobalVar.gpy == nemicoBersaglio.y) or (rx == nemicoBersaglio.x and ry - GlobalVar.gpy == nemicoBersaglio.y):
            mostroAccanto = True
            mostroVisto = True
        if mostroAccanto and (azione == 1 or azione == 2 or azione == 3 or azione == 8 or azione == 9 or azione == 12 or azione == 13 or azione == 16 or azione == 18):
            if dati[10] >= costoTecnicaUsata:
                azioneEseguita = True
                attaccoDiColco.append("Colco")
                attaccoDiColco.append(-costoTecnicaUsata)
                attaccoDiColco.append("")
                dati[10] -= costoTecnicaUsata
            # scossa
            if azione == 1 and dati[10] >= costoTecnicaUsata:
                danno = GlobalVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = danno - nemicoBersaglio.difesa
                if dannoEffettivo < 0:
                    dannoEffettivo = 0
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # cura
            if azione == 2 and dati[10] >= costoTecnicaUsata:
                nemicoBersaglio.vita += GlobalVar.dannoTecniche[azione - 1]
                if nemicoBersaglio.vita > nemicoBersaglio.vitaTotale:
                    nemicoBersaglio.vita = nemicoBersaglio.vitaTotale
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(GlobalVar.dannoTecniche[azione - 1])
                attaccoDiColco.append("")
            # antidoto
            if azione == 3 and dati[10] >= costoTecnicaUsata:
                nemicoBersaglio.avvelenato = False
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(0)
                attaccoDiColco.append("antidoto")
            # cura+
            if azione == 8 and dati[10] >= costoTecnicaUsata:
                nemicoBersaglio.vita += GlobalVar.dannoTecniche[azione - 1]
                if nemicoBersaglio.vita > nemicoBersaglio.vitaTotale:
                    nemicoBersaglio.vita = nemicoBersaglio.vitaTotale
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(GlobalVar.dannoTecniche[azione - 1])
                attaccoDiColco.append("")
            # scossa+
            if azione == 9 and dati[10] >= costoTecnicaUsata:
                danno = GlobalVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = danno - nemicoBersaglio.difesa
                if dannoEffettivo < 0:
                    dannoEffettivo = 0
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # attP
            if azione == 12 and dati[10] >= costoTecnicaUsata:
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(0)
                attaccoDiColco.append("")
            # difP
            if azione == 13 and dati[10] >= costoTecnicaUsata:
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(0)
                attaccoDiColco.append("")
            # cura++
            if azione == 16 and dati[10] >= costoTecnicaUsata:
                nemicoBersaglio.vita += GlobalVar.dannoTecniche[azione - 1]
                if nemicoBersaglio.vita > nemicoBersaglio.vitaTotale:
                    nemicoBersaglio.vita = nemicoBersaglio.vitaTotale
                attaccoDiColco.append(nemicoBersaglio)
                attaccoDiColco.append(GlobalVar.dannoTecniche[azione - 1])
                attaccoDiColco.append("")
            # scossa++
            if azione == 18 and dati[10] >= costoTecnicaUsata:
                danno = GlobalVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = danno - nemicoBersaglio.difesa
                if dannoEffettivo < 0:
                    dannoEffettivo = 0
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
                if (abs(nemicoBersaglio.x - rx) == abs(nemicoBersaglio.y - ry)) and (
                        nemicoBersaglio.x != rx) and (nemicoBersaglio.y != ry):
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
            if dati[10] >= costoTecnicaUsata:
                azioneEseguita = True
                attaccoDiColco.append("Colco")
                attaccoDiColco.append(-costoTecnicaUsata)
                attaccoDiColco.append("")
                dati[10] -= costoTecnicaUsata
            # freccia
            if azione == 4 and dati[10] >= costoTecnicaUsata:
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                danno = GlobalVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    attaccoDiColco.append(nemico)
                    dannoEffettivo = danno - nemico.difesa
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
            # tempesta
            if azione == 5 and dati[10] >= costoTecnicaUsata:
                if ralloVisto:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                danno = GlobalVar.dannoTecniche[azione - 1]
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if nemico != "Rallo":
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = danno - nemico.difesa
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = danno - nemicoBersaglio.difesa
                if dannoEffettivo < 0:
                    dannoEffettivo = 0
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # freccia+
            if azione == 10 and dati[10] >= costoTecnicaUsata:
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                danno = GlobalVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    attaccoDiColco.append(nemico)
                    dannoEffettivo = danno - nemico.difesa
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
            # tempesta+
            if azione == 15 and dati[10] >= costoTecnicaUsata:
                if ralloVisto:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                danno = GlobalVar.dannoTecniche[azione - 1]
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if nemico != "Rallo":
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = danno - nemico.difesa
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = danno - nemicoBersaglio.difesa
                if dannoEffettivo < 0:
                    dannoEffettivo = 0
                attaccoDiColco.append(-dannoEffettivo)
                attaccoDiColco.append("")
            # freccia++
            if azione == 19 and dati[10] >= costoTecnicaUsata:
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                danno = GlobalVar.dannoTecniche[azione - 1]
                if danno < 0:
                    danno = 0
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    attaccoDiColco.append(nemico)
                    dannoEffettivo = danno - nemico.difesa
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
            # tempesta++
            if azione == 20 and dati[10] >= costoTecnicaUsata:
                if ralloVisto:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                danno = GlobalVar.dannoTecniche[azione - 1]
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if nemico != "Rallo":
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = danno - nemico.difesa
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                listaNemiciAttaccatiADistanzaRobo.append(nemicoBersaglio)
                attaccoDiColco.append(nemicoBersaglio)
                dannoEffettivo = danno - nemicoBersaglio.difesa
                if dannoEffettivo < 0:
                    dannoEffettivo = 0
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
                if (abs(nemicoBersaglio.x - rx) == abs(nemicoBersaglio.y - ry)) and (
                        nemicoBersaglio.x != rx) and (nemicoBersaglio.y != ry):
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
            # rimuovo Rallo dagli ostacoli se è nella stessa casella di Colco
            if rx == x and ry == y:
                i = 0
                while i < len(vetNemiciSoloConXeY):
                    if vetNemiciSoloConXeY[i] == x and vetNemiciSoloConXeY[i + 1] == y:
                        del vetNemiciSoloConXeY[i + 1]
                        del vetNemiciSoloConXeY[i]
                        break
                    i += 2
            percorsoTrovato = pathFinding(rx, ry, nemicoBersaglio.x, nemicoBersaglio.y, vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato and percorsoTrovato != "arrivato":
                if len(percorsoTrovato) >= 4:
                    if percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry:
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
        return azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco
    else:
        ralloAccanto = False
        ralloVisto = False
        if (rx == x and ry == y) or (rx + GlobalVar.gpx == x and ry == y) or (rx - GlobalVar.gpx == x and ry == y) or (rx == x and ry + GlobalVar.gpy == y) or (rx == x and ry - GlobalVar.gpy == y):
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
                    if dati[10] >= costoTecnicaUsata and not (azione == 12 and dati[123] > 0) and not (azione == 13 and dati[124] > 0):
                        azioneEseguita = True
                        attaccoDiColco.append("Colco")
                        attaccoDiColco.append(-costoTecnicaUsata)
                        attaccoDiColco.append("")
                        dati[10] -= costoTecnicaUsata
                    # scossa
                    if azione == 1 and dati[10] >= costoTecnicaUsata:
                        danno = GlobalVar.dannoTecniche[azione - 1] - dif
                        if danno < 0:
                            danno = 0
                        dati[5] -= danno
                        if dati[5] < 0:
                            dati[5] = 0
                        attaccoDiColco.append("Rallo")
                        dannoEffettivo = danno
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                    # cura
                    if azione == 2 and dati[10] >= costoTecnicaUsata:
                        dati[5] += GlobalVar.dannoTecniche[azione - 1]
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(GlobalVar.dannoTecniche[azione - 1])
                        attaccoDiColco.append("")
                    # antidoto
                    if azione == 3 and dati[10] >= costoTecnicaUsata:
                        dati[121] = False
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(0)
                        attaccoDiColco.append("antidoto")
                    # cura+
                    if azione == 8 and dati[10] >= costoTecnicaUsata:
                        dati[5] += GlobalVar.dannoTecniche[azione - 1]
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(GlobalVar.dannoTecniche[azione - 1])
                        attaccoDiColco.append("")
                    # scossa+
                    if azione == 9 and dati[10] >= costoTecnicaUsata:
                        danno = GlobalVar.dannoTecniche[azione - 1] - dif
                        if danno < 0:
                            danno = 0
                        dati[5] -= danno
                        if dati[5] < 0:
                            dati[5] = 0
                        attaccoDiColco.append("Rallo")
                        dannoEffettivo = danno
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
                    # attP
                    if azione == 12 and dati[10] >= costoTecnicaUsata and dati[123] <= 0:
                        dati[123] = GlobalVar.dannoTecniche[azione - 1]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(0)
                        attaccoDiColco.append("attP")
                    # difP
                    if azione == 13 and dati[10] >= costoTecnicaUsata and dati[124] <= 0:
                        dati[124] = GlobalVar.dannoTecniche[azione - 1]
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(0)
                        attaccoDiColco.append("difP")
                    # cura++
                    if azione == 16 and dati[10] >= costoTecnicaUsata:
                        dati[5] += GlobalVar.dannoTecniche[azione - 1]
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        attaccoDiColco.append("Rallo")
                        attaccoDiColco.append(GlobalVar.dannoTecniche[azione - 1])
                        attaccoDiColco.append("")
                    # scossa++
                    if azione == 18 and dati[10] >= costoTecnicaUsata:
                        danno = GlobalVar.dannoTecniche[azione - 1] - dif
                        if danno < 0:
                            danno = 0
                        dati[5] -= danno
                        if dati[5] < 0:
                            dati[5] = 0
                        attaccoDiColco.append("Rallo")
                        dannoEffettivo = danno
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
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
                        if (abs(x - rx) == abs(y - ry)) and (
                                x != rx) and (y != ry):
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
                if dati[10] >= costoTecnicaUsata:
                    azioneEseguita = True
                    attaccoDiColco.append("Colco")
                    attaccoDiColco.append(-costoTecnicaUsata)
                    attaccoDiColco.append("")
                    dati[10] -= costoTecnicaUsata
                # freccia
                if azione == 4 and dati[10] >= costoTecnicaUsata:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                # tempesta
                if azione == 5 and dati[10] >= costoTecnicaUsata:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                    danno = GlobalVar.dannoTecniche[azione - 1]
                    for nemico in nemiciVistiDaColco:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                    if nemicoBersaglio:
                        nemicoBersaglio.danneggia(danno, "Colco")
                    for nemico in listaNemiciAttaccatiADistanzaRobo:
                        if nemico != "Rallo":
                            dannoEffettivo = danno - nemico.difesa
                            if dannoEffettivo < 0:
                                dannoEffettivo = 0
                            attaccoDiColco.append(-dannoEffettivo)
                            attaccoDiColco.append("")
                # freccia+
                if azione == 10 and dati[10] >= costoTecnicaUsata:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                # tempesta+
                if azione == 15 and dati[10] >= costoTecnicaUsata:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                    danno = GlobalVar.dannoTecniche[azione - 1]
                    for nemico in nemiciVistiDaColco:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                    if nemicoBersaglio:
                        nemicoBersaglio.danneggia(danno, "Colco")
                    for nemico in listaNemiciAttaccatiADistanzaRobo:
                        if nemico != "Rallo":
                            attaccoDiColco.append(nemico)
                            dannoEffettivo = danno - nemico.difesa
                            if dannoEffettivo < 0:
                                dannoEffettivo = 0
                            attaccoDiColco.append(-dannoEffettivo)
                            attaccoDiColco.append("")
                # freccia++
                if azione == 19 and dati[10] >= costoTecnicaUsata:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                # tempesta++
                if azione == 20 and dati[10] >= costoTecnicaUsata:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                    danno = GlobalVar.dannoTecniche[azione - 1]
                    for nemico in nemiciVistiDaColco:
                        listaNemiciAttaccatiADistanzaRobo.append(nemico)
                        nemico.danneggia(danno, "Colco")
                    if nemicoBersaglio:
                        nemicoBersaglio.danneggia(danno, "Colco")
                    for nemico in listaNemiciAttaccatiADistanzaRobo:
                        if nemico != "Rallo":
                            attaccoDiColco.append(nemico)
                            dannoEffettivo = danno - nemico.difesa
                            if dannoEffettivo < 0:
                                dannoEffettivo = 0
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
                    if (abs(x - rx) == abs(y - ry)) and (
                            x != rx) and (y != ry):
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
                if abs(rx - x) == GlobalVar.gpx and abs(ry - y) == GlobalVar.gpy and ((vx == rx + GlobalVar.gpx and vy == ry) or (vx == rx - GlobalVar.gpx and vy == ry) or (vx == rx and vy == ry + GlobalVar.gpy) or (vx == rx and vy == ry - GlobalVar.gpy)):
                    azioneEseguita = True
                    if vx == rx + GlobalVar.gpx and vy == ry:
                        nrob = 1
                    elif vx == rx - GlobalVar.gpx and vy == ry:
                        nrob = 2
                    elif vy == ry + GlobalVar.gpy and vx == rx:
                        nrob = 3
                    elif vy == ry - GlobalVar.gpy and vx == rx:
                        nrob = 4
                    sposta = True
                else:
                    percorsoTrovato = pathFinding(rx, ry, x, y, vetNemiciSoloConXeY, caseviste)
                    if percorsoTrovato and percorsoTrovato != "arrivato":
                        if len(percorsoTrovato) >= 4:
                            if percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry:
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
        if suAlleato == 2:
            if dati[10] >= costoTecnicaUsata:
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
            if azione == 5 and dati[10] >= costoTecnicaUsata:
                if ralloVisto:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                danno = GlobalVar.dannoTecniche[azione - 1]
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if nemico != "Rallo":
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = danno - nemico.difesa
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # tempesta+
            if azione == 15 and dati[10] >= costoTecnicaUsata:
                if ralloVisto:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                danno = GlobalVar.dannoTecniche[azione - 1]
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if nemico != "Rallo":
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = danno - nemico.difesa
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
            # tempesa++
            if azione == 20 and dati[10] >= costoTecnicaUsata:
                if ralloVisto:
                    listaNemiciAttaccatiADistanzaRobo.append("Rallo")
                    danno = GlobalVar.dannoTecniche[azione - 1] - dif
                    if danno < 0:
                        danno = 0
                    dati[5] -= danno
                    if dati[5] < 0:
                        dati[5] = 0
                    attaccoDiColco.append("Rallo")
                    dannoEffettivo = danno
                    if dannoEffettivo < 0:
                        dannoEffettivo = 0
                    attaccoDiColco.append(-dannoEffettivo)
                    attaccoDiColco.append("")
                danno = GlobalVar.dannoTecniche[azione - 1]
                for nemico in nemiciVistiDaColco:
                    listaNemiciAttaccatiADistanzaRobo.append(nemico)
                    nemico.danneggia(danno, "Colco")
                if nemicoBersaglio:
                    nemicoBersaglio.danneggia(danno, "Colco")
                for nemico in listaNemiciAttaccatiADistanzaRobo:
                    if nemico != "Rallo":
                        attaccoDiColco.append(nemico)
                        dannoEffettivo = danno - nemico.difesa
                        if dannoEffettivo < 0:
                            dannoEffettivo = 0
                        attaccoDiColco.append(-dannoEffettivo)
                        attaccoDiColco.append("")
        return azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco


def movrobo(x, y, vx, vy, rx, ry, stanza, chiamarob, dati, porte, cofanetti, listaNemici, nmost, difesa, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggi, caseviste):
    robo = True
    nrx = 0
    nry = 0
    raffreddamento = False
    ricarica1 = False
    ricarica2 = False
    listaNemiciAttaccatiADistanzaRobo = []
    tecnicaUsata = False
    attaccoDiColco = []
    nemiciVistiDaColco = []

    # burocrazia
    carim = False

    # vetDatiNemici = [vita, x, y, vitaTot, stato]
    nrob = 0
    sposta = False
    # movimento robot
    if chiamarob:
        azioneEseguita = False
        if abs(rx - x) == GlobalVar.gpx and abs(ry - y) == GlobalVar.gpy and ((vx == rx + GlobalVar.gpx and vy == ry) or (vx == rx - GlobalVar.gpx and vy == ry) or (vx == rx and vy == ry + GlobalVar.gpy) or (vx == rx and vy == ry - GlobalVar.gpy)):
            if vx == rx + GlobalVar.gpx and vy == ry:
                nrob = 1
            elif vx == rx - GlobalVar.gpx and vy == ry:
                nrob = 2
            elif vy == ry + GlobalVar.gpy and vx == rx:
                nrob = 3
            elif vy == ry - GlobalVar.gpy and vx == rx:
                nrob = 4
            sposta = True
            azioneEseguita = True
        else:
            vetNemiciSoloConXeY = []
            for nemico in listaNemici:
                vetNemiciSoloConXeY.append(nemico.x)
                vetNemiciSoloConXeY.append(nemico.y)
            for personaggio in listaPersonaggi:
                if not personaggio.mantieniSempreASchermo:
                    vetNemiciSoloConXeY.append(personaggio.x)
                    vetNemiciSoloConXeY.append(personaggio.y)
            percorsoTrovato = pathFinding(rx, ry, x, y, vetNemiciSoloConXeY, caseviste)
            if percorsoTrovato and percorsoTrovato != "arrivato":
                if len(percorsoTrovato) >= 4:
                    if percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry:
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
        if azioneEseguita and sposta:
            tecnicaUsata = "spostamento"
            ultimoObbiettivoColco = []
            ultimoObbiettivoColco.append("Telecomando")
            ultimoObbiettivoColco.append(x)
            ultimoObbiettivoColco.append(y)
        else:
            ultimoObbiettivoColco = []
    else:
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, difesa)

        # trova i nemici visti
        vistaRobo = GlobalVar.gpx * GlobalVar.vistaRobo
        caselleAttaccabili = trovacasattaccabili(rx, ry, stanza, porte, cofanetti, listaPersonaggi, vistaRobo)
        k = 0
        while k < len(caselleAttaccabili):
            if caselleAttaccabili[k + 2]:
                for nemico in listaNemici:
                    if caselleAttaccabili[k] == nemico.x and caselleAttaccabili[k + 1] == nemico.y and nemico.vita > 0:
                        listaNemici.remove(nemico)
                        nemiciVistiDaColco.append(nemico)
                        break
            k += 3

        # dati: tecniche(11-30) / condizioni(81-100) / gambit(101-120) / pvRallo(5) / veleno(121) / attP(123) / difP(124) / peColco(10) / surriscalda(122) / velP(125) / efficienza(126)
        # in gambit: prime 10 -> condizioni, ultime 10 -> tecniche
        #            condizioni = intero da 1 a 20: pvR<80, pvR<50, pvR<30, velenoR, surrisC, peC<80, peC<50, peC<30, sempreR, sempreC, nemicoCasuale, nemicoVicino, nemicoLontano, pvN<80, pvN<50, pvN<30, nemico-pv, numN>1, numN>4, numN>7
        #            tecniche = intero da 1 a 20: scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesta++

        # controllo se la condizione è rispettata
        azioneEseguita = False
        i = 101
        while i <= 110 and not azioneEseguita:
            if dati[i] != 0 and dati[i + 10] != 0 and dati[10] >= GlobalVar.costoTecniche[dati[i + 10] - 1]:
                # azioni su alleati
                # pv rallo < 80
                if dati[i] == 1:
                    if dati[5] < pvtot / float(100) * 80 and dati[5] >= 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # pv rallo < 50
                if dati[i] == 2:
                    if dati[5] < pvtot / float(100) * 50 and dati[5] > 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # pv rallo < 30
                if dati[i] == 3:
                    if dati[5] < pvtot / float(100) * 30 and dati[5] > 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # rallo avvelenato
                if dati[i] == 4:
                    if dati[121]:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # colco surriscaldato
                if dati[i] == 5:
                    if dati[122] > 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # pe colco < 80
                if dati[i] == 6:
                    if dati[10] < entot / float(100) * 80 and dati[10] > 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # pe colco < 50
                if dati[i] == 7:
                    if dati[10] < entot / float(100) * 50 and dati[10] > 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # pe colco < 30
                if dati[i] == 8:
                    if dati[10] < entot / float(100) * 30 and dati[10] > 0:
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # sempre rallo
                if dati[i] == 9 and not (dati[i + 10] == 12 and dati[123] > 0) and not (dati[i + 10] == 13 and dati[124] > 0):
                    if (dati[i + 10] != 12 and dati[i + 10] != 13) or (dati[i + 10] == 12 and dati[123] == 0) or (dati[i + 10] == 13 and dati[124] == 0):
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 1, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # sempre colco
                if dati[i] == 10 and not (dati[i + 10] == 11 and dati[125] > 0) and not (dati[i + 10] == 14 and dati[126] > 0):
                    if (dati[i + 10] != 11 and dati[i + 10] != 14) or (dati[i + 10] == 11 and dati[125] == 0) or (dati[i + 10] == 14 and dati[126] == 0):
                        azioneEseguita, nrob, sposta, dati, nemiciVistiDaColco, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, False, dati[i + 10], 2, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                # azioni su nemici
                if nmost > 0 and len(nemiciVistiDaColco) > 0:
                    nemicoBersaglio = False
                    # nemico a caso
                    if dati[i] == 11:
                        if obbiettivoCasualeColco:
                            for nemico in nemiciVistiDaColco:
                                if nemico.x == obbiettivoCasualeColco.x and nemico.y == obbiettivoCasualeColco.y:
                                    nemicoBersaglio = obbiettivoCasualeColco
                                    break
                        elif not nemicoBersaglio and len(nemiciVistiDaColco) > 0:
                            nemicoBersaglio = nemiciVistiDaColco[random.randint(0, (len(nemiciVistiDaColco) - 1))]
                            obbiettivoCasualeColco = nemicoBersaglio
                        else:
                            obbiettivoCasualeColco = False
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                            if len(attaccoDiColco) > 0:
                                obbiettivoCasualeColco = False
                    # nemico vicino
                    if dati[i] == 12:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if abs(nemico.x - rx) <= (GlobalVar.gpx * 2) and abs(nemico.y - ry) <= (GlobalVar.gpy * 2):
                                if primoMostro:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # nemico lontano
                    if dati[i] == 13:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if abs(nemico.x - rx) >= (GlobalVar.gpx * 3) or abs(nemico.y - ry) >= (GlobalVar.gpy * 3):
                                if primoMostro:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # nemico pv < 80
                    if dati[i] == 14:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if nemico.vita < nemico.vitaTotale / float(100) * 80:
                                if primoMostro:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # nemico pv < 50
                    if dati[i] == 15:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if nemico.vita < nemico.vitaTotale / float(100) * 50:
                                if primoMostro:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # nemico pv < 30
                    if dati[i] == 16:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if nemico.vita < nemico.vitaTotale / float(100) * 30:
                                if primoMostro:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                                    primoMostro = False
                                elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                    distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                    nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # nemico con meno pv
                    if dati[i] == 17:
                        distMin = False
                        pvMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if primoMostro:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                pvMin = nemico.vita
                                nemicoBersaglio = nemico
                                primoMostro = False
                            elif nemico.vita < pvMin or (nemico.vita == pvMin and abs(nemico.x - rx) + abs(nemico.y - ry) < distMin):
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                pvMin = nemico.vita
                                nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # numero nemici > 1
                    if dati[i] == 18 and len(nemiciVistiDaColco) > 1:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if primoMostro:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                nemicoBersaglio = nemico
                                primoMostro = False
                            elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # numero nemici > 4
                    if dati[i] == 19 and len(nemiciVistiDaColco) > 4:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if primoMostro:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                nemicoBersaglio = nemico
                                primoMostro = False
                            elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
                                ultimoObbiettivoColco = []
                    # numero nemici > 7
                    if dati[i] == 20 and len(nemiciVistiDaColco) > 7:
                        distMin = False
                        primoMostro = True
                        for nemico in nemiciVistiDaColco:
                            if primoMostro:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                nemicoBersaglio = nemico
                                primoMostro = False
                            elif abs(nemico.x - rx) + abs(nemico.y - ry) < distMin:
                                distMin = abs(nemico.x - rx) + abs(nemico.y - ry)
                                nemicoBersaglio = nemico
                        if nemicoBersaglio:
                            nemiciVistiDaColco.remove(nemicoBersaglio)
                            azioneEseguita, nemicoBersaglio, nemiciVistiDaColco, nrob, sposta, raffreddamento, ricarica1, ricarica2, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco = eseguiAzione(rx, ry, nemicoBersaglio, dati[i + 10], False, nemiciVistiDaColco, dati, caselleAttaccabili, difesa, vx, vy, x, y, listaNemiciAttaccatiADistanzaRobo, attaccoDiColco, listaPersonaggi, caseviste)
                            nemiciVistiDaColco.append(nemicoBersaglio)
                            ultimoObbiettivoColco = []
                            if nemicoBersaglio.vita > 0:
                                ultimoObbiettivoColco.append("Nemico")
                                ultimoObbiettivoColco.append(nemicoBersaglio.x)
                                ultimoObbiettivoColco.append(nemicoBersaglio.y)
                            else:
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
            i += 1

        if not azioneEseguita and len(ultimoObbiettivoColco) > 0:
            vetNemiciSoloConXeY = []
            if ultimoObbiettivoColco[0] == "Telecomando":
                vetNemiciSoloConXeY.append(x)
                vetNemiciSoloConXeY.append(y)
                for nemico in listaNemici:
                    vetNemiciSoloConXeY.append(nemico.x)
                    vetNemiciSoloConXeY.append(nemico.y)
                for personaggio in listaPersonaggi:
                    if not personaggio.mantieniSempreASchermo:
                        vetNemiciSoloConXeY.append(personaggio.x)
                        vetNemiciSoloConXeY.append(personaggio.y)
            elif ultimoObbiettivoColco[0] == "Nemico":
                vetNemiciSoloConXeY.append(x)
                vetNemiciSoloConXeY.append(y)
                for nemico in listaNemici:
                    if not (ultimoObbiettivoColco[1] == nemico.x and ultimoObbiettivoColco[2] == nemico.y):
                        vetNemiciSoloConXeY.append(nemico.x)
                        vetNemiciSoloConXeY.append(nemico.y)
                for personaggio in listaPersonaggi:
                    if not personaggio.mantieniSempreASchermo:
                        vetNemiciSoloConXeY.append(personaggio.x)
                        vetNemiciSoloConXeY.append(personaggio.y)

            if (abs(rx - ultimoObbiettivoColco[1]) == GlobalVar.gpx and abs(ry - ultimoObbiettivoColco[2]) == 0) or (abs(rx - ultimoObbiettivoColco[1]) == 0 and abs(ry - ultimoObbiettivoColco[2]) == GlobalVar.gpy):
                posizioneOstacolata = False
                for nemico in listaNemici:
                    if ultimoObbiettivoColco[1] == nemico.x and ultimoObbiettivoColco[2] == nemico.y:
                        posizioneOstacolata = True
                        break
                if not posizioneOstacolata:
                    if rx + GlobalVar.gpx == ultimoObbiettivoColco[1] and ry == ultimoObbiettivoColco[2]:
                        nrob = 1
                    if rx - GlobalVar.gpx == ultimoObbiettivoColco[1] and ry == ultimoObbiettivoColco[2]:
                        nrob = 2
                    if rx == ultimoObbiettivoColco[1] and ry + GlobalVar.gpy == ultimoObbiettivoColco[2]:
                        nrob = 3
                    if rx == ultimoObbiettivoColco[1] and ry - GlobalVar.gpy == ultimoObbiettivoColco[2]:
                        nrob = 4
                    sposta = True
                    azioneEseguita = True
            else:
                percorsoTrovato = pathFinding(rx, ry, ultimoObbiettivoColco[1], ultimoObbiettivoColco[2], vetNemiciSoloConXeY, caseviste)
                if percorsoTrovato and percorsoTrovato != "arrivato":
                    if len(percorsoTrovato) >= 4:
                        if percorsoTrovato[len(percorsoTrovato) - 4] != rx or percorsoTrovato[len(percorsoTrovato) - 3] != ry:
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
            if azioneEseguita and sposta:
                tecnicaUsata = "spostamento"
            else:
                ultimoObbiettivoColco = []

    for nemico in nemiciVistiDaColco:
        listaNemici.append(nemico)
    if len(listaNemiciAttaccatiADistanzaRobo) == 0:
        listaNemiciAttaccatiADistanzaRobo = False

    # spostamento
    if sposta:
        if nrob == 1:
            if rx + GlobalVar.gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = GlobalVar.gpx
                nry = 0
        if nrob == 2:
            if rx - GlobalVar.gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = -GlobalVar.gpx
                nry = 0
        if nrob == 3:
            if rx == x and ry + GlobalVar.gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = GlobalVar.gpy
        if nrob == 4:
            if rx == x and ry - GlobalVar.gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = -GlobalVar.gpy

    # alcuni sono inutili!!!
    rx, ry, stanza, carim, cambiosta = muri_porte(rx, ry, nrx, nry, stanza, carim, False, robo, porte, cofanetti, listaPersonaggi)
    return rx, ry, nrob, dati, listaNemici, raffreddamento, ricarica1, ricarica2, azioneEseguita, listaNemiciAttaccatiADistanzaRobo, tecnicaUsata, attaccoDiColco, ultimoObbiettivoColco, obbiettivoCasualeColco
