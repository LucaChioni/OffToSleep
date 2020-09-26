# -*- coding: utf-8 -*-

from NemicoObj import *
from PersonaggioObj import *


def salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, listaNemiciTotali, vitaesca, vettoreDenaro, stanzeGiaVisitate, listaPersonaggiTotali):
    # conversione della posizione in caselle
    dati[2] = dati[2] // GlobalVar.gpx
    dati[3] = dati[3] // GlobalVar.gpy
    dati[134] = dati[134] // GlobalVar.gpx
    dati[135] = dati[135] // GlobalVar.gpy
    i = porteini
    while i <= portefin:
        j = 0
        while j < len(porte):
            if dati[i] == porte[j] and dati[i + 1] == porte[j + 1] and dati[i + 2] == porte[j + 2]:
                dati[i + 3] = porte[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // GlobalVar.gpx
        dati[i + 2] = dati[i + 2] // GlobalVar.gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        j = 0
        while j < len(cofanetti):
            if dati[i] == cofanetti[j] and dati[i + 1] == cofanetti[j + 1] and dati[i + 2] == cofanetti[j + 2]:
                dati[i + 3] = cofanetti[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // GlobalVar.gpx
        dati[i + 2] = dati[i + 2] // GlobalVar.gpy
        i = i + 4

    scrivi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
    for i in range(0, len(dati)):
        scrivi.write("%i_" % dati[i])
    scrivi.write("\n")
    for nemico in listaNemiciTotali:
        scrivi.write("%s_" % nemico.tipo)
        scrivi.write("%i_" % nemico.stanzaDiAppartenenza)
        scrivi.write("%i_" % (nemico.x // GlobalVar.gpx))
        scrivi.write("%i_" % (nemico.y // GlobalVar.gpy))
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
        scrivi.write("%i_" % (vitaesca[i + 2] // GlobalVar.gpx))
        scrivi.write("%i_" % (vitaesca[i + 3] // GlobalVar.gpy))
        i += 4
    scrivi.write("\n")
    i = 0
    while i < len(vettoreDenaro):
        scrivi.write("%i_" % vettoreDenaro[i])
        scrivi.write("%i_" % (vettoreDenaro[i + 1] // GlobalVar.gpx))
        scrivi.write("%i_" % (vettoreDenaro[i + 2] // GlobalVar.gpy))
        i += 3
    scrivi.write("\n")
    i = 0
    while i < len(stanzeGiaVisitate):
        scrivi.write("%i_" % stanzeGiaVisitate[i])
        i += 1
    scrivi.write("\n")
    for personaggio in listaPersonaggiTotali:
        scrivi.write("%i_" % (personaggio.x // GlobalVar.gpx))
        scrivi.write("%i_" % (personaggio.y // GlobalVar.gpy))
        scrivi.write("%s_" % personaggio.direzione)
        scrivi.write("%s_" % personaggio.tipo)
        scrivi.write("%i_" % personaggio.stanzaDiAppartenenza)
        scrivi.write("%i_" % personaggio.avanzaStoria)
        scrivi.write("[_")
        for direzione in personaggio.percorso:
            scrivi.write("%s_" % direzione)
        scrivi.write("]_")
        scrivi.write("%i_" % personaggio.numeroMovimento)
    scrivi.close()

    # critta il salvataggio
    # leggi = open("Salvataggi/Salvataggio%i.txt" % n, "r")
    # contenutoFile = leggi.read()
    # leggi.close()
    # encoded_text = contenutoFile.encode('base64')
    # scrivi = open("Salvataggi/Salvataggio%i.txt" % n, "w")
    # scrivi.write(encoded_text)
    # scrivi.close()

    # conversione della posizione in pixel
    dati[2] = dati[2] * GlobalVar.gpx
    dati[3] = dati[3] * GlobalVar.gpy
    dati[134] = dati[134] * GlobalVar.gpx
    dati[135] = dati[135] * GlobalVar.gpy
    i = porteini
    while i <= portefin:
        dati[i + 1] = dati[i + 1] * GlobalVar.gpx
        dati[i + 2] = dati[i + 2] * GlobalVar.gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        dati[i + 1] = dati[i + 1] * GlobalVar.gpx
        dati[i + 2] = dati[i + 2] * GlobalVar.gpy
        i = i + 4


def caricaPartita(n, lunghezzadati, porteini, portefin, cofaniini, cofanifin, canzone, background=False, mostraErrori=True):
    errore = False
    tipoErrore = 0

    dati = []
    listaNemiciTotali = []
    listaEsche = []
    listaMonete = []
    stanzeGiaVisitate = []
    listaPersonaggiTotali = []

    leggi = open("Salvataggi/Salvataggio%i.txt" % n, "r")
    contenutoFile = leggi.read()
    leggi.close()

    # decritta il salvataggio
    datiTotali = [""]
    try:
        # contenutoFile = contenutoFile.decode('base64')
        datiTotali = contenutoFile.split("\n")
    except Exception:
        errore = True
        tipoErrore = 2

    if not errore and not (len(datiTotali) == 1 and datiTotali[0] == ""):
        if len(datiTotali) == 6:
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
                    dati[2] = dati[2] * GlobalVar.gpx
                    dati[3] = dati[3] * GlobalVar.gpy
                    dati[134] = dati[134] * GlobalVar.gpx
                    dati[135] = dati[135] * GlobalVar.gpy
                    i = porteini
                    while i <= portefin:
                        dati[i + 1] = dati[i + 1] * GlobalVar.gpx
                        dati[i + 2] = dati[i + 2] * GlobalVar.gpy
                        i = i + 4
                    i = cofaniini
                    while i <= cofanifin:
                        dati[i + 1] = dati[i + 1] * GlobalVar.gpx
                        dati[i + 2] = dati[i + 2] * GlobalVar.gpy
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
                        nemico = NemicoObj(GlobalVar.gsx // 32 * int(datiNemici[i + 2]), GlobalVar.gsy // 18 * int(datiNemici[i + 3]), datiNemici[i + 8], datiNemici[i], int(datiNemici[i + 1]), datiNemici[i + 15], int(datiNemici[i + 13]), bool(int(datiNemici[i + 14])))
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
                        listaEsche[i + 2] = int(GlobalVar.gpx * listaEsche[i + 2])
                        listaEsche[i + 3] = int(GlobalVar.gpy * listaEsche[i + 3])
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
                        listaMonete[i + 1] = int(GlobalVar.gpx * int(listaMonete[i + 1]))
                        listaMonete[i + 2] = int(GlobalVar.gpy * int(listaMonete[i + 2]))
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
            datiPersonaggi = datiTotali[5].split("_")
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
                        personaggio = PersonaggioObj(GlobalVar.gsx // 32 * int(datiPersonaggi[i]), GlobalVar.gsy // 18 * int(datiPersonaggi[i + 1]), datiPersonaggi[i + 2], datiPersonaggi[i + 3], int(datiPersonaggi[i + 4]), int(datiPersonaggi[i + 5]), datiPersonaggi[i + 6], int(datiPersonaggi[i + 7]))
                        listaPersonaggiTotali.append(personaggio)
                    except ValueError:
                        errore = True
                        break
                    i += 8
        else:
            errore = True
        if errore:
            tipoErrore = 2
    elif not errore and len(datiTotali) == 1 and datiTotali[0] == "":
        errore = True
        tipoErrore = 1

    if errore and tipoErrore == 1 and mostraErrori:
        print ("Slot vuoto")
        aggiornaSchermata = True
        indietro = False
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while not indietro:
            if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
                GlobalVar.canaleSoundCanzone.play(canzone)
            xMouse, yMouse = pygame.mouse.get_pos()
            deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
            if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
                aggiornaSchermata = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True
            if GlobalVar.mouseVisibile:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            for event in pygame.event.get():
                sinistroMouseVecchio = sinistroMouse
                centraleMouseVecchio = centraleMouse
                destroMouseVecchio = destroMouse
                sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                rotellaConCentralePremuto = False
                if centraleMouseVecchio and centraleMouse:
                    rotellaConCentralePremuto = True
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
                    if GlobalVar.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVar.mouseVisibile = False
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (GlobalVar.mouseVisibile and ((event.type == pygame.MOUSEBUTTONDOWN and destroMouse) or (event.type == pygame.MOUSEBUTTONDOWN and not GlobalVar.mouseBloccato and sinistroMouse)) and not rotellaConCentralePremuto):
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    indietro = True
                if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                    aggiornaSchermata = True
                    pygame.mouse.set_visible(True)
                    GlobalVar.mouseVisibile = True
            if aggiornaSchermata:
                aggiornaSchermata = False
                if background:
                    GlobalVar.schermo.blit(background, (0, 0))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 4.7, GlobalVar.gsy // 18 * 3.2, GlobalVar.gsx // 32 * 22.6, GlobalVar.gsy // 18 * 13.6))
                else:
                    GlobalVar.schermo.fill(GlobalVar.grigioscu)
                GlobalVar.schermo.blit(GlobalVar.robograf2, (GlobalVar.gpx * 7, -GlobalVar.gpy * 4.5))
                pygame.draw.line(GlobalVar.schermo, GlobalVar.nero, (GlobalVar.gpx * 10, GlobalVar.gpy * 13.5), (GlobalVar.gpx * 22, GlobalVar.gpy * 13.5), 2)
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
                messaggio("Slot di memoria vuoto...", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 8.5, GlobalVar.gsy // 18 * 14, 100)
                pygame.display.update()
    if errore and tipoErrore == 2 and mostraErrori:
        print ("Dati corrotti")
        aggiornaSchermata = True
        indietro = False
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while not indietro:
            if canzone and not GlobalVar.canaleSoundCanzone.get_busy():
                GlobalVar.canaleSoundCanzone.play(canzone)
            xMouse, yMouse = pygame.mouse.get_pos()
            deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
            if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVar.mouseVisibile:
                aggiornaSchermata = True
                pygame.mouse.set_visible(True)
                GlobalVar.mouseVisibile = True
            if GlobalVar.mouseVisibile:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            for event in pygame.event.get():
                sinistroMouseVecchio = sinistroMouse
                centraleMouseVecchio = centraleMouse
                destroMouseVecchio = destroMouse
                sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                rotellaConCentralePremuto = False
                if centraleMouseVecchio and centraleMouse:
                    rotellaConCentralePremuto = True
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
                    if GlobalVar.mouseVisibile:
                        pygame.mouse.set_visible(False)
                        GlobalVar.mouseVisibile = False
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (GlobalVar.mouseVisibile and ((event.type == pygame.MOUSEBUTTONDOWN and destroMouse) or (event.type == pygame.MOUSEBUTTONDOWN and not GlobalVar.mouseBloccato and sinistroMouse)) and not rotellaConCentralePremuto):
                    GlobalVar.canaleSoundPuntatore.play(GlobalVar.selind)
                    indietro = True
                if (sinistroMouse or centraleMouse or destroMouse) and not rotellaConCentralePremuto and not GlobalVar.mouseVisibile:
                    aggiornaSchermata = True
                    pygame.mouse.set_visible(True)
                    GlobalVar.mouseVisibile = True
            if aggiornaSchermata:
                aggiornaSchermata = False
                if background:
                    GlobalVar.schermo.blit(background, (0, 0))
                    pygame.draw.rect(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 4.7, GlobalVar.gsy // 18 * 3.2, GlobalVar.gsx // 32 * 22.6, GlobalVar.gsy // 18 * 13.6))
                else:
                    GlobalVar.schermo.fill(GlobalVar.grigioscu)
                GlobalVar.schermo.blit(GlobalVar.robograf4, (GlobalVar.gpx * 7, -GlobalVar.gpy * 4.5))
                pygame.draw.line(GlobalVar.schermo, GlobalVar.nero, (GlobalVar.gpx * 10, GlobalVar.gpy * 13.5), (GlobalVar.gpx * 22, GlobalVar.gpy * 13.5), 2)
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)
                messaggio("Slot di memoria danneggiato...", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 6.2, GlobalVar.gsy // 18 * 14, 100)
                pygame.display.update()

    if not errore:
        if mostraErrori:
            print ("Salvataggio: " + str(n))
            GlobalVar.canaleSoundCanzone.stop()
            return dati, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali
        else:
            return dati, tipoErrore
    else:
        if mostraErrori:
            return False, listaNemiciTotali, listaEsche, listaMonete, stanzeGiaVisitate, listaPersonaggiTotali
        else:
            return False, tipoErrore
