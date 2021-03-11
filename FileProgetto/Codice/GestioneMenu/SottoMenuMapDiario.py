# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def menuMappa(avanzamentoStoria):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    imgOmbreggiaturaContorniMappaMenu = GlobalImgVar.imgOmbreggiaturaContorniMappaMenu
    backgroundTornaIndietro = GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2))
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.5
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = False
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico la mappa a seconda dell'avanzamento
    imgMappaA = GlobalImgVar.imgMappa1A
    imgMappaB = GlobalImgVar.imgMappa1B
    postiSbloccati = {"Casa": False, "Città": False, "Avamposto di Rod": False, "Castello": False, "Palazzo di Rod": False, "Vulcano": False, "Laboratorio": False, "Foresta cadetta": False, "Selva arida": False, "Labirinto": False, "Passo montano": False, "Caverna": False, "Tunnel di Rod": False, "Tunnel subacqueo": False}
    if avanzamentoStoria >= 0:
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCasa"]:
            postiSbloccati["Casa"] = True
            imgMappaA = GlobalImgVar.imgMappa1A
            imgMappaB = GlobalImgVar.imgMappa1B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaForestaCadetta"]:
            postiSbloccati["Foresta cadetta"] = True
            imgMappaA = GlobalImgVar.imgMappa2A
            imgMappaB = GlobalImgVar.imgMappa2B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCittà"]:
            postiSbloccati["Città"] = True
            imgMappaA = GlobalImgVar.imgMappa3A
            imgMappaB = GlobalImgVar.imgMappa3B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaSelvaArida"]:
            postiSbloccati["Selva arida"] = True
            imgMappaA = GlobalImgVar.imgMappa4A
            imgMappaB = GlobalImgVar.imgMappa4B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaAvampostoDiRod"]:
            postiSbloccati["Avamposto di Rod"] = True
            imgMappaA = GlobalImgVar.imgMappa5A
            imgMappaB = GlobalImgVar.imgMappa5B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLabirinto"]:
            postiSbloccati["Labirinto"] = True
            imgMappaA = GlobalImgVar.imgMappa6A
            imgMappaB = GlobalImgVar.imgMappa6B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCastello"]:
            postiSbloccati["Castello"] = True
            imgMappaA = GlobalImgVar.imgMappa7A
            imgMappaB = GlobalImgVar.imgMappa7B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPassoMontano"]:
            postiSbloccati["Passo montano"] = True
            imgMappaA = GlobalImgVar.imgMappa8A
            imgMappaB = GlobalImgVar.imgMappa8B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPalazzoDiRod"]:
            postiSbloccati["Palazzo di Rod"] = True
            imgMappaA = GlobalImgVar.imgMappa9A
            imgMappaB = GlobalImgVar.imgMappa9B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCaverna"]:
            postiSbloccati["Caverna"] = True
            imgMappaA = GlobalImgVar.imgMappa10A
            imgMappaB = GlobalImgVar.imgMappa10B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaVulcano"]:
            postiSbloccati["Vulcano"] = True
            imgMappaA = GlobalImgVar.imgMappa10A
            imgMappaB = GlobalImgVar.imgMappa10B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod1"]:
            postiSbloccati["Tunnel di Rod"] = True# <- il tunnel di Rod è diviso in due parti
            imgMappaA = GlobalImgVar.imgMappa11A
            imgMappaB = GlobalImgVar.imgMappa11B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod2"]:
            postiSbloccati["Tunnel di Rod"] = True
            imgMappaA = GlobalImgVar.imgMappa12A
            imgMappaB = GlobalImgVar.imgMappa12B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelSubacqueo"]:
            postiSbloccati["Tunnel subacqueo"] = True
            imgMappaA = GlobalImgVar.imgMappa13A
            imgMappaB = GlobalImgVar.imgMappa13B
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLaboratorio"]:
            postiSbloccati["Laboratorio"] = True
            imgMappaA = GlobalImgVar.imgMappa14A
            imgMappaB = GlobalImgVar.imgMappa14B

    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoAperturaMappa)
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
            elif not voceMarcataSottoMenu and GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 10:
                if GlobalHWVar.gsy // 18 * 4.3 <= yMouse <= GlobalHWVar.gsy // 18 * 5.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 4.5
                elif GlobalHWVar.gsy // 18 * 5.1 <= yMouse <= GlobalHWVar.gsy // 18 * 5.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 5.3
                elif GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 6.7:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.1
                elif GlobalHWVar.gsy // 18 * 6.7 <= yMouse <= GlobalHWVar.gsy // 18 * 7.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.9
                elif GlobalHWVar.gsy // 18 * 7.5 <= yMouse <= GlobalHWVar.gsy // 18 * 8.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7.7
                elif GlobalHWVar.gsy // 18 * 8.3 <= yMouse <= GlobalHWVar.gsy // 18 * 9.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.5
                elif GlobalHWVar.gsy // 18 * 9.1 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9.3
                elif GlobalHWVar.gsy // 18 * 10.5 <= yMouse <= GlobalHWVar.gsy // 18 * 11.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 8
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.7
                elif GlobalHWVar.gsy // 18 * 11.3 <= yMouse <= GlobalHWVar.gsy // 18 * 12.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 9
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 11.5
                elif GlobalHWVar.gsy // 18 * 12.1 <= yMouse <= GlobalHWVar.gsy // 18 * 12.9:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 10
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 12.3
                elif GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 13.7:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 11
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.1
                elif GlobalHWVar.gsy // 18 * 13.7 <= yMouse <= GlobalHWVar.gsy // 18 * 14.5:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 12
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.9
                elif GlobalHWVar.gsy // 18 * 14.5 <= yMouse <= GlobalHWVar.gsy // 18 * 15.3:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 13
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.7
                elif GlobalHWVar.gsy // 18 * 15.3 <= yMouse <= GlobalHWVar.gsy // 18 * 16.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 14
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 15.5
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
            if voceMarcataSottoMenu:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                voceMarcataSottoMenu = False
                primoFrame = True
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            primoFrame = True
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                if voceMarcataSottoMenu:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    voceMarcataSottoMenu = False
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
            elif not voceMarcataSottoMenu or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato):
                luogoMarcato = ""
                if voceMarcata == 1:
                    luogoMarcato = "Casa"
                if voceMarcata == 2:
                    luogoMarcato = "Città"
                if voceMarcata == 3:
                    luogoMarcato = "Avamposto di Rod"
                if voceMarcata == 4:
                    luogoMarcato = "Castello"
                if voceMarcata == 5:
                    luogoMarcato = "Palazzo di Rod"
                if voceMarcata == 6:
                    luogoMarcato = "Vulcano"
                if voceMarcata == 7:
                    luogoMarcato = "Laboratorio"
                if voceMarcata == 8:
                    luogoMarcato = "Foresta cadetta"
                if voceMarcata == 9:
                    luogoMarcato = "Selva arida"
                if voceMarcata == 10:
                    luogoMarcato = "Labirinto"
                if voceMarcata == 11:
                    luogoMarcato = "Passo montano"
                if voceMarcata == 12:
                    luogoMarcato = "Caverna"
                if voceMarcata == 13:
                    luogoMarcato = "Tunnel di Rod"
                if voceMarcata == 14:
                    luogoMarcato = "Tunnel subacqueo"
                if postiSbloccati[luogoMarcato]:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    voceMarcataSottoMenu = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if not voceMarcataSottoMenu:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata = 14
                        yp = GlobalHWVar.gsy // 18 * 15.5
                    elif voceMarcata == 8:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 1.4
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 0.8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if not voceMarcataSottoMenu:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 14:
                        voceMarcata = 1
                        yp = GlobalHWVar.gsy // 18 * 4.5
                    elif voceMarcata == 7:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 1.4
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 0.8
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if not voceMarcataSottoMenu:
                if primoFrame:
                    aggiornaInterfacciaPerCambioInput = True
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                    screen = GlobalHWVar.schermo.copy()
                    backgroundTornaIndietro = screen.subsurface(pygame.Rect(GlobalHWVar.gpx * 21, 0, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 2)).convert()
                    imgMappa = imgMappaA
                    GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                else:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.6))
            else:
                if primoFrame:
                    aggiornaInterfacciaPerCambioInput = True
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscuPiuScu, (GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 16))
                    imgMappa = imgMappaB
                    if voceMarcata == 1:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-16), GlobalHWVar.gsy // 18 * 1))
                    if voceMarcata == 2:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-4.5), GlobalHWVar.gsy // 18 * (-1.5)))
                    if voceMarcata == 3:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (3), GlobalHWVar.gsy // 18 * (-9.5)))
                    if voceMarcata == 4:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (8.5), GlobalHWVar.gsy // 18 * (-17)))
                    if voceMarcata == 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (7.5), GlobalHWVar.gsy // 18 * (-0.5)))
                    if voceMarcata == 6:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (16), GlobalHWVar.gsy // 18 * (0)))
                    if voceMarcata == 7:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-8), GlobalHWVar.gsy // 18 * (-17)))
                    if voceMarcata == 8:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-13.5), GlobalHWVar.gsy // 18 * (-5)))
                    if voceMarcata == 9:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (0.5), GlobalHWVar.gsy // 18 * (-8)))
                    if voceMarcata == 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (4), GlobalHWVar.gsy // 18 * (-13)))
                    if voceMarcata == 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (3.5), GlobalHWVar.gsy // 18 * (-1.5)))
                    if voceMarcata == 12:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (11.5), GlobalHWVar.gsy // 18 * (0)))
                    if voceMarcata == 13:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (7), GlobalHWVar.gsy // 18 * (-6)))
                    if voceMarcata == 14:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-1.5), GlobalHWVar.gsy // 18 * (-18.5)))
                    GlobalHWVar.disegnaImmagineSuSchermo(imgOmbreggiaturaContorniMappaMenu, (0, 0))
                    screen = GlobalHWVar.schermo.copy()
                    backgroundTornaIndietro = screen.subsurface(pygame.Rect(GlobalHWVar.gpx * 21, 0, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 2)).convert()
                    # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4))
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15.5))
                    GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
                    larghezzaTestoDescrizioni = GlobalHWVar.gpx * 9
                    spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
                    grandezzaScritteDescrizioni = 40
                    if voceMarcata == 1:
                        FunzioniGraficheGeneriche.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"È l'abitazione in cui ho vissuto con la mia famiglia fin'ora. È stata costruita da un mio vecchio antenato e, da allora, è sempre stata abitata dalle varie generazioni della mia famiglia. Secondo il babbo Hans sarà il prossimo proprietario e l'idea non lo entusiasma affatto: durante diverse discussioni Hans ha detto di non voler fare questo lavoro per tutta la vita come lui. Dice che è monotono, faticoso e anche instabile a causa delle enormi imposte e della spietata concorrenza.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 2:
                        FunzioniGraficheGeneriche.messaggio(u"Città", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Da quando ne ho sentito parlare per la prima volta, ho sempre avuto il desiderio di viverci. Da quello che so, lì a tutti è concesso scegliere quale mansione svolgere nella vita. Questo è diventato possibile grazie ai nuovi strumenti di produzione che hanno reso possibile un sistema in cui poche persone riescono a produrre abbastanza anche per tutte le altre. La parte di popolazione \"impoduttiva\" può quindi dedicarsi ad altre attività come musica, teatro, studio, sport e chissà cos'altro.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 3:
                        FunzioniGraficheGeneriche.messaggio("Avamposto di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Una piccola baracca che Rod esalta in maniera esagerata definendola \"avamposto\". Quella non è la sua abitazione ma, a suo dire, un luogo strategicamente fondamentale per la sopravvivenza dell'intero ecosistema cittadino. Rod non ispira molta fiducia ma tutti i suoi pensieri e ragionamenti mi sono sempre sembranti almeno sensati e coerenti... mi domando cosa nasconda quella baracca...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 4:
                        FunzioniGraficheGeneriche.messaggio("Castello", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"La più grande struttura che abbia mai visto fino ad ora. È un castello composto da un centinaio di stanze abitato dall'amico del bibliotecario e dai suoi numerosi servitori. Il vasto terreno su cui è stato costruito comprende anche l'intero labirinto che è stato appositamente elaborato per tenere lontani i visitatori indesiderati. Il silenzio e il comportamento dei servi creano un'atmosfera molto cupa...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 5:
                        FunzioniGraficheGeneriche.messaggio("Palazzo di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"La villa in cui dimora Rod. Risulta essere quasi sempre vuota e silenziosa dato che lui è costantemente fuori per lavoro o ricerche (mi domando ancora che cosa stia ricercando...). Il posto ricorda vagamente il castello di Norm ma in miniatura e con un passaggio montano al posto del labirinto per scoraggiare l'avvicinamento di viaggiatori sconosciuti.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 6:
                        FunzioniGraficheGeneriche.messaggio("Vulcano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un vulcano sommerso nelle montagne a ovest della città. È simile ad una montagna ma più grande e con un cratere sulla cima dal quale, a detta di Rod, fuoriesce del vapore incandescente. Chissà cosa c'è lì dentro...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 7:
                        FunzioniGraficheGeneriche.messaggio("Laboratorio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Il laboratorio in cui Norm svolge le sue ricerche. È molto piccolo ma al suo interno è presente tutto ciò che serve, ossia un calcolatore di eventi, che si estende anche sotto il terreno, e diversi altri calcolatori che credo servano per gestire i sistemi di alimentazione e raffreddamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 8:
                        FunzioniGraficheGeneriche.messaggio("Foresta cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"La foresta che mi ha sempre separata dalla città... non ho mai avuto il permesso di attraversarla perchè entrambi i miei genitori la ritenevano troppo pericolosa per me. Il nome deriva dal fatto che viene utilizzata come terreno di prova per selezionare, tra i giovani appartenenti alla nobiltà, i futuri ufficiali dell'esercito.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 9:
                        FunzioniGraficheGeneriche.messaggio("Selva arida", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Denominata in questo modo perchè un tempo fitta e intricata ed ora composta soltanto da secchi abusti e funghi. Le ragioni di questo suo decadimento non sono note agli abitanti locali ma, diversi libri della biblioteca in città, sostenevano che ciò fosse dovuto ad un cambiamento climatico avvenuto circa 50 anni fa... strano... <br> Rod è solito attraversarla per tornare al suo avamposto.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 10:
                        FunzioniGraficheGeneriche.messaggio("Labirinto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un enorme terreno estremamente complicato da superare a causa delle innumerevoli strade percorribili al suo interno prive di punti di riferimento. Rod mi ha fornito una mappa che mostra nel dettaglio la sua struttura sconsigliandomi di procedere: è molto probabile non riuscire ad uscirne se non si ha un buon senso dell'orientamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 11:
                        FunzioniGraficheGeneriche.messaggio("Passo montano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un passaggio tra le alture a ovest della città. In città nessuno sembrava sapere di questo varco apparte Rod che lo utilizza per raggiungere il proprio palazzo da più di vent'anni.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 12:
                        FunzioniGraficheGeneriche.messaggio("Caverna", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Una caverna in mezzo alle montagne che conduce ad un vulcano. All'interno vivono degli animali simili a Impo ma aggressivi. Rod è solito avventurarsi in quel posto per recuperare alimentazioni. Non mi spiego perché abbia deciso di viverci così vicino... forse ne è geloso e ne vuole controllare gli accessi?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 13:
                        FunzioniGraficheGeneriche.messaggio("Tunnel di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"È un passaggio sicuro e veloce tra il palazzo di Rod e il suo avamposto. Rod lo utilizzava per trasportare direttamente le alimentazioni dalla caverna al castello di Norm. Adesso capisco l'importanza \"strategica\" di questi luoghi.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 14:
                        FunzioniGraficheGeneriche.messaggio("Tunnel subacqueo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un passaggio segreto nei sotterranei del castello di Norm che porta al suo laboratorio principale sul fondo del lago. Nonostante le pareti del tunnel siano fatte di un materiale trasparente simile al vetro, non si riesce ad osservare chiaramente il fondale del bacino a causa delle sostanze con cui questo è stato contaminato circa 50 anni fa.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundTornaIndietro, (GlobalHWVar.gsx // 32 * 21, 0))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if primoFrame:
                FunzioniGraficheGeneriche.messaggio("Mappa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                grandezzaScritteNormali = 45
                if postiSbloccati["Casa"]:
                    FunzioniGraficheGeneriche.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                if postiSbloccati["Città"]:
                    FunzioniGraficheGeneriche.messaggio(u"Città", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                if postiSbloccati["Avamposto di Rod"]:
                    FunzioniGraficheGeneriche.messaggio("Avamposto di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                if postiSbloccati["Castello"]:
                    FunzioniGraficheGeneriche.messaggio("Castello", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                if postiSbloccati["Palazzo di Rod"]:
                    FunzioniGraficheGeneriche.messaggio("Palazzo di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                if postiSbloccati["Vulcano"]:
                    FunzioniGraficheGeneriche.messaggio("Vulcano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                if postiSbloccati["Laboratorio"]:
                    FunzioniGraficheGeneriche.messaggio("Laboratorio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                if postiSbloccati["Foresta cadetta"]:
                    FunzioniGraficheGeneriche.messaggio("Foresta cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                if postiSbloccati["Selva arida"]:
                    FunzioniGraficheGeneriche.messaggio("Selva arida", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                if postiSbloccati["Labirinto"]:
                    FunzioniGraficheGeneriche.messaggio("Labirinto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                if postiSbloccati["Passo montano"]:
                    FunzioniGraficheGeneriche.messaggio("Passo montano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                if postiSbloccati["Caverna"]:
                    FunzioniGraficheGeneriche.messaggio("Caverna", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                if postiSbloccati["Tunnel di Rod"]:
                    FunzioniGraficheGeneriche.messaggio("Tunnel di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                if postiSbloccati["Tunnel subacqueo"]:
                    FunzioniGraficheGeneriche.messaggio("Tunnel subacqueo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)

            if not voceMarcataSottoMenu:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menuDiario(dati):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.6
    xpv = xp
    ypv = yp
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = 0
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

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
            if voceMarcataSottoMenu != 0:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                voceMarcataSottoMenu = 0
                xp = xpv
                yp = ypv
            else:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                if voceMarcataSottoMenu != 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    voceMarcataSottoMenu = 0
                    xp = xpv
                    yp = ypv
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
            elif voceMarcataSottoMenu == 0:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                voceMarcataSottoMenu = 1
                xpv = xp
                ypv = yp
                if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                    xp = GlobalHWVar.gsx // 32 * 10
                    yp = GlobalHWVar.gsy // 18 * 8
            bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 1:
                        voceMarcata += 5
                        yp = GlobalHWVar.gsy // 18 * 14.6
                    elif voceMarcata == 4:
                        voceMarcata -= 1
                        yp = GlobalHWVar.gsy // 18 * 8.6
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                        if voceMarcataSottoMenu == 1:
                            voceMarcataSottoMenu += 2
                            yp = GlobalHWVar.gsy // 18 * 12
                        else:
                            voceMarcataSottoMenu -= 1
                            yp = yp - GlobalHWVar.gpy * 2
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                if voceMarcataSottoMenu == 0:
                    if voceMarcata == 6:
                        voceMarcata -= 5
                        yp = GlobalHWVar.gsy // 18 * 5.6
                    elif voceMarcata == 3:
                        voceMarcata += 1
                        yp = GlobalHWVar.gsy // 18 * 11.6
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 1.5
                else:
                    if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                        if voceMarcataSottoMenu == 3:
                            voceMarcataSottoMenu -= 2
                            yp = GlobalHWVar.gsy // 18 * 8
                        else:
                            voceMarcataSottoMenu += 1
                            yp = yp + GlobalHWVar.gpy * 2
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))

                FunzioniGraficheGeneriche.messaggio("Diario", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Oggetti speciali", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.5, 55)
                FunzioniGraficheGeneriche.messaggio("Persone incontrate", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 55)
                FunzioniGraficheGeneriche.messaggio("Nemici incontrati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, 55)
                FunzioniGraficheGeneriche.messaggio("Guida tastiera", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, 55)
                FunzioniGraficheGeneriche.messaggio("Guida mouse", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, 55)
                FunzioniGraficheGeneriche.messaggio("Guida controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.5, 55)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.6, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                if voceMarcataSottoMenu == 0:
                    GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            if voceMarcataSottoMenu != 0:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                if voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                    FunzioniGraficheGeneriche.messaggio("Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7.9, 55)
                    FunzioniGraficheGeneriche.messaggio("Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9.9, 55)
                    FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11.9, 55)
                    if voceMarcata == 4:
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.1), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 6.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7.5), 2)
                            FunzioniGraficheGeneriche.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.9), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.9), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 9.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 10.3), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 10.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.8), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.1), 2)
                            FunzioniGraficheGeneriche.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 6.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7.5), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.9), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.9), 2)
                            FunzioniGraficheGeneriche.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 9.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 10.3), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 10.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.8), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.8, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 6.9, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 7.5), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7.5), 2)
                            FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.9), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.9), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.4), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.4), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 12, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.8), 2)
                            FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.4, 35)
                    if voceMarcata == 5:
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Movimento (su casella libera) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5.6, 35)
                            FunzioniGraficheGeneriche.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.1, 35)
                            FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo (su teleImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.6, 35)
                            FunzioniGraficheGeneriche.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.1, 35)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.6), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.6), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9.9, 35)
                            FunzioniGraficheGeneriche.messaggio("Rimuovi selezione (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12), 2)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Inquadra o attacca (su casella nemica) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5.6, 35)
                            FunzioniGraficheGeneriche.messaggio("Interagisci (su casella interagibile) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.1, 35)
                            FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo (su teleImpo) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.6, 35)
                            FunzioniGraficheGeneriche.messaggio("Menu (su stato personaggio) /", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.1, 35)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento (su stato nemico)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.6), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.6), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12), 2)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13.5, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8.6), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8.6), 2)
                            FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13.5, 35)
                    if voceMarcata == 6:
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.4), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.4), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8), 2)
                            FunzioniGraficheGeneriche.messaggio("Deseleziona bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.65, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 9.55), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9.55), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.1), 2)
                            FunzioniGraficheGeneriche.messaggio("Movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.65), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.65), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.9, 35)
                        if voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 5.5, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 6.4), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6.4), 2)
                            FunzioniGraficheGeneriche.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.65, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 9.55), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9.55), 2)
                            FunzioniGraficheGeneriche.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.1), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.65), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.65), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva o disattiva Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 14.2), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 14.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Attacca / Interagisci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 14.9, 35)
                        if voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (GlobalHWVar.gsx // 32 * 20.2, GlobalHWVar.gsy // 18 * 4.8))
                            FunzioniGraficheGeneriche.messaggio("Esci (dove specificato)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 7.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 8), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 8), 2)
                            FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 8.65, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 9.55), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9.55), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 10.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 11.1), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11.1), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 11.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 20.5, GlobalHWVar.gsy // 18 * 12.65), (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.65), 2)
                            FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24.2, GlobalHWVar.gsy // 18 * 13.3, 35)

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
