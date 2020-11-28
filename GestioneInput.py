# -*- coding: utf-8 -*-

from FadeToBlackClass import *
from SetOstacoliContenutoCofanetti import *


def getInput(bottoneDown, aggiornaInterfaccia, controllerDaConfigurare=False):
    tastoTrovato = False
    for event in pygame.event.get():
        # faccio apparire/sparire il cursore
        if event.type == pygame.KEYDOWN and (GlobalVar.mouseVisibile or GlobalVar.usandoIlController):
            GlobalVar.listaTastiPremuti = []
            GlobalVar.padUtilizzato = False
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalVar.setCursoreVisibile(False)
            GlobalVar.usandoIlController = False
        elif event.type == pygame.MOUSEBUTTONDOWN and (not GlobalVar.mouseVisibile or GlobalVar.usandoIlController):
            GlobalVar.listaTastiPremuti = []
            GlobalVar.padUtilizzato = False
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalVar.setCursoreVisibile(True)
            GlobalVar.usandoIlController = False
        elif (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION) and (GlobalVar.mouseVisibile or not GlobalVar.usandoIlController):
            padTrovato = False
            for pad in GlobalVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    buttons = pad.get_numbuttons()
                    for idTasto in range(buttons):
                        if pad.get_button(idTasto):
                            if pad != GlobalVar.padUtilizzato:
                                GlobalVar.listaTastiPremuti =[]
                                GlobalVar.inizializzaPad(pad)
                            padTrovato = True
                            break
                    if padTrovato:
                        break
            for pad in GlobalVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    hats = pad.get_numhats()
                    for idCroceDirezionale in range(hats):
                        hat = pad.get_hat(idCroceDirezionale)
                        direzioneX, direzioneY = hat
                        if direzioneX != 0 or direzioneY != 0:
                            if pad != GlobalVar.padUtilizzato:
                                GlobalVar.listaTastiPremuti =[]
                                GlobalVar.inizializzaPad(pad)
                            padTrovato = True
                            break
                    if padTrovato:
                        break
            if padTrovato:
                tastoTrovato = True
                aggiornaInterfaccia = True
                bottoneDown = False
                GlobalVar.setCursoreVisibile(False)
                GlobalVar.usandoIlController = True

        # esco dal gioco
        if event.type == pygame.QUIT:
            tastoTrovato = True
            pygame.quit()
            GlobalVar.quit()

        # tasto tastiera
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
                GlobalVar.listaTastiPremuti.append(bottoneDown)

            if event.type == pygame.KEYUP and event.key in GlobalVar.listaTastiPremuti:
                GlobalVar.listaTastiPremuti.remove(event.key)

            if len(GlobalVar.listaTastiPremuti) == 0:
                bottoneDown = False

        # tasto mouse
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and not tastoTrovato:
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            tastoTrovato = True

            if not sinistroMouse and "mouseSinistro" in GlobalVar.listaTastiPremuti:
                GlobalVar.listaTastiPremuti.remove("mouseSinistro")
            if not centraleMouse and "mouseCentrale" in GlobalVar.listaTastiPremuti:
                GlobalVar.listaTastiPremuti.remove("mouseCentrale")
            if not destroMouse and "mouseDestro" in GlobalVar.listaTastiPremuti:
                GlobalVar.listaTastiPremuti.remove("mouseDestro")

            if sinistroMouse and not "mouseSinistro" in GlobalVar.listaTastiPremuti:
                bottoneDown = "mouseSinistro"
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            elif destroMouse and not "mouseDestro" in GlobalVar.listaTastiPremuti:
                bottoneDown = "mouseDestro"
                GlobalVar.listaTastiPremuti.append(bottoneDown)
            elif centraleMouse and not "mouseCentrale" in GlobalVar.listaTastiPremuti:
                bottoneDown = "mouseCentrale"
                GlobalVar.listaTastiPremuti.append(bottoneDown)

            if not "mouseSinistro" in GlobalVar.listaTastiPremuti and not "mouseDestro" in GlobalVar.listaTastiPremuti and not "mouseCentrale" in GlobalVar.listaTastiPremuti:
                bottoneDown = False

        # tasto joypad
        if (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP) and not tastoTrovato:
            padCambiato = False
            padTrovato = False
            for pad in GlobalVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    buttons = pad.get_numbuttons()
                    for idTasto in range(buttons):
                        if pad.get_button(idTasto):
                            if pad != GlobalVar.padUtilizzato:
                                GlobalVar.listaTastiPremuti =[]
                                GlobalVar.inizializzaPad(pad)
                                padCambiato = True
                            padTrovato = True
                            break
                    if padTrovato:
                        break

            if not padCambiato and GlobalVar.padUtilizzato and GlobalVar.padUtilizzato != controllerDaConfigurare:
                buttons = GlobalVar.padUtilizzato.get_numbuttons()
                for idTasto in range(buttons):
                    button = GlobalVar.padUtilizzato.get_button(idTasto)
                    if button and not idTasto in GlobalVar.configPadInUso[2]:
                        tastoTrovato = True
                        bottoneDown = False
                    if button:
                        if idTasto == GlobalVar.configPadInUso[2][0] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padCroce"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalVar.configPadInUso[2][1] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padCerchio"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalVar.configPadInUso[2][2] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padQuadrato"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalVar.configPadInUso[2][3] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padTriangolo"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalVar.configPadInUso[2][4] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padL1"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalVar.configPadInUso[2][5] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padR1"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                        elif idTasto == GlobalVar.configPadInUso[2][6] and not idTasto in GlobalVar.listaTastiPremuti:
                            tastoTrovato = True
                            bottoneDown = "padStart"
                            GlobalVar.listaTastiPremuti.append(idTasto)
                    elif idTasto in GlobalVar.listaTastiPremuti:
                        GlobalVar.listaTastiPremuti.remove(idTasto)

            if len(GlobalVar.listaTastiPremuti) == 0:
                bottoneDown = False
        if event.type == pygame.JOYHATMOTION and not tastoTrovato:
            padCambiato = False
            padTrovato = False
            for pad in GlobalVar.listaPadConnessiConfigurati:
                if controllerDaConfigurare != pad:
                    hats = pad.get_numhats()
                    for idCroceDirezionale in range(hats):
                        hat = pad.get_hat(idCroceDirezionale)
                        direzioneX, direzioneY = hat
                        if direzioneX != 0 or direzioneY != 0:
                            if pad != GlobalVar.padUtilizzato:
                                GlobalVar.listaTastiPremuti =[]
                                GlobalVar.inizializzaPad(pad)
                                padCambiato = True
                            padTrovato = True
                            break
                    if padTrovato:
                        break

            if not padCambiato and GlobalVar.padUtilizzato and GlobalVar.padUtilizzato != controllerDaConfigurare:
                hats = GlobalVar.padUtilizzato.get_numhats()
                for idCroceDirezionale in range(hats):
                    if idCroceDirezionale == GlobalVar.configPadInUso[3]:
                        hat = GlobalVar.padUtilizzato.get_hat(idCroceDirezionale)
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
