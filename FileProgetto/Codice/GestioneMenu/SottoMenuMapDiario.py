# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def menuMappa(avanzamentoStoria, tutticofanetti, apriLabirinto=False):
    imgMappaNormale = GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappa"]
    imgMappaZoom = GlobalGameVar.imgDaAggiornareAvanzandoStoria["imgMappaZoom"]

    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    imgOmbreggiaturaContorniMappaMenu = GlobalImgVar.imgOmbreggiaturaContorniMappaMenu
    backgroundTornaIndietro = GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2))
    risposta = False
    aggiornaSchermo = False
    esci = False
    if apriLabirinto:
        xp = GlobalHWVar.gsx // 32 * 1
        yp = GlobalHWVar.gsy // 18 * 12.3
        voceMarcata = 10
        voceMarcataSottoMenu = True
    else:
        xp = GlobalHWVar.gsx // 32 * 1
        yp = GlobalHWVar.gsy // 18 * 4.5
        voceMarcata = 1
        voceMarcataSottoMenu = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    # carico la mappa a seconda dell'avanzamento
    imgMappaA = imgMappaNormale
    imgMappaB = imgMappaZoom
    postiSbloccati = {"Casa": False, "Città": False, "Avamposto di Rod": False, "Castello": False, "Palazzo di Rod": False, "Vulcano": False, "Laboratorio": False, "Foresta Cadetta": False, "Selva Arida": False, "Labirinto": False, "Passo Montano": False, "Tunnel di Rod": False, "Caverna": False, "Tunnel Subacqueo": False}
    if avanzamentoStoria >= 0:
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCasa"]:
            postiSbloccati["Casa"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaForestaCadetta"]:
            postiSbloccati["Foresta Cadetta"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCittà"]:
            postiSbloccati["Città"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaSelvaArida"]:
            postiSbloccati["Selva Arida"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaAvampostoDiRod"]:
            postiSbloccati["Avamposto di Rod"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLabirinto"]:
            postiSbloccati["Labirinto"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLabirintoRisolto"]:
            postiSbloccati["Labirinto"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCastello"]:
            postiSbloccati["Castello"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaScorciatoiaLabirinto"]:
            postiSbloccati["Castello"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPassoMontano"]:
            postiSbloccati["Passo Montano"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaPalazzoDiRod"]:
            postiSbloccati["Palazzo di Rod"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelDiRod"]:
            postiSbloccati["Tunnel di Rod"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaCaverna"]:
            postiSbloccati["Caverna"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaVulcano"]:
            postiSbloccati["Vulcano"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaTunnelSubacqueo"]:
            postiSbloccati["Tunnel Subacqueo"] = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["mappaLaboratorio"]:
            postiSbloccati["Laboratorio"] = True

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
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            esci = True
            bottoneDown = False
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            if voceMarcataSottoMenu:
                voceMarcataSottoMenu = False
                primoFrame = True
            else:
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
                    luogoMarcato = "Foresta Cadetta"
                if voceMarcata == 9:
                    luogoMarcato = "Selva Arida"
                if voceMarcata == 10:
                    luogoMarcato = "Labirinto"
                if voceMarcata == 11:
                    luogoMarcato = "Passo Montano"
                if voceMarcata == 12:
                    luogoMarcato = "Tunnel di Rod"
                if voceMarcata == 13:
                    luogoMarcato = "Caverna"
                if voceMarcata == 14:
                    luogoMarcato = "Tunnel Subacqueo"
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

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
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
                    GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
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
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-29), GlobalHWVar.gsy // 18 * (-1)))
                    if voceMarcata == 2:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-14.1), GlobalHWVar.gsy // 18 * (-5.5)))
                    if voceMarcata == 3:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-4), GlobalHWVar.gsy // 18 * (-15.5)))
                    if voceMarcata == 4:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (2.6), GlobalHWVar.gsy // 18 * (-24.5)))
                    if voceMarcata == 5:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (1.2), GlobalHWVar.gsy // 18 * (-4.5)))
                    if voceMarcata == 6:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (12.5), GlobalHWVar.gsy // 18 * (-3.5)))
                    if voceMarcata == 7:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-18.2), GlobalHWVar.gsy // 18 * (-25)))
                    if voceMarcata == 8:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-26.5), GlobalHWVar.gsy // 18 * (-10)))
                    if voceMarcata == 9:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-7.5), GlobalHWVar.gsy // 18 * (-13)))
                    if voceMarcata == 10:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-4.4), GlobalHWVar.gsy // 18 * (-19.7)))
                    if voceMarcata == 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-3.5), GlobalHWVar.gsy // 18 * (-5)))
                    if voceMarcata == 12:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (0.5), GlobalHWVar.gsy // 18 * (-10.5)))
                    if voceMarcata == 13:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (6.5), GlobalHWVar.gsy // 18 * (-3.5)))
                    if voceMarcata == 14:
                        GlobalHWVar.disegnaImmagineSuSchermo(imgMappa, (GlobalHWVar.gsx // 32 * (-11.5), GlobalHWVar.gsy // 18 * (-27)))
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
                    stanzaInizioCofanetti = 0
                    stanzaFineCofanetti = 0
                    if voceMarcata == 1:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["casaHansSara1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["casaHansSara4"]
                        FunzioniGraficheGeneriche.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"È l'abitazione in cui ho vissuto con la mia famiglia fin'ora. È stata costruita da un mio vecchio antenato e, da allora, è sempre stata abitata dalle varie generazioni della mia famiglia. Secondo mio padre, Hans sarà il prossimo proprietario e l'idea non lo entusiasma affatto: durante diverse discussioni Hans ha detto di non voler fare questo lavoro per tutta la vita. Dice che è monotono, faticoso e anche instabile a causa delle enormi imposte e della spietata concorrenza.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 2:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["stradaPerCittà1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["stradaPerSelvaArida2"]
                        FunzioniGraficheGeneriche.messaggio(u"Città", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Da quando ne ho sentito parlare per la prima volta, ho sempre avuto il desiderio di viverci. Da quello che so, lì a tutti è concesso scegliere quale mansione svolgere nella vita. Questo è diventato possibile grazie ai nuovi strumenti di produzione, che hanno permesso la realizzazione di un sistema in cui poche persone riescono a produrre abbastanza anche per tutte le altre. La parte di popolazione \"impoduttiva\" può quindi dedicarsi ad altre attività come musica, teatro, studio, sport e chissà cos'altro...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 3:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["avampostoDiRod1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["avampostoDiRod3"]
                        FunzioniGraficheGeneriche.messaggio("Avamposto di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Una piccola baracca che Rod esalta in maniera esagerata definendola \"avamposto\". Quella non è la sua abitazione, ma, a suo dire, un luogo fondamentale per il mantenimento dell'ecosistema cittadino. Nonostante Rod non mi abbia mai ispirato molta fiducia, i suoi ragionamenti non mi sono mai sembrati quelli di un folle esaltato... forse stava semplicemente scherzando...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 4:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["esternoCastello1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["internoCastello21"]
                        FunzioniGraficheGeneriche.messaggio("Castello", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"La più grande struttura che abbia mai visto fino ad ora. È un castello composto da almeno un centinaio di stanze, abitato da Neil e dai suoi numerosi servitori. Il vasto terreno su cui è stato costruito comprende anche l'intero labirinto, che dev'essere stato appositamente elaborato per tenere lontani i visitatori indesiderati. Il silenzio e il comportamento dei servi creano un'atmosfera cupa e surreale...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 5:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["palazzoDiRod1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["palazzoDiRod5"]
                        FunzioniGraficheGeneriche.messaggio("Palazzo di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Il palazzo in cui dimora Rod. Dentro è tutto molto disordinato, ci sono fogli e cartacce ovunque con dei suoi studi o progetti. Sembrerebbe più una specie di magazzino dove tenere un sacco di roba. Vista la polvere sugli scatoloni, non credo che utilizzi effettivamente tutti quegli oggetti. Mi domando perché non li butti... <br> L'ambiente ricorda vagamente il castello di Neil, ma un po' più piccolo e con il Passo Montano al posto del labirinto per scoraggiare l'avvicinamento di viaggiatori sconosciuti.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 6:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["sognoSara1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["sognoSara1"]
                        FunzioniGraficheGeneriche.messaggio("Vulcano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un vulcano sommerso nelle montagne a ovest della città. È simile a una montagna ma più grande e con un cratere sulla cima. A detta di Rod, da lì spesso fuoriesce del vapore incandescente. Chissà cosa c'è là dentro...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 7:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["sognoSara1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["sognoSara1"]
                        FunzioniGraficheGeneriche.messaggio("Laboratorio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Il laboratorio in cui Neil svolge le sue ricerche. È molto piccolo ma al suo interno è presente tutto ciò che serve, ossia un calcolatore di eventi, che si estende anche sotto il terreno, e diversi altri calcolatori che credo servano per gestire i sistemi di alimentazione e raffreddamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 8:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["forestaCadetta1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["forestaCadetta9"]
                        FunzioniGraficheGeneriche.messaggio("Foresta Cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"La foresta che mi ha sempre separata dalla città... non ho mai avuto il permesso di attraversarla perché i miei genitori la ritenevano troppo pericolosa per me. Il nome deriva dal fatto che viene utilizzata come terreno di prova per selezionare, tra i giovani appartenenti alla nobiltà, i futuri ufficiali dell'esercito.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 9:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["selvaArida1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["selvaArida16"]
                        FunzioniGraficheGeneriche.messaggio("Selva Arida", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Denominata in questo modo perché un tempo fitta e intricata ed ora composta soltanto da secchi abusti e funghi. Le ragioni di questo suo decadimento non sono note agli abitanti locali, ma si dà praticamente per scontato che ci sia stato un intervento umano dietro... perché qualcuno avrebbe interesse nel fare una cosa del genere?", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 10:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["labirinto1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["labirinto23"]
                        FunzioniGraficheGeneriche.messaggio("Labirinto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un enorme terreno estremamente complicato da superare a causa delle innumerevoli strade percorribili prive di punti di riferimento. Rod mi ha fornito una mappa che mostra nel dettaglio la sua struttura sconsigliandomi di procedere: è molto probabile non riuscire a uscirne, se non si ha un buon senso dell'orientamento.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 11:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["passoMontano1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["passoMontano10"]
                        FunzioniGraficheGeneriche.messaggio("Passo Montano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un passaggio tra le alture a ovest della città. In pochi mettono piede in quei territori, e quelli che lo fanno ne parlano come se fosse il posto più pericoloso al mondo. In città nessuno sa molto di quei passaggi. Alcuni mi hanno detto di aver visto diverse volte Rod arrivare da quelle parti...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 12:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["tunnelDiRod1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["tunnelDiRod3"]
                        FunzioniGraficheGeneriche.messaggio("Tunnel di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"È un passaggio sicuro e veloce tra il palazzo di Rod e il suo avamposto. Al suo interno passa un tubo molliccio che parte dal palazzo e va da qualche parte nella Selva Arida. Dev'essere di Rod, ma mi domando a che cosa serva...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 13:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["caverna1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["caverna17"]
                        FunzioniGraficheGeneriche.messaggio("Caverna Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Una caverna in mezzo alle montagne occidentali. All'interno vivono degli animali simili a Impo ma aggressivi. Da quello che ho capito, Rod era solito avventurarsi in questi cunicoli per recuperare ImpoFrutti. Probabilmente è per questo che ha deciso di costruire il suo palazzo lì accanto... per assicurarsi che nessun altro vi accedesse e tenere per sé tutto il bottino...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 14:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["sognoSara1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["sognoSara1"]
                        FunzioniGraficheGeneriche.messaggio("Tunnel Subacqueo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(u"Un passaggio segreto nei sotterranei del castello di Neil che porta al suo laboratorio principale sul fondo del lago. Nonostante le pareti del tunnel siano fatte di un materiale trasparente simile al vetro, non si riesce a osservare chiaramente il fondale del bacino a causa delle sostanze con cui questo è stato contaminato.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    cofanettiTotali = 0
                    cofanettiTrovati = 0
                    i = 0
                    while i < len(tutticofanetti):
                        if stanzaInizioCofanetti <= tutticofanetti[i] <= stanzaFineCofanetti:
                            cofanettiTotali += 1
                            if tutticofanetti[i + 3]:
                                cofanettiTrovati += 1
                        i += 4
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.cofanichiu, (GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 15.1))
                    FunzioniGraficheGeneriche.messaggio("        Cofanetti trovati: " + str(cofanettiTrovati) + "/" + str(cofanettiTotali), GlobalHWVar.grigiochi, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 15.5, grandezzaScritteDescrizioni, centrale=True)
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
                if postiSbloccati["Foresta Cadetta"]:
                    FunzioniGraficheGeneriche.messaggio("Foresta Cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                if postiSbloccati["Selva Arida"]:
                    FunzioniGraficheGeneriche.messaggio("Selva Arida", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                if postiSbloccati["Labirinto"]:
                    FunzioniGraficheGeneriche.messaggio("Labirinto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                if postiSbloccati["Passo Montano"]:
                    FunzioniGraficheGeneriche.messaggio("Passo Montano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                if postiSbloccati["Tunnel di Rod"]:
                    FunzioniGraficheGeneriche.messaggio("Tunnel di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                if postiSbloccati["Caverna"]:
                    FunzioniGraficheGeneriche.messaggio("Caverna Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                if postiSbloccati["Tunnel Subacqueo"]:
                    FunzioniGraficheGeneriche.messaggio("Tunnel Subacqueo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)

            if not voceMarcataSottoMenu:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    return esci


def menuDiario(avanzamentoStoria, listaAvanzamentoDialoghi):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.6
    xpv = xp
    ypv = yp
    risposta = False
    voceMarcata = 1
    voceMarcataSottoMenu = 0
    sottovoceSelezionata = False
    aggiornaSchermo = False
    esci = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    dictOggettiSbloccati = {"NonEsistente":False, "BicchiereConAcqua":False, "ChiaveRipostiglio":False, "ChiaveStanzaCasaDavid":False, "CertificatoResidenza":False, "ImpoPietra":False, "ChiaveStanzaCastello":False, "ListaStrumenti":False, "ChiaveAvamposto":False, "StrumentiDiRod":False, "ChiaveUfficioDiNeil":False, "ChiaveSeminterratoPalazzoRod":False}
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
        dictOggettiSbloccati["BicchiereConAcqua"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
        dictOggettiSbloccati["ChiaveRipostiglio"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
        dictOggettiSbloccati["ChiaveStanzaCasaDavid"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
        dictOggettiSbloccati["CertificatoResidenza"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoImpoPietra"]:
        dictOggettiSbloccati["ImpoPietra"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presoChiaveCameraDaLettoCastello"]:
        dictOggettiSbloccati["ChiaveStanzaCastello"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ricevutoListaStrumentiDaNeil"]:
        dictOggettiSbloccati["ListaStrumenti"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"]:
        dictOggettiSbloccati["ChiaveAvamposto"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
        dictOggettiSbloccati["StrumentiDiRod"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presaChiaveSoldatoInternoCastello20"]:
        dictOggettiSbloccati["ChiaveUfficioDiNeil"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presoChiavePianoInterratoPalazzoRod"]:
        dictOggettiSbloccati["ChiaveSeminterratoPalazzoRod"] = True

    pazzo1NumDialogo = 0
    pazzo2NumDialogo = 0
    pappagalloNumDialogo = 0
    i = 0
    while i < len(listaAvanzamentoDialoghi):
        if listaAvanzamentoDialoghi[i] == "Pazzo1-0":
            pazzo1NumDialogo = listaAvanzamentoDialoghi[i + 1]
        elif listaAvanzamentoDialoghi[i] == "Pazzo2-0":
            pazzo2NumDialogo = listaAvanzamentoDialoghi[i + 1]
        elif listaAvanzamentoDialoghi[i] == "OggettoPappaLibroSonoroMercante-0":
            pappagalloNumDialogo = listaAvanzamentoDialoghi[i + 1]
        i += 2
    pazzoNumDialogo = pazzo1NumDialogo
    if pazzo2NumDialogo != 0:
        pazzoNumDialogo = pazzo2NumDialogo
    dictPersonaggiSbloccati = {"Hans":0, "Norm":0, "Teresa":0, "Lino":0, "Sam":0, "David":0, "Olivia":0, "Rod":0, "Pazzo":0, "Rene":0, "Impo":0, "Neil":0, "Pappagallo":0, "Controllore1":0, "Controllore2":0, "Sara":0}
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
        dictPersonaggiSbloccati["Hans"] = 1
        dictPersonaggiSbloccati["Norm"] = 1
        dictPersonaggiSbloccati["Teresa"] = 1
        dictPersonaggiSbloccati["Lino"] = 1
    if GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"]:
        dictPersonaggiSbloccati["Sam"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"]:
        dictPersonaggiSbloccati["Sam"] = 2
    if GlobalGameVar.dictAvanzamentoStoria["primoDialogoDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
        dictPersonaggiSbloccati["David"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
        dictPersonaggiSbloccati["David"] = 2
    if GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoConGuardiaCasaDavid"]:
        dictPersonaggiSbloccati["Olivia"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["dialogoConGuardiaCasaDavid"]:
        dictPersonaggiSbloccati["Olivia"] = 2
    if GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerEntrareInConfraternita"]:
        dictPersonaggiSbloccati["Rod"] = 1
    elif GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerEntrareInConfraternita"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"]:
        dictPersonaggiSbloccati["Rod"] = 2
    elif GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoUscitoDalPalazzoDiRod"]:
        dictPersonaggiSbloccati["Rod"] = 3
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoUscitoDalPalazzoDiRod"]:
        dictPersonaggiSbloccati["Rod"] = 4
    if pazzoNumDialogo == 1:
        dictPersonaggiSbloccati["Pazzo"] = 1
    elif pazzoNumDialogo == 2:
        dictPersonaggiSbloccati["Pazzo"] = 2
    elif pazzoNumDialogo > 2 and not GlobalGameVar.pazzoStrabico:
        dictPersonaggiSbloccati["Pazzo"] = 3
    elif pazzoNumDialogo > 2 and GlobalGameVar.pazzoStrabico:
        dictPersonaggiSbloccati["Pazzo"] = 4
    if GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario1"]:
        dictPersonaggiSbloccati["Rene"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario1"]:
        dictPersonaggiSbloccati["Rene"] = 2
    if GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["liberatoDaiControllori"]:
        dictPersonaggiSbloccati["Impo"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["liberatoDaiControllori"]:
        dictPersonaggiSbloccati["Impo"] = 3
    if GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"]:
        dictPersonaggiSbloccati["Neil"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"]:
        dictPersonaggiSbloccati["Neil"] = 2
    if pappagalloNumDialogo >= 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
        dictPersonaggiSbloccati["Pappagallo"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
        dictPersonaggiSbloccati["Pappagallo"] = 2
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["liberatoDaiControllori"]:
        dictPersonaggiSbloccati["Controllore1"] = 1
        dictPersonaggiSbloccati["Controllore2"] = 1
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnni"]:
        dictPersonaggiSbloccati["Sara"] = 1

    dictNemiciSbloccati = {"nemiciSogno":False, "nemiciForesta":False, "nemiciCitta":False, "nemiciSelva":False, "nemiciMontagne":False, "nemiciCastello":False, "nemiciCaverna":False, "nemiciVulcano":False}
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
        dictNemiciSbloccati["nemiciSogno"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["uscitoDaForesta"]:
        dictNemiciSbloccati["nemiciForesta"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
        dictNemiciSbloccati["nemiciCitta"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelva"]:
        dictNemiciSbloccati["nemiciSelva"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["uscitoDaPassoMontano"]:
        dictNemiciSbloccati["nemiciMontagne"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
        dictNemiciSbloccati["nemiciCastello"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["arrivoIngressoVulcano"]:
        dictNemiciSbloccati["nemiciCaverna"] = True
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["liberatoDaiControllori"]:
        dictNemiciSbloccati["nemiciVulcano"] = True

    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        voceMarcataSottoMenuVecchia = voceMarcataSottoMenu
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        suFrecciaSu = False
        suFrecciaGiu = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif voceMarcataSottoMenu == 0 and GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 10:
                if GlobalHWVar.gsy // 18 * 5.1 <= yMouse <= GlobalHWVar.gsy // 18 * 6.6:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 5.6
                elif GlobalHWVar.gsy // 18 * 6.6 <= yMouse <= GlobalHWVar.gsy // 18 * 8.1:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7.1
                elif GlobalHWVar.gsy // 18 * 8.1 <= yMouse <= GlobalHWVar.gsy // 18 * 9.6:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 8.6
                elif GlobalHWVar.gsy // 18 * 14.1 <= yMouse <= GlobalHWVar.gsy // 18 * 15.6:
                    if GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(False)
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 14.6
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            elif voceMarcataSottoMenu != 0 and not sottovoceSelezionata:
                if (voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3) and GlobalHWVar.gsx // 32 * 10 <= xMouse <= GlobalHWVar.gsx // 32 * 18:
                    if GlobalHWVar.gsx // 32 * 13.5 <= xMouse <= GlobalHWVar.gsx // 32 * 14.5 and GlobalHWVar.gsy // 18 * 4 <= yMouse <= GlobalHWVar.gsy // 18 * 4.75 and ((voceMarcata == 2 and voceMarcataSottoMenu > 11) or (voceMarcata == 3 and voceMarcataSottoMenu > 11)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        suFrecciaSu = True
                    elif GlobalHWVar.gsx // 32 * 13.5 <= xMouse <= GlobalHWVar.gsx // 32 * 14.5 and GlobalHWVar.gsy // 18 * 15.75 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5 and ((voceMarcata == 2 and voceMarcataSottoMenu <= 11) or (voceMarcata == 3 and voceMarcataSottoMenu <= 22)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        suFrecciaGiu = True
                    elif GlobalHWVar.gsy // 18 * 4.75 <= yMouse <= GlobalHWVar.gsy // 18 * 5.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1:
                            voceMarcataSottoMenu = 1
                        elif voceMarcata == 2:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 1
                            else:
                                voceMarcataSottoMenu = 12
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 1
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 12
                            else:
                                voceMarcataSottoMenu = 23
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 5
                    elif GlobalHWVar.gsy // 18 * 5.75 <= yMouse <= GlobalHWVar.gsy // 18 * 6.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1:
                            voceMarcataSottoMenu = 2
                        elif voceMarcata == 2:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 2
                            else:
                                voceMarcataSottoMenu = 13
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 2
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 13
                            else:
                                voceMarcataSottoMenu = 24
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 6
                    elif GlobalHWVar.gsy // 18 * 6.75 <= yMouse <= GlobalHWVar.gsy // 18 * 7.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1:
                            voceMarcataSottoMenu = 3
                        elif voceMarcata == 2:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 3
                            else:
                                voceMarcataSottoMenu = 14
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 3
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 14
                            else:
                                voceMarcataSottoMenu = 25
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 7
                    elif GlobalHWVar.gsy // 18 * 7.75 <= yMouse <= GlobalHWVar.gsy // 18 * 8.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1:
                            voceMarcataSottoMenu = 4
                        elif voceMarcata == 2:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 4
                            else:
                                voceMarcataSottoMenu = 15
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 4
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 15
                            else:
                                voceMarcataSottoMenu = 26
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 8
                    elif GlobalHWVar.gsy // 18 * 8.75 <= yMouse <= GlobalHWVar.gsy // 18 * 9.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1:
                            voceMarcataSottoMenu = 5
                        elif voceMarcata == 2:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 5
                            else:
                                voceMarcataSottoMenu = 16
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 5
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 16
                            else:
                                voceMarcataSottoMenu = 27
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 9
                    elif GlobalHWVar.gsy // 18 * 9.75 <= yMouse <= GlobalHWVar.gsy // 18 * 10.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 6
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 6
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 17
                            else:
                                voceMarcataSottoMenu = 28
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 10
                    elif GlobalHWVar.gsy // 18 * 10.75 <= yMouse <= GlobalHWVar.gsy // 18 * 11.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 7
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 7
                            elif voceMarcataSottoMenu <= 22:
                                voceMarcataSottoMenu = 18
                            else:
                                voceMarcataSottoMenu = 29
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 11
                    elif GlobalHWVar.gsy // 18 * 11.75 <= yMouse <= GlobalHWVar.gsy // 18 * 12.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3 and voceMarcataSottoMenu <= 22)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 8
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 8
                            else:
                                voceMarcataSottoMenu = 19
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 12
                    elif GlobalHWVar.gsy // 18 * 12.75 <= yMouse <= GlobalHWVar.gsy // 18 * 13.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3 and voceMarcataSottoMenu <= 22)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 9
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 9
                            else:
                                voceMarcataSottoMenu = 20
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 13
                    elif GlobalHWVar.gsy // 18 * 13.75 <= yMouse <= GlobalHWVar.gsy // 18 * 14.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3 and voceMarcataSottoMenu <= 22)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 10
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 10
                            else:
                                voceMarcataSottoMenu = 21
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 14
                    elif GlobalHWVar.gsy // 18 * 14.75 <= yMouse <= GlobalHWVar.gsy // 18 * 15.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3 and voceMarcataSottoMenu <= 22)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 11
                        elif voceMarcata == 3:
                            if voceMarcataSottoMenu <= 11:
                                voceMarcataSottoMenu = 11
                            else:
                                voceMarcataSottoMenu = 22
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 15
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                elif voceMarcata == 4 and GlobalHWVar.gsx // 32 * 10 <= xMouse <= GlobalHWVar.gsx // 32 * 18:
                    if GlobalHWVar.gsy // 18 * 4.75 <= yMouse <= GlobalHWVar.gsy // 18 * 5.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 1
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 5
                    elif GlobalHWVar.gsy // 18 * 5.75 <= yMouse <= GlobalHWVar.gsy // 18 * 6.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 2
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 6
                    elif GlobalHWVar.gsy // 18 * 6.75 <= yMouse <= GlobalHWVar.gsy // 18 * 7.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 3
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 7
                    elif GlobalHWVar.gsy // 18 * 8.75 <= yMouse <= GlobalHWVar.gsy // 18 * 9.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 4
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 9
                    elif GlobalHWVar.gsy // 18 * 9.75 <= yMouse <= GlobalHWVar.gsy // 18 * 10.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 5
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 10
                    elif GlobalHWVar.gsy // 18 * 10.75 <= yMouse <= GlobalHWVar.gsy // 18 * 11.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 6
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 11
                    elif GlobalHWVar.gsy // 18 * 12.75 <= yMouse <= GlobalHWVar.gsy // 18 * 13.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 7
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 13
                    elif GlobalHWVar.gsy // 18 * 13.75 <= yMouse <= GlobalHWVar.gsy // 18 * 14.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 8
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 14
                    elif GlobalHWVar.gsy // 18 * 14.75 <= yMouse <= GlobalHWVar.gsy // 18 * 15.75:
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        voceMarcataSottoMenu = 9
                        xp = GlobalHWVar.gsx // 32 * 10
                        yp = GlobalHWVar.gsy // 18 * 15
                    else:
                        if not GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(True)
                else:
                    if not GlobalHWVar.mouseBloccato:
                        GlobalHWVar.configuraCursore(True)
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if (voceMarcataVecchia != voceMarcata or voceMarcataSottoMenuVecchia != voceMarcataSottoMenu) and not primoFrame:
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
            if voceMarcataSottoMenu != 0:
                if sottovoceSelezionata:
                    sottovoceSelezionata = False
                    aggiornaSchermo = True
                else:
                    voceMarcataSottoMenu = 0
                    xp = xpv
                    yp = ypv
            else:
                risposta = True
            bottoneDown = False
        if bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                bottoneDown = False
                if voceMarcataSottoMenu != 0:
                    if sottovoceSelezionata:
                        sottovoceSelezionata = False
                        aggiornaSchermo = True
                    else:
                        voceMarcataSottoMenu = 0
                        xp = xpv
                        yp = ypv
                else:
                    risposta = True
            elif bottoneDown == "mouseSinistro" and suFrecciaSu:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostapun)
                if voceMarcataSottoMenu > 22:
                    voceMarcataSottoMenu = 21
                elif voceMarcataSottoMenu > 11:
                    voceMarcataSottoMenu = 11
                xp = GlobalHWVar.gsx // 32 * 10
                yp = GlobalHWVar.gsy // 18 * 15
                bottoneDown = False
            elif bottoneDown == "mouseSinistro" and suFrecciaGiu:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostapun)
                if voceMarcataSottoMenu <= 11:
                    voceMarcataSottoMenu = 12
                elif voceMarcataSottoMenu <= 22:
                    voceMarcataSottoMenu = 23
                xp = GlobalHWVar.gsx // 32 * 10
                yp = GlobalHWVar.gsy // 18 * 5
                bottoneDown = False
            elif voceMarcataSottoMenu == 0:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                voceMarcataSottoMenu = 1
                xpv = xp
                ypv = yp
                xp = GlobalHWVar.gsx // 32 * 10
                yp = GlobalHWVar.gsy // 18 * 5
                bottoneDown = False
            elif voceMarcataSottoMenu != 0 and not sottovoceSelezionata:
                if voceMarcata == 1:
                    nomeVoceMarcataPerControllo = "NonEsistente"
                    if voceMarcataSottoMenu == 1:
                        nomeVoceMarcataPerControllo = "BicchiereConAcqua"
                    elif voceMarcataSottoMenu == 2:
                        nomeVoceMarcataPerControllo = "ChiaveRipostiglio"
                    elif voceMarcataSottoMenu == 3:
                        nomeVoceMarcataPerControllo = "ChiaveStanzaCasaDavid"
                    elif voceMarcataSottoMenu == 4:
                        nomeVoceMarcataPerControllo = "CertificatoResidenza"
                    elif voceMarcataSottoMenu == 5:
                        nomeVoceMarcataPerControllo = "ImpoPietra"
                    elif voceMarcataSottoMenu == 6:
                        nomeVoceMarcataPerControllo = "ChiaveStanzaCastello"
                    elif voceMarcataSottoMenu == 7:
                        nomeVoceMarcataPerControllo = "ListaStrumenti"
                    elif voceMarcataSottoMenu == 8:
                        nomeVoceMarcataPerControllo = "ChiaveAvamposto"
                    elif voceMarcataSottoMenu == 9:
                        nomeVoceMarcataPerControllo = "StrumentiDiRod"
                    elif voceMarcataSottoMenu == 10:
                        nomeVoceMarcataPerControllo = "ChiaveUfficioDiNeil"
                    elif voceMarcataSottoMenu == 11:
                        nomeVoceMarcataPerControllo = "ChiaveSeminterratoPalazzoRod"
                    if dictOggettiSbloccati[nomeVoceMarcataPerControllo]:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        sottovoceSelezionata = True
                        aggiornaSchermo = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 2:
                    nomeVoceMarcataPerControllo = ""
                    if voceMarcataSottoMenu == 1:
                        nomeVoceMarcataPerControllo = "Hans"
                    elif voceMarcataSottoMenu == 2:
                        nomeVoceMarcataPerControllo = "Norm"
                    elif voceMarcataSottoMenu == 3:
                        nomeVoceMarcataPerControllo = "Teresa"
                    elif voceMarcataSottoMenu == 4:
                        nomeVoceMarcataPerControllo = "Lino"
                    elif voceMarcataSottoMenu == 5:
                        nomeVoceMarcataPerControllo = "Sam"
                    elif voceMarcataSottoMenu == 6:
                        nomeVoceMarcataPerControllo = "David"
                    elif voceMarcataSottoMenu == 7:
                        nomeVoceMarcataPerControllo = "Olivia"
                    elif voceMarcataSottoMenu == 8:
                        nomeVoceMarcataPerControllo = "Rod"
                    elif voceMarcataSottoMenu == 9:
                        nomeVoceMarcataPerControllo = "Pazzo"
                    elif voceMarcataSottoMenu == 10:
                        nomeVoceMarcataPerControllo = "Rene"
                    elif voceMarcataSottoMenu == 11:
                        nomeVoceMarcataPerControllo = "Impo"
                    elif voceMarcataSottoMenu == 12:
                        nomeVoceMarcataPerControllo = "Neil"
                    elif voceMarcataSottoMenu == 13:
                        nomeVoceMarcataPerControllo = "Pappagallo"
                    elif voceMarcataSottoMenu == 14:
                        nomeVoceMarcataPerControllo = "Controllore1"
                    elif voceMarcataSottoMenu == 15:
                        nomeVoceMarcataPerControllo = "Controllore2"
                    elif voceMarcataSottoMenu == 16:
                        nomeVoceMarcataPerControllo = "Sara"
                    if dictPersonaggiSbloccati[nomeVoceMarcataPerControllo] > 0:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        sottovoceSelezionata = True
                        aggiornaSchermo = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 3:
                    nomeVoceMarcataPerControllo = ""
                    if 1 <= voceMarcataSottoMenu <= 2:
                        nomeVoceMarcataPerControllo = "nemiciSogno"
                    elif 3 <= voceMarcataSottoMenu <= 8:
                        nomeVoceMarcataPerControllo = "nemiciForesta"
                    elif 9 <= voceMarcataSottoMenu <= 10:
                        nomeVoceMarcataPerControllo = "nemiciCitta"
                    elif 11 <= voceMarcataSottoMenu <= 15:
                        nomeVoceMarcataPerControllo = "nemiciSelva"
                    elif 16 <= voceMarcataSottoMenu <= 21:
                        nomeVoceMarcataPerControllo = "nemiciMontagne"
                    elif 22 <= voceMarcataSottoMenu <= 24:
                        nomeVoceMarcataPerControllo = "nemiciCastello"
                    elif 25 <= voceMarcataSottoMenu <= 27:
                        nomeVoceMarcataPerControllo = "nemiciCaverna"
                    elif 28 <= voceMarcataSottoMenu <= 29:
                        nomeVoceMarcataPerControllo = "nemiciVulcano"
                    if dictNemiciSbloccati[nomeVoceMarcataPerControllo]:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        sottovoceSelezionata = True
                        aggiornaSchermo = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 4:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    sottovoceSelezionata = True
                    aggiornaSchermo = True
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if not sottovoceSelezionata and (bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu"):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or voceMarcataSottoMenuVecchia != voceMarcataSottoMenu or aggiornaInterfacciaPerCambioInput):
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcataSottoMenu == 0:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 3
                        yp = GlobalHWVar.gsy // 18 * 14.6
                    elif voceMarcata == 4:
                        voceMarcata -= 1
                        yp = GlobalHWVar.gsy // 18 * 8.6
                    else:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gpy * 1.5
                elif not sottovoceSelezionata:
                    if voceMarcata == 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if voceMarcataSottoMenu == 1:
                            voceMarcataSottoMenu += 10
                            yp = GlobalHWVar.gsy // 18 * 15
                        else:
                            voceMarcataSottoMenu -= 1
                            yp -= GlobalHWVar.gpy * 1
                    elif voceMarcata == 2:
                        if voceMarcataSottoMenu != 1:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            if voceMarcataSottoMenu == 12:
                                voceMarcataSottoMenu -= 1
                                yp = GlobalHWVar.gsy // 18 * 15
                            else:
                                voceMarcataSottoMenu -= 1
                                yp -= GlobalHWVar.gpy * 1
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.selimp)
                            bottoneDown = False
                    elif voceMarcata == 3:
                        if voceMarcataSottoMenu != 1:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            if voceMarcataSottoMenu == 12 or voceMarcataSottoMenu == 23:
                                voceMarcataSottoMenu -= 1
                                yp = GlobalHWVar.gsy // 18 * 15
                            else:
                                voceMarcataSottoMenu -= 1
                                yp -= GlobalHWVar.gpy * 1
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.selimp)
                            bottoneDown = False
                    elif voceMarcata == 4:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if voceMarcataSottoMenu == 1:
                            voceMarcataSottoMenu += 8
                            yp = GlobalHWVar.gsy // 18 * 15
                        elif voceMarcataSottoMenu == 4 or voceMarcataSottoMenu == 7:
                            voceMarcataSottoMenu -= 1
                            yp -= GlobalHWVar.gsy // 18 * 2
                        else:
                            voceMarcataSottoMenu -= 1
                            yp -= GlobalHWVar.gpy * 1
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcataSottoMenu == 0:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 4:
                        voceMarcata -= 3
                        yp = GlobalHWVar.gsy // 18 * 5.6
                    elif voceMarcata == 3:
                        voceMarcata += 1
                        yp = GlobalHWVar.gsy // 18 * 14.6
                    else:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gpy * 1.5
                elif not sottovoceSelezionata:
                    if voceMarcata == 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if voceMarcataSottoMenu == 11:
                            voceMarcataSottoMenu -= 10
                            yp = GlobalHWVar.gsy // 18 * 5
                        else:
                            voceMarcataSottoMenu += 1
                            yp += GlobalHWVar.gpy * 1
                    elif voceMarcata == 2:
                        if voceMarcataSottoMenu != 16:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            if voceMarcataSottoMenu == 11:
                                voceMarcataSottoMenu += 1
                                yp = GlobalHWVar.gsy // 18 * 5
                            else:
                                voceMarcataSottoMenu += 1
                                yp += GlobalHWVar.gpy * 1
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.selimp)
                            bottoneDown = False
                    elif voceMarcata == 3:
                        if voceMarcataSottoMenu != 29:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            if voceMarcataSottoMenu == 11 or voceMarcataSottoMenu == 22:
                                voceMarcataSottoMenu += 1
                                yp = GlobalHWVar.gsy // 18 * 5
                            else:
                                voceMarcataSottoMenu += 1
                                yp += GlobalHWVar.gpy * 1
                        else:
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.selimp)
                            bottoneDown = False
                    elif voceMarcata == 4:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if voceMarcataSottoMenu == 3 or voceMarcataSottoMenu == 6:
                            voceMarcataSottoMenu += 1
                            yp += GlobalHWVar.gsy // 18 * 2
                        elif voceMarcataSottoMenu == 9:
                            voceMarcataSottoMenu -= 8
                            yp = GlobalHWVar.gsy // 18 * 5
                        else:
                            voceMarcataSottoMenu += 1
                            yp += GlobalHWVar.gpy * 1
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
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
                FunzioniGraficheGeneriche.messaggio("Guida comandi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.5, 55)

                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDiarioChiusoMenu, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.6, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5, GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15))
                if voceMarcataSottoMenu == 0 or not sottovoceSelezionata:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDiarioChiusoMenu, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgDiarioApertoMenu, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
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
                if voceMarcata == 1:
                    if dictOggettiSbloccati["BicchiereConAcqua"]:
                        FunzioniGraficheGeneriche.messaggio("Bicchiere con acqua", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5, 45)
                    if dictOggettiSbloccati["ChiaveRipostiglio"]:
                        FunzioniGraficheGeneriche.messaggio("Chiave del ripostiglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6, 45)
                    if dictOggettiSbloccati["ChiaveStanzaCasaDavid"]:
                        FunzioniGraficheGeneriche.messaggio("Chiave stanza casa di David", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 7, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 7, 45)
                    if dictOggettiSbloccati["CertificatoResidenza"]:
                        FunzioniGraficheGeneriche.messaggio("Certificato di residenza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 8, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 8, 45)
                    if dictOggettiSbloccati["ImpoPietra"]:
                        FunzioniGraficheGeneriche.messaggio("ImpoPietra", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 9, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 9, 45)
                    if dictOggettiSbloccati["ChiaveStanzaCastello"]:
                        FunzioniGraficheGeneriche.messaggio("Chiave stanza castello di Neil", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 10, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 10, 45)
                    if dictOggettiSbloccati["ListaStrumenti"]:
                        FunzioniGraficheGeneriche.messaggio("Lista strumenti", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 11, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 11, 45)
                    if dictOggettiSbloccati["ChiaveAvamposto"]:
                        FunzioniGraficheGeneriche.messaggio("Chiave avamposto di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 12, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 12, 45)
                    if dictOggettiSbloccati["StrumentiDiRod"]:
                        FunzioniGraficheGeneriche.messaggio("Strumenti di Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 13, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 13, 45)
                    if dictOggettiSbloccati["ChiaveUfficioDiNeil"]:
                        FunzioniGraficheGeneriche.messaggio("Chiave ufficio di Neil", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 14, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 14, 45)
                    if dictOggettiSbloccati["ChiaveSeminterratoPalazzoRod"]:
                        FunzioniGraficheGeneriche.messaggio("Chiave del seminterrato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 15, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 15, 45)
                    if sottovoceSelezionata:
                        xImgOggetto = GlobalHWVar.gsx // 32 * 20.1
                        yImgOggetto = GlobalHWVar.gsy // 18 * 3
                        xNomeOggetto = GlobalHWVar.gsx // 32 * 25.15
                        yNomeOggetto = GlobalHWVar.gsy // 18 * 12.7
                        xDescrizioneOggetto = GlobalHWVar.gsx // 32 * 20.3
                        yDescrizioneOggetto = GlobalHWVar.gsy // 18 * 13.9
                        largezzaFoglio = GlobalHWVar.gpx * 9.7
                        spazioTraLeRighe = GlobalHWVar.gpy * 0.5
                        if voceMarcataSottoMenu == 1 and dictOggettiSbloccati["BicchiereConAcqua"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgBicchiereConAcqua, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Bicchiere con acqua", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Il bicchiere d'acqua che ho chiesto a Hans. Perché me lo sto portando dietro?", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 2 and dictOggettiSbloccati["ChiaveRipostiglio"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveRipostiglio, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Chiave del ripostiglio", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"La chiave del ripostiglio dei miei genitori. Ci sono un sacco di cose interessanti là dentro.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 3 and dictOggettiSbloccati["ChiaveStanzaCasaDavid"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveStanzaCasaDavid, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Chiave stanza casa di David", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"La chiave della mia stanza a casa di David. Credo ci siano molte altre stanze disponibili... perché non le utilizzano al posto di ammassare tutti agli alloggi profughi?", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 4 and dictOggettiSbloccati["CertificatoResidenza"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgCertificazioneResidenza, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Certificato di residenza", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Documento che dimostra la mia permanenza in città. Non capisco perché ce ne sia bisogno... non basta la mia presenza per dimostrare la mia permanenza in città?", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 5 and dictOggettiSbloccati["ImpoPietra"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgImpoPietra, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("ImpoPietra", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Una strana pietra che s'illumina premendo il piccolo pulsante che si trova nella parte superiore. Non ho ben capito perché, ma Impo è attratto quasi ipnoticamente dalla sua luce.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 6 and dictOggettiSbloccati["ChiaveStanzaCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveStanzaCastello, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Chiave stanza castello di Neil", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"La chiave della camera da letto che mi hanno assegnato nel castello di Neil.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 7 and dictOggettiSbloccati["ListaStrumenti"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgListaStrumentiStudioImpo, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Lista strumenti", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Questa busta contiene la lista degli strumenti necessari per studiare Impo. Neil mi ha incaricata di richiederli a Rod.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 8 and dictOggettiSbloccati["ChiaveAvamposto"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveAvamposto, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Chiave avamposto di Rod", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"La chiave dell'avamposto di Rod. L'ho trovata in mezzo alle sue cianfrusaglie.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 9 and dictOggettiSbloccati["StrumentiDiRod"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgStrumentiDiRod, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Strumenti di Rod", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Gli strumenti necessari per studiare Impo. Rod era sorpreso quando gli ho mostrato la lista... per qualche motivo non si aspettava che Neil li avrebbe richiesti a lui.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 10 and dictOggettiSbloccati["ChiaveUfficioDiNeil"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveUfficioNeil, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Chiave ufficio di Neil", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"La chiave dell'ufficio di Neil. Era di un soldato. Io mi sono solo difesa...", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 11 and dictOggettiSbloccati["ChiaveSeminterratoPalazzoRod"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveSeminterratoPalazzoRod, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Chiave del seminterrato", GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"La chiave di una stanza nel seminterrato del palazzo di Rod. L'ho trovata in mezzo a dei suoi appunti.", GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                elif voceMarcata == 2:
                    if voceMarcataSottoMenu <= 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 15.8))
                        if dictPersonaggiSbloccati["Hans"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Hans", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        if dictPersonaggiSbloccati["Norm"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Norm", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictPersonaggiSbloccati["Teresa"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Teresa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        if dictPersonaggiSbloccati["Lino"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Lino", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        if dictPersonaggiSbloccati["Sam"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Soldato deceduto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        if dictPersonaggiSbloccati["David"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("David", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                        if dictPersonaggiSbloccati["Olivia"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Olivia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                        if dictPersonaggiSbloccati["Rod"] == 1:
                            FunzioniGraficheGeneriche.messaggio("Ragazzo strano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        elif dictPersonaggiSbloccati["Rod"] == 2:
                            FunzioniGraficheGeneriche.messaggio("Rod", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        elif dictPersonaggiSbloccati["Rod"] == 3 or dictPersonaggiSbloccati["Rod"] == 4:
                            FunzioniGraficheGeneriche.messaggio("Rodolfo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        if dictPersonaggiSbloccati["Pazzo"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Rallo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                        if dictPersonaggiSbloccati["Rene"] == 1:
                            FunzioniGraficheGeneriche.messaggio("Bibliotecario", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        elif dictPersonaggiSbloccati["Rene"] == 2:
                            FunzioniGraficheGeneriche.messaggio(u"René", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        if dictPersonaggiSbloccati["Impo"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                    elif voceMarcataSottoMenu > 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 3.7))
                        if dictPersonaggiSbloccati["Neil"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Neil", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        if dictPersonaggiSbloccati["Pappagallo"] == 1:
                            FunzioniGraficheGeneriche.messaggio("Pappagallo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        elif dictPersonaggiSbloccati["Pappagallo"] == 2:
                            FunzioniGraficheGeneriche.messaggio("PappaLibroSonoro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictPersonaggiSbloccati["Controllore1"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Controllore 1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        if dictPersonaggiSbloccati["Controllore2"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Controllore 2", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        if dictPersonaggiSbloccati["Sara"] >= 1:
                            FunzioniGraficheGeneriche.messaggio("Sara", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                    if sottovoceSelezionata:
                        xImgPersonaggio = GlobalHWVar.gsx // 32 * 20.7
                        yImgPersonaggio = GlobalHWVar.gsy // 18 * 3.5
                        xNomePersonaggio = GlobalHWVar.gsx // 32 * 25.15
                        yNomePersonaggio = GlobalHWVar.gsy // 18 * 12.7
                        xDescrizionePersonaggio = GlobalHWVar.gsx // 32 * 20.3
                        yDescrizionePersonaggio = GlobalHWVar.gsy // 18 * 13.9
                        largezzaFoglio = GlobalHWVar.gpx * 9.7
                        spazioTraLeRighe = GlobalHWVar.gpy * 0.5
                        if voceMarcataSottoMenu == 1 and dictPersonaggiSbloccati["Hans"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.fraMaggioreDiario, (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Hans", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Mio fratello. Mi piace stare con lui, anche se in questo periodo è sempre più pensieroso e irritabile. Forse succede crescendo... Mio padre dice che si sta \"rincoglionendo\".", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 2 and dictPersonaggiSbloccati["Norm"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Padre"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Norm", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Il padrone, il governante, il capo supremo della famiglia: mio padre. Io e Hans \"dobbiamo ancora crescere\", quindi è lui l'unico illuminato da Dio per prendere le scelte giuste per tutti.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 3 and dictPersonaggiSbloccati["Teresa"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Madre"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Teresa", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Mia madre. Ascolta e ripete quello che dice mio padre. Mi sento un po' stupida e arrogante ora che l'ho pure scritto... A parte questo, si prende cura della casa e ama la sua famiglia.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 4 and dictPersonaggiSbloccati["Lino"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["CaneCasa"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Lino", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Linooo... Mio padre l'ha portato a casa circa 12 anni fa quando era ancora un cucciolo. Adesso è ben addestrato per la caccia e per tenere lontani i malintenzionati.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 5:
                            if dictPersonaggiSbloccati["Sam"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["FiglioUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Soldato deceduto", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Un soldato che ho trovato a terra martoriato nella Foresta Cadetta. L'armatura che gli ho preso lo teneva più o meno insieme... me ne sono accorta troppo tardi...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Sam"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["FiglioUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Soldato deceduto", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Quel soldato nella foresta era il figlio di David e Olivia. Non avrei dovuto rubargli l'armatura...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 6:
                            if dictPersonaggiSbloccati["David"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["PadreUfficialeServizio"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("David", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Il \"Capitano della guardia notturna\". Mi ha fatta entrare in città nonostante non ci fosse più spazio per altri profughi. Ha detto che mi ospiterà in casa sua.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["David"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["PadreUfficialeCasa"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("David", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Il capitano della guardia notturna. Mi ha ospitata solo perché voleva che gli parlassi del soldato morto nella foresta, suo figlio... Ha anche parlato di una guerra in corso...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 7:
                            if dictPersonaggiSbloccati["Olivia"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["MadreUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Olivia", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Moglie di David e madre del soldato a cui ho rubato l'armatura. Era visibilmente sconvolta durante la cena. Alla fine se n'è andata senza dire una parola.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Olivia"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["MadreUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Olivia", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Moglie di David. Ha deciso di suicidarsi... Possibile che per lei non aveva senso vivere se non per suo figlio? Cosa avrebbe fatto se non ne avesse mai avuto uno?", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 8:
                            if dictPersonaggiSbloccati["Rod"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Ragazzo strano", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Un tipo strano che ho trovato in città. Si guardava intorno di continuo, ma il suo sguardo ricadeva continuamente su una ragazza poco distante. Mi ha aiutata a trovare gli alloggi.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rod"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rod", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Un tipo losco a cui ho dato " + str(GlobalGameVar.monetePerEntrareNellaConfraternita) + u" monete per entrare nella sua \"confraternita\"... complimenti Sara. Non sembra molto affidabile, ma potrebbe rivelarsi utile in caso di necessità. Spero...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rod"] == 3:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rodolfo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Si fa chiamare Rod, penso non gli piaccia il suo nome completo. Potrei chiamarlo solo \"Olfo\"... Non sembra molto affidabile, ma devo dire che si è rivelato utile in diverse occasioni.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rod"] == 4:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rodolfo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Penso non gli piaccia il suo nome, quindi si fa chiamare \"Rod\" o semplicemente \"Olfo\". Non sembra molto affidabile, ma devo dire che si è rivelato utile in diverse occasioni.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 9:
                            if dictPersonaggiSbloccati["Pazzo"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo1"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rallo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Uno strano individuo che ho trovato in città. Parlava in maniera assurda e aveva lo sguardo perso nel vuoto.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Pazzo"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo1"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rallo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Uno strano individuo che ho trovato in città. Parlava in maniera assurda e aveva lo sguardo perso nel vuoto. Mi ha proposto di partecipare al test \"Sono Pazzo o sono Rallo\".", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Pazzo"] == 3:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo1"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rallo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Il suo nome dovrebbe essere \"Rallo\", anche se ogni volta lo pronuncia diversamente. Dà l'impressione di essere un pazzo, ma è cosciente di quello che gli accade: si è ricordato di me.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Pazzo"] == 4:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo2"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Rallo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Il suo nome dovrebbe essere \"Rallo\", anche se ogni volta lo pronuncia diversamente. Dà l'impressione di essere un pazzo, ma è cosciente di quello che gli accade: si è ricordato di me.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 10:
                            if dictPersonaggiSbloccati["Rene"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Bibliotecario"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Bibliotecario", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Gestisce la biblioteca in città. Ha deciso di aiutarmi nonostante fossi stata abbastanza molesta. Poi gli ho pure vomitato nello studio... Come fa ad avere così tanta pazienza?", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rene"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Bibliotecario"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(u"René", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Gestisce la biblioteca in città. È una persona molto interessante, le sue teorie sulla realtà sono abbastanza sconvolgenti soprattutto perché sono incredibilmente sensate.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 11:
                            if dictPersonaggiSbloccati["Impo"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Impo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"La scritta \"Impo\" è incisa sulla nuca di tutti gli animali di questa specie, assurdo! È l'ultimo della sua specie, gli altri si sono estinti dopo l'improvvisa contaminazione del lago.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Impo"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Impo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 12:
                            if dictPersonaggiSbloccati["Neil"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.neilSconosciutoDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Neil", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Un potente che, a detta di René, controlla gli spostamenti di tutta la regione. Che sia stato delegato dall'autorità cittadina? Non importa, spero che potrà aiutarmi con Hans.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Neil"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Neil"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Neil", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"È alto due metri, ha la pelle pallidissima e i suoi occhi sono sproporzionati. Credo si sia fatto delle operazioni per diventare così. A quanto pare ha centosettant'anni.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 13:
                            if dictPersonaggiSbloccati["Pappagallo"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.pappagalloDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("Pappagallo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Un pappagallo parlante che vende le stesse merci di Rod. Che faccia parte della sua \"confraternita\"? Gli è bastato vedermi per riconoscermi e darmi l'accesso al catalogo...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Pappagallo"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.pappagalloDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio("PappaLibroSonoro", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(u"Un pappagallo parlante addestrato da Rod per vendere merci. Da quello che ho capito, mi dà l'accesso al catalogo perché sono stata in qualche modo associata a un suo ricordo...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 14 and dictPersonaggiSbloccati["Controllore1"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Alieno1"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Controllore - 1", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 15 and dictPersonaggiSbloccati["Controllore2"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Alieno2"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Controllore - 2", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 16 and dictPersonaggiSbloccati["Sara"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.ralloDiario, (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Sara", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                elif voceMarcata == 3:
                    if voceMarcataSottoMenu <= 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 15.8))
                        if dictNemiciSbloccati["nemiciSogno"]:
                            FunzioniGraficheGeneriche.messaggio("Orco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("Pipistrello", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictNemiciSbloccati["nemiciForesta"]:
                            FunzioniGraficheGeneriche.messaggio("Tartaruga verde", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("Tartaruga marrone", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio("Lupo grigio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio("Lupo bianco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("Lupo nero", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio("Cinghiale", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        if dictNemiciSbloccati["nemiciCitta"] == 1:
                            FunzioniGraficheGeneriche.messaggio("Aggressore 1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio("Aggressore 2", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        if dictNemiciSbloccati["nemiciSelva"]:
                            FunzioniGraficheGeneriche.messaggio("Serpente verde", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                    elif 11 < voceMarcataSottoMenu <= 22:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 3.7))
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 15.8))
                        if dictNemiciSbloccati["nemiciSelva"]:
                            FunzioniGraficheGeneriche.messaggio("Serpente arancione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("Ragno nero", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                            FunzioniGraficheGeneriche.messaggio("Ragno rosso", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("Scorpione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        if dictNemiciSbloccati["nemiciMontagne"]:
                            FunzioniGraficheGeneriche.messaggio("Gufo marrone", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio("Gufo bianco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("Struzzo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio("Casuario", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                            FunzioniGraficheGeneriche.messaggio("Falco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio("Aquila", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        if dictNemiciSbloccati["nemiciCastello"]:
                            FunzioniGraficheGeneriche.messaggio("Servo con spada", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                    elif voceMarcataSottoMenu > 22:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 3.7))
                        if dictNemiciSbloccati["nemiciCastello"]:
                            FunzioniGraficheGeneriche.messaggio("Servo con arco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("Servo con lancia", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictNemiciSbloccati["nemiciCaverna"]:
                            FunzioniGraficheGeneriche.messaggio("Impo leggero", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("Impo volante", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio("Impo pesante", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        if dictNemiciSbloccati["nemiciVulcano"]:
                            FunzioniGraficheGeneriche.messaggio("Impo volante pesante", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("Impo torre", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                    if sottovoceSelezionata:
                        xImgPersonaggio = GlobalHWVar.gsx // 32 * 20.7
                        yImgPersonaggio = GlobalHWVar.gsy // 18 * 3.5
                        xNomePersonaggio = GlobalHWVar.gsx // 32 * 25.15
                        yNomePersonaggio = GlobalHWVar.gsy // 18 * 12.7
                        xDescrizionePersonaggio = GlobalHWVar.gsx // 32 * 20.3
                        yDescrizionePersonaggio = GlobalHWVar.gsy // 18 * 13.9
                        largezzaFoglio = GlobalHWVar.gpx * 9.7
                        spazioTraLeRighe = GlobalHWVar.gpy * 0.5
                        if voceMarcataSottoMenu == 1 and dictNemiciSbloccati["nemiciSogno"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Orco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Orco", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Dei giganteschi orchi che impugnano enormi spadoni. Mio padre ne parla spesso e ho notato che a volte alcuni racconti si contraddicono tra loro... forse non esistono veramente.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 2 and dictNemiciSbloccati["nemiciSogno"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Pipistrello"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Pipistrello", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Dei pipistrelli velenosi. Non li ho mai visti al di fuori dei miei incubi, quindi anche questi potrebbero essere un'altra invenzione di mio padre per non farmi andare nella foresta.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 3 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["TartarugaVerde"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Tartaruga verde", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Foresta Cadetta. Non è molto pericolosa in quanto si muove molto lentamente e i suoi morsi non sono per niente dolorosi.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 4 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["TartarugaMarrone"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Tartaruga marrone", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Foresta Cadetta. Un po' più forte della Tartaruga verde, ma niente di troppo proccupante. Si muove lentamente.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 5 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["LupoGrigio"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Lupo grigio", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Foresta Cadetta. Linooo... un tuo simile. Un lupo abbastanza aggressivo ma poco resistente. È abbastanza veloce, non facile da seminare.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 6 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["LupoBianco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Lupo bianco", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Foresta Cadetta. È un po' più forte e resistente del Lupo grigio. Quei pochi secondi in cui ti fissa prima di attaccharti sono gelanti.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 7 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["LupoNero"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Lupo nero", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Foresta Cadetta. La razza di lupo più forte. Nel buio della foresta, sarebbe difficile notarli se non viaggiassero in branco.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 8 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Cinghiale"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Cinghiale", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Foresta Cadetta. È un bestione grande il doppio di me. Ne ho dovuto affrontare uno e per poco non ci rimanevo secca come quel soldato...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 9 and dictNemiciSbloccati["nemiciCitta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Cittadino1"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Aggressore 1", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Non volevo ucciderlo. Aveva un tono violento, mi avrebbe stuprata... forse sarebbe stato meglio non opporsi...?", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 10 and dictNemiciSbloccati["nemiciCitta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Cittadino3"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Aggressore 2", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"L'ho ucciso prima che potesse toccarmi. Non sono una pazza assassina, voleva chiaramente farmi del male... che cazzo ho fatto...", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 11 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["SerpeVerde"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Serpente verde", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Selva Arida. Li odio, fanno molta confusione con i loro sonagli! Si muovono lentamente finché non trovano una preda, poi accelerano di colpo.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 12 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["SerpeArancio"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Serpente arancione", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Selva Arida. Questi maledetti sono velenosi! Sembrano muoversi lentamente ma, quando avvistano la preda, sono fulminei nel raggiungerla.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 13 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RagnoNero"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Ragno nero", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Selva Arida. Sono enormi, veloci e abbastanza resistenti. I loro morsi fanno abbastanza male, ma per fortuna non sono velenosi.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 14 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RagnoRosso"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Ragno rosso", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Selva Arida. Questi sono veramente i più fastidiosi. Attaccano a distanza lanciando la loro saliva velenosa. Per fortuna non sono molto resistenti.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 15 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Scorpione"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Scorpione", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nella Selva Arida. Senza dubbio la belva più temibile del posto. È forte, veloce, resistente e pure velenoso... Impossibile affrontarli in branco.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 16 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["GufoMarrone"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Gufo marrone", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nel Passo Montano. Questi gufetti sembrano tanto innoqui e amichevoli, ma, appena ti vedono, ti piombano addosso e iniziano ad artigliarti senza sosta.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 17 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["GufoBianco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Gufo bianco", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nel Passo Montano. A primo impatto, anche loro innoqui e amichevoli, ma, come i loro simili gufi marroni, sono ostili e persino più aggressivi e resistenti.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 18 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Struzzo"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Struzzo", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nel Passo Montano. Degli strani volatili che però non ho mai visto volare... immagino non possano per la loro stazza. Sono un po' goffi, ma molto forti.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 19 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Casuario"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Casuario", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nel Passo Montano. Degli struzzi un po' più bassi, tozzi e velenosi. Le loro piume nere sono unte e appiccicose, non è bello vederseli arrivare addosso.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 20 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Falco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Falco", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nel Passo Montano. Uno dei volatili più temibili. La loro apertura alare misura quasi il doppio della mia altezza. Sono veloci, aggressivi e molto resistenti.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 21 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Aquila"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Aquila", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Creatura ostile che si trova nel Passo Montano. La più pericolosa della zona. È grande circa quanto un falco, ma è più feroce e resistente. Fortunatamente non si incontra spesso.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 22 and dictNemiciSbloccati["nemiciCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["ServoSpada"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Servo con spada", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Soldato di Neil a guardia del castello. Il suo compito è stare immobile in un punto del castello. Capace di infliggere ingenti danni data la sua abilità nell'utilizzo della spada.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 23 and dictNemiciSbloccati["nemiciCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["ServoArco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Servo con arco", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Soldato di Neil a guardia del castello. Il suo compito è stare immobile in un punto del castello. Specializzato nell'uso dell'arco, attacca di continuo il nemico dalla distanza.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 24 and dictNemiciSbloccati["nemiciCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["ServoLancia"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Servo con lancia", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"Soldato di Neil a guardia del castello. Il suo compito è stare immobile in un punto del castello. Usa una lunga lancia non particolarmente efficace, ma pregna di veleno.", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 25 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboLeggero"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Impo leggero", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 26 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboVolante"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Impo volante", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 27 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboPesante"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Impo pesante", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 28 and dictNemiciSbloccati["nemiciVulcano"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboPesanteVolante"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Impo volante pesante", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 29 and dictNemiciSbloccati["nemiciVulcano"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboTorre"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Impo torre", GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(u"", GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                elif voceMarcata == 4:
                    FunzioniGraficheGeneriche.messaggio("Tastiera: Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5, 45)
                    FunzioniGraficheGeneriche.messaggio("Tastiera: Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6, 45)
                    FunzioniGraficheGeneriche.messaggio("Tastiera: Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 7, 45)
                    FunzioniGraficheGeneriche.messaggio("Mouse: Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 9, 45)
                    FunzioniGraficheGeneriche.messaggio("Mouse: Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 10, 45)
                    FunzioniGraficheGeneriche.messaggio("Mouse: Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 11, 45)
                    FunzioniGraficheGeneriche.messaggio("Controller: Mod. movimento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 13, 45)
                    FunzioniGraficheGeneriche.messaggio("Controller: Mod. interazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 14, 45)
                    FunzioniGraficheGeneriche.messaggio("Controller: Menu", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 15, 45)
                    if sottovoceSelezionata:
                        xInizioTutorialComandi = GlobalHWVar.gsx // 32 * 20.1
                        yInizioTutorialComandi = GlobalHWVar.gsy // 18 * 5.2
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Tastiera: Mod. movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 1.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), 2)
                            FunzioniGraficheGeneriche.messaggio("Deseleziona bersaglio", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.19, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), 2)
                            FunzioniGraficheGeneriche.messaggio("Movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.9, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva / Disattiva Impo", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), 2)
                            FunzioniGraficheGeneriche.messaggio("Salta turno", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), 2)
                            FunzioniGraficheGeneriche.messaggio("Interagisci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.19, 35)
                        elif voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Tastiera: Mod. interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 1.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), 2)
                            FunzioniGraficheGeneriche.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.19, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.9, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva / Disattiva Impo", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), 2)
                            FunzioniGraficheGeneriche.messaggio("Salta turno", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), 2)
                            FunzioniGraficheGeneriche.messaggio("Attacca / Interagisci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.19, 35)
                        elif voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Tastiera: Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Esci (se consentito)", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7), 2)
                            FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.1), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.1), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.6), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.6), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8), 2)
                            FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.6, 35)
                        elif voceMarcataSottoMenu == 4:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Mouse: Mod. movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Su casella libera - Movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            FunzioniGraficheGeneriche.messaggio("Su casella interagibile - Interagisci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2, 35)
                            FunzioniGraficheGeneriche.messaggio("Su ImpoPietra - Attiva / Disattiva Impo", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.7, 35)
                            FunzioniGraficheGeneriche.messaggio("Su stato personaggio - Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.2, 35)
                            FunzioniGraficheGeneriche.messaggio(u"Su stato nemico - Modalità interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7, 35)
                            FunzioniGraficheGeneriche.messaggio("Su icona \"SaltaTurno\" - Salta turno", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.1, 35)
                            FunzioniGraficheGeneriche.messaggio("Su stato nemico - Rimuovi selezione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.7, 35)
                        elif voceMarcataSottoMenu == 5:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Mouse: Mod. interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Su casella nemica - Inquadra / Attacca", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            FunzioniGraficheGeneriche.messaggio("Su casella interagibile - Interagisci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2, 35)
                            FunzioniGraficheGeneriche.messaggio("Su ImpoPietra - Attiva / Disattiva Impo", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.7, 35)
                            FunzioniGraficheGeneriche.messaggio("Su stato personaggio - Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.2, 35)
                            FunzioniGraficheGeneriche.messaggio(u"Su stato nemico - Modalità movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7, 35)
                            FunzioniGraficheGeneriche.messaggio("Su icona \"SaltaTurno\" - Salta turno", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.7, 35)
                        elif voceMarcataSottoMenu == 6:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Mouse: Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.8, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), 2)
                            FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.5, 35)
                            FunzioniGraficheGeneriche.messaggio("Esci (se consentito)", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9, 35)
                        elif voceMarcataSottoMenu == 7:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Controller: Mod. movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia bersaglio inquadrato", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.05, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), 2)
                            FunzioniGraficheGeneriche.messaggio("Deseleziona bersaglio", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), 2)
                            FunzioniGraficheGeneriche.messaggio("Movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 6.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva / Disattiva Impo", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.45, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), 2)
                            FunzioniGraficheGeneriche.messaggio("Salta turno", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.8, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), 2)
                            FunzioniGraficheGeneriche.messaggio("Interagisci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.15, 35)
                        elif voceMarcataSottoMenu == 8:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Controller: Mod. interazione", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), 2)
                            FunzioniGraficheGeneriche.messaggio("Punta sul prossimo bersaglio", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.05, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), 2)
                            FunzioniGraficheGeneriche.messaggio(u"Modalità movimento", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Inquadra bersaglio puntato", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 6.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), 2)
                            FunzioniGraficheGeneriche.messaggio("Attiva / Disattiva Impo", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.45, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), 2)
                            FunzioniGraficheGeneriche.messaggio("Salta turno", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.8, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), 2)
                            FunzioniGraficheGeneriche.messaggio("Attacca / Interagisci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.15, 35)
                        elif voceMarcataSottoMenu == 9:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio("Controller: Menu", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio("Esci (se consentito)", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2), 2)
                            FunzioniGraficheGeneriche.messaggio("Indietro / Esci", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.85, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75), 2)
                            FunzioniGraficheGeneriche.messaggio("Sposta puntatore", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.3), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.3), 2)
                            FunzioniGraficheGeneriche.messaggio("Cambia operazione (se consentito)", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 6.95, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.85), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.85), 2)
                            FunzioniGraficheGeneriche.messaggio("Seleziona", GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.5, 35)

            if sottovoceSelezionata:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    return esci
