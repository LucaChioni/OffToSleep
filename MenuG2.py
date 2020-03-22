# -*- coding: utf-8 -*-

from SottoMenuAG2 import *


def menu():
    # video
    fermavideo = guardaVideo('Video/videoinizio')
    # attesa dopo video
    if not fermavideo:
        if GlobalVarG2.mouseBloccato:
            GlobalVarG2.configuraCursore(False)
        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
        messaggio("Premi un tasto per continuare...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 100)
        pygame.display.update()
        finevideo = True
        sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
        while finevideo:
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
                if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and (sinistroMouse or centraleMouse or destroMouse)):
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    finevideo = False

    xp = GlobalVarG2.gsx // 32 * 3
    yp = GlobalVarG2.gsy // 18 * 3.5
    voceMarcata = 1
    primoFrame = True
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    robomenuinizio = pygame.transform.scale(GlobalVarG2.robogra, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    # numero per la posizione di robo all'avvio
    c = random.randint(1, 4)

    # posizione porte e cofanetti nel vettore dati
    porteini = 134
    portefin = 161
    cofaniini = portefin + 1
    cofanifin = 185
    lunghezzadati = cofanifin + 1

    while True:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(GlobalVarG2.c11)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if deltaXMouse != 0 or deltaYMouse != 0:
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if GlobalVarG2.gsx // 32 * 2.5 <= xMouse <= GlobalVarG2.gsx // 32 * 12.5:
                if GlobalVarG2.gsy // 18 * 2.5 <= yMouse <= GlobalVarG2.gsy // 18 * 5:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 3
                    yp = GlobalVarG2.gsy // 18 * 3.5
                elif GlobalVarG2.gsy // 18 * 5 <= yMouse <= GlobalVarG2.gsy // 18 * 7.5:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 3
                    yp = GlobalVarG2.gsy // 18 * 6
                elif GlobalVarG2.gsy // 18 * 7.5 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 3
                    yp = GlobalVarG2.gsy // 18 * 8.5
                elif GlobalVarG2.gsy // 18 * 12.5 <= yMouse <= GlobalVarG2.gsy // 18 * 15:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 3
                    yp = GlobalVarG2.gsy // 18 * 13.5
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if not GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        primoMovimento = False
        tastoTrovato = False
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
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)

                # nuova partita
                if voceMarcata == 1:
                    x = GlobalVarG2.gsx // 32 * 6
                    y = GlobalVarG2.gsy // 18 * 2
                    # progresso - stanza - x - y - liv - pv - spada - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - equipaggiamento(30) - batterie(10) - condizioni(20) - gambit(20) -
                    # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - arco - guanti - collana - monete - frecce - faretra - porte(134-?) - cofanetti(?-?) // dimensione: 0-133 + porte e cofanetti
                    dati = [0, 1, x, y, 1, 55, 0, 0, 0, 0, 220,# <- statistiche
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- tecniche
                            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,# <- oggetti
                            2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0,# <- equpaggiamento
                            2, 0, 0, 0, 0, -1, -1, -1, -1, -1,# <- batterie (sono utilizzati solo i primi 5)
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- condizioni
                            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,# <- gambit
                            False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,# <- altre statistiche
                            2, 3, 7, False, 2, 7, 12, False, 2, 12, 11, False, 2, 15, 9, False, 2, 15, 3, False, 2, 23, 5, False, 2, 23, 12, False,# <- porte
                            1, 3, 7, False, 1, 7, 12, False, 1, 12, 11, False, 2, 3, 5, False, 2, 5, 10, False, 2, 10, 9, False]# <- cofanetti
                    GlobalVarG2.canaleSoundCanzone.stop()
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
                    return dati, porteini, portefin, cofaniini, cofanifin

                # carica partita
                if voceMarcata == 2:
                    n = scegli_sal(1, lunghezzadati, GlobalVarG2.c11)

                    # lettura salvataggio
                    if n != -1:
                        leggi = open("Salvataggi/Salvataggio%i.txt" % n, "r")
                        leggifile = leggi.read()
                        dati = leggifile.split("_")
                        dati.pop(len(dati) - 1)
                        if len(dati) == 0:
                            print "Slot vuoto"
                            aggiornaSchermata = True
                            indietro = False
                            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                            while not indietro:
                                deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
                                if deltaXMouse != 0 or deltaYMouse != 0:
                                    aggiornaSchermata = True
                                    pygame.mouse.set_visible(True)
                                    GlobalVarG2.mouseVisibile = True
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
                                        pygame.mouse.set_visible(False)
                                        GlobalVarG2.mouseVisibile = False
                                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.MOUSEBUTTONDOWN and destroMouse):
                                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                                        indietro = True
                                if aggiornaSchermata:
                                    aggiornaSchermata = False
                                    GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
                                    robograsalva = pygame.transform.scale(GlobalVarG2.robograff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
                                    GlobalVarG2.schermo.blit(robograsalva, (GlobalVarG2.gpx * 3, -GlobalVarG2.gpy * 5))
                                    if GlobalVarG2.mouseVisibile:
                                        messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
                                    else:
                                        messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
                                    messaggio("Slot di salvataggio vuoto...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 100)
                                    pygame.display.update()
                        else:
                            errore = False
                            if len(dati) != lunghezzadati:
                                errore = True
                            else:
                                for i in range(0, len(dati)):
                                    try:
                                        dati[i] = int(dati[i])
                                    except ValueError:
                                        errore = True
                                if not errore:
                                    # conversione della posizione in pixel
                                    dati[2] = dati[2] * GlobalVarG2.gpx
                                    dati[3] = dati[3] * GlobalVarG2.gpy
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

                                    print "Salvataggio: " + str(n)
                                    leggi.close()
                                    GlobalVarG2.canaleSoundCanzone.stop()
                                    return dati, porteini, portefin, cofaniini, cofanifin
                            if len(dati) != lunghezzadati or errore:
                                print "Dati corrotti: " + str(len(dati))
                                aggiornaSchermata = True
                                indietro = False
                                sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
                                while not indietro:
                                    deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
                                    if deltaXMouse != 0 or deltaYMouse != 0:
                                        aggiornaSchermata = True
                                        pygame.mouse.set_visible(True)
                                        GlobalVarG2.mouseVisibile = True
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
                                            pygame.mouse.set_visible(False)
                                            GlobalVarG2.mouseVisibile = False
                                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.MOUSEBUTTONDOWN and destroMouse):
                                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                                            indietro = True
                                    if aggiornaSchermata:
                                        aggiornaSchermata = False
                                        GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
                                        robograsalva = pygame.transform.scale(GlobalVarG2.robograffff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
                                        GlobalVarG2.schermo.blit(robograsalva, (GlobalVarG2.gpx * 15, -GlobalVarG2.gpy * 3))
                                        if GlobalVarG2.mouseVisibile:
                                            messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
                                        else:
                                            messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
                                        messaggio("I dati sono corrotti...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 100)
                                        pygame.display.update()
                        leggi.close()

                # Impostazioni
                if voceMarcata == 3:
                    menuImpostazioni(GlobalVarG2.c11, True)
                    primoFrame = True

                # esci dal gioco
                if voceMarcata == 4:
                    pygame.quit()
                    quit()
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata:
            if primoFrame:
                puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
                if voceMarcata == 1:
                    yp = GlobalVarG2.gsy // 18 * 3.5
                if voceMarcata == 2:
                    yp = GlobalVarG2.gsy // 18 * 6
                if voceMarcata == 3:
                    yp = GlobalVarG2.gsy // 18 * 8.5
                if voceMarcata == 4:
                    yp = GlobalVarG2.gsy // 18 * 13.5
                primoFrame = False
            if not primoMovimento and (tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 2
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 4:
                    if voceMarcata == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 6
                    elif voceMarcata == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 8.5
                    elif voceMarcata == 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 13.5
                    voceMarcata += 1
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 3.5
                    voceMarcata -= 3
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 1:
                    if voceMarcata == 2:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 3.5
                    elif voceMarcata == 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 6
                    elif voceMarcata == 4:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 8.5
                    voceMarcata -= 1
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 13.5
                    voceMarcata += 3
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            persomenuinizio = pygame.transform.scale(GlobalVarG2.persGrafInizio, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 1):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robogra, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 2):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 3):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robograff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            if (c == 4):
                robomenuinizio = pygame.transform.scale(GlobalVarG2.robografff, (GlobalVarG2.gpx * 18, GlobalVarG2.gpy * 18))
            GlobalVarG2.schermo.blit(persomenuinizio, (GlobalVarG2.gpx * 15, 0))
            GlobalVarG2.schermo.blit(robomenuinizio, (GlobalVarG2.gpx * 3, 0))
            messaggio("Nuova partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 3, 90)
            messaggio("Carica partita", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 5.5, 90)
            messaggio("Impostazioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 8, 90)
            messaggio("Esci", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 4, GlobalVarG2.gsy // 18 * 13, 90)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)


def start(dati, nmost, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, apriocchio):
    sfondostastart = pygame.transform.scale(GlobalVarG2.sfondostax3, (GlobalVarG2.gpx * 4, GlobalVarG2.gpy))
    perssta = pygame.transform.scale(GlobalVarG2.persGrafMenu, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    robosta = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatoreVecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    avvelenatosta = pygame.transform.scale(GlobalVarG2.avvelenatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    surriscaldatosta = pygame.transform.scale(GlobalVarG2.surriscaldatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    attaccopiusta = pygame.transform.scale(GlobalVarG2.attaccopiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    difesapiusta = pygame.transform.scale(GlobalVarG2.difesapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    velocitapiusta = pygame.transform.scale(GlobalVarG2.velocitapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    efficienzapiusta = pygame.transform.scale(GlobalVarG2.efficienzapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
    if dati[133] == 0:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart0
        maxFrecce = 1
    elif dati[133] == 1:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart1
        maxFrecce = 5
    elif dati[133] == 2:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart2
        maxFrecce = 20
    elif dati[133] == 3:
        faretraFrecceStart = GlobalVarG2.faretraFrecceStart3
        maxFrecce = 60
    else:
        faretraFrecceStart = 0
        maxFrecce = 0
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 5
    carim = True
    risposta = False
    attacco = 0
    conferma = 0
    inizio = False
    voceMarcata = 1
    primoFrame = True
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(GlobalVarG2.c27)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 11:
                if GlobalVarG2.gsy // 18 * 4.8 <= yMouse <= GlobalVarG2.gsy // 18 * 5.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 5
                elif GlobalVarG2.gsy // 18 * 5.8 <= yMouse <= GlobalVarG2.gsy // 18 * 6.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6
                elif GlobalVarG2.gsy // 18 * 6.8 <= yMouse <= GlobalVarG2.gsy // 18 * 7.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 7
                elif GlobalVarG2.gsy // 18 * 7.8 <= yMouse <= GlobalVarG2.gsy // 18 * 8.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8
                elif GlobalVarG2.gsy // 18 * 8.8 <= yMouse <= GlobalVarG2.gsy // 18 * 9.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 9
                elif GlobalVarG2.gsy // 18 * 11.8 <= yMouse <= GlobalVarG2.gsy // 18 * 12.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12
                elif GlobalVarG2.gsy // 18 * 12.8 <= yMouse <= GlobalVarG2.gsy // 18 * 13.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 13
                elif GlobalVarG2.gsy // 18 * 13.8 <= yMouse <= GlobalVarG2.gsy // 18 * 14.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 14
                elif GlobalVarG2.gsy // 18 * 14.8 <= yMouse <= GlobalVarG2.gsy // 18 * 15.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 15
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if not GlobalVarG2.mouseBloccato:
                    GlobalVarG2.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        primoMovimento = False
        tastoTrovato = False
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
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_ESCAPE) and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    inizio = False
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and (destroMouse or centraleMouse):
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                inizio = False
                risposta = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                if voceMarcata != 6 or (voceMarcata == 6 and nmost == -1):
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                inizio = False
                # oggetti
                if voceMarcata == 1:
                    dati, attacco = oggetti(dati, GlobalVarG2.c27)
                    carim = True
                # equip pers
                if voceMarcata == 2:
                    dati = equip(dati, GlobalVarG2.c27)
                    carim = True
                # equip robot
                if voceMarcata == 3:
                    dati = equiprobo(dati, GlobalVarG2.c27)
                    carim = True
                # mappa
                if voceMarcata == 4:
                    menuMappa(dati[0], GlobalVarG2.c27)
                # diario
                if voceMarcata == 5:
                    menuDiario(dati[0], GlobalVarG2.c27)
                # salva
                if voceMarcata == 6:
                    #if nmost == -1:
                    n = scegli_sal(3, len(dati), GlobalVarG2.c27)
                    if n != -1:
                        salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti)
                # impostazioni
                if voceMarcata == 7:
                    menuImpostazioni(GlobalVarG2.c27, False)
                # menu
                if voceMarcata == 8:
                    GlobalVarG2.schermo.blit(puntatoreVecchio, (xp, yp))
                    conferma = 1
                # chiudi
                if voceMarcata == 9:
                    GlobalVarG2.schermo.blit(puntatoreVecchio, (xp, yp))
                    conferma = 2
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 5 and voceMarcata != 9:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1
                    voceMarcata += 1
                else:
                    if voceMarcata == 5:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp + GlobalVarG2.gsy // 18 * 3
                        voceMarcata += 1
                    elif voceMarcata == 9:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 5
                        voceMarcata = 1
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 6 and voceMarcata != 1:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp - GlobalVarG2.gsy // 18 * 1
                    voceMarcata -= 1
                else:
                    if voceMarcata == 6:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 3
                        voceMarcata -= 1
                    elif voceMarcata == 1:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15
                        voceMarcata = 9
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma, GlobalVarG2.c27)
                conferma = 0

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            messaggio("Menu start", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 50)
            messaggio("Equipaggiamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 50)
            messaggio("Setta Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 50)
            messaggio("Mappa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 50)
            messaggio("Diario", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 50)
            if nmost == -1:
                messaggio("Salva", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 50)
            else:
                messaggio("Salva", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 50)
            messaggio("Impostazioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 50)
            messaggio("Torna al menu principale", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 50)
            messaggio("Torna a Windows", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 50)
            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Esc / Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 1, 50)
            if carim:
                if dati[10] <= 0:
                    robosta = GlobalVarG2.robograff
                    robosta = pygame.transform.scale(robosta, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
                else:
                    robosta = GlobalVarG2.robograf
                    robosta = pygame.transform.scale(robosta, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
                carim = False

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 13, 50)
            messaggio("Lv:  " + str(dati[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 14, 50)
            if dati[4] < 100:
                messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 14, 50)
            else:
                messaggio("Esp:  -- / --", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 14, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 15, 50)
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 13.5, (GlobalVarG2.gsy // 18 * 16) + (GlobalVarG2.gpy // 8)))
            if dati[121]:
                GlobalVarG2.schermo.blit(avvelenatosta, (GlobalVarG2.gsx // 32 * 13.5, GlobalVarG2.gsy // 18 * 16))
            if dati[123] > 0:
                GlobalVarG2.schermo.blit(attaccopiusta, ((GlobalVarG2.gsx // 32 * 13.5) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 16))
            if dati[124] > 0:
                GlobalVarG2.schermo.blit(difesapiusta, ((GlobalVarG2.gsx // 32 * 13.5) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 16))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 13, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 14, 50)
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 23.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 8)))
            if dati[122] > 0:
                GlobalVarG2.schermo.blit(surriscaldatosta, (GlobalVarG2.gsx // 32 * 23.5, GlobalVarG2.gsy // 18 * 15))
            if dati[125] > 0:
                GlobalVarG2.schermo.blit(velocitapiusta, ((GlobalVarG2.gsx // 32 * 23.5) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 15))
            if dati[126] > 0:
                GlobalVarG2.schermo.blit(efficienzapiusta, ((GlobalVarG2.gsx // 32 * 23.5) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 15))

            if attacco != 0:
                risposta = True

            if faretraFrecceStart != 0:
                GlobalVarG2.schermo.blit(faretraFrecceStart, (GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 2.5))
                messaggio("Frecce: " + str(dati[132]) + " / " + str(maxFrecce), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 21.5, GlobalVarG2.gsy // 18 * 6, 50)
            GlobalVarG2.schermo.blit(GlobalVarG2.sacchettoDenaroStart, (GlobalVarG2.gsx // 32 * 26.5, GlobalVarG2.gsy // 18 * 2.5))
            messaggio("Monete: " + str(dati[131]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 26.5, GlobalVarG2.gsy // 18 * 6, 50)

            GlobalVarG2.schermo.blit(perssta, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 2))
            GlobalVarG2.schermo.blit(robosta, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 2))
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if not risposta:
                pygame.display.update()
            else:
                GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    GlobalVarG2.canaleSoundCanzone.stop()
    return dati, inizio, attacco


def startBattaglia(dati, animaOggetto, x, y, npers, rx, ry):
    xp = GlobalVarG2.gpx * 1
    yp = GlobalVarG2.gpy * 5
    sconosciutoOggetto = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoMenu, (GlobalVarG2.gpx * 4, GlobalVarG2.gpy * 4))
    sconosciutoOggettoIco = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoIcoMenu, (GlobalVarG2.gpx, GlobalVarG2.gpy))

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

    attacco = 0
    disegnoOggetto = 0
    risposta = False
    voceMarcata = 1
    primoFrame = True
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    difensivi = True
    offensivi = False
    sposta = False

    oggetton = 1
    vettoreOggettiGraf = []
    vettoreOggettiIco = []
    while oggetton <= 10:
        if dati[oggetton + 30] >= 0:
            vettoreOggettiGraf.append(GlobalVarG2.vetImgOggettiStart[oggetton - 1])
            vettoreOggettiIco.append(GlobalVarG2.vetIcoOggettiMenu[oggetton - 1])
        else:
            vettoreOggettiGraf.append(sconosciutoOggetto)
            vettoreOggettiIco.append(sconosciutoOggettoIco)
        oggetton += 1

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        mouseInquadraFreccia = False
        if deltaXMouse != 0 or deltaYMouse != 0:
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if difensivi:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 7 and GlobalVarG2.gsx // 32 * 3 <= xMouse <= GlobalVarG2.gsx // 32 * 4:
                    mouseInquadraFreccia = True
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                elif GlobalVarG2.gsy // 18 * 5 <= yMouse <= GlobalVarG2.gsy // 18 * 6:
                    if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 2:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 5
                    elif GlobalVarG2.gsx // 32 * 2 <= xMouse <= GlobalVarG2.gsx // 32 * 3:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVarG2.gsx // 32 * 2
                        yp = GlobalVarG2.gsy // 18 * 5
                    elif GlobalVarG2.gsx // 32 * 3 <= xMouse <= GlobalVarG2.gsx // 32 * 4:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalVarG2.gsx // 32 * 3
                        yp = GlobalVarG2.gsy // 18 * 5
                    elif GlobalVarG2.gsx // 32 * 4 <= xMouse <= GlobalVarG2.gsx // 32 * 5:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalVarG2.gsx // 32 * 4
                        yp = GlobalVarG2.gsy // 18 * 5
                    elif GlobalVarG2.gsx // 32 * 5 <= xMouse <= GlobalVarG2.gsx // 32 * 6:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 5
                        xp = GlobalVarG2.gsx // 32 * 5
                        yp = GlobalVarG2.gsy // 18 * 5
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif offensivi:
                if GlobalVarG2.gsy // 18 * 4.5 <= yMouse <= GlobalVarG2.gsy // 18 * 5.5 and GlobalVarG2.gsx // 32 * 3 <= xMouse <= GlobalVarG2.gsx // 32 * 4:
                    mouseInquadraFreccia = True
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                elif GlobalVarG2.gsy // 18 * 5.5 <= yMouse <= GlobalVarG2.gsy // 18 * 6.5:
                    if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 2:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 5.5
                    elif GlobalVarG2.gsx // 32 * 2 <= xMouse <= GlobalVarG2.gsx // 32 * 3:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVarG2.gsx // 32 * 2
                        yp = GlobalVarG2.gsy // 18 * 5.5
                    elif GlobalVarG2.gsx // 32 * 3 <= xMouse <= GlobalVarG2.gsx // 32 * 4:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 3
                        xp = GlobalVarG2.gsx // 32 * 3
                        yp = GlobalVarG2.gsy // 18 * 5.5
                    elif GlobalVarG2.gsx // 32 * 4 <= xMouse <= GlobalVarG2.gsx // 32 * 5:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 4
                        xp = GlobalVarG2.gsx // 32 * 4
                        yp = GlobalVarG2.gsy // 18 * 5.5
                    elif GlobalVarG2.gsx // 32 * 5 <= xMouse <= GlobalVarG2.gsx // 32 * 6:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 5
                        xp = GlobalVarG2.gsx // 32 * 5
                        yp = GlobalVarG2.gsy // 18 * 5.5
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        primoMovimento = False
        tastoTrovato = False
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
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if (event.key == pygame.K_q or event.key == pygame.K_ESCAPE) and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and (destroMouse or centraleMouse):
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                risposta = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and mouseInquadraFreccia:
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                if difensivi:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = (GlobalVarG2.gpy * 5) + (GlobalVarG2.gpy // 2)
                    difensivi = False
                    offensivi = True
                elif offensivi:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gpy * 5
                    offensivi = False
                    difensivi = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and not mouseInquadraFreccia):
                tastoTrovato = True
                tastop = "spazioOsinistroMouse"
                if difensivi:
                    # pozione
                    if voceMarcata == 1 and dati[31] > 0:
                        animaOggetto[0] = "pozione"
                        dati[5] = dati[5] + 100
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[31] = dati[31] - 1
                        sposta = True
                        risposta = True
                    # carica batt
                    if voceMarcata == 2 and dati[32] > 0 and (abs(x - rx) + abs(y - ry)) <= GlobalVarG2.gpx:
                        animaOggetto[0] = "caricaBatterie"
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[32] = dati[32] - 1
                        # npers: 1=d, 2=a, 3=w, 4=s
                        if x < rx:
                            npers = 1
                        elif x > rx:
                            npers = 2
                        elif y < ry:
                            npers = 4
                        elif y > ry:
                            npers = 3
                        sposta = True
                        risposta = True
                    # antidoto
                    if voceMarcata == 3 and dati[33] > 0:
                        animaOggetto[0] = "medicina"
                        dati[121] = 0
                        dati[33] = dati[33] - 1
                        sposta = True
                        risposta = True
                    # super pozione
                    if voceMarcata == 4 and dati[34] > 0:
                        animaOggetto[0] = "superPozione"
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[34] = dati[34] - 1
                        sposta = True
                        risposta = True
                    # carica migliorato
                    if voceMarcata == 5 and dati[35] > 0 and (abs(x - rx) + abs(y - ry)) <= GlobalVarG2.gpx:
                        animaOggetto[0] = "caricaBatterieMigliorato"
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[35] = dati[35] - 1
                        # npers: 1=d, 2=a, 3=w, 4=s
                        if x < rx:
                            npers = 1
                        elif x > rx:
                            npers = 2
                        elif y < ry:
                            npers = 4
                        elif y > ry:
                            npers = 3
                        sposta = True
                        risposta = True
                elif offensivi:
                    # bomba
                    if voceMarcata == 1 and dati[36] > 0:
                        attacco = 2
                        risposta = True
                    # bomba veleno
                    if voceMarcata == 2 and dati[37] > 0:
                        attacco = 3
                        risposta = True
                    # esca
                    if voceMarcata == 3 and dati[38] > 0:
                        attacco = 4
                        risposta = True
                    # bomba appiccicosa
                    if voceMarcata == 4 and dati[39] > 0:
                        attacco = 5
                        risposta = True
                    # bomba potenziata
                    if voceMarcata == 5 and dati[40] > 0:
                        attacco = 6
                        risposta = True
                if risposta:
                    if offensivi:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata:
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if offensivi:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gpy * 5
                    offensivi = False
                    difensivi = True
            if tastop == pygame.K_a:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 1:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gpx
                else:
                    voceMarcata += 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gpx * 5
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if difensivi:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = (GlobalVarG2.gpy * 5) + (GlobalVarG2.gpy // 2)
                    difensivi = False
                    offensivi = True
            if tastop == pygame.K_d:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 5:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gpx
                else:
                    voceMarcata -= 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gpx * 1
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoStartBattaglia, (0, 0))
            if difensivi:
                if voceMarcata == 1:
                    disegnoOggetto = 0
                if voceMarcata == 2:
                    disegnoOggetto = 1
                if voceMarcata == 3:
                    disegnoOggetto = 2
                if voceMarcata == 4:
                    disegnoOggetto = 3
                if voceMarcata == 5:
                    disegnoOggetto = 4
            elif offensivi:
                if voceMarcata == 1:
                    disegnoOggetto = 5
                if voceMarcata == 2:
                    disegnoOggetto = 6
                if voceMarcata == 3:
                    disegnoOggetto = 7
                if voceMarcata == 4:
                    disegnoOggetto = 8
                if voceMarcata == 5:
                    disegnoOggetto = 9
            GlobalVarG2.schermo.blit(vettoreOggettiGraf[disegnoOggetto], (GlobalVarG2.gpx // 2, GlobalVarG2.gpy * 1))
            if dati[disegnoOggetto + 31] <= 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatOut, (xp, yp))
                qta = 0
            elif (disegnoOggetto == 1 or disegnoOggetto == 4) and abs(x - rx) + abs(y - ry) > GlobalVarG2.gpx:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatOut, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            else:
                GlobalVarG2.schermo.blit(GlobalVarG2.puntatIn, (xp, yp))
                qta = dati[disegnoOggetto + 31]
            messaggio("x%i" % qta, GlobalVarG2.grigiochi, (GlobalVarG2.gpx * 4) + (GlobalVarG2.gpx // 2), GlobalVarG2.gpy * 3, 80)
            disegnati = 0
            i = 0
            while i < 10:
                if difensivi and (i == 0 or i == 1 or i == 2 or i == 3 or i == 4):
                    GlobalVarG2.schermo.blit(vettoreOggettiIco[i], (GlobalVarG2.gpx * (disegnati + 1), GlobalVarG2.gpy * 5))
                    disegnati += 1
                if offensivi and (i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
                    GlobalVarG2.schermo.blit(vettoreOggettiIco[i], (GlobalVarG2.gpx * (disegnati + 1), (GlobalVarG2.gpy * 5) + (GlobalVarG2.gpy // 2)))
                    disegnati += 1
                i += 1
            if difensivi:
                if voceMarcata == 1:
                    messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 2:
                    messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 3:
                    messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 4:
                    messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 5:
                    messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                GlobalVarG2.schermo.blit(GlobalVarG2.scorriGiu, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 6))
            if offensivi:
                if voceMarcata == 1:
                    messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 2:
                    messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 3:
                    messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 4:
                    messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                if voceMarcata == 5:
                    messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gpx // 3, GlobalVarG2.gpy // 3, 55)
                GlobalVarG2.schermo.blit(GlobalVarG2.scorriSu, (GlobalVarG2.gpx * 3, (GlobalVarG2.gpy * 5) - (GlobalVarG2.gpy // 2)))

            if not risposta:
                pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati, attacco, sposta, animaOggetto, npers


def menuMercante(dati):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sconosciutoOggetto = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoMenu, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    xp = GlobalVarG2.gsx // 32 * 10.5
    yp = GlobalVarG2.gsy // 18 * 6.1
    xpv = xp
    ypv = yp
    usauno = False
    confermaOggettoDaAcquistare = 0
    risposta = False
    oggetton = 0
    voceMarcata = 0
    numeroOggettiAcquistati = 1
    moneteInsufficienti = False
    inventarioPieno = False
    primoFrame = True
    mouseSinistroPremuto = False
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    maxFrecce = 1
    if dati[133] == 1:
        maxFrecce = 5
    elif dati[133] == 2:
        maxFrecce = 20
    elif dati[133] == 3:
        maxFrecce = 60

    tastop = 0
    tastotempfps = 5

    imgOggetti = []
    i = 1
    while i <= 10:
        if (i == 1 and dati[0] > -1) or (i == 2 and dati[0] > -1) or (i == 3 and dati[0] > -1) or (i == 4 and dati[0] > -1) or (i == 5 and dati[0] > -1) or (i == 6 and dati[0] > -1) or (i == 7 and dati[0] > -1) or (i == 8 and dati[0] > -1) or (i == 9 and dati[0] > -1) or (i == 10 and dati[0] > -1):
            imgOggetti.append(GlobalVarG2.vetImgOggettiMercante[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(GlobalVarG2.c27)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        oggettonVecchio = oggetton
        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        mouseInquadraFrecciaSu = False
        mouseInquadraFrecciaGiu = False
        if deltaXMouse != 0 or deltaYMouse != 0:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if voceMarcata == 0:
                if GlobalVarG2.gsx // 32 * 10.5 <= xMouse <= GlobalVarG2.gsx // 32 * 21.5:
                    if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 6.8:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 0
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 6.1
                    elif GlobalVarG2.gsy // 18 * 6.8 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 1
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 7
                    elif GlobalVarG2.gsy // 18 * 7.7 <= yMouse <= GlobalVarG2.gsy // 18 * 8.6:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 2
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 7.9
                    elif GlobalVarG2.gsy // 18 * 8.6 <= yMouse <= GlobalVarG2.gsy // 18 * 9.5:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 3
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    elif GlobalVarG2.gsy // 18 * 9.5 <= yMouse <= GlobalVarG2.gsy // 18 * 10.4:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 4
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 9.7
                    elif GlobalVarG2.gsy // 18 * 10.4 <= yMouse <= GlobalVarG2.gsy // 18 * 11.3:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 5
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 10.6
                    elif GlobalVarG2.gsy // 18 * 11.3 <= yMouse <= GlobalVarG2.gsy // 18 * 12.2:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 6
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 11.5
                    elif GlobalVarG2.gsy // 18 * 12.2 <= yMouse <= GlobalVarG2.gsy // 18 * 13.1:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 7
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 12.4
                    elif GlobalVarG2.gsy // 18 * 13.1 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 8
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 13.3
                    elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 14.9:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 9
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 14.2
                    elif GlobalVarG2.gsy // 18 * 14.9 <= yMouse <= GlobalVarG2.gsy // 18 * 15.8:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 10
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    elif GlobalVarG2.gsy // 18 * 15.8 <= yMouse <= GlobalVarG2.gsy // 18 * 16.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 11
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        yp = GlobalVarG2.gsy // 18 * 16
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if GlobalVarG2.gsy // 18 * 4.3 <= yMouse <= GlobalVarG2.gsy // 18 * 4.8 and GlobalVarG2.gsx // 32 * 8.5 <= xMouse <= GlobalVarG2.gsx // 32 * 9.5:
                    mouseInquadraFrecciaSu = True
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                elif GlobalVarG2.gsy // 18 * 4.8 <= yMouse <= GlobalVarG2.gsy // 18 * 5.3 and GlobalVarG2.gsx // 32 * 8.5 <= xMouse <= GlobalVarG2.gsx // 32 * 9.5:
                    mouseInquadraFrecciaGiu = True
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                elif GlobalVarG2.gsy // 18 * 6.6 <= yMouse <= GlobalVarG2.gsy // 18 * 7.6:
                    if GlobalVarG2.gsx // 32 * 1.3 <= xMouse <= GlobalVarG2.gsx // 32 * 5.3:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVarG2.gsx // 32 * 1.3
                        yp = GlobalVarG2.gsy // 18 * 6.9
                    elif GlobalVarG2.gsx // 32 * 5.3 <= xMouse <= GlobalVarG2.gsx // 32 * 9.2:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVarG2.gsx // 32 * 5.3
                        yp = GlobalVarG2.gsy // 18 * 6.9
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            if (oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata) and not primoFrame:
                inventarioPieno = False
                moneteInsufficienti = False
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)

        primoMovimento = False
        tastoTrovato = False
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
                tastoTrovato = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not tastoTrovato and oggettonVecchio == oggetton and voceMarcataVecchia == voceMarcata:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    numeroOggettiAcquistati = 1
                    moneteInsufficienti = False
                    inventarioPieno = False
                    tastoTrovato = True
                    voceMarcata = 0
                    if confermaOggettoDaAcquistare != 0:
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        if confermaOggettoDaAcquistare == -1:
                            yp = GlobalVarG2.gsy // 18 * 6.1
                        if confermaOggettoDaAcquistare == 1:
                            yp = GlobalVarG2.gsy // 18 * 7
                        if confermaOggettoDaAcquistare == 2:
                            yp = GlobalVarG2.gsy // 18 * 7.9
                        if confermaOggettoDaAcquistare == 3:
                            yp = GlobalVarG2.gsy // 18 * 8.8
                        if confermaOggettoDaAcquistare == 4:
                            yp = GlobalVarG2.gsy // 18 * 9.7
                        if confermaOggettoDaAcquistare == 5:
                            yp = GlobalVarG2.gsy // 18 * 10.6
                        if confermaOggettoDaAcquistare == 6:
                            yp = GlobalVarG2.gsy // 18 * 11.5
                        if confermaOggettoDaAcquistare == 7:
                            yp = GlobalVarG2.gsy // 18 * 12.4
                        if confermaOggettoDaAcquistare == 8:
                            yp = GlobalVarG2.gsy // 18 * 13.3
                        if confermaOggettoDaAcquistare == 9:
                            yp = GlobalVarG2.gsy // 18 * 14.2
                        if confermaOggettoDaAcquistare == 10:
                            yp = GlobalVarG2.gsy // 18 * 15.1
                        if confermaOggettoDaAcquistare == 11:
                            yp = GlobalVarG2.gsy // 18 * 16
                        confermaOggettoDaAcquistare = 0
                    else:
                        risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and voceMarcata != 0 and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and voceMarcata != 0 and not tastoTrovato:
                    moneteInsufficienti = False
                    inventarioPieno = False
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                numeroOggettiAcquistati = 1
                moneteInsufficienti = False
                inventarioPieno = False
                tastoTrovato = True
                voceMarcata = 0
                if confermaOggettoDaAcquistare != 0:
                    xp = GlobalVarG2.gsx // 32 * 10.5
                    if confermaOggettoDaAcquistare == -1:
                        yp = GlobalVarG2.gsy // 18 * 6.1
                    if confermaOggettoDaAcquistare == 1:
                        yp = GlobalVarG2.gsy // 18 * 7
                    if confermaOggettoDaAcquistare == 2:
                        yp = GlobalVarG2.gsy // 18 * 7.9
                    if confermaOggettoDaAcquistare == 3:
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    if confermaOggettoDaAcquistare == 4:
                        yp = GlobalVarG2.gsy // 18 * 9.7
                    if confermaOggettoDaAcquistare == 5:
                        yp = GlobalVarG2.gsy // 18 * 10.6
                    if confermaOggettoDaAcquistare == 6:
                        yp = GlobalVarG2.gsy // 18 * 11.5
                    if confermaOggettoDaAcquistare == 7:
                        yp = GlobalVarG2.gsy // 18 * 12.4
                    if confermaOggettoDaAcquistare == 8:
                        yp = GlobalVarG2.gsy // 18 * 13.3
                    if confermaOggettoDaAcquistare == 9:
                        yp = GlobalVarG2.gsy // 18 * 14.2
                    if confermaOggettoDaAcquistare == 10:
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    if confermaOggettoDaAcquistare == 11:
                        yp = GlobalVarG2.gsy // 18 * 16
                    confermaOggettoDaAcquistare = 0
                else:
                    risposta = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu):
                tastoTrovato = True
                tastotempfps = 5
                primoMovimento = True
                tastop = "spazioOsinistroMouse"
                mouseSinistroPremuto = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato and not (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu)):
                moneteInsufficienti = False
                inventarioPieno = False
                tastotempfps = 5
                primoMovimento = True
                tastoTrovato = True
                procediAllAcquisto = True
                tastop = "spazioOsinistroMouse"

                # confermaOggettoDaAcquistare?
                if voceMarcata == 1:
                    if 0 <= oggetton <= 10 and GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                        GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                        dati[131] -= GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati
                        voceMarcata = 0
                        xp = GlobalVarG2.gsx // 32 * 10.5
                        # freccia
                        if confermaOggettoDaAcquistare == -1:
                            dati[132] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 6.1
                        # pozione
                        if confermaOggettoDaAcquistare == 1:
                            dati[31] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 7
                        # carica batt
                        if confermaOggettoDaAcquistare == 2:
                            dati[32] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 7.9
                        # antidoto
                        if confermaOggettoDaAcquistare == 3:
                            dati[33] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 8.8
                        # super pozione
                        if confermaOggettoDaAcquistare == 4:
                            dati[34] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 9.7
                        # carica migliorato
                        if confermaOggettoDaAcquistare == 5:
                            dati[35] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 10.6
                        # bomba
                        if confermaOggettoDaAcquistare == 6:
                            dati[36] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 11.5
                        # bomba veleno
                        if confermaOggettoDaAcquistare == 7:
                            dati[37] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 12.4
                        # esca
                        if confermaOggettoDaAcquistare == 8:
                            dati[38] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 13.3
                        # bomba appiccicosa
                        if confermaOggettoDaAcquistare == 9:
                            dati[39] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 14.2
                        # bomba potenziata
                        if confermaOggettoDaAcquistare == 10:
                            dati[40] += numeroOggettiAcquistati
                            yp = GlobalVarG2.gsy // 18 * 15.1
                        confermaOggettoDaAcquistare = 0
                        procediAllAcquisto = False
                    elif oggetton == 11:
                        if dati[133] == 0 and GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                            dati[131] -= GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVarG2.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 15.1
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 1 and GlobalVarG2.costoOggetti[oggetton + 1] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                            dati[131] -= GlobalVarG2.costoOggetti[oggetton + 1] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVarG2.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 15.1
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        elif dati[133] == 2 and GlobalVarG2.costoOggetti[oggetton + 2] * numeroOggettiAcquistati <= dati[131]:
                            GlobalVarG2.canaleSoundInterazioni.play(GlobalVarG2.rumoreAcquisto)
                            dati[131] -= GlobalVarG2.costoOggetti[oggetton + 2] * numeroOggettiAcquistati
                            voceMarcata = 0
                            xp = GlobalVarG2.gsx // 32 * 10.5
                            # faretra
                            if confermaOggettoDaAcquistare == 10:
                                dati[40] += numeroOggettiAcquistati
                                yp = GlobalVarG2.gsy // 18 * 15.1
                            confermaOggettoDaAcquistare = 0
                            procediAllAcquisto = False
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            moneteInsufficienti = True
                            procediAllAcquisto = False
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        moneteInsufficienti = True
                        procediAllAcquisto = False
                elif voceMarcata == 2:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    voceMarcata = 0
                    numeroOggettiAcquistati = 1
                    moneteInsufficienti = False
                    inventarioPieno = False
                    xp = GlobalVarG2.gsx // 32 * 10.5
                    if confermaOggettoDaAcquistare == -1:
                        yp = GlobalVarG2.gsy // 18 * 6.1
                    if confermaOggettoDaAcquistare == 1:
                        yp = GlobalVarG2.gsy // 18 * 7
                    if confermaOggettoDaAcquistare == 2:
                        yp = GlobalVarG2.gsy // 18 * 7.9
                    if confermaOggettoDaAcquistare == 3:
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    if confermaOggettoDaAcquistare == 4:
                        yp = GlobalVarG2.gsy // 18 * 9.7
                    if confermaOggettoDaAcquistare == 5:
                        yp = GlobalVarG2.gsy // 18 * 10.6
                    if confermaOggettoDaAcquistare == 6:
                        yp = GlobalVarG2.gsy // 18 * 11.5
                    if confermaOggettoDaAcquistare == 7:
                        yp = GlobalVarG2.gsy // 18 * 12.4
                    if confermaOggettoDaAcquistare == 8:
                        yp = GlobalVarG2.gsy // 18 * 13.3
                    if confermaOggettoDaAcquistare == 9:
                        yp = GlobalVarG2.gsy // 18 * 14.2
                    if confermaOggettoDaAcquistare == 10:
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    if confermaOggettoDaAcquistare == 11:
                        yp = GlobalVarG2.gsy // 18 * 16
                    confermaOggettoDaAcquistare = 0
                    procediAllAcquisto = False

                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                if procediAllAcquisto:
                    if 1 <= oggetton <= 10 and dati[30 + oggetton] < 99:
                        numeroOggettiAcquistati = 1
                        if oggetton == 1:
                            if imgOggetti[0] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 1
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 2:
                            if imgOggetti[1] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 2
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 3:
                            if imgOggetti[2] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 3
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 4:
                            if imgOggetti[3] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 4
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 5:
                            if imgOggetti[4] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 5
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 6:
                            if imgOggetti[5] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 6
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 7:
                            if imgOggetti[6] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 7
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 8:
                            if imgOggetti[7] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 8
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 9:
                            if imgOggetti[8] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 9
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        if oggetton == 10:
                            if imgOggetti[9] != sconosciutoOggetto:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                confermaOggettoDaAcquistare = 10
                                usauno = True
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    elif oggetton == 0 and dati[132] < maxFrecce:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        confermaOggettoDaAcquistare = -1
                        usauno = True
                    elif oggetton == 11 and dati[133] != 3:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        confermaOggettoDaAcquistare = 11
                        usauno = True
                    else:
                        inventarioPieno = True
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                mouseSinistroPremuto = False
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or ((tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or oggettonVecchio != oggetton or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == "spazioOsinistroMouse" or tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 0:
                    if oggetton != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        oggetton = oggetton - 1
                        yp = yp - GlobalVarG2.gsy // 18 * 0.9
                    elif oggetton == 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 16
                        oggetton = 11
                elif voceMarcata != 0:
                    if oggetton != 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati + dati[30 + oggetton] >= 99:
                            numeroOggettiAcquistati = 1
                        elif oggetton == 0 and numeroOggettiAcquistati + dati[132] >= maxFrecce:
                            numeroOggettiAcquistati = 1
                        else:
                            numeroOggettiAcquistati += 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        numeroOggettiAcquistati = 1
            if tastop == pygame.K_a and voceMarcata != 0:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gsx // 32 * 4
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 0:
                    if oggetton != 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        oggetton = oggetton + 1
                        yp = yp + GlobalVarG2.gsy // 18 * 0.9
                    elif oggetton == 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 6.1
                        oggetton = 0
                elif voceMarcata != 0:
                    if oggetton != 11:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = 99 - dati[30 + oggetton]
                        elif oggetton == 0 and numeroOggettiAcquistati == 1:
                            numeroOggettiAcquistati = maxFrecce - dati[132]
                        else:
                            numeroOggettiAcquistati -= 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        numeroOggettiAcquistati = 1
            if tastop == pygame.K_d and voceMarcata != 0:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gsx // 32 * 4
            if mouseSinistroPremuto and (mouseInquadraFrecciaSu or mouseInquadraFrecciaGiu):
                if mouseInquadraFrecciaSu:
                    if voceMarcata != 0:
                        if oggetton != 11:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            if 1 <= oggetton <= 10 and numeroOggettiAcquistati + dati[30 + oggetton] >= 99:
                                numeroOggettiAcquistati = 1
                            elif oggetton == 0 and numeroOggettiAcquistati + dati[132] >= maxFrecce:
                                numeroOggettiAcquistati = 1
                            else:
                                numeroOggettiAcquistati += 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            numeroOggettiAcquistati = 1
                elif mouseInquadraFrecciaGiu:
                    if voceMarcata != 0:
                        if oggetton != 11:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            if 1 <= oggetton <= 10 and numeroOggettiAcquistati == 1:
                                numeroOggettiAcquistati = 99 - dati[30 + oggetton]
                            elif oggetton == 0 and numeroOggettiAcquistati == 1:
                                numeroOggettiAcquistati = maxFrecce - dati[132]
                            else:
                                numeroOggettiAcquistati -= 1
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                            numeroOggettiAcquistati = 1

            maxFrecce = 1
            if dati[133] == 1:
                maxFrecce = 5
            elif dati[133] == 2:
                maxFrecce = 20
            elif dati[133] == 3:
                maxFrecce = 60

            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 13.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 20.5, GlobalVarG2.gsy // 18 * 16.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 10.5, GlobalVarG2.gsy // 18 * 16.5))

            GlobalVarG2.schermo.blit(GlobalVarG2.sacchettoDenaroMercante, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 14))
            messaggio("Monete: " + str(dati[131]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 26, GlobalVarG2.gsy // 18 * 15.8, 50)

            GlobalVarG2.schermo.blit(GlobalVarG2.mercanteGraf, (GlobalVarG2.gsx // 32 * 0, GlobalVarG2.gsy // 18 * 8.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoDialogoMercante, (GlobalVarG2.gsx // 32 * 0.5, GlobalVarG2.gsy // 18 * 4))
            if moneteInsufficienti:
                messaggio("Non hai abbastanza monete!", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 2.1, GlobalVarG2.gsy // 18 * 6.1, 40)
            if inventarioPieno:
                messaggio("Non puoi prenderne altri...", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 2.4, GlobalVarG2.gsy // 18 * 5.3, 40)
            if confermaOggettoDaAcquistare == 0:
                messaggio("Prendi quello che ti serve", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.5, 50)
            else:
                messaggio("Quanti te ne servono?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.5, 50)

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            if 1 <= oggetton <= 10:
                GlobalVarG2.schermo.blit(imgOggetti[oggetton - 1], (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
            elif oggetton == 0:
                GlobalVarG2.schermo.blit(GlobalVarG2.frecciaMenu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
            elif oggetton == 11:
                if dati[133] == 0:
                    GlobalVarG2.schermo.blit(GlobalVarG2.faretra1Menu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
                elif dati[133] == 1:
                    GlobalVarG2.schermo.blit(GlobalVarG2.faretra2Menu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.faretra3Menu, (GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3))

            # menu conferma
            if confermaOggettoDaAcquistare != 0:
                # posizionare il cursore sul menu compra
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalVarG2.gsx // 32 * 5.3
                    yp = GlobalVarG2.gsy // 18 * 6.9
                    voceMarcata = 2
                    usauno = False
                GlobalVarG2.schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("x" + str(numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 4.5, 50)
                if oggetton == 11:
                    GlobalVarG2.schermo.blit(GlobalVarG2.scorriSuGiuBloccato, (GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * 4.3))
                    if dati[133] == 1:
                        messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton + 1] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                    elif dati[133] >= 2:
                        messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton + 2] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                    else:
                        messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                else:
                    GlobalVarG2.schermo.blit(GlobalVarG2.scorriSuGiu, (GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * 4.3))
                    messaggio("(Monete necessarie: %i)" % (GlobalVarG2.costoOggetti[oggetton] * numeroOggettiAcquistati), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 5.3, 50)
                messaggio("Conferma", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.9, 50)
                messaggio("Annulla", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 6, GlobalVarG2.gsy // 18 * 6.9, 50)

            messaggio("Acquista oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Oggetti acquistabili", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 4.8, 40)
            messaggio("Costo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.5, GlobalVarG2.gsy // 18 * 4.8, 40)
            messaggio("Posseduti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 4.8, 40)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigiochi, (int(GlobalVarG2.gpx * 11), int(GlobalVarG2.gpy * 5.5)), (int(GlobalVarG2.gpx * 21), int(GlobalVarG2.gpy * 5.5)), 1)

            messaggio("Freccia", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 6.2, 40)
            messaggio(str(GlobalVarG2.costoOggetti[0]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 6.2, 40)
            messaggio("x%i" % dati[132], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 6.2, 40)
            if oggetton == 0:
                messaggio("Freccia:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                messaggio("Usate per attaccare i nemici a distanza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            if imgOggetti[0] != sconosciutoOggetto:
                messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 7.1, 40)
                messaggio(str(GlobalVarG2.costoOggetti[1]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 7.1, 40)
                if dati[31] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 7.1, 40)
                else:
                    messaggio("x%i" % dati[31], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 7.1, 40)
                if oggetton == 1:
                    messaggio("Pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 100 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 7.1, 40)
            if imgOggetti[1] != sconosciutoOggetto:
                messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8, 40)
                messaggio(str(GlobalVarG2.costoOggetti[2]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 8, 40)
                if dati[32] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8, 40)
                else:
                    messaggio("x%i" % dati[32], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8, 40)
                if oggetton == 2:
                    messaggio("Caricabatterie:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 250 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8, 40)
            if imgOggetti[2] != sconosciutoOggetto:
                messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.9, 40)
                messaggio(str(GlobalVarG2.costoOggetti[3]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 8.9, 40)
                if dati[33] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8.9, 40)
                else:
                    messaggio("x%i" % dati[33], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 8.9, 40)
                if oggetton == 3:
                    messaggio("Medicina:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.9, 40)
            if imgOggetti[3] != sconosciutoOggetto:
                messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 9.8, 40)
                messaggio(str(GlobalVarG2.costoOggetti[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 9.8, 40)
                if dati[34] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.8, 40)
                else:
                    messaggio("x%i" % dati[34], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 9.8, 40)
                if oggetton == 4:
                    messaggio("Super pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 300 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 9.8, 40)
            if imgOggetti[4] != sconosciutoOggetto:
                messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.7, 40)
                messaggio(str(GlobalVarG2.costoOggetti[5]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 10.7, 40)
                if dati[35] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 10.7, 40)
                else:
                    messaggio("x%i" % dati[35], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 10.7, 40)
                if oggetton == 5:
                    messaggio("Carica plus:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Recupera 600 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.7, 40)
            if imgOggetti[5] != sconosciutoOggetto:
                messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 11.6, 40)
                messaggio(str(GlobalVarG2.costoOggetti[6]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 11.6, 40)
                if dati[36] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 11.6, 40)
                else:
                    messaggio("x%i" % dati[36], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 11.6, 40)
                if oggetton == 6:
                    messaggio("Bomba:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Infligge un po' di danni ai nemici su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 11.6, 40)
            if imgOggetti[6] != sconosciutoOggetto:
                messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.5, 40)
                messaggio(str(GlobalVarG2.costoOggetti[7]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 12.5, 40)
                if dati[37] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 12.5, 40)
                else:
                    messaggio("x%i" % dati[37], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 12.5, 40)
                if oggetton == 7:
                    messaggio("Bomba velenosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Infligge avvelenamento al nemico su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.5, 40)
            if imgOggetti[7] != sconosciutoOggetto:
                messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 13.4, 40)
                messaggio(str(GlobalVarG2.costoOggetti[8]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 13.4, 40)
                if dati[38] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 13.4, 40)
                else:
                    messaggio("x%i" % dati[38], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 13.4, 40)
                if oggetton == 8:
                    messaggio("Esca:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio(u"Distrae i nemici finché non viene distrutta. È", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("possibile riprenderla passandoci sopra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 13.4, 40)
            if imgOggetti[8] != sconosciutoOggetto:
                messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.3, 40)
                messaggio(str(GlobalVarG2.costoOggetti[9]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 14.3, 40)
                if dati[39] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 14.3, 40)
                else:
                    messaggio("x%i" % dati[39], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 14.3, 40)
                if oggetton == 9:
                    messaggio("Bomba appiccicosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio(u"Dimezza la velocità del nemico su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.3, 40)
            if imgOggetti[9] != sconosciutoOggetto:
                messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 15.2, 40)
                messaggio(str(GlobalVarG2.costoOggetti[10]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 15.2, 40)
                if dati[40] < 0:
                    messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 15.2, 40)
                else:
                    messaggio("x%i" % dati[40], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 15.2, 40)
                if oggetton == 10:
                    messaggio("Bomba potenziata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                    messaggio("Infligge molti danni ai nemici su cui viene", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                    messaggio("lanciata in un vasto raggio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)
            else:
                messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 15.2, 40)
            messaggio("Faretra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] == 0:
                messaggio(str(GlobalVarG2.costoOggetti[11]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] == 1:
                messaggio(str(GlobalVarG2.costoOggetti[12]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] >= 2:
                messaggio(str(GlobalVarG2.costoOggetti[13]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.8, GlobalVarG2.gsy // 18 * 16.1, 40)
            if dati[133] == 3:
                messaggio("x1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 16.1, 40)
            else:
                messaggio("x0", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19, GlobalVarG2.gsy // 18 * 16.1, 40)
            if oggetton == 11:
                messaggio("Faretra:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 11.5, 60)
                messaggio(u"Permette di trasportare più frecce", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 12.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 13.5, 35)

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if confermaOggettoDaAcquistare == 0:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 0.7))), (xp + (int(GlobalVarG2.gpx * 9.5)), yp + (int(GlobalVarG2.gpy * 0.7))), 2)
            else:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xpv + (int(GlobalVarG2.gpx // 1.5))), ypv + (int(GlobalVarG2.gpy * 0.7))), (xpv + (int(GlobalVarG2.gpx * 9.5)), ypv + (int(GlobalVarG2.gpy * 0.7))), 2)
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)

    GlobalVarG2.canaleSoundCanzone.stop()
    return dati
