# -*- coding: utf-8 -*-

from NemicoObj import *
from PersonaggioObj import *


def salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggiTotali):
    # conversione della posizione in caselle
    dati[2] = dati[2] // GlobalVarG2.gpx
    dati[3] = dati[3] // GlobalVarG2.gpy
    dati[134] = dati[134] // GlobalVarG2.gpx
    dati[135] = dati[135] // GlobalVarG2.gpy
    i = porteini
    while i <= portefin:
        j = 0
        while j < len(porte):
            if dati[i] == porte[j] and dati[i + 1] == porte[j + 1] and dati[i + 2] == porte[j + 2]:
                dati[i + 3] = porte[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // GlobalVarG2.gpx
        dati[i + 2] = dati[i + 2] // GlobalVarG2.gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        j = 0
        while j < len(cofanetti):
            if dati[i] == cofanetti[j] and dati[i + 1] == cofanetti[j + 1] and dati[i + 2] == cofanetti[j + 2]:
                dati[i + 3] = cofanetti[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // GlobalVarG2.gpx
        dati[i + 2] = dati[i + 2] // GlobalVarG2.gpy
        i = i + 4

    scrivi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
    for i in range(0, len(dati)):
        scrivi.write("%i_" % dati[i])
    scrivi.write("\n")
    for nemico in listaNemiciTotali:
        scrivi.write("%s_" % nemico.tipo)
        scrivi.write("%i_" % nemico.stanzaDiAppartenenza)
        scrivi.write("%i_" % (nemico.x // GlobalVarG2.gpx))
        scrivi.write("%i_" % (nemico.y // GlobalVarG2.gpy))
        scrivi.write("%i_" % nemico.vita)
        scrivi.write("%i_" % nemico.avvelenato)
        scrivi.write("%i_" % nemico.appiccicato)
        if nemico.stanzaDiAppartenenza == dati[1]:
            scrivi.write("%i_" % nemico.mosseRimaste)
        else:
            scrivi.write("0_")
        scrivi.write("%s_" % nemico.direzione)
        scrivi.write("%i_" % nemico.xObbiettivo)
        scrivi.write("%i_" % nemico.yObbiettivo)
        scrivi.write("%i_" % nemico.xPosizioneUltimoBersaglio)
        scrivi.write("%i_" % nemico.yPosizioneUltimoBersaglio)
        scrivi.write("%i_" % nemico.numeroMovimento)
        scrivi.write("%i_" % nemico.triggerato)
        scrivi.write("[_")
        for direzione in nemico.percorso:
            scrivi.write("%s_" % direzione)
        scrivi.write("]_")
    scrivi.write("\n")
    i = 0
    while i < len(vitaesca):
        scrivi.write("%i_" % vitaesca[i])
        scrivi.write("%i_" % vitaesca[i + 1])
        scrivi.write("%i_" % (vitaesca[i + 2] // GlobalVarG2.gpx))
        scrivi.write("%i_" % (vitaesca[i + 3] // GlobalVarG2.gpy))
        i += 4
    scrivi.write("\n")
    i = 0
    while i < len(vettoreDenaro):
        scrivi.write("%i_" % vettoreDenaro[i])
        scrivi.write("%i_" % (vettoreDenaro[i + 1] // GlobalVarG2.gpx))
        scrivi.write("%i_" % (vettoreDenaro[i + 2] // GlobalVarG2.gpy))
        i += 3
    scrivi.write("\n")
    i = 0
    while i < len(stanzeGiaVisitate):
        scrivi.write("%i_" % stanzeGiaVisitate[i])
        i += 1
    scrivi.write("\n")
    if ultimoObbiettivoColco and ultimoObbiettivoColco[0] == "Telecomando":
        scrivi.write("%s_" % ultimoObbiettivoColco[0])
    elif ultimoObbiettivoColco and len(ultimoObbiettivoColco) > 0:
        scrivi.write("%i_" % ultimoObbiettivoColco[0])
        scrivi.write("%i_" % ultimoObbiettivoColco[1])
    scrivi.write("\n")
    if obbiettivoCasualeColco:
        scrivi.write("%i_" % obbiettivoCasualeColco.stanzaDiAppartenenza)
        scrivi.write("%i_" % obbiettivoCasualeColco.x)
        scrivi.write("%i_" % obbiettivoCasualeColco.y)
    scrivi.write("\n")
    for personaggio in listaPersonaggiTotali:
        scrivi.write("%i_" % (personaggio.x // GlobalVarG2.gpx))
        scrivi.write("%i_" % (personaggio.y // GlobalVarG2.gpy))
        scrivi.write("%s_" % personaggio.direzione)
        scrivi.write("%s_" % personaggio.tipo)
        scrivi.write("%i_" % personaggio.stanzaDiAppartenenza)
        scrivi.write("%i_" % personaggio.avanzamentoStoria)
        scrivi.write("[_")
        for direzione in personaggio.percorso:
            scrivi.write("%s_" % direzione)
        scrivi.write("]_")
        scrivi.write("%i_" % personaggio.numeroMovimento)
    scrivi.close()

    # conversione della posizione in pixel
    dati[2] = dati[2] * GlobalVarG2.gpx
    dati[3] = dati[3] * GlobalVarG2.gpy
    dati[134] = dati[134] * GlobalVarG2.gpx
    dati[135] = dati[135] * GlobalVarG2.gpy
    i = porteini
    while i <= portefin:
        dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
        dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
        dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
        i = i + 4


def caricaPartita(n, lunghezzadati, porteini, portefin, cofaniini, cofanifin, background=False, mostraErrori=True):
    errore = False
    tipoErrore = 0

    dati = []
    ultimoObbiettivoColco = []
    obbiettivoCasualeColco = False
    listaNemiciTotali = []
    listaEsche = []
    listaMonete = []
    stanzeGiaVisitate = []
    listaPersonaggiTotali = []

    leggi = open("Salvataggi/Salvataggio%i.txt" % n, "r")
    leggifile = leggi.read()
    leggi.close()
    datiTotali = leggifile.split("\n")
    if not (len(datiTotali) == 1 and datiTotali[0] == ""):
        if len(datiTotali) == 8:
            dati = datiTotali[0].split("_")
            dati.pop(len(dati) - 1)
            if len(dati) == 0 or len(dati) != lunghezzadati:
                errore = True
            else:
                for i in range(0, len(dati)):
                    try:
                        dati[i] = int(dati[i])
                    except ValueError:
                        errore = True
                        break
                if not errore:
                    # conversione della posizione in pixel
                    dati[2] = dati[2] * GlobalVarG2.gpx
                    dati[3] = dati[3] * GlobalVarG2.gpy
                    dati[134] = dati[134] * GlobalVarG2.gpx
                    dati[135] = dati[135] * GlobalVarG2.gpy
                    i = porteini
                    while i <= portefin:
                        dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
                        dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
                        i = i + 4
                    i = cofaniini
                    while i <= cofanifin:
                        dati[i + 1] = dati[i + 1] * GlobalVarG2.gpx
                        dati[i + 2] = dati[i + 2] * GlobalVarG2.gpy
                        i = i + 4
            datiNemici = datiTotali[1].split("_")
            datiNemici.pop(len(datiNemici) - 1)
            try:
                i = 0
                while i < len(datiNemici):
                    j = i + 15 + 1
                    while j < len(datiNemici):
                        if datiNemici[j] == "]":
                            datiNemici.pop(j)
                            datiNemici.pop(i + 15)
                            percorsoNemico = []
                            k = i + 15
                            while k < j - 1:
                                percorsoNemico.append(datiNemici.pop(i + 15))
                                k += 1
                            datiNemici.insert(i + 15, percorsoNemico)
                            break
                        j += 1
                    i += 16
            except ValueError:
                errore = True
            if len(datiNemici) % 16 != 0:
                errore = True
            else:
                i = 0
                while i < len(datiNemici):
                    try:
                        nemico = NemicoObj(GlobalVarG2.gsx // 32 * int(datiNemici[i + 2]), GlobalVarG2.gsy // 18 * int(datiNemici[i + 3]), datiNemici[i + 8], datiNemici[i], int(datiNemici[i + 1]), datiNemici[i + 15], int(datiNemici[i + 13]), bool(int(datiNemici[i + 14])))
                        nemico.vita = int(datiNemici[i + 4])
                        nemico.avvelenato = bool(int(datiNemici[i + 5]))
                        nemico.appiccicato = bool(int(datiNemici[i + 6]))
                        nemico.mosseRimaste = int(datiNemici[i + 7])
                        nemico.xObbiettivo = int(datiNemici[i + 9])
                        nemico.yObbiettivo = int(datiNemici[i + 10])
                        nemico.xPosizioneUltimoBersaglio = int(datiNemici[i + 11])
                        nemico.yPosizioneUltimoBersaglio = int(datiNemici[i + 12])
                        listaNemiciTotali.append(nemico)
                    except ValueError:
                        errore = True
                        break
                    i += 16
            listaEsche = datiTotali[2].split("_")
            listaEsche.pop(len(listaEsche) - 1)
            if len(listaEsche) % 4 != 0:
                errore = True
            else:
                i = 0
                while i < len(listaEsche):
                    try:
                        listaEsche[i] = int(listaEsche[i])
                        listaEsche[i + 1] = int(listaEsche[i + 1])
                        listaEsche[i + 2] = int(GlobalVarG2.gpx * listaEsche[i + 2])
                        listaEsche[i + 3] = int(GlobalVarG2.gpy * listaEsche[i + 3])
                    except ValueError:
                        errore = True
                        break
                    i += 4
            listaMonete = datiTotali[3].split("_")
            listaMonete.pop(len(listaMonete) - 1)
            if len(listaMonete) % 3 != 0:
                errore = True
            else:
                i = 0
                while i < len(listaMonete):
                    try:
                        listaMonete[i] = int(listaMonete[i])
                        listaMonete[i + 1] = int(GlobalVarG2.gpx * int(listaMonete[i + 1]))
                        listaMonete[i + 2] = int(GlobalVarG2.gpy * int(listaMonete[i + 2]))
                    except ValueError:
                        errore = True
                        break
                    i += 3
            stanzeGiaVisitate = datiTotali[4].split("_")
            stanzeGiaVisitate.pop(len(stanzeGiaVisitate) - 1)
            i = 0
            while i < len(stanzeGiaVisitate):
                try:
                    stanzeGiaVisitate[i] = int(stanzeGiaVisitate[i])
                except ValueError:
                    errore = True
                    break
                i += 1
            ultimoObbiettivoColco = datiTotali[5].split("_")
            ultimoObbiettivoColco.pop(len(ultimoObbiettivoColco) - 1)
            if len(ultimoObbiettivoColco) > 0 and ultimoObbiettivoColco[0] != "Telecomando":
                try:
                    ultimoObbiettivoColco[0] = int(ultimoObbiettivoColco[0])
                    ultimoObbiettivoColco[1] = int(ultimoObbiettivoColco[1])
                except ValueError:
                    errore = True
            obbiettivoCasualeColcoVet = datiTotali[6].split("_")
            obbiettivoCasualeColcoVet.pop(len(obbiettivoCasualeColcoVet) - 1)
            if len(obbiettivoCasualeColcoVet) > 0:
                try:
                    for nemico in listaNemiciTotali:
                        if nemico.stanzaDiAppartenenza == int(obbiettivoCasualeColcoVet[0]) and nemico.x == int(obbiettivoCasualeColcoVet[1]) and nemico.y == int(obbiettivoCasualeColcoVet[2]):
                            obbiettivoCasualeColco = nemico
                            break
                except ValueError:
                    errore = True
            else:
                obbiettivoCasualeColco = False
            datiPersonaggi = datiTotali[7].split("_")
            datiPersonaggi.pop(len(datiPersonaggi) - 1)
            try:
                i = 0
                while i < len(datiPersonaggi):
                    j = i + 6 + 1
                    while j < len(datiPersonaggi):
                        if datiPersonaggi[j] == "]":
                            datiPersonaggi.pop(j)
                            datiPersonaggi.pop(i + 6)
                            percorsoPersonaggio = []
                            k = i + 6
                            while k < j - 1:
                                percorsoPersonaggio.append(datiPersonaggi.pop(i + 6))
                                k += 1
                            datiPersonaggi.insert(i + 6, percorsoPersonaggio)
                            break
                        j += 1
                    i += 8
            except ValueError:
                errore = True
            if len(datiPersonaggi) % 8 != 0:
                errore = True
            else:
                i = 0
                while i < len(datiPersonaggi):
                    try:
                        personaggio = PersonaggioObj(GlobalVarG2.gsx // 32 * int(datiPersonaggi[i]), GlobalVarG2.gsy // 18 * int(datiPersonaggi[i + 1]), datiPersonaggi[i + 2], datiPersonaggi[i + 3], int(datiPersonaggi[i + 4]), int(datiPersonaggi[i + 5]), datiPersonaggi[i + 6], int(datiPersonaggi[i + 7]))
                        listaPersonaggiTotali.append(personaggio)
                    except ValueError:
                        errore = True
                        break
                    i += 8
        else:
            errore = True
        if errore:
            tipoErrore = 2
            if mostraErrori:
                print "Dati corrotti"
                aggiornaSchermata = True
                indietro = False
                sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                while not indietro:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
                    if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
                        aggiornaSchermata = True
                        pygame.mouse.set_visible(True)
                        GlobalVarG2.mouseVisibile = True
                    if GlobalVarG2.mouseVisibile:
                        if GlobalVarG2.gsx // 32 * 21.5 <= xMouse <= GlobalVarG2.gsx and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                            if GlobalVarG2.mouseBloccato:
                                GlobalVarG2.configuraCursore(False)
                        else:
                            if not GlobalVarG2.mouseBloccato:
                                GlobalVarG2.configuraCursore(True)
                    for event in pygame.event.get():
                        sinistroMouseVecchio = sinistroMouse
                        centraleMouseVecchio = centraleMouse
                        destroMouseVecchio = destroMouse
                        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                        if not sinistroMouseVecchio and sinistroMouse:
                            centraleMouse = False
                            destroMouse = False
                        elif not centraleMouseVecchio and centraleMouse:
                            sinistroMouse = False
                            destroMouse = False
                        elif not destroMouseVecchio and destroMouse:
                            sinistroMouse = False
                            centraleMouse = False
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN:
                            aggiornaSchermata = True
                            if GlobalVarG2.mouseVisibile:
                                pygame.mouse.set_visible(False)
                                GlobalVarG2.mouseVisibile = False
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (GlobalVarG2.mouseVisibile and ((event.type == pygame.MOUSEBUTTONDOWN and destroMouse) or (event.type == pygame.MOUSEBUTTONDOWN and not GlobalVarG2.mouseBloccato and sinistroMouse))):
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                            indietro = True
                        if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                            aggiornaSchermata = True
                            pygame.mouse.set_visible(True)
                            GlobalVarG2.mouseVisibile = True
                    if aggiornaSchermata:
                        aggiornaSchermata = False
                        if background:
                            GlobalVarG2.schermo.blit(background, (0, 0))
                            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 4.7, GlobalVarG2.gsy // 18 * 3.2, GlobalVarG2.gsx // 32 * 22.6, GlobalVarG2.gsy // 18 * 13.6))
                        else:
                            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
                        robograsalva = pygame.transform.scale(GlobalVarG2.robograffff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
                        GlobalVarG2.schermo.blit(robograsalva, (GlobalVarG2.gpx * 7, -GlobalVarG2.gpy * 4.5))
                        pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.nero, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 13.5), (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 13.5), 2)
                        if GlobalVarG2.mouseVisibile:
                            messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
                        else:
                            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
                        messaggio("Slot di memoria danneggiato...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 6.2, GlobalVarG2.gsy // 18 * 14, 100)
                        pygame.display.update()
    else:
        errore = True
        tipoErrore = 1
        if mostraErrori:
            print "Slot vuoto"
            aggiornaSchermata = True
            indietro = False
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            while not indietro:
                xMouse, yMouse = pygame.mouse.get_pos()
                deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
                if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
                    aggiornaSchermata = True
                    pygame.mouse.set_visible(True)
                    GlobalVarG2.mouseVisibile = True
                if GlobalVarG2.mouseVisibile:
                    if GlobalVarG2.gsx // 32 * 21.5 <= xMouse <= GlobalVarG2.gsx and 0 <= yMouse <= GlobalVarG2.gsy // 18 * 2:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                for event in pygame.event.get():
                    sinistroMouseVecchio = sinistroMouse
                    centraleMouseVecchio = centraleMouse
                    destroMouseVecchio = destroMouse
                    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                    if not sinistroMouseVecchio and sinistroMouse:
                        centraleMouse = False
                        destroMouse = False
                    elif not centraleMouseVecchio and centraleMouse:
                        sinistroMouse = False
                        destroMouse = False
                    elif not destroMouseVecchio and destroMouse:
                        sinistroMouse = False
                        centraleMouse = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        aggiornaSchermata = True
                        if GlobalVarG2.mouseVisibile:
                            pygame.mouse.set_visible(False)
                            GlobalVarG2.mouseVisibile = False
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (GlobalVarG2.mouseVisibile and (
                            (event.type == pygame.MOUSEBUTTONDOWN and destroMouse) or (
                            event.type == pygame.MOUSEBUTTONDOWN and not GlobalVarG2.mouseBloccato and sinistroMouse))):
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        indietro = True
                    if (sinistroMouse or centraleMouse or destroMouse) and not GlobalVarG2.mouseVisibile:
                        aggiornaSchermata = True
                        pygame.mouse.set_visible(True)
                        GlobalVarG2.mouseVisibile = True
                if aggiornaSchermata:
                    aggiornaSchermata = False
                    if background:
                        GlobalVarG2.schermo.blit(background, (0, 0))
                        pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (
                        GlobalVarG2.gsx // 32 * 4.7, GlobalVarG2.gsy // 18 * 3.2, GlobalVarG2.gsx // 32 * 22.6,
                        GlobalVarG2.gsy // 18 * 13.6))
                    else:
                        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
                    robograsalva = pygame.transform.scale(GlobalVarG2.robograff,
                                                          (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
                    GlobalVarG2.schermo.blit(robograsalva, (GlobalVarG2.gpx * 7, -GlobalVarG2.gpy * 4.5))
                    pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.nero, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 13.5),
                                     (GlobalVarG2.gpx * 22, GlobalVarG2.gpy * 13.5), 2)
                    if GlobalVarG2.mouseVisibile:
                        messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5,
                                  GlobalVarG2.gsy // 18 * 1, 50)
                    else:
                        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25,
                                  GlobalVarG2.gsy // 18 * 1, 50)
                    messaggio("Slot di memoria vuoto...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.5,
                              GlobalVarG2.gsy // 18 * 14, 100)
                    pygame.display.update()
    if not errore:
        if mostraErrori:
            print "Salvataggio: " + str(n)
            GlobalVarG2.canaleSoundCanzone.stop()
            return dati, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggiTotali
        else:
            return dati, tipoErrore
    else:
        if mostraErrori:
            return False, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, ultimoObbiettivoColco, obbiettivoCasualeColco, listaPersonaggiTotali
        else:
            return False, tipoErrore
