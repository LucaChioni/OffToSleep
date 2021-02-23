# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc


def equip(dati):
    perssta = GlobalImgVar.perso
    persstab = GlobalImgVar.persob
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sfondoOggetto = GlobalImgVar.sfondoOggettoMenu
    sconosciutoEquip = GlobalImgVar.sconosciutoEquipMenu
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 6.8
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    spada = GlobalImgVar.vetImgSpadePixellate[dati[6]]
    arco = GlobalImgVar.vetImgArchiPixellate[dati[128]]
    scudo = GlobalImgVar.vetImgScudiPixellate[dati[7]]
    armatura = GlobalImgVar.vetImgArmaturePixellate[dati[8]]
    guanti = GlobalImgVar.vetImgGuantiPixellate[dati[129]]
    collana = GlobalImgVar.vetImgCollanePixellate[dati[130]]
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
            vetImgSpade.append(GlobalImgVar.vetImgSpadeMenu[i])
        else:
            vetImgSpade.append(sconosciutoEquip)
        if dati[46 + i] > 0:
            vetImgArchi.append(GlobalImgVar.vetImgArchiMenu[i])
        else:
            vetImgArchi.append(sconosciutoEquip)
        if dati[51 + i] > 0:
            vetImgArmature.append(GlobalImgVar.vetImgArmatureMenu[i])
        else:
            vetImgArmature.append(sconosciutoEquip)
        if dati[56 + i] > 0:
            vetImgScudi.append(GlobalImgVar.vetImgScudiMenu[i])
        else:
            vetImgScudi.append(sconosciutoEquip)
        if dati[61 + i] > 0:
            vetImgGuanti.append(GlobalImgVar.vetImgGuantiMenu[i])
        else:
            vetImgGuanti.append(sconosciutoEquip)
        if dati[66 + i] > 0:
            vetImgCollane.append(GlobalImgVar.vetImgCollaneMenu[i])
        else:
            vetImgCollane.append(sconosciutoEquip)
        i += 1

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 4.5:
                if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 4.5 <= xMouse <= GlobalHWVar.gsx // 32 * 8:
                if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 4.5
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 4.5
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 4.5
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 4.5
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 4.5
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 8 <= xMouse <= GlobalHWVar.gsx // 32 * 11.5:
                if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 11.5 <= xMouse <= GlobalHWVar.gsx // 32 * 15:
                if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalHWVar.gsx // 32 * 11.5
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalHWVar.gsx // 32 * 11.5
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalHWVar.gsx // 32 * 11.5
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalHWVar.gsx // 32 * 11.5
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalHWVar.gsx // 32 * 11.5
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 15 <= xMouse <= GlobalHWVar.gsx // 32 * 18.5:
                if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 21
                    xp = GlobalHWVar.gsx // 32 * 15
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 22
                    xp = GlobalHWVar.gsx // 32 * 15
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 23
                    xp = GlobalHWVar.gsx // 32 * 15
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 24
                    xp = GlobalHWVar.gsx // 32 * 15
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 25
                    xp = GlobalHWVar.gsx // 32 * 15
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 18.5 <= xMouse <= GlobalHWVar.gsx // 32 * 22:
                if GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 26
                    xp = GlobalHWVar.gsx // 32 * 18.5
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 27
                    xp = GlobalHWVar.gsx // 32 * 18.5
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 28
                    xp = GlobalHWVar.gsx // 32 * 18.5
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 29
                    xp = GlobalHWVar.gsx // 32 * 18.5
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 30
                    xp = GlobalHWVar.gsx // 32 * 18.5
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            else:
                carim = True
                # progresso-stanza-x-y-liv-pv-spada-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                # spade
                if voceMarcata == 1:
                    if dati[41] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[6] = 0
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 2:
                    if dati[42] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[6] = 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 3:
                    if dati[43] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[6] = 2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 4:
                    if dati[44] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[6] = 3
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 5:
                    if dati[45] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[6] = 4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # archi
                if voceMarcata == 6:
                    if dati[46] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[128] = 0
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 7:
                    if dati[47] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[128] = 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 8:
                    if dati[48] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[128] = 2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 9:
                    if dati[49] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[128] = 3
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 10:
                    if dati[50] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[128] = 4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # armature
                if voceMarcata == 11:
                    if dati[51] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[8] = 0
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 12:
                    if dati[52] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[8] = 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 13:
                    if dati[53] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[8] = 2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 14:
                    if dati[54] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[8] = 3
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 15:
                    if dati[55] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[8] = 4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # scudi
                if voceMarcata == 16:
                    if dati[56] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[7] = 0
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 17:
                    if dati[57] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[7] = 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 18:
                    if dati[58] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[7] = 2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 19:
                    if dati[59] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[7] = 3
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 20:
                    if dati[60] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[7] = 4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # guanti
                if voceMarcata == 21:
                    if dati[61] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[129] = 0
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 22:
                    if dati[62] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[129] = 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 23:
                    if dati[63] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[129] = 2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 24:
                    if dati[64] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[129] = 3
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 25:
                    if dati[65] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[129] = 4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # collane
                if voceMarcata == 26:
                    if dati[66] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[130] = 0
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 27:
                    if dati[67] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[130] = 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 28:
                    if dati[68] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[130] = 2
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 29:
                    if dati[69] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[130] = 3
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                if voceMarcata == 30:
                    if dati[70] != 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        dati[130] = 4
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 5 or voceMarcata == 10 or voceMarcata == 15 or voceMarcata == 20 or voceMarcata == 25 or voceMarcata == 30:
                    voceMarcata -= 4
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 6.8
                else:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp += GlobalHWVar.gsy // 18 * 2
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 6 or voceMarcata == 11 or voceMarcata == 16 or voceMarcata == 21 or voceMarcata == 26:
                    voceMarcata += 4
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 14.8
                else:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp - GlobalHWVar.gsy // 18 * 2
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 26 or voceMarcata == 27 or voceMarcata == 28 or voceMarcata == 29 or voceMarcata == 30:
                    voceMarcata -= 25
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 1
                else:
                    voceMarcata += 5
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp + GlobalHWVar.gsx // 32 * 3.5
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata += 25
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 18.5
                else:
                    voceMarcata -= 5
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = xp - GlobalHWVar.gsx // 32 * 3.5
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))

                GenericFunc.messaggio("Equipaggiamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Armi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 4.5, 65, centrale=True)
                GenericFunc.messaggio("Protezioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 4.5, 65, centrale=True)
                GenericFunc.messaggio("Accessori", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 4.5, 65, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 1.5), int(GlobalHWVar.gpy * 5.6)), (int(GlobalHWVar.gpx * 21.5), int(GlobalHWVar.gpy * 5.6)), 1)
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 1.7, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImgSpade[i], (GlobalHWVar.gsx // 32 * 1.7, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 5.2, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImgArchi[i], (GlobalHWVar.gsx // 32 * 5.2, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 8.7, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImgArmature[i], (GlobalHWVar.gsx // 32 * 8.7, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 12.2, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImgScudi[i], (GlobalHWVar.gsx // 32 * 12.2, int((GlobalHWVar.gsy // 18 * 6) + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 15.7, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImgGuanti[i], (GlobalHWVar.gsx // 32 * 15.7, int((GlobalHWVar.gsy // 18 * 6) + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 19.2, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetImgCollane[i], (GlobalHWVar.gsx // 32 * 19.2, ((GlobalHWVar.gsy // 18 * 6) + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if carim:
                spada = GlobalImgVar.vetImgSpadePixellate[dati[6]]
                arco = GlobalImgVar.vetImgArchiPixellate[dati[128]]
                scudo = GlobalImgVar.vetImgScudiPixellate[dati[7]]
                armatura = GlobalImgVar.vetImgArmaturePixellate[dati[8]]
                guanti = GlobalImgVar.vetImgGuantiPixellate[dati[129]]
                collana = GlobalImgVar.vetImgCollanePixellate[dati[130]]
                carim = False

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 4.5) - 1, (GlobalHWVar.gsy // 18 * 6.1) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 4.5) - 1, (GlobalHWVar.gsy // 18 * 15) + (GlobalHWVar.gpy // 2)), 1)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 8) - 1, (GlobalHWVar.gsy // 18 * 3.8) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 8) - 1, (GlobalHWVar.gsy // 18 * 4.9) + (GlobalHWVar.gpy // 2)), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 8) - 1, (GlobalHWVar.gsy // 18 * 5.3) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 8) - 1, (GlobalHWVar.gsy // 18 * 15.5) + (GlobalHWVar.gpy // 2)), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 11.5) - 1, (GlobalHWVar.gsy // 18 * 6.1) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 11.5) - 1, (GlobalHWVar.gsy // 18 * 15) + (GlobalHWVar.gpy // 2)), 1)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 15) - 1, (GlobalHWVar.gsy // 18 * 3.8) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 15) - 1, (GlobalHWVar.gsy // 18 * 4.9) + (GlobalHWVar.gpy // 2)), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 15) - 1, (GlobalHWVar.gsy // 18 * 5.3) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 15) - 1, (GlobalHWVar.gsy // 18 * 15.5) + (GlobalHWVar.gpy // 2)), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gsx // 32 * 18.5) - 1, (GlobalHWVar.gsy // 18 * 6.1) + (GlobalHWVar.gpy // 2)), ((GlobalHWVar.gsx // 32 * 18.5) - 1, (GlobalHWVar.gsy // 18 * 15) + (GlobalHWVar.gpy // 2)), 1)

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati, inMenu=True)
            if dati[5] > pvtot:
                dati[5] = pvtot

            grandezzaCarattereStatistiche = 40
            posizioneStatisticheX = int(GlobalHWVar.gsx // 32 * 28)
            posizioneStatPvY = int(GlobalHWVar.gsy // 18 * 8.3)
            posizioneStatAttRavY = int(GlobalHWVar.gsy // 18 * 8.9)
            posizioneStatAttDistY = int(GlobalHWVar.gsy // 18 * 9.5)
            posizioneStatDifY = int(GlobalHWVar.gsy // 18 * 10.1)
            posizioneStatParY = int(GlobalHWVar.gsy // 18 * 10.7)
            GlobalHWVar.disegnaImmagineSuSchermo(arco, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(perssta, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(persstab, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(armatura, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(collana, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(spada, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(guanti, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaImmagineSuSchermo(scudo, (GlobalHWVar.gsx // 32 * 24.5, GlobalHWVar.gsy // 18 * 11.5))
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 24.5), int(GlobalHWVar.gpy * 16.5)), (int(GlobalHWVar.gpx * 29.5), int(GlobalHWVar.gpy * 16.5)), 2)
            GenericFunc.messaggio("Statistiche:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 7.3, 60)
            GenericFunc.messaggio("Punti vita: %i" % pvtot, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatPvY, grandezzaCarattereStatistiche)
            GenericFunc.messaggio("Attacco ravvicinato: %i" % attVicino, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatAttRavY, grandezzaCarattereStatistiche)
            GenericFunc.messaggio("Attacco a distanza: %i" % attLontano, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatAttDistY, grandezzaCarattereStatistiche)
            GenericFunc.messaggio("Difesa: %i" % dif, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatDifY, grandezzaCarattereStatistiche)
            GenericFunc.messaggio(u"Probabilità parata: %i" % par + "%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatParY, grandezzaCarattereStatistiche)
            # confronto statistiche
            grandezzaCarattereDescrizioni = 40
            posizioneTitoliY = int(GlobalHWVar.gsy // 18 * 4)
            posizioneDescrizioniX = int(GlobalHWVar.gsx // 32 * 22.5)
            posizioneDescrizioniY = int(GlobalHWVar.gsy // 18 * 5)
            larghezzaTestoDescrizioni = int(GlobalHWVar.gpx * 9)
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            # spade
            if voceMarcata == 1:
                if dati[41] != 0:
                    GenericFunc.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Rimuovi spada.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 0 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 0:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 2:
                if dati[42] != 0:
                    GenericFunc.messaggio("Spada di ferro:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Semplice spada di ferro.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 10 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 1:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif dati[6] < 1:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 3:
                if dati[43] != 0:
                    GenericFunc.messaggio("Spadone d'acciaio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Grande spadone in acciaio con ornamenti in oro. Rappresenta il modello di spada migliore mai prodotto dall'uomo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 40 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 2:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif dati[6] < 2:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 4:
                if dati[44] != 0:
                    GenericFunc.messaggio("Lykother:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Spada molto leggera e affilata. Si dice essere stata ricavata da un dente di un enorme lupo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 90 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 3:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif dati[6] < 3:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 5:
                if dati[45] != 0:
                    GenericFunc.messaggio("Mendaxritas:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Potentissima spada composta da materiali ignoti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 160 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 4:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif dati[6] < 4:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # archi
            if voceMarcata == 6:
                if dati[46] != 0:
                    GenericFunc.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Rimuovi arco.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 0 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 0:
                        GenericFunc.messaggio(str(diffAtt), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 7:
                if dati[47] != 0:
                    GenericFunc.messaggio("Arco di legno:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Semplice arco in legno usato dalla maggior parte dei forestieri.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 10 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 1:
                        GenericFunc.messaggio(str(diffAtt), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[128] < 1:
                        GenericFunc.messaggio("+" + str(diffAtt), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 8:
                if dati[48] != 0:
                    GenericFunc.messaggio("Arco di ferro:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Elaborato arco in ferro usato solo dai più esperti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 40 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 2:
                        GenericFunc.messaggio(str(diffAtt), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[128] < 2:
                        GenericFunc.messaggio("+" + str(diffAtt), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 9:
                if dati[49] != 0:
                    GenericFunc.messaggio("Arco di precisione:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Sofisticato arco in legno e acciaio. Molto leggero e potente. Massima espressione dell'ingegno umano.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 90 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 3:
                        GenericFunc.messaggio(str(diffAtt), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[128] < 3:
                        GenericFunc.messaggio("+" + str(diffAtt), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 10:
                if dati[50] != 0:
                    GenericFunc.messaggio("Accipiter:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Potentissimo arco di origine sconosciuta.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 160 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 4:
                        GenericFunc.messaggio(str(diffAtt), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[128] < 4:
                        GenericFunc.messaggio("+" + str(diffAtt), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # armature
            if voceMarcata == 11:
                if dati[51] != 0:
                    GenericFunc.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Rimuovi armatura.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 0 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 0:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 12:
                if dati[52] != 0:
                    GenericFunc.messaggio("Armatura di pelle:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Semplice armatura in pelle.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 10 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 1:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[8] < 1:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 13:
                if dati[53] != 0:
                    GenericFunc.messaggio("Armatura d'acciaio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Grande armatura d'acciaio con ornamenti in oro. Usata solo dagli ufficiali dell'esercito.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 40 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 2:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[8] < 2:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 14:
                if dati[54] != 0:
                    GenericFunc.messaggio("Lykodes:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Armatura formata da materiali leggieri e resistenti. Si dice essere stata ricavata dalle ossa di un enorme lupo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 90 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 3:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[8] < 3:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 15:
                if dati[55] != 0:
                    GenericFunc.messaggio("Loriquam:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Armatura incredibilmente resistente. La sua origine è ignota.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 160 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 4:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[8] < 4:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # scudi
            if voceMarcata == 16:
                if dati[56] != 0:
                    GenericFunc.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Rimuovi scudo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 0 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 0:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = 0 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 0:
                        GenericFunc.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 17:
                if dati[57] != 0:
                    GenericFunc.messaggio("Scudo di pelle:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Semplice scudo in pelle.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 5 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 1:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[7] < 1:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = 3 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 1:
                        GenericFunc.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif dati[7] < 1:
                        GenericFunc.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 18:
                if dati[58] != 0:
                    GenericFunc.messaggio("Scudo d'acciaio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Sofisticato scudo in acciaio e oro. Studiato per respingere gli attacchi più pesanti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 20 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 2:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[7] < 2:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = 12 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 2:
                        GenericFunc.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif dati[7] < 2:
                        GenericFunc.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 19:
                if dati[59] != 0:
                    GenericFunc.messaggio("Lykethmos:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Scudo molto leggero e resistente. Si dice essere stato ricavato dalle ossa più resistenti di un enorme lupo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 45 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 3:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[7] < 3:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = 27 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 3:
                        GenericFunc.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif dati[7] < 3:
                        GenericFunc.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 20:
                if dati[60] != 0:
                    GenericFunc.messaggio("Clipequam:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Scudo incredibilmente resistente. Non è nota l'origine.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 80 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 4:
                        GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[7] < 4:
                        GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = 48 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 4:
                        GenericFunc.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif dati[7] < 4:
                        GenericFunc.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # guanti
            if voceMarcata == 21:
                if dati[61] != 0:
                    GenericFunc.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Rimuovi guanti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] == 1:
                        GenericFunc.messaggio("-50", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 2:
                        GenericFunc.messaggio("-30", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        GenericFunc.messaggio("-10%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 22:
                if dati[62] != 0:
                    GenericFunc.messaggio("Guanti vitali:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Guanti che aumentano i <*>#italic#Pv<*> massimi del portatore.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 1:
                        GenericFunc.messaggio("+50", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    if dati[129] == 2:
                        GenericFunc.messaggio("-30", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        GenericFunc.messaggio("-10%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 23:
                if dati[63] != 0:
                    GenericFunc.messaggio("Guanti difensivi:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Guanti che consentono di subire meno danno grazie ad una presa salda dello scudo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 2:
                        GenericFunc.messaggio("+30", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    if dati[129] == 1:
                        GenericFunc.messaggio("-50", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        GenericFunc.messaggio("-10%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 24:
                if dati[64] != 0:
                    GenericFunc.messaggio("Guanti offensivi:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Guanti che aumentano l'attacco del portatore grazie ad una presa salda dell'arma.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 3:
                        GenericFunc.messaggio("+20", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        GenericFunc.messaggio("+20", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    if dati[129] == 1:
                        GenericFunc.messaggio("-50", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 2:
                        GenericFunc.messaggio("-30", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        GenericFunc.messaggio("-10%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 25:
                if dati[65] != 0:
                    GenericFunc.messaggio("Guanti confortevoli:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Guanti che aumentano la probabilità di parare gli attacchi grazie ad una presa agevole dello scudo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 4:
                        GenericFunc.messaggio("+10%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    if dati[129] == 1:
                        GenericFunc.messaggio("-50", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 2:
                        GenericFunc.messaggio("-30", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        GenericFunc.messaggio("-20", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # collane
            if voceMarcata == 26:
                if dati[66] != 0:
                    GenericFunc.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Rimuovi collana.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 27:
                if dati[67] != 0:
                    GenericFunc.messaggio("Collana rigenerante:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio("Collana composta da erbe il cui odore ripristina <*>#italic#Pv<*> ogni turno.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 28:
                if dati[68] != 0:
                    GenericFunc.messaggio("Collana medicinale:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Collana composta da erbe il cui odore neutralizza la tossicità del veleno (non ha effetto se si è già avvelenati).", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 29:
                if dati[69] != 0:
                    GenericFunc.messaggio("Apprendimaschera:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Collana che consente di ricevere più punti esperienza.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 30:
                if dati[70] != 0:
                    GenericFunc.messaggio("Portafortuna:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Collana che permette di ottenere più monete dai nemici.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)

            # puntatore vecchio
            if dati[6] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6.8))
            if dati[6] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8.8))
            if dati[6] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 10.8))
            if dati[6] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 12.8))
            if dati[6] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14.8))
            if dati[128] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 6.8))
            if dati[128] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 8.8))
            if dati[128] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 10.8))
            if dati[128] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 12.8))
            if dati[128] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 14.8))
            if dati[8] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6.8))
            if dati[8] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8.8))
            if dati[8] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10.8))
            if dati[8] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12.8))
            if dati[8] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14.8))
            if dati[7] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 6.8))
            if dati[7] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 8.8))
            if dati[7] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 10.8))
            if dati[7] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 12.8))
            if dati[7] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.8))
            if dati[129] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6.8))
            if dati[129] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8.8))
            if dati[129] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10.8))
            if dati[129] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.8))
            if dati[129] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14.8))
            if dati[130] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 6.8))
            if dati[130] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 8.8))
            if dati[130] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 10.8))
            if dati[130] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 12.8))
            if dati[130] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 14.8))

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return dati


def sceglicondiz(dati, condizione):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    condSconosciuta = GlobalImgVar.imgGambitSconosciuta
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico le scenette
    scecond = GlobalImgVar.vetImgCondizioniMenu

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 8:
                if GlobalHWVar.gsy // 18 * 4.4 <= yMouse <= GlobalHWVar.gsy // 18 * 5.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 0
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 4.6
                elif GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.1
                elif GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7.1
                elif GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.1
                elif GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9.1
                elif GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.1
                elif GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 11.1
                elif GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.1
                elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.1
                elif GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.1
                elif GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 15.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 15.1
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 8 <= xMouse <= GlobalHWVar.gsx // 32 * 16:
                if GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 6.1
                elif GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 7.1
                elif GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 8.1
                elif GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 9.1
                elif GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 10.1
                elif GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 11.1
                elif GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 12.1
                elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 13.1
                elif GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 14.1
                elif GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 15.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 15.1
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            else:
                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
                i = 81
                c = 1
                while i <= 100:
                    if voceMarcata == c:
                        if dati[i] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            return c
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    i += 1
                    c += 1
                if voceMarcata == 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    return 0
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp - GlobalHWVar.gsy // 18 * 1.5
                        xp = GlobalHWVar.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 15.1
                else:
                    if voceMarcata != 0:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp - GlobalHWVar.gsy // 18 * 1
                    else:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 15.1
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = xp - GlobalHWVar.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp + GlobalHWVar.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 4.6
                            xp = GlobalHWVar.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp + GlobalHWVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = xp + GlobalHWVar.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GenericFunc.messaggio("Scegli condizione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Cancella settaggio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.7, 45)
                if dati[81] > 0:
                    GenericFunc.messaggio("Lucy con Pv < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[82] > 0:
                    GenericFunc.messaggio("Lucy con Pv < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[83] > 0:
                    GenericFunc.messaggio("Lucy con Pv < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[84] > 0:
                    GenericFunc.messaggio("Lucy con veleno", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[85] > 0:
                    GenericFunc.messaggio("Impo surriscaldato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[86] > 0:
                    GenericFunc.messaggio("Impo con Pe < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[87] > 0:
                    GenericFunc.messaggio("Impo con Pe < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[88] > 0:
                    GenericFunc.messaggio("Impo con Pe < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[89] > 0:
                    GenericFunc.messaggio("Sempre a Lucy", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[90] > 0:
                    GenericFunc.messaggio("Sempre a Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                if dati[91] > 0:
                    GenericFunc.messaggio("Nemico a caso", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[92] > 0:
                    GenericFunc.messaggio("Nemico vicino", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[93] > 0:
                    GenericFunc.messaggio("Nemico lontano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[94] > 0:
                    GenericFunc.messaggio("Nemico con Pv < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[95] > 0:
                    GenericFunc.messaggio("Nemico con Pv < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[96] > 0:
                    GenericFunc.messaggio("Nemico con Pv < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[97] > 0:
                    GenericFunc.messaggio("Nemico con meno Pv", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[98] > 0:
                    GenericFunc.messaggio("Numero di nemici > 1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[99] > 0:
                    GenericFunc.messaggio("Numero di nemici > 4", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[100] > 0:
                    GenericFunc.messaggio("Numero di nemici > 7", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 16)), 2)

            grandezzaCarattereDescrizioni = 40
            larghezzaTestoDescrizioni = GlobalHWVar.gpx * 13
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            if voceMarcata == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(scecond[0], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                GenericFunc.messaggio("Cancella settaggio:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Cancella il settaggio di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if voceMarcata == 1:
                if dati[81] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[1], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Lucy con Pv < 80%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su Lucy se la vede e ha <*>#italic#Pv<*> < 80%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 2:
                if dati[82] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[2], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Lucy con Pv < 50%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su Lucy se la vede e ha <*>#italic#Pv<*> < 50%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 3:
                if dati[83] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[3], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Lucy con Pv < 30%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su Lucy se la vede e ha <*>#italic#Pv<*> < 30%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 4:
                if dati[84] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[4], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Lucy con veleno:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su Lucy se la vede ed è avvelenata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 5:
                if dati[85] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[5], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Impo surriscaldato:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su Impo quando è surriscaldato.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 6:
                if dati[86] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[6], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Impo con Pe < 80%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su Impo quando ha <*>#italic#Pe<*> < 80%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 7:
                if dati[87] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[7], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Impo con Pe < 50%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su Impo quando ha <*>#italic#Pe<*> < 50%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 8:
                if dati[88] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[8], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Impo con Pe < 30%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su Impo quando ha <*>#italic#Pe<*> < 30%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 9:
                if dati[89] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[9], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sempre a Lucy:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su Lucy in continuazione quando la vede (se la tecnica associata comporta un'alterazione di stato, viene eseguita solo se lo status non è attivo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 10:
                if dati[90] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[10], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sempre a Impo:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su Impo in continuazione (se la tecnica associata comporta un'alterazione di stato, viene eseguita solo se lo status non è attivo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 11:
                if dati[91] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[11], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico a caso:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Esegue l'azione su un nemico a caso.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 12:
                if dati[92] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[12], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico vicino:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione sul nemico più vicino nel raggio di 2 caselle.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 13:
                if dati[93] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[13], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico lontano:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 14:
                if dati[94] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[14], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico con Pv < 80%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su un nemico con <*>#italic#Pv<*> < 80% (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 15:
                if dati[95] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[15], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico con Pv < 50%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su un nemico con <*>#italic#Pv<*> < 50% (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 16:
                if dati[96] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[16], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico con Pv < 30%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione su un nemico con <*>#italic#Pv<*> < 30% (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 17:
                if dati[97] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[17], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Nemico con meno Pv:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione sul nemico con meno <*>#italic#Pv<*> (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 18:
                if dati[98] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[18], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Numero di nemici > 1:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 19:
                if dati[99] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[19], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Numero di nemici > 4:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 20:
                if dati[100] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[20], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Numero di nemici > 7:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if condizione == i:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            i = 11
            k = 6.1
            while i <= 20:
                if condizione == i:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            if condizione == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.6))
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return condizione


def sceglitecn(dati, tecnica):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    condSconosciuta = GlobalImgVar.imgGambitSconosciuta
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico le scenette
    scetecn = GlobalImgVar.vetImgTecnicheMenu

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 8:
                if GlobalHWVar.gsy // 18 * 4.4 <= yMouse <= GlobalHWVar.gsy // 18 * 5.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 0
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 4.6
                elif GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.1
                elif GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7.1
                elif GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.1
                elif GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9.1
                elif GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.1
                elif GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 11.1
                elif GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.1
                elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.1
                elif GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.1
                elif GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 15.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 15.1
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif GlobalHWVar.gsx // 32 * 8 <= xMouse <= GlobalHWVar.gsx // 32 * 16:
                if GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 6.1
                elif GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 7.1
                elif GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 8.1
                elif GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 9.1
                elif GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 10.1
                elif GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 11.1
                elif GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 12.1
                elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 13.1
                elif GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 14.1
                elif GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 15.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalHWVar.gsx // 32 * 8
                    yp = GlobalHWVar.gsy // 18 * 15.1
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            else:
                i = 11
                c = 1
                while i <= 30:
                    if voceMarcata == c:
                        if dati[i] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            tecnica = c
                            risposta = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        break
                    i += 1
                    c += 1
                if voceMarcata == 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    tecnica = 0
                    risposta = True
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp - GlobalHWVar.gsy // 18 * 1.5
                        xp = GlobalHWVar.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 15.1
                else:
                    if voceMarcata == 0:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 15.1
                    else:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp - GlobalHWVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = xp - GlobalHWVar.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp + GlobalHWVar.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 4.6
                            xp = GlobalHWVar.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = yp + GlobalHWVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = xp + GlobalHWVar.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GenericFunc.messaggio("Scegli tecnica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Cancella settaggio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.7, 45)
                if dati[11] > 0:
                    GenericFunc.messaggio("Scossa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[12] > 0:
                    GenericFunc.messaggio("Cura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[13] > 0:
                    GenericFunc.messaggio("Antidoto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[14] > 0:
                    GenericFunc.messaggio("Freccia elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[15] > 0:
                    GenericFunc.messaggio("Tempesta elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[16] > 0:
                    GenericFunc.messaggio("Raffreddamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[17] > 0:
                    GenericFunc.messaggio("Auto-ricarica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[18] > 0:
                    GenericFunc.messaggio("Cura +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[19] > 0:
                    GenericFunc.messaggio("Scossa +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[20] > 0:
                    GenericFunc.messaggio("Freccia elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                if dati[21] > 0:
                    GenericFunc.messaggio("Velocizza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[22] > 0:
                    GenericFunc.messaggio("Carica attacco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[23] > 0:
                    GenericFunc.messaggio("Carica difesa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[24] > 0:
                    GenericFunc.messaggio("Efficienza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[25] > 0:
                    GenericFunc.messaggio("Tempesta elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[26] > 0:
                    GenericFunc.messaggio("Cura ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[27] > 0:
                    GenericFunc.messaggio("Auto-ricarica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[28] > 0:
                    GenericFunc.messaggio("Scossa ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[29] > 0:
                    GenericFunc.messaggio("Freccia Elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[30] > 0:
                    GenericFunc.messaggio("Tempesta elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 40)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 16)), 2)

            grandezzaCarattereDescrizioni = 40
            larghezzaTestoDescrizioni = GlobalHWVar.gpx * 13
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            if voceMarcata == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(scetecn[0], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                GenericFunc.messaggio("Cancella settaggio:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Cancella il settaggio di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if voceMarcata == 1:
                if dati[11] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[1], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Scossa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[0]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge danni a un nemico vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 2:
                if dati[12] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[2], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Cura:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[1]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Recupera un po' di <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 3:
                if dati[13] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[3], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Antidoto:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[2]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Cura avvelenamento a Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 4:
                if dati[14] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[4], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Freccia elettrica:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[3]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge danni a distanza a un nemico.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 5:
                if dati[15] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[5], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Tempesta elettrica:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[4]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 6:
                if dati[16] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[6], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Raffreddamento:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[5]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 7:
                if dati[17] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[7], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Auto-ricarica:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[6]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Ricarica un po' Impo ma richiede due turni e provoca surriscaldamento (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 8:
                if dati[18] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[8], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Cura +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[7]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Recupera molti <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 9:
                if dati[19] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[9], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Scossa +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[8]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge molti danni a un nemico vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 10:
                if dati[20] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[10], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Freccia elettrica +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[9]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge molti danni a distanza a un nemico.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 11:
                if dati[21] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[11], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Velocizza:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[10]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Permette a Impo, se non surriscaldato, di eseguire due azioni al turno. Provoca surriscaldamento dopo 15 turni dall'esecuzione (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 12:
                if dati[22] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[12], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Carica attacco:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[11]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Incrementa l'attacco di Lucy per 10 turni (non ha effetto sui nemici).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 13:
                if dati[23] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[13], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Carica difesa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[12]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Incrementa la difesa di Lucy per 10 turni (non ha effetto sui nemici).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 14:
                if dati[24] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[14], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Efficienza:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[13]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio(u"Tutte le tecniche costano la metà dei <*>#italic#Pe<*> per 15 turni. Si annulla con surriscaldamento (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 15:
                if dati[25] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[15], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Tempesta elettrica +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[14]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 16:
                if dati[26] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[16], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Cura ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[15]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio(u"Recupera un enorme quantità dei <*>#italic#Pv<*> di Lucy.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 17:
                if dati[27] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[17], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Auto-ricarica +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[16]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Ricarica di molto Impo ma richiede due turni e provoca surriscaldamento (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 18:
                if dati[28] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[18], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Scossa ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[17]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge enormi danni a un nemico vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 19:
                if dati[29] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[19], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Freccia Elettrica ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[18]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge enormi danni a distanza a un nemico.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 20:
                if dati[30] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[20], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Tempesta elettrica ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    GenericFunc.messaggio("Costo Pe: " + str(GlobalGameVar.costoTecniche[19]), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27.5, GlobalHWVar.gsy // 18 * 13.8, 45)
                    GenericFunc.messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    GenericFunc.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if tecnica == i:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            i = 11
            k = 6.1
            while i <= 20:
                if tecnica == i:
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            if tecnica == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.6))
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return tecnica


def modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit):
    if voceMarcata > voceMarcataVecchia:
        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
        imgRigaSelezionata = imgRigheGambit[voceMarcataVecchia - 6]
        i = voceMarcataVecchia - 6
        while i < voceMarcata - 6:
            dati[101 + i] = dati[101 + i + 1]
            dati[111 + i] = dati[111 + i + 1]
            imgRigheGambit[i] = imgRigheGambit[i + 1]
            i += 1
        dati[101 + voceMarcata - 6] = condizioneSelezionata
        dati[111 + voceMarcata - 6] = azioneSelezionata
        imgRigheGambit[voceMarcata - 6] = imgRigaSelezionata
    elif voceMarcata < voceMarcataVecchia:
        condizioneSelezionata = dati[101 + voceMarcataVecchia - 6]
        azioneSelezionata = dati[111 + voceMarcataVecchia - 6]
        imgRigaSelezionata = imgRigheGambit[voceMarcataVecchia - 6]
        i = voceMarcataVecchia - 6
        while i > voceMarcata - 6:
            dati[101 + i] = dati[101 + i - 1]
            dati[111 + i] = dati[111 + i - 1]
            imgRigheGambit[i] = imgRigheGambit[i - 1]
            i -= 1
        dati[101 + voceMarcata - 6] = condizioneSelezionata
        dati[111 + voceMarcata - 6] = azioneSelezionata
        imgRigheGambit[voceMarcata - 6] = imgRigaSelezionata
    return dati, imgRigheGambit


def equiprobo(dati):
    robosta = GlobalImgVar.roboo1
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sfondoOggetto = GlobalImgVar.sfondoOggettoMenu
    sconosciutoEquip = GlobalImgVar.sconosciutoEquipMenu
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 6.8
    risposta = False
    riordinamento = False
    annullaRiordinamento = False
    imgRigheGambit = []
    datiPrimaDiRiordinamento = list(dati)
    vxpGambit = xp
    vypGambit = yp
    voceMarcata = 1
    voceGambitMarcata = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    vetImgBatterie = GlobalImgVar.vetImgBatterieMenu

    vetIcoBatterie = []
    i = 0
    while i < 5:
        if dati[71 + i] > 0:
            vetIcoBatterie.append(GlobalImgVar.vetIcoBatterieMenu[i])
        else:
            vetIcoBatterie.append(sconosciutoEquip)
        i += 1

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if not riordinamento:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 6 and GlobalHWVar.gsy // 18 * 6 <= yMouse <= GlobalHWVar.gsy // 18 * 8:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.8
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 6 and GlobalHWVar.gsy // 18 * 8 <= yMouse <= GlobalHWVar.gsy // 18 * 10:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.8
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 6 and GlobalHWVar.gsy // 18 * 10 <= yMouse <= GlobalHWVar.gsy // 18 * 12:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.8
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 6 and GlobalHWVar.gsy // 18 * 12 <= yMouse <= GlobalHWVar.gsy // 18 * 14:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.8
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 6 and GlobalHWVar.gsy // 18 * 14 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.8
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 6.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 7.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 8.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 9.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 10.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 11.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 12.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 13.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 14.2
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 10.8 and GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 15.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 6.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 7.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 8.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 9.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 10.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 21
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 11.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 22
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 12.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 23
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 13.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 24
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 14.2
                elif GlobalHWVar.gsx // 32 * 10.8 <= xMouse <= GlobalHWVar.gsx // 32 * 17 and GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 25
                    xp = GlobalHWVar.gsx // 32 * 10.8
                    yp = GlobalHWVar.gsy // 18 * 15.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 26
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 6.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 27
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 7.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 28
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 8.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 29
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 9.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 30
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 10.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 31
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 11.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 32
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 12.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 33
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 13.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 34
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 14.2
                elif GlobalHWVar.gsx // 32 * 17 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 35
                    xp = GlobalHWVar.gsx // 32 * 17
                    yp = GlobalHWVar.gsy // 18 * 15.2
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif riordinamento:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 6.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 7.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 8.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 9.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 10.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 11.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 12.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 13.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 14.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalHWVar.gsx // 32 * 7 <= xMouse <= GlobalHWVar.gsx // 32 * 23 and GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 16:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalHWVar.gsx // 32 * 7
                    yp = GlobalHWVar.gsy // 18 * 15.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            if not riordinamento:
                risposta = True
            else:
                primoFrame = True
                riordinamento = False
                annullaRiordinamento = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            # riordina
            if riordinamento:
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    primoFrame = True
                    riordinamento = False
                    annullaRiordinamento = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    primoFrame = True
                    riordinamento = False
            else:
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                else:
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armrob
                    if voceMarcata == 1:
                        if dati[71] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            dati[9] = 0
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if voceMarcata == 2:
                        if dati[72] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            dati[9] = 1
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if voceMarcata == 3:
                        if dati[73] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            dati[9] = 2
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if voceMarcata == 4:
                        if dati[74] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            dati[9] = 3
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if voceMarcata == 5:
                        if dati[75] != 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            dati[9] = 4
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)

                    # riordina
                    if 6 <= voceMarcata <= 15:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        riordinamento = True
                        primoFrame = True
                        datiPrimaDiRiordinamento = list(dati)
                        vxpGambit = xp
                        vypGambit = yp
                        voceGambitMarcata = voceMarcata

                    # condizioni
                    i = 101
                    c = 16
                    while i <= 110:
                        if voceMarcata == c:
                            primoFrame = True
                            if dati[i] != -1:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                dati[i] = sceglicondiz(dati, dati[i])
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        i += 1
                        c += 1

                    # tecniche
                    i = 111
                    c = 26
                    while i <= 120:
                        if voceMarcata == c:
                            primoFrame = True
                            if dati[i] != -1:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                dati[i] = sceglitecn(dati, dati[i])
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        i += 1
                        c += 1
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if riordinamento:
                    if voceMarcata != 6:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        i = 0
                        while i < 10:
                            if voceMarcata == i + 6:
                                condizioneSelezionata = dati[101 + i]
                                dati[101 + i] = dati[101 + i - 1]
                                dati[101 + i - 1] = condizioneSelezionata
                                azioneSelezionata = dati[111 + i]
                                dati[111 + i] = dati[111 + i - 1]
                                dati[111 + i - 1] = azioneSelezionata

                                # modifico anche il vettore delle immagini
                                rigaSelezionata = imgRigheGambit[i]
                                imgRigheGambit[i] = imgRigheGambit[i - 1]
                                imgRigheGambit[i - 1] = rigaSelezionata
                                break
                            i += 1
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gsy // 18 * 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDown = False
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 1:
                            voceMarcata += 4
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 14.8
                        else:
                            voceMarcata -= 1
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = yp - GlobalHWVar.gsy // 18 * 2
                    else:
                        if voceMarcata == 6 or voceMarcata == 16 or voceMarcata == 26:
                            voceMarcata += 9
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 15.2
                        else:
                            voceMarcata -= 1
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = yp - GlobalHWVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if not riordinamento:
                    if 1 <= voceMarcata <= 5:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if voceMarcata == 1:
                            voceMarcata += 26
                            yp = GlobalHWVar.gsy // 18 * 7.2
                        elif voceMarcata == 2:
                            voceMarcata += 27
                            yp = GlobalHWVar.gsy // 18 * 9.2
                        elif voceMarcata == 3:
                            voceMarcata += 28
                            yp = GlobalHWVar.gsy // 18 * 11.2
                        elif voceMarcata == 4:
                            voceMarcata += 29
                            yp = GlobalHWVar.gsy // 18 * 13.2
                        elif voceMarcata == 5:
                            voceMarcata += 30
                            yp = GlobalHWVar.gsy // 18 * 15.2
                        xp = GlobalHWVar.gsx // 32 * 17
                    elif 6 <= voceMarcata <= 15:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if 6 <= voceMarcata <= 7:
                            if voceMarcata == 6:
                                voceMarcata -= 5
                            elif voceMarcata == 7:
                                voceMarcata -= 6
                            yp = GlobalHWVar.gsy // 18 * 6.8
                        elif 8 <= voceMarcata <= 9:
                            if voceMarcata == 8:
                                voceMarcata -= 6
                            elif voceMarcata == 9:
                                voceMarcata -= 7
                            yp = GlobalHWVar.gsy // 18 * 8.8
                        elif 10 <= voceMarcata <= 11:
                            if voceMarcata == 10:
                                voceMarcata -= 7
                            elif voceMarcata == 11:
                                voceMarcata -= 8
                            yp = GlobalHWVar.gsy // 18 * 10.8
                        elif 12 <= voceMarcata <= 13:
                            if voceMarcata == 12:
                                voceMarcata -= 8
                            elif voceMarcata == 13:
                                voceMarcata -= 9
                            yp = GlobalHWVar.gsy // 18 * 12.8
                        elif 14 <= voceMarcata <= 15:
                            if voceMarcata == 14:
                                voceMarcata -= 9
                            elif voceMarcata == 15:
                                voceMarcata -= 10
                            yp = GlobalHWVar.gsy // 18 * 14.8
                        xp = GlobalHWVar.gsx // 32 * 1
                    elif 16 <= voceMarcata <= 25:
                        voceMarcata -= 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 7
                    elif 26 <= voceMarcata <= 35:
                        voceMarcata -= 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 10.8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if riordinamento:
                    if voceMarcata != 15:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        i = 0
                        while i < 10:
                            if voceMarcata == i + 6:
                                condizioneSelezionata = dati[101 + i]
                                dati[101 + i] = dati[101 + i + 1]
                                dati[101 + i + 1] = condizioneSelezionata
                                azioneSelezionata = dati[111 + i]
                                dati[111 + i] = dati[111 + i + 1]
                                dati[111 + i + 1] = azioneSelezionata

                                # modifico anche il vettore delle immagini
                                rigaSelezionata = imgRigheGambit[i]
                                imgRigheGambit[i] = imgRigheGambit[i + 1]
                                imgRigheGambit[i + 1] = rigaSelezionata
                                break
                            i += 1
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gsy // 18 * 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        bottoneDown = False
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 5:
                            voceMarcata -= 4
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 6.8
                        else:
                            voceMarcata += 1
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = yp + GlobalHWVar.gsy // 18 * 2
                    else:
                        if voceMarcata == 15 or voceMarcata == 25 or voceMarcata == 35:
                            voceMarcata -= 9
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 6.2
                        else:
                            voceMarcata += 1
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = yp + GlobalHWVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if not riordinamento:
                    if 1 <= voceMarcata <= 5:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if voceMarcata == 1:
                            voceMarcata += 6
                            yp = GlobalHWVar.gsy // 18 * 7.2
                        elif voceMarcata == 2:
                            voceMarcata += 7
                            yp = GlobalHWVar.gsy // 18 * 9.2
                        elif voceMarcata == 3:
                            voceMarcata += 8
                            yp = GlobalHWVar.gsy // 18 * 11.2
                        elif voceMarcata == 4:
                            voceMarcata += 9
                            yp = GlobalHWVar.gsy // 18 * 13.2
                        elif voceMarcata == 5:
                            voceMarcata += 10
                            yp = GlobalHWVar.gsy // 18 * 15.2
                        xp = GlobalHWVar.gsx // 32 * 7
                    elif 6 <= voceMarcata <= 15:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 10.8
                    elif 16 <= voceMarcata <= 25:
                        voceMarcata += 10
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        xp = GlobalHWVar.gsx // 32 * 17
                    elif 26 <= voceMarcata <= 35:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if 26 <= voceMarcata <= 27:
                            if voceMarcata == 26:
                                voceMarcata -= 25
                            elif voceMarcata == 27:
                                voceMarcata -= 26
                            yp = GlobalHWVar.gsy // 18 * 6.8
                        elif 28 <= voceMarcata <= 29:
                            if voceMarcata == 28:
                                voceMarcata -= 26
                            elif voceMarcata == 29:
                                voceMarcata -= 27
                            yp = GlobalHWVar.gsy // 18 * 8.8
                        elif 30 <= voceMarcata <= 31:
                            if voceMarcata == 30:
                                voceMarcata -= 27
                            elif voceMarcata == 31:
                                voceMarcata -= 28
                            yp = GlobalHWVar.gsy // 18 * 10.8
                        elif 32 <= voceMarcata <= 33:
                            if voceMarcata == 32:
                                voceMarcata -= 28
                            elif voceMarcata == 33:
                                voceMarcata -= 29
                            yp = GlobalHWVar.gsy // 18 * 12.8
                        elif 34 <= voceMarcata <= 35:
                            if voceMarcata == 34:
                                voceMarcata -= 29
                            elif voceMarcata == 35:
                                voceMarcata -= 30
                            yp = GlobalHWVar.gsy // 18 * 14.8
                        xp = GlobalHWVar.gsx // 32 * 1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15.5))

                GenericFunc.messaggio("Setta Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Batterie", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.5, GlobalHWVar.gsy // 18 * 4.6, 60, centrale=True)
                GenericFunc.messaggio("Ordine", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.8, GlobalHWVar.gsy // 18 * 4.6, 60, centrale=True)
                GenericFunc.messaggio("Condizione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.9, GlobalHWVar.gsy // 18 * 4.6, 60, centrale=True)
                GenericFunc.messaggio("Tecnica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.8, GlobalHWVar.gsy // 18 * 4.6, 60, centrale=True)
                # equip batteria
                i = 0
                while i < 5:
                    GlobalHWVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalHWVar.gsx // 32 * 2.5, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    GlobalHWVar.disegnaImmagineSuSchermo(vetIcoBatterie[i], (GlobalHWVar.gsx // 32 * 2.5, (GlobalHWVar.gsy // 18 * 6 + (GlobalHWVar.gpy * 2 * i))))
                    i += 1
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 1.5), int(GlobalHWVar.gpy * 5.6)), (int(GlobalHWVar.gpx * 5.5), int(GlobalHWVar.gpy * 5.6)), 1)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 4.4)), (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 5.4)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 4.4)), (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 5.4)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 7.5), int(GlobalHWVar.gpy * 5.6)), (int(GlobalHWVar.gpx * 22.5), int(GlobalHWVar.gpy * 5.6)), 1)
            elif not riordinamento:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10.2))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 10.8, GlobalHWVar.gsy // 18 * 5.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10.2))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5.8, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10.2))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 10.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 11.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 13.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 14.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15.8, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 16)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 16)), 2)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if annullaRiordinamento:
                dati = list(datiPrimaDiRiordinamento)
                annullaRiordinamento = False
                xp = vxpGambit
                yp = vypGambit
                voceMarcata = voceGambitMarcata

            if primoFrame:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5.8, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10.3))
                if riordinamento:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (xp, yp - (GlobalHWVar.gpy // 4), GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 1))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 16)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 16)), 2)
                # programmazione Colco
                i = 1
                while i <= 10:
                    GenericFunc.messaggio(str(i), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.8, GlobalHWVar.gsy // 18 * (i + 5.2), 50, centrale=True)
                    i += 1
                posXCondizioni = 11.8
                c = 6.3
                for i in range(101, 111):
                    if dati[i] == -1:
                        GenericFunc.messaggio("---", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 0:
                        GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 1:
                        GenericFunc.messaggio("Lucy con Pv < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 2:
                        GenericFunc.messaggio("Lucy con Pv < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 3:
                        GenericFunc.messaggio("Lucy con Pv < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 4:
                        GenericFunc.messaggio("Lucy con veleno", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 5:
                        GenericFunc.messaggio("Impo surriscaldato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 6:
                        GenericFunc.messaggio("Impo con Pe < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 7:
                        GenericFunc.messaggio("Impo con Pe < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 8:
                        GenericFunc.messaggio("Impo con Pe < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 9:
                        GenericFunc.messaggio("Sempre a Lucy", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 10:
                        GenericFunc.messaggio("Sempre a Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 11:
                        GenericFunc.messaggio("Nemico a caso", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 12:
                        GenericFunc.messaggio("Nemico vicino", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 13:
                        GenericFunc.messaggio("Nemico lontano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 14:
                        GenericFunc.messaggio("Nemico con Pv < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 15:
                        GenericFunc.messaggio("Nemico con Pv < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 16:
                        GenericFunc.messaggio("Nemico con Pv < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 17:
                        GenericFunc.messaggio("Nemico con meno Pv", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 18:
                        GenericFunc.messaggio("Numero di nemici > 1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 19:
                        GenericFunc.messaggio("Numero di nemici > 4", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 20:
                        GenericFunc.messaggio("Numero di nemici > 7", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    c += 1
                posXTecniche = 18
                c = 6.3
                for i in range(111, 121):
                    if dati[i] == -1:
                        GenericFunc.messaggio("---", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 0:
                        GenericFunc.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 1:
                        GenericFunc.messaggio("Scossa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 2:
                        GenericFunc.messaggio("Cura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 3:
                        GenericFunc.messaggio("Antidoto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 4:
                        GenericFunc.messaggio("Freccia elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 5:
                        GenericFunc.messaggio("Tempesta elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 6:
                        GenericFunc.messaggio("Raffreddamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 7:
                        GenericFunc.messaggio("Auto-ricarica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 8:
                        GenericFunc.messaggio("Cura +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 9:
                        GenericFunc.messaggio("Scossa +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 10:
                        GenericFunc.messaggio("Freccia elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 11:
                        GenericFunc.messaggio("Velocizza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 12:
                        GenericFunc.messaggio("Carica attacco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 13:
                        GenericFunc.messaggio("Carica difesa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 14:
                        GenericFunc.messaggio("Efficienza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 15:
                        GenericFunc.messaggio("Tempesta elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 16:
                        GenericFunc.messaggio("Cura ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 17:
                        GenericFunc.messaggio("Auto-ricarica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 18:
                        GenericFunc.messaggio("Scossa ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 19:
                        GenericFunc.messaggio("Freccia Elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 20:
                        GenericFunc.messaggio("Tempesta elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    c += 1

                if riordinamento:
                    screenRiordinamento = GlobalHWVar.schermo.copy()
                    imgRigheGambit = []
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 6.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 7.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 8.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 9.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 10.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 11.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 12.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 13.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 14.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 15.2, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 0.6)).convert())

            if annullaRiordinamento:
                annullaRiordinamento = False

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)

            if primoFrame or not riordinamento:
                grandezzaCarattereStatistiche = 40
                posizioneStatisticheX = int(GlobalHWVar.gsx // 32 * 28)
                posizioneStatPeY = int(GlobalHWVar.gsy // 18 * 9.1)
                posizioneStatDifY = int(GlobalHWVar.gsy // 18 * 9.7)
                GlobalHWVar.disegnaImmagineSuSchermo(robosta, (GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 25), int(GlobalHWVar.gpy * 15)), (int(GlobalHWVar.gpx * 30), int(GlobalHWVar.gpy * 15)), 2)
                GlobalHWVar.disegnaImmagineSuSchermo(vetImgBatterie[dati[9]], (GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10))
                GenericFunc.messaggio("Statistiche:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 8.1, 60)
                GenericFunc.messaggio("Pe totali: %i" % entot, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, posizioneStatPeY, grandezzaCarattereStatistiche)
                GenericFunc.messaggio("Difesa: %i" % difro, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, posizioneStatDifY, grandezzaCarattereStatistiche)

                # mostrare descrizione batterie / priorità / condizioni / azioni
                grandezzaCarattereDescrizioni = 40
                posizioneTitoliY = int(GlobalHWVar.gsy // 18 * 4.8)
                posizioneDescrizioniX = int(GlobalHWVar.gsx // 32 * 23.5)
                posizioneDescrizioniY = int(GlobalHWVar.gsy // 18 * 5.8)
                larghezzaTestoDescrizioni = int(GlobalHWVar.gpx * 8)
                spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
                if voceMarcata == 1:
                    if dati[71] != 0:
                        GenericFunc.messaggio("Batteria piccola:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        GenericFunc.messaggio("Batteria che contiene poca alimentazione.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 0:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = 0 - (dati[9] * dati[9] * 30)
                        if dati[9] > 0:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 2:
                    if dati[72] != 0:
                        GenericFunc.messaggio("Batteria discreta:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        GenericFunc.messaggio("Batteria con una buona capienza e ottimizzazione del sistema difensivo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 1:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif dati[9] < 1:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = 30 - (dati[9] * dati[9] * 30)
                        if dati[9] > 1:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif dati[9] < 1:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 3:
                    if dati[73] != 0:
                        GenericFunc.messaggio("Batteria capiente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        GenericFunc.messaggio(u"Batteria con una grande capacità e un ottimo sistema difensivo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 2:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif dati[9] < 2:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = 120 - (dati[9] * dati[9] * 30)
                        if dati[9] > 2:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif dati[9] < 2:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 4:
                    if dati[74] != 0:
                        GenericFunc.messaggio("Batteria enorme:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        GenericFunc.messaggio(u"Grande batteria che permette a Impo di utilizzare le tecniche più dispendiose.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 3:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif dati[9] < 3:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = 270 - (dati[9] * dati[9] * 30)
                        if dati[9] > 3:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif dati[9] < 3:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 5:
                    if dati[75] != 0:
                        GenericFunc.messaggio("Batteria illimitata:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        GenericFunc.messaggio("Batteria incredibilmente capiente. Permette un eccellente ottimizzazione del sistema difensivo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 4:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif dati[9] < 4:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = 480 - (dati[9] * dati[9] * 30)
                        if dati[9] > 4:
                            GenericFunc.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif dati[9] < 4:
                            GenericFunc.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)

                if 6 <= voceMarcata <= 15:
                    GenericFunc.messaggio(u"Ordine:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Indica la priorità dell'azione. Impo eseguirà la tecnica associata alla prima condizione verificata della lista.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

                if 16 <= voceMarcata <= 25:
                    GenericFunc.messaggio("Condizione:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"Indica la situazione che si deve verificare affinché Impo esegua la tecnica associata.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

                if 26 <= voceMarcata <= 35:
                    GenericFunc.messaggio("Tecnica:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    GenericFunc.messaggio(u"La tecnica che Impo eseguirà quando si verifica la condizione associata.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5.8, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (xp, yp - (GlobalHWVar.gpy // 4), GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 1))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 10.8) - 1, int(GlobalHWVar.gpy * 16)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 17) - 1, int(GlobalHWVar.gpy * 16)), 2)
                i = 0
                for riga in imgRigheGambit:
                    GlobalHWVar.disegnaImmagineSuSchermo(riga, (GlobalHWVar.gsx // 32 * 7, (GlobalHWVar.gsy // 18 * 6.2) + (GlobalHWVar.gpy * i)))
                    i += 1

            # puntatore vecchio batterie/riordinamento gambit
            if dati[9] == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6.8))
            if dati[9] == 1:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8.8))
            if dati[9] == 2:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 10.8))
            if dati[9] == 3:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 12.8))
            if dati[9] == 4:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14.8))
            if riordinamento:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (vxpGambit, vypGambit))

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if voceMarcata >= 6 and not riordinamento:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 7.5, yp + (int(GlobalHWVar.gpy * 0.7))), (GlobalHWVar.gsx // 32 * 10.6, yp + (int(GlobalHWVar.gpy * 0.7))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11, yp + (int(GlobalHWVar.gpy * 0.7))), (GlobalHWVar.gsx // 32 * 16.8, yp + (int(GlobalHWVar.gpy * 0.7))), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 17.2, yp + (int(GlobalHWVar.gpy * 0.7))), (GlobalHWVar.gsx // 32 * 22.5, yp + (int(GlobalHWVar.gpy * 0.7))), 2)
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return dati


def oggetti(dati, colcoInCasellaVista):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sconosciutoOggetto = GlobalImgVar.sconosciutoOggettoMenu3
    if dati[0] < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        perssta = GlobalImgVar.imgLucy1MenuOggetti
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        perssta = GlobalImgVar.imgFraMaggioreMenuOggetti
    elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        perssta = GlobalImgVar.imgLucy1MenuOggetti
    else:
        perssta = GlobalImgVar.imgLucy2MenuOggetti
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 6.2
    xpv = xp
    ypv = yp
    usauno = False
    usa = 0
    risposta = False
    attacco = 0
    oggetton = 1
    voceMarcata = 0
    aggiornaSchermo = False
    impossibileUsareCaricaBatt = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    imgOggetti = []
    i = 1
    while i <= 10:
        if dati[i + 30] >= 0:
            imgOggetti.append(GlobalImgVar.vetImgOggettiMenu[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        oggettonVecchio = oggetton
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if usa != 0:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalHWVar.gsy // 18 * 14.5 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5:
                    if GlobalHWVar.gsx // 32 * 11 <= xMouse <= GlobalHWVar.gsx // 32 * 15:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 12.7
                        yp = GlobalHWVar.gsy // 18 * 15.1
                    elif GlobalHWVar.gsx // 32 * 15 <= xMouse <= GlobalHWVar.gsx // 32 * 19:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 15
                        yp = GlobalHWVar.gsy // 18 * 15.1
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 11:
                    if GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 1
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 6.2
                    elif GlobalHWVar.gsy // 18 * 6.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 2
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 7.2
                    elif GlobalHWVar.gsy // 18 * 7.9 <= yMouse <= GlobalHWVar.gsy // 18 * 8.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 3
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    elif GlobalHWVar.gsy // 18 * 8.9 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 4
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 9.2
                    elif GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 10.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 5
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 10.2
                    elif GlobalHWVar.gsy // 18 * 10.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 6
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 11.2
                    elif GlobalHWVar.gsy // 18 * 11.9 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 7
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.2
                    elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 8
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 13.2
                    elif GlobalHWVar.gsy // 18 * 13.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 9
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 14.2
                    elif GlobalHWVar.gsy // 18 * 14.9 <= yMouse <= GlobalHWVar.gsy // 18 * 15.9:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        oggetton = 10
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton) and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            voceMarcata = 0
            if usa != 0:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                xp = GlobalHWVar.gsx // 32 * 1
                if usa == 1:
                    yp = GlobalHWVar.gsy // 18 * 6.2
                if usa == 2:
                    yp = GlobalHWVar.gsy // 18 * 7.2
                if usa == 3:
                    yp = GlobalHWVar.gsy // 18 * 8.2
                if usa == 4:
                    yp = GlobalHWVar.gsy // 18 * 9.2
                if usa == 5:
                    yp = GlobalHWVar.gsy // 18 * 10.2
                if usa == 6:
                    yp = GlobalHWVar.gsy // 18 * 11.2
                if usa == 7:
                    yp = GlobalHWVar.gsy // 18 * 12.2
                if usa == 8:
                    yp = GlobalHWVar.gsy // 18 * 13.2
                if usa == 9:
                    yp = GlobalHWVar.gsy // 18 * 14.2
                if usa == 10:
                    yp = GlobalHWVar.gsy // 18 * 15.2
                usa = 0
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                voceMarcata = 0
                if usa != 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    xp = GlobalHWVar.gsx // 32 * 1
                    if usa == 1:
                        yp = GlobalHWVar.gsy // 18 * 6.2
                    if usa == 2:
                        yp = GlobalHWVar.gsy // 18 * 7.2
                    if usa == 3:
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    if usa == 4:
                        yp = GlobalHWVar.gsy // 18 * 9.2
                    if usa == 5:
                        yp = GlobalHWVar.gsy // 18 * 10.2
                    if usa == 6:
                        yp = GlobalHWVar.gsy // 18 * 11.2
                    if usa == 7:
                        yp = GlobalHWVar.gsy // 18 * 12.2
                    if usa == 8:
                        yp = GlobalHWVar.gsy // 18 * 13.2
                    if usa == 9:
                        yp = GlobalHWVar.gsy // 18 * 14.2
                    if usa == 10:
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    usa = 0
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
            else:
                usadue = True
                # usa?
                if voceMarcata == 1:
                    usadue = False
                    # pozione
                    if usa == 1:
                        dati[5] = dati[5] + 100
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[31] = dati[31] - 1
                        yp = GlobalHWVar.gsy // 18 * 6.2
                    # carica batt
                    if usa == 2:
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[32] = dati[32] - 1
                        yp = GlobalHWVar.gsy // 18 * 7.2
                    # antidoto
                    if usa == 3:
                        dati[121] = 0
                        dati[33] = dati[33] - 1
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    # super pozione
                    if usa == 4:
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[34] = dati[34] - 1
                        yp = GlobalHWVar.gsy // 18 * 9.2
                    # carica migliorato
                    if usa == 5:
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[35] = dati[35] - 1
                        yp = GlobalHWVar.gsy // 18 * 10.2
                    # bomba
                    if usa == 6:
                        attacco = 2
                        yp = GlobalHWVar.gsy // 18 * 11.2
                    # bomba veleno
                    if usa == 7:
                        attacco = 3
                        yp = GlobalHWVar.gsy // 18 * 12.2
                    # esca
                    if usa == 8:
                        attacco = 4
                        yp = GlobalHWVar.gsy // 18 * 13.2
                    # bomba appiccicosa
                    if usa == 9:
                        attacco = 5
                        yp = GlobalHWVar.gsy // 18 * 14.2
                    # bomba potenziata
                    if usa == 10:
                        attacco = 6
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    if (usa == 2 or usa == 5) and dati[0] < GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        primoFrame = True
                        xp = GlobalHWVar.gsx // 32 * 1
                        voceMarcata = 0
                        usa = 0
                elif voceMarcata == 2:
                    voceMarcata = 0
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    xp = GlobalHWVar.gsx // 32 * 1
                    if usa == 1:
                        yp = GlobalHWVar.gsy // 18 * 6.2
                    if usa == 2:
                        yp = GlobalHWVar.gsy // 18 * 7.2
                    if usa == 3:
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    if usa == 4:
                        yp = GlobalHWVar.gsy // 18 * 9.2
                    if usa == 5:
                        yp = GlobalHWVar.gsy // 18 * 10.2
                    if usa == 6:
                        yp = GlobalHWVar.gsy // 18 * 11.2
                    if usa == 7:
                        yp = GlobalHWVar.gsy // 18 * 12.2
                    if usa == 8:
                        yp = GlobalHWVar.gsy // 18 * 13.2
                    if usa == 9:
                        yp = GlobalHWVar.gsy // 18 * 14.2
                    if usa == 10:
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    usa = 0
                    usadue = False
                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                if usadue:
                    if oggetton == 1:
                        if dati[31] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 1
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 2:
                        if dati[32] > 0 and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 2
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            if not dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] or not colcoInCasellaVista:
                                impossibileUsareCaricaBatt = True
                    if oggetton == 3:
                        if dati[33] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 3
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 4:
                        if dati[34] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 4
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 5:
                        if dati[35] > 0 and dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 5
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            if not dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] or not colcoInCasellaVista:
                                impossibileUsareCaricaBatt = True
                    if oggetton == 6:
                        if dati[36] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 6
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 7:
                        if dati[37] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 7
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 8:
                        if dati[38] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 8
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 9:
                        if dati[39] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 9
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 10:
                        if dati[40] > 0:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 10
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    if oggetton != 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        oggetton = oggetton - 1
                        yp = yp - GlobalHWVar.gsy // 18 * 1
                    elif oggetton == 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 15.2
                        oggetton = 10
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 12.7
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    if oggetton != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        oggetton = oggetton + 1
                        yp = yp + GlobalHWVar.gsy // 18 * 1
                    elif oggetton == 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 6.2
                        oggetton = 1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 15
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GenericFunc.messaggio("Oggetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                GenericFunc.messaggio("Nome oggetto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.3, GlobalHWVar.gsy // 18 * 4.7, 50, centrale=True)
                GenericFunc.messaggio(u"Quantità", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 4.7, 50, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 1.5), int(GlobalHWVar.gpy * 5.6)), (int(GlobalHWVar.gpx * 10.5), int(GlobalHWVar.gpy * 5.6)), 1)
                if dati[31] >= 0:
                    GenericFunc.messaggio("Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 45)
                    GenericFunc.messaggio("x%i" % dati[31], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 6.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 45)
                if dati[32] >= 0:
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                        GenericFunc.messaggio("Alimentazione 100gr", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 45)
                    else:
                        GenericFunc.messaggio("Alimentazione 100gr", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 45)
                    GenericFunc.messaggio("x%i" % dati[32], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 7.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 45)
                if dati[33] >= 0:
                    GenericFunc.messaggio("Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 45)
                    GenericFunc.messaggio("x%i" % dati[33], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 8.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 45)
                if dati[34] >= 0:
                    GenericFunc.messaggio("Super pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 45)
                    GenericFunc.messaggio("x%i" % dati[34], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 9.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 45)
                if dati[35] >= 0:
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                        GenericFunc.messaggio("Alimentazione 250gr", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 45)
                    else:
                        GenericFunc.messaggio("Alimentazione 250gr", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 45)
                    GenericFunc.messaggio("x%i" % dati[35], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 10.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 45)
                if dati[36] >= 0:
                    GenericFunc.messaggio("Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 45)
                    GenericFunc.messaggio("x%i" % dati[36], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 11.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 45)
                if dati[37] >= 0:
                    GenericFunc.messaggio("Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 45)
                    GenericFunc.messaggio("x%i" % dati[37], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 12.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 45)
                if dati[38] >= 0:
                    GenericFunc.messaggio("Esca", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 45)
                    GenericFunc.messaggio("x%i" % dati[38], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 13.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 45)
                if dati[39] >= 0:
                    GenericFunc.messaggio("Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 45)
                    GenericFunc.messaggio("x%i" % dati[39], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 14.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 45)
                if dati[40] >= 0:
                    GenericFunc.messaggio("Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 45)
                    GenericFunc.messaggio("x%i" % dati[40], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 15.2, 45, centrale=True)
                else:
                    GenericFunc.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 45)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 7.6) - 1, int(GlobalHWVar.gpy * 4.5)), (int(GlobalHWVar.gpx * 7.6) - 1, int(GlobalHWVar.gpy * 5.4)), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 7.6) - 1, int(GlobalHWVar.gpy * 5.8)), (int(GlobalHWVar.gpx * 7.6) - 1, int(GlobalHWVar.gpy * 16)), 2)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 6.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 7.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 8.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 9.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 9.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 10.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 10.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 11.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 11.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 12.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 12.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 13.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 13.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 14.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.77, GlobalHWVar.gsx // 32 * 6.5, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 7.7, GlobalHWVar.gsy // 18 * 15.77, GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 19.5, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 14))
                if impossibileUsareCaricaBatt:
                    GenericFunc.messaggio(u"Impo è irraggiungibile!", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 12.2, GlobalHWVar.gsy // 18 * 15, 50)
                    if oggettonVecchio != oggetton:
                        impossibileUsareCaricaBatt = False
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14))
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14))
            if aggiornaInterfacciaPerCambioInput:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                aggiornaInterfacciaPerCambioInput = False
                if GlobalHWVar.mouseVisibile:
                    GenericFunc.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    GenericFunc.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    GenericFunc.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            # menu conferma
            if usa != 0:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15.5))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalHWVar.gsx // 32 * 15
                    yp = GlobalHWVar.gsy // 18 * 15.1
                    voceMarcata = 2
                    usauno = False
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                GenericFunc.messaggio("Usare?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 15.1, GlobalHWVar.gsy // 18 * 13.1, 85, centrale=True)
                GenericFunc.messaggio(u"Sì", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.4, GlobalHWVar.gsy // 18 * 14.9, 70)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 15) - 1, int(GlobalHWVar.gpy * 14.8)), (int(GlobalHWVar.gpx * 15) - 1, int(GlobalHWVar.gpy * 15.9)), 2)
                GenericFunc.messaggio("No", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 14.9, 70)

            grandezzaCarattereDescrizioni = 40
            larghezzaTestoDescrizioni = GlobalHWVar.gpx * 11
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            if dati[31] >= 0 and oggetton == 1:
                GenericFunc.messaggio("Pozione:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Recupera 100 <*>#italic#Pv<*>.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 1:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[32] >= 0 and oggetton == 2:
                GenericFunc.messaggio("Alimentazione 100gr:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Recupera 250 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 2:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[33] >= 0 and oggetton == 3:
                GenericFunc.messaggio("Medicina:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Cura avvelenamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 3:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[34] >= 0 and oggetton == 4:
                GenericFunc.messaggio("Super pozione:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Recupera 300 <*>#italic#Pv<*>.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 4:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[35] >= 0 and oggetton == 5:
                GenericFunc.messaggio("Alimentazione 250gr:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Recupera 600 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 5:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[36] >= 0 and oggetton == 6:
                GenericFunc.messaggio("Bomba:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Infligge un po' di danni ai nemici su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 6:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[37] >= 0 and oggetton == 7:
                GenericFunc.messaggio("Bomba velenosa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Infligge avvelenamento al nemico su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 7:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[38] >= 0 and oggetton == 8:
                GenericFunc.messaggio("Esca:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio(u"Distrae i nemici finché non viene distrutta. È possibile riprenderla passandoci sopra.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 8:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[39] >= 0 and oggetton == 9:
                GenericFunc.messaggio("Bomba appiccicosa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio(u"Dimezza la velocità del nemico su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 9:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
            if dati[40] >= 0 and oggetton == 10:
                GenericFunc.messaggio("Bomba potenziata:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)
                GenericFunc.messaggio("Infligge molti danni ai nemici su cui viene lanciata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 10:
                GenericFunc.messaggio("Sconosciuto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13.5, 60)

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            GenericFunc.messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 4.9, 50)
            GenericFunc.messaggio("Status alterati: ", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 5.7, 50)
            GlobalHWVar.disegnaImmagineSuSchermo(perssta, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4.6))
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 7.6)), (int(GlobalHWVar.gpx * 18.2), int(GlobalHWVar.gpy * 7.6)), 2)
            if dati[121]:
                avvelenato = GlobalImgVar.avvelenatoMenu
                GlobalHWVar.disegnaImmagineSuSchermo(avvelenato, (GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6.5))
            if dati[123] > 0:
                attaccopiu = GlobalImgVar.attaccopiuMenu
                GlobalHWVar.disegnaImmagineSuSchermo(attaccopiu, ((GlobalHWVar.gsx // 32 * 14) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 6.5))
            if dati[124] > 0:
                difesapiu = GlobalImgVar.difesapiuMenu
                GlobalHWVar.disegnaImmagineSuSchermo(difesapiu, ((GlobalHWVar.gsx // 32 * 14) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 6.5))
            # vita-status robo
            if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["incontratoColco"]:
                if dati[10] < 0:
                    dati[10] = 0
                GenericFunc.messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 8.4, 50)
                GenericFunc.messaggio("Status alterati: ", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 9.2, 50)
                robomen = GlobalImgVar.roboo2
                GlobalHWVar.disegnaImmagineSuSchermo(robomen, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8.1))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 11.1)), (int(GlobalHWVar.gpx * 18.2), int(GlobalHWVar.gpy * 11.1)), 2)
                if dati[122] > 0:
                    surriscaldato = GlobalImgVar.surriscaldatoMenu
                    GlobalHWVar.disegnaImmagineSuSchermo(surriscaldato, (GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10))
                if dati[125] > 0:
                    velocitapiu = GlobalImgVar.velocitapiuMenu
                    GlobalHWVar.disegnaImmagineSuSchermo(velocitapiu, ((GlobalHWVar.gsx // 32 * 14) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 10))
                if dati[126] > 0:
                    efficienzapiu = GlobalImgVar.efficienzapiuMenu
                    GlobalHWVar.disegnaImmagineSuSchermo(efficienzapiu, ((GlobalHWVar.gsx // 32 * 14) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 10))

            if attacco != 0:
                risposta = True

            GlobalHWVar.disegnaImmagineSuSchermo(imgOggetti[oggetton - 1], (GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3))
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if usa == 0:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 0.5))), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), (xp + (int(GlobalHWVar.gpx * 6.4)), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 6.8))), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), (xp + (int(GlobalHWVar.gpx * 9.5)), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
            else:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 0.5))), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), (xpv + (int(GlobalHWVar.gpx * 6.4)), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 6.8))), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), (xpv + (int(GlobalHWVar.gpx * 9.5)), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return dati, attacco
