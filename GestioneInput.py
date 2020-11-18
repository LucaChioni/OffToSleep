# -*- coding: utf-8 -*-

from FadeToBlackClass import *
from SetOstacoliContenutoCofanetti import *


def cambiaDisposizioneTastiController():
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
            for idPad in range(GlobalVar.joystick_count):
                joystick = pygame.joystick.Joystick(idPad)
                name = joystick.get_name()
                premutoCroce = False
                premutoCerchio = False
                premutoQuadrato = False
                premutoTriangolo = False
                premutoL1 = False
                premutoR1 = False
                premutoSelect = False
                premutoStart = False
                premutoL3 = False
                premutoR3 = False
                buttons = joystick.get_numbuttons()
                for idTasto in range(buttons):
                    button = joystick.get_button(idTasto)
                    if button:
                        if idTasto == 0:
                            premutoCroce = True
                        if idTasto == 1:
                            premutoCerchio = True
                        if idTasto == 2:
                            premutoQuadrato = True
                        if idTasto == 3:
                            premutoTriangolo = True
                        if idTasto == 4:
                            premutoL1 = True
                        if idTasto == 5:
                            premutoR1 = True
                        if idTasto == 6:
                            premutoSelect = True
                        if idTasto == 7:
                            premutoStart = True
                        if idTasto == 8:
                            premutoL3 = True
                        if idTasto == 9:
                            premutoR3 = True
                if premutoCroce or premutoCerchio or premutoQuadrato or premutoTriangolo or premutoL1 or premutoR1 or premutoSelect or premutoStart or premutoL3 or premutoR3:
                    print ("Nome pad: " + str(name))
                    if premutoCroce:
                        print ("Tasto premuto: croce")
                    if premutoCerchio:
                        print ("Tasto premuto: cerchio")
                    if premutoQuadrato:
                        print ("Tasto premuto: quadrato")
                    if premutoTriangolo:
                        print ("Tasto premuto: triangolo")
                    if premutoL1:
                        print ("Tasto premuto: l1")
                    if premutoR1:
                        print ("Tasto premuto: r1")
                    if premutoSelect:
                        print ("Tasto premuto: select")
                    if premutoStart:
                        print ("Tasto premuto: start")
                    if premutoL3:
                        print ("Tasto premuto: l3")
                    if premutoR3:
                        print ("Tasto premuto: r3")
                    print ("\n")
        if event.type == pygame.JOYHATMOTION:
            for idPad in range(GlobalVar.joystick_count):
                joystick = pygame.joystick.Joystick(idPad)
                name = joystick.get_name()
                hats = joystick.get_numhats()
                for idCroceDirezionale in range(hats):
                    hat = joystick.get_hat(idCroceDirezionale)
                    direzioneX, direzioneY = hat
                    if direzioneX != 0 or direzioneY != 0:
                        print ("Nome pad: " + str(name))
                        if direzioneX == 1:
                            print ("Croce direzionale " + str(idCroceDirezionale) + ": verso destra")
                        if direzioneX == -1:
                            print ("Croce direzionale " + str(idCroceDirezionale) + ": verso sinistra")
                        if direzioneY == 1:
                            print ("Croce direzionale " + str(idCroceDirezionale) + ": verso l'alto")
                        if direzioneY == -1:
                            print ("Croce direzionale " + str(idCroceDirezionale) + ": verso il basso")
                        print ("\n")
        if event.type == pygame.JOYAXISMOTION:
            for idPad in range(GlobalVar.joystick_count):
                joystick = pygame.joystick.Joystick(idPad)
                name = joystick.get_name()
                levettaSpostata = False
                xAnagSinistro = 0
                yAnagSinistro = 0
                grilDestro = 0
                grilSinistro = 0
                xAnagDestro = 0
                yAnagDestro = 0
                axes = joystick.get_numaxes()
                for idAsse in range(axes):
                    axis = joystick.get_axis(idAsse)
                    if 0.1 <= abs(axis) <= 1:
                        if idAsse == 0:
                            levettaSpostata = True
                            xAnagSinistro = axis
                        elif idAsse == 1:
                            levettaSpostata = True
                            yAnagSinistro = axis
                        elif idAsse == 2:
                            if axis > 0:
                                levettaSpostata = True
                                grilSinistro = abs(axis)
                            if axis < 0:
                                levettaSpostata = True
                                grilDestro = abs(axis)
                        elif idAsse == 3:
                            levettaSpostata = True
                            yAnagDestro = axis
                        elif idAsse == 4:
                            levettaSpostata = True
                            xAnagDestro = axis
                if levettaSpostata:
                    print ("Nome pad: " + str(name))
                    if xAnagSinistro or yAnagSinistro:
                        print ("Analogico sinistro: (" + str(xAnagSinistro) + ", " + str(yAnagSinistro) + ")")
                    if grilSinistro:
                        print ("Grilletto sinistro: (" + str(grilSinistro) + ")")
                    if grilDestro:
                        print ("Grilletto destro: (" + str(grilDestro) + ")")
                    if xAnagDestro or yAnagDestro:
                        print ("Analogico destro: (" + str(xAnagDestro) + ", " + str(yAnagDestro) + ")")
                    print ("\n")


