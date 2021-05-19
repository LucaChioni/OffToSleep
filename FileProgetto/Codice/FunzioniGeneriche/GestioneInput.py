# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar


def getInput(bottoneDown, aggiornaInterfaccia, controllerDaConfigurare=False, gestioneDuranteLePause=False):
    if controllerDaConfigurare:
        GlobalHWVar.listaInputInSospeso = []
    if not gestioneDuranteLePause and len(GlobalHWVar.listaInputInSospeso) > 0:
        for inputInSospeso in GlobalHWVar.listaInputInSospeso:
            if inputInSospeso.endswith("Up") and str(bottoneDown) == inputInSospeso[:-2]:
                bottoneDown = False
            elif inputInSospeso.endswith("Down"):
                bottoneDown = inputInSospeso[:-4]
                if not (GlobalHWVar.mouseVisibile or GlobalHWVar.usandoIlController):
                    bottoneDown = int(bottoneDown)
        GlobalHWVar.listaInputInSospeso = []

    tastoTrovato = False
    for event in pygame.event.get():
        # faccio apparire/sparire il cursore
        if event.type == pygame.KEYDOWN and (GlobalHWVar.mouseVisibile or GlobalHWVar.usandoIlController):
            GlobalHWVar.listaTastiPremuti = []
            GlobalHWVar.listaInputInSospeso = []
            GlobalHWVar.padUtilizzato = False
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalHWVar.setCursoreVisibile(False)
            GlobalHWVar.usandoIlController = False
        elif event.type == pygame.MOUSEBUTTONDOWN and (not GlobalHWVar.mouseVisibile or GlobalHWVar.usandoIlController):
            GlobalHWVar.listaTastiPremuti = []
            GlobalHWVar.listaInputInSospeso = []
            GlobalHWVar.padUtilizzato = False
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalHWVar.setCursoreVisibile(True)
            GlobalHWVar.usandoIlController = False
        elif (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION) and (GlobalHWVar.mouseVisibile or not GlobalHWVar.usandoIlController):
            padTrovato = False
            for pad in GlobalHWVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    buttons = pad.get_numbuttons()
                    for idTasto in range(buttons):
                        if pad.get_button(idTasto):
                            if pad != GlobalHWVar.padUtilizzato:
                                GlobalHWVar.inizializzaPad(pad)
                            padTrovato = True
                            break
                    if padTrovato:
                        break
            for pad in GlobalHWVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    hats = pad.get_numhats()
                    for idCroceDirezionale in range(hats):
                        hat = pad.get_hat(idCroceDirezionale)
                        direzioneX, direzioneY = hat
                        if direzioneX != 0 or direzioneY != 0:
                            if pad != GlobalHWVar.padUtilizzato:
                                GlobalHWVar.inizializzaPad(pad)
                            padTrovato = True
                            break
                    if padTrovato:
                        break
            if padTrovato:
                GlobalHWVar.listaTastiPremuti = []
                GlobalHWVar.listaInputInSospeso = []
                tastoTrovato = True
                aggiornaInterfaccia = True
                bottoneDown = False
                GlobalHWVar.setCursoreVisibile(False)
                GlobalHWVar.usandoIlController = True

        # esco dal gioco
        if event.type == pygame.QUIT:
            tastoTrovato = True
            pygame.quit()
            GlobalHWVar.quit()

        # tasto tastiera
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_3 or event.key == pygame.K_KP3):
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2):
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                GlobalHWVar.listaTastiPremuti.append(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Down")
                elif not tastoTrovato:
                    bottoneDown = event.key
                tastoTrovato = True

            if event.type == pygame.KEYUP and event.key in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove(event.key)
                if gestioneDuranteLePause:
                    GlobalHWVar.listaInputInSospeso.append(str(event.key) + "Up")

            if event.type == pygame.KEYUP and event.key == bottoneDown:
                bottoneDown = False

        # tasto mouse
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()

            if gestioneDuranteLePause:
                if not sinistroMouse and "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
                    GlobalHWVar.listaInputInSospeso.append("mouseSinistroUp")
                if not centraleMouse and "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                    GlobalHWVar.listaInputInSospeso.append("mouseCentraleUp")
                if not destroMouse and "mouseDestro" in GlobalHWVar.listaTastiPremuti:
                    GlobalHWVar.listaInputInSospeso.append("mouseDestroUp")

                if sinistroMouse and not "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
                    GlobalHWVar.listaInputInSospeso.append("mouseSinistroDown")
                elif destroMouse and not "mouseDestro" in GlobalHWVar.listaTastiPremuti:
                    GlobalHWVar.listaInputInSospeso.append("mouseDestroDown")
                elif centraleMouse and not "mouseCentraleDown" in GlobalHWVar.listaTastiPremuti:
                    GlobalHWVar.listaInputInSospeso.append("mouseCentraleDown")
            else:
                if sinistroMouse and not "mouseSinistro" in GlobalHWVar.listaTastiPremuti and not tastoTrovato:
                    bottoneDown = "mouseSinistro"
                    tastoTrovato = True
                if destroMouse and not "mouseDestro" in GlobalHWVar.listaTastiPremuti and not tastoTrovato:
                    bottoneDown = "mouseDestro"
                    tastoTrovato = True
                if centraleMouse and not "mouseCentrale" in GlobalHWVar.listaTastiPremuti and not tastoTrovato:
                    bottoneDown = "mouseCentrale"
                    tastoTrovato = True

            if not sinistroMouse and "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove("mouseSinistro")
            if not centraleMouse and "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove("mouseCentrale")
            if not destroMouse and "mouseDestro" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove("mouseDestro")

            if sinistroMouse and not "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.append("mouseSinistro")
            if centraleMouse and not "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.append("mouseCentrale")
            if destroMouse and not "mouseDestro" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.append("mouseDestro")

            if not "mouseSinistro" in GlobalHWVar.listaTastiPremuti and not "mouseDestro" in GlobalHWVar.listaTastiPremuti and not "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                bottoneDown = False

        # tasto joypad
        if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
            padCambiato = False
            padTrovato = False
            for pad in GlobalHWVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    buttons = pad.get_numbuttons()
                    for idTasto in range(buttons):
                        if pad.get_button(idTasto):
                            if pad != GlobalHWVar.padUtilizzato:
                                GlobalHWVar.listaTastiPremuti = []
                                GlobalHWVar.inizializzaPad(pad)
                                padCambiato = True
                            padTrovato = True
                            break
                    if padTrovato:
                        break

            if not padCambiato and GlobalHWVar.padUtilizzato and GlobalHWVar.padUtilizzato != controllerDaConfigurare:
                buttons = GlobalHWVar.padUtilizzato.get_numbuttons()
                for idTasto in range(buttons):
                    if idTasto in GlobalHWVar.configPadInUso[2]:
                        button = GlobalHWVar.padUtilizzato.get_button(idTasto)
                        if button:
                            if idTasto == GlobalHWVar.configPadInUso[2][0] and not "padCroce" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padCroceDown")
                                elif not tastoTrovato:
                                    bottoneDown = "padCroce"
                                GlobalHWVar.listaTastiPremuti.append("padCroce")
                                tastoTrovato = True
                            if idTasto == GlobalHWVar.configPadInUso[2][1] and not "padCerchio" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padCerchioDown")
                                elif not tastoTrovato:
                                    bottoneDown = "padCerchio"
                                GlobalHWVar.listaTastiPremuti.append("padCerchio")
                                tastoTrovato = True
                            if idTasto == GlobalHWVar.configPadInUso[2][2] and not "padQuadrato" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padQuadratoDown")
                                elif not tastoTrovato:
                                    bottoneDown = "padQuadrato"
                                GlobalHWVar.listaTastiPremuti.append("padQuadrato")
                                tastoTrovato = True
                            if idTasto == GlobalHWVar.configPadInUso[2][3] and not "padTriangolo" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padTriangoloDown")
                                elif not tastoTrovato:
                                    bottoneDown = "padTriangolo"
                                GlobalHWVar.listaTastiPremuti.append("padTriangolo")
                                tastoTrovato = True
                            if idTasto == GlobalHWVar.configPadInUso[2][4] and not "padL1" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padL1Down")
                                elif not tastoTrovato:
                                    bottoneDown = "padL1"
                                GlobalHWVar.listaTastiPremuti.append("padL1")
                                tastoTrovato = True
                            if idTasto == GlobalHWVar.configPadInUso[2][5] and not "padR1" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padR1Down")
                                elif not tastoTrovato:
                                    bottoneDown = "padR1"
                                GlobalHWVar.listaTastiPremuti.append("padR1")
                                tastoTrovato = True
                            if idTasto == GlobalHWVar.configPadInUso[2][6] and not "padStart" in GlobalHWVar.listaTastiPremuti:
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padStartDown")
                                elif not tastoTrovato:
                                    bottoneDown = "padStart"
                                GlobalHWVar.listaTastiPremuti.append("padStart")
                                tastoTrovato = True
                        else:
                            if idTasto == GlobalHWVar.configPadInUso[2][0] and "padCroce" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padCroce")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padCroceUp")
                            if idTasto == GlobalHWVar.configPadInUso[2][1] and "padCerchio" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padCerchio")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padCerchioUp")
                            if idTasto == GlobalHWVar.configPadInUso[2][2] and "padQuadrato" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padQuadrato")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padQuadratoUp")
                            if idTasto == GlobalHWVar.configPadInUso[2][3] and "padTriangolo" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padTriangolo")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padTriangoloUp")
                            if idTasto == GlobalHWVar.configPadInUso[2][4] and "padL1" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padL1")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padL1Up")
                            if idTasto == GlobalHWVar.configPadInUso[2][5] and "padR1" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padR1")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padR1Up")
                            if idTasto == GlobalHWVar.configPadInUso[2][6] and "padStart" in GlobalHWVar.listaTastiPremuti:
                                GlobalHWVar.listaTastiPremuti.remove("padStart")
                                if gestioneDuranteLePause:
                                    GlobalHWVar.listaInputInSospeso.append("padStartUp")

            if len(GlobalHWVar.listaTastiPremuti) == 0:
                bottoneDown = False
        if event.type == pygame.JOYHATMOTION:
            padCambiato = False
            padTrovato = False
            for pad in GlobalHWVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    hats = pad.get_numhats()
                    for idCroceDirezionale in range(hats):
                        hat = pad.get_hat(idCroceDirezionale)
                        direzioneX, direzioneY = hat
                        if direzioneX != 0 or direzioneY != 0:
                            if pad != GlobalHWVar.padUtilizzato:
                                GlobalHWVar.listaTastiPremuti = []
                                GlobalHWVar.inizializzaPad(pad)
                                padCambiato = True
                            padTrovato = True
                            break
                    if padTrovato:
                        break

            if not padCambiato and GlobalHWVar.padUtilizzato and GlobalHWVar.padUtilizzato != controllerDaConfigurare:
                hats = GlobalHWVar.padUtilizzato.get_numhats()
                for idCroceDirezionale in range(hats):
                    if idCroceDirezionale == GlobalHWVar.configPadInUso[3]:
                        if not tastoTrovato:
                            bottoneDown = False
                        hat = GlobalHWVar.padUtilizzato.get_hat(idCroceDirezionale)
                        direzioneX, direzioneY = hat
                        if direzioneX == 1 and not "padDestra" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padDestraDown")
                            elif not tastoTrovato:
                                bottoneDown = "padDestra"
                            GlobalHWVar.listaTastiPremuti.append("padDestra")
                            tastoTrovato = True
                        elif direzioneX != 1 and "padDestra" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padDestraUp")
                            GlobalHWVar.listaTastiPremuti.remove("padDestra")
                        if direzioneX == -1 and not "padSinistra" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padSinistraDown")
                            elif not tastoTrovato:
                                bottoneDown = "padSinistra"
                            GlobalHWVar.listaTastiPremuti.append("padSinistra")
                            tastoTrovato = True
                        elif direzioneX != -1 and "padSinistra" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padSinistraUp")
                            GlobalHWVar.listaTastiPremuti.remove("padSinistra")
                        if direzioneY == 1 and not "padSu" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padSuDown")
                            elif not tastoTrovato:
                                bottoneDown = "padSu"
                            GlobalHWVar.listaTastiPremuti.append("padSu")
                            tastoTrovato = True
                        elif direzioneY != 1 and "padSu" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padSuUp")
                            GlobalHWVar.listaTastiPremuti.remove("padSu")
                        if direzioneY == -1 and not "padGiu" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padGiuDown")
                            elif not tastoTrovato:
                                bottoneDown = "padGiu"
                            GlobalHWVar.listaTastiPremuti.append("padGiu")
                            tastoTrovato = True
                        elif direzioneY != -1 and "padGiu" in GlobalHWVar.listaTastiPremuti:
                            if gestioneDuranteLePause:
                                GlobalHWVar.listaInputInSospeso.append("padGiuUp")
                            GlobalHWVar.listaTastiPremuti.remove("padGiu")

    return bottoneDown, aggiornaInterfaccia
