# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def sceglicondiz(dati, condizione):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    condSconosciuta = GlobalImgVar.imgGambitSconosciuta
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.7
    risposta = False
    voceMarcata = 0
    aggiornaSchermo = False
    esci = False

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
                    yp = GlobalHWVar.gsy // 18 * 4.7
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
                if voceMarcata == 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    condizione = 0
                    risposta = True
                else:
                    # reimposto la condizione giusta perché ho messo un ordine diverso nel menu rispetto a tutto il resto (scambiati "Impo surriscaldato" con "Sempre a Sara")
                    c = 1
                    while c <= 20:
                        if voceMarcata == c:
                            condizioneTemp = c
                            if c == 5:
                                condizioneTemp = 9
                            elif c == 9:
                                condizioneTemp = 5
                            if dati[condizioneTemp + 80] != 0:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                condizione = condizioneTemp
                                risposta = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
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

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 4.7
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
                    yp = GlobalHWVar.gsy // 18 * 6.1
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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                FunzioniGraficheGeneriche.messaggio("Condizio-ImpoFogli", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Togli Condizio-ImpoFoglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.8, 40)
                if dati[81] > 0:
                    FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[82] > 0:
                    FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[83] > 0:
                    FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[84] > 0:
                    FunzioniGraficheGeneriche.messaggio("Sara con veleno", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[89] > 0:
                    FunzioniGraficheGeneriche.messaggio("Sempre a Sara", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[86] > 0:
                    FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[87] > 0:
                    FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[88] > 0:
                    FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[85] > 0:
                    FunzioniGraficheGeneriche.messaggio("Impo surriscaldato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[90] > 0:
                    FunzioniGraficheGeneriche.messaggio("Sempre a Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                if dati[91] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico a caso", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[92] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico vicino", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[93] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico lontano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[94] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[95] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[96] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[97] > 0:
                    FunzioniGraficheGeneriche.messaggio("Nemico con meno <*>#italic#Pv<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[98] > 0:
                    FunzioniGraficheGeneriche.messaggio("Numero di nemici > 1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[99] > 0:
                    FunzioniGraficheGeneriche.messaggio("Numero di nemici > 2", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[100] > 0:
                    FunzioniGraficheGeneriche.messaggio("Numero di nemici > 3", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, 0, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 16)), 2)

            grandezzaCarattereDescrizioni = 40
            larghezzaTestoDescrizioni = GlobalHWVar.gpx * 13
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            if voceMarcata == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(scecond[0], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                FunzioniGraficheGeneriche.messaggio("Togli Condizio-ImpoFoglio:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                FunzioniGraficheGeneriche.messaggio("Togli il Condizio-ImpoFoglio dalla cella di memoria.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if voceMarcata == 1:
                if dati[81] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[1], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 80%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su Sara se la vede e ha <*>#italic#Pv<*> < 80%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 2:
                if dati[82] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[2], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 50%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su Sara se la vede e ha <*>#italic#Pv<*> < 50%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 3:
                if dati[83] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[3], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 30%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su Sara se la vede e ha <*>#italic#Pv<*> < 30%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 4:
                if dati[84] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[4], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sara con veleno:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su Sara se la vede ed è avvelenata.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 5:
                if dati[89] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[9], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sempre a Sara:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su Sara in continuazione quando la vede (se l'Azio-ImpoFoglio associato comporta un'alterazione di stato, viene eseguito solo se lo status non è attivo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 6:
                if dati[86] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[6], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 80%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su Impo quando ha <*>#italic#Pe<*> < 80%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 7:
                if dati[87] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[7], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 50%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su Impo quando ha <*>#italic#Pe<*> < 50%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 8:
                if dati[88] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[8], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 30%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su Impo quando ha <*>#italic#Pe<*> < 30%.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 9:
                if dati[85] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[5], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Impo surriscaldato:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su Impo quando è surriscaldato.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 10:
                if dati[90] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[10], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sempre a Impo:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su Impo in continuazione (se l'Azio-ImpoFoglio associato comporta un'alterazione di stato, viene eseguito solo se lo status non è attivo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 11:
                if dati[91] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[11], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico a caso:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Esegue l'azione su un nemico a caso.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 12:
                if dati[92] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[12], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico vicino:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su un nemico in una casella accanto alla propria.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 13:
                if dati[93] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[13], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico lontano:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su un nemico distante di almeno una casella (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 14:
                if dati[94] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[14], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 80%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su un nemico con <*>#italic#Pv<*> < 80% (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 15:
                if dati[95] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[15], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 50%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su un nemico con <*>#italic#Pv<*> < 50% (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 16:
                if dati[96] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[16], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 30%:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione su un nemico con <*>#italic#Pv<*> < 30% (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 17:
                if dati[97] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[17], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Nemico con meno <*>#italic#Pv<*>:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione sul nemico con meno <*>#italic#Pv<*> (in caso di molteplici bersagli, esegue l'azione su quello più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 18:
                if dati[98] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[18], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Numero di nemici > 1:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione quando nei paraggi c'è più di 1 nemico (in caso di Azio-ImpoFoglio a bersaglio singolo, l'azione viene eseguita sul nemico più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 19:
                if dati[99] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[19], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Numero di nemici > 2:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 2 nemici (in caso di Azio-ImpoFoglio a bersaglio singolo, l'azione viene eseguita sul nemico più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 20:
                if dati[100] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scecond[20], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Numero di nemici > 3:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Esegue l'azione quando nei paraggi ci sono più di 3 nemici (in caso di Azio-ImpoFoglio a bersaglio singolo, l'azione viene eseguita sul nemico più vicino).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)

            # puntatore vecchio
            xPuntatoreVecchio = GlobalHWVar.gpx * 1
            yPuntatoreVecchio = GlobalHWVar.gpy * 4.7
            if condizione == 5:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 14.1
            elif condizione == 9:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 10.1
            elif condizione != 0:
                if condizione <= 10:
                    xPuntatoreVecchio = GlobalHWVar.gpx * 1
                    yPuntatoreVecchio = (GlobalHWVar.gpy * condizione) + (GlobalHWVar.gpy * 5.1)
                else:
                    xPuntatoreVecchio = GlobalHWVar.gpx * 8
                    yPuntatoreVecchio = (GlobalHWVar.gpy * (condizione - 10)) + (GlobalHWVar.gpy * 5.1)
            GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xPuntatoreVecchio, yPuntatoreVecchio))

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return condizione, esci


def sceglitecn(dati, tecnica):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    condSconosciuta = GlobalImgVar.imgGambitSconosciuta
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.7
    risposta = False
    voceMarcata = 0
    aggiornaSchermo = False
    esci = False

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
                    yp = GlobalHWVar.gsy // 18 * 4.7
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
                if voceMarcata == 0:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    tecnica = 0
                    risposta = True
                else:
                    # reimposto la tecnica giusta perché ho messo un ordine diverso nel menu rispetto a tutto il resto (non avevo voglia di andare a modificare tutto il resto)
                    # ordine menu => [1 cura, 2 cura+, 3 cura++, 4 antidoto, 5 attP, 6 difP, 7 ricarica, 8 ricarica+, 9 raffred, 10 efficienza, 11 scossa, 12 scossa+, 13 scossa++, 14 freccia, 15 freccia+, 16 freccia++, 17 tempesta, 18 tempesta+, 19 tempesta++, 20 velocizza]
                    # ordine vero => [1 scossa, 2 cura, 3 antidoto, 4 freccia, 5 tempesta, 6 raffred, 7 ricarica, 8 cura+, 9 scossa+, 10 freccia+, 11 velocizza, 12 attP, 13 difP, 14 efficienza, 15 tempesta+, 16 cura++, 17 ricarica+, 18 scossa++, 19 freccia++, 20 tempesta++]
                    c = 1
                    while c <= 20:
                        if voceMarcata == c:
                            tecnicaTemp = c
                            if c == 1:
                                tecnicaTemp = 2
                            elif c == 2:
                                tecnicaTemp = 8
                            elif c == 3:
                                tecnicaTemp = 16
                            elif c == 4:
                                tecnicaTemp = 3
                            elif c == 5:
                                tecnicaTemp = 12
                            elif c == 6:
                                tecnicaTemp = 13
                            elif c == 7:
                                tecnicaTemp = 7
                            elif c == 8:
                                tecnicaTemp = 17
                            elif c == 9:
                                tecnicaTemp = 6
                            elif c == 10:
                                tecnicaTemp = 14
                            elif c == 11:
                                tecnicaTemp = 1
                            elif c == 12:
                                tecnicaTemp = 9
                            elif c == 13:
                                tecnicaTemp = 18
                            elif c == 14:
                                tecnicaTemp = 4
                            elif c == 15:
                                tecnicaTemp = 10
                            elif c == 16:
                                tecnicaTemp = 19
                            elif c == 17:
                                tecnicaTemp = 5
                            elif c == 18:
                                tecnicaTemp = 15
                            elif c == 19:
                                tecnicaTemp = 20
                            elif c == 20:
                                tecnicaTemp = 11
                            if dati[tecnicaTemp + 10] != 0:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                                tecnica = tecnicaTemp
                                risposta = True
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                            break
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

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 11:
                    if voceMarcata == 1:
                        voceMarcata -= 1
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        yp = GlobalHWVar.gsy // 18 * 4.7
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
                    yp = GlobalHWVar.gsy // 18 * 6.1
                else:
                    if voceMarcata == 10 or voceMarcata == 20:
                        if voceMarcata == 10:
                            voceMarcata -= 10
                            GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                            yp = GlobalHWVar.gsy // 18 * 4.7
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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                FunzioniGraficheGeneriche.messaggio("Azio-ImpoFogli", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Togli Azio-ImpoFoglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.8, 40)
                if dati[12] > 0:
                    FunzioniGraficheGeneriche.messaggio("Cura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[18] > 0:
                    FunzioniGraficheGeneriche.messaggio("Cura +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[26] > 0:
                    FunzioniGraficheGeneriche.messaggio("Cura ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[13] > 0:
                    FunzioniGraficheGeneriche.messaggio("Antidoto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[22] > 0:
                    FunzioniGraficheGeneriche.messaggio("Carica attacco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[23] > 0:
                    FunzioniGraficheGeneriche.messaggio("Carica difesa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[17] > 0:
                    FunzioniGraficheGeneriche.messaggio("Auto-ricarica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[27] > 0:
                    FunzioniGraficheGeneriche.messaggio("Auto-ricarica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[16] > 0:
                    FunzioniGraficheGeneriche.messaggio("Raffreddamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[24] > 0:
                    FunzioniGraficheGeneriche.messaggio("Efficienza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15.2, 40)
                if dati[11] > 0:
                    FunzioniGraficheGeneriche.messaggio("Scossa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6.2, 40)
                if dati[19] > 0:
                    FunzioniGraficheGeneriche.messaggio("Scossa +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7.2, 40)
                if dati[28] > 0:
                    FunzioniGraficheGeneriche.messaggio("Scossa ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8.2, 40)
                if dati[14] > 0:
                    FunzioniGraficheGeneriche.messaggio("Freccia elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9.2, 40)
                if dati[20] > 0:
                    FunzioniGraficheGeneriche.messaggio("Freccia elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10.2, 40)
                if dati[29] > 0:
                    FunzioniGraficheGeneriche.messaggio("Freccia Elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11.2, 40)
                if dati[15] > 0:
                    FunzioniGraficheGeneriche.messaggio("Tempesta elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12.2, 40)
                if dati[25] > 0:
                    FunzioniGraficheGeneriche.messaggio("Tempesta elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13.2, 40)
                if dati[30] > 0:
                    FunzioniGraficheGeneriche.messaggio("Tempesta elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14.2, 40)
                if dati[21] > 0:
                    FunzioniGraficheGeneriche.messaggio("Velocizza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
                else:
                    FunzioniGraficheGeneriche.messaggio("???", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15.2, 40)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 11.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, 0, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 5.7)), (int(GlobalHWVar.gpx * 8) - 1, int(GlobalHWVar.gpy * 16)), 2)

            grandezzaCarattereDescrizioni = 40
            larghezzaTestoDescrizioni = GlobalHWVar.gpx * 13
            spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
            if voceMarcata == 0:
                GlobalHWVar.disegnaImmagineSuSchermo(scetecn[0], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                FunzioniGraficheGeneriche.messaggio("Togli Azio-ImpoFoglio:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                FunzioniGraficheGeneriche.messaggio("Togli l'Azio-ImpoFoglio dalla cella di memoria.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
            if voceMarcata == 1:
                if dati[12] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[2], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Cura:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[1]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Recupera un po' di <*>#italic#Pv<*> di Sara.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 2:
                if dati[18] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[8], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Cura +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[7]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Recupera molti <*>#italic#Pv<*> di Sara.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 3:
                if dati[26] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[16], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Cura ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[15]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio(u"Recupera un'enorme quantità dei <*>#italic#Pv<*> di Sara.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 4:
                if dati[13] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[3], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Antidoto:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[2]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Cura avvelenamento a Sara.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 5:
                if dati[22] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[12], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Carica attacco:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[11]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Incrementa l'attacco di Sara per un po' di tempo (non ha effetto sui nemici).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 6:
                if dati[23] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[13], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Carica difesa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[12]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Incrementa la difesa di Sara per un po' di tempo (non ha effetto sui nemici).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 7:
                if dati[17] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[7], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Auto-ricarica:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[6]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Ricarica un po' Impo ma richiede due turni e provoca surriscaldamento (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 8:
                if dati[27] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[17], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Auto-ricarica +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[16]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Ricarica di molto Impo ma richiede due turni e provoca surriscaldamento (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 9:
                if dati[16] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[6], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Raffreddamento:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[5]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Annulla il surriscaldamento ma richiede due turni (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 10:
                if dati[24] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[14], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Efficienza:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[13]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio(u"Tutte le tecniche costano la metà dei <*>#italic#Pe<*> per 30 turni. Si annulla con surriscaldamento (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 11:
                if dati[11] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[1], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Scossa:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[0]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge danni a un nemico vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 12:
                if dati[19] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[9], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Scossa +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[8]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge molti danni a un nemico vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 13:
                if dati[28] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[18], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Scossa ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[17]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge enormi danni a un nemico vicino.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 14:
                if dati[14] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[4], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Freccia elettrica:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[3]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge danni a distanza a un nemico.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 15:
                if dati[20] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[10], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Freccia elettrica +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[9]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge molti danni a distanza a un nemico.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 16:
                if dati[29] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[19], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Freccia Elettrica ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[18]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge enormi danni a distanza a un nemico.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 17:
                if dati[15] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[5], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Tempesta elettrica:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[4]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge danni a tutti i nemici o alleati nel raggio visivo di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 18:
                if dati[25] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[15], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Tempesta elettrica +:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[14]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge molti danni a tutti i nemici o alleati nel raggio visivo di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 19:
                if dati[30] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[20], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Tempesta elettrica ++:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[19]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Infligge enormi danni a tutti i nemici o alleati nel raggio visivo di Impo.", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
            if voceMarcata == 20:
                if dati[21] > 0:
                    GlobalHWVar.disegnaImmagineSuSchermo(scetecn[11], (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Velocizza:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)
                    FunzioniGraficheGeneriche.messaggio("Consumo: " + str(GlobalGameVar.costoTecniche[10]) + " <*>#italic#Pe<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13.8, 45)
                    FunzioniGraficheGeneriche.messaggio("Permette a Impo, se non surriscaldato, di eseguire due azioni al turno. Provoca surriscaldamento dopo 30 turni dall'esecuzione (applicata sempre su Impo).", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14.5, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(condSconosciuta, (GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4))
                    FunzioniGraficheGeneriche.messaggio("Sconosciuta", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13.5, 60)

            # puntatore vecchio
            xPuntatoreVecchio = GlobalHWVar.gpx * 1
            yPuntatoreVecchio = GlobalHWVar.gpy * 4.7
            if tecnica == 2:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 6.1
            elif tecnica == 8:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 7.1
            elif tecnica == 16:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 8.1
            elif tecnica == 3:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 9.1
            elif tecnica == 12:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 10.1
            elif tecnica == 13:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 11.1
            elif tecnica == 7:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 12.1
            elif tecnica == 17:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 13.1
            elif tecnica == 6:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 14.1
            elif tecnica == 14:
                xPuntatoreVecchio = GlobalHWVar.gpx * 1
                yPuntatoreVecchio = GlobalHWVar.gpy * 15.1
            elif tecnica == 1:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 6.1
            elif tecnica == 9:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 7.1
            elif tecnica == 18:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 8.1
            elif tecnica == 4:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 9.1
            elif tecnica == 10:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 10.1
            elif tecnica == 19:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 11.1
            elif tecnica == 5:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 12.1
            elif tecnica == 15:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 13.1
            elif tecnica == 20:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 14.1
            elif tecnica == 11:
                xPuntatoreVecchio = GlobalHWVar.gpx * 8
                yPuntatoreVecchio = GlobalHWVar.gpy * 15.1
            GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xPuntatoreVecchio, yPuntatoreVecchio))

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return tecnica, esci


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
    esci = False

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
        if bottoneDown == pygame.K_ESCAPE or bottoneDown == "mouseCentrale" or bottoneDown == "padStart":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            risposta = True
            if riordinamento:
                primoFrame = True
                riordinamento = False
                annullaRiordinamento = True
            esci = True
            bottoneDown = False
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
                                dati[i], esci = sceglicondiz(dati, dati[i])
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
                                dati[i], esci = sceglitecn(dati, dati[i])
                            else:
                                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                        i += 1
                        c += 1

                    if esci:
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

        if not esci and (aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput):
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
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
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

                FunzioniGraficheGeneriche.messaggio("Setta Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                FunzioniGraficheGeneriche.messaggio("Sacche Energetiche", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 3.5, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio(u"Priorità", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.8, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio("Condizio-ImpoFoglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 13.9, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
                FunzioniGraficheGeneriche.messaggio("Azio-ImpoFoglio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 19.8, GlobalHWVar.gsy // 18 * 4.7, 45, centrale=True)
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
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

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
                    FunzioniGraficheGeneriche.messaggio(str(i), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.8, GlobalHWVar.gsy // 18 * (i + 5.2), 50, centrale=True)
                    i += 1
                posXCondizioni = 11.8
                c = 6.3
                for i in range(101, 111):
                    if dati[i] == -1:
                        FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 0:
                        FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 1:
                        FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 2:
                        FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 3:
                        FunzioniGraficheGeneriche.messaggio("Sara con <*>#italic#Pv<*> < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 4:
                        FunzioniGraficheGeneriche.messaggio("Sara con veleno", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 5:
                        FunzioniGraficheGeneriche.messaggio("Impo surriscaldato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 6:
                        FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 7:
                        FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 8:
                        FunzioniGraficheGeneriche.messaggio("Impo con <*>#italic#Pe<*> < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 9:
                        FunzioniGraficheGeneriche.messaggio("Sempre a Sara", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 10:
                        FunzioniGraficheGeneriche.messaggio("Sempre a Impo", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 11:
                        FunzioniGraficheGeneriche.messaggio("Nemico a caso", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 12:
                        FunzioniGraficheGeneriche.messaggio("Nemico vicino", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 13:
                        FunzioniGraficheGeneriche.messaggio("Nemico lontano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 14:
                        FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 80%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 15:
                        FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 50%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 16:
                        FunzioniGraficheGeneriche.messaggio("Nemico con <*>#italic#Pv<*> < 30%", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 17:
                        FunzioniGraficheGeneriche.messaggio("Nemico con meno <*>#italic#Pv<*>", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 18:
                        FunzioniGraficheGeneriche.messaggio("Numero di nemici > 1", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 19:
                        FunzioniGraficheGeneriche.messaggio("Numero di nemici > 2", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 20:
                        FunzioniGraficheGeneriche.messaggio("Numero di nemici > 3", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXCondizioni, GlobalHWVar.gsy // 18 * c, 40)
                    c += 1
                posXTecniche = 18
                c = 6.3
                for i in range(111, 121):
                    if dati[i] == -1:
                        FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 0:
                        FunzioniGraficheGeneriche.messaggio("---", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 1:
                        FunzioniGraficheGeneriche.messaggio("Scossa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 2:
                        FunzioniGraficheGeneriche.messaggio("Cura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 3:
                        FunzioniGraficheGeneriche.messaggio("Antidoto", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 4:
                        FunzioniGraficheGeneriche.messaggio("Freccia elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 5:
                        FunzioniGraficheGeneriche.messaggio("Tempesta elettrica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 6:
                        FunzioniGraficheGeneriche.messaggio("Raffreddamento", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 7:
                        FunzioniGraficheGeneriche.messaggio("Auto-ricarica", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 8:
                        FunzioniGraficheGeneriche.messaggio("Cura +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 9:
                        FunzioniGraficheGeneriche.messaggio("Scossa +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 10:
                        FunzioniGraficheGeneriche.messaggio("Freccia elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 11:
                        FunzioniGraficheGeneriche.messaggio("Velocizza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 12:
                        FunzioniGraficheGeneriche.messaggio("Carica attacco", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 13:
                        FunzioniGraficheGeneriche.messaggio("Carica difesa", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 14:
                        FunzioniGraficheGeneriche.messaggio("Efficienza", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 15:
                        FunzioniGraficheGeneriche.messaggio("Tempesta elettrica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 16:
                        FunzioniGraficheGeneriche.messaggio("Cura ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 17:
                        FunzioniGraficheGeneriche.messaggio("Auto-ricarica +", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 18:
                        FunzioniGraficheGeneriche.messaggio("Scossa ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 19:
                        FunzioniGraficheGeneriche.messaggio("Freccia Elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
                    if dati[i] == 20:
                        FunzioniGraficheGeneriche.messaggio("Tempesta elettrica ++", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * posXTecniche, GlobalHWVar.gsy // 18 * c, 40)
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
                FunzioniGraficheGeneriche.messaggio("Statistiche:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 8.1, 60)
                FunzioniGraficheGeneriche.messaggio("Punti energia: %i" % entot, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, posizioneStatPeY, grandezzaCarattereStatistiche)
                FunzioniGraficheGeneriche.messaggio("Difesa: %i" % difro, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, posizioneStatDifY, grandezzaCarattereStatistiche)

                # mostrare descrizione batterie / priorità / condizioni / azioni
                grandezzaCarattereDescrizioni = 40
                posizioneTitoliY = int(GlobalHWVar.gsy // 18 * 4.8)
                posizioneDescrizioniX = int(GlobalHWVar.gsx // 32 * 23.5)
                posizioneDescrizioniY = int(GlobalHWVar.gsy // 18 * 5.8)
                larghezzaTestoDescrizioni = int(GlobalHWVar.gpx * 8)
                spazioTraLeRigheTestoDescrizione = int(GlobalHWVar.gpy * 0.6)
                if voceMarcata == 1:
                    if dati[71] != 0:
                        FunzioniGraficheGeneriche.messaggio("Sacca piccola:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Sacca Energetica che può contenere poca alimentazione.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][0] - GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][0] - GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 2:
                    if dati[72] != 0:
                        FunzioniGraficheGeneriche.messaggio("Sacca discreta:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Sacca Energetica con una buona capienza e ottimizzazione del sistema difensivo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][1] - GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][1] - GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 3:
                    if dati[73] != 0:
                        FunzioniGraficheGeneriche.messaggio("Sacca capiente:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Sacca Energetica con una grande capacità e un ottimo sistema difensivo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][2] - GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][2] - GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 4:
                    if dati[74] != 0:
                        FunzioniGraficheGeneriche.messaggio("Sacca enorme:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Grande Sacca Energetica che permette a Impo di utilizzare le tecniche più dispendiose.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][3] - GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][3] - GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                if voceMarcata == 5:
                    if dati[75] != 0:
                        FunzioniGraficheGeneriche.messaggio("Sacca illimitata:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                        FunzioniGraficheGeneriche.messaggio(u"Sacca Energetica incredibilmente capiente. Permette un eccellente ottimizzazione del sistema difensivo.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][4] - GlobalGameVar.statisticheEquipaggiamento["batteriaPe"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatPeY, grandezzaCarattereStatistiche)
                        diff = GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][4] - GlobalGameVar.statisticheEquipaggiamento["batteriaDif"][dati[9]]
                        if diff < 0:
                            FunzioniGraficheGeneriche.messaggio(str(diff), GlobalHWVar.rosso, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                        elif diff > 0:
                            FunzioniGraficheGeneriche.messaggio("+" + str(diff), GlobalHWVar.verde, posizioneStatisticheX, posizioneStatDifY, grandezzaCarattereStatistiche)
                    else:
                        FunzioniGraficheGeneriche.messaggio("Sconosciuto", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)

                if 6 <= voceMarcata <= 15:
                    FunzioniGraficheGeneriche.messaggio(u"Priorità:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Indica la priorità dell'azione. Impo eseguirà l'azione associata alla prima condizione verificata della lista.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

                if 16 <= voceMarcata <= 25:
                    FunzioniGraficheGeneriche.messaggio("Condizio-ImpoFoglio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Indica la situazione che si deve verificare affinché Impo esegua l'Azio-ImpoFoglio associato.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)

                if 26 <= voceMarcata <= 35:
                    FunzioniGraficheGeneriche.messaggio("Azio-ImpoFoglio:", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneTitoliY, 60)
                    FunzioniGraficheGeneriche.messaggio(u"Indica l'azione che Impo eseguirà quando si verifica la condizione nel Condizio-ImpoFoglio associato.", GlobalHWVar.grigiochi, posizioneDescrizioniX, posizioneDescrizioniY, grandezzaCarattereDescrizioni, larghezzaTestoDescrizioni, spazioTraLeRigheTestoDescrizione)
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
        elif esci and annullaRiordinamento:
            dati = list(datiPrimaDiRiordinamento)
            annullaRiordinamento = False

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)
    return dati, esci
