# -*- coding: utf-8 -*-

import GlobalHWVar
import GenericFunc
import CaricaFileProgetto
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def salvataggio(n, datiAttuali, datiGameover):
    backup = False
    salvataggio = False
    while not salvataggio or not backup:
        if not salvataggio:
            salvataggio = True
        elif not backup:
            backup = True

        if not backup:
            scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "w")
        else:
            scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i-backup.txt" % n, "w")

        gameoverSalvato = False
        salvandoGameover = False
        while not gameoverSalvato:
            if not salvandoGameover:
                dati = datiAttuali[0]
                tutteporte = datiAttuali[1]
                tutticofanetti = datiAttuali[2]
                listaNemiciTotali = datiAttuali[3]
                vettoreEsche = datiAttuali[4]
                vettoreDenaro = datiAttuali[5]
                stanzeGiaVisitate = datiAttuali[6]
                listaPersonaggiTotali = datiAttuali[7]
                listaAvanzamentoDialoghi = datiAttuali[8]
                oggettiRimastiAHans = datiAttuali[9]
                ultimoObbiettivoColco = datiAttuali[10]
                obbiettivoCasualeColco = datiAttuali[11]
            else:
                dati = datiGameover[0]
                tutteporte = datiGameover[1]
                tutticofanetti = datiGameover[2]
                listaNemiciTotali = datiGameover[3]
                vettoreEsche = datiGameover[4]
                vettoreDenaro = datiGameover[5]
                stanzeGiaVisitate = datiGameover[6]
                listaPersonaggiTotali = datiGameover[7]
                listaAvanzamentoDialoghi = datiGameover[8]
                oggettiRimastiAHans = datiGameover[9]
                ultimoObbiettivoColco = datiGameover[10]
                obbiettivoCasualeColco = datiGameover[11]

            # conversione della posizione in caselle
            dati[2] = dati[2] // GlobalHWVar.gpx
            dati[3] = dati[3] // GlobalHWVar.gpy
            dati[134] = dati[134] // GlobalHWVar.gpx
            dati[135] = dati[135] // GlobalHWVar.gpy
            i = 0
            while i < len(tutteporte):
                tutteporte[i + 1] = tutteporte[i + 1] // GlobalHWVar.gpx
                tutteporte[i + 2] = tutteporte[i + 2] // GlobalHWVar.gpy
                i += 4
            i = 0
            while i < len(tutticofanetti):
                tutticofanetti[i + 1] = tutticofanetti[i + 1] // GlobalHWVar.gpx
                tutticofanetti[i + 2] = tutticofanetti[i + 2] // GlobalHWVar.gpy
                i += 4

            for i in range(0, len(dati)):
                scrivi.write("%i_" % dati[i])
            scrivi.write("\n")
            for i in range(0, len(tutteporte)):
                scrivi.write("%i_" % tutteporte[i])
            scrivi.write("\n")
            for i in range(0, len(tutticofanetti)):
                scrivi.write("%i_" % tutticofanetti[i])
            scrivi.write("\n")
            for nemico in listaNemiciTotali:
                scrivi.write("%s_" % nemico.tipo)
                scrivi.write("%i_" % nemico.stanzaDiAppartenenza)
                scrivi.write("%i_" % (nemico.x // GlobalHWVar.gpx))
                scrivi.write("%i_" % (nemico.y // GlobalHWVar.gpy))
                scrivi.write("%i_" % nemico.vita)
                scrivi.write("%i_" % nemico.avvelenato)
                scrivi.write("%i_" % nemico.appiccicato)
                if nemico.stanzaDiAppartenenza == dati[1]:
                    scrivi.write("%i_" % nemico.mosseRimaste)
                else:
                    scrivi.write("0_")
                scrivi.write("%s_" % nemico.direzione)
                scrivi.write("%i_" % (nemico.obbiettivo[1] // GlobalHWVar.gpx))
                scrivi.write("%i_" % (nemico.obbiettivo[2] // GlobalHWVar.gpy))
                scrivi.write("%i_" % (nemico.xPosizioneUltimoBersaglio // GlobalHWVar.gpx))
                scrivi.write("%i_" % (nemico.yPosizioneUltimoBersaglio // GlobalHWVar.gpy))
                scrivi.write("%i_" % nemico.numeroMovimento)
                scrivi.write("%i_" % nemico.triggerato)
                scrivi.write("%i_" % nemico.denaro)
                scrivi.write("[_")
                for direzione in nemico.percorso:
                    scrivi.write("%s_" % direzione)
                scrivi.write("]_")
            scrivi.write("\n")
            i = 0
            while i < len(vettoreEsche):
                scrivi.write("%i_" % vettoreEsche[i])
                scrivi.write("%i_" % vettoreEsche[i + 1])
                scrivi.write("%i_" % (vettoreEsche[i + 2] // GlobalHWVar.gpx))
                scrivi.write("%i_" % (vettoreEsche[i + 3] // GlobalHWVar.gpy))
                i += 4
            scrivi.write("\n")
            i = 0
            while i < len(vettoreDenaro):
                scrivi.write("%i_" % vettoreDenaro[i])
                scrivi.write("%i_" % (vettoreDenaro[i + 1] // GlobalHWVar.gpx))
                scrivi.write("%i_" % (vettoreDenaro[i + 2] // GlobalHWVar.gpy))
                i += 3
            scrivi.write("\n")
            i = 0
            while i < len(stanzeGiaVisitate):
                scrivi.write("%i_" % stanzeGiaVisitate[i])
                i += 1
            scrivi.write("\n")
            for personaggio in listaPersonaggiTotali:
                scrivi.write("%i_" % (personaggio.x // GlobalHWVar.gpx))
                scrivi.write("%i_" % (personaggio.y // GlobalHWVar.gpy))
                scrivi.write("%s_" % personaggio.direzione)
                scrivi.write("%s_" % personaggio.tipo)
                scrivi.write("%i_" % personaggio.stanzaDiAppartenenza)
                scrivi.write("%i_" % personaggio.avanzaStoria)
                scrivi.write("[_")
                for direzione in personaggio.percorso:
                    scrivi.write("%s_" % direzione)
                scrivi.write("]_")
                scrivi.write("%i_" % personaggio.numeroMovimento)
                scrivi.write("%i_" % personaggio.avanzamentoDialogo)
            scrivi.write("\n")
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                scrivi.write("%s_" % listaAvanzamentoDialoghi[i])
                scrivi.write("%i_" % listaAvanzamentoDialoghi[i + 1])
                i += 2
            scrivi.write("\n")
            for oggetto in oggettiRimastiAHans:
                scrivi.write("%i_" % oggetto)
            scrivi.write("\n")
            if len(ultimoObbiettivoColco) > 0:
                scrivi.write("%s_" % ultimoObbiettivoColco[0])
                scrivi.write("%i_" % (ultimoObbiettivoColco[1] // GlobalHWVar.gpx))
                scrivi.write("%i_" % (ultimoObbiettivoColco[2] // GlobalHWVar.gpy))
            else:
                scrivi.write("_")
                scrivi.write("-1_")
                scrivi.write("-1_")
            scrivi.write("\n")
            if obbiettivoCasualeColco:
                scrivi.write("%i_" % obbiettivoCasualeColco.stanzaDiAppartenenza)
                scrivi.write("%i_" % (obbiettivoCasualeColco.x // GlobalHWVar.gpx))
                scrivi.write("%i_" % (obbiettivoCasualeColco.y // GlobalHWVar.gpy))
            else:
                scrivi.write("-1_")
                scrivi.write("-1_")
                scrivi.write("-1_")

            # conversione della posizione in pixel
            dati[2] = dati[2] * GlobalHWVar.gpx
            dati[3] = dati[3] * GlobalHWVar.gpy
            dati[134] = dati[134] * GlobalHWVar.gpx
            dati[135] = dati[135] * GlobalHWVar.gpy
            i = 0
            while i < len(tutteporte):
                tutteporte[i + 1] = tutteporte[i + 1] * GlobalHWVar.gpx
                tutteporte[i + 2] = tutteporte[i + 2] * GlobalHWVar.gpy
                i += 4
            i = 0
            while i < len(tutticofanetti):
                tutticofanetti[i + 1] = tutticofanetti[i + 1] * GlobalHWVar.gpx
                tutticofanetti[i + 2] = tutticofanetti[i + 2] * GlobalHWVar.gpy
                i += 4

            if not salvandoGameover:
                scrivi.write("\n\n")
                salvandoGameover = True
            else:
                gameoverSalvato = True

        scrivi.close()

    # critta il salvataggio
    # leggi = GlobalVar.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "r")
    # contenutoFile = leggi.read()
    # leggi.close()
    # encoded_text = contenutoFile.encode('base64')
    # scrivi = GlobalVar.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "w")
    # scrivi.write(encoded_text)
    # scrivi.close()


def caricaPartita(n, lunghezzadati, lunghezzadatiPorte, lunghezzadatiCofanetti, checkErrori):
    errore = False
    tipoErrore = 0

    datiAttuali = []
    datiGameover = []

    partitaCaricata = False
    backupNecessario = False
    while not partitaCaricata:
        errore = False
        tipoErrore = 0

        datiAttuali = []
        datiGameover = []

        if not backupNecessario:
            leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "r")
        else:
            leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i-backup.txt" % n, "r")
        contenutoFile = leggi.read()
        leggi.close()

        # decritta il salvataggio
        datiTotali = [""]
        try:
            # contenutoFile = contenutoFile.decode('base64')
            datiTotali = contenutoFile.split("\n")
        except:
            errore = True
            tipoErrore = 2

        if not errore and not (len(datiTotali) == 1 and datiTotali[0] == ""):
            if len(datiTotali) == 25:
                caricandoGameover = False
                gameoverCaricato = False
                c = 0
                while not gameoverCaricato:
                    dati = []
                    tutteporte = []
                    tutticofanetti = []
                    listaNemiciTotali = []
                    listaEsche = []
                    listaMonete = []
                    stanzeGiaVisitate = []
                    listaPersonaggiTotali = []
                    listaAvanzamentoDialoghi = []
                    oggettiRimastiAHans = []
                    ultimoObbiettivoColco = []
                    obbiettivoCasualeColco = False

                    datiStringa = datiTotali[c].split("_")
                    datiStringa.pop(len(datiStringa) - 1)
                    if len(datiStringa) == 0 or len(datiStringa) != lunghezzadati:
                        errore = True
                    else:
                        for i in range(0, len(datiStringa)):
                            try:
                                dati.append(int(datiStringa[i]))
                            except:
                                errore = True
                                break
                        if not errore:
                            # conversione della posizione in pixel
                            dati[2] = dati[2] * GlobalHWVar.gpx
                            dati[3] = dati[3] * GlobalHWVar.gpy
                            dati[134] = dati[134] * GlobalHWVar.gpx
                            dati[135] = dati[135] * GlobalHWVar.gpy
                    porteStringa = datiTotali[c + 1].split("_")
                    porteStringa.pop(len(porteStringa) - 1)
                    if len(porteStringa) == 0 or len(porteStringa) != lunghezzadatiPorte:
                        errore = True
                    else:
                        for i in range(0, len(porteStringa)):
                            try:
                                tutteporte.append(int(porteStringa[i]))
                            except:
                                errore = True
                                break
                        if not errore:
                            # conversione della posizione in pixel
                            i = 0
                            while i < len(tutteporte):
                                tutteporte[i + 1] = tutteporte[i + 1] * GlobalHWVar.gpx
                                tutteporte[i + 2] = tutteporte[i + 2] * GlobalHWVar.gpy
                                i += 4
                    cofanettiStringa = datiTotali[c + 2].split("_")
                    cofanettiStringa.pop(len(cofanettiStringa) - 1)
                    if len(cofanettiStringa) == 0 or len(cofanettiStringa) != lunghezzadatiCofanetti:
                        errore = True
                    else:
                        for i in range(0, len(cofanettiStringa)):
                            try:
                                tutticofanetti.append(int(cofanettiStringa[i]))
                            except:
                                errore = True
                                break
                        if not errore:
                            # conversione della posizione in pixel
                            i = 0
                            while i < len(tutticofanetti):
                                tutticofanetti[i + 1] = tutticofanetti[i + 1] * GlobalHWVar.gpx
                                tutticofanetti[i + 2] = tutticofanetti[i + 2] * GlobalHWVar.gpy
                                i += 4
                    datiNemici = datiTotali[c + 3].split("_")
                    datiNemici.pop(len(datiNemici) - 1)
                    try:
                        i = 0
                        while i < len(datiNemici):
                            j = i + 16 + 1
                            while j < len(datiNemici):
                                if datiNemici[j] == "]":
                                    datiNemici.pop(j)
                                    datiNemici.pop(i + 16)
                                    percorsoNemico = []
                                    k = i + 16
                                    while k < j - 1:
                                        percorsoNemico.append(datiNemici.pop(i + 16))
                                        k += 1
                                    datiNemici.insert(i + 16, percorsoNemico)
                                    break
                                j += 1
                            i += 17
                    except:
                        errore = True
                    if len(datiNemici) % 17 != 0:
                        errore = True
                    else:
                        i = 0
                        while i < len(datiNemici):
                            try:
                                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * int(datiNemici[i + 2]), GlobalHWVar.gsy // 18 * int(datiNemici[i + 3]), datiNemici[i + 8], datiNemici[i], int(datiNemici[i + 1]), datiNemici[i + 16], int(datiNemici[i + 13]), bool(int(datiNemici[i + 14])), int(datiNemici[i + 15]), nonCaricareImg=checkErrori)
                                nemico.vita = int(datiNemici[i + 4])
                                nemico.avvelenato = bool(int(datiNemici[i + 5]))
                                nemico.appiccicato = bool(int(datiNemici[i + 6]))
                                nemico.mosseRimaste = int(datiNemici[i + 7])
                                nemico.obbiettivo[1] = int(datiNemici[i + 9]) * GlobalHWVar.gpx
                                nemico.obbiettivo[2] = int(datiNemici[i + 10]) * GlobalHWVar.gpy
                                nemico.xPosizioneUltimoBersaglio = int(datiNemici[i + 11]) * GlobalHWVar.gpx
                                nemico.yPosizioneUltimoBersaglio = int(datiNemici[i + 12]) * GlobalHWVar.gpy
                                listaNemiciTotali.append(nemico)
                            except:
                                errore = True
                                break
                            i += 17
                    listaEscheStringa = datiTotali[c + 4].split("_")
                    listaEscheStringa.pop(len(listaEscheStringa) - 1)
                    if len(listaEscheStringa) % 4 != 0:
                        errore = True
                    else:
                        i = 0
                        while i < len(listaEscheStringa):
                            try:
                                listaEsche.append(int(listaEscheStringa[i]))
                                listaEsche.append(int(listaEscheStringa[i + 1]))
                                listaEsche.append(GlobalHWVar.gpx * int(listaEscheStringa[i + 2]))
                                listaEsche.append(GlobalHWVar.gpy * int(listaEscheStringa[i + 3]))
                            except:
                                errore = True
                                break
                            i += 4
                    listaMoneteStringa = datiTotali[c + 5].split("_")
                    listaMoneteStringa.pop(len(listaMoneteStringa) - 1)
                    if len(listaMoneteStringa) % 3 != 0:
                        errore = True
                    else:
                        i = 0
                        while i < len(listaMoneteStringa):
                            try:
                                listaMonete.append(int(listaMoneteStringa[i]))
                                listaMonete.append(GlobalHWVar.gpx * int(listaMoneteStringa[i + 1]))
                                listaMonete.append(GlobalHWVar.gpy * int(listaMoneteStringa[i + 2]))
                            except:
                                errore = True
                                break
                            i += 3
                    stanzeGiaVisitateStringa = datiTotali[c + 6].split("_")
                    stanzeGiaVisitateStringa.pop(len(stanzeGiaVisitateStringa) - 1)
                    i = 0
                    while i < len(stanzeGiaVisitateStringa):
                        try:
                            stanzeGiaVisitate.append(int(stanzeGiaVisitateStringa[i]))
                        except:
                            errore = True
                            break
                        i += 1
                    datiPersonaggi = datiTotali[c + 7].split("_")
                    datiPersonaggi.pop(len(datiPersonaggi) - 1)
                    try:
                        i = 0
                        while i < len(datiPersonaggi):
                            j = i + 6 + 1
                            while j < len(datiPersonaggi):
                                if datiPersonaggi[j] == "]":
                                    datiPersonaggi.pop(j)
                                    datiPersonaggi.pop(i + 6)
                                    percorsoPersonaggio = []
                                    k = i + 6
                                    while k < j - 1:
                                        percorsoPersonaggio.append(datiPersonaggi.pop(i + 6))
                                        k += 1
                                    datiPersonaggi.insert(i + 6, percorsoPersonaggio)
                                    break
                                j += 1
                            i += 9
                    except:
                        errore = True
                    if len(datiPersonaggi) % 9 != 0:
                        errore = True
                    else:
                        i = 0
                        while i < len(datiPersonaggi):
                            try:
                                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * int(datiPersonaggi[i]), GlobalHWVar.gsy // 18 * int(datiPersonaggi[i + 1]), datiPersonaggi[i + 2], datiPersonaggi[i + 3], int(datiPersonaggi[i + 4]), int(datiPersonaggi[i + 5]), datiPersonaggi[i + 6], int(datiPersonaggi[i + 7]), int(datiPersonaggi[i + 8]), nonCaricareImg=checkErrori)
                                listaPersonaggiTotali.append(personaggio)
                            except:
                                errore = True
                                break
                            i += 9
                    datiDialoghi = datiTotali[c + 8].split("_")
                    datiDialoghi.pop(len(datiDialoghi) - 1)
                    if len(datiDialoghi) % 2 != 0:
                        errore = True
                    else:
                        i = 0
                        while i < len(datiDialoghi):
                            try:
                                listaAvanzamentoDialoghi.append(datiDialoghi[i])
                                listaAvanzamentoDialoghi.append(int(datiDialoghi[i + 1]))
                            except:
                                errore = True
                                break
                            i += 2
                    oggettiRimastiAHansStringa = datiTotali[c + 9].split("_")
                    oggettiRimastiAHansStringa.pop(len(oggettiRimastiAHansStringa) - 1)
                    if len(oggettiRimastiAHansStringa) != 13:
                        errore = True
                    else:
                        for i in range(0, len(oggettiRimastiAHansStringa)):
                            try:
                                oggettiRimastiAHans.append(int(oggettiRimastiAHansStringa[i]))
                            except:
                                errore = True
                                break
                    ultimoObbiettivoColcoStringa = datiTotali[c + 10].split("_")
                    ultimoObbiettivoColcoStringa.pop(len(ultimoObbiettivoColcoStringa) - 1)
                    if len(ultimoObbiettivoColcoStringa) != 3:
                        errore = True
                    else:
                        if ultimoObbiettivoColcoStringa[0] != "":
                            ultimoObbiettivoColco.append(ultimoObbiettivoColcoStringa[0])
                            ultimoObbiettivoColco.append(int(ultimoObbiettivoColcoStringa[1]) * GlobalHWVar.gpx)
                            ultimoObbiettivoColco.append(int(ultimoObbiettivoColcoStringa[2]) * GlobalHWVar.gpx)
                    obbiettivoCasualeColcoStringa = datiTotali[c + 11].split("_")
                    obbiettivoCasualeColcoStringa.pop(len(obbiettivoCasualeColcoStringa) - 1)
                    if len(obbiettivoCasualeColcoStringa) != 3:
                        errore = True
                    else:
                        if obbiettivoCasualeColcoStringa[0] != "-1" and obbiettivoCasualeColcoStringa[1] != "-1" and obbiettivoCasualeColcoStringa[2] != "-1":
                            for nemico in listaNemiciTotali:
                                if nemico.stanzaDiAppartenenza == int(obbiettivoCasualeColcoStringa[0]) and nemico.x == int(obbiettivoCasualeColcoStringa[1] * GlobalHWVar.gpx) and nemico.y == int(obbiettivoCasualeColcoStringa[2] * GlobalHWVar.gpy):
                                    obbiettivoCasualeColco = nemico
                                    break

                    if not caricandoGameover:
                        datiAttuali = [dati[:], tutteporte[:], tutticofanetti[:], GenericFunc.copiaListaDiOggettiConImmagini(listaNemiciTotali, True, checkErrori=checkErrori), listaEsche[:], listaMonete[:], stanzeGiaVisitate[:], GenericFunc.copiaListaDiOggettiConImmagini(listaPersonaggiTotali, False, checkErrori=checkErrori), listaAvanzamentoDialoghi[:], oggettiRimastiAHans[:], ultimoObbiettivoColco[:], GenericFunc.copiaNemico(obbiettivoCasualeColco, checkErrori=checkErrori)]
                        caricandoGameover = True
                    else:
                        datiGameover = [dati[:], tutteporte[:], tutticofanetti[:], GenericFunc.copiaListaDiOggettiConImmagini(listaNemiciTotali, True, checkErrori=checkErrori), listaEsche[:], listaMonete[:], stanzeGiaVisitate[:], GenericFunc.copiaListaDiOggettiConImmagini(listaPersonaggiTotali, False, checkErrori=checkErrori), listaAvanzamentoDialoghi[:], oggettiRimastiAHans[:], ultimoObbiettivoColco[:], GenericFunc.copiaNemico(obbiettivoCasualeColco, checkErrori=checkErrori)]
                        gameoverCaricato = True
                    c += 13
            else:
                errore = True
            if errore:
                tipoErrore = 2
        elif not errore and len(datiTotali) == 1 and datiTotali[0] == "":
            errore = True
            tipoErrore = 1
            datiAttuali = [[], [], [], [], [], [], [], [], [], [], [], []]
            datiGameover = [[], [], [], [], [], [], [], [], [], [], [], []]

        if not errore:
            partitaCaricata = True
        elif not backupNecessario:
            backupNecessario = True
        else:
            partitaCaricata = True

    if not errore:
        if not checkErrori:
            if not backupNecessario:
                leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "r")
            else:
                leggi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i-backup.txt" % n, "r")
            contenutoFile = leggi.read()
            leggi.close()
            if not backupNecessario:
                scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i-backup.txt" % n, "w")
            else:
                scrivi = CaricaFileProgetto.loadFile("DatiSalvati/Salvataggi/Salvataggio%i.txt" % n, "w")
            scrivi.write(contenutoFile)
            scrivi.close()
    else:
        if len(datiAttuali) == 0:
            datiAttuali = [[], [], [], [], [], [], [], [], [], [], [], []]
        if len(datiGameover) == 0:
            datiGameover = [[], [], [], [], [], [], [], [], [], [], [], []]

    return datiAttuali, datiGameover, tipoErrore
