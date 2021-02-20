# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar


def getInput(bottoneDown, aggiornaInterfaccia, controllerDaConfigurare=False):
    tastoTrovato = False
    for event in pygame.event.get():
        # faccio apparire/sparire il cursore
        if event.type == pygame.KEYDOWN and (GlobalHWVar.mouseVisibile or GlobalHWVar.usandoIlController):
            GlobalHWVar.listaTastiPremuti = []
            GlobalHWVar.padUtilizzato = False
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalHWVar.setCursoreVisibile(False)
            GlobalHWVar.usandoIlController = False
        elif event.type == pygame.MOUSEBUTTONDOWN and (not GlobalHWVar.mouseVisibile or GlobalHWVar.usandoIlController):
            GlobalHWVar.listaTastiPremuti = []
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)

            if event.type == pygame.KEYUP and event.key in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove(event.key)

            if len(GlobalHWVar.listaTastiPremuti) == 0:
                bottoneDown = False

        # tasto mouse
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and not tastoTrovato:
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            tastoTrovato = True

            if not sinistroMouse and "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove("mouseSinistro")
            if not centraleMouse and "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove("mouseCentrale")
            if not destroMouse and "mouseDestro" in GlobalHWVar.listaTastiPremuti:
                GlobalHWVar.listaTastiPremuti.remove("mouseDestro")

            if sinistroMouse and not "mouseSinistro" in GlobalHWVar.listaTastiPremuti:
                bottoneDown = "mouseSinistro"
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            elif destroMouse and not "mouseDestro" in GlobalHWVar.listaTastiPremuti:
                bottoneDown = "mouseDestro"
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)
            elif centraleMouse and not "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                bottoneDown = "mouseCentrale"
                GlobalHWVar.listaTastiPremuti.append(bottoneDown)

            if not "mouseSinistro" in GlobalHWVar.listaTastiPremuti and not "mouseDestro" in GlobalHWVar.listaTastiPremuti and not "mouseCentrale" in GlobalHWVar.listaTastiPremuti:
                bottoneDown = False

        # tasto joypad
        if (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP) and not tastoTrovato:
            padCambiato = False
            padTrovato = False
            for pad in GlobalHWVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    buttons = pad.get_numbuttons()
                    for idTasto in range(buttons):
                        if pad.get_button(idTasto):
                            if pad != GlobalHWVar.padUtilizzato:
                                GlobalHWVar.listaTastiPremuti =[]
                                GlobalHWVar.inizializzaPad(pad)
                                padCambiato = True
                            padTrovato = True
                            break
                    if padTrovato:
                        break

            if not padCambiato and GlobalHWVar.padUtilizzato and GlobalHWVar.padUtilizzato != controllerDaConfigurare:
                buttons = GlobalHWVar.padUtilizzato.get_numbuttons()
                for idTasto in range(buttons):
                    button = GlobalHWVar.padUtilizzato.get_button(idTasto)
                    if button and not idTasto in GlobalHWVar.configPadInUso[2]:
                        tastoTrovato = True
                        bottoneDown = False
                    if button:
                        if idTasto == GlobalHWVar.configPadInUso[2][0] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padCroce"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalHWVar.configPadInUso[2][1] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padCerchio"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalHWVar.configPadInUso[2][2] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padQuadrato"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalHWVar.configPadInUso[2][3] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padTriangolo"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalHWVar.configPadInUso[2][4] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padL1"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalHWVar.configPadInUso[2][5] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padR1"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalHWVar.configPadInUso[2][6] and not idTasto in GlobalHWVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padStart"
                            GlobalHWVar.listaTastiPremuti.append(idTasto)
                    elif idTasto in GlobalHWVar.listaTastiPremuti:
                        GlobalHWVar.listaTastiPremuti.remove(idTasto)

            if len(GlobalHWVar.listaTastiPremuti) == 0:
                bottoneDown = False
        if event.type == pygame.JOYHATMOTION and not tastoTrovato:
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
                                GlobalHWVar.listaTastiPremuti =[]
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
                        hat = GlobalHWVar.padUtilizzato.get_hat(idCroceDirezionale)
                        if not tastoTrovato:
                            direzioneX, direzioneY = hat
                            bottoneDown = False
                            if direzioneX == 1:
                                tastoTrovato = True
                                bottoneDown = "padDestra"
                            elif direzioneX == -1:
                                tastoTrovato = True
                                bottoneDown = "padSinistra"
                            elif direzioneY == 1:
                                tastoTrovato = True
                                bottoneDown = "padSu"
                            elif direzioneY == -1:
                                tastoTrovato = True
                                bottoneDown = "padGiu"

    return bottoneDown, aggiornaInterfaccia
