# -*- coding: utf-8 -*-

import os
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.SettaggiLivelli.SetImgOggettiMappaPersonaggi as SetImgOggettiMappaPersonaggi


def settaController(arrivatoDaMenuPrincipale):
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.1
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8
    countdownAggiornamentoModulo = -1
    mostraErrore = False

    listaIdPadConfigModificata = []
    tastiPremutiPadConfig = []
    tastoDaConfigurare = 0
    ordineConfigTasti = ["croce", "cerchio", "quadrato", "triangolo", "l1", "r1", "start", "select", "croceDir"]
    configurazioneTastiFatta = []

    precedentementeInizializzato = True
    numPadSelezionato = 0
    if len(GlobalHWVar.configPadConnessi) > 0:
        controllerDaConfigurare = False
        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
        padInizialmeteConfigurato = False
        for pad in GlobalHWVar.listaPadConnessiConfigurati:
            if idController == pad.get_id():
                controllerDaConfigurare = pad
                padInizialmeteConfigurato = True
                break
        if not controllerDaConfigurare:
            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                if idController == pad.get_id():
                    controllerDaConfigurare = pad
                    padInizialmeteConfigurato = False
                    break
    else:
        controllerDaConfigurare = False
        idController = -1
        nomeController = "Nessun controller rilevato"
        padInizialmeteConfigurato = False

    configTemp = []
    impoControllerErrato, datiImpostazioniController = GlobalHWVar.caricaImpostazioniController()
    for confPad in datiImpostazioniController:
        impoPad = confPad.split("_")
        impoPad.pop(len(impoPad) - 1)
        if len(impoPad) > 0:
            configTemp.append(impoPad)

    configurando = False
    testando = False
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        cursoreSuFrecciaSinistra = False
        cursoreSuFrecciaDestra = False
        suTornaIndietro = False
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 8.5 and GlobalHWVar.gsy // 18 * 14.4 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 6
                xp = GlobalHWVar.gsx // 32 * 4.4
                yp = GlobalHWVar.gsy // 18 * 15.2
            elif GlobalHWVar.gsx // 32 * 8.5 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 14.4 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 7
                xp = GlobalHWVar.gsx // 32 * 8.5
                yp = GlobalHWVar.gsy // 18 * 15.2
            elif GlobalHWVar.gsx // 32 * 1.8 <= xMouse <= GlobalHWVar.gsx // 32 * 2.7 and GlobalHWVar.gsy // 18 * 7.5 <= yMouse <= GlobalHWVar.gsy // 18 * 8.7 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 14.3 <= xMouse <= GlobalHWVar.gsx // 32 * 15.2 and GlobalHWVar.gsy // 18 * 7.5 <= yMouse <= GlobalHWVar.gsy // 18 * 8.7 and not (configurando or testando):
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 4.7 <= yMouse <= GlobalHWVar.gsy // 18 * 6.2 and not (configurando or testando):
                voceMarcata = 1
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 5.1
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 9.2 <= yMouse <= GlobalHWVar.gsy // 18 * 10.7 and not (configurando or testando):
                voceMarcata = 3
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 9.6
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 10.7 <= yMouse <= GlobalHWVar.gsy // 18 * 12.2 and not (configurando or testando):
                voceMarcata = 4
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 11.1
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 12.2 <= yMouse <= GlobalHWVar.gsy // 18 * 13.7 and not (configurando or testando):
                voceMarcata = 5
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 12.6
            elif not GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(True)
            if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 6.2 <= yMouse < GlobalHWVar.gsy // 18 * 9.2 and not (configurando or testando):
                voceMarcata = 2
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 6.6
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown
        padPassatoPerTestEConf = False
        tastiPremutiPadConfigVecchi = tastiPremutiPadConfig[:]
        tastiPremutiPadConfig = []
        if configurando or testando:
            padPassatoPerTestEConf = controllerDaConfigurare
            # trovo i tasti premuti dal pad che sto configurando
            buttons = controllerDaConfigurare.get_numbuttons()
            for idTasto in range(buttons):
                if controllerDaConfigurare.get_button(idTasto):
                    tastiPremutiPadConfig.append(idTasto)
            hats = controllerDaConfigurare.get_numhats()
            for idCroceDirezionale in range(hats):
                hat = controllerDaConfigurare.get_hat(idCroceDirezionale)
                direzioneX, direzioneY = hat
                if direzioneX != 0 or direzioneY != 0:
                    tastiPremutiPadConfig.append("croceDir:" + str(idCroceDirezionale))
            if configurando and len(tastiPremutiPadConfig) == 1:
                if not ((ordineConfigTasti[tastoDaConfigurare].startswith("croceDir") and not (type(tastiPremutiPadConfig[0]) is str and tastiPremutiPadConfig[0].startswith("croceDir"))) or (not ordineConfigTasti[tastoDaConfigurare].startswith("croceDir") and type(tastiPremutiPadConfig[0]) is str and tastiPremutiPadConfig[0].startswith("croceDir"))):
                    tastoGiaUsato = False
                    for tasto in configurazioneTastiFatta:
                        if tasto == tastiPremutiPadConfig[0]:
                            tastoGiaUsato = True
                    if not tastoGiaUsato:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        configurazioneTastiFatta.append(tastiPremutiPadConfig[0])
                        tastoDaConfigurare += 1
                        aggiornaSchermo = True
        if configurando and len(configurazioneTastiFatta) == 10:
            configurazioneSalvata = False
            i = 0
            while i < len(configTemp):
                if configTemp[i][0] == nomeController:
                    configTemp[i][1] = configurazioneTastiFatta[1]
                    configTemp[i][2] = configurazioneTastiFatta[2]
                    configTemp[i][3] = configurazioneTastiFatta[3]
                    configTemp[i][4] = configurazioneTastiFatta[4]
                    configTemp[i][5] = configurazioneTastiFatta[5]
                    configTemp[i][6] = configurazioneTastiFatta[6]
                    configTemp[i][7] = configurazioneTastiFatta[7]
                    configTemp[i][8] = configurazioneTastiFatta[8]
                    configTemp[i][9] = int(configurazioneTastiFatta[9].split(":")[1])
                    configurazioneSalvata = True
                    break
                i += 1
            if not configurazioneSalvata:
                configurazioneTastiFatta[9] = int(configurazioneTastiFatta[9].split(":")[1])
                configTemp.append(configurazioneTastiFatta)
            if not precedentementeInizializzato:
                controllerDaConfigurare.quit()
            listaIdPadConfigModificata.append(idController)
            configurazioneTastiFatta = []
            configurando = False

        if tastiPremutiPadConfig != tastiPremutiPadConfigVecchi:
            aggiornaSchermo = True

        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput, controllerDaConfigurare=padPassatoPerTestEConf)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            if configurando or testando:
                configurando = False
                testando = False
            else:
                risposta = True
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if not (bottoneDown == "mouseSinistro" and (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra)):
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    if configurando or testando:
                        if not precedentementeInizializzato:
                            controllerDaConfigurare.quit()
                        configurando = False
                        testando = False
                    else:
                        risposta = True
                # aggiorna lista controller
                elif voceMarcata == 1:
                    if arrivatoDaMenuPrincipale and countdownAggiornamentoModulo <= 0:
                        countdownAggiornamentoModulo = 150
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            pad.quit()
                        if controllerDaConfigurare and controllerDaConfigurare.get_init():
                            controllerDaConfigurare.quit()
                        GlobalHWVar.inizializzaModuloJoistick()

                        numPadSelezionato = 0
                        if len(GlobalHWVar.configPadConnessi) > 0:
                            controllerDaConfigurare = False
                            idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                            nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                            padInizialmeteConfigurato = False
                            for pad in GlobalHWVar.listaPadConnessiConfigurati:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = True
                                    break
                            if not controllerDaConfigurare:
                                for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                    if idController == pad.get_id():
                                        controllerDaConfigurare = pad
                                        padInizialmeteConfigurato = False
                                        break
                        else:
                            controllerDaConfigurare = False
                            idController = -1
                            nomeController = "Nessun controller rilevato"
                            padInizialmeteConfigurato = False
                    elif not arrivatoDaMenuPrincipale:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
                        mostraErrore = "nonInMenuPrincipale"
                    elif countdownAggiornamentoModulo > 0:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
                        mostraErrore = "attendiQualcheSecondo"
                # inizia configurazione
                elif not configurando and voceMarcata == 3:
                    if controllerDaConfigurare and not controllerDaConfigurare.get_init():
                        precedentementeInizializzato = False
                        controllerDaConfigurare.init()
                    elif controllerDaConfigurare and controllerDaConfigurare.get_init():
                        precedentementeInizializzato = True
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        configurazioneTastiFatta = []
                        configurazioneTastiFatta.append(nomeController)
                        tastoDaConfigurare = 0
                        configurando = True
                        aggiornaSchermo = True
                        if controllerDaConfigurare == GlobalHWVar.padUtilizzato:
                            pygame.time.wait(200)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # canella configurazione
                elif voceMarcata == 4:
                    if controllerDaConfigurare:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        i = 0
                        while i < len(configTemp):
                            if configTemp[i][0] == nomeController:
                                del configTemp[i]
                                break
                            i += 1
                        i = 0
                        while i < len(listaIdPadConfigModificata):
                            if listaIdPadConfigModificata[i] == idController:
                                del listaIdPadConfigModificata[i]
                                break
                            i += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # testa controller
                elif not testando and voceMarcata == 5:
                    if controllerDaConfigurare and not controllerDaConfigurare.get_init():
                        precedentementeInizializzato = False
                        controllerDaConfigurare.init()
                    elif controllerDaConfigurare and controllerDaConfigurare.get_init():
                        precedentementeInizializzato = True
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                        testando = True
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                # salva
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Impostazioni/ImpoController.txt", "w")
                    for padConf in configTemp:
                        for elemento in padConf:
                            scrivi.write(str(elemento) + "_")
                        scrivi.write("\n")
                    scrivi.close()
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        pad.quit()
                    if controllerDaConfigurare and controllerDaConfigurare.get_init():
                        controllerDaConfigurare.quit()
                    GlobalHWVar.assegnaConfigurazioneController()

                    listaIdPadConfigModificata = []
                    numPadSelezionato = 0
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                # esci
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                else:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
                bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == "mouseSinistro" or bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu" or ((voceMarcata == 2 or voceMarcata == 6 or voceMarcata == 7) and (bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padDestra" or bottoneDown == "padSinistra")):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput or countdownAggiornamentoModulo == 0:
            if countdownAggiornamentoModulo == 0:
                countdownAggiornamentoModulo = -1
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if not (configurando or testando):
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 5
                        xp = GlobalHWVar.gsx // 32 * 4.4
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    elif voceMarcata == 2 or voceMarcata == 4 or voceMarcata == 5:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gsy // 18 * 1.5
                    elif voceMarcata == 3:
                        voceMarcata -= 1
                        yp = GlobalHWVar.gsy // 18 * 6.6
                    elif voceMarcata == 6:
                        voceMarcata -= 1
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.6
                    elif voceMarcata == 7:
                        voceMarcata -= 2
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.6
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento) and not (configurando or testando):
                if voceMarcata == 2:
                    if len(GlobalHWVar.configPadConnessi) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    numPadSelezionato -= 1
                    if numPadSelezionato < 0:
                        numPadSelezionato = len(GlobalHWVar.configPadConnessi) - 1
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    xp = GlobalHWVar.gsx // 32 * 8.5
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    xp = GlobalHWVar.gsx // 32 * 4.4
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if not (configurando or testando):
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1 or voceMarcata == 3 or voceMarcata == 4:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gsy // 18 * 1.5
                    elif voceMarcata == 2:
                        voceMarcata += 1
                        yp = GlobalHWVar.gsy // 18 * 9.6
                    elif voceMarcata == 5:
                        voceMarcata += 1
                        xp = GlobalHWVar.gsx // 32 * 4.4
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    elif voceMarcata == 6:
                        voceMarcata -= 5
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 5.1
                    elif voceMarcata == 7:
                        voceMarcata -= 6
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 5.1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento) and not (configurando or testando):
                if voceMarcata == 2:
                    if len(GlobalHWVar.configPadConnessi) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    numPadSelezionato += 1
                    if numPadSelezionato > len(GlobalHWVar.configPadConnessi) - 1:
                        numPadSelezionato = 0
                    if len(GlobalHWVar.configPadConnessi) > 0:
                        controllerDaConfigurare = False
                        idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                        nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                        padInizialmeteConfigurato = False
                        for pad in GlobalHWVar.listaPadConnessiConfigurati:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = True
                                break
                        if not controllerDaConfigurare:
                            for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                                if idController == pad.get_id():
                                    controllerDaConfigurare = pad
                                    padInizialmeteConfigurato = False
                                    break
                    else:
                        controllerDaConfigurare = False
                        idController = -1
                        nomeController = "Nessun controller rilevato"
                        padInizialmeteConfigurato = False
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    xp = GlobalHWVar.gsx // 32 * 8.5
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    xp = GlobalHWVar.gsx // 32 * 4.4
            if bottoneDown == "mouseSinistro" and voceMarcata == 2 and cursoreSuFrecciaSinistra and (tastotempfps == 0 or primoMovimento):
                if len(GlobalHWVar.configPadConnessi) > 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                numPadSelezionato -= 1
                if numPadSelezionato < 0:
                    numPadSelezionato = len(GlobalHWVar.configPadConnessi) - 1
                if len(GlobalHWVar.configPadConnessi) > 0:
                    controllerDaConfigurare = False
                    idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                    nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                    padInizialmeteConfigurato = False
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        if idController == pad.get_id():
                            controllerDaConfigurare = pad
                            padInizialmeteConfigurato = True
                            break
                    if not controllerDaConfigurare:
                        for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = False
                                break
                else:
                    controllerDaConfigurare = False
                    idController = -1
                    nomeController = "Nessun controller rilevato"
                    padInizialmeteConfigurato = False
            if bottoneDown == "mouseSinistro" and voceMarcata == 2 and cursoreSuFrecciaDestra and (tastotempfps == 0 or primoMovimento):
                if len(GlobalHWVar.configPadConnessi) > 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                numPadSelezionato += 1
                if numPadSelezionato > len(GlobalHWVar.configPadConnessi) - 1:
                    numPadSelezionato = 0
                if len(GlobalHWVar.configPadConnessi) > 0:
                    controllerDaConfigurare = False
                    idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                    nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                    padInizialmeteConfigurato = False
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        if idController == pad.get_id():
                            controllerDaConfigurare = pad
                            padInizialmeteConfigurato = True
                            break
                    if not controllerDaConfigurare:
                        for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = False
                                break
                else:
                    controllerDaConfigurare = False
                    idController = -1
                    nomeController = "Nessun controller rilevato"
                    padInizialmeteConfigurato = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                FunzioniGraficheGeneriche.messaggio("Configura controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostazioniController, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                FunzioniGraficheGeneriche.messaggio("Seleziona il controller da configurare:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.5, 60)
                FunzioniGraficheGeneriche.messaggio("Inizia configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.5, 60)
                FunzioniGraficheGeneriche.messaggio("Cancella configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, 60)
                FunzioniGraficheGeneriche.messaggio("Testa configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.5, 60)

                FunzioniGraficheGeneriche.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 15, 70)
                FunzioniGraficheGeneriche.messaggio("Indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.4, GlobalHWVar.gsy // 18 * 15, 70)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.7, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7.5, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 15.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 15.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostazioniController, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if mostraErrore == "nonInMenuPrincipale":
                    FunzioniGraficheGeneriche.messaggio("Opzione disponibile solo accedendo da menu principale", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
                if mostraErrore == "attendiQualcheSecondo":
                    FunzioniGraficheGeneriche.messaggio("Attendi qualche secondo", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
                mostraErrore = False
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, 0, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 1.5, (GlobalHWVar.gpy * 14.4) - 1), (GlobalHWVar.gpx * 15.5, (GlobalHWVar.gpy * 14.4) - 1), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 8.5) - 1, GlobalHWVar.gpy * 14.65), ((GlobalHWVar.gpx * 8.5) - 1, GlobalHWVar.gpy * 16.2), 2)

            if countdownAggiornamentoModulo <= 0 and arrivatoDaMenuPrincipale:
                FunzioniGraficheGeneriche.messaggio("Aggiorna lista controller collegati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 60)
            else:
                FunzioniGraficheGeneriche.messaggio("Aggiorna lista controller collegati", GlobalHWVar.grigioscu, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, 60)
            if idController != -1:
                FunzioniGraficheGeneriche.messaggio("#" + str(idController) + " " + nomeController, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 7.8, 50, centrale=True, lungMax=11)
            else:
                FunzioniGraficheGeneriche.messaggio(nomeController, GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 7.8, 50, centrale=True, lungMax=11)
            if voceMarcata == 2:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 7.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 1.5, GlobalHWVar.gsy // 18 * 7.6))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 14.5, GlobalHWVar.gsy // 18 * 7.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 14.5, GlobalHWVar.gsy // 18 * 7.6))

            if configurando:
                FunzioniGraficheGeneriche.messaggio("Clicca i tasti illuminati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                if ordineConfigTasti[tastoDaConfigurare] == "croce":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroce, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "cerchio":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCerchio, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "quadrato":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerQuadrato, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "triangolo":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerTriangolo, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "l1":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerL1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "r1":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerR1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "start":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerStart, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "select":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerSelect, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "croceDir":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroceDirezionale, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
            elif testando:
                configurazioneDaTestare = []
                for padConf in configTemp:
                    if padConf[0] == nomeController:
                        configurazioneDaTestare.append(int(padConf[1]))
                        configurazioneDaTestare.append(int(padConf[2]))
                        configurazioneDaTestare.append(int(padConf[3]))
                        configurazioneDaTestare.append(int(padConf[4]))
                        configurazioneDaTestare.append(int(padConf[5]))
                        configurazioneDaTestare.append(int(padConf[6]))
                        configurazioneDaTestare.append(int(padConf[7]))
                        configurazioneDaTestare.append(int(padConf[8]))
                        configurazioneDaTestare.append("croceDir:" + str(padConf[9]))
                        break
                if len(configurazioneDaTestare) > 0:
                    if configurazioneDaTestare[0] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroce, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[1] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCerchio, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[2] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerQuadrato, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[3] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerTriangolo, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[4] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerL1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[5] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerR1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[6] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerStart, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[7] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerSelect, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                    if configurazioneDaTestare[8] in tastiPremutiPadConfig:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroceDirezionale, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                FunzioniGraficheGeneriche.messaggio("Controlla che i tasti premuti corrispondano a quelli illuminati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
            else:
                if controllerDaConfigurare:
                    if padInizialmeteConfigurato:
                        FunzioniGraficheGeneriche.messaggio(u"Controller configurato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                    else:
                        FunzioniGraficheGeneriche.messaggio(u"Controller non configurato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("Nessun controller rilevato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
            padConfiguratoTemp = False
            for padConf in configTemp:
                if padConf[0] == nomeController:
                    padConfiguratoTemp = True
            if padInizialmeteConfigurato != padConfiguratoTemp:
                if padConfiguratoTemp:
                    FunzioniGraficheGeneriche.messaggio("Controller temporaneamente configurato", GlobalHWVar.verde, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("Controller temporaneamente non configurato", GlobalHWVar.rosso, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
            else:
                if idController in listaIdPadConfigModificata:
                    FunzioniGraficheGeneriche.messaggio("Configurazione temporaneamente modificata", GlobalHWVar.verde, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)

            if configurando or testando:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        if countdownAggiornamentoModulo > 0:
            countdownAggiornamentoModulo -= 1
        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def settaTastiera():
    puntatore = GlobalImgVar.puntatore
    puntatorevecchio = GlobalImgVar.puntatorevecchio
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 5.1
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    aggiornaInterfacciaPerCambioInput = True
    primoFrame = True
    bottoneDown = False
    tastotempfps = 8

    tastoDaConfigurare = False
    tastiDaNonModificare = [pygame.K_0, pygame.K_KP0, pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_3, pygame.K_KP3, pygame.K_2, pygame.K_KP2, pygame.K_SPACE, pygame.K_ESCAPE]
    configAttuale = GlobalHWVar.caricaImpostazioniTastiera()
    configTemp = configAttuale.copy()

    configurando = False
    while not risposta:
        # rallenta per i 30 fps
        if tastotempfps != 0 and bottoneDown:
            tastotempfps -= 1
        elif tastotempfps == 0 and bottoneDown:
            tastotempfps = 2

        voceMarcataVecchia = voceMarcata
        suTornaIndietro = False
        xMouse, yMouse = pygame.mouse.get_pos()
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 4.7 <= yMouse <= GlobalHWVar.gsy // 18 * 6.2 and not configurando:
                voceMarcata = 1
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 5.1
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 9.2 <= yMouse <= GlobalHWVar.gsy // 18 * 10.7 and not configurando:
                voceMarcata = 3
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 9.6
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 10.7 <= yMouse <= GlobalHWVar.gsy // 18 * 12.2 and not configurando:
                voceMarcata = 4
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                xp = GlobalHWVar.gsx // 32 * 1
                yp = GlobalHWVar.gsy // 18 * 11.1
            elif GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 8.5 and GlobalHWVar.gsy // 18 * 14.4 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5 and not configurando:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 6
                xp = GlobalHWVar.gsx // 32 * 4.4
                yp = GlobalHWVar.gsy // 18 * 15.2
            elif GlobalHWVar.gsx // 32 * 8.5 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 14.4 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5 and not configurando:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 7
                xp = GlobalHWVar.gsx // 32 * 8.5
                yp = GlobalHWVar.gsy // 18 * 15.2
            elif not GlobalHWVar.mouseBloccato:
                GlobalHWVar.configuraCursore(True)
            if voceMarcataVecchia != voceMarcata and not primoFrame:
                GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)

        # gestione degli input
        primoMovimento = False
        bottoneDownVecchio = bottoneDown

        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, aggiornaInterfacciaPerCambioInput, configurandoTastiera=configurando)
        if bottoneDownVecchio != bottoneDown:
            primoMovimento = True
            tastotempfps = 8
        if bottoneDown == pygame.K_q or bottoneDown == "mouseDestro" or bottoneDown == "padCerchio":
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
            if configurando:
                configurando = False
            else:
                risposta = True
            bottoneDown = False
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if bottoneDown == "mouseSinistro" and suTornaIndietro:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                if configurando:
                    configurando = False
                else:
                    risposta = True
            # aggiorna tasto Q
            elif voceMarcata == 1:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                tastoDaConfigurare = "Q"
                configurando = True
                aggiornaSchermo = True
            # resetta configurazione
            elif voceMarcata == 7:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                aggiornaSchermo = True
            # salva
            elif voceMarcata == 8:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Impostazioni/ImpoController.txt", "w")
                for padConf in configTemp:
                    for elemento in padConf:
                        scrivi.write(str(elemento) + "_")
                    scrivi.write("\n")
                scrivi.close()
                for pad in GlobalHWVar.listaPadConnessiConfigurati:
                    pad.quit()
                if controllerDaConfigurare and controllerDaConfigurare.get_init():
                    controllerDaConfigurare.quit()
                GlobalHWVar.assegnaConfigurazioneController()

                listaIdPadConfigModificata = []
                numPadSelezionato = 0
                if len(GlobalHWVar.configPadConnessi) > 0:
                    controllerDaConfigurare = False
                    idController = GlobalHWVar.configPadConnessi[numPadSelezionato][0]
                    nomeController = GlobalHWVar.configPadConnessi[numPadSelezionato][1]
                    padInizialmeteConfigurato = False
                    for pad in GlobalHWVar.listaPadConnessiConfigurati:
                        if idController == pad.get_id():
                            controllerDaConfigurare = pad
                            padInizialmeteConfigurato = True
                            break
                    if not controllerDaConfigurare:
                        for pad in GlobalHWVar.listaPadConnessiSconosciuti:
                            if idController == pad.get_id():
                                controllerDaConfigurare = pad
                                padInizialmeteConfigurato = False
                                break
                else:
                    controllerDaConfigurare = False
                    idController = -1
                    nomeController = "Nessun controller rilevato"
                    padInizialmeteConfigurato = False
            # esci
            elif voceMarcata == 9:
                GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                risposta = True
            else:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
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
                if configurando:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1:
                        voceMarcata += 5
                        xp = GlobalHWVar.gsx // 32 * 4.4
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    elif voceMarcata == 2 or voceMarcata == 4 or voceMarcata == 5:
                        voceMarcata -= 1
                        yp = yp - GlobalHWVar.gsy // 18 * 1.5
                    elif voceMarcata == 3:
                        voceMarcata -= 1
                        yp = GlobalHWVar.gsy // 18 * 6.6
                    elif voceMarcata == 6:
                        voceMarcata -= 1
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.6
                    elif voceMarcata == 7:
                        voceMarcata -= 2
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 12.6
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if not configurando:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if voceMarcata == 1 or voceMarcata == 3 or voceMarcata == 4:
                        voceMarcata += 1
                        yp = yp + GlobalHWVar.gsy // 18 * 1.5
                    elif voceMarcata == 2:
                        voceMarcata += 1
                        yp = GlobalHWVar.gsy // 18 * 9.6
                    elif voceMarcata == 5:
                        voceMarcata += 1
                        xp = GlobalHWVar.gsx // 32 * 4.4
                        yp = GlobalHWVar.gsy // 18 * 15.2
                    elif voceMarcata == 6:
                        voceMarcata -= 5
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 5.1
                    elif voceMarcata == 7:
                        voceMarcata -= 6
                        xp = GlobalHWVar.gsx // 32 * 1
                        yp = GlobalHWVar.gsy // 18 * 5.1
                else:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                    bottoneDown = False
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                FunzioniGraficheGeneriche.messaggio("Configura controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostazioniController, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                FunzioniGraficheGeneriche.messaggio("Seleziona il controller da configurare:", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.5, 60)
                FunzioniGraficheGeneriche.messaggio("Inizia configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9.5, 60)
                FunzioniGraficheGeneriche.messaggio("Cancella configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, 60)
                FunzioniGraficheGeneriche.messaggio("Testa configurazione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12.5, 60)

                FunzioniGraficheGeneriche.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 5.3, GlobalHWVar.gsy // 18 * 15, 70)
                FunzioniGraficheGeneriche.messaggio("Indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 9.4, GlobalHWVar.gsy // 18 * 15, 70)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.7, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7.5, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 1.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 4.4, GlobalHWVar.gsy // 18 * 15.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 8.5, GlobalHWVar.gsy // 18 * 15.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 16.5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostazioniController, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 22, 0, GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gpx * 1.5, (GlobalHWVar.gpy * 14.4) - 1), (GlobalHWVar.gpx * 15.5, (GlobalHWVar.gpy * 14.4) - 1), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 8.5) - 1, GlobalHWVar.gpy * 14.65), ((GlobalHWVar.gpx * 8.5) - 1, GlobalHWVar.gpy * 16.2), 2)

            if configurando:
                FunzioniGraficheGeneriche.messaggio("Clicca i tasti illuminati", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13.5, 40, centrale=True)
                if ordineConfigTasti[tastoDaConfigurare] == "croce":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroce, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "cerchio":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCerchio, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "quadrato":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerQuadrato, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "triangolo":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerTriangolo, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "l1":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerL1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "r1":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerR1, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "start":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerStart, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "select":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerSelect, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
                if ordineConfigTasti[tastoDaConfigurare] == "croceDir":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.impostaControllerCroceDirezionale, (GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2))
            padConfiguratoTemp = False
            if padInizialmeteConfigurato != padConfiguratoTemp:
                if padConfiguratoTemp:
                    FunzioniGraficheGeneriche.messaggio("Configurazione temporaneamente modificata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
                else:
                    FunzioniGraficheGeneriche.messaggio("Configurazione salvata", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)
            else:
                if idController in listaIdPadConfigModificata:
                    FunzioniGraficheGeneriche.messaggio("Configurazione temporaneamente modificata", GlobalHWVar.verde, GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14.5, 40, centrale=True)

            if configurando:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatorevecchio, (xp, yp))
            else:
                GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)


def menuImpostazioni(arrivatoDaMenuPrincipale, dimezzaVolumeCanzone, avanzamentoStoria, cambiatoRisoluzione):
    puntatore = GlobalImgVar.puntatore
    xp = GlobalHWVar.gsx // 32 * 1
    yp = GlobalHWVar.gsy // 18 * 4.8
    risposta = False
    voceMarcata = 1
    aggiornaSchermo = False

    linguaTemp = GlobalHWVar.linguaImpostata
    volumeEffettiTemp = GlobalHWVar.volumeEffetti * 10
    gsxTemp = GlobalHWVar.gsx
    gsyTemp = GlobalHWVar.gsy
    modalitaSchermoTemp = GlobalHWVar.modalitaSchermo
    vSyncTemp = GlobalHWVar.vSyncEnabled

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
        cursoreSuFrecciaSinistra = False
        cursoreSuFrecciaDestra = False
        cursoreSuImpoController = False
        cursoreSuImpoTastiera = False
        xMouse, yMouse = pygame.mouse.get_pos()
        suTornaIndietro = False
        if GlobalHWVar.mouseVisibile:
            if GlobalHWVar.gsx // 32 * 21.5 <= xMouse <= GlobalHWVar.gsx and 0 <= yMouse <= GlobalHWVar.gsy // 18 * 2:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                suTornaIndietro = True
            elif GlobalHWVar.gsx // 32 * 10 <= xMouse <= GlobalHWVar.gsx // 32 * 16 and GlobalHWVar.gsy // 18 * 14.45 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 8
                xp = GlobalHWVar.gsx // 32 * 11.9
                yp = GlobalHWVar.gsy // 18 * 15.2
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 22 and GlobalHWVar.gsy // 18 * 14.45 <= yMouse <= GlobalHWVar.gsy // 18 * 16.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                voceMarcata = 9
                xp = GlobalHWVar.gsx // 32 * 16
                yp = GlobalHWVar.gsy // 18 * 15.2
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 4.5 <= yMouse <= GlobalHWVar.gsy // 18 * 5.7:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 19.7 <= xMouse <= GlobalHWVar.gsx // 32 * 20.6 and GlobalHWVar.gsy // 18 * 4.5 <= yMouse <= GlobalHWVar.gsy // 18 * 5.7:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 18 <= xMouse <= GlobalHWVar.gsx // 32 * 18.9 and GlobalHWVar.gsy // 18 * 5.9 <= yMouse <= GlobalHWVar.gsy // 18 * 7.1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 21.2 and GlobalHWVar.gsy // 18 * 7.3 <= yMouse <= GlobalHWVar.gsy // 18 * 8.5:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuImpoTastiera = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 21.2 and GlobalHWVar.gsy // 18 * 8.7 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuImpoController = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 10.1 <= yMouse <= GlobalHWVar.gsy // 18 * 11.3:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 21 <= xMouse <= GlobalHWVar.gsx // 32 * 21.9 and GlobalHWVar.gsy // 18 * 10.1 <= yMouse <= GlobalHWVar.gsy // 18 * 11.3:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 11.5 <= yMouse <= GlobalHWVar.gsy // 18 * 12.7:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 23.7 <= xMouse <= GlobalHWVar.gsx // 32 * 24.6 and GlobalHWVar.gsy // 18 * 11.5 <= yMouse <= GlobalHWVar.gsy // 18 * 12.7:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            elif GlobalHWVar.gsx // 32 * 16 <= xMouse <= GlobalHWVar.gsx // 32 * 16.9 and GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaSinistra = True
            elif GlobalHWVar.gsx // 32 * 20.7 <= xMouse <= GlobalHWVar.gsx // 32 * 21.6 and GlobalHWVar.gsy // 18 * 12.9 <= yMouse <= GlobalHWVar.gsy // 18 * 14.1:
                if GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(False)
                cursoreSuFrecciaDestra = True
            else:
                if not GlobalHWVar.mouseBloccato:
                    GlobalHWVar.configuraCursore(True)
            if GlobalHWVar.gsx // 32 * 1 <= xMouse <= GlobalHWVar.gsx // 32 * 31:
                if GlobalHWVar.gsy // 18 * 4.3 <= yMouse <= GlobalHWVar.gsy // 18 * 5.7:
                    voceMarcata = 1
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 4.8
                elif GlobalHWVar.gsy // 18 * 5.7 <= yMouse <= GlobalHWVar.gsy // 18 * 7.1:
                    voceMarcata = 2
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 6.2
                elif GlobalHWVar.gsy // 18 * 7.1 <= yMouse <= GlobalHWVar.gsy // 18 * 8.5:
                    voceMarcata = 3
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 7.6
                elif GlobalHWVar.gsy // 18 * 8.5 <= yMouse <= GlobalHWVar.gsy // 18 * 9.9:
                    voceMarcata = 4
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 9
                elif GlobalHWVar.gsy // 18 * 9.9 <= yMouse <= GlobalHWVar.gsy // 18 * 11.3:
                    voceMarcata = 5
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 10.4
                elif GlobalHWVar.gsy // 18 * 11.3 <= yMouse <= GlobalHWVar.gsy // 18 * 12.7:
                    voceMarcata = 6
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 11.8
                elif GlobalHWVar.gsy // 18 * 12.7 <= yMouse <= GlobalHWVar.gsy // 18 * 14.1:
                    voceMarcata = 7
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = GlobalHWVar.gsy // 18 * 13.2
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
        elif bottoneDown == pygame.K_SPACE or (bottoneDown == "mouseSinistro" and not GlobalHWVar.mouseBloccato) or bottoneDown == "padCroce":
            if not (bottoneDown == "mouseSinistro" and (cursoreSuFrecciaSinistra or cursoreSuFrecciaDestra)):
                if bottoneDown == "mouseSinistro" and suTornaIndietro:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                elif bottoneDown == "mouseSinistro" and cursoreSuImpoTastiera:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    settaTastiera()
                elif voceMarcata == 3 and not bottoneDown == "mouseSinistro":
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    settaTastiera()
                    primoFrame = True
                elif bottoneDown == "mouseSinistro" and cursoreSuImpoController:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    settaController(arrivatoDaMenuPrincipale)
                    primoFrame = True
                elif voceMarcata == 4 and not bottoneDown == "mouseSinistro":
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    settaController(arrivatoDaMenuPrincipale)
                    primoFrame = True
                elif voceMarcata == 8:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selezione)
                    GlobalHWVar.linguaImpostata = linguaTemp
                    GlobalHWVar.volumeEffetti = volumeEffettiTemp / 10.0
                    GlobalHWVar.volumeCanzoni = volumeEffettiTemp / 10.0
                    GlobalHWVar.vSyncEnabled = vSyncTemp
                    GlobalHWVar.initVolumeSounds()
                    if dimezzaVolumeCanzone:
                        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2.0)
                        GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti / 3.0)
                    if GlobalHWVar.gsx != gsxTemp or GlobalHWVar.gsy != gsyTemp or GlobalHWVar.modalitaSchermo != modalitaSchermoTemp:
                        ricaricaImgs = False
                        if GlobalHWVar.gsx != gsxTemp or GlobalHWVar.gsy != gsyTemp:
                            ricaricaImgs = True
                        GlobalHWVar.modalitaSchermo = modalitaSchermoTemp
                        GlobalHWVar.gsx = gsxTemp
                        GlobalHWVar.gsy = gsyTemp
                        GlobalHWVar.gpx = GlobalHWVar.gsx // 32
                        GlobalHWVar.gpy = GlobalHWVar.gsy // 18
                        if GlobalHWVar.modalitaSchermo == 0:
                            opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
                            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx, GlobalHWVar.gsy), opzioni_schermo)
                        elif GlobalHWVar.modalitaSchermo == 1:
                            opzioni_schermo = pygame.DOUBLEBUF
                            if not (GlobalHWVar.gsx == GlobalHWVar.maxGsx and GlobalHWVar.gsy == GlobalHWVar.maxGsy):
                                os.environ['SDL_VIDEO_WINDOW_POS'] = str((GlobalHWVar.maxGsx // 2) - (GlobalHWVar.gsx // 2)) + "," + str((GlobalHWVar.maxGsy // 2) - (GlobalHWVar.gsy // 2))
                            else:
                                os.environ['SDL_VIDEO_WINDOW_POS'] = str((GlobalHWVar.maxGsx // 2) - (GlobalHWVar.gsx // 2)) + "," + str((GlobalHWVar.maxGsy // 2) - (GlobalHWVar.gsy // 2) + (GlobalHWVar.gpy // 3))
                            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx + 1, GlobalHWVar.gsy), opzioni_schermo)
                            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx, GlobalHWVar.gsy), opzioni_schermo)
                            pygame.display.set_caption(GlobalHWVar.titolo)
                            pygame.display.set_icon(GlobalHWVar.icona)
                        else:
                            opzioni_schermo = pygame.NOFRAME | pygame.DOUBLEBUF
                            if GlobalHWVar.gsx == GlobalHWVar.maxGsx and GlobalHWVar.gsy == GlobalHWVar.maxGsy:
                                os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
                                GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx + 1, GlobalHWVar.gsy), opzioni_schermo)
                            GlobalHWVar.schermo = pygame.display.set_mode((GlobalHWVar.gsx, GlobalHWVar.gsy), opzioni_schermo)
                        if ricaricaImgs:
                            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                            FunzioniGraficheGeneriche.messaggio("Cambio risoluzione in corso...", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7.5, 120, centrale=True)
                            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
                            GlobalGameVar.numImgCaricata = 0
                            GlobalImgVar.loadImgs(GlobalGameVar.numImgCaricata, cambioRisoluzione=True)
                            if not arrivatoDaMenuPrincipale:
                                # aggiorna img mappa, protagonista
                                GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgMappaAttuale"] = False
                                GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaStartAttuale"] = False
                                GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaMenuOggettiAttuale"] = False
                                GlobalGameVar.nomiImgDaAggiornareAvanzandoStoriaAttuali["imgProtagonistaDialogoAttuale"] = False
                                SetImgOggettiMappaPersonaggi.settaImgMappa(avanzamentoStoria)
                                SetImgOggettiMappaPersonaggi.setImgMenuStartProtagonista(avanzamentoStoria)
                                SetImgOggettiMappaPersonaggi.setImgMenuOggettiProtagonista(avanzamentoStoria)
                                SetImgOggettiMappaPersonaggi.setImgDialogoProtagonista(avanzamentoStoria)
                                cambiatoRisoluzione = True
                            GlobalGameVar.schemataDiCaricamento = CaricaFileProgetto.loadImage("Risorse/Immagini/DecorazioniMenu/SchermataDiCaricamento.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
                            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.spostapun)
                    # salvo in un file la configurazione (ordine => lingua, volEffetti, volCanzoni, modalitaSchermo, gsx, gsy)
                    scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Impostazioni/Impostazioni.txt", "w")
                    if GlobalHWVar.linguaImpostata == "ita":
                        scrivi.write("0_")
                    elif GlobalHWVar.linguaImpostata == "eng":
                        scrivi.write("1_")
                    scrivi.write(str(int(GlobalHWVar.volumeEffetti * 10)) + "_")
                    scrivi.write(str(int(GlobalHWVar.volumeCanzoni * 10)) + "_")
                    scrivi.write(str(GlobalHWVar.modalitaSchermo) + "_")
                    scrivi.write(str(GlobalHWVar.gsx) + "_")
                    scrivi.write(str(GlobalHWVar.gsy) + "_")
                    scrivi.close()
                    puntatore = GlobalImgVar.puntatore
                    yp = GlobalHWVar.gsy // 18 * 15.2
                    xp = GlobalHWVar.gsx // 32 * 11.9
                    primoFrame = True
                elif voceMarcata == 9:
                    GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selind)
                    risposta = True
                else:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
                bottoneDown = False
        elif bottoneDown == "mouseSinistro" and GlobalHWVar.mouseBloccato:
            GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
            bottoneDown = False
        tastoMovimentoPremuto = False
        if bottoneDown == "mouseSinistro" or bottoneDown == pygame.K_s or bottoneDown == pygame.K_w or bottoneDown == "padGiu" or bottoneDown == "padSu" or ((voceMarcata != 3 and voceMarcata != 4) and (bottoneDown == pygame.K_d or bottoneDown == pygame.K_a or bottoneDown == "padDestra" or bottoneDown == "padSinistra")):
            tastoMovimentoPremuto = True
        elif bottoneDown:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.selimp)
            bottoneDown = False

        if aggiornaSchermo or primoMovimento or (tastoMovimentoPremuto and tastotempfps == 0) or primoFrame or voceMarcataVecchia != voceMarcata or aggiornaInterfacciaPerCambioInput:
            aggiornaSchermo = False
            if (bottoneDown == pygame.K_w or bottoneDown == "padSu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6 or voceMarcata == 7:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = yp - GlobalHWVar.gsy // 18 * 1.4
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 8:
                    voceMarcata -= 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 13.2
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 9:
                    voceMarcata -= 2
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 13.2
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 1:
                    voceMarcata += 7
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 15.2
                    xp = GlobalHWVar.gsx // 32 * 11.9
            if (bottoneDown == pygame.K_a or bottoneDown == "padSinistra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "ita":
                        linguaTemp = "eng"
                    elif linguaTemp == "eng":
                        linguaTemp = "ita"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if len(GlobalHWVar.listaRisoluzioniDisponibili) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == GlobalHWVar.listaRisoluzioniDisponibili[0][0]:
                            gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[len(GlobalHWVar.listaRisoluzioniDisponibili) - 1][0]
                            gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[len(GlobalHWVar.listaRisoluzioniDisponibili) - 1][1]
                        else:
                            i = len(GlobalHWVar.listaRisoluzioniDisponibili) - 1
                            while i >= 0:
                                if GlobalHWVar.listaRisoluzioniDisponibili[i][0] < gsxTemp:
                                    gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][0]
                                    gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][1]
                                    break
                                i -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if modalitaSchermoTemp == 0:
                        modalitaSchermoTemp = 2
                    elif modalitaSchermoTemp == 1:
                        modalitaSchermoTemp = 0
                    else:
                        modalitaSchermoTemp = 1
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if vSyncTemp:
                        vSyncTemp = False
                    else:
                        vSyncTemp = True
                elif voceMarcata == 8:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    xp = GlobalHWVar.gsx // 32 * 16
                elif voceMarcata == 9:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    xp = GlobalHWVar.gsx // 32 * 11.9
            if (bottoneDown == pygame.K_s or bottoneDown == "padGiu") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1 or voceMarcata == 2 or voceMarcata == 3 or voceMarcata == 4 or voceMarcata == 5 or voceMarcata == 6:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    xp = GlobalHWVar.gsx // 32 * 1
                    yp = yp + GlobalHWVar.gsy // 18 * 1.4
                elif voceMarcata == 7:
                    voceMarcata += 1
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 15.2
                    xp = GlobalHWVar.gsx // 32 * 11.9
                elif voceMarcata == 8:
                    voceMarcata -= 7
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 4.8
                    xp = GlobalHWVar.gsx // 32 * 1
                elif voceMarcata == 9:
                    voceMarcata -= 8
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    yp = GlobalHWVar.gsy // 18 * 4.8
                    xp = GlobalHWVar.gsx // 32 * 1
            if (bottoneDown == pygame.K_d or bottoneDown == "padDestra") and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "ita":
                        linguaTemp = "eng"
                    elif linguaTemp == "eng":
                        linguaTemp = "ita"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if len(GlobalHWVar.listaRisoluzioniDisponibili) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == GlobalHWVar.listaRisoluzioniDisponibili[len(GlobalHWVar.listaRisoluzioniDisponibili) - 1][0]:
                            gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[0][0]
                            gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[0][1]
                        else:
                            i = 0
                            while i < len(GlobalHWVar.listaRisoluzioniDisponibili):
                                if GlobalHWVar.listaRisoluzioniDisponibili[i][0] > gsxTemp:
                                    gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][0]
                                    gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][1]
                                    break
                                i += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if modalitaSchermoTemp == 0:
                        modalitaSchermoTemp = 1
                    elif modalitaSchermoTemp == 1:
                        modalitaSchermoTemp = 2
                    else:
                        modalitaSchermoTemp = 0
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if vSyncTemp:
                        vSyncTemp = False
                    else:
                        vSyncTemp = True
                elif voceMarcata == 8:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata += 1
                    xp = GlobalHWVar.gsx // 32 * 16
                elif voceMarcata == 9:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    voceMarcata -= 1
                    xp = GlobalHWVar.gsx // 32 * 11.9
            if bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "ita":
                        linguaTemp = "eng"
                    elif linguaTemp == "eng":
                        linguaTemp = "ita"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 0:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if len(GlobalHWVar.listaRisoluzioniDisponibili) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == GlobalHWVar.listaRisoluzioniDisponibili[0][0]:
                            gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[len(GlobalHWVar.listaRisoluzioniDisponibili) - 1][0]
                            gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[len(GlobalHWVar.listaRisoluzioniDisponibili) - 1][1]
                        else:
                            i = len(GlobalHWVar.listaRisoluzioniDisponibili) - 1
                            while i >= 0:
                                if GlobalHWVar.listaRisoluzioniDisponibili[i][0] < gsxTemp:
                                    gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][0]
                                    gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][1]
                                    break
                                i -= 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if modalitaSchermoTemp == 0:
                        modalitaSchermoTemp = 2
                    elif modalitaSchermoTemp == 1:
                        modalitaSchermoTemp = 0
                    else:
                        modalitaSchermoTemp = 1
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if vSyncTemp:
                        vSyncTemp = False
                    else:
                        vSyncTemp = True
            if bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra and (tastotempfps == 0 or primoMovimento):
                if voceMarcata == 1:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if linguaTemp == "ita":
                        linguaTemp = "eng"
                    elif linguaTemp == "eng":
                        linguaTemp = "ita"
                elif voceMarcata == 2:
                    if volumeEffettiTemp != 10:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        volumeEffettiTemp += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 5:
                    if len(GlobalHWVar.listaRisoluzioniDisponibili) > 1:
                        GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                        if gsxTemp == GlobalHWVar.listaRisoluzioniDisponibili[len(GlobalHWVar.listaRisoluzioniDisponibili) - 1][0]:
                            gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[0][0]
                            gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[0][1]
                        else:
                            i = 0
                            while i < len(GlobalHWVar.listaRisoluzioniDisponibili):
                                if GlobalHWVar.listaRisoluzioniDisponibili[i][0] > gsxTemp:
                                    gsxTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][0]
                                    gsyTemp = GlobalHWVar.listaRisoluzioniDisponibili[i][1]
                                    break
                                i += 1
                    else:
                        GlobalHWVar.canaleSoundPuntatoreSeleziona.play(GlobalSndVar.selimp)
                elif voceMarcata == 6:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if modalitaSchermoTemp == 0:
                        modalitaSchermoTemp = 1
                    elif modalitaSchermoTemp == 1:
                        modalitaSchermoTemp = 2
                    else:
                        modalitaSchermoTemp = 0
                elif voceMarcata == 7:
                    GlobalHWVar.canaleSoundPuntatoreSposta.play(GlobalSndVar.spostapun)
                    if vSyncTemp:
                        vSyncTemp = False
                    else:
                        vSyncTemp = True
            if not primoMovimento and tastoMovimentoPremuto:
                tastotempfps = 2

            if primoFrame:
                aggiornaInterfacciaPerCambioInput = True
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu)
                FunzioniGraficheGeneriche.messaggio("Impostazioni", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 1, 150)
                # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoAltoDestra, (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 4))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoDestra, (GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 15.5))
                GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.sfondoTriangolinoBassoSinistra, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15.5))
                FunzioniGraficheGeneriche.messaggio("Lingua", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4.7, 60)
                FunzioniGraficheGeneriche.messaggio("Volume audio", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6.1, 60)
                FunzioniGraficheGeneriche.messaggio("Tastiera", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7.5, 60)
                FunzioniGraficheGeneriche.messaggio("Controller", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8.9, 60)
                FunzioniGraficheGeneriche.messaggio("Risoluzione", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10.3, 60)
                FunzioniGraficheGeneriche.messaggio(u"Modalità finestra", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11.7, 60)
                FunzioniGraficheGeneriche.messaggio("VSync", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13.1, 60)
                FunzioniGraficheGeneriche.messaggio("Salva", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 12.8, GlobalHWVar.gsy // 18 * 15, 70)
                FunzioniGraficheGeneriche.messaggio("Indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 16.9, GlobalHWVar.gsy // 18 * 15, 70)
            else:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 9.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5.55, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6.95, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8.35, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 9.75, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 11.15, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 12.55, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 13.95, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14.35, GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 0.3))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4.5, GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 11.9, GlobalHWVar.gsy // 18 * 15.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigio, (GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15.2, GlobalHWVar.gsx // 32 * 0.5, GlobalHWVar.gsy // 18 * 0.5))
            if aggiornaInterfacciaPerCambioInput:
                aggiornaInterfacciaPerCambioInput = False
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (GlobalHWVar.gsx // 32 * 21, 0, GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2.5))
                if GlobalHWVar.mouseVisibile:
                    FunzioniGraficheGeneriche.messaggio("Tasto destro: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 22.5, GlobalHWVar.gsy // 18 * 1, 50)
                elif GlobalHWVar.usandoIlController:
                    FunzioniGraficheGeneriche.messaggio("Cerchio: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 23.5, GlobalHWVar.gsy // 18 * 1, 50)
                else:
                    FunzioniGraficheGeneriche.messaggio("Q: torna indietro", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, 50)

            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 4.3), ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 14.23), 2)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 14.65), ((GlobalHWVar.gpx * 16) - 1, GlobalHWVar.gpy * 16.2), 2)

            if linguaTemp == "ita":
                FunzioniGraficheGeneriche.messaggio("Italiano", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4.7, 60)
            if linguaTemp == "eng":
                FunzioniGraficheGeneriche.messaggio("English", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4.7, 60)
            if voceMarcata == 1:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 4.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 4.6))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 19.9, GlobalHWVar.gsy // 18 * 4.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 19.9, GlobalHWVar.gsy // 18 * 4.6))
            FunzioniGraficheGeneriche.messaggio(str(int(volumeEffettiTemp)), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 6.1, 60)
            if voceMarcata == 2:
                if volumeEffettiTemp != 0:
                    if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 6))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 6))
                if volumeEffettiTemp != 10:
                    if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 6))
                    else:
                        GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 18.2, GlobalHWVar.gsy // 18 * 6))
            FunzioniGraficheGeneriche.messaggio("Configura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 7.5, 60)
            FunzioniGraficheGeneriche.messaggio("Configura", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8.9, 60)
            FunzioniGraficheGeneriche.messaggio(str(gsxTemp) + u"×" + str(gsyTemp), GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 10.3, 60)
            if voceMarcata == 5:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 10.2))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 10.2))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 10.2))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 21.2, GlobalHWVar.gsy // 18 * 10.2))
            if modalitaSchermoTemp == 0:
                FunzioniGraficheGeneriche.messaggio(u"Schermo intero", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11.7, 60)
            elif modalitaSchermoTemp == 1:
                FunzioniGraficheGeneriche.messaggio(u"Finestra", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11.7, 60)
            else:
                FunzioniGraficheGeneriche.messaggio("Finestra senza bordi", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11.7, 60)
            if voceMarcata == 6:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 11.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 11.6))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 23.9, GlobalHWVar.gsy // 18 * 11.6))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 23.9, GlobalHWVar.gsy // 18 * 11.6))
            if vSyncTemp:
                FunzioniGraficheGeneriche.messaggio(u"Attivato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13.1, 60)
            else:
                FunzioniGraficheGeneriche.messaggio(u"Disattivato", GlobalHWVar.grigiochi, GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13.1, 60)
            if voceMarcata == 7:
                if bottoneDown == pygame.K_a or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaSinistra) or bottoneDown == "padSinistra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistraBloccato, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 13))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniSinistra, (GlobalHWVar.gsx // 32 * 15.7, GlobalHWVar.gsy // 18 * 13))
                if bottoneDown == pygame.K_d or (bottoneDown == "mouseSinistro" and cursoreSuFrecciaDestra) or bottoneDown == "padDestra":
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestraBloccato, (GlobalHWVar.gsx // 32 * 20.9, GlobalHWVar.gsy // 18 * 13))
                else:
                    GlobalHWVar.disegnaImmagineSuSchermo(GlobalImgVar.puntatoreImpostazioniDestra, (GlobalHWVar.gsx // 32 * 20.9, GlobalHWVar.gsy // 18 * 13))

            GlobalHWVar.disegnaImmagineSuSchermo(puntatore, (xp, yp))
            if voceMarcata != 8 and voceMarcata != 9:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 0.5))), yp + (int(GlobalHWVar.gpy * 0.9)) - 1), (xp + (int(GlobalHWVar.gpx * 14.65)), yp + (int(GlobalHWVar.gpy * 0.9)) - 1), 2)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, ((xp + (int(GlobalHWVar.gpx * 15.3))), yp + (int(GlobalHWVar.gpy * 0.9)) - 1), (xp + (int(GlobalHWVar.gpx * 29.4)), yp + (int(GlobalHWVar.gpy * 0.9)) - 1), 2)
            else:
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigioscu, (int(GlobalHWVar.gpx * 1.5), int(GlobalHWVar.gpy * 14.45) - 1), (int(GlobalHWVar.gpx * 30.45), int(GlobalHWVar.gpy * 14.45) - 1), 2)
            primoFrame = False

            GlobalHWVar.aggiornaSchermo()

        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.clockMenu.tick(GlobalHWVar.fpsMenu)

    return cambiatoRisoluzione
