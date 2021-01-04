# -*- coding: utf-8 -*-

from SottoMenuB import *


def equip(dati):
    perssta = GlobalVar.perso
    persstab = GlobalVar.persob
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    sfondoOggetto = GlobalVar.sfondoOggettoMenu
    sconosciutoEquip = GlobalVar.sconosciutoEquipMenu
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 6.8
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    spada = GlobalVar.vetImgSpadePixellate[dati[6]]
    arco = GlobalVar.vetImgArchiPixellate[dati[128]]
    scudo = GlobalVar.vetImgScudiPixellate[dati[7]]
    armatura = GlobalVar.vetImgArmaturePixellate[dati[8]]
    guanti = GlobalVar.vetImgGuantiPixellate[dati[129]]
    collana = GlobalVar.vetImgCollanePixellate[dati[130]]
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
            vetImgSpade.append(GlobalVar.vetImgSpadeMenu[i])
        else:
            vetImgSpade.append(sconosciutoEquip)
        if dati[46 + i] > 0:
            vetImgArchi.append(GlobalVar.vetImgArchiMenu[i])
        else:
            vetImgArchi.append(sconosciutoEquip)
        if dati[51 + i] > 0:
            vetImgArmature.append(GlobalVar.vetImgArmatureMenu[i])
        else:
            vetImgArmature.append(sconosciutoEquip)
        if dati[56 + i] > 0:
            vetImgScudi.append(GlobalVar.vetImgScudiMenu[i])
        else:
            vetImgScudi.append(sconosciutoEquip)
        if dati[61 + i] > 0:
            vetImgGuanti.append(GlobalVar.vetImgGuantiMenu[i])
        else:
            vetImgGuanti.append(sconosciutoEquip)
        if dati[66 + i] > 0:
            vetImgCollane.append(GlobalVar.vetImgCollaneMenu[i])
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
        if GlobalVar.mouseVisibile:
            if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 4.5:
                if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 4.5 <= xMouse <= GlobalVar.gsx // 32 * 8:
                if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 4.5
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 4.5
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 4.5
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVar.gsx // 32 * 4.5
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVar.gsx // 32 * 4.5
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 8 <= xMouse <= GlobalVar.gsx // 32 * 11.5:
                if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 11.5 <= xMouse <= GlobalVar.gsx // 32 * 15:
                if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVar.gsx // 32 * 11.5
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVar.gsx // 32 * 11.5
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVar.gsx // 32 * 11.5
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVar.gsx // 32 * 11.5
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVar.gsx // 32 * 11.5
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 15 <= xMouse <= GlobalVar.gsx // 32 * 18.5:
                if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 21
                    xp = GlobalVar.gsx // 32 * 15
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 22
                    xp = GlobalVar.gsx // 32 * 15
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 23
                    xp = GlobalVar.gsx // 32 * 15
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 24
                    xp = GlobalVar.gsx // 32 * 15
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 25
                    xp = GlobalVar.gsx // 32 * 15
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 18.5 <= xMouse <= GlobalVar.gsx // 32 * 22:
                if GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 26
                    xp = GlobalVar.gsx // 32 * 18.5
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 27
                    xp = GlobalVar.gsx // 32 * 18.5
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 28
                    xp = GlobalVar.gsx // 32 * 18.5
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 29
                    xp = GlobalVar.gsx // 32 * 18.5
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 30
                    xp = GlobalVar.gsx // 32 * 18.5
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if not GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                risposta = True
            else:
                carim = True
                # progresso-stanza-x-y-liv-pv-spada-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                # spade
                if voceMarcata == 1:
                    if dati[41] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[6] = 0
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 2:
                    if dati[42] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[6] = 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 3:
                    if dati[43] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[6] = 2
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 4:
                    if dati[44] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[6] = 3
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 5:
                    if dati[45] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[6] = 4
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                # archi
                if voceMarcata == 6:
                    if dati[46] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[128] = 0
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 7:
                    if dati[47] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[128] = 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 8:
                    if dati[48] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[128] = 2
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 9:
                    if dati[49] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[128] = 3
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 10:
                    if dati[50] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[128] = 4
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                # armature
                if voceMarcata == 11:
                    if dati[51] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[8] = 0
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 12:
                    if dati[52] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[8] = 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 13:
                    if dati[53] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[8] = 2
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 14:
                    if dati[54] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[8] = 3
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 15:
                    if dati[55] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[8] = 4
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                # scudi
                if voceMarcata == 16:
                    if dati[56] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[7] = 0
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 17:
                    if dati[57] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[7] = 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 18:
                    if dati[58] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[7] = 2
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 19:
                    if dati[59] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[7] = 3
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 20:
                    if dati[60] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[7] = 4
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                # guanti
                if voceMarcata == 21:
                    if dati[61] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[129] = 0
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 22:
                    if dati[62] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[129] = 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 23:
                    if dati[63] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[129] = 2
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 24:
                    if dati[64] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[129] = 3
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 25:
                    if dati[65] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[129] = 4
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                # collane
                if voceMarcata == 26:
                    if dati[66] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[130] = 0
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 27:
                    if dati[67] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[130] = 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 28:
                    if dati[68] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[130] = 2
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 29:
                    if dati[69] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[130] = 3
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                if voceMarcata == 30:
                    if dati[70] != 0:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        dati[130] = 4
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 5 or voceMarcata == 10 or voceMarcata == 15 or voceMarcata == 20 or voceMarcata == 25 or voceMarcata == 30:
                    voceMarcata -= 4
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 6.8
                else:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    yp += GlobalVar.gsy // 18 * 2
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 6 or voceMarcata == 11 or voceMarcata == 16 or voceMarcata == 21 or voceMarcata == 26:
                    voceMarcata += 4
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    yp = GlobalVar.gsy // 18 * 14.8
                else:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    yp = yp - GlobalVar.gsy // 18 * 2
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 26 or voceMarcata == 27 or voceMarcata == 28 or voceMarcata == 29 or voceMarcata == 30:
                    voceMarcata -= 25
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 1
                else:
                    voceMarcata += 5
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    xp = xp + GlobalVar.gsx // 32 * 3.5
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5:
                    voceMarcata += 25
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 18.5
                else:
                    voceMarcata -= 5
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    xp = xp - GlobalVar.gsx // 32 * 3.5
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))

                messaggio("Equipaggiamento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                messaggio("Armi", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 4.5, 65, centrale=True)
                messaggio("Protezioni", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 4.5, 65, centrale=True)
                messaggio("Accessori", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 4.5, 65, centrale=True)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 1.5), int(GlobalVar.gpy * 5.6)), (int(GlobalVar.gpx * 21.5), int(GlobalVar.gpy * 5.6)), 1)
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 1.7, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetImgSpade[i], (GlobalVar.gsx // 32 * 1.7, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 5.2, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetImgArchi[i], (GlobalVar.gsx // 32 * 5.2, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 8.7, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetImgArmature[i], (GlobalVar.gsx // 32 * 8.7, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 12.2, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetImgScudi[i], (GlobalVar.gsx // 32 * 12.2, int((GlobalVar.gsy // 18 * 6) + (GlobalVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 15.7, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetImgGuanti[i], (GlobalVar.gsx // 32 * 15.7, int((GlobalVar.gsy // 18 * 6) + (GlobalVar.gpy * 2 * i))))
                    i += 1
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 19.2, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetImgCollane[i], (GlobalVar.gsx // 32 * 19.2, ((GlobalVar.gsy // 18 * 6) + (GlobalVar.gpy * 2 * i))))
                    i += 1
            else:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 3, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 14))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                elif GlobalVar.usandoIlController:
                    messaggio("Cerchio: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)

            if carim:
                spada = GlobalVar.vetImgSpadePixellate[dati[6]]
                arco = GlobalVar.vetImgArchiPixellate[dati[128]]
                scudo = GlobalVar.vetImgScudiPixellate[dati[7]]
                armatura = GlobalVar.vetImgArmaturePixellate[dati[8]]
                guanti = GlobalVar.vetImgGuantiPixellate[dati[129]]
                collana = GlobalVar.vetImgCollanePixellate[dati[130]]
                carim = False

            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 4.5) - 1, (GlobalVar.gsy // 18 * 6.1) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 4.5) - 1, (GlobalVar.gsy // 18 * 15) + (GlobalVar.gpy // 2)), 1)
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 8) - 1, (GlobalVar.gsy // 18 * 3.8) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 8) - 1, (GlobalVar.gsy // 18 * 4.9) + (GlobalVar.gpy // 2)), 2)
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 8) - 1, (GlobalVar.gsy // 18 * 5.3) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 8) - 1, (GlobalVar.gsy // 18 * 15.5) + (GlobalVar.gpy // 2)), 2)
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 11.5) - 1, (GlobalVar.gsy // 18 * 6.1) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 11.5) - 1, (GlobalVar.gsy // 18 * 15) + (GlobalVar.gpy // 2)), 1)
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 15) - 1, (GlobalVar.gsy // 18 * 3.8) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 15) - 1, (GlobalVar.gsy // 18 * 4.9) + (GlobalVar.gpy // 2)), 2)
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 15) - 1, (GlobalVar.gsy // 18 * 5.3) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 15) - 1, (GlobalVar.gsy // 18 * 15.5) + (GlobalVar.gpy // 2)), 2)
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((GlobalVar.gsx // 32 * 18.5) - 1, (GlobalVar.gsy // 18 * 6.1) + (GlobalVar.gpy // 2)), ((GlobalVar.gsx // 32 * 18.5) - 1, (GlobalVar.gsy // 18 * 15) + (GlobalVar.gpy // 2)), 1)

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati, inMenu=True)
            if dati[5] > pvtot:
                dati[5] = pvtot

            GlobalVar.disegnaImmagineSuSchermo(arco, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(perssta, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(persstab, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(armatura, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(collana, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(spada, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(guanti, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaImmagineSuSchermo(scudo, (GlobalVar.gsx // 32 * 24.5, GlobalVar.gsy // 18 * 11.3))
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (int(GlobalVar.gpx * 24.5), int(GlobalVar.gpy * 16.3)), (int(GlobalVar.gpx * 29.5), int(GlobalVar.gpy * 16.3)), 2)
            messaggio("Statistiche:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 6.7, 50)
            messaggio("Punti vita: %i" % pvtot, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7.5, 35)
            messaggio("Attacco ravvicinato: %i" % attVicino, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 8, 35)
            messaggio("Attacco a distanza: %i" % attLontano, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 8.5, 35)
            messaggio("Difesa: %i" % dif, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 9, 35)
            messaggio(u"Probabilità parata: %i" % par + "%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 9.5, 35)
            # confronto statistiche
            larghezzaTestoDescrizioni = GlobalVar.gpx * 8
            spazioTraLeRigheTestoDescrizione = GlobalVar.gpy // 2
            # spade
            if voceMarcata == 1:
                if dati[41] != 0:
                    messaggio("Niente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi spada", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 0 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 0:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 2:
                if dati[42] != 0:
                    messaggio("Spada di ferro:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Semplice spada di ferro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 10 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 1:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                    elif dati[6] < 1:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 3:
                if dati[43] != 0:
                    messaggio("Spadone d'acciaio:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Grande spadone in acciaio con ornamenti in oro. Rappresenta il modello di spada migliore mai prodotto dall'uomo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 40 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 2:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                    elif dati[6] < 2:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 4:
                if dati[44] != 0:
                    messaggio("Lykother:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Spada molto leggera e affilata. Si dice che in origine fosse un dente di un lupo enorme", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 90 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 3:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                    elif dati[6] < 3:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 5:
                if dati[45] != 0:
                    messaggio("Mendaxritas:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Potentissima spada composta da materiali ignoti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 160 - ((dati[6] * dati[6]) * 10)
                    if dati[6] > 4:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                    elif dati[6] < 4:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            # archi
            if voceMarcata == 6:
                if dati[46] != 0:
                    messaggio("Niente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi arco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 0 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 0:
                        messaggio(str(diffAtt), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 7:
                if dati[47] != 0:
                    messaggio("Arco di legno:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Semplice arco in legno usato dalla maggior parte dei forestieri", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 10 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 1:
                        messaggio(str(diffAtt), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[128] < 1:
                        messaggio("+" + str(diffAtt), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 8:
                if dati[48] != 0:
                    messaggio("Arco di ferro:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Elaborato arco in ferro usato solo dai più esperti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 40 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 2:
                        messaggio(str(diffAtt), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[128] < 2:
                        messaggio("+" + str(diffAtt), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 9:
                if dati[49] != 0:
                    messaggio("Arco di precisione:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Sofisticato arco in legno e acciaio. Molto leggero e potente. Massima espressione dell'ingegno umano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 90 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 3:
                        messaggio(str(diffAtt), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[128] < 3:
                        messaggio("+" + str(diffAtt), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 10:
                if dati[50] != 0:
                    messaggio("Accipiter:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Potentissimo arco di origine sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diffAtt = 160 - ((dati[128] * dati[128]) * 10)
                    if dati[128] > 4:
                        messaggio(str(diffAtt), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[128] < 4:
                        messaggio("+" + str(diffAtt), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            # armature
            if voceMarcata == 11:
                if dati[51] != 0:
                    messaggio("Niente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi armatura", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 0 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 0:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 12:
                if dati[52] != 0:
                    messaggio("Armatura di pelle:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Semplice armatura in pelle", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 10 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 1:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[8] < 1:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 13:
                if dati[53] != 0:
                    messaggio("Armatura d'acciaio:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Grande armatura d'acciaio con ornamenti in oro. Usata solo dagli ufficiali dell'esercito", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 40 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 2:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[8] < 2:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 14:
                if dati[54] != 0:
                    messaggio("Lykodes:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Armatura formata da materiali leggieri e resistenti. Si dice essere composta da ossa di un enorme lupo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 90 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 3:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[8] < 3:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 15:
                if dati[55] != 0:
                    messaggio("Loriquam:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Armatura incredibilmente resistente. La sua origine è ignota", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 160 - ((dati[8] * dati[8]) * 10)
                    if dati[8] > 4:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[8] < 4:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            # scudi
            if voceMarcata == 16:
                if dati[56] != 0:
                    messaggio("Niente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi scudo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 0 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 0:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    diff = 0 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 0:
                        messaggio(str(diff) + "%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 17:
                if dati[57] != 0:
                    messaggio("Scudo di pelle:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Semplice scudo in pelle", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 5 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 1:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    diff = 3 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 1:
                        messaggio(str(diff) + "%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff) + "%", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 18:
                if dati[58] != 0:
                    messaggio("Scudo d'acciaio:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Sofisticato scudo in acciaio e oro. Studiato per respingere gli attacchi più pesanti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 20 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 2:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    diff = 12 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 2:
                        messaggio(str(diff) + "%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff) + "%", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 19:
                if dati[59] != 0:
                    messaggio("Lykethmos:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Scudo molto leggere e resistente. Si dice essere composto dalle ossa più resistenti di un enorme lupo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 45 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 3:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    diff = 27 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 3:
                        messaggio(str(diff) + "%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff) + "%", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 20:
                if dati[60] != 0:
                    messaggio("Clipequam:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Scudo incredibilmente resistente. Non è nota l'origine", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    diff = 80 - ((dati[7] * dati[7]) * 5)
                    if dati[7] > 4:
                        messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    diff = 48 - ((dati[7] * dati[7]) * 3)
                    if dati[7] > 4:
                        messaggio(str(diff) + "%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff) + "%", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            # guanti
            if voceMarcata == 21:
                if dati[61] != 0:
                    messaggio("Niente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi guanti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 22:
                if dati[62] != 0:
                    messaggio("Guanti vitali:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che aumentano i punti vita massimi del portatore", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 1:
                        messaggio("+50", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7.5, 35)
                    if dati[129] == 2:
                        messaggio("-30", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 23:
                if dati[63] != 0:
                    messaggio("Guanti difensivi:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che consentono di subire meno danno grazie ad una presa salda dello scudo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 2:
                        messaggio("+30", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7.5, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 24:
                if dati[64] != 0:
                    messaggio("Guanti offensivi:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Guanti che aumentano l'attacco del portatore grazie ad una presa salda dell'arma", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 3:
                        messaggio("+20", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                        messaggio("+20", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[129] == 4:
                        messaggio("-10%", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 25:
                if dati[65] != 0:
                    messaggio("Guanti confortevoli:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Guanti che aumentano la probabilità di parare gli attacchi grazie ad una presa agevole dello scudo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if dati[129] != 4:
                        messaggio("+10%", GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9.5, 35)
                    if dati[129] == 1:
                        messaggio("-50", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 7.5, 35)
                    elif dati[129] == 2:
                        messaggio("-30", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    elif dati[129] == 3:
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8, 35)
                        messaggio("-20", GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            # collane
            if voceMarcata == 26:
                if dati[66] != 0:
                    messaggio("Niente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Rimuovi collana", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 27:
                if dati[67] != 0:
                    messaggio("Collana rigenerante:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio("Collana composta da erbe il cui odore ripristina punti vita ogni turno", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 28:
                if dati[68] != 0:
                    messaggio("Collana medicinale:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana composta da erbe il cui odore neutralizza la tissicità del veleno (non ha effetto se si è già avvelenati)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 29:
                if dati[69] != 0:
                    messaggio("Apprendimaschera:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che consente di ricevere più punti esperienza", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
            if voceMarcata == 30:
                if dati[70] != 0:
                    messaggio("Portafortuna:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)
                    messaggio(u"Collana che permette di ottenere più monete dai nemici", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 3.8, 60)

            # puntatore vecchio
            if dati[6] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 6.8))
            if dati[6] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 8.8))
            if dati[6] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 10.8))
            if dati[6] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 12.8))
            if dati[6] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 14.8))
            if dati[128] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 6.8))
            if dati[128] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 8.8))
            if dati[128] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 10.8))
            if dati[128] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 12.8))
            if dati[128] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 4.5, GlobalVar.gsy // 18 * 14.8))
            if dati[8] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 6.8))
            if dati[8] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 8.8))
            if dati[8] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 10.8))
            if dati[8] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 12.8))
            if dati[8] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 14.8))
            if dati[7] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 6.8))
            if dati[7] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 8.8))
            if dati[7] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 10.8))
            if dati[7] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 12.8))
            if dati[7] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 11.5, GlobalVar.gsy // 18 * 14.8))
            if dati[129] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 6.8))
            if dati[129] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 8.8))
            if dati[129] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 10.8))
            if dati[129] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 12.8))
            if dati[129] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 14.8))
            if dati[130] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 6.8))
            if dati[130] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 8.8))
            if dati[130] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 10.8))
            if dati[130] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 12.8))
            if dati[130] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 18.5, GlobalVar.gsy // 18 * 14.8))

            GlobalVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
    return dati


def sceglicondiz(dati, condizione):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    condSconosciuta = GlobalVar.imgGambitSconosciuta
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico le scenette
    scecond = GlobalVar.vetImgCondizioniMenu

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalVar.mouseVisibile:
            if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 8:
                if GlobalVar.gsy // 18 * 4.4 <= yMouse <= GlobalVar.gsy // 18 * 5.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 0
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 4.6
                elif GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.1
                elif GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 7.1
                elif GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8.1
                elif GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 9.1
                elif GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 10.1
                elif GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 11.1
                elif GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 12.1
                elif GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 13.1
                elif GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 14.1
                elif GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 15.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 15.1
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 8 <= xMouse <= GlobalVar.gsx // 32 * 16:
                if GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 6.1
                elif GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 7.1
                elif GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 8.1
                elif GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 9.1
                elif GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 10.1
                elif GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 11.1
                elif GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 12.1
                elif GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 13.1
                elif GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 14.1
                elif GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 15.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 15.1
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if not GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                risposta = True
            else:
                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
                i = 81
                c = 1
                while i <= 100:
                    if voceMarcata == c:
                        if dati[i] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            return c
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    i += 1
                    c += 1
                if voceMarcata == 0:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                    return 0
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = yp - GlobalVar.gsy // 18 * 1.5
                        xp = GlobalVar.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 15.1
                else:
                    if voceMarcata != 0:
                        voceMarcata -= 1
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = yp - GlobalVar.gsy // 18 * 1
                    else:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 15.1
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = xp - GlobalVar.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 8
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    yp = yp + GlobalVar.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 4.6
                            xp = GlobalVar.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = yp + GlobalVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = xp + GlobalVar.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 1
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
                messaggio("Scegli condizione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                messaggio("Cancella settaggio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4.7, 45)
                if dati[81] > 0:
                    messaggio("Lucy con pv < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.2, 40)
                if dati[82] > 0:
                    messaggio("Lucy con pv < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 40)
                if dati[83] > 0:
                    messaggio("Lucy con pv < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.2, 40)
                if dati[84] > 0:
                    messaggio("Lucy con veleno", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.2, 40)
                if dati[85] > 0:
                    messaggio("Impo surriscaldato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 40)
                if dati[86] > 0:
                    messaggio("Impo con pe < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.2, 40)
                if dati[87] > 0:
                    messaggio("Impo con pe < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.2, 40)
                if dati[88] > 0:
                    messaggio("Impo con pe < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.2, 40)
                if dati[89] > 0:
                    messaggio("Sempre a Lucy", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.2, 40)
                if dati[90] > 0:
                    messaggio("Sempre a Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.2, 40)
                if dati[91] > 0:
                    messaggio("Nemico a caso", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 6.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 6.2, 40)
                if dati[92] > 0:
                    messaggio("Nemico vicino", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 7.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 7.2, 40)
                if dati[93] > 0:
                    messaggio("Nemico lontano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8.2, 40)
                if dati[94] > 0:
                    messaggio("Nemico con pv < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9.2, 40)
                if dati[95] > 0:
                    messaggio("Nemico con pv < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 10.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 10.2, 40)
                if dati[96] > 0:
                    messaggio("Nemico con pv < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11.2, 40)
                if dati[97] > 0:
                    messaggio("Nemico con meno pv", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.2, 40)
                if dati[98] > 0:
                    messaggio("Numero di nemici > 1", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13.2, 40)
                if dati[99] > 0:
                    messaggio("Numero di nemici > 4", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 14.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 14.2, 40)
                if dati[100] > 0:
                    messaggio("Numero di nemici > 7", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15.2, 40)
            elif voceMarcataVecchia != voceMarcata:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 11.5))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 4.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 11.5))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 16.5, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 13))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                elif GlobalVar.usandoIlController:
                    messaggio("Cerchio: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)

            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 8) - 1, int(GlobalVar.gpy * 5.7)), (int(GlobalVar.gpx * 8) - 1, int(GlobalVar.gpy * 16)), 2)

            larghezzaTestoDescrizioni = GlobalVar.gpx * 13
            spazioTraLeRigheTestoDescrizione = GlobalVar.gpy // 2
            if voceMarcata == 0:
                GlobalVar.disegnaImmagineSuSchermo(scecond[0], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                messaggio("Cancella settaggio:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if voceMarcata == 1:
                if dati[81] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[1], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Lucy con pv < 80%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Lucy se la vede e ha pv < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 2:
                if dati[82] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[2], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Lucy con pv < 50%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Lucy se la vede e ha pv < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 3:
                if dati[83] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[3], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Lucy con pv < 30%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Lucy se la vede e ha pv < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 4:
                if dati[84] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[4], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Lucy con veleno:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Lucy se la vede ed è avvelenata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 5:
                if dati[85] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[5], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Impo surriscaldato:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Impo quando è surriscaldato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 6:
                if dati[86] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[6], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Impo con pe < 80%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Impo quando ha pe < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 7:
                if dati[87] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[7], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Impo con pe < 50%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Impo quando ha pe < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 8:
                if dati[88] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[8], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Impo con pe < 30%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su Impo quando ha pe < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 9:
                if dati[89] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[9], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sempre a Lucy:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Lucy in continuazione quando la vede (se la tecnica associata comporta un'alterazione di stato, viene eseguita solo se lo status non è attivo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 10:
                if dati[90] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[10], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sempre a Impo:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su Impo in continuazione (se la tecnica associata comporta un'alterazione di stato, viene eseguita solo se lo status non è attivo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 11:
                if dati[91] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[11], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico a caso:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Esegue l'azione su un nemico a caso", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 12:
                if dati[92] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[12], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico vicino:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico più vicino nel raggio di 2 caselle", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 13:
                if dati[93] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[13], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico lontano:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico lontano (distante di 3 o più caselle) più vicino", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 14:
                if dati[94] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[14], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico con pv < 80%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su un nemico con pv < 80% (in caso di molteplici bersagli, esegue l'azione su quello più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 15:
                if dati[95] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[15], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico con pv < 50%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su un nemico con pv < 50% (in caso di molteplici bersagli, esegue l'azione su quello più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 16:
                if dati[96] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[16], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico con pv < 30%:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione su un nemico con pv < 30% (in caso di molteplici bersagli, esegue l'azione su quello più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 17:
                if dati[97] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[17], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Nemico con meno pv:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione sul nemico con meno pv (in caso di molteplici bersagli, esegue l'azione su quello più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 18:
                if dati[98] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[18], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Numero di nemici > 1:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 19:
                if dati[99] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[19], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Numero di nemici > 4:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 4 nemici (in caso di tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 20:
                if dati[100] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scecond[20], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Numero di nemici > 7:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 7 nemici (in caso di tecnica a bersaglio singolo, questa viene eseguita sul nemico più vicino)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if condizione == i:
                    GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            i = 11
            k = 6.1
            while i <= 20:
                if condizione == i:
                    GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            if condizione == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.6))
            GlobalVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
    return condizione


def sceglitecn(dati, tecnica):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    condSconosciuta = GlobalVar.imgGambitSconosciuta
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 4.6
    risposta = False
    voceMarcata = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico le scenette
    scetecn = GlobalVar.vetImgTecnicheMenu

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalVar.mouseVisibile:
            if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                if GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 8:
                if GlobalVar.gsy // 18 * 4.4 <= yMouse <= GlobalVar.gsy // 18 * 5.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 0
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 4.6
                elif GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.1
                elif GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 7.1
                elif GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8.1
                elif GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 9.1
                elif GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 10.1
                elif GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 11.1
                elif GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 12.1
                elif GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 13.1
                elif GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 14.1
                elif GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 15.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 15.1
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif GlobalVar.gsx // 32 * 8 <= xMouse <= GlobalVar.gsx // 32 * 16:
                if GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 6.1
                elif GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 7.1
                elif GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 8.1
                elif GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 9.1
                elif GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 10.1
                elif GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 11.1
                elif GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 12.1
                elif GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 13.1
                elif GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 14.1
                elif GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 15.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVar.gsx // 32 * 8
                    yp = GlobalVar.gsy // 18 * 15.1
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if not GlobalVar.mouseBloccato:
                    GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
            risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                risposta = True
            else:
                i = 11
                c = 1
                while i <= 30:
                    if voceMarcata == c:
                        if dati[i] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            tecnica = c
                            risposta = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                        break
                    i += 1
                    c += 1
                if voceMarcata == 0:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                    tecnica = 0
                    risposta = True
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = yp - GlobalVar.gsy // 18 * 1.5
                        xp = GlobalVar.gsx // 32 * 1
                    else:
                        voceMarcata += 9
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 15.1
                else:
                    if voceMarcata == 0:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 15.1
                    else:
                        voceMarcata -= 1
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = yp - GlobalVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 11 <= voceMarcata <= 20:
                        voceMarcata -= 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = xp - GlobalVar.gsx // 32 * 7
                    else:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 8
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    yp = yp + GlobalVar.gsy // 18 * 1.5
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 4.6
                            xp = GlobalVar.gsx // 32 * 1
                        else:
                            voceMarcata -= 9
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 6.1
                    else:
                        voceMarcata += 1
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = yp + GlobalVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata != 0:
                    if 1 <= voceMarcata <= 10:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = xp + GlobalVar.gsx // 32 * 7
                    else:
                        voceMarcata -= 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 1
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.grigioscu)
                # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
                messaggio("Scegli tecnica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                messaggio("Cancella settaggio", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4.7, 45)
                if dati[11] > 0:
                    messaggio("Scossa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.2, 40)
                if dati[12] > 0:
                    messaggio("Cura", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 40)
                if dati[13] > 0:
                    messaggio("Antidoto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.2, 40)
                if dati[14] > 0:
                    messaggio("Freccia elettrica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.2, 40)
                if dati[15] > 0:
                    messaggio("Tempesta elettrica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 40)
                if dati[16] > 0:
                    messaggio("Raffreddamento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.2, 40)
                if dati[17] > 0:
                    messaggio("Auto-ricarica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.2, 40)
                if dati[18] > 0:
                    messaggio("Cura +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.2, 40)
                if dati[19] > 0:
                    messaggio("Scossa +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.2, 40)
                if dati[20] > 0:
                    messaggio("Freccia elettrica +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.2, 40)
                if dati[21] > 0:
                    messaggio("Velocizza", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 6.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 6.2, 40)
                if dati[22] > 0:
                    messaggio("Carica attacco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 7.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 7.2, 40)
                if dati[23] > 0:
                    messaggio("Carica difesa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8.2, 40)
                if dati[24] > 0:
                    messaggio("Efficienza", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 9.2, 40)
                if dati[25] > 0:
                    messaggio("Tempesta elettrica +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 10.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 10.2, 40)
                if dati[26] > 0:
                    messaggio("Cura ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 11.2, 40)
                if dati[27] > 0:
                    messaggio("Auto-ricarica +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12.2, 40)
                if dati[28] > 0:
                    messaggio("Scossa ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13.2, 40)
                if dati[29] > 0:
                    messaggio("Freccia Elettrica ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 14.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 14.2, 40)
                if dati[30] > 0:
                    messaggio("Tempesta elettrica ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15.2, 40)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 15, 40)
            else:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 11.5))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 4.5, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 11.5))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 16.5, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 13))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                elif GlobalVar.usandoIlController:
                    messaggio("Cerchio: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)

            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 8) - 1, int(GlobalVar.gpy * 5.7)), (int(GlobalVar.gpx * 8) - 1, int(GlobalVar.gpy * 16)), 2)

            larghezzaTestoDescrizioni = GlobalVar.gpx * 13
            spazioTraLeRigheTestoDescrizione = GlobalVar.gpy // 2
            if voceMarcata == 0:
                GlobalVar.disegnaImmagineSuSchermo(scetecn[0], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                messaggio("Cancella settaggio:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Cancella il settaggio di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if voceMarcata == 1:
                if dati[11] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[1], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Scossa:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[0]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a un nemico vicino", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 2:
                if dati[12] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[2], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Cura:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[1]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Recupera un po' di pv di Lucy", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 3:
                if dati[13] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[3], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Antidoto:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[2]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Cura avvelenamento a Lucy", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 4:
                if dati[14] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[4], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Freccia elettrica:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[3]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a distanza a un nemico", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 5:
                if dati[15] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[5], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Tempesta elettrica:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[4]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 6:
                if dati[16] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[6], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Raffreddamento:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[5]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre su Impo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 7:
                if dati[17] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[7], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Auto-ricarica:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[6]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Ricarica un po' Impo ma richiede due turni e provoca surriscaldamento (applicata sempre su Impo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 8:
                if dati[18] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[8], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Cura +:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[7]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Recupera molti pv di Lucy", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 9:
                if dati[19] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[9], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Scossa +:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[8]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a un nemico vicino", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 10:
                if dati[20] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[10], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Freccia elettrica +:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[9]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a distanza a un nemico", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 11:
                if dati[21] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[11], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Velocizza:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[10]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Permette a Impo, se non surriscaldato, di eseguire due azioni al turno. Provoca surriscaldamento dopo 15 turni dall'esecuzione (applicata sempre su Impo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 12:
                if dati[22] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[12], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Carica attacco:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[11]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Incrementa l'attacco di Lucy per 10 turni (non ha effetto sui nemici)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 13:
                if dati[23] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[13], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Carica difesa:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[12]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Incrementa la difesa di Lucy per 10 turni (non ha effetto sui nemici)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 14:
                if dati[24] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[14], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Efficienza:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[13]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio(u"Tutte le tecniche costano la metà dei pe per 15 turni. Si annulla con surriscaldamento (applicata sempre su Impo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 15:
                if dati[25] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[15], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Tempesta elettrica +:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[14]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 16:
                if dati[26] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[16], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Cura ++:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[15]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio(u"Recupera un enorme quantità dei pv di Lucy", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 17:
                if dati[27] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[17], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Auto-ricarica +:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[16]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Ricarica di molto Impo ma richiede due turni e provoca surriscaldamento (applicata sempre su Impo)", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 18:
                if dati[28] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[18], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Scossa ++:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[17]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a un nemico vicino", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 19:
                if dati[29] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[19], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Freccia Elettrica ++:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[18]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a distanza a un nemico", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 20:
                if dati[30] > 0:
                    GlobalVar.disegnaImmagineSuSchermo(scetecn[20], (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Tempesta elettrica ++:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)
                    messaggio("Costo Pe: " + str(GlobalVar.costoTecniche[19]), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 27.5, GlobalVar.gsy // 18 * 13.8, 45)
                    messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 4))
                    messaggio("Sconosciuta", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13.5, 60)

            # puntatore vecchio
            i = 1
            k = 6.1
            while i <= 10:
                if tecnica == i:
                    GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            i = 11
            k = 6.1
            while i <= 20:
                if tecnica == i:
                    GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * k))
                    break
                i += 1
                k += 1
            if tecnica == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4.6))
            GlobalVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
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
    robosta = GlobalVar.roboo1
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    sfondoOggetto = GlobalVar.sfondoOggettoMenu
    sconosciutoEquip = GlobalVar.sconosciutoEquipMenu
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 6.8
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

    vetImgBatterie = GlobalVar.vetImgBatterieMenu

    vetIcoBatterie = []
    i = 0
    while i < 5:
        if dati[71 + i] > 0:
            vetIcoBatterie.append(GlobalVar.vetIcoBatterieMenu[i])
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
        if GlobalVar.mouseVisibile:
            if not riordinamento:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 6 and GlobalVar.gsy // 18 * 6 <= yMouse <= GlobalVar.gsy // 18 * 8:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 6.8
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 6 and GlobalVar.gsy // 18 * 8 <= yMouse <= GlobalVar.gsy // 18 * 10:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 8.8
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 6 and GlobalVar.gsy // 18 * 10 <= yMouse <= GlobalVar.gsy // 18 * 12:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 10.8
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 6 and GlobalVar.gsy // 18 * 12 <= yMouse <= GlobalVar.gsy // 18 * 14:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 12.8
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 6 and GlobalVar.gsy // 18 * 14 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalVar.gsx // 32 * 1
                    yp = GlobalVar.gsy // 18 * 14.8
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 6.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 7.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 8.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 9.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 10.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 11.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 12.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 13.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 14.2
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 10.8 and GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 15.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 16
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 6.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 17
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 7.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 18
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 8.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 19
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 9.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 20
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 10.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 21
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 11.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 22
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 12.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 23
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 13.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 24
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 14.2
                elif GlobalVar.gsx // 32 * 10.8 <= xMouse <= GlobalVar.gsx // 32 * 17 and GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 25
                    xp = GlobalVar.gsx // 32 * 10.8
                    yp = GlobalVar.gsy // 18 * 15.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 26
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 6.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 27
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 7.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 28
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 8.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 29
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 9.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 30
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 10.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 31
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 11.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 32
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 12.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 33
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 13.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 34
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 14.2
                elif GlobalVar.gsx // 32 * 17 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 35
                    xp = GlobalVar.gsx // 32 * 17
                    yp = GlobalVar.gsy // 18 * 15.2
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            elif riordinamento:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 6.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 7.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 8.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 9.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 10.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 11.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 12.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 13.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 14.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                elif GlobalVar.gsx // 32 * 7 <= xMouse <= GlobalVar.gsx // 32 * 23 and GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 16:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    voceMarcata = 15
                    xp = GlobalVar.gsx // 32 * 7
                    yp = GlobalVar.gsy // 18 * 15.2
                    dati, imgRigheGambit = modificaOrdineGambitConMouse(dati, voceMarcata, voceMarcataVecchia, imgRigheGambit)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
            if not riordinamento:
                risposta = True
            else:
                primoFrame = True
                riordinamento = False
                annullaRiordinamento = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato) or bottoneDown == "padCroce":
            # riordina
            if riordinamento:
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                    primoFrame = True
                    riordinamento = False
                    annullaRiordinamento = True
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                    primoFrame = True
                    riordinamento = False
            else:
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                    risposta = True
                else:
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armrob
                    if voceMarcata == 1:
                        if dati[71] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            dati[9] = 0
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if voceMarcata == 2:
                        if dati[72] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            dati[9] = 1
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if voceMarcata == 3:
                        if dati[73] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            dati[9] = 2
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if voceMarcata == 4:
                        if dati[74] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            dati[9] = 3
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if voceMarcata == 5:
                        if dati[75] != 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            dati[9] = 4
                            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)
                            if dati[10] > entot:
                                dati[10] = entot
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)

                    # riordina
                    if 6 <= voceMarcata <= 15:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
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
                                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                                dati[i] = sceglicondiz(dati, dati[i])
                            else:
                                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                        i += 1
                        c += 1

                    # tecniche
                    i = 111
                    c = 26
                    while i <= 120:
                        if voceMarcata == c:
                            primoFrame = True
                            if dati[i] != -1:
                                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                                dati[i] = sceglitecn(dati, dati[i])
                            else:
                                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                        i += 1
                        c += 1
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if riordinamento:
                    if voceMarcata != 6:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
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
                        yp = yp - GlobalVar.gsy // 18 * 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                        bottoneDown = False
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 1:
                            voceMarcata += 4
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 14.8
                        else:
                            voceMarcata -= 1
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = yp - GlobalVar.gsy // 18 * 2
                    else:
                        if voceMarcata == 6 or voceMarcata == 16 or voceMarcata == 26:
                            voceMarcata += 9
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 15.2
                        else:
                            voceMarcata -= 1
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = yp - GlobalVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if not riordinamento:
                    if 1 <= voceMarcata <= 5:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        if voceMarcata == 1:
                            voceMarcata += 26
                            yp = GlobalVar.gsy // 18 * 7.2
                        elif voceMarcata == 2:
                            voceMarcata += 27
                            yp = GlobalVar.gsy // 18 * 9.2
                        elif voceMarcata == 3:
                            voceMarcata += 28
                            yp = GlobalVar.gsy // 18 * 11.2
                        elif voceMarcata == 4:
                            voceMarcata += 29
                            yp = GlobalVar.gsy // 18 * 13.2
                        elif voceMarcata == 5:
                            voceMarcata += 30
                            yp = GlobalVar.gsy // 18 * 15.2
                        xp = GlobalVar.gsx // 32 * 17
                    elif 6 <= voceMarcata <= 15:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        if 6 <= voceMarcata <= 7:
                            if voceMarcata == 6:
                                voceMarcata -= 5
                            elif voceMarcata == 7:
                                voceMarcata -= 6
                            yp = GlobalVar.gsy // 18 * 6.8
                        elif 8 <= voceMarcata <= 9:
                            if voceMarcata == 8:
                                voceMarcata -= 6
                            elif voceMarcata == 9:
                                voceMarcata -= 7
                            yp = GlobalVar.gsy // 18 * 8.8
                        elif 10 <= voceMarcata <= 11:
                            if voceMarcata == 10:
                                voceMarcata -= 7
                            elif voceMarcata == 11:
                                voceMarcata -= 8
                            yp = GlobalVar.gsy // 18 * 10.8
                        elif 12 <= voceMarcata <= 13:
                            if voceMarcata == 12:
                                voceMarcata -= 8
                            elif voceMarcata == 13:
                                voceMarcata -= 9
                            yp = GlobalVar.gsy // 18 * 12.8
                        elif 14 <= voceMarcata <= 15:
                            if voceMarcata == 14:
                                voceMarcata -= 9
                            elif voceMarcata == 15:
                                voceMarcata -= 10
                            yp = GlobalVar.gsy // 18 * 14.8
                        xp = GlobalVar.gsx // 32 * 1
                    elif 16 <= voceMarcata <= 25:
                        voceMarcata -= 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 7
                    elif 26 <= voceMarcata <= 35:
                        voceMarcata -= 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 10.8
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if riordinamento:
                    if voceMarcata != 15:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
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
                        yp = yp + GlobalVar.gsy // 18 * 1
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                        bottoneDown = False
                else:
                    if 1 <= voceMarcata <= 5:
                        if voceMarcata == 5:
                            voceMarcata -= 4
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 6.8
                        else:
                            voceMarcata += 1
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = yp + GlobalVar.gsy // 18 * 2
                    else:
                        if voceMarcata == 15 or voceMarcata == 25 or voceMarcata == 35:
                            voceMarcata -= 9
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = GlobalVar.gsy // 18 * 6.2
                        else:
                            voceMarcata += 1
                            GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                            yp = yp + GlobalVar.gsy // 18 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if not riordinamento:
                    if 1 <= voceMarcata <= 5:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        if voceMarcata == 1:
                            voceMarcata += 6
                            yp = GlobalVar.gsy // 18 * 7.2
                        elif voceMarcata == 2:
                            voceMarcata += 7
                            yp = GlobalVar.gsy // 18 * 9.2
                        elif voceMarcata == 3:
                            voceMarcata += 8
                            yp = GlobalVar.gsy // 18 * 11.2
                        elif voceMarcata == 4:
                            voceMarcata += 9
                            yp = GlobalVar.gsy // 18 * 13.2
                        elif voceMarcata == 5:
                            voceMarcata += 10
                            yp = GlobalVar.gsy // 18 * 15.2
                        xp = GlobalVar.gsx // 32 * 7
                    elif 6 <= voceMarcata <= 15:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 10.8
                    elif 16 <= voceMarcata <= 25:
                        voceMarcata += 10
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        xp = GlobalVar.gsx // 32 * 17
                    elif 26 <= voceMarcata <= 35:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        if 26 <= voceMarcata <= 27:
                            if voceMarcata == 26:
                                voceMarcata -= 25
                            elif voceMarcata == 27:
                                voceMarcata -= 26
                            yp = GlobalVar.gsy // 18 * 6.8
                        elif 28 <= voceMarcata <= 29:
                            if voceMarcata == 28:
                                voceMarcata -= 26
                            elif voceMarcata == 29:
                                voceMarcata -= 27
                            yp = GlobalVar.gsy // 18 * 8.8
                        elif 30 <= voceMarcata <= 31:
                            if voceMarcata == 30:
                                voceMarcata -= 27
                            elif voceMarcata == 31:
                                voceMarcata -= 28
                            yp = GlobalVar.gsy // 18 * 10.8
                        elif 32 <= voceMarcata <= 33:
                            if voceMarcata == 32:
                                voceMarcata -= 28
                            elif voceMarcata == 33:
                                voceMarcata -= 29
                            yp = GlobalVar.gsy // 18 * 12.8
                        elif 34 <= voceMarcata <= 35:
                            if voceMarcata == 34:
                                voceMarcata -= 29
                            elif voceMarcata == 35:
                                voceMarcata -= 30
                            yp = GlobalVar.gsy // 18 * 14.8
                        xp = GlobalVar.gsx // 32 * 1
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.grigioscu)
                # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 15.5))

                messaggio("Setta Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                messaggio("Batterie", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 3.5, GlobalVar.gsy // 18 * 4.6, 60, centrale=True)
                messaggio("Ordine", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 8.8, GlobalVar.gsy // 18 * 4.6, 60, centrale=True)
                messaggio("Condizione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.9, GlobalVar.gsy // 18 * 4.6, 60, centrale=True)
                messaggio("Tecnica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 19.8, GlobalVar.gsy // 18 * 4.6, 60, centrale=True)
                # equip batteria
                i = 0
                while i < 5:
                    GlobalVar.disegnaImmagineSuSchermo(sfondoOggetto, (GlobalVar.gsx // 32 * 2.5, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    GlobalVar.disegnaImmagineSuSchermo(vetIcoBatterie[i], (GlobalVar.gsx // 32 * 2.5, (GlobalVar.gsy // 18 * 6 + (GlobalVar.gpy * 2 * i))))
                    i += 1
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 1.5), int(GlobalVar.gpy * 5.6)), (int(GlobalVar.gpx * 5.5), int(GlobalVar.gpy * 5.6)), 1)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 10.8) - 1, int(GlobalVar.gpy * 4.4)), (int(GlobalVar.gpx * 10.8) - 1, int(GlobalVar.gpy * 5.4)), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 17) - 1, int(GlobalVar.gpy * 4.4)), (int(GlobalVar.gpx * 17) - 1, int(GlobalVar.gpy * 5.4)), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 7.5), int(GlobalVar.gpy * 5.6)), (int(GlobalVar.gpx * 22.5), int(GlobalVar.gpy * 5.6)), 1)
            elif not riordinamento:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 9))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 5.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 10.2))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 10.8, GlobalVar.gsy // 18 * 5.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 10.2))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 5.8, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 10.2))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 6.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 7.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 8.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 10.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 11.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 12.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 13.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 14.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 15.8, GlobalVar.gsx // 32 * 15.8, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 10.8) - 1, int(GlobalVar.gpy * 5.8)), (int(GlobalVar.gpx * 10.8) - 1, int(GlobalVar.gpy * 16)), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 17) - 1, int(GlobalVar.gpy * 5.8)), (int(GlobalVar.gpx * 17) - 1, int(GlobalVar.gpy * 16)), 2)
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 12))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                elif GlobalVar.usandoIlController:
                    messaggio("Cerchio: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)

            if annullaRiordinamento:
                dati = list(datiPrimaDiRiordinamento)
                annullaRiordinamento = False
                xp = vxpGambit
                yp = vypGambit
                voceMarcata = voceGambitMarcata

            if primoFrame:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 5.8, GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 10.3))
                if riordinamento:
                    GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscurino, (xp, yp - (GlobalVar.gpy // 4), GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 1))
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 10.8) - 1, int(GlobalVar.gpy * 5.8)), (int(GlobalVar.gpx * 10.8) - 1, int(GlobalVar.gpy * 16)), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 17) - 1, int(GlobalVar.gpy * 5.8)), (int(GlobalVar.gpx * 17) - 1, int(GlobalVar.gpy * 16)), 2)
                # programmazione Colco
                i = 1
                while i <= 10:
                    messaggio(str(i), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 8.8, GlobalVar.gsy // 18 * (i + 5.2), 50, centrale=True)
                    i += 1
                posXCondizioni = 11.8
                c = 6.3
                for i in range(101, 111):
                    if dati[i] == -1:
                        messaggio("---", GlobalVar.grigioscu, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 0:
                        messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 1:
                        messaggio("Lucy con pv < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 2:
                        messaggio("Lucy con pv < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 3:
                        messaggio("Lucy con pv < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 4:
                        messaggio("Lucy con veleno", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 5:
                        messaggio("Impo surriscaldato", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 6:
                        messaggio("Impo con pe < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 7:
                        messaggio("Impo con pe < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 8:
                        messaggio("Impo con pe < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 9:
                        messaggio("Sempre a Lucy", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 10:
                        messaggio("Sempre a Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 11:
                        messaggio("Nemico a caso", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 12:
                        messaggio("Nemico vicino", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 13:
                        messaggio("Nemico lontano", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 14:
                        messaggio("Nemico con pv < 80%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 15:
                        messaggio("Nemico con pv < 50%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 16:
                        messaggio("Nemico con pv < 30%", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 17:
                        messaggio("Nemico con meno pv", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 18:
                        messaggio("Numero di nemici > 1", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 19:
                        messaggio("Numero di nemici > 4", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 20:
                        messaggio("Numero di nemici > 7", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXCondizioni, GlobalVar.gsy // 18 * c, 40)
                    c += 1
                posXTecniche = 18
                c = 6.3
                for i in range(111, 121):
                    if dati[i] == -1:
                        messaggio("---", GlobalVar.grigioscu, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 0:
                        messaggio("---", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 1:
                        messaggio("Scossa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 2:
                        messaggio("Cura", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 3:
                        messaggio("Antidoto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 4:
                        messaggio("Freccia elettrica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 5:
                        messaggio("Tempesta elettrica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 6:
                        messaggio("Raffreddamento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 7:
                        messaggio("Auto-ricarica", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 8:
                        messaggio("Cura +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 9:
                        messaggio("Scossa +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 10:
                        messaggio("Freccia elettrica +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 11:
                        messaggio("Velocizza", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 12:
                        messaggio("Carica attacco", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 13:
                        messaggio("Carica difesa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 14:
                        messaggio("Efficienza", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 15:
                        messaggio("Tempesta elettrica +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 16:
                        messaggio("Cura ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 17:
                        messaggio("Auto-ricarica +", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 18:
                        messaggio("Scossa ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 19:
                        messaggio("Freccia Elettrica ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    if dati[i] == 20:
                        messaggio("Tempesta elettrica ++", GlobalVar.grigiochi, GlobalVar.gsx // 32 * posXTecniche, GlobalVar.gsy // 18 * c, 40)
                    c += 1

                if riordinamento:
                    screenRiordinamento = GlobalVar.schermo.copy()
                    imgRigheGambit = []
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 6.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 7.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 8.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 9.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 10.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 11.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 12.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 13.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 14.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())
                    imgRigheGambit.append(screenRiordinamento.subsurface(pygame.Rect(GlobalVar.gpx * 7, (GlobalVar.gpy * 15.2) - (GlobalVar.gpy // 4), GlobalVar.gpx * 16, GlobalVar.gpy)).convert())

            if annullaRiordinamento:
                annullaRiordinamento = False

            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

            if not riordinamento:
                GlobalVar.disegnaImmagineSuSchermo(robosta, (GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 10))
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (int(GlobalVar.gpx * 25), int(GlobalVar.gpy * 15)), (int(GlobalVar.gpx * 30), int(GlobalVar.gpy * 15)), 2)
                GlobalVar.disegnaImmagineSuSchermo(vetImgBatterie[dati[9]], (GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 10))
                messaggio("Statistiche:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 7.7, 50)
                messaggio("Pe totali: %i" % entot, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 8.5, 35)
                messaggio("Difesa: %i" % difro, GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 9, 35)

                # mostrare descrizione batterie / priorità / condizioni / azioni
                larghezzaTestoDescrizioni = GlobalVar.gpx * 7.5
                spazioTraLeRigheTestoDescrizione = GlobalVar.gpy // 2
                if voceMarcata == 1:
                    if dati[71] != 0:
                        messaggio("Batteria piccola:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                        messaggio("Batteria che contiene poca alimentazione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (0 * 0 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 0:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        diff = 0 - (dati[9] * dati[9] * 30)
                        if dati[9] > 0:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    else:
                        messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                if voceMarcata == 2:
                    if dati[72] != 0:
                        messaggio("Batteria discreta:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                        messaggio("Batteria con una buona capienza e ottimizzazione del sistema difensivo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (1 * 1 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 1:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        elif dati[9] < 1:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        diff = 30 - (dati[9] * dati[9] * 30)
                        if dati[9] > 1:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                        elif dati[9] < 1:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    else:
                        messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                if voceMarcata == 3:
                    if dati[73] != 0:
                        messaggio("Batteria capiente:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                        messaggio(u"Batteria con una grande capacità e un ottimo sistema difensivo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (2 * 2 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 2:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        elif dati[9] < 2:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        diff = 120 - (dati[9] * dati[9] * 30)
                        if dati[9] > 2:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                        elif dati[9] < 2:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    else:
                        messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                if voceMarcata == 4:
                    if dati[74] != 0:
                        messaggio("Batteria enorme:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                        messaggio(u"Grande batteria che permette a Impo di utilizzare le tecniche più dispendiose", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (3 * 3 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 3:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        elif dati[9] < 3:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        diff = 270 - (dati[9] * dati[9] * 30)
                        if dati[9] > 3:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                        elif dati[9] < 3:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    else:
                        messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                if voceMarcata == 5:
                    if dati[75] != 0:
                        messaggio("Batteria illimitata:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                        messaggio("Batteria incredibilmente capiente. Permette un eccellente ottimizzazione del sistema difensivo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = (4 * 4 * 80) - (dati[9] * dati[9] * 80)
                        if dati[9] > 4:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        elif dati[9] < 4:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 8.5, 35)
                        diff = 480 - (dati[9] * dati[9] * 30)
                        if dati[9] > 4:
                            messaggio(str(diff), GlobalVar.rosso, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                        elif dati[9] < 4:
                            messaggio("+" + str(diff), GlobalVar.verde, GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 9, 35)
                    else:
                        messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)

                if 6 <= voceMarcata <= 15:
                    messaggio(u"Ordine:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                    messaggio(u"Indica la priorità dell'azione. Impo eseguirà la tecnica associata alla prima condizione verificata della lista", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

                if 16 <= voceMarcata <= 25:
                    messaggio("Condizione:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                    messaggio(u"Indica la situazione che si deve verificare affinché Impo esegua la tecnica associata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

                if 26 <= voceMarcata <= 35:
                    messaggio("Tecnica:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4.8, 60)
                    messaggio(u"La tecnica che Impo eseguirà quando si verifica la condizione associata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 5.8, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            else:
                i = 0
                for riga in imgRigheGambit:
                    GlobalVar.disegnaImmagineSuSchermo(riga, (GlobalVar.gsx // 32 * 7, (GlobalVar.gsy // 18 * 6.2) - (GlobalVar.gpy // 4) + (GlobalVar.gpx * i)))
                    i += 1

            # puntatore vecchio batterie/riordinamento gambit
            if dati[9] == 0:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 6.8))
            if dati[9] == 1:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 8.8))
            if dati[9] == 2:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 10.8))
            if dati[9] == 3:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 12.8))
            if dati[9] == 4:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 14.8))
            if riordinamento:
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (vxpGambit, vypGambit))

            GlobalVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if voceMarcata >= 6 and not riordinamento:
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 7.5, yp + (int(GlobalVar.gpy * 0.7))), (GlobalVar.gsx // 32 * 10.6, yp + (int(GlobalVar.gpy * 0.7))), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 11, yp + (int(GlobalVar.gpy * 0.7))), (GlobalVar.gsx // 32 * 16.8, yp + (int(GlobalVar.gpy * 0.7))), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 17.2, yp + (int(GlobalVar.gpy * 0.7))), (GlobalVar.gsx // 32 * 22.5, yp + (int(GlobalVar.gpy * 0.7))), 2)
            primoFrame = False

            GlobalVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
    return dati


def oggetti(dati, colcoInCasellaVista):
    puntatore = GlobalVar.puntatore
    puntatorevecchio = GlobalVar.puntatorevecchio
    sconosciutoOggetto = GlobalVar.sconosciutoOggettoMenu3
    if GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= dati[0] < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        perssta = GlobalVar.imgFraMaggioreMenuOggetti
    else:
        perssta = GlobalVar.imgLucyMenuOggetti
    xp = GlobalVar.gsx // 32 * 1
    yp = GlobalVar.gsy // 18 * 6.2
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
            imgOggetti.append(GlobalVar.vetImgOggettiMenu[i - 1])
        else:
            imgOggetti.append(sconosciutoOggetto)
        i += 1

    esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = getStatistiche(dati)

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
        if GlobalVar.mouseVisibile:
            if usa != 0:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVar.gsy // 18 * 14.5 <= yMouse <= GlobalVar.gsy // 18 * 16.5:
                    if GlobalVar.gsx // 32 * 11 <= xMouse <= GlobalVar.gsx // 32 * 15:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 1
                        xp = GlobalVar.gsx // 32 * 12.7
                        yp = GlobalVar.gsy // 18 * 15.1
                    elif GlobalVar.gsx // 32 * 15 <= xMouse <= GlobalVar.gsx // 32 * 19:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        voceMarcata = 2
                        xp = GlobalVar.gsx // 32 * 15
                        yp = GlobalVar.gsy // 18 * 15.1
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            else:
                if GlobalVar.gsx // 32 * 21.5 <= xMouse <= GlobalVar.gsx and 0 <= yMouse <= GlobalVar.gsy // 18 * 2:
                    if GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(False)
                    suTornaIndietro = True
                elif GlobalVar.gsx // 32 * 1 <= xMouse <= GlobalVar.gsx // 32 * 11:
                    if GlobalVar.gsy // 18 * 5.9 <= yMouse <= GlobalVar.gsy // 18 * 6.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 1
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 6.2
                    elif GlobalVar.gsy // 18 * 6.9 <= yMouse <= GlobalVar.gsy // 18 * 7.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 2
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 7.2
                    elif GlobalVar.gsy // 18 * 7.9 <= yMouse <= GlobalVar.gsy // 18 * 8.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 3
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 8.2
                    elif GlobalVar.gsy // 18 * 8.9 <= yMouse <= GlobalVar.gsy // 18 * 9.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 4
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 9.2
                    elif GlobalVar.gsy // 18 * 9.9 <= yMouse <= GlobalVar.gsy // 18 * 10.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 5
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 10.2
                    elif GlobalVar.gsy // 18 * 10.9 <= yMouse <= GlobalVar.gsy // 18 * 11.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 6
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 11.2
                    elif GlobalVar.gsy // 18 * 11.9 <= yMouse <= GlobalVar.gsy // 18 * 12.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 7
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 12.2
                    elif GlobalVar.gsy // 18 * 12.9 <= yMouse <= GlobalVar.gsy // 18 * 13.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 8
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 13.2
                    elif GlobalVar.gsy // 18 * 13.9 <= yMouse <= GlobalVar.gsy // 18 * 14.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 9
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 14.2
                    elif GlobalVar.gsy // 18 * 14.9 <= yMouse <= GlobalVar.gsy // 18 * 15.9:
                        if GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(False)
                        oggetton = 10
                        xp = GlobalVar.gsx // 32 * 1
                        yp = GlobalVar.gsy // 18 * 15.2
                    else:
                        if not GlobalVar.mouseBloccato:
                            GlobalVar.configuraCursore(True)
                else:
                    if not GlobalVar.mouseBloccato:
                        GlobalVar.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton) and not primoFrame:
                GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        bottoneDown, aggiornaInterfacciaPerCambioInput = getInput(bottoneDown, aggiornaInterfacciaPerCambioInput)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            voceMarcata = 0
            if usa != 0:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                xp = GlobalVar.gsx // 32 * 1
                if usa == 1:
                    yp = GlobalVar.gsy // 18 * 6.2
                if usa == 2:
                    yp = GlobalVar.gsy // 18 * 7.2
                if usa == 3:
                    yp = GlobalVar.gsy // 18 * 8.2
                if usa == 4:
                    yp = GlobalVar.gsy // 18 * 9.2
                if usa == 5:
                    yp = GlobalVar.gsy // 18 * 10.2
                if usa == 6:
                    yp = GlobalVar.gsy // 18 * 11.2
                if usa == 7:
                    yp = GlobalVar.gsy // 18 * 12.2
                if usa == 8:
                    yp = GlobalVar.gsy // 18 * 13.2
                if usa == 9:
                    yp = GlobalVar.gsy // 18 * 14.2
                if usa == 10:
                    yp = GlobalVar.gsy // 18 * 15.2
                usa = 0
            else:
                GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                voceMarcata = 0
                if usa != 0:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                    xp = GlobalVar.gsx // 32 * 1
                    if usa == 1:
                        yp = GlobalVar.gsy // 18 * 6.2
                    if usa == 2:
                        yp = GlobalVar.gsy // 18 * 7.2
                    if usa == 3:
                        yp = GlobalVar.gsy // 18 * 8.2
                    if usa == 4:
                        yp = GlobalVar.gsy // 18 * 9.2
                    if usa == 5:
                        yp = GlobalVar.gsy // 18 * 10.2
                    if usa == 6:
                        yp = GlobalVar.gsy // 18 * 11.2
                    if usa == 7:
                        yp = GlobalVar.gsy // 18 * 12.2
                    if usa == 8:
                        yp = GlobalVar.gsy // 18 * 13.2
                    if usa == 9:
                        yp = GlobalVar.gsy // 18 * 14.2
                    if usa == 10:
                        yp = GlobalVar.gsy // 18 * 15.2
                    usa = 0
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
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
                        yp = GlobalVar.gsy // 18 * 6.2
                    # carica batt
                    if usa == 2:
                        dati[10] = dati[10] + 250
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[32] = dati[32] - 1
                        yp = GlobalVar.gsy // 18 * 7.2
                    # antidoto
                    if usa == 3:
                        dati[121] = 0
                        dati[33] = dati[33] - 1
                        yp = GlobalVar.gsy // 18 * 8.2
                    # super pozione
                    if usa == 4:
                        dati[5] = dati[5] + 300
                        if dati[5] > pvtot:
                            dati[5] = pvtot
                        dati[34] = dati[34] - 1
                        yp = GlobalVar.gsy // 18 * 9.2
                    # carica migliorato
                    if usa == 5:
                        dati[10] = dati[10] + 600
                        if dati[10] > entot:
                            dati[10] = entot
                        dati[35] = dati[35] - 1
                        yp = GlobalVar.gsy // 18 * 10.2
                    # bomba
                    if usa == 6:
                        attacco = 2
                        yp = GlobalVar.gsy // 18 * 11.2
                    # bomba veleno
                    if usa == 7:
                        attacco = 3
                        yp = GlobalVar.gsy // 18 * 12.2
                    # esca
                    if usa == 8:
                        attacco = 4
                        yp = GlobalVar.gsy // 18 * 13.2
                    # bomba appiccicosa
                    if usa == 9:
                        attacco = 5
                        yp = GlobalVar.gsy // 18 * 14.2
                    # bomba potenziata
                    if usa == 10:
                        attacco = 6
                        yp = GlobalVar.gsy // 18 * 15.2
                    if (usa == 2 or usa == 5) and dati[0] < GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    else:
                        GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                        primoFrame = True
                        xp = GlobalVar.gsx // 32 * 1
                        voceMarcata = 0
                        usa = 0
                elif voceMarcata == 2:
                    voceMarcata = 0
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selind)
                    xp = GlobalVar.gsx // 32 * 1
                    if usa == 1:
                        yp = GlobalVar.gsy // 18 * 6.2
                    if usa == 2:
                        yp = GlobalVar.gsy // 18 * 7.2
                    if usa == 3:
                        yp = GlobalVar.gsy // 18 * 8.2
                    if usa == 4:
                        yp = GlobalVar.gsy // 18 * 9.2
                    if usa == 5:
                        yp = GlobalVar.gsy // 18 * 10.2
                    if usa == 6:
                        yp = GlobalVar.gsy // 18 * 11.2
                    if usa == 7:
                        yp = GlobalVar.gsy // 18 * 12.2
                    if usa == 8:
                        yp = GlobalVar.gsy // 18 * 13.2
                    if usa == 9:
                        yp = GlobalVar.gsy // 18 * 14.2
                    if usa == 10:
                        yp = GlobalVar.gsy // 18 * 15.2
                    usa = 0
                    usadue = False
                # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                if usadue:
                    if oggetton == 1:
                        if dati[31] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 1
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 2:
                        if dati[32] > 0 and dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 2
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                            if not dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] or not colcoInCasellaVista:
                                impossibileUsareCaricaBatt = True
                    if oggetton == 3:
                        if dati[33] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 3
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 4:
                        if dati[34] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 4
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 5:
                        if dati[35] > 0 and dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 5
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                            if not dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] or not colcoInCasellaVista:
                                impossibileUsareCaricaBatt = True
                    if oggetton == 6:
                        if dati[36] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 6
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 7:
                        if dati[37] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 7
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 8:
                        if dati[38] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 8
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 9:
                        if dati[39] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 9
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    if oggetton == 10:
                        if dati[40] > 0:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selezione)
                            usa = 10
                            usauno = True
                        else:
                            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalVar.mouseBloccato:
            GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padGiu" or bottoneDown == "padSu" or bottoneDown == "padDestra" or bottoneDown == "padSinistra":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalVar.canaleSoundInterazioni.play(GlobalVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or oggettonVecchio != oggetton or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    if oggetton != 1:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        oggetton = oggetton - 1
                        yp = yp - GlobalVar.gsy // 18 * 1
                    elif oggetton == 1:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 15.2
                        oggetton = 10
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2:
                    voceMarcata -= 1
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 12.7
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 0:
                    if oggetton != 10:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        oggetton = oggetton + 1
                        yp = yp + GlobalVar.gsy // 18 * 1
                    elif oggetton == 10:
                        GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                        yp = GlobalVar.gsy // 18 * 6.2
                        oggetton = 1
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    voceMarcata += 1
                    GlobalVar.canaleSoundPuntatoreSposta.play(GlobalVar.spostapun)
                    xp = GlobalVar.gsx // 32 * 15
                else:
                    GlobalVar.canaleSoundPuntatoreSeleziona.play(GlobalVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4, GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 15.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoSinistra, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.5))
                messaggio("Oggetti", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 1, 150)
                messaggio("Nome oggetto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 4.3, GlobalVar.gsy // 18 * 4.7, 50, centrale=True)
                messaggio(u"Quantità", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 4.7, 50, centrale=True)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 1.5), int(GlobalVar.gpy * 5.6)), (int(GlobalVar.gpx * 10.5), int(GlobalVar.gpy * 5.6)), 1)
                if dati[31] >= 0:
                    messaggio("Pozione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.2, 45)
                    messaggio("x%i" % dati[31], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 6.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 6.2, 45)
                if dati[32] >= 0:
                    if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                        messaggio("Alimentazione 100gr", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 45)
                    else:
                        messaggio("Alimentazione 100gr", GlobalVar.grigioscu, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 45)
                    messaggio("x%i" % dati[32], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 7.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7.2, 45)
                if dati[33] >= 0:
                    messaggio("Medicina", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.2, 45)
                    messaggio("x%i" % dati[33], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 8.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 8.2, 45)
                if dati[34] >= 0:
                    messaggio("Super pozione", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.2, 45)
                    messaggio("x%i" % dati[34], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 9.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 9.2, 45)
                if dati[35] >= 0:
                    if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"] and colcoInCasellaVista:
                        messaggio("Alimentazione 250gr", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 45)
                    else:
                        messaggio("Alimentazione 250gr", GlobalVar.grigioscu, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 45)
                    messaggio("x%i" % dati[35], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 10.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 10.2, 45)
                if dati[36] >= 0:
                    messaggio("Bomba", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.2, 45)
                    messaggio("x%i" % dati[36], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 11.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 11.2, 45)
                if dati[37] >= 0:
                    messaggio("Bomba velenosa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.2, 45)
                    messaggio("x%i" % dati[37], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 12.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 12.2, 45)
                if dati[38] >= 0:
                    messaggio("Esca", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.2, 45)
                    messaggio("x%i" % dati[38], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 13.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13.2, 45)
                if dati[39] >= 0:
                    messaggio("Bomba appiccicosa", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.2, 45)
                    messaggio("x%i" % dati[39], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 14.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 14.2, 45)
                if dati[40] >= 0:
                    messaggio("Bomba potenziata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.2, 45)
                    messaggio("x%i" % dati[40], GlobalVar.grigiochi, GlobalVar.gsx // 32 * 9.1, GlobalVar.gsy // 18 * 15.2, 45, centrale=True)
                else:
                    messaggio("???", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 15.2, 45)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 7.6) - 1, int(GlobalVar.gpy * 4.5)), (int(GlobalVar.gpx * 7.6) - 1, int(GlobalVar.gpy * 5.4)), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 7.6) - 1, int(GlobalVar.gpy * 5.8)), (int(GlobalVar.gpx * 7.6) - 1, int(GlobalVar.gpy * 16)), 2)
            else:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 6, GlobalVar.gsx // 32 * 0.5, GlobalVar.gsy // 18 * 10))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 6.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 6.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 7.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 7.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 8.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 8.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 9.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 9.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 10.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 10.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 11.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 11.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 12.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 12.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 13.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 13.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 14.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 14.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 15.77, GlobalVar.gsx // 32 * 6.5, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (GlobalVar.gsx // 32 * 7.7, GlobalVar.gsy // 18 * 15.77, GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 0.3))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 14))
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 19.5, GlobalVar.gsy // 18 * 3, GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 14))
                if impossibileUsareCaricaBatt:
                    messaggio(u"Impo è irraggiungibile!", GlobalVar.rosso, GlobalVar.gsx // 32 * 12.2, GlobalVar.gsy // 18 * 15, 50)
                    if oggettonVecchio != oggetton:
                        impossibileUsareCaricaBatt = False
                        GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 14))
                else:
                    GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 14))
            if aggiornaInterfacciaPerCambioInput:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (GlobalVar.gsx // 32 * 21, 0, GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 2.5))
                aggiornaInterfacciaPerCambioInput = False
                if GlobalVar.mouseVisibile:
                    messaggio("Tasto destro: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 22.5, GlobalVar.gsy // 18 * 1, 50)
                elif GlobalVar.usandoIlController:
                    messaggio("Cerchio: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 23.5, GlobalVar.gsy // 18 * 1, 50)
                else:
                    messaggio("Q: torna indietro", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 1, 50)

            # menu conferma
            if usa != 0:
                GlobalVar.disegnaRettangoloSuSchermo(GlobalVar.schermo, GlobalVar.grigioscurino, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 12.5, GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 4))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoAltoDestra, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 12.5))
                GlobalVar.disegnaImmagineSuSchermo(GlobalVar.sfondoTriangolinoBassoDestra, (GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 15.5))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = GlobalVar.gsx // 32 * 15
                    yp = GlobalVar.gsy // 18 * 15.1
                    voceMarcata = 2
                    usauno = False
                GlobalVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.3, GlobalVar.gsy // 18 * 13, 90)
                messaggio("Si", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 13.4, GlobalVar.gsy // 18 * 14.9, 70)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, (int(GlobalVar.gpx * 15) - 1, int(GlobalVar.gpy * 14.8)), (int(GlobalVar.gpx * 15) - 1, int(GlobalVar.gpy * 15.9)), 2)
                messaggio("No", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 15.7, GlobalVar.gsy // 18 * 14.9, 70)

            larghezzaTestoDescrizioni = GlobalVar.gpx * 11
            spazioTraLeRigheTestoDescrizione = GlobalVar.gpy // 2
            if dati[31] >= 0 and oggetton == 1:
                messaggio("Pozione:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Recupera 100 pv", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 1:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[32] >= 0 and oggetton == 2:
                messaggio("Alimentazione 100gr:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Recupera 250 pe di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 2:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[33] >= 0 and oggetton == 3:
                messaggio("Medicina:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Cura avvelenamento", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 3:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[34] >= 0 and oggetton == 4:
                messaggio("Super pozione:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Recupera 300 pv", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 4:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[35] >= 0 and oggetton == 5:
                messaggio("Alimentazione 250gr:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Recupera 600 pe di Impo", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 5:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[36] >= 0 and oggetton == 6:
                messaggio("Bomba:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Infligge un po' di danni ai nemici su cui viene lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 6:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[37] >= 0 and oggetton == 7:
                messaggio("Bomba velenosa:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Infligge avvelenamento al nemico su cui viene lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 7:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[38] >= 0 and oggetton == 8:
                messaggio("Esca:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio(u"Distrae i nemici finché non viene distrutta. È possibile riprenderla passandoci sopra", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 8:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[39] >= 0 and oggetton == 9:
                messaggio("Bomba appiccicosa:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio(u"Dimezza la velocità del nemico su cui viene lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 9:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
            if dati[40] >= 0 and oggetton == 10:
                messaggio("Bomba potenziata:", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)
                messaggio("Infligge molti danni ai nemici su cui viene lanciata", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 14.5, 35, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            elif oggetton == 10:
                messaggio("Sconosciuto", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 13.5, 60)

            # vita-status personaggio
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.1, GlobalVar.gsy // 18 * 4.9, 50)
            messaggio("Status alterati: ", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.1, GlobalVar.gsy // 18 * 5.7, 50)
            GlobalVar.disegnaImmagineSuSchermo(perssta, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 4.6))
            GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (int(GlobalVar.gpx * 11), int(GlobalVar.gpy * 7.6)), (int(GlobalVar.gpx * 18.2), int(GlobalVar.gpy * 7.6)), 2)
            if dati[121]:
                avvelenato = GlobalVar.avvelenatoMenu
                GlobalVar.disegnaImmagineSuSchermo(avvelenato, (GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 6.5))
            if dati[123] > 0:
                attaccopiu = GlobalVar.attaccopiuMenu
                GlobalVar.disegnaImmagineSuSchermo(attaccopiu, ((GlobalVar.gsx // 32 * 14) + (2 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 6.5))
            if dati[124] > 0:
                difesapiu = GlobalVar.difesapiuMenu
                GlobalVar.disegnaImmagineSuSchermo(difesapiu, ((GlobalVar.gsx // 32 * 14) + (4 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 6.5))
            # vita-status robo
            if dati[0] >= GlobalVar.dictAvanzamentoStoria["incontratoColco"]:
                if dati[10] < 0:
                    dati[10] = 0
                messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.1, GlobalVar.gsy // 18 * 8.4, 50)
                messaggio("Status alterati: ", GlobalVar.grigiochi, GlobalVar.gsx // 32 * 14.1, GlobalVar.gsy // 18 * 9.2, 50)
                robomen = GlobalVar.roboo2
                GlobalVar.disegnaImmagineSuSchermo(robomen, (GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 8.1))
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigio, (int(GlobalVar.gpx * 11), int(GlobalVar.gpy * 11.1)), (int(GlobalVar.gpx * 18.2), int(GlobalVar.gpy * 11.1)), 2)
                if dati[122] > 0:
                    surriscaldato = GlobalVar.surriscaldatoMenu
                    GlobalVar.disegnaImmagineSuSchermo(surriscaldato, (GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 10))
                if dati[125] > 0:
                    velocitapiu = GlobalVar.velocitapiuMenu
                    GlobalVar.disegnaImmagineSuSchermo(velocitapiu, ((GlobalVar.gsx // 32 * 14) + (2 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 10))
                if dati[126] > 0:
                    efficienzapiu = GlobalVar.efficienzapiuMenu
                    GlobalVar.disegnaImmagineSuSchermo(efficienzapiu, ((GlobalVar.gsx // 32 * 14) + (4 * GlobalVar.gpx // 4 * 3), GlobalVar.gsy // 18 * 10))

            if attacco != 0:
                risposta = True

            GlobalVar.disegnaImmagineSuSchermo(imgOggetti[oggetton - 1], (GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 3))
            GlobalVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if usa == 0:
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((xp + (int(GlobalVar.gpx * 0.5))), yp + (int(GlobalVar.gpy * 0.7)) - 1), (xp + (int(GlobalVar.gpx * 6.4)), yp + (int(GlobalVar.gpy * 0.7)) - 1), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((xp + (int(GlobalVar.gpx * 6.8))), yp + (int(GlobalVar.gpy * 0.7)) - 1), (xp + (int(GlobalVar.gpx * 9.5)), yp + (int(GlobalVar.gpy * 0.7)) - 1), 2)
            else:
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((xpv + (int(GlobalVar.gpx * 0.5))), ypv + (int(GlobalVar.gpy * 0.7)) - 1), (xpv + (int(GlobalVar.gpx * 6.4)), ypv + (int(GlobalVar.gpy * 0.7)) - 1), 2)
                GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigioscu, ((xpv + (int(GlobalVar.gpx * 6.8))), ypv + (int(GlobalVar.gpy * 0.7)) - 1), (xpv + (int(GlobalVar.gpx * 9.5)), ypv + (int(GlobalVar.gpy * 0.7)) - 1), 2)
            primoFrame = False

            GlobalVar.aggiornaSchermo()

        pygame.event.pump()
        GlobalVar.clockMenu.tick(GlobalVar.fpsMenu)
    return dati, attacco
