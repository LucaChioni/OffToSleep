# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


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
    esci = False

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
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            esci = True
            bottoneDown = False
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

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))

                FunzioniGraficheGeneriche.messaggio("Equipaggiamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Armi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.5, GlobalHWVar.gsy // 18 * 4.5, 65, centrale=True)
                FunzioniGraficheGeneriche.messaggio("Protezioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 4.5, 65, centrale=True)
                FunzioniGraficheGeneriche.messaggio("Accessori", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18.5, GlobalHWVar.gsy // 18 * 4.5, 65, centrale=True)
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
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

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
            FunzioniGraficheGeneriche.messaggio("Statistiche:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 7.3, 60)
            FunzioniGraficheGeneriche.messaggio("Punti vita: %i" % pvtot, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatPvY, grandezzaCarattereStatistiche)
            FunzioniGraficheGeneriche.messaggio("Attacco ravvicinato: %i" % attVicino, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatAttRavY, grandezzaCarattereStatistiche)
            FunzioniGraficheGeneriche.messaggio("Attacco a distanza: %i" % attLontano, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatAttDistY, grandezzaCarattereStatistiche)
            FunzioniGraficheGeneriche.messaggio("Difesa: %i" % dif, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatDifY, grandezzaCarattereStatistiche)
            FunzioniGraficheGeneriche.messaggio(u"Probabilità parata: %i" % par + "%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, posizioneStatParY, grandezzaCarattereStatistiche)
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
                    FunzioniGraficheGeneriche.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi spada.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["spade"][0] - GlobalGameVar.statisticheEquipaggiamento["spade"][dati[6]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 2:
                if dati[42] != 0:
                    FunzioniGraficheGeneriche.messaggio("Spada di ferro:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Semplice spada di ferro.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["spade"][1] - GlobalGameVar.statisticheEquipaggiamento["spade"][dati[6]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 3:
                if dati[43] != 0:
                    FunzioniGraficheGeneriche.messaggio("Spadone d'acciaio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Grande spadone d'acciaio con ornamenti in oro. Studiato per permettere attacchi rapidi e potenti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["spade"][2] - GlobalGameVar.statisticheEquipaggiamento["spade"][dati[6]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 4:
                if dati[44] != 0:
                    FunzioniGraficheGeneriche.messaggio("Lykother:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Spada molto leggera e affilata. Sembra essere stata ricavata da un dente di una bestia enorme.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["spade"][3] - GlobalGameVar.statisticheEquipaggiamento["spade"][dati[6]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 5:
                if dati[45] != 0:
                    FunzioniGraficheGeneriche.messaggio("Mendaxritas:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Potentissima spada composta da materiali ignoti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["spade"][4] - GlobalGameVar.statisticheEquipaggiamento["spade"][dati[6]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # archi
            if voceMarcata == 6:
                if dati[46] != 0:
                    FunzioniGraficheGeneriche.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi arco.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["archi"][0] - GlobalGameVar.statisticheEquipaggiamento["archi"][dati[128]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 7:
                if dati[47] != 0:
                    FunzioniGraficheGeneriche.messaggio("Arco di legno:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Semplice arco in legno usato dalla maggior parte dei forestieri.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["archi"][1] - GlobalGameVar.statisticheEquipaggiamento["archi"][dati[128]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 8:
                if dati[48] != 0:
                    FunzioniGraficheGeneriche.messaggio("Arco di ferro:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Elaborato arco in ferro usato solo dai più esperti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["archi"][2] - GlobalGameVar.statisticheEquipaggiamento["archi"][dati[128]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 9:
                if dati[49] != 0:
                    FunzioniGraficheGeneriche.messaggio("Arco di precisione:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Sofisticato arco in legno e acciaio. Molto leggero e potente.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["archi"][3] - GlobalGameVar.statisticheEquipaggiamento["archi"][dati[128]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 10:
                if dati[50] != 0:
                    FunzioniGraficheGeneriche.messaggio("Accipiter:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Potentissimo arco di origine sconosciuta.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["archi"][4] - GlobalGameVar.statisticheEquipaggiamento["archi"][dati[128]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # armature
            if voceMarcata == 11:
                if dati[51] != 0:
                    FunzioniGraficheGeneriche.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi armatura.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["armature"][0] - GlobalGameVar.statisticheEquipaggiamento["armature"][dati[8]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 12:
                if dati[52] != 0:
                    FunzioniGraficheGeneriche.messaggio("Armatura di pelle:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Semplice armatura in pelle.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["armature"][1] - GlobalGameVar.statisticheEquipaggiamento["armature"][dati[8]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 13:
                if dati[53] != 0:
                    FunzioniGraficheGeneriche.messaggio("Armatura d'acciaio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Armatura d'acciaio con ornamenti in oro. Usata solo dagli ufficiali dell'esercito.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["armature"][2] - GlobalGameVar.statisticheEquipaggiamento["armature"][dati[8]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 14:
                if dati[54] != 0:
                    FunzioniGraficheGeneriche.messaggio("Lykodes:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Armatura formata da materiali leggeri e resistenti. Sembra essere stata ricavata dalle ossa di una bestia.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["armature"][3] - GlobalGameVar.statisticheEquipaggiamento["armature"][dati[8]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 15:
                if dati[55] != 0:
                    FunzioniGraficheGeneriche.messaggio("Loriquam:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Armatura incredibilmente resistente e leggera. La sua origine è ignota.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["armature"][4] - GlobalGameVar.statisticheEquipaggiamento["armature"][dati[8]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # scudi
            if voceMarcata == 16:
                if dati[56] != 0:
                    FunzioniGraficheGeneriche.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi scudo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiDif"][0] - GlobalGameVar.statisticheEquipaggiamento["scudiDif"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiPar"][0] - GlobalGameVar.statisticheEquipaggiamento["scudiPar"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 17:
                if dati[57] != 0:
                    FunzioniGraficheGeneriche.messaggio("Scudo di pelle:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Semplice scudo in pelle.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiDif"][1] - GlobalGameVar.statisticheEquipaggiamento["scudiDif"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiPar"][1] - GlobalGameVar.statisticheEquipaggiamento["scudiPar"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 18:
                if dati[58] != 0:
                    FunzioniGraficheGeneriche.messaggio("Scudo d'acciaio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Sofisticato scudo in acciaio e oro. Studiato per respingere gli attacchi più pesanti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiDif"][2] - GlobalGameVar.statisticheEquipaggiamento["scudiDif"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiPar"][2] - GlobalGameVar.statisticheEquipaggiamento["scudiPar"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 19:
                if dati[59] != 0:
                    FunzioniGraficheGeneriche.messaggio("Lykethmos:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Scudo molto leggero e resistente. Sembra essere stato ricavato dalle ossa più resistenti di una qualche bestia.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiDif"][3] - GlobalGameVar.statisticheEquipaggiamento["scudiDif"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiPar"][3] - GlobalGameVar.statisticheEquipaggiamento["scudiPar"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 20:
                if dati[60] != 0:
                    FunzioniGraficheGeneriche.messaggio("Clipequam:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Scudo incredibilmente resistente e leggero. Non è nota l'origine.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiDif"][4] - GlobalGameVar.statisticheEquipaggiamento["scudiDif"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    diff = GlobalGameVar.statisticheEquipaggiamento["scudiPar"][4] - GlobalGameVar.statisticheEquipaggiamento["scudiPar"][dati[7]]
                    if diff < 0:
                        FunzioniGraficheGeneriche.messaggio(str(diff) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    elif diff > 0:
                        FunzioniGraficheGeneriche.messaggio("+" + str(diff) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # guanti
            if voceMarcata == 21:
                if dati[61] != 0:
                    FunzioniGraficheGeneriche.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi guanti.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] == 1:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][1]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 2:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][2]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][4]) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 22:
                if dati[62] != 0:
                    FunzioniGraficheGeneriche.messaggio("Guanti vitali:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Guanti che aumentano i <*>#italic#Pv<*> massimi del portatore.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 1:
                        FunzioniGraficheGeneriche.messaggio("+" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][1]), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    if dati[129] == 2:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][2]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][4]) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 23:
                if dati[63] != 0:
                    FunzioniGraficheGeneriche.messaggio("Guanti difensivi:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Guanti che consentono di subire meno danni grazie a una presa salda dello scudo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 2:
                        FunzioniGraficheGeneriche.messaggio("+" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][2]), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    if dati[129] == 1:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][1]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][4]) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 24:
                if dati[64] != 0:
                    FunzioniGraficheGeneriche.messaggio("Guanti offensivi:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Guanti che aumentano l'attacco del portatore grazie a una presa salda dell'arma.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 3:
                        FunzioniGraficheGeneriche.messaggio("+" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        FunzioniGraficheGeneriche.messaggio("+" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                    if dati[129] == 1:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][1]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 2:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][2]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 4:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][4]) + "%", GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 25:
                if dati[65] != 0:
                    FunzioniGraficheGeneriche.messaggio("Guanti confortevoli:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Guanti che aumentano la probabilità di parare gli attacchi grazie a una presa agevole dello scudo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 4:
                        FunzioniGraficheGeneriche.messaggio("+" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][4]) + "%", GlobalHWVar.verde, posizioneStatisticheX, posizioneStatParY, grandezzaCarattereStatistiche)
                    if dati[129] == 1:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][1]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPvY, grandezzaCarattereStatistiche)
                    elif dati[129] == 2:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][2]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    elif dati[129] == 3:
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttRavY, grandezzaCarattereStatistiche)
                        FunzioniGraficheGeneriche.messaggio("-" + str(GlobalGameVar.statisticheEquipaggiamento["guanti"][3]), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatAttDistY, grandezzaCarattereStatistiche)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            # collane
            if voceMarcata == 26:
                if dati[66] != 0:
                    FunzioniGraficheGeneriche.messaggio("Niente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Rimuovi collana.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 27:
                if dati[67] != 0:
                    FunzioniGraficheGeneriche.messaggio("Collana rigenerante:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio("Collana composta da erbe il cui odore ripristina <*>#italic#Pv<*> ogni turno.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 28:
                if dati[68] != 0:
                    FunzioniGraficheGeneriche.messaggio("Collana medicinale:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Collana composta da erbe il cui odore neutralizza la tossicità del veleno (non ha effetto se si è già avvelenati).", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 29:
                if dati[69] != 0:
                    FunzioniGraficheGeneriche.messaggio("Portafortuna:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Collana che permette di ottenere più monete dai nemici.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
            if voceMarcata == 30:
                if dati[70] != 0:
                    FunzioniGraficheGeneriche.messaggio("Assorbilampo:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Collana che ti rende immune agli attacchi di Impo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)

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

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return dati, esci


def oggetti(dati, colcoInCasellaVista):
    imgProtagonista = GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgPersonaggioMenuOggetti"]

    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    sconosciutoOggetto = GlobalImgVar.sconosciutoOggettoMenu3
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
    esci = False
    usandoRod = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= dati[0] < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        usandoRod = True
    qtaOggettiDiRod = 99

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
                    if GlobalHWVar.gsx // 32 * 11 <= xMouse <= GlobalHWVar.gsx // 32 * 14.8:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalHWVar.gsx // 32 * 11.9
                        yp = GlobalHWVar.gsy // 18 * 15.25
                    elif GlobalHWVar.gsx // 32 * 14.8 <= xMouse <= GlobalHWVar.gsx // 32 * 18.5:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalHWVar.gsx // 32 * 14.8
                        yp = GlobalHWVar.gsy // 18 * 15.25
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
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            esci = True
            bottoneDown = False
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
                        if not usandoRod:
                            dati[31] -= 1
                        yp = GlobalHWVar.gsy // 18 * 6.2
                    # carica batt
                    if usa == 2:
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        if not usandoRod:
                            dati[32] -= 1
                        yp = GlobalHWVar.gsy // 18 * 7.2
                    # antidoto
                    if usa == 3:
                        dati[121] = 0
                        if not usandoRod:
                            dati[33] -= 1
                        yp = GlobalHWVar.gsy // 18 * 8.2
                    # super pozione
                    if usa == 4:
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        if not usandoRod:
                            dati[34] -= 1
                        yp = GlobalHWVar.gsy // 18 * 9.2
                    # carica migliorato
                    if usa == 5:
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        if not usandoRod:
                            dati[35] -= 1
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
                    if (usa == 2 or usa == 5) and not GlobalGameVar.impoPresente:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    else:
                        if usa == 1:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.suonoUsoPozione)
                        elif usa == 2:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.suonoUsoCaricabatterie)
                        elif usa == 3:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.suonoUsoMedicina)
                        elif usa == 4:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.suonoUsoPozione)
                        elif usa == 5:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.suonoUsoCaricabatterie)
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
                        if dati[31] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 1
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 2:
                        if (dati[32] > 0 or usandoRod) and GlobalGameVar.impoPresente and colcoInCasellaVista:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 2
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            if (not GlobalGameVar.impoPresente or not colcoInCasellaVista) and not usandoRod:
                                impossibileUsareCaricaBatt = True
                    if oggetton == 3:
                        if dati[33] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 3
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 4:
                        if dati[34] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 4
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 5:
                        if (dati[35] > 0 or usandoRod) and GlobalGameVar.impoPresente and colcoInCasellaVista:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 5
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            if (not GlobalGameVar.impoPresente or not colcoInCasellaVista) and not usandoRod:
                                impossibileUsareCaricaBatt = True
                    if oggetton == 6:
                        if dati[36] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 6
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 7:
                        if dati[37] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 7
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 8:
                        if dati[38] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 8
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 9:
                        if dati[39] > 0 or usandoRod:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                            usa = 9
                            usauno = True
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    if oggetton == 10:
                        if dati[40] > 0 or usandoRod:
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

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton or aggiornaInterfacciaPerCambioInput):
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
                    xp = GlobalHWVar.gsx // 32 * 11.9
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
                    xp = GlobalHWVar.gsx // 32 * 14.8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                FunzioniGraficheGeneriche.messaggio("Oggetti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Nome oggetto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 4.3, GlobalHWVar.gsy // 18 * 4.7, 50, centrale=True)
                FunzioniGraficheGeneriche.messaggio(u"Quantità", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 4.7, 50, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 1.5), int(GlobalHWVar.gpy * 5.6)), (int(GlobalHWVar.gpx * 10.5), int(GlobalHWVar.gpy * 5.6)), 1)
                if dati[31] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[31]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 6.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 45)
                if dati[32] >= 0:
                    if GlobalGameVar.impoPresente and colcoInCasellaVista:
                        FunzioniGraficheGeneriche.messaggio("ImpoFrutto piccolo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("ImpoFrutto piccolo", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[32]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 7.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 45)
                if dati[33] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Medicina", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[33]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 8.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 45)
                if dati[34] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Super pozione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[34]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 9.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 45)
                if dati[35] >= 0:
                    if GlobalGameVar.impoPresente and colcoInCasellaVista:
                        FunzioniGraficheGeneriche.messaggio("ImpoFrutto grande", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("ImpoFrutto grande", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[35]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 10.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 45)
                if dati[36] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Bomba", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[36]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 11.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 45)
                if dati[37] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Bomba velenosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[37]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 12.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 45)
                if dati[38] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Esca", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[38]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 13.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 45)
                if dati[39] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Bomba appiccicosa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[39]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 14.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 45)
                if dati[40] >= 0:
                    FunzioniGraficheGeneriche.messaggio("Bomba potenziata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 45)
                    if usandoRod:
                        qta = qtaOggettiDiRod
                    else:
                        qta = dati[40]
                    FunzioniGraficheGeneriche.messaggio(u"×%i" % qta, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.1, GlobalHWVar.gsy // 18 * 15.2, 45, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 45)
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
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 19.5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15.1))
                if impossibileUsareCaricaBatt:
                    if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and not colcoInCasellaVista:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4))
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 12.5))
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 15.5))
                        FunzioniGraficheGeneriche.messaggio(u"Impo è irraggiungibile!", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 14.8, GlobalHWVar.gsy // 18 * 14.2, 50, centrale=True)
                    elif dati[0] < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4))
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 12.5))
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 15.5))
                        FunzioniGraficheGeneriche.messaggio(u"Inutilizzabile...", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 14.8, GlobalHWVar.gsy // 18 * 14.2, 50, centrale=True)
                    if oggettonVecchio != oggetton:
                        impossibileUsareCaricaBatt = False
                        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14))
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14))
            if aggiornaInterfacciaPerCambioInput:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                aggiornaInterfacciaPerCambioInput = False
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            # menu conferma
            if usa != 0:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12.5, GlobalHWVar.gsx // 32 * 7.5, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 17.5, GlobalHWVar.gsy // 18 * 15.5))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalHWVar.gsx // 32 * 14.8
                    yp = GlobalHWVar.gsy // 18 * 15.25
                    voceMarcata = 2
                    usauno = False
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                FunzioniGraficheGeneriche.messaggio("Usare?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.8, GlobalHWVar.gsy // 18 * 13.1, 85, centrale=True)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 11.5, GlobalHWVar.gsy // 18 * 14.5), (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5), 2)
                FunzioniGraficheGeneriche.messaggio(u"Sì", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 12.8, GlobalHWVar.gsy // 18 * 15, 70)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 14.8) - 1, int(GlobalHWVar.gpy * 14.8)), (int(GlobalHWVar.gpx * 14.8) - 1, int(GlobalHWVar.gpy * 16.2)), 2)
                FunzioniGraficheGeneriche.messaggio("No", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 15.8, GlobalHWVar.gsy // 18 * 15, 70)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 19.5), int(GlobalHWVar.gpy * 3.5)), (int(GlobalHWVar.gpx * 19.5), int(GlobalHWVar.gpy * 17)), 2)

            grandezzaCarattereDescrizioni = 40
            posizioneXTitoli = GlobalHWVar.gsx // 32 * 21
            posizioneYTitoli = GlobalHWVar.gsy // 18 * 13.5
            posizioneXDescrizioni = GlobalHWVar.gsx // 32 * 21
            posizioneYDescrizioni = GlobalHWVar.gsy // 18 * 14.5
            larghezzaTestoDescrizioni = GlobalHWVar.gpx * 10
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            if dati[31] >= 0 and oggetton == 1:
                FunzioniGraficheGeneriche.messaggio("Pozione:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio("Recupera 100 <*>#italic#Pv.<*>", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 1:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[32] >= 0 and oggetton == 2:
                FunzioniGraficheGeneriche.messaggio("ImpoFrutto piccolo:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                    FunzioniGraficheGeneriche.messaggio("Recupera 250 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Nutrimento per una specie in via di estinzione...", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 2:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[33] >= 0 and oggetton == 3:
                FunzioniGraficheGeneriche.messaggio("Medicina:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio("Cura avvelenamento.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 3:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[34] >= 0 and oggetton == 4:
                FunzioniGraficheGeneriche.messaggio("Super pozione:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio("Recupera 300 <*>#italic#Pv.<*>", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 4:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[35] >= 0 and oggetton == 5:
                FunzioniGraficheGeneriche.messaggio("ImpoFrutto grande:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                if dati[0] >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                    FunzioniGraficheGeneriche.messaggio("Recupera 600 <*>#italic#Pe<*> di Impo.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    FunzioniGraficheGeneriche.messaggio("Nutrimento per una specie in via di estinzione...", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 5:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[36] >= 0 and oggetton == 6:
                FunzioniGraficheGeneriche.messaggio("Bomba:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio("Infligge un po' di danni ai nemici su cui viene lanciata.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 6:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[37] >= 0 and oggetton == 7:
                FunzioniGraficheGeneriche.messaggio("Bomba velenosa:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio("Infligge avvelenamento al nemico su cui viene lanciata.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 7:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[38] >= 0 and oggetton == 8:
                FunzioniGraficheGeneriche.messaggio("Esca:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio(u"Distrae i nemici finché non viene distrutta. È possibile riprenderla passandoci sopra.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 8:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[39] >= 0 and oggetton == 9:
                FunzioniGraficheGeneriche.messaggio("Bomba appiccicosa:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio(u"Dimezza la velocità del nemico su cui viene lanciata.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 9:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
            if dati[40] >= 0 and oggetton == 10:
                FunzioniGraficheGeneriche.messaggio("Bomba potenziata:", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)
                FunzioniGraficheGeneriche.messaggio("Infligge molti danni ai nemici su cui viene lanciata.", GlobalHWVar.grigiochi, posizioneXDescrizioni, posizioneYDescrizioni, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 10:
                FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneXTitoli, posizioneYTitoli, 60)

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            FunzioniGraficheGeneriche.messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 4.8, 50)
            FunzioniGraficheGeneriche.messaggio("Status alterati: ", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 5.6, 50)
            GlobalHWVar.disegnaImmagineSuSchermo(imgProtagonista, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4.5))
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 4)), (int(GlobalHWVar.gpx * 18.5), int(GlobalHWVar.gpy * 4)), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 7.5)), (int(GlobalHWVar.gpx * 18.5), int(GlobalHWVar.gpy * 7.5)), 2)
            if dati[121]:
                avvelenato = GlobalImgVar.avvelenatoMenu
                GlobalHWVar.disegnaImmagineSuSchermo(avvelenato, (GlobalHWVar.gsx // 32 * 13.9, GlobalHWVar.gsy // 18 * 6.3))
            if dati[123] > 0:
                attaccopiu = GlobalImgVar.attaccopiuMenu
                GlobalHWVar.disegnaImmagineSuSchermo(attaccopiu, ((GlobalHWVar.gsx // 32 * 13.9) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 6.3))
            if dati[124] > 0:
                difesapiu = GlobalImgVar.difesapiuMenu
                GlobalHWVar.disegnaImmagineSuSchermo(difesapiu, ((GlobalHWVar.gsx // 32 * 13.9) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 6.3))
            # vita-status robo
            if GlobalGameVar.impoPresente:
                if dati[10] < 0:
                    dati[10] = 0
                FunzioniGraficheGeneriche.messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 8.3, 50)
                FunzioniGraficheGeneriche.messaggio("Status alterati: ", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 14.1, GlobalHWVar.gsy // 18 * 9.1, 50)
                robomen = GlobalImgVar.roboo2
                GlobalHWVar.disegnaImmagineSuSchermo(robomen, (GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8))
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (int(GlobalHWVar.gpx * 11), int(GlobalHWVar.gpy * 11)), (int(GlobalHWVar.gpx * 18.5), int(GlobalHWVar.gpy * 11)), 2)
                if dati[122] > 0:
                    surriscaldato = GlobalImgVar.surriscaldatoMenu
                    GlobalHWVar.disegnaImmagineSuSchermo(surriscaldato, (GlobalHWVar.gsx // 32 * 13.9, GlobalHWVar.gsy // 18 * 9.8))
                if dati[125] > 0:
                    velocitapiu = GlobalImgVar.velocitapiuMenu
                    GlobalHWVar.disegnaImmagineSuSchermo(velocitapiu, ((GlobalHWVar.gsx // 32 * 13.9) + (2 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 9.8))
                if dati[126] > 0:
                    efficienzapiu = GlobalImgVar.efficienzapiuMenu
                    GlobalHWVar.disegnaImmagineSuSchermo(efficienzapiu, ((GlobalHWVar.gsx // 32 * 13.9) + (4 * GlobalHWVar.gpx // 4 * 3), GlobalHWVar.gsy // 18 * 9.8))

            if attacco != 0:
                risposta = True

            GlobalHWVar.disegnaImmagineSuSchermo(imgOggetti[oggetton - 1], (GlobalHWVar.gsx // 32 * 20.7, GlobalHWVar.gsy // 18 * 2.5))
            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if usa == 0:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 0.5))), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), (xp + (int(GlobalHWVar.gpx * 6.4)), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 6.8))), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), (xp + (int(GlobalHWVar.gpx * 9.5)), yp + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
            else:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 0.5))), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), (xpv + (int(GlobalHWVar.gpx * 6.4)), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xpv + (int(GlobalHWVar.gpx * 6.8))), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), (xpv + (int(GlobalHWVar.gpx * 9.5)), ypv + (int(GlobalHWVar.gpy * 0.7)) - 1), 2)
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return dati, attacco, esci