def getInput(bottoneDown, aggiornaInterfaccia):
    tastoTrovato = False
    for event in pygame.event.get():
        # faccio apparire/sparire il cursore
        if event.type == pygame.KEYDOWN and (GlobalVar.mouseVisibile or GlobalVar.usandoIlController):
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalVar.setCursoreVisibile(False)
            GlobalVar.usandoIlController = False
        elif event.type == pygame.MOUSEBUTTONDOWN and (not GlobalVar.mouseVisibile or GlobalVar.usandoIlController):
            tastoTrovato = True
            aggiornaInterfaccia = True
            bottoneDown = False
            GlobalVar.setCursoreVisibile(True)
            GlobalVar.usandoIlController = False
        elif (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION) and (GlobalVar.mouseVisibile or not GlobalVar.usandoIlController):
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
        if event.type == pygame.KEYDOWN and not tastoTrovato:
            if event.key == pygame.K_w and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_a and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_s and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_d and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_e and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_q and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_SPACE and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key
            if event.key == pygame.K_ESCAPE and not tastoTrovato:
                tastoTrovato = True
                bottoneDown = event.key

        # tasto mouse
        if event.type == pygame.MOUSEBUTTONDOWN and not tastoTrovato:
            sinistroMouse, centraleMouse, destroMouse = pygame.mouse.get_pressed()
            tastoTrovato = True

            if sinistroMouse and not bottoneDown == "mouseSinistro":
                bottoneDown = "mouseSinistro"
            elif destroMouse and not bottoneDown == "mouseDestro":
                bottoneDown = "mouseDestro"
            elif centraleMouse and not bottoneDown == "mouseCentrale":
                bottoneDown = "mouseCentrale"

        # tasto joypad
        if GlobalVar.joystick:
            if event.type == pygame.JOYBUTTONDOWN and not tastoTrovato:
                buttons = GlobalVar.joystick.get_numbuttons()
                for idTasto in range(buttons):
                    button = GlobalVar.joystick.get_button(idTasto)
                    if button and not idTasto in GlobalVar.configTastiPad:
                        tastoTrovato = True
                        bottoneDown = False
                    if button and not tastoTrovato:
                        if idTasto == GlobalVar.configTastiPad[0] and not bottoneDown == "padCroce":
                            tastoTrovato = True
                            bottoneDown = "padCroce"
                        elif idTasto == GlobalVar.configTastiPad[1] and not bottoneDown == "padCerchio":
                            tastoTrovato = True
                            bottoneDown = "padCerchio"
                        elif idTasto == GlobalVar.configTastiPad[2] and not bottoneDown == "padQuadrato":
                            tastoTrovato = True
                            bottoneDown = "padQuadrato"
                        elif idTasto == GlobalVar.configTastiPad[3] and not bottoneDown == "padTriangolo":
                            tastoTrovato = True
                            bottoneDown = "padTriangolo"
                        elif idTasto == GlobalVar.configTastiPad[4] and not bottoneDown == "padL1":
                            tastoTrovato = True
                            bottoneDown = "padL1"
                        elif idTasto == GlobalVar.configTastiPad[5] and not bottoneDown == "padR1":
                            tastoTrovato = True
                            bottoneDown = "padR1"
                        elif idTasto == GlobalVar.configTastiPad[6] and not bottoneDown == "padStart":
                            tastoTrovato = True
                            bottoneDown = "padStart"
            if event.type == pygame.JOYHATMOTION and not tastoTrovato:
                hats = GlobalVar.joystick.get_numhats()
                for idCroceDirezionale in range(hats):
                    hat = GlobalVar.joystick.get_hat(idCroceDirezionale)
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
            # if event.type == pygame.JOYAXISMOTION and not tastoTrovato:
            #     levettaSpostata = False
            #     xAnagSinistro = 0
            #     yAnagSinistro = 0
            #     axes = GlobalVar.joystick.get_numaxes()
            #     for idAsse in range(axes):
            #         axis = GlobalVar.joystick.get_axis(idAsse)
            #         if 0.1 <= abs(axis) <= 1:
            #             if idAsse == GlobalVar.configAnalogicoPad[0]:
            #                 levettaSpostata = True
            #                 xAnagSinistro = axis
            #             elif idAsse == GlobalVar.configAnalogicoPad[1]:
            #                 levettaSpostata = True
            #                 yAnagSinistro = axis
            #     if levettaSpostata:
            #         if int(abs(xAnagSinistro) * 10) == int(abs(yAnagSinistro) * 10):
            #             if xAnagSinistro > 0 and yAnagSinistro > 0:
            #                 tastoTrovato = True
            #                 bottoneDown = "padSuDestra"
            #             elif xAnagSinistro > 0 and yAnagSinistro < 0:
            #                 tastoTrovato = True
            #                 bottoneDown = "padGiuDestra"
            #             elif xAnagSinistro < 0 and yAnagSinistro > 0:
            #                 tastoTrovato = True
            #                 bottoneDown = "padSuSinistra"
            #             elif xAnagSinistro < 0 and yAnagSinistro < 0:
            #                 tastoTrovato = True
            #                 bottoneDown = "padGiuSinistra"
            #         elif abs(xAnagSinistro) > abs(yAnagSinistro):
            #             if xAnagSinistro > 0:
            #                 bottoneDown = "padDestra"
            #             elif xAnagSinistro < 0:
            #                 bottoneDown = "padSinistra"
            #         else:
            #             if yAnagSinistro > 0:
            #                 bottoneDown = "padSu"
            #             elif yAnagSinistro < 0:
            #                 bottoneDown = "padGiu"

        # se lascio un tasto e non ne ho premuti altri resetto la variabile "bottoneDown" (non ha effetto se nella lista di eventi ci sono altri tasti premuti)
        if (event.type == pygame.KEYUP and event.key == bottoneDown) or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.JOYBUTTONUP:
            bottoneDown = False

    return bottoneDown, aggiornaInterfaccia
