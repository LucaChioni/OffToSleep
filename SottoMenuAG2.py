# -*- coding: utf-8 -*-

from SottoMenuBG2 import *


def equip(dati, canzone):
    perssta = pygame.transform.scale(GlobalVarG2.perso, (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    persstab = pygame.transform.scale(GlobalVarG2.persob, (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sfondoOggetto = pygame.transform.scale(GlobalVarG2.sfondoOggettoMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    sconosciutoEquip = pygame.transform.scale(GlobalVarG2.sconosciutoEquipMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 6.8
    risposta = False
    voceMarcata = 1
    primoFrame = True
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
    spada = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    arco = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    scudo = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    armatura = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    guanti = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    collana = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    carim = False

    vetImgSpade = []
    vetImgArchi = []
    vetImgArmature = []
    vetImgScudi = []
    vetImgGuanti = []
    vetImgCollane = []
    i = 0
    while i < 5:
        if dati[41 + i] > 0:
            vetImgSpade.append(GlobalVarG2.vetImgSpadeMenu[i])
        else:
            vetImgSpade.append(sconosciutoEquip)
        if dati[46 + i] > 0:
            vetImgArchi.append(GlobalVarG2.vetImgArchiMenu[i])
        else:
            vetImgArchi.append(sconosciutoEquip)
        if dati[51 + i] > 0:
            vetImgArmature.append(GlobalVarG2.vetImgArmatureMenu[i])
        else:
            vetImgArmature.append(sconosciutoEquip)
        if dati[56 + i] > 0:
            vetImgScudi.append(GlobalVarG2.vetImgScudiMenu[i])
        else:
            vetImgScudi.append(sconosciutoEquip)
        if dati[61 + i] > 0:
            vetImgGuanti.append(GlobalVarG2.vetImgGuantiMenu[i])
        else:
            vetImgGuanti.append(sconosciutoEquip)
        if dati[66 + i] > 0:
            vetImgCollane.append(GlobalVarG2.vetImgCollaneMenu[i])
        else:
            vetImgCollane.append(sconosciutoEquip)
        i += 1

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

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
            if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 4.5:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 4.5 <= xMouse <= GlobalVarG2.gsx // 32 * 8:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 4.5
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 4.5
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 4.5
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 4.5
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVarG2.gsx // 32 * 4.5
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 8 <= xMouse <= GlobalVarG2.gsx // 32 * 11.5:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 11.5 <= xMouse <= GlobalVarG2.gsx // 32 * 15:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVarG2.gsx // 32 * 11.5
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVarG2.gsx // 32 * 11.5
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVarG2.gsx // 32 * 11.5
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVarG2.gsx // 32 * 11.5
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVarG2.gsx // 32 * 11.5
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 15 <= xMouse <= GlobalVarG2.gsx // 32 * 18.5:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 21
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 22
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 23
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 24
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 25
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 18.5 <= xMouse <= GlobalVarG2.gsx // 32 * 22:
                if GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 26
                    xp = GlobalVarG2.gsx // 32 * 18.5
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 27
                    xp = GlobalVarG2.gsx // 32 * 18.5
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 28
                    xp = GlobalVarG2.gsx // 32 * 18.5
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 29
                    xp = GlobalVarG2.gsx // 32 * 18.5
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 30
                    xp = GlobalVarG2.gsx // 32 * 18.5
                    yp = GlobalVarG2.gsy // 18 * 14.8
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
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                risposta = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                carim = True
                # progresso-stanza-x-y-liv-pv-spada-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                # spade
                if voceMarcata == 1:
                    if dati[41] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[6] = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 2:
                    if dati[42] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[6] = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 3:
                    if dati[43] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[6] = 2
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 4:
                    if dati[44] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[6] = 3
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 5:
                    if dati[45] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[6] = 4
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                # spade
                if voceMarcata == 6:
                    if dati[46] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[128] = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 7:
                    if dati[47] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[128] = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 8:
                    if dati[48] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[128] = 2
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 9:
                    if dati[49] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[128] = 3
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 10:
                    if dati[50] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[128] = 4
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                # armature
                if voceMarcata == 11:
                    if dati[51] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[8] = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 12:
                    if dati[52] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[8] = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 13:
                    if dati[53] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[8] = 2
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 14:
                    if dati[54] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[8] = 3
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 15:
                    if dati[55] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[8] = 4
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                # scudi
                if voceMarcata == 16:
                    if dati[56] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[7] = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 17:
                    if dati[57] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[7] = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 18:
                    if dati[58] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[7] = 2
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 19:
                    if dati[59] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[7] = 3
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 20:
                    if dati[60] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[7] = 4
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                # guanti
                if voceMarcata == 21:
                    if dati[61] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[129] = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 22:
                    if dati[62] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[129] = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 23:
                    if dati[63] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[129] = 2
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 24:
                    if dati[64] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[129] = 3
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 25:
                    if dati[65] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[129] = 4
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                # collane
                if voceMarcata == 26:
                    if dati[66] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[130] = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 27:
                    if dati[67] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[130] = 1
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 28:
                    if dati[68] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[130] = 2
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 29:
                    if dati[69] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[130] = 3
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                if voceMarcata == 30:
                    if dati[70] != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        dati[130] = 4
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

        if primoMovimento or tastop == pygame.K_q or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_d or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_w) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_d or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_w):
                tastotempfps = 2
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 5 or voceMarcata == 10 or voceMarcata == 15 or voceMarcata == 20 or voceMarcata == 25 or voceMarcata == 30:
                    voceMarcata -= 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 6.8
                else:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp += GlobalVarG2.gsy // 18 * 2
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1 or voceMarcata == 6 or voceMarcata == 11 or voceMarcata == 16 or voceMarcata == 21 or voceMarcata == 26:
                    voceMarcata += 4
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 14.8
                else:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp - GlobalVarG2.gsy // 18 * 2
            if tastop == pygame.K_d:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 26 or voceMarcata == 27 or voceMarcata == 28 or voceMarcata == 29 or voceMarcata == 30:
                    voceMarcata -= 25
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 1
                else:
                    voceMarcata += 5
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gsx // 32 * 3.5
            if tastop == pygame.K_a:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata += 25
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 18.5
                else:
                    voceMarcata -= 5
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gsx // 32 * 3.5
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 21, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            # linea(dove,colore,inizio,fine,spessore)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 4.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 4.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 8, (GlobalVarG2.gsy // 18 * 4) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 8, (GlobalVarG2.gsy // 18 * 15.5) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 20)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 11.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 11.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 15, (GlobalVarG2.gsy // 18 * 4) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 15, (GlobalVarG2.gsy // 18 * 15.5) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 20)
            pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 18.5, (GlobalVarG2.gsy // 18 * 5.5) + (GlobalVarG2.gpy // 2)), (GlobalVarG2.gsx // 32 * 18.5, (GlobalVarG2.gsy // 18 * 15) + (GlobalVarG2.gpy // 2)), GlobalVarG2.gpx // 30)

            if carim:
                spada = pygame.transform.scale(GlobalVarG2.vetImgSpadePixellate[dati[6]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                arco = pygame.transform.scale(GlobalVarG2.vetImgArchiPixellate[dati[128]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                scudo = pygame.transform.scale(GlobalVarG2.vetImgScudiPixellate[dati[7]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                armatura = pygame.transform.scale(GlobalVarG2.vetImgArmaturePixellate[dati[8]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                guanti = pygame.transform.scale(GlobalVarG2.vetImgGuantiPixellate[dati[129]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                collana = pygame.transform.scale(GlobalVarG2.vetImgCollanePixellate[dati[130]], (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
                carim = False
            messaggio("Equipaggiamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Armi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 3.6, GlobalVarG2.gsy // 18 * 4.3, 60)
            messaggio("Spade", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 1.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgSpade[i], (GlobalVarG2.gsx // 32 * 1.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Archi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 5.5, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 5.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgArchi[i], (GlobalVarG2.gsx // 32 * 5.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Protezioni", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.6, GlobalVarG2.gsy // 18 * 4.3, 60)
            messaggio("Armature", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.4, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 8.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgArmature[i], (GlobalVarG2.gsx // 32 * 8.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Scudi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 12.5, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 12.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgScudi[i], (GlobalVarG2.gsx // 32 * 12.2, int((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Accessori", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16.7, GlobalVarG2.gsy // 18 * 4.3, 60)
            messaggio("Guanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 15.8, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 15.7, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgGuanti[i], (GlobalVarG2.gsx // 32 * 15.7, int((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
                i += 1
            messaggio("Collane", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 19.2, GlobalVarG2.gsy // 18 * 5.3, 50)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 19.2, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetImgCollane[i], (GlobalVarG2.gsx // 32 * 19.2, ((GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy * 2 * i))))
                i += 1

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
            if dati[5] > pvtot:
                dati[5] = pvtot

            GlobalVarG2.schermo.blit(arco, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(perssta, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(persstab, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(armatura, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(collana, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(spada, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(guanti, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            GlobalVarG2.schermo.blit(scudo, (GlobalVarG2.gsx // 32 * 24.5, GlobalVarG2.gsy // 18 * 11.3))
            messaggio("Statistiche:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 6.7, 50)
            messaggio("Punti vita: %i" % pvtot, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 7.5, 35)
            messaggio("Attacco ravvicinato: %i" % attVicino, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 8, 35)
            messaggio("Attacco a distanza: %i" % attLontano, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % dif, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9, 35)
            messaggio(u"Probabilità parata: %i" % par + "%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 9.5, 35)
            # confronto statistiche
            # spade
            if voceMarcata == 1:
                if dati[41] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi spada", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 2:
                if dati[42] != 0:
                    messaggio("Spada di ferro:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice spada di ferro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 10 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 3:
                if dati[43] != 0:
                    messaggio("Spadone d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Grande spadone in acciaio con ornamenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("in oro. Rappresenta il modello di spada", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("migliore mai prodotto dall'uomo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 40 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 4:
                if dati[44] != 0:
                    messaggio("Lykother:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Spada molto leggera e affilata. Si dice che in", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("origine fosse un dente di un lupo enorme", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 90 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            if voceMarcata == 5:
                if dati[45] != 0:
                    messaggio("Mendaxritas:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Potentissima spada composta da materiali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("ignoti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 160 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                    elif dati[6] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
            # archi
            if voceMarcata == 6:
                if dati[46] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi arco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 0 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 0:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 7:
                if dati[47] != 0:
                    messaggio("Arco di legno:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice arco in legno usato dalla maggior", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("parte dei forestieri", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 5 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 1:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 1:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 8:
                if dati[48] != 0:
                    messaggio("Arco di ferro:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Elaborato arco in ferro usato solo dai più", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("esperti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 20 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 2:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 2:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 9:
                if dati[49] != 0:
                    messaggio("Arco di precisione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato arco in legno e acciaio. Molto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("leggero e potente. Massima espressione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("dell'ingegno umano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 45 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 3:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 3:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            if voceMarcata == 10:
                if dati[50] != 0:
                    messaggio("Accipiter:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Potentissimo arco di origine sconosciuta", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diffAtt = 80 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 4:
                        messaggio(str(diffAtt), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[128] < 4:
                        messaggio("+" + str(diffAtt), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            # armature
            if voceMarcata == 11:
                if dati[51] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi armatura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 12:
                if dati[52] != 0:
                    messaggio("Armatura di pelle:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice armatura in pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 10 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 13:
                if dati[53] != 0:
                    messaggio("Armatura d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Grande armatura d'acciaio con ornamenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("in oro. Usata solo dagli ufficiali", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("dell'esercito", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 40 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 14:
                if dati[54] != 0:
                    messaggio("Lykodes:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Armatura formata da materiali leggieri e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("resistenti. Si dice essere composta da ossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("di un enorme lupo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 90 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 15:
                if dati[55] != 0:
                    messaggio("Loriquam:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Armatura incredibilmente resistente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"La sua origine è ignota", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 160 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[8] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            # scudi
            if voceMarcata == 16:
                if dati[56] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 0:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 17:
                if dati[57] != 0:
                    messaggio("Scudo di pelle:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Semplice scudo in pelle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 5 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 3 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 1:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 18:
                if dati[58] != 0:
                    messaggio("Scudo d'acciaio:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato scudo in acciaio e oro. Studiato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"per respingere gli attacchi più pesanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 20 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 12 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 2:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 19:
                if dati[59] != 0:
                    messaggio("Lykethmos:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Scudo molto leggere e resistente. Si dice", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"essere composto dalle ossa più resistenti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("di un enorme lupo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 45 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 27 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 3:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 20:
                if dati[60] != 0:
                    messaggio("Clipequam:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Scudo incredibilmente resistente. Non è ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("nota l'origine", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    diff = 80 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    diff = 48 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 4:
                        messaggio(str(diff) + "%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff) + "%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            # guanti
            if voceMarcata == 21:
                if dati[61] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi guanti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 22:
                if dati[62] != 0:
                    messaggio("Guanti vitali:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che aumentano i punti vita massimi", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("del portatore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 1:
                        messaggio("+50", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    if dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 23:
                if dati[63] != 0:
                    messaggio("Guanti difensivi:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono di subire meno danno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("grazie ad una presa salda dello scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 2:
                        messaggio("+30", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 24:
                if dati[64] != 0:
                    messaggio("Guanti offensivi:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono una presa salda", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("dell'arma. Aumentano l'attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 3:
                        messaggio("+20", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("+20", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
            if voceMarcata == 25:
                if dati[65] != 0:
                    messaggio("Guanti confortevoli:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Guanti che aumentano la probabilità di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("parare gli attacchi grazie ad una presa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("agevole dello scudo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
                    if dati[129] != 4:
                        messaggio("+10%", GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
            # collane
            if voceMarcata == 26:
                if dati[66] != 0:
                    messaggio("Niente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi collana", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 27:
                if dati[67] != 0:
                    messaggio("Collana medicinale:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio(u"neutralizza la tissicità del veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio(u"(non ha effetto se si è già avvelenati)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 28:
                if dati[68] != 0:
                    messaggio("Collana rigenerante:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("ripristina punti vita ogni turno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 29:
                if dati[69] != 0:
                    messaggio("Apprendimaschera:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che consente di ricevere più punti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("esperienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)
            if voceMarcata == 30:
                if dati[70] != 0:
                    messaggio("Portafortuna:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che permette di ottenere più monete", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 4.8, 35)
                    messaggio("dai nemici", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 23, GlobalVarG2.gsy // 18 * 5.8, 35)

            # puntatore vecchio
            if dati[6] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 6.8))
            if dati[6] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 8.8))
            if dati[6] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 10.8))
            if dati[6] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 12.8))
            if dati[6] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 14.8))
            if dati[128] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 6.8))
            if dati[128] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 8.8))
            if dati[128] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 10.8))
            if dati[128] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 12.8))
            if dati[128] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 4.5, GlobalVarG2.gsy // 18 * 14.8))
            if dati[8] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 6.8))
            if dati[8] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 8.8))
            if dati[8] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 10.8))
            if dati[8] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 12.8))
            if dati[8] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 14.8))
            if dati[7] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 6.8))
            if dati[7] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 8.8))
            if dati[7] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 10.8))
            if dati[7] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 12.8))
            if dati[7] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 11.5, GlobalVarG2.gsy // 18 * 14.8))
            if dati[129] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 6.8))
            if dati[129] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 8.8))
            if dati[129] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 10.8))
            if dati[129] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.8))
            if dati[129] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 14.8))
            if dati[130] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 6.8))
            if dati[130] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 8.8))
            if dati[130] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 10.8))
            if dati[130] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 12.8))
            if dati[130] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 18.5, GlobalVarG2.gsy // 18 * 14.8))

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati


def sceglicondiz(dati, condizione, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0
    primoFrame = True
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    # carico le scenette
    scecond = GlobalVarG2.vetImgCondizioniMenu

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

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
            if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 8:
                if GlobalVarG2.gsy // 18 * 4.4 <= yMouse <= GlobalVarG2.gsy // 18 * 5.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 0
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 4.6
                elif GlobalVarG2.gsy // 18 * 5.9 <= yMouse <= GlobalVarG2.gsy // 18 * 6.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.1
                elif GlobalVarG2.gsy // 18 * 6.9 <= yMouse <= GlobalVarG2.gsy // 18 * 7.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 7.1
                elif GlobalVarG2.gsy // 18 * 7.9 <= yMouse <= GlobalVarG2.gsy // 18 * 8.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8.1
                elif GlobalVarG2.gsy // 18 * 8.9 <= yMouse <= GlobalVarG2.gsy // 18 * 9.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 9.1
                elif GlobalVarG2.gsy // 18 * 9.9 <= yMouse <= GlobalVarG2.gsy // 18 * 10.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 10.1
                elif GlobalVarG2.gsy // 18 * 10.9 <= yMouse <= GlobalVarG2.gsy // 18 * 11.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 11.1
                elif GlobalVarG2.gsy // 18 * 11.9 <= yMouse <= GlobalVarG2.gsy // 18 * 12.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12.1
                elif GlobalVarG2.gsy // 18 * 12.9 <= yMouse <= GlobalVarG2.gsy // 18 * 13.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 13.1
                elif GlobalVarG2.gsy // 18 * 13.9 <= yMouse <= GlobalVarG2.gsy // 18 * 14.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 14.1
                elif GlobalVarG2.gsy // 18 * 14.9 <= yMouse <= GlobalVarG2.gsy // 18 * 15.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 15.1
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 8 <= xMouse <= GlobalVarG2.gsx // 32 * 16:
                if GlobalVarG2.gsy // 18 * 5.9 <= yMouse <= GlobalVarG2.gsy // 18 * 6.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 6.1
                elif GlobalVarG2.gsy // 18 * 6.9 <= yMouse <= GlobalVarG2.gsy // 18 * 7.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 7.1
                elif GlobalVarG2.gsy // 18 * 7.9 <= yMouse <= GlobalVarG2.gsy // 18 * 8.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 8.1
                elif GlobalVarG2.gsy // 18 * 8.9 <= yMouse <= GlobalVarG2.gsy // 18 * 9.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 9.1
                elif GlobalVarG2.gsy // 18 * 9.9 <= yMouse <= GlobalVarG2.gsy // 18 * 10.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 10.1
                elif GlobalVarG2.gsy // 18 * 10.9 <= yMouse <= GlobalVarG2.gsy // 18 * 11.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 11.1
                elif GlobalVarG2.gsy // 18 * 11.9 <= yMouse <= GlobalVarG2.gsy // 18 * 12.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 12.1
                elif GlobalVarG2.gsy // 18 * 12.9 <= yMouse <= GlobalVarG2.gsy // 18 * 13.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 13.1
                elif GlobalVarG2.gsy // 18 * 13.9 <= yMouse <= GlobalVarG2.gsy // 18 * 14.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 14.1
                elif GlobalVarG2.gsy // 18 * 14.9 <= yMouse <= GlobalVarG2.gsy // 18 * 15.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 15.1
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
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                risposta = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True

                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
                i = 81
                c = 1
                while i <= 100:
                    if voceMarcata == c:
                        if dati[i] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            return c
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    i += 1
                    c += 1
                if voceMarcata == 0:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    return 0
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1.5
                        xp = GlobalVarG2.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
                else:
                    if voceMarcata != 0:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1
                    else:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
            if tastop == pygame.K_a:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp - GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 8
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 4.6
                            xp = GlobalVarG2.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp + GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_d:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp + GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 1
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            messaggio("Scegli condizione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Cancella", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.7, 45)
            if voceMarcata == 0:
                messaggio("Cancella:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            if dati[81] > 0:
                messaggio("Rallo con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 1:
                    GlobalVarG2.schermo.blit(scecond[1], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con pv < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[82] > 0:
                messaggio("Rallo con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 2:
                    GlobalVarG2.schermo.blit(scecond[2], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con pv < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[83] > 0:
                messaggio("Rallo con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 3:
                    GlobalVarG2.schermo.blit(scecond[3], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con pv < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo quando ha pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[84] > 0:
                messaggio("Rallo con veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(scecond[4], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Rallo con veleno:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Rallo quando è avvelenato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[85] > 0:
                messaggio("Colco surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(scecond[5], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco surriscaldato:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Colco quando è surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[86] > 0:
                messaggio("Colco con pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 6:
                    GlobalVarG2.schermo.blit(scecond[6], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco con pe < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[87] > 0:
                messaggio("Colco con pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 7:
                    GlobalVarG2.schermo.blit(scecond[7], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco con pe < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[88] > 0:
                messaggio("Colco con pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 8:
                    GlobalVarG2.schermo.blit(scecond[8], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Colco con pe < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco quando ha pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[89] > 0:
                messaggio("Sempre a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 9:
                    GlobalVarG2.schermo.blit(scecond[9], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Sempre a Rallo:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Rallo in continuazione (se la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio(u"è attivo)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[90] > 0:
                messaggio("Sempre a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 10:
                    GlobalVarG2.schermo.blit(scecond[10], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Sempre a Colco:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Colco in continuazione (se la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("comporta uno status alterativo, viene eseguita solo se lo status non", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio(u"è attivo)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
            if dati[91] > 0:
                messaggio("Nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 11:
                    GlobalVarG2.schermo.blit(scecond[11], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico a caso:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[92] > 0:
                messaggio("Nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 12:
                    GlobalVarG2.schermo.blit(scecond[12], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico vicino:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico più vicino a Colco nel raggio di 2 caselle", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[93] > 0:
                messaggio("Nemico lontano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 13:
                    GlobalVarG2.schermo.blit(scecond[13], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico lontano:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("vicino a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[94] > 0:
                messaggio("Nemico con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 14:
                    GlobalVarG2.schermo.blit(scecond[14], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con pv < 80%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 80% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[95] > 0:
                messaggio("Nemico con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 15:
                    GlobalVarG2.schermo.blit(scecond[15], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con pv < 50%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 50% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[96] > 0:
                messaggio("Nemico con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 16:
                    GlobalVarG2.schermo.blit(scecond[16], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con pv < 30%:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico con pv < 30% (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[97] > 0:
                messaggio("Nemico con meno pv", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 17:
                    GlobalVarG2.schermo.blit(scecond[17], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Nemico con meno pv:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione sul nemico con meno pv (in caso di molteplici bersagli,", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"esegue l'azione su quello più vicino a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[98] > 0:
                messaggio("Numero di nemici > 1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 18:
                    GlobalVarG2.schermo.blit(scecond[18], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Numero di nemici > 1:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[99] > 0:
                messaggio("Numero di nemici > 4", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 19:
                    GlobalVarG2.schermo.blit(scecond[19], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Numero di nemici > 4:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[100] > 0:
                messaggio("Numero di nemici > 7", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 20:
                    GlobalVarG2.schermo.blit(scecond[20], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Numero di nemici > 7:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio(u"tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("a Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if condizione == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6.1
            while i <= 20:
                if condizione == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            if condizione == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.6))

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return condizione


def sceglitecn(dati, tecnica, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0
    primoFrame = True
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    # carico le scenette
    scetecn = GlobalVarG2.vetImgTecnicheMenu

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

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
            if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 8:
                if GlobalVarG2.gsy // 18 * 4.4 <= yMouse <= GlobalVarG2.gsy // 18 * 5.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 0
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 4.6
                elif GlobalVarG2.gsy // 18 * 5.9 <= yMouse <= GlobalVarG2.gsy // 18 * 6.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.1
                elif GlobalVarG2.gsy // 18 * 6.9 <= yMouse <= GlobalVarG2.gsy // 18 * 7.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 7.1
                elif GlobalVarG2.gsy // 18 * 7.9 <= yMouse <= GlobalVarG2.gsy // 18 * 8.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8.1
                elif GlobalVarG2.gsy // 18 * 8.9 <= yMouse <= GlobalVarG2.gsy // 18 * 9.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 9.1
                elif GlobalVarG2.gsy // 18 * 9.9 <= yMouse <= GlobalVarG2.gsy // 18 * 10.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 10.1
                elif GlobalVarG2.gsy // 18 * 10.9 <= yMouse <= GlobalVarG2.gsy // 18 * 11.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 11.1
                elif GlobalVarG2.gsy // 18 * 11.9 <= yMouse <= GlobalVarG2.gsy // 18 * 12.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12.1
                elif GlobalVarG2.gsy // 18 * 12.9 <= yMouse <= GlobalVarG2.gsy // 18 * 13.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 13.1
                elif GlobalVarG2.gsy // 18 * 13.9 <= yMouse <= GlobalVarG2.gsy // 18 * 14.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 14.1
                elif GlobalVarG2.gsy // 18 * 14.9 <= yMouse <= GlobalVarG2.gsy // 18 * 15.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 15.1
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif GlobalVarG2.gsx // 32 * 8 <= xMouse <= GlobalVarG2.gsx // 32 * 16:
                if GlobalVarG2.gsy // 18 * 5.9 <= yMouse <= GlobalVarG2.gsy // 18 * 6.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 6.1
                elif GlobalVarG2.gsy // 18 * 6.9 <= yMouse <= GlobalVarG2.gsy // 18 * 7.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 7.1
                elif GlobalVarG2.gsy // 18 * 7.9 <= yMouse <= GlobalVarG2.gsy // 18 * 8.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 8.1
                elif GlobalVarG2.gsy // 18 * 8.9 <= yMouse <= GlobalVarG2.gsy // 18 * 9.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 9.1
                elif GlobalVarG2.gsy // 18 * 9.9 <= yMouse <= GlobalVarG2.gsy // 18 * 10.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 10.1
                elif GlobalVarG2.gsy // 18 * 10.9 <= yMouse <= GlobalVarG2.gsy // 18 * 11.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 11.1
                elif GlobalVarG2.gsy // 18 * 11.9 <= yMouse <= GlobalVarG2.gsy // 18 * 12.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 12.1
                elif GlobalVarG2.gsy // 18 * 12.9 <= yMouse <= GlobalVarG2.gsy // 18 * 13.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 13.1
                elif GlobalVarG2.gsy // 18 * 13.9 <= yMouse <= GlobalVarG2.gsy // 18 * 14.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 14.1
                elif GlobalVarG2.gsy // 18 * 14.9 <= yMouse <= GlobalVarG2.gsy // 18 * 15.9:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVarG2.gsx // 32 * 8
                    yp = GlobalVarG2.gsy // 18 * 15.1
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
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                risposta = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOsinistroMouse"
                tastoTrovato = True
                i = 11
                c = 1
                while i <= 30:
                    if voceMarcata == c:
                        if dati[i] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            tecnica = c
                            risposta = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        break
                    i += 1
                    c += 1
                if voceMarcata == 0:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    tecnica = 0
                    risposta = True
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == "spazioOsinistroMouse" or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1.5
                        xp = GlobalVarG2.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
                else:
                    if voceMarcata == 0:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    else:
                        voceMarcata -= 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp - GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_a:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp - GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 8
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = yp + GlobalVarG2.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 4.6
                            xp = GlobalVarG2.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        yp = yp + GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_d:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = xp + GlobalVarG2.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        xp = GlobalVarG2.gsx // 32 * 1
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 15, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            messaggio("Scegli tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            messaggio("Cancella", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.7, 45)
            if voceMarcata == 0:
                messaggio("Cancella:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            if dati[11] > 0:
                messaggio("Scossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 1:
                    GlobalVarG2.schermo.blit(scetecn[1], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Scossa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[0]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[12] > 0:
                messaggio("Cura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 2:
                    GlobalVarG2.schermo.blit(scetecn[2], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Cura:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[1]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Recupera un po' di pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[13] > 0:
                messaggio("Antidoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 3:
                    GlobalVarG2.schermo.blit(scetecn[3], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Antidoto:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[2]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[14] > 0:
                messaggio("Freccia elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 4:
                    GlobalVarG2.schermo.blit(scetecn[4], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Freccia elettrica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[3]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[15] > 0:
                messaggio("Tempesta elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 5:
                    GlobalVarG2.schermo.blit(scetecn[5], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Tempesta elettrica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[4]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[16] > 0:
                messaggio("Raffreddamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 6:
                    GlobalVarG2.schermo.blit(scetecn[6], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Raffreddamento:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[5]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[17] > 0:
                messaggio("Auto-ricarica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 7:
                    GlobalVarG2.schermo.blit(scetecn[7], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Auto-ricarica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[6]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Ricarica un po' Colco ma richiede due turni e provoca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[18] > 0:
                messaggio("Cura +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 8:
                    GlobalVarG2.schermo.blit(scetecn[8], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Cura +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[7]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("recupera molti pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[19] > 0:
                messaggio("Scossa +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 9:
                    GlobalVarG2.schermo.blit(scetecn[9], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Scossa +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[8]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[20] > 0:
                messaggio("Freccia elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 10:
                    GlobalVarG2.schermo.blit(scetecn[10], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Freccia elettrica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[9]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15.2, 40)
            if dati[21] > 0:
                messaggio("Velocizza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
                if voceMarcata == 11:
                    GlobalVarG2.schermo.blit(scetecn[11], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Velocizza:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[10]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Permette a Colco, se non surriscaldato, di eseguire due azioni al turno.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("Dopo 15 turni provoca surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 6.2, 40)
            if dati[22] > 0:
                messaggio("Carica attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
                if voceMarcata == 12:
                    GlobalVarG2.schermo.blit(scetecn[12], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Carica attacco:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[11]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Incrementa l'attacco di Rallo per 10 turni (non ha effetto sui nemici)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 7.2, 40)
            if dati[23] > 0:
                messaggio("Carica difesa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
                if voceMarcata == 13:
                    GlobalVarG2.schermo.blit(scetecn[13], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Carica difesa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[12]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Incrementa la difesa di Rallo per 10 turni (non ha effetto sui nemici)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 8.2, 40)
            if dati[24] > 0:
                messaggio("Efficienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
                if voceMarcata == 14:
                    GlobalVarG2.schermo.blit(scetecn[14], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Efficienza:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[13]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio(u"Tutte le tecniche costano la metà dei pe per 15 turni. Si annulla con", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 9.2, 40)
            if dati[25] > 0:
                messaggio("Tempesta elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
                if voceMarcata == 15:
                    GlobalVarG2.schermo.blit(scetecn[15], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Tempesta elettrica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[14]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 10.2, 40)
            if dati[26] > 0:
                messaggio("Cura ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
                if voceMarcata == 16:
                    GlobalVarG2.schermo.blit(scetecn[16], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Cura ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[15]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio(u"Recupera un enorme quantità dei pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 11.2, 40)
            if dati[27] > 0:
                messaggio("Auto-ricarica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
                if voceMarcata == 17:
                    GlobalVarG2.schermo.blit(scetecn[17], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Auto-ricarica +:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[16]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Ricarica di molto Colco ma richiede due turni e provoca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("surriscaldamento (applicata sempre su Colco)", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 12.2, 40)
            if dati[28] > 0:
                messaggio("Scossa ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
                if voceMarcata == 18:
                    GlobalVarG2.schermo.blit(scetecn[18], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Scossa ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[17]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a un nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 13.2, 40)
            if dati[29] > 0:
                messaggio("Freccia Elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
                if voceMarcata == 19:
                    GlobalVarG2.schermo.blit(scetecn[19], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Freccia Elettrica ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[18]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a distanza a un nemico", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 14.2, 40)
            if dati[30] > 0:
                messaggio("Tempesta elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15.2, 40)
                if voceMarcata == 20:
                    GlobalVarG2.schermo.blit(scetecn[20], (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 4))
                    messaggio("Tempesta elettrica ++:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVarG2.costoTecniche[19]), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 27.5, GlobalVarG2.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9, GlobalVarG2.gsy // 18 * 15, 40)

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if tecnica == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6.1
            while i <= 20:
                if tecnica == i:
                    GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * k))
                i = i + 1
                k = k + 1
            if tecnica == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4.6))

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return tecnica


def equiprobo(dati, canzone):
    robosta = pygame.transform.scale(GlobalVarG2.roboo, (GlobalVarG2.gpx * 5, GlobalVarG2.gpy * 5))
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sfondoOggetto = pygame.transform.scale(GlobalVarG2.sfondoOggettoMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    sconosciutoEquip = pygame.transform.scale(GlobalVarG2.sconosciutoEquipMenu, (int(GlobalVarG2.gpx * 2), int(GlobalVarG2.gpy * 2)))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 6.8
    risposta = False
    riordinamento = False
    annullaRiordinamento = False
    datiPrimaDiRiordinamento = list(dati)
    vxpGambit = xp
    vypGambit = yp
    voceMarcata = 1
    voceGambitMarcata = 0
    primoFrame = True
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    vetImgBatterie = GlobalVarG2.vetImgBatterieMenu

    vetIcoBatterie = []
    i = 0
    while i < 5:
        if dati[41 + i] > 0:
            vetIcoBatterie.append(GlobalVarG2.vetIcoBatterieMenu[i])
        else:
            vetIcoBatterie.append(sconosciutoEquip)
        i += 1

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

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
            if not riordinamento:
                if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 6 and GlobalVarG2.gsy // 18 * 6 <= yMouse <= GlobalVarG2.gsy // 18 * 8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 6.8
                elif GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 6 and GlobalVarG2.gsy // 18 * 8 <= yMouse <= GlobalVarG2.gsy // 18 * 10:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 8.8
                elif GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 6 and GlobalVarG2.gsy // 18 * 10 <= yMouse <= GlobalVarG2.gsy // 18 * 12:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 10.8
                elif GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 6 and GlobalVarG2.gsy // 18 * 12 <= yMouse <= GlobalVarG2.gsy // 18 * 14:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 12.8
                elif GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 6 and GlobalVarG2.gsy // 18 * 14 <= yMouse <= GlobalVarG2.gsy // 18 * 16:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVarG2.gsx // 32 * 1
                    yp = GlobalVarG2.gsy // 18 * 14.8
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 5.7 <= yMouse <= GlobalVarG2.gsy // 18 * 6.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 6
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 7
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 7.7 <= yMouse <= GlobalVarG2.gsy // 18 * 8.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 8
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 8.7 <= yMouse <= GlobalVarG2.gsy // 18 * 9.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 9
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 9.7 <= yMouse <= GlobalVarG2.gsy // 18 * 10.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 10
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 10.7 <= yMouse <= GlobalVarG2.gsy // 18 * 11.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 11
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 12
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 12.7 <= yMouse <= GlobalVarG2.gsy // 18 * 13.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 13
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 13.7 <= yMouse <= GlobalVarG2.gsy // 18 * 14.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 14
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 10 and GlobalVarG2.gsy // 18 * 14.7 <= yMouse <= GlobalVarG2.gsy // 18 * 15.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 15
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 5.7 <= yMouse <= GlobalVarG2.gsy // 18 * 6.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 6
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 7
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 7.7 <= yMouse <= GlobalVarG2.gsy // 18 * 8.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 8
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 8.7 <= yMouse <= GlobalVarG2.gsy // 18 * 9.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 9
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 9.7 <= yMouse <= GlobalVarG2.gsy // 18 * 10.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 10
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 10.7 <= yMouse <= GlobalVarG2.gsy // 18 * 11.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 21
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 11
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 22
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 12
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 12.7 <= yMouse <= GlobalVarG2.gsy // 18 * 13.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 23
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 13
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 13.7 <= yMouse <= GlobalVarG2.gsy // 18 * 14.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 24
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 14
                elif GlobalVarG2.gsx // 32 * 10 <= xMouse <= GlobalVarG2.gsx // 32 * 16.5 and GlobalVarG2.gsy // 18 * 14.7 <= yMouse <= GlobalVarG2.gsy // 18 * 15.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 25
                    xp = GlobalVarG2.gsx // 32 * 10
                    yp = GlobalVarG2.gsy // 18 * 15
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 5.7 <= yMouse <= GlobalVarG2.gsy // 18 * 6.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 26
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 6
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 27
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 7
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 7.7 <= yMouse <= GlobalVarG2.gsy // 18 * 8.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 28
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 8
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 8.7 <= yMouse <= GlobalVarG2.gsy // 18 * 9.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 29
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 9
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 9.7 <= yMouse <= GlobalVarG2.gsy // 18 * 10.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 30
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 10
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 10.7 <= yMouse <= GlobalVarG2.gsy // 18 * 11.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 31
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 11
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 32
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 12
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 12.7 <= yMouse <= GlobalVarG2.gsy // 18 * 13.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 33
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 13
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 13.7 <= yMouse <= GlobalVarG2.gsy // 18 * 14.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 34
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 14
                elif GlobalVarG2.gsx // 32 * 16.5 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 14.7 <= yMouse <= GlobalVarG2.gsy // 18 * 15.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 35
                    xp = GlobalVarG2.gsx // 32 * 16.5
                    yp = GlobalVarG2.gsy // 18 * 15
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            elif riordinamento:
                if GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 5.7 <= yMouse <= GlobalVarG2.gsy // 18 * 6.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 6
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 7
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 7.7 <= yMouse <= GlobalVarG2.gsy // 18 * 8.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 8
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 8.7 <= yMouse <= GlobalVarG2.gsy // 18 * 9.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 9
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 9.7 <= yMouse <= GlobalVarG2.gsy // 18 * 10.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 10
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 10.7 <= yMouse <= GlobalVarG2.gsy // 18 * 11.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 11
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 12
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 12.7 <= yMouse <= GlobalVarG2.gsy // 18 * 13.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 13
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 13.7 <= yMouse <= GlobalVarG2.gsy // 18 * 14.7:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 14
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                elif GlobalVarG2.gsx // 32 * 7 <= xMouse <= GlobalVarG2.gsx // 32 * 23 and GlobalVarG2.gsy // 18 * 14.7 <= yMouse <= GlobalVarG2.gsy // 18 * 15.8:
                    if GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVarG2.gsx // 32 * 7
                    yp = GlobalVarG2.gsy // 18 * 15
                    if voceMarcata > voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i <= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i + 1]
                            dati[111 + i] = dati[111 + i + 1]
                            i += 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
                    elif voceMarcata < voceMarcataVecchia:
                        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
                        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
                        i = voceMarcataVecchia - 6
                        while i >= voceMarcata - 6:
                            dati[101 + i] = dati[101 + i - 1]
                            dati[111 + i] = dati[111 + i - 1]
                            i -= 1
                        dati[101 + voceMarcata - 6] = condizioneSelezionata
                        dati[111 + voceMarcata - 6] = azioneSelezionata
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
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    if not riordinamento:
                        risposta = True
                    else:
                        riordinamento = False
                        annullaRiordinamento = True
                if event.key == pygame.K_s and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and not riordinamento and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and not riordinamento and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastop = "spazioOmouse"
                tastoTrovato = True
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                if not riordinamento:
                    risposta = True
                else:
                    riordinamento = False
                    annullaRiordinamento = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOmouse"
                tastoTrovato = True
                # riordina
                if riordinamento:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    riordinamento = False
                else:
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armrob
                    if voceMarcata == 1:
                        if dati[71] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[9] = 0
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 2:
                        if dati[72] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[9] = 1
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 3:
                        if dati[73] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[9] = 2
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 4:
                        if dati[74] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[9] = 3
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if voceMarcata == 5:
                        if dati[75] != 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            dati[9] = 4
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)

                    # riordina
                    if 6 <= voceMarcata <= 15:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                        riordinamento = True
                        datiPrimaDiRiordinamento = list(dati)
                        vxpGambit = xp
                        vypGambit = yp
                        voceGambitMarcata = voceMarcata

                    # condizioni
                    i = 101
                    c = 16
                    while i <= 110:
                        if voceMarcata == c:
                            if dati[i] != -1:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[i] = sceglicondiz(dati, dati[i], canzone)
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        i += 1
                        c += 1

                    # tecniche
                    i = 111
                    c = 26
                    while i <= 120:
                        if voceMarcata == c:
                            if dati[i] != -1:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                                dati[i] = sceglitecn(dati, dati[i], canzone)
                            else:
                                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                        i += 1
                        c += 1
            elif GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and GlobalVarG2.mouseBloccato:
                GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
            if sinistroMouse or centraleMouse or destroMouse:
                pygame.mouse.set_visible(True)
                GlobalVarG2.mouseVisibile = True
            if event.type == pygame.KEYUP and tastop == event.key:
                tastop = 0
            if event.type == pygame.MOUSEBUTTONUP:
                tastop = 0

        if primoMovimento or tastop == pygame.K_q or tastop == "spazioOmouse" or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if riordinamento:
                    if voceMarcata != 6:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        i = 0
                        while i < 10:
                            if voceMarcata == i + 6:
                                condizioneSelezionata = dati[101 + i]
                                dati[101 + i] = dati[101 + i - 1]
                                dati[101 + i - 1] = condizioneSelezionata
                                azioneSelezionata = dati[111 + i]
                                dati[111 + i] = dati[111 + i - 1]
                                dati[111 + i - 1] = azioneSelezionata
                                break
                            i += 1
                        voceMarcata -= 1
                        yp = yp - GlobalVarG2.gsy // 18 * 1
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 1:
                            voceMarcata += 4
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 14.8
                        else:
                            voceMarcata -= 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp - GlobalVarG2.gsy // 18 * 2
                    else:
                        if voceMarcata == 6 or voceMarcata == 16 or voceMarcata == 26:
                            voceMarcata += 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 15
                        else:
                            voceMarcata -= 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp - GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_a and not riordinamento:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if 1 <= voceMarcata <= 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 26
                        yp = GlobalVarG2.gsy // 18 * 7
                    elif voceMarcata == 2:
                        voceMarcata += 27
                        yp = GlobalVarG2.gsy // 18 * 9
                    elif voceMarcata == 3:
                        voceMarcata += 28
                        yp = GlobalVarG2.gsy // 18 * 11
                    elif voceMarcata == 4:
                        voceMarcata += 29
                        yp = GlobalVarG2.gsy // 18 * 13
                    elif voceMarcata == 5:
                        voceMarcata += 30
                        yp = GlobalVarG2.gsy // 18 * 15
                    xp = GlobalVarG2.gsx // 32 * 16.5
                elif 6 <= voceMarcata <= 15:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if 6 <= voceMarcata <= 7:
                        if voceMarcata == 6:
                            voceMarcata -= 5
                        elif voceMarcata == 7:
                            voceMarcata -= 6
                        yp = GlobalVarG2.gsy // 18 * 6.8
                    elif 8 <= voceMarcata <= 9:
                        if voceMarcata == 8:
                            voceMarcata -= 6
                        elif voceMarcata == 9:
                            voceMarcata -= 7
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    elif 10 <= voceMarcata <= 11:
                        if voceMarcata == 10:
                            voceMarcata -= 7
                        elif voceMarcata == 11:
                            voceMarcata -= 8
                        yp = GlobalVarG2.gsy // 18 * 10.8
                    elif 12 <= voceMarcata <= 13:
                        if voceMarcata == 12:
                            voceMarcata -= 8
                        elif voceMarcata == 13:
                            voceMarcata -= 9
                        yp = GlobalVarG2.gsy // 18 * 12.8
                    elif 14 <= voceMarcata <= 15:
                        if voceMarcata == 14:
                            voceMarcata -= 9
                        elif voceMarcata == 15:
                            voceMarcata -= 10
                        yp = GlobalVarG2.gsy // 18 * 14.8
                    xp = GlobalVarG2.gsx // 32 * 1
                elif 16 <= voceMarcata <= 25:
                    voceMarcata -= 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 7
                elif 26 <= voceMarcata <= 35:
                    voceMarcata -= 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 10
            if tastop == pygame.K_s:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if riordinamento:
                    if voceMarcata != 15:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                        i = 0
                        while i < 10:
                            if voceMarcata == i + 6:
                                condizioneSelezionata = dati[101 + i]
                                dati[101 + i] = dati[101 + i + 1]
                                dati[101 + i + 1] = condizioneSelezionata
                                azioneSelezionata = dati[111 + i]
                                dati[111 + i] = dati[111 + i + 1]
                                dati[111 + i + 1] = azioneSelezionata
                                break
                            i += 1
                        voceMarcata += 1
                        yp = yp + GlobalVarG2.gsy // 18 * 1
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 5:
                            voceMarcata -= 4
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6.8
                        else:
                            voceMarcata += 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp + GlobalVarG2.gsy // 18 * 2
                    else:
                        if voceMarcata == 15 or voceMarcata == 25 or voceMarcata == 35:
                            voceMarcata -= 9
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = GlobalVarG2.gsy // 18 * 6
                        else:
                            voceMarcata += 1
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                            yp = yp + GlobalVarG2.gsy // 18 * 1
            if tastop == pygame.K_d and not riordinamento:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if 1 <= voceMarcata <= 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 6
                        yp = GlobalVarG2.gsy // 18 * 7
                    elif voceMarcata == 2:
                        voceMarcata += 7
                        yp = GlobalVarG2.gsy // 18 * 9
                    elif voceMarcata == 3:
                        voceMarcata += 8
                        yp = GlobalVarG2.gsy // 18 * 11
                    elif voceMarcata == 4:
                        voceMarcata += 9
                        yp = GlobalVarG2.gsy // 18 * 13
                    elif voceMarcata == 5:
                        voceMarcata += 10
                        yp = GlobalVarG2.gsy // 18 * 15
                    xp = GlobalVarG2.gsx // 32 * 7
                elif 6 <= voceMarcata <= 15:
                    voceMarcata += 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 10
                elif 16 <= voceMarcata <= 25:
                    voceMarcata += 10
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = GlobalVarG2.gsx // 32 * 16.5
                elif 26 <= voceMarcata <= 35:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    if 26 <= voceMarcata <= 27:
                        if voceMarcata == 26:
                            voceMarcata -= 25
                        elif voceMarcata == 27:
                            voceMarcata -= 26
                        yp = GlobalVarG2.gsy // 18 * 6.8
                    elif 28 <= voceMarcata <= 29:
                        if voceMarcata == 28:
                            voceMarcata -= 26
                        elif voceMarcata == 29:
                            voceMarcata -= 27
                        yp = GlobalVarG2.gsy // 18 * 8.8
                    elif 30 <= voceMarcata <= 31:
                        if voceMarcata == 30:
                            voceMarcata -= 27
                        elif voceMarcata == 31:
                            voceMarcata -= 28
                        yp = GlobalVarG2.gsy // 18 * 10.8
                    elif 32 <= voceMarcata <= 33:
                        if voceMarcata == 32:
                            voceMarcata -= 28
                        elif voceMarcata == 33:
                            voceMarcata -= 29
                        yp = GlobalVarG2.gsy // 18 * 12.8
                    elif 34 <= voceMarcata <= 35:
                        if voceMarcata == 34:
                            voceMarcata -= 29
                        elif voceMarcata == 35:
                            voceMarcata -= 30
                        yp = GlobalVarG2.gsy // 18 * 14.8
                    xp = GlobalVarG2.gsx // 32 * 1
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 5, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 22, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 7, GlobalVarG2.gsy // 18 * 15.5))

            if annullaRiordinamento:
                dati = list(datiPrimaDiRiordinamento)
                annullaRiordinamento = False
                xp = vxpGambit
                yp = vypGambit
                voceMarcata = voceGambitMarcata

            if riordinamento:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (xp, yp - (GlobalVarG2.gpy // 4), GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 1))
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (vxpGambit, vypGambit - (GlobalVarG2.gpy // 4), GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 1))

            messaggio("Setta Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)

            # equip batteria
            messaggio("Batterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 4.5, 60)
            i = 0
            while i < 5:
                GlobalVarG2.schermo.blit(sfondoOggetto, (GlobalVarG2.gsx // 32 * 2.5, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                GlobalVarG2.schermo.blit(vetIcoBatterie[i], (GlobalVarG2.gsx // 32 * 2.5, (GlobalVarG2.gsy // 18 * 6 + (GlobalVarG2.gpy * 2 * i))))
                i += 1

            # programmazione Colco
            messaggio("Ordine", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 7.5, GlobalVarG2.gsy // 18 * 4.5, 60)
            i = 1
            while i <= 10:
                if i == 10:
                    messaggio(str(i), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.3, GlobalVarG2.gsy // 18 * (i + 5), 50)
                else:
                    messaggio(str(i), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 8.5, GlobalVarG2.gsy // 18 * (i + 5), 50)
                i += 1
            messaggio("Condizione...", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 4.5, 60)
            c = 6.1
            for i in range(101, 111):
                if dati[i] == -1:
                    messaggio("---", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 0:
                    messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 1:
                    messaggio("Rallo con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 2:
                    messaggio("Rallo con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 3:
                    messaggio("Rallo con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 4:
                    messaggio("Rallo con veleno", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 5:
                    messaggio("Colco surriscaldato", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 6:
                    messaggio("Colco con pe < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 7:
                    messaggio("Colco con pe < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 8:
                    messaggio("Colco con pe < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 9:
                    messaggio("Sempre a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 10:
                    messaggio("Sempre a Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 11:
                    messaggio("Nemico a caso", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 12:
                    messaggio("Nemico vicino", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 13:
                    messaggio("Nemico lontano", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 14:
                    messaggio("Nemico con pv < 80%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 15:
                    messaggio("Nemico con pv < 50%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 16:
                    messaggio("Nemico con pv < 30%", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 17:
                    messaggio("Nemico con meno pv", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 18:
                    messaggio("Numero di nemici > 1", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 19:
                    messaggio("Numero di nemici > 4", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 20:
                    messaggio("Numero di nemici > 7", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * c, 40)
                c += 1
            messaggio("...Tecnica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * 4.5, 60)
            c = 6.1
            for i in range(111, 121):
                if dati[i] == -1:
                    messaggio("---", GlobalVarG2.grigioscu, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 0:
                    messaggio("---", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 1:
                    messaggio("Scossa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 2:
                    messaggio("Cura", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 3:
                    messaggio("Antidoto", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 4:
                    messaggio("Freccia elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 5:
                    messaggio("Tempesta elettrica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 6:
                    messaggio("Raffreddamento", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 7:
                    messaggio("Auto-ricarica", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 8:
                    messaggio("Cura +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 9:
                    messaggio("Scossa +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 10:
                    messaggio("Freccia elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 11:
                    messaggio("Velocizza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 12:
                    messaggio("Carica attacco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 13:
                    messaggio("Carica difesa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 14:
                    messaggio("Efficienza", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 15:
                    messaggio("Tempesta elettrica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 16:
                    messaggio("Cura ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 17:
                    messaggio("Auto-ricarica +", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 18:
                    messaggio("Scossa ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 19:
                    messaggio("Freccia Elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                if dati[i] == 20:
                    messaggio("Tempesta elettrica ++", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 17.5, GlobalVarG2.gsy // 18 * c, 40)
                c = c + 1

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            GlobalVarG2.schermo.blit(robosta, (GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 10))
            GlobalVarG2.schermo.blit(vetImgBatterie[dati[9]], (GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 10))
            messaggio("Statistiche:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 7.7, 50)
            messaggio("Pe totali: %i" % entot, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % difro, GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 9, 35)

            # mostrare descrizione batterie / priorità / condizioni / azioni
            if voceMarcata == 1:
                if dati[71] != 0:
                    messaggio("Batteria piccola:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Batteria che contiene poca alimentazione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 0 - (dati[9] * dati[9] * 30)
                    if dati[9] > 0:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 2:
                if dati[72] != 0:
                    messaggio("Batteria discreta:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Batteria con una buona capienza e", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("ottimizzazione del sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 30 - (dati[9] * dati[9] * 30)
                    if dati[9] > 1:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 3:
                if dati[73] != 0:
                    messaggio("Batteria capiente:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio(u"Batteria con una grande capacità e un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("ottimo sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 120 - (dati[9] * dati[9] * 30)
                    if dati[9] > 2:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 4:
                if dati[74] != 0:
                    messaggio("Batteria enorme:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Grande batteria che permette a Colco di", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio(u"utilizzare le tecniche più dispendiose", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 270 - (dati[9] * dati[9] * 30)
                    if dati[9] > 3:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
            if voceMarcata == 5:
                if dati[75] != 0:
                    messaggio("Batteria illimitata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                    messaggio("Batteria incredibilmente capiente.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                    messaggio("Permette un eccellente ottimizzazione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                    messaggio("del sistema difensivo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)
                    diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                    if dati[9] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 8.5, 35)
                    diff = 480 - (dati[9] * dati[9] * 30)
                    if dati[9] > 4:
                        messaggio(str(diff), GlobalVarG2.rosso, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), GlobalVarG2.verde, GlobalVarG2.gsx // 32 * 28, GlobalVarG2.gsy // 18 * 9, 35)

            if 6 <= voceMarcata <= 15:
                messaggio(u"Ordine:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio(u"Determina il livello di priorità dell'evento.", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio(u"Colco eseguirà la prima tecnica della lista", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio(u"la cui condizione si è verificata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

            if 16 <= voceMarcata <= 25:
                messaggio("Condizione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio("Indica la situazione che si deve verificare", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio(u"affinchè Colco esegua la tecnica associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

            if 26 <= voceMarcata <= 35:
                messaggio("Tecnica:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 4.8, 60)
                messaggio(u"La tecnica che Colco eseguirà quando si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 5.8, 35)
                messaggio("verifica la condizione associata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.3, 35)
                messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 24, GlobalVarG2.gsy // 18 * 6.8, 35)

            # puntatore vecchio batterie/riordinamento gambit
            if dati[9] == 0:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 6.8))
            if dati[9] == 1:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 8.8))
            if dati[9] == 2:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 10.8))
            if dati[9] == 3:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 12.8))
            if dati[9] == 4:
                GlobalVarG2.schermo.blit(puntatorevecchio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 14.8))
            if riordinamento:
                GlobalVarG2.schermo.blit(puntatorevecchio, (vxpGambit, vypGambit))

            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if voceMarcata >= 6 and not riordinamento:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, (GlobalVarG2.gsx // 32 * 7.5, yp + (int(GlobalVarG2.gpy * 0.7))), (GlobalVarG2.gsx // 32 * 22.5, yp + (int(GlobalVarG2.gpy * 0.7))), 2)

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati


def oggetti(dati, canzone):
    puntatore = pygame.transform.scale(GlobalVarG2.puntatoreorigi, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    puntatorevecchio = pygame.transform.scale(GlobalVarG2.puntatoreorigivecchio, (GlobalVarG2.gpx // 2, GlobalVarG2.gpy // 2))
    sfondostastart = pygame.transform.scale(GlobalVarG2.sfondostax3, (GlobalVarG2.gpx * 4, GlobalVarG2.gpy))
    sconosciutoOggetto = pygame.transform.scale(GlobalVarG2.sconosciutoOggettoMenu, (GlobalVarG2.gpx * 10, GlobalVarG2.gpy * 10))
    xp = GlobalVarG2.gsx // 32 * 1
    yp = GlobalVarG2.gsy // 18 * 5
    xpv = xp
    ypv = yp
    usauno = False
    usa = 0
    risposta = False
    attacco = 0
    oggetton = 1
    voceMarcata = 0
    primoFrame = True
    aggiornaInterfacciaPerMouse = False
    sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

    tastop = 0
    tastotempfps = 5

    imgOggetti = []
    i = 1
    while i <= 10:
        if dati[i + 30] >= 0:
            imgOggetti.append(GlobalVarG2.vetImgOggettiMenu[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

    while not risposta:
        if not GlobalVarG2.canaleSoundCanzone.get_busy():
            GlobalVarG2.canaleSoundCanzone.play(canzone)

        # rallenta per i 30 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
        else:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        oggettonVecchio = oggetton
        xMouse, yMouse = pygame.mouse.get_pos()
        deltaXMouse, deltaYMouse = pygame.mouse.get_rel()
        if (deltaXMouse != 0 or deltaYMouse != 0) and not GlobalVarG2.mouseVisibile:
            aggiornaInterfacciaPerMouse = True
            pygame.mouse.set_visible(True)
            GlobalVarG2.mouseVisibile = True
        if GlobalVarG2.mouseVisibile:
            if usa != 0:
                if GlobalVarG2.gsy // 18 * 14.5 <= yMouse <= GlobalVarG2.gsy // 18 * 16.5:
                    if GlobalVarG2.gsx // 32 * 11 <= xMouse <= GlobalVarG2.gsx // 32 * 15:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVarG2.gsx // 32 * 12
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    elif GlobalVarG2.gsx // 32 * 15 <= xMouse <= GlobalVarG2.gsx // 32 * 19:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVarG2.gsx // 32 * 15
                        yp = GlobalVarG2.gsy // 18 * 15.1
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            else:
                if GlobalVarG2.gsx // 32 * 1 <= xMouse <= GlobalVarG2.gsx // 32 * 11:
                    if GlobalVarG2.gsy // 18 * 4.7 <= yMouse <= GlobalVarG2.gsy // 18 * 5.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 1
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 5
                    elif GlobalVarG2.gsy // 18 * 5.7 <= yMouse <= GlobalVarG2.gsy // 18 * 6.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 2
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 6
                    elif GlobalVarG2.gsy // 18 * 6.7 <= yMouse <= GlobalVarG2.gsy // 18 * 7.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 3
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 7
                    elif GlobalVarG2.gsy // 18 * 7.7 <= yMouse <= GlobalVarG2.gsy // 18 * 8.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 4
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 8
                    elif GlobalVarG2.gsy // 18 * 8.7 <= yMouse <= GlobalVarG2.gsy // 18 * 9.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 5
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 9
                    elif GlobalVarG2.gsy // 18 * 10.7 <= yMouse <= GlobalVarG2.gsy // 18 * 11.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 6
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 11
                    elif GlobalVarG2.gsy // 18 * 11.7 <= yMouse <= GlobalVarG2.gsy // 18 * 12.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 7
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 12
                    elif GlobalVarG2.gsy // 18 * 12.7 <= yMouse <= GlobalVarG2.gsy // 18 * 13.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 8
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 13
                    elif GlobalVarG2.gsy // 18 * 13.7 <= yMouse <= GlobalVarG2.gsy // 18 * 14.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 9
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 14
                    elif GlobalVarG2.gsy // 18 * 14.7 <= yMouse <= GlobalVarG2.gsy // 18 * 15.7:
                        if GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(False)
                        oggetton = 10
                        xp = GlobalVarG2.gsx // 32 * 1
                        yp = GlobalVarG2.gsy // 18 * 15
                    else:
                        if not GlobalVarG2.mouseBloccato:
                            GlobalVarG2.configuraCursore(True)
                else:
                    if not GlobalVarG2.mouseBloccato:
                        GlobalVarG2.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton) and not primoFrame:
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
            if event.type == pygame.KEYDOWN and not tastoTrovato and voceMarcataVecchia == voceMarcata and oggettonVecchio == oggetton:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                tastop = event.key
                tastotempfps = 5
                if event.key == pygame.K_q and not tastoTrovato:
                    tastoTrovato = True
                    voceMarcata = 0
                    if usa != 0:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        xp = GlobalVarG2.gsx // 32 * 1
                        if usa == 1:
                            yp = GlobalVarG2.gsy // 18 * 5
                        if usa == 2:
                            yp = GlobalVarG2.gsy // 18 * 6
                        if usa == 3:
                            yp = GlobalVarG2.gsy // 18 * 7
                        if usa == 4:
                            yp = GlobalVarG2.gsy // 18 * 8
                        if usa == 5:
                            yp = GlobalVarG2.gsy // 18 * 9
                        if usa == 6:
                            yp = GlobalVarG2.gsy // 18 * 11
                        if usa == 7:
                            yp = GlobalVarG2.gsy // 18 * 12
                        if usa == 8:
                            yp = GlobalVarG2.gsy // 18 * 13
                        if usa == 9:
                            yp = GlobalVarG2.gsy // 18 * 14
                        if usa == 10:
                            yp = GlobalVarG2.gsy // 18 * 15
                        usa = 0
                    else:
                        GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                        risposta = True
                if event.key == pygame.K_s and voceMarcata == 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_w and voceMarcata == 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_a and voceMarcata != 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
                if event.key == pygame.K_d and voceMarcata != 0 and not tastoTrovato:
                    primoMovimento = True
                    tastoTrovato = True
            if GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and destroMouse:
                tastop = "spazioOmouse"
                tastoTrovato = True
                voceMarcata = 0
                if usa != 0:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    xp = GlobalVarG2.gsx // 32 * 1
                    if usa == 1:
                        yp = GlobalVarG2.gsy // 18 * 5
                    if usa == 2:
                        yp = GlobalVarG2.gsy // 18 * 6
                    if usa == 3:
                        yp = GlobalVarG2.gsy // 18 * 7
                    if usa == 4:
                        yp = GlobalVarG2.gsy // 18 * 8
                    if usa == 5:
                        yp = GlobalVarG2.gsy // 18 * 9
                    if usa == 6:
                        yp = GlobalVarG2.gsy // 18 * 11
                    if usa == 7:
                        yp = GlobalVarG2.gsy // 18 * 12
                    if usa == 8:
                        yp = GlobalVarG2.gsy // 18 * 13
                    if usa == 9:
                        yp = GlobalVarG2.gsy // 18 * 14
                    if usa == 10:
                        yp = GlobalVarG2.gsy // 18 * 15
                    usa = 0
                else:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    risposta = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (GlobalVarG2.mouseVisibile and event.type == pygame.MOUSEBUTTONDOWN and sinistroMouse and not GlobalVarG2.mouseBloccato):
                tastop = "spazioOmouse"
                tastoTrovato = True
                usadue = True

                # usa?
                if voceMarcata == 1:
                    voceMarcata = 0
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                    xp = GlobalVarG2.gsx // 32 * 1
                    # pozione
                    if usa == 1:
                        dati[5] = dati[5] + 100
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[31] = dati[31] - 1
                        yp = GlobalVarG2.gsy // 18 * 5
                    # carica batt
                    if usa == 2:
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[32] = dati[32] - 1
                        yp = GlobalVarG2.gsy // 18 * 6
                    # antidoto
                    if usa == 3:
                        dati[121] = 0
                        dati[33] = dati[33] - 1
                        yp = GlobalVarG2.gsy // 18 * 7
                    # super pozione
                    if usa == 4:
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[34] = dati[34] - 1
                        yp = GlobalVarG2.gsy // 18 * 8
                    # carica migliorato
                    if usa == 5:
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[35] = dati[35] - 1
                        yp = GlobalVarG2.gsy // 18 * 9
                    # bomba
                    if usa == 6:
                        attacco = 2
                        yp = GlobalVarG2.gsy // 18 * 11
                    # bomba veleno
                    if usa == 7:
                        attacco = 3
                        yp = GlobalVarG2.gsy // 18 * 12
                    # esca
                    if usa == 8:
                        attacco = 4
                        yp = GlobalVarG2.gsy // 18 * 13
                    # bomba appiccicosa
                    if usa == 9:
                        attacco = 5
                        yp = GlobalVarG2.gsy // 18 * 14
                    # bomba potenziata
                    if usa == 10:
                        attacco = 6
                        yp = GlobalVarG2.gsy // 18 * 15
                    usa = 0
                    usadue = False
                elif voceMarcata == 2:
                    voceMarcata = 0
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selind)
                    xp = GlobalVarG2.gsx // 32 * 1
                    if usa == 1:
                        yp = GlobalVarG2.gsy // 18 * 5
                    if usa == 2:
                        yp = GlobalVarG2.gsy // 18 * 6
                    if usa == 3:
                        yp = GlobalVarG2.gsy // 18 * 7
                    if usa == 4:
                        yp = GlobalVarG2.gsy // 18 * 8
                    if usa == 5:
                        yp = GlobalVarG2.gsy // 18 * 9
                    if usa == 6:
                        yp = GlobalVarG2.gsy // 18 * 11
                    if usa == 7:
                        yp = GlobalVarG2.gsy // 18 * 12
                    if usa == 8:
                        yp = GlobalVarG2.gsy // 18 * 13
                    if usa == 9:
                        yp = GlobalVarG2.gsy // 18 * 14
                    if usa == 10:
                        yp = GlobalVarG2.gsy // 18 * 15
                    usa = 0
                    usadue = False

                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                if usadue:
                    if oggetton == 1:
                        if dati[31] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 1
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 2:
                        if dati[32] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 2
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 3:
                        if dati[33] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 3
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 4:
                        if dati[34] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 4
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 5:
                        if dati[35] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 5
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 6:
                        if dati[36] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 6
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 7:
                        if dati[37] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 7
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 8:
                        if dati[38] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 8
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 9:
                        if dati[39] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 9
                            usauno = True
                        else:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selimp)
                    if oggetton == 10:
                        if dati[40] > 0:
                            GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.selezione)
                            usa = 10
                            usauno = True
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

        if primoMovimento or tastop == pygame.K_q or tastop == "spazioOmouse" or ((tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d) and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton or aggiornaInterfacciaPerMouse:
            aggiornaInterfacciaPerMouse = False
            primoFrame = False
            if not primoMovimento and (tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d):
                tastotempfps = 2
            if tastop == pygame.K_w and voceMarcata == 0:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if oggetton != 1 and oggetton != 6:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton - 1
                    yp = yp - GlobalVarG2.gsy // 18 * 1
                elif oggetton == 6:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton - 1
                    yp = yp - GlobalVarG2.gsy // 18 * 2
                elif oggetton == 1:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 15
                    oggetton = 10
            if tastop == pygame.K_a and voceMarcata != 0:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp - GlobalVarG2.gsx // 32 * 3
            if tastop == pygame.K_s and voceMarcata == 0:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if oggetton != 10 and oggetton != 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton + 1
                    yp = yp + GlobalVarG2.gsy // 18 * 1
                elif oggetton == 5:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    oggetton = oggetton + 1
                    yp = yp + GlobalVarG2.gsy // 18 * 2
                elif oggetton == 10:
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    yp = GlobalVarG2.gsy // 18 * 5
                    oggetton = 1
            if tastop == pygame.K_d and voceMarcata != 0:
                pygame.mouse.set_visible(False)
                GlobalVarG2.mouseVisibile = False
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVarG2.canaleSoundPuntatore.play(GlobalVarG2.spostapun)
                    xp = xp + GlobalVarG2.gsx // 32 * 3
            GlobalVarG2.schermo.fill(GlobalVarG2.grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigio, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4, GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 12.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 10, GlobalVarG2.gsy // 18 * 15.5))
            GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoSinistra, (GlobalVarG2.gsx // 32 * 1, GlobalVarG2.gsy // 18 * 15.5))

            # menu conferma
            if usa != 0:
                pygame.draw.rect(GlobalVarG2.schermo, GlobalVarG2.grigioscurino, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 12.5, GlobalVarG2.gsx // 32 * 8, GlobalVarG2.gsy // 18 * 4))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoAltoDestra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 12.5))
                GlobalVarG2.schermo.blit(GlobalVarG2.sfondoTriangolinoBassoDestra, (GlobalVarG2.gsx // 32 * 18, GlobalVarG2.gsy // 18 * 15.5))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalVarG2.gsx // 32 * 15
                    yp = GlobalVarG2.gsy // 18 * 15.1
                    voceMarcata = 2
                    usauno = False
                GlobalVarG2.schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13.3, GlobalVarG2.gsy // 18 * 13.2, 80)
                messaggio("Si", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 13, GlobalVarG2.gsy // 18 * 15, 60)
                messaggio("No", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 16, GlobalVarG2.gsy // 18 * 15, 60)

            # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
            messaggio("Oggetti", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 1, 150)
            if dati[31] >= 0:
                messaggio("Pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 45)
                messaggio("x %i" % dati[31], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 5, 45)
                if oggetton == 1:
                    messaggio("Pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 100 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 5, 45)
            if dati[32] >= 0:
                messaggio("Caricabatterie", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 45)
                messaggio("x %i" % dati[32], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 6, 45)
                if oggetton == 2:
                    messaggio("Caricabatterie:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 250 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 6, 45)
            if dati[33] >= 0:
                messaggio("Medicina", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 45)
                messaggio("x %i" % dati[33], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 7, 45)
                if oggetton == 3:
                    messaggio("Medicina:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Cura avvelenamento a Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 7, 45)
            if dati[34] >= 0:
                messaggio("Super pozione", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 45)
                messaggio("x %i" % dati[34], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 8, 45)
                if oggetton == 4:
                    messaggio("Super pozione:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 300 pv di Rallo", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 8, 45)
            if dati[35] >= 0:
                messaggio("Carica plus", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 45)
                messaggio("x %i" % dati[35], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 9, 45)
                if oggetton == 5:
                    messaggio("Carica plus:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Recupera 600 pe di Colco", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 9, 45)
            if dati[36] >= 0:
                messaggio("Bomba", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, 45)
                messaggio("x %i" % dati[36], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 11, 45)
                if oggetton == 6:
                    messaggio("Bomba:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Infligge un po' di danni ai nemici su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 11, 45)
            if dati[37] >= 0:
                messaggio("Bomba velenosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 45)
                messaggio("x %i" % dati[37], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 12, 45)
                if oggetton == 7:
                    messaggio("Bomba velenosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Infligge avvelenamento al nemico su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 12, 45)
            if dati[38] >= 0:
                messaggio("Esca", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 45)
                messaggio("x %i" % dati[38], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 13, 45)
                if oggetton == 8:
                    messaggio("Esca:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Distrae i nemici finché non viene distrutta. È possibile", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("riprenderla passandoci sopra", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 13, 45)
            if dati[39] >= 0:
                messaggio("Bomba appiccicosa", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 45)
                messaggio("x %i" % dati[39], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 14, 45)
                if oggetton == 9:
                    messaggio("Bomba appiccicosa:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio(u"Dimezza la velocità del nemico su cui viene lanciata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 14, 45)
            if dati[40] >= 0:
                messaggio("Bomba potenziata", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 45)
                messaggio("x %i" % dati[40], GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 9.3, GlobalVarG2.gsy // 18 * 15, 45)
                if oggetton == 10:
                    messaggio("Bomba potenziata:", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 13.5, 60)
                    messaggio("Infligge molti danni ai nemici su cui viene lanciata in un", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20,
                              GlobalVarG2.gsy // 18 * 14.5, 35)
                    messaggio("vasto raggio", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15, 35)
                    messaggio("", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 15.5, 35)
            else:
                messaggio("???", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 2, GlobalVarG2.gsy // 18 * 15, 45)

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 4, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 5, 50)
            persmen = pygame.transform.scale(GlobalVarG2.persGrafMenu, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
            GlobalVarG2.schermo.blit(persmen, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 4))
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 14, (GlobalVarG2.gsy // 18 * 6) + (GlobalVarG2.gpy // 8)))
            if dati[121]:
                avvelenato = pygame.transform.scale(GlobalVarG2.avvelenatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(avvelenato, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 6))
            if dati[123] > 0:
                attaccopiu = pygame.transform.scale(GlobalVarG2.attaccopiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(attaccopiu, ((GlobalVarG2.gsx // 32 * 14) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 6))
            if dati[124] > 0:
                difesapiu = pygame.transform.scale(GlobalVarG2.difesapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(difesapiu, ((GlobalVarG2.gsx // 32 * 14) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 6))
            # vita-status robo
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 9, 50)
            messaggio("Status alterativi: ", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 10, 50)
            robomen = pygame.transform.scale(GlobalVarG2.robograf, (GlobalVarG2.gpx * 3, GlobalVarG2.gpy * 3))
            GlobalVarG2.schermo.blit(robomen, (GlobalVarG2.gsx // 32 * 11, GlobalVarG2.gsy // 18 * 8))
            GlobalVarG2.schermo.blit(sfondostastart, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 11))
            if dati[122] > 0:
                surriscaldato = pygame.transform.scale(GlobalVarG2.surriscaldatoo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(surriscaldato, (GlobalVarG2.gsx // 32 * 14, GlobalVarG2.gsy // 18 * 11))
            if dati[125] > 0:
                velocitapiu = pygame.transform.scale(GlobalVarG2.velocitapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(velocitapiu, ((GlobalVarG2.gsx // 32 * 14) + (2 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 11))
            if dati[126] > 0:
                efficienzapiu = pygame.transform.scale(GlobalVarG2.efficienzapiuo, (GlobalVarG2.gpx, GlobalVarG2.gpy))
                GlobalVarG2.schermo.blit(efficienzapiu, ((GlobalVarG2.gsx // 32 * 14) + (4 * GlobalVarG2.gpx // 4 * 3), GlobalVarG2.gsy // 18 * 11))

            if attacco != 0:
                risposta = True

            if GlobalVarG2.mouseVisibile:
                messaggio("Tasto destro: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 22.5, GlobalVarG2.gsy // 18 * 1, 50)
            else:
                messaggio("Q: torna indietro", GlobalVarG2.grigiochi, GlobalVarG2.gsx // 32 * 25, GlobalVarG2.gsy // 18 * 1, 50)
            GlobalVarG2.schermo.blit(imgOggetti[oggetton - 1], (GlobalVarG2.gsx // 32 * 20, GlobalVarG2.gsy // 18 * 3))
            GlobalVarG2.schermo.blit(puntatore, (xp, yp))
            if usa == 0:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xp + (int(GlobalVarG2.gpx // 1.5))), yp + (int(GlobalVarG2.gpy * 0.7))), (xp + (int(GlobalVarG2.gpx * 9.5)), yp + (int(GlobalVarG2.gpy * 0.7))), 2)
            else:
                pygame.draw.line(GlobalVarG2.schermo, GlobalVarG2.grigioscu, ((xpv + (int(GlobalVarG2.gpx // 1.5))), ypv + (int(GlobalVarG2.gpy * 0.7))), (xpv + (int(GlobalVarG2.gpx * 9.5)), ypv + (int(GlobalVarG2.gpy * 0.7))), 2)

            pygame.display.update()

        GlobalVarG2.clockMenu.tick(GlobalVarG2.fpsMenu)
    return dati, attacco
