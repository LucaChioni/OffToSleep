# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.Localizzazione.LocalizInterfaccia as LI


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
            if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padGiu" or bottoneDown == "padSu":
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
            aggiornaSchermo = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
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
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
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
                        FunzioniGraficheGeneriche.messaggio(LI.CASA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI._LAB_IN_CUI_HO_VIS_CON_LA_MIA_FAM_FIN__STA_COS_DA_UN_MIO_VEC_ANT_E_DA_ALL__SEM_STA_ABI_DAL_VAR_GEN_DEL_MIA_FAM_SEC_MIO_PAD_HAN_SAR_IL_PRO_PRO_E_LID_NON_LO_ENT_AFF_DUR_DIV_DIS_HAN_HA_DET_DI_NON_VOL_FAR_QUE_LAV_PER_TUT_LA_VIT_DIC_CHE__MON_FAT_E_ANC_INS_A_CAU_DEL_ENO_IMP_E_DEL_SPI_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 2:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["stradaPerCittà1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["stradaPerSelvaArida2"]
                        FunzioniGraficheGeneriche.messaggio(LI.CITT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.DA_QUA_NE_HO_SEN_PAR_PER_LA_PRI_VOL_HO_SEM_AVU_IL_DES_DI_VIV_DA_QUE_CHE_SO_L_A_TUT__CON_SCE_QUA_MAN_SVO_NEL_VIT_QUE__DIV_POS_GRA_AI_NUO_STR_DI_PRO_CHE_HAN_PER_LA_REA_DI_UN_SIS_IN_CUI_POC_PER_RIE_A_PRO_ABB_ANC_PER_TUT_LE_ALT_LA_PAR_DI_POP_IM_PU_QUI_DED_AD_ALT_ATT_COM_MUS_TEA_STU_SPO_E_CHI_COS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 3:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["avampostoDiRod1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["avampostoDiRod3"]
                        FunzioniGraficheGeneriche.messaggio(LI.AVA_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.UNA_PIC_BAR_CHE_ROD_ESA_IN_MAN_ESA_DEF_AV_QUE_NON__LA_SUA_ABI_MA_A_SUO_DIR_UN_LUO_FON_PER_IL_MAN_DEL_CIT_NON_ROD_NON_MI_ABB_MAI_ISP_MOL_FID_I_SUO_RAG_NON_MI_SON_MAI_SEM_QUE_DI_UN_FOL_ESA_FOR_STA_SEM_SCH[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 4:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["esternoCastello1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["internoCastello21"]
                        FunzioniGraficheGeneriche.messaggio(LI.CASTELLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.LA_PI_GRA_STR_CHE_ABB_MAI_VIS_FIN_AD_ORA__UN_CAS_COM_DA_ALM_UN_CEN_DI_STA_ABI_DA_NEI_E_DAI_SUO_NUM_SER_IL_VAS_TER_SU_CUI__STA_COS_COM_ANC_LIN_LAB_CHE_DEV_STA_APP_ELA_PER_TEN_LON_I_VIS_IND_IL_SIL_E_IL_COM_DEI_SER_CRE_UNA_CUP_E_SUR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 5:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["palazzoDiRod1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["palazzoDiRod5"]
                        FunzioniGraficheGeneriche.messaggio(LI.PAL_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.IL_PAL_IN_CUI_DIM_ROD_DEN__TUT_MOL_DIS_CI_SON_FOG_E_CAR_OVU_CON_DEI_SUO_STU_O_PRO_SEM_PI_UNA_SPE_DI_MAG_DOV_TIE_UN_SAC_DI_ROB_VIS_LA_POL_SUG_SCA_NON_CRE_CHE_UTI_EFF_TUT_QUE_OGG_MI_DOM_PER_NON_LI_BUT_BR_LAM_RIC_VAG_IL_CAS_DI_NEI_MA_UN_PO_PI_PIC_E_CON_IL_PAS_MON_AL_POS_DEL_LAB_PER_SCO_LAV_DI_VIA_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 6:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["vulcano1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["vulcano3"]
                        FunzioniGraficheGeneriche.messaggio(LI.VULCANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.UNA_MON_CON_UN_CRA_SUL_CIM_SI_TRO_A_OVE_DEL_CIT_OLT_IL_PAS_MON_LHO_VIS_ESP_MEN_USC_DAL_CAS_DI_NEI_ALL_OLT_A_UNE_DIS_DI_ACQ_INC_E_UNA_STR_ROC_CON_DEI_DIS_DI_IMP_C_UN_CAD_CHE_GIA_IN_UNA_CEL_DI_VET[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 7:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                        FunzioniGraficheGeneriche.messaggio(LI.LAB_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.IL_LAB_SEG_DI_NEI_SI_TRO_SUL_FON_DEL_LAG_NON__MOL_GRA_DEN_C_QUA_TAV_CON_DEG_APP_UN_CAL_DI_EVE_E_UNA_CEL_SIM_A_QUE_PRE_NEL_VUL_PER_EV_DA_QUE_DIM_DEN_LA_CEL_C_IL_COR_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 8:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["forestaCadetta1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["forestaCadetta9"]
                        FunzioniGraficheGeneriche.messaggio(LI.FORESTA_CADETTA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.LA_FOR_CHE_MI_HA_SEM_SEP_DAL_CIT_NON_HO_MAI_AVU_IL_PER_DI_ATT_PER_I_MIE_GEN_LA_RIT_TRO_PER_PER_ME_IL_NOM_DER_DAL_FAT_CHE_VIE_UTI_COM_TER_DI_PRO_PER_SEL_TRA_I_GIO_APP_ALL_NOB_I_FUT_UFF_DEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 9:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["selvaArida1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["selvaArida16"]
                        FunzioniGraficheGeneriche.messaggio(LI.SELVA_ARIDA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.DEN_IN_QUE_MOD_PER_UN_TEM_FIT_E_INT_ED_ORA_COM_SOL_DA_SEC_ABU_E_FUN_LE_RAG_DI_QUE_SUO_DEC_NON_SON_NOT_AGL_ABI_LOC_MA_SI_D_PRA_PER_SCO_CHE_CI_SIA_STA_UN_INT_UMA_DIE_PER_QUA_AVR_INT_NEL_FAR_UNA_COS_DEL_GEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 10:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["labirinto1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["labirinto23"]
                        FunzioniGraficheGeneriche.messaggio(LI.LABIRINTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.UN_ENO_TER_EST_COM_DA_SUP_A_CAU_DEL_INN_STR_PER_PRI_DI_PUN_DI_RIF_ROD_MI_HA_FOR_UNA_MAP_CHE_MOS_NEL_DET_LA_SUA_STR_SCO_DI_PRO__MOL_PRO_NON_RIU_A_USC_SE_NON_SI_HA_UN_BUO_SEN_DEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 11:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["passoMontano1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["passoMontano10"]
                        FunzioniGraficheGeneriche.messaggio(LI.PASSO_MONTANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.UN_PAS_TRA_LE_ALT_A_OVE_DEL_CIT_IN_POC_MET_PIE_IN_QUE_TER_E_QUE_CHE_LO_FAN_NE_PAR_COM_SE_FOS_IL_POS_PI_PER_AL_MON_IN_CIT_NES_SA_MOL_DI_QUE_PAS_ALC_MI_HAN_DET_DI_AVE_VIS_DIV_VOL_ROD_ARR_DA_QUE_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 12:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["tunnelDiRod1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["tunnelDiRod3"]
                        FunzioniGraficheGeneriche.messaggio(LI.TUN_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI._UN_PAS_SIC_E_VEL_TRA_IL_PAL_DI_ROD_E_IL_SUO_AVA_AL_SUO_INT_PAS_UN_TUB_MOL_CHE_PAR_DAL_PAL_E_VA_DA_QUA_PAR_NEL_SEL_ARI_DEV_DI_ROD_MA_MI_DOM_A_CHE_COS_SER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 13:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["caverna1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["caverna18"]
                        FunzioniGraficheGeneriche.messaggio(LI.CAVERNA_IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.UNA_CAV_IN_MEZ_ALL_MON_OCC_ALL_VIV_DEG_ANI_SIM_A_IMP_MA_AGG_DA_QUE_CHE_HO_CAP_ROD_ERA_SOL_AVV_IN_QUE_CUN_PER_REC_IMP_PRO__PER_QUE_CHE_HA_DEC_DI_COS_IL_SUO_PAL_L_ACC_PER_ASS_CHE_NES_ALT_VI_ACC_E_TEN_PER_S_TUT_IL_BOT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                    if voceMarcata == 14:
                        stanzaInizioCofanetti = GlobalGameVar.dictStanze["tunnelSubacqueo1"]
                        stanzaFineCofanetti = GlobalGameVar.dictStanze["tunnelSubacqueo2"]
                        FunzioniGraficheGeneriche.messaggio(LI.TUNNEL_SUBACQUEO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 70)
                        FunzioniGraficheGeneriche.messaggio(LI.UN_PAS_SEG_NEI_SOT_DEL_CAS_DI_NEI_CHE_POR_AL_SUO_LAB_PRI_SUL_FON_DEL_LAG_NON_LE_PAR_DEL_TUN_SIA_FAT_DI_UN_MAT_TRA_SIM_AL_VET_NON_SI_RIE_A_OSS_CHI_IL_FON_DEL_BAC_A_CAU_DEL_SOS_CON_CUI__STA_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.5, GlobalHWVar.gsy // 18 * 6.5, grandezzaScritteDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
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
                    FunzioniGraficheGeneriche.messaggio(LI.________COF_TRO___STR__[GlobalHWVar.linguaImpostata] %(cofanettiTrovati, cofanettiTotali), GlobalHWVar.grigiochi, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 15.5, grandezzaScritteDescrizioni, centrale=True)
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaImmagineSuSchermo(backgroundTornaIndietro, (GlobalHWVar.gsx // 32 * 21, 0))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)

            if primoFrame:
                FunzioniGraficheGeneriche.messaggio(LI.MAPPA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                grandezzaScritteNormali = 45
                if postiSbloccati["Casa"]:
                    FunzioniGraficheGeneriche.messaggio(LI.CASA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.5, grandezzaScritteNormali)
                if postiSbloccati["Città"]:
                    FunzioniGraficheGeneriche.messaggio(LI.CITT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.3, grandezzaScritteNormali)
                if postiSbloccati["Avamposto di Rod"]:
                    FunzioniGraficheGeneriche.messaggio(LI.AVA_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, grandezzaScritteNormali)
                if postiSbloccati["Castello"]:
                    FunzioniGraficheGeneriche.messaggio(LI.CASTELLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.9, grandezzaScritteNormali)
                if postiSbloccati["Palazzo di Rod"]:
                    FunzioniGraficheGeneriche.messaggio(LI.PAL_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.7, grandezzaScritteNormali)
                if postiSbloccati["Vulcano"]:
                    FunzioniGraficheGeneriche.messaggio(LI.VULCANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, grandezzaScritteNormali)
                if postiSbloccati["Laboratorio"]:
                    FunzioniGraficheGeneriche.messaggio(LI.LAB_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.3, grandezzaScritteNormali)
                if postiSbloccati["Foresta Cadetta"]:
                    FunzioniGraficheGeneriche.messaggio(LI.FORESTA_CADETTA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.7, grandezzaScritteNormali)
                if postiSbloccati["Selva Arida"]:
                    FunzioniGraficheGeneriche.messaggio(LI.SELVA_ARIDA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.5, grandezzaScritteNormali)
                if postiSbloccati["Labirinto"]:
                    FunzioniGraficheGeneriche.messaggio(LI.LABIRINTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.3, grandezzaScritteNormali)
                if postiSbloccati["Passo Montano"]:
                    FunzioniGraficheGeneriche.messaggio(LI.PASSO_MONTANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, grandezzaScritteNormali)
                if postiSbloccati["Tunnel di Rod"]:
                    FunzioniGraficheGeneriche.messaggio(LI.TUN_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.9, grandezzaScritteNormali)
                if postiSbloccati["Caverna"]:
                    FunzioniGraficheGeneriche.messaggio(LI.CAVERNA_IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.7, grandezzaScritteNormali)
                if postiSbloccati["Tunnel Subacqueo"]:
                    FunzioniGraficheGeneriche.messaggio(LI.TUNNEL_SUBACQUEO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.5, grandezzaScritteNormali)
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
    dictPersonaggiSbloccati = {"Hans":0, "Norm":0, "Teresa":0, "Lino":0, "Sam":0, "David":0, "Olivia":0, "Rod":0, "Pazzo":0, "Rene":0, "Impo":0, "Neil":0, "Pappagallo":0, "Costruttore":0, "Sara":0}
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
    if GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["scopertoNaturaDegliImpo"]:
        dictPersonaggiSbloccati["Impo"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["scopertoNaturaDegliImpo"]:
        dictPersonaggiSbloccati["Impo"] = 2
    if GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"]:
        dictPersonaggiSbloccati["Neil"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"]:
        dictPersonaggiSbloccati["Neil"] = 2
    if pappagalloNumDialogo >= 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
        dictPersonaggiSbloccati["Pappagallo"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
        dictPersonaggiSbloccati["Pappagallo"] = 2
    if GlobalGameVar.dictAvanzamentoStoria["vistoCostruttoreInLaboratorioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
        dictPersonaggiSbloccati["Costruttore"] = 1
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
        dictPersonaggiSbloccati["Costruttore"] = 2
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
        dictPersonaggiSbloccati["Sara"] = 1

    dictNemiciSbloccati = {"nemiciSogno":False, "nemiciForesta":False, "nemiciCitta":False, "nemiciSelva":False, "nemiciMontagne":False, "nemiciCastello":False, "nemiciCaverna":False}
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
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["monologoArrivoUltimaStanzaCavernaImpo"]:
        dictNemiciSbloccati["nemiciCaverna"] = True

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
            if GlobalHWVar.gsx // 32 * 22.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
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
                    elif GlobalHWVar.gsy // 18 * 8.75 <= yMouse <= GlobalHWVar.gsy // 18 * 9.75 and (((voceMarcata == 1 or voceMarcata == 2) and voceMarcataSottoMenu <= 11) or (voceMarcata == 3)):
                        if GlobalHWVar.mouseBloccato:
                            GlobalHWVar.configuraCursore(False)
                        if voceMarcata == 1 or voceMarcata == 2:
                            voceMarcataSottoMenu = 5
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
        if bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["Q"] or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
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
                        nomeVoceMarcataPerControllo = "Costruttore"
                    elif voceMarcataSottoMenu == 15:
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
                    elif 25 <= voceMarcataSottoMenu <= 29:
                        nomeVoceMarcataPerControllo = "nemiciCaverna"
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
        if not sottovoceSelezionata and (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padGiu" or bottoneDown == "padSu"):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or voceMarcataSottoMenuVecchia != voceMarcataSottoMenu or aggiornaInterfacciaPerCambioInput):
            aggiornaSchermo = False
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["W"] or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
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
            if (bottoneDown == GlobalHWVar.tastiConfiguratiTastiera["S"] or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
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
                        if voceMarcataSottoMenu != 15:
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

                FunzioniGraficheGeneriche.messaggio(LI.DIARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio(LI.OGGETTI_SPECIALI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5.5, 55)
                FunzioniGraficheGeneriche.messaggio(LI.PERSONE_INCONTRATE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, 55)
                FunzioniGraficheGeneriche.messaggio(LI.NEMICI_INCONTRATI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.5, 55)
                FunzioniGraficheGeneriche.messaggio(LI.GUIDA_COMANDI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.5, 55)

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
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_DES_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio(LI.B_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio(LI.Q_TOR_IND[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 1, 50, centrale=True)

            if voceMarcataSottoMenu != 0:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscurino, (GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xpv, ypv))
                if voceMarcata == 1:
                    if dictOggettiSbloccati["BicchiereConAcqua"]:
                        FunzioniGraficheGeneriche.messaggio(LI.BIC_CON_ACQ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5, 45)
                    if dictOggettiSbloccati["ChiaveRipostiglio"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CHI_DEL_RIP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6, 45)
                    if dictOggettiSbloccati["ChiaveStanzaCasaDavid"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CHI_STA_CAS_DI_DAV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 7, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 7, 45)
                    if dictOggettiSbloccati["CertificatoResidenza"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CER_DI_RES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 8, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 8, 45)
                    if dictOggettiSbloccati["ImpoPietra"]:
                        FunzioniGraficheGeneriche.messaggio(LI.IMPOPIETRA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 9, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 9, 45)
                    if dictOggettiSbloccati["ChiaveStanzaCastello"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CHI_STA_CAS_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 10, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 10, 45)
                    if dictOggettiSbloccati["ListaStrumenti"]:
                        FunzioniGraficheGeneriche.messaggio(LI.LISTA_STRUMENTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 11, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 11, 45)
                    if dictOggettiSbloccati["ChiaveAvamposto"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CHI_AVA_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 12, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 12, 45)
                    if dictOggettiSbloccati["StrumentiDiRod"]:
                        FunzioniGraficheGeneriche.messaggio(LI.STR_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 13, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 13, 45)
                    if dictOggettiSbloccati["ChiaveUfficioDiNeil"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CHI_UFF_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 14, 45)
                    else:
                        FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 14, 45)
                    if dictOggettiSbloccati["ChiaveSeminterratoPalazzoRod"]:
                        FunzioniGraficheGeneriche.messaggio(LI.CHI_DEL_SEM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 15, 45)
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
                            FunzioniGraficheGeneriche.messaggio(LI.BIC_CON_ACQ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.IL_BIC_DAC_CHE_HO_CHI_A_HAN_PER_ME_LO_STO_POR_DIE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 2 and dictOggettiSbloccati["ChiaveRipostiglio"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveRipostiglio, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CHI_DEL_RIP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LA_CHI_DEL_RIP_DEI_MIE_GEN_CI_SON_UN_SAC_DI_COS_INT_L_DEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 3 and dictOggettiSbloccati["ChiaveStanzaCasaDavid"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveStanzaCasaDavid, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CHI_STA_CAS_DI_DAV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LA_CHI_DEL_MIA_STA_A_CAS_DI_DAV_CRE_CI_SIA_MOL_ALT_STA_DIS_PER_NON_LE_UTI_AL_POS_DI_AMM_TUT_AGL_ALL_PRO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 4 and dictOggettiSbloccati["CertificatoResidenza"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgCertificazioneResidenza, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CER_DI_RES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.DOC_CHE_DIM_LA_MIA_PER_IN_CIT_NON_CAP_PER_CE_NE_SIA_BIS_NON_BAS_LA_MIA_PRE_PER_DIM_LA_MIA_PER_IN_CIT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 5 and dictOggettiSbloccati["ImpoPietra"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgImpoPietra, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPOPIETRA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.UNA_STR_PIE_CHE_SIL_PRE_IL_PIC_PUL_CHE_SI_TRO_NEL_PAR_SUP_NON_HO_BEN_CAP_PER_MA_IMP__ATT_QUA_IPN_DAL_SUA_LUC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 6 and dictOggettiSbloccati["ChiaveStanzaCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveStanzaCastello, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CHI_STA_CAS_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LA_CHI_DEL_CAM_DA_LET_CHE_MI_HAN_ASS_NEL_CAS_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 7 and dictOggettiSbloccati["ListaStrumenti"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgListaStrumentiStudioImpo, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.LISTA_STRUMENTI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.QUE_BUS_CON_LA_LIS_DEG_STR_NEC_PER_STU_IMP_NEI_MI_HA_INC_DI_RIC_A_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 8 and dictOggettiSbloccati["ChiaveAvamposto"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveAvamposto, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CHI_AVA_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LA_CHI_DEL_DI_ROD_LHO_TRO_IN_MEZ_ALL_SUE_CIA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 9 and dictOggettiSbloccati["StrumentiDiRod"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgStrumentiDiRod, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.STR_DI_ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.GLI_STR_NEC_PER_STU_IMP_ROD_ERA_SOR_QUA_GLI_HO_MOS_LA_LIS_PER_QUA_MOT_NON_SI_ASP_CHE_NEI_LI_AVR_RIC_A_LUI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 10 and dictOggettiSbloccati["ChiaveUfficioDiNeil"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveUfficioNeil, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CHI_UFF_DI_NEI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LA_CHI_DEL_DI_NEI_ERA_DI_UN_SOL_IO_MI_SON_SOL_DIF[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 11 and dictOggettiSbloccati["ChiaveSeminterratoPalazzoRod"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgChiaveSeminterratoPalazzoRod, (xImgOggetto, yImgOggetto))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizioneOggetto, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), (xDescrizioneOggetto + largezzaFoglio, yDescrizioneOggetto - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CHI_DEL_SEM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomeOggetto, yNomeOggetto, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LA_CHI_DI_UNA_STA_NEL_SEM_DEL_PAL_DI_ROD_LHO_TRO_IN_MEZ_A_DEI_SUO_APP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizioneOggetto, yDescrizioneOggetto, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                elif voceMarcata == 2:
                    if voceMarcataSottoMenu <= 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 15.8))
                        if dictPersonaggiSbloccati["Hans"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.HANS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        if dictPersonaggiSbloccati["Norm"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.NORM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictPersonaggiSbloccati["Teresa"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.TERESA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        if dictPersonaggiSbloccati["Lino"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.LINO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        if dictPersonaggiSbloccati["Sam"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.SOLDATO_DECEDUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                        if dictPersonaggiSbloccati["David"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.DAVID[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                        if dictPersonaggiSbloccati["Olivia"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.OLIVIA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                        if dictPersonaggiSbloccati["Rod"] == 1:
                            FunzioniGraficheGeneriche.messaggio(LI.RAGAZZO_STRANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        elif dictPersonaggiSbloccati["Rod"] == 2:
                            FunzioniGraficheGeneriche.messaggio(LI.ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        elif dictPersonaggiSbloccati["Rod"] == 3 or dictPersonaggiSbloccati["Rod"] == 4:
                            FunzioniGraficheGeneriche.messaggio(LI.RODOLFO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        if dictPersonaggiSbloccati["Pazzo"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.RALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                        if dictPersonaggiSbloccati["Rene"] == 1:
                            FunzioniGraficheGeneriche.messaggio(LI.BIBLIOTECARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        elif dictPersonaggiSbloccati["Rene"] == 2:
                            FunzioniGraficheGeneriche.messaggio(LI.REN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        if dictPersonaggiSbloccati["Impo"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                    elif voceMarcataSottoMenu > 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 3.7))
                        if dictPersonaggiSbloccati["Neil"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.NEIL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                        if dictPersonaggiSbloccati["Pappagallo"] == 1:
                            FunzioniGraficheGeneriche.messaggio(LI.PAPPAGALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        elif dictPersonaggiSbloccati["Pappagallo"] == 2:
                            FunzioniGraficheGeneriche.messaggio(LI.PAPPALIBROSONORO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictPersonaggiSbloccati["Costruttore"] == 1:
                            FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        elif dictPersonaggiSbloccati["Costruttore"] == 2:
                            FunzioniGraficheGeneriche.messaggio(LI.COSTRUTTORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                        if dictPersonaggiSbloccati["Sara"] >= 1:
                            FunzioniGraficheGeneriche.messaggio(LI.SARA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
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
                            FunzioniGraficheGeneriche.messaggio(LI.HANS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.MIO_FRA_MI_PIA_STA_CON_LUI_ANC_SE_IN_QUE_PER__SEM_PI_PEN_E_IRR_FOR_SUC_CRE_MIO_PAD_DIC_CHE_SI_STA_RI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 2 and dictPersonaggiSbloccati["Norm"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Padre"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.NORM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.IL_PAD_IL_GOV_IL_CAP_SUP_DEL_FAM_MIO_PAD_IO_E_HAN_DO_ANC_CRE_QUI__LUI_LUN_ILL_DA_DIO_PER_PRE_LE_SCE_GIU_PER_TUT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 3 and dictPersonaggiSbloccati["Teresa"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Madre"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.TERESA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.MIA_MAD_ASC_E_RIP_QUE_CHE_DIC_MIO_PAD_MI_SEN_UN_PO_STU_E_ARR_ORA_CHE_LHO_PUR_SCR_A_PAR_QUE_SI_PRE_CUR_DEL_CAS_E_AMA_LA_SUA_FAM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 4 and dictPersonaggiSbloccati["Lino"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["CaneCasa"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.LINO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LIN_MIO_PAD_LHA_POR_A_CAS_CIR_5_ANN_FA_QUA_ERA_ANC_UN_CUC_ADE__BEN_ADD_PER_LA_CAC_E_PER_TEN_LON_I_MAL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 5:
                            if dictPersonaggiSbloccati["Sam"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["FiglioUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.SOLDATO_DECEDUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UN_SOL_CHE_HO_TRO_A_TER_MAR_NEL_FOR_CAD_LAR_CHE_GLI_HO_PRE_LO_TEN_PI_O_MEN_INS_ME_NE_SON_ACC_TRO_TAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Sam"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["FiglioUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.SOLDATO_DECEDUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.QUE_SOL_NEL_FOR_ERA_IL_FIG_DI_DAV_E_OLI_NON_AVR_DOV_RUB_LAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 6:
                            if dictPersonaggiSbloccati["David"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["PadreUfficialeServizio"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.DAVID[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.IL_CA_DEL_GUA_NOT_MI_HA_FAT_ENT_IN_CIT_NON_NON_CI_FOS_PI_SPA_PER_ALT_PRO_HA_DET_CHE_MI_OSP_IN_CAS_SUA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["David"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["PadreUfficialeCasa"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.DAVID[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.IL_CAP_DEL_GUA_NOT_MI_HA_OSP_SOL_PER_VOL_CHE_GLI_PAR_DEL_SOL_MOR_NEL_FOR_SUO_FIG_HA_ANC_PAR_DI_UNA_GUE_IN_COR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 7:
                            if dictPersonaggiSbloccati["Olivia"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["MadreUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.OLIVIA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.MOG_DI_DAV_E_MAD_DEL_SOL_A_CUI_HO_RUB_LAR_ERA_VIS_SCO_DUR_LA_CEN_ALL_FIN_SE_N_AND_SEN_DIR_UNA_PAR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Olivia"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["MadreUfficiale"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.OLIVIA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.MOG_DI_DAV_HA_DEC_DI_SUI_POS_CHE_PER_LEI_NON_AVE_SEN_VIV_SE_NON_PER_SUO_FIG_COS_AVR_FAT_SE_NON_NE_AVE_MAI_AVU_UNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 8:
                            if dictPersonaggiSbloccati["Rod"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RAGAZZO_STRANO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UN_TIP_STR_CHE_HO_TRO_IN_CIT_SI_GUA_INT_DI_CON_MA_IL_SUO_SGU_RIC_CON_SU_UNA_RAG_POC_DIS_MI_HA_AIU_A_TRO_GLI_ALL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rod"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.ROD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UN_TIP_LOS_A_CUI_HO_DAT___STR__U_MON_PER_ENT_NEL_SUA_CO_COM_SAR_NON_SEM_MOL_AFF_MA_POT_RIV_UTI_IN_CAS_DI_NEC_SPE[GlobalHWVar.linguaImpostata] %GlobalGameVar.monetePerEntrareNellaConfraternita, GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rod"] == 3:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RODOLFO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.SI_FA_CHI_ROD_PEN_NON_GLI_PIA_IL_SUO_NOM_COM_POT_CHI_SOL_OL_NON_SEM_MOL_AFF_MA_DEV_DIR_CHE_SI__RIV_UTI_IN_DIV_OCC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rod"] == 4:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Mercante"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RODOLFO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.PEN_NON_GLI_PIA_IL_SUO_NOM_QUI_SI_FA_CHI_RO_O_SEM_OL_NON_SEM_MOL_AFF_MA_DEV_DIR_CHE_SI__RIV_UTI_IN_DIV_OCC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 9:
                            if dictPersonaggiSbloccati["Pazzo"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo1"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UNO_STR_IND_CHE_HO_TRO_IN_CIT_PAR_IN_MAN_ASS_E_AVE_LO_SGU_PER_NEL_VUO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Pazzo"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo1"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UNO_STR_IND_CHE_HO_TRO_IN_CIT_PAR_IN_MAN_ASS_E_AVE_LO_SGU_PER_NEL_VUO_MI_HA_PRO_DI_PAR_AL_TES_SO_PAZ_O_SON_RAL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Pazzo"] == 3:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo1"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.IL_SUO_NOM_DOV_ESS_RA_ANC_SE_OGN_VOL_LO_PRO_DIV_D_LIM_DI_ESS_UN_PAZ_MA__COS_DI_QUE_CHE_GLI_ACC_SI__RIC_DI_ME[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Pazzo"] == 4:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Pazzo2"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.RALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.IL_SUO_NOM_DOV_ESS_RA_ANC_SE_OGN_VOL_LO_PRO_DIV_D_LIM_DI_ESS_UN_PAZ_MA__COS_DI_QUE_CHE_GLI_ACC_SI__RIC_DI_ME[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 10:
                            if dictPersonaggiSbloccati["Rene"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Bibliotecario"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.BIBLIOTECARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.GES_LA_BIB_IN_CIT_HA_DEC_DI_AIU_NON_FOS_STA_ABB_MOL_POI_GLI_HO_PUR_VOM_NEL_STU_COM_FA_AD_AVE_COS_TAN_PAZ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            if dictPersonaggiSbloccati["Rene"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Bibliotecario"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.REN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.GES_LA_BIB_IN_CIT__UNA_PER_MOL_INT_LE_SUE_TEO_SUL_REA_SON_ABB_SCO_SOP_PER_SON_INC_SEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 11:
                            if dictPersonaggiSbloccati["Impo"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.LA_SCR_IM__INC_SUL_NUC_DI_TUT_GLI_ANI_DI_QUE_SPE_ASS__LUL_DEL_SUA_SPE_GLI_ALT_SI_SON_EST_POC_PRI_CHE_IL_LAG_SI_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Impo"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.roboDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.IMPO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.MOL_PRO_SON_STA_PRO_DAL_COS_LA_LOR_FUN__QUE_DI_MAN_IN_ATT_IL_CAL_NEL_VUL_E_PRO_CI_CHE_QUE_RIC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 12:
                            if dictPersonaggiSbloccati["Neil"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.neilSconosciutoDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.NEIL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UN_POT_CHE_A_DET_DI_REN_CON_GLI_SPO_DI_TUT_LA_REG_CHE_SIA_STA_DEL_DAL_CIT_NON_IMP_SPE_CHE_POT_AIU_CON_HAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Neil"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Neil"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.NEIL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI._ALT_DUE_MET_HA_LA_PEL_PAL_E_I_SUO_OCC_SON_SPR_CRE_SI_SIA_FAT_DEL_OPE_PER_DIV_COS_A_QUA_PAR_HA_CEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 13:
                            if dictPersonaggiSbloccati["Pappagallo"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.pappagalloDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.PAPPAGALLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UN_PAP_PAR_CHE_VEN_LE_STE_MER_DI_ROD_CHE_FAC_PAR_DEL_SUA_CO_GLI__BAS_VED_PER_RIC_E_DAR_LAC_AL_CAT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Pappagallo"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.pappagalloDiario, (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.PAPPALIBROSONORO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.UN_PAP_PAR_ADD_DA_ROD_PER_VEN_MER_DA_QUE_CHE_HO_CAP_MI_D_LAC_AL_CAT_PER_SON_STA_IN_QUA_MOD_ASS_A_UN_SUO_RIC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 14:
                            if dictPersonaggiSbloccati["Costruttore"] == 1:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Costruttore"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.SCONOSCIUTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI._UN_TIZ_CHE_HO_TRO_MOR_DEN_UNA_CEL_NEL_CAV_IMP_IND_UNA_STR_TUT_E_HA_DEI_TUB_CHE_GLI_ESC_DAL_COR_MI_DOM_COS_CI_FAC_L_DEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                            elif dictPersonaggiSbloccati["Costruttore"] == 2:
                                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgPersonaggiDiario["Costruttore"], (xImgPersonaggio, yImgPersonaggio))
                                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                                FunzioniGraficheGeneriche.messaggio(LI.COSTRUTTORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                                FunzioniGraficheGeneriche.messaggio(LI.LUI__COL_CHE_HA_MAN_APE_E_IN_EQU_IL_CON_TRA_NOI_E_IL_NEM_NEI_IPO_CHE_VOL_IMP_ALL_DEL_RIC_INT_E_CON_IN_AMB_BEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 15 and dictPersonaggiSbloccati["Sara"] == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.imgProtagonistaDiario, (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SARA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.POT_POR_AVA_LE_RIC_DI_ROD_MA_CHE_SEN_HA_SON_ANC_IO_BR_FOR_NON_HA_SEN_NEA_POR_IL_PRO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                elif voceMarcata == 3:
                    if voceMarcataSottoMenu <= 11:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 15.8))
                        if dictNemiciSbloccati["nemiciSogno"]:
                            FunzioniGraficheGeneriche.messaggio(LI.ORCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.PIPISTRELLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictNemiciSbloccati["nemiciForesta"]:
                            FunzioniGraficheGeneriche.messaggio(LI.TARTARUGA_VERDE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.TARTARUGA_MARRONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.LUPO_GRIGIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.LUPO_BIANCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.LUPO_NERO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.CINGHIALE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                        if dictNemiciSbloccati["nemiciCitta"] == 1:
                            FunzioniGraficheGeneriche.messaggio(LI.AGGRESSORE_1[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.AGGRESSORE_2[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        if dictNemiciSbloccati["nemiciSelva"]:
                            FunzioniGraficheGeneriche.messaggio(LI.SERPENTE_VERDE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                    elif 11 < voceMarcataSottoMenu <= 22:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 3.7))
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriGiu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 15.8))
                        if dictNemiciSbloccati["nemiciSelva"]:
                            FunzioniGraficheGeneriche.messaggio(LI.SERPENTE_ARANCIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.RAGNO_NERO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.RAGNO_ROSSO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.SCORPIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                        if dictNemiciSbloccati["nemiciMontagne"]:
                            FunzioniGraficheGeneriche.messaggio(LI.GUFO_MARRONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.GUFO_BIANCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.STRUZZO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.CASUARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.FALCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.AQUILA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, 45)
                        if dictNemiciSbloccati["nemiciCastello"]:
                            FunzioniGraficheGeneriche.messaggio(LI.SER_CON_SPA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 45)
                    elif voceMarcataSottoMenu > 22:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.scorriSu, (GlobalHWVar.gpx * 13.5, GlobalHWVar.gpy * 3.7))
                        if dictNemiciSbloccati["nemiciCastello"]:
                            FunzioniGraficheGeneriche.messaggio(LI.SER_CON_ARC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.SER_CON_LAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, 45)
                        if dictNemiciSbloccati["nemiciCaverna"]:
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_LEGGERO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_VOLANTE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_PESANTE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.IMP_VOL_PES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, 45)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_TORRE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, 45)
                        else:
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, 45)
                            FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, 45)
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
                            FunzioniGraficheGeneriche.messaggio(LI.ORCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.DEI_GIG_ORC_CHE_IMP_ENO_SPA_MIO_PAD_NE_PAR_SPE_E_HO_NOT_CHE_A_VOL_ALC_RAC_SI_CON_TRA_LOR_FOR_NON_ESI_VER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 2 and dictNemiciSbloccati["nemiciSogno"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Pipistrello"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.PIPISTRELLO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.DEI_PIP_VEL_NON_LI_HO_MAI_VIS_AL_DI_FUO_DEI_MIE_INC_QUI_ANC_QUE_POT_ESS_UNA_INV_DI_MIO_PAD_PER_NON_FAR_AND_NEL_FOR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 3 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["TartarugaVerde"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.TARTARUGA_VERDE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_FOR_CAD_NON__MOL_PER_IN_QUA_SI_MUO_MOL_LEN_E_I_SUO_MOR_NON_SON_PER_NIE_DOL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 4 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["TartarugaMarrone"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.TARTARUGA_MARRONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_FOR_CAD_UN_PO_PI_FOR_DEL_TAR_VER_MA_NIE_DI_TRO_PRE_SI_MUO_LEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 5 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["LupoGrigio"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.LUPO_GRIGIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_FOR_CAD_LIN_UN_TUO_SIM_UN_LUP_ABB_AGG_MA_POC_RES__ABB_VEL_NON_FAC_DA_SEM[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 6 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["LupoBianco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.LUPO_BIANCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_FOR_CAD__UN_PO_PI_FOR_E_RES_DEL_LUP_GRI_QUE_POC_SEC_IN_CUI_TI_FIS_PRI_DI_ATT_SON_GEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 7 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["LupoNero"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.LUPO_NERO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_FOR_CAD_LA_RAZ_DI_LUP_PI_FOR_NEL_BUI_DEL_FOR_SAR_DIF_NOT_SE_NON_VIA_IN_BRA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 8 and dictNemiciSbloccati["nemiciForesta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Cinghiale"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CINGHIALE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_FOR_CAD__UN_BES_GRA_IL_DOP_DI_ME_NE_HO_DOV_AFF_UNO_E_PER_POC_NON_CI_RIM_SEC_COM_QUE_SOL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 9 and dictNemiciSbloccati["nemiciCitta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Cittadino1"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.AGGRESSORE_1[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.NON_VOL_UCC_AVE_UN_TON_VIO_MI_AVR_STU_FOR_SAR_STA_MEG_NON_OPP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 10 and dictNemiciSbloccati["nemiciCitta"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Cittadino3"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.AGGRESSORE_2[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.LHO_UCC_PRI_CHE_POT_TOC_NON_SON_UNA_PAZ_ASS_VOL_CHI_FAR_DEL_MAL_CHE_CAZ_HO_FAT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 11 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["SerpeVerde"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SERPENTE_VERDE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_SEL_ARI_LI_ODI_FAN_TRO_CON_CON_I_LOR_SON_SI_MUO_LEN_FIN_NON_TRO_UNA_PRE_POI_ACC_DI_COL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 12 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["SerpeArancio"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SERPENTE_ARANCIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_SEL_ARI_QUE_MAL_SON_VEL_SEM_MUO_LEN_MA_QUA_AVV_LA_PRE_SON_FUL_NEL_RAG[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 13 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RagnoNero"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.RAGNO_NERO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_SEL_ARI_SON_ENO_VEL_E_ABB_RES_I_LOR_MOR_FAN_ABB_MAL_MA_PER_FOR_NON_SON_VEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 14 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RagnoRosso"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.RAGNO_ROSSO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_SEL_ARI_QUE_SON_VER_I_PI_FAS_ATT_A_DIS_LAN_LA_LOR_SAL_VEL_PER_FOR_NON_SON_MOL_RES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 15 and dictNemiciSbloccati["nemiciSelva"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Scorpione"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SCORPIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_SEL_ARI_SEN_DUB_LA_BEL_PI_TEM_DEL_POS__FOR_VEL_RES_E_PUR_VEL_IMP_AFF_IN_BRA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 16 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["GufoMarrone"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.GUFO_MARRONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_PAS_MON_QUE_GUF_SEM_TAN_INN_E_AMI_MA_APP_TI_VED_TI_PIO_ADD_E_INI_AD_ART_SEN_SOS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 17 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["GufoBianco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.GUFO_BIANCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_PAS_MON_A_PRI_IMP_ANC_LOR_INN_E_AMI_MA_COM_I_LOR_SIM_GUF_MAR_SON_OST_E_PER_PI_AGG_E_RES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 18 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Struzzo"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.STRUZZO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_PAS_MON_DEG_STR_VOL_CHE_PER_NON_HO_MAI_VIS_VOL_IMM_NON_POS_PER_LA_LOR_STA_SON_UN_PO_GOF_MA_MOL_FOR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 19 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Casuario"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CASUARIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_PAS_MON_DEG_STR_UN_PO_PI_BAS_TOZ_E_VEL_LE_LOR_PIU_NER_SON_UNT_E_APP_NON__BEL_VED_ARR_ADD[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 20 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Falco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.FALCO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_PAS_MON_UNO_DEI_VOL_PI_TEM_LA_LOR_APE_ALA_MIS_QUA_IL_DOP_DEL_MIA_ALT_SON_VEL_AGG_E_MOL_RES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 21 and dictNemiciSbloccati["nemiciMontagne"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["Aquila"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.AQUILA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_PAS_MON_LA_PI_PER_DEL_ZON__GRA_CIR_QUA_UN_FAL_MA__PI_FER_E_RES_FOR_NON_SI_INC_SPE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 22 and dictNemiciSbloccati["nemiciCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["ServoSpada"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SER_CON_SPA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.SOL_DI_NEI_A_GUA_DEL_CAS_IL_SUO_COM__STA_IMM_IN_UN_PUN_DEL_CAS_CAP_DI_INF_ING_DAN_DAT_LA_SUA_ABI_NEL_DEL_SPA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 23 and dictNemiciSbloccati["nemiciCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["ServoArco"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SER_CON_ARC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.SOL_DI_NEI_A_GUA_DEL_CAS_IL_SUO_COM__STA_IMM_IN_UN_PUN_DEL_CAS_SPE_NEL_DEL_ATT_DI_CON_IL_NEM_DAL_DIS[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 24 and dictNemiciSbloccati["nemiciCastello"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["ServoLancia"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SER_CON_LAN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.SOL_DI_NEI_A_GUA_DEL_CAS_IL_SUO_COM__STA_IMM_IN_UN_PUN_DEL_CAS_USA_UNA_LUN_LAN_NON_PAR_EFF_MA_PRE_DI_VEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 25 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboLeggero"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_LEGGERO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_CAV_IMP_VAG_IN_GIR_ACC_IMP_CHE_RIC_SCA_NEL_ROC_DEL_CAV_NEL_ROC_NON_PIA_NON_SON_FR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 26 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboVolante"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_VOLANTE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_CAV_IMP_SOR_LA_ZON_MEN_GLI_ALT_IMP_RAC_IMP_CRE_CHE_SIA_SUO_COM_ANC_IND_AGL_ALT_DOV_SCA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 27 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboPesante"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_PESANTE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_CAV_IMP_COM_GLI_IMP_LEG_RIC_IMP_DAL_ROC_DEL_CAV__PI_GRO_E_LEN_DEG_ALT_MA__IN_GRA_DI_TRA_PI_MAT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 28 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboPesanteVolante"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IMP_VOL_PES[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_CAV_IMP_COM_I_NOR_IMP_VOL_SOR_LA_ZON_MEN_GLI_ALT_RAC_IMP__PI_GRO_E_LEN_DEG_ALT_MA_MOL_PI_FOR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                        elif voceMarcataSottoMenu == 29 and dictNemiciSbloccati["nemiciCaverna"]:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.dictImgNemiciDiario["RoboTorre"], (xImgPersonaggio, yImgPersonaggio))
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xDescrizionePersonaggio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), (xDescrizionePersonaggio + largezzaFoglio, yDescrizionePersonaggio - GlobalHWVar.gpy * 0.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IMPO_TORRE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xNomePersonaggio, yNomePersonaggio, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.CRE_OST_CHE_SI_TRO_NEL_CAV_IMP_NON_HA_UN_RUO_EFF_NEL_RAC_DEG_IMP_SE_NON_QUE_DI_PRO_GLI_ALT__LEN_MA_QUA_COL_FA_PAR_MAL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xDescrizionePersonaggio, yDescrizionePersonaggio, 40, largezzaFoglio=largezzaFoglio, spazioTraLeRighe=spazioTraLeRighe)
                elif voceMarcata == 4:
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 5, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.TAS_MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 6, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.TASTIERA_MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 7, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.MOU_MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 9, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.MOU_MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 10, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.MOUSE_MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 11, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.CON_MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 13, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.CON_MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 14, 45)
                    FunzioniGraficheGeneriche.messaggio(LI.CONTROLLER_MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 10.7, GlobalHWVar.gsy // 18 * 15, 45)
                    if sottovoceSelezionata:
                        xInizioTutorialComandi = GlobalHWVar.gsx // 32 * 20.1
                        yInizioTutorialComandi = GlobalHWVar.gsy // 18 * 5.2
                        if voceMarcataSottoMenu == 1:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.TAS_MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CAM_BER_INQ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 1.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.DESELEZIONA_BERSAGLIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MODALIT_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.19, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.9, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.INTERAGISCI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.19, 35)
                        elif voceMarcataSottoMenu == 2:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.TAS_MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.PUN_SUL_PRO_BER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 1.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.43), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MODALIT_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.66), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.INQ_BER_PUN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.19, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.89), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.9, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.73, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.43), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.96, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.66), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.ATT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.19, 35)
                        elif voceMarcataSottoMenu == 3:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialTastieraInMenu, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.TASTIERA_MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.ESC_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IND__ESC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.1), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.1), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.6), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.6), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CAM_OPE_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SELEZIONA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.6, 35)
                        elif voceMarcataSottoMenu == 4:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.MOU_MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_LIB__MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_INT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_IMP__ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.7, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_STA_PER__MEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.2, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_LE__MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_SA__SAL_TUR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MODALIT_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.1, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_LE__RIM_SEL[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.6, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.7, 35)
                        elif voceMarcataSottoMenu == 5:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.MOU_MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_NEM__INQ__ATT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_CAS_INT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.2, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_IMP__ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.7, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_STA_PER__MEN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.2, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_LE__MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.7, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.SU_ICO_SA__SAL_TUR[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MODALIT_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.7, 35)
                        elif voceMarcataSottoMenu == 6:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialMouse, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.MOUSE_MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.SELEZIONA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.8, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.8), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IND__ESC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CAM_OPE_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.5, 35)
                            FunzioniGraficheGeneriche.messaggio(LI.ESC_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 2.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9, 35)
                        elif voceMarcataSottoMenu == 7:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.CON_MOD_MOV[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CAM_BER_INQ[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.05, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.DESELEZIONA_BERSAGLIO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MODALIT_INTERAZIONE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 6.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.45, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.8, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.INTERAGISCI[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.15, 35)
                        elif voceMarcataSottoMenu == 8:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInGioco, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.CON_MOD_INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 0.7, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 1.5), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.PUN_SUL_PRO_BER[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.05, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 2.85), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.MODALIT_MOVIMENTO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.INQ_BER_PUN[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 5.55), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 6.1, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.9), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.ATT__DIS_IMP[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 7.45, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 8.25), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SALTA_TURNO[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.8, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 9.6), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.ATT__INT[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 10.15, 35)
                        elif voceMarcataSottoMenu == 9:
                            GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.tutorialControllerInMenu, (xInizioTutorialComandi, yInizioTutorialComandi))
                            FunzioniGraficheGeneriche.messaggio(LI.CONTROLLER_MENU[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 5.05, yInizioTutorialComandi - GlobalHWVar.gpy * 1.1, 60, centrale=True)
                            FunzioniGraficheGeneriche.messaggio(LI.ESC_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 2.3, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 3.2), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.IND__ESC[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 3.85, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 4.75), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SPOSTA_PUNTATORE[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 5.4, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 6.3), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 6.3), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.CAM_OPE_SE_CON[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 6.95, 35)
                            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (xInizioTutorialComandi + GlobalHWVar.gpx * 0.3, yInizioTutorialComandi + GlobalHWVar.gpy * 7.85), (xInizioTutorialComandi + GlobalHWVar.gpx * 9.8, yInizioTutorialComandi + GlobalHWVar.gpy * 7.85), 2)
                            FunzioniGraficheGeneriche.messaggio(LI.SELEZIONA[GlobalHWVar.linguaImpostata], GlobalHWVar.grigioscu, xInizioTutorialComandi + GlobalHWVar.gpx * 4, yInizioTutorialComandi + GlobalHWVar.gpy * 8.5, 35)

            if sottovoceSelezionata:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    return esci
