# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.UtilityOstacoliContenutoCofanetti as UtilityOstacoliContenutoCofanetti
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliSogno as OstacoliSogno
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliCasa as OstacoliCasa
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliForestaCadetta as OstacoliForestaCadetta
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliStradaPerCitta as OstacoliStradaPerCitta
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliCitta as OstacoliCitta
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliCasaUfficiale as OstacoliCasaUfficiale
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliBiblioteca as OstacoliBiblioteca
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliStradaPerSelvaArida as OstacoliStradaPerSelvaArida
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliSelvaArida as OstacoliSelvaArida
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliAvampostoDiRod as OstacoliAvampostoDiRod
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliLabirinto as OstacoliLabirinto
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliEsternoCastello as OstacoliEsternoCastello
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliInternoCastello as OstacoliInternoCastello
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliScorciatoiaLabirinto as OstacoliScorciatoiaLabirinto
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliStradaPerPassoMontano as OstacoliStradaPerPassoMontano
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliPassoMontano as OstacoliPassoMontano
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliPalazzoDiRod as OstacoliPalazzoDiRod
import Codice.SettaggiLivelli.OstacoliPerZona.OstacoliTunnelDiRod as OstacoliTunnelDiRod


def getEntrateStanze(stanza, avanzamentoStoria):
    entrateStanza = []

    if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
        if stanza == GlobalGameVar.dictStanze["sognoSara1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoSara2"]])
        elif stanza == GlobalGameVar.dictStanze["sognoSara2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoSara1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["sognoSara3"]])
        elif stanza == GlobalGameVar.dictStanze["sognoSara3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["sognoSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoSara4"]])
        elif stanza == GlobalGameVar.dictStanze["sognoSara4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoSara3"]])
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        if stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
        elif stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
        elif stanza == GlobalGameVar.dictStanze["casaHansSara3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
        elif stanza == GlobalGameVar.dictStanze["casaHansSara4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara2"]])
            if GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta5"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta5"]])
            else:
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta1"]])
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        if stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansSara4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["forestaCadetta2"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["forestaCadetta1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta3"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta4"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta5"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["forestaCadetta6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta7"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta6"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["forestaCadetta5"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta8"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
        elif stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerCittà1"]])
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
        elif stanza == GlobalGameVar.dictStanze["stradaPerCittà2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
        elif stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà2"]])
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
        if stanza == GlobalGameVar.dictStanze["città1"]:
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerCittà3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
        elif stanza == GlobalGameVar.dictStanze["città2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
        elif stanza == GlobalGameVar.dictStanze["città3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["città4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid1"]])
        elif stanza == GlobalGameVar.dictStanze["città5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città8"]])
        elif stanza == GlobalGameVar.dictStanze["città6"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
        elif stanza == GlobalGameVar.dictStanze["città7"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città5"]])
        elif stanza == GlobalGameVar.dictStanze["città8"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["città9"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
        elif stanza == GlobalGameVar.dictStanze["città10"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
        if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 11, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["casaDavid2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 4, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["casaDavid3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["casaDavid2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 13, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 9, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, 0, -GlobalHWVar.gpy, -1])
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
        if stanza == GlobalGameVar.dictStanze["biblioteca1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca2"]])
        elif stanza == GlobalGameVar.dictStanze["biblioteca2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["biblioteca1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["biblioteca3"]])
        elif stanza == GlobalGameVar.dictStanze["biblioteca3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["biblioteca2"]])
    elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        if stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["città9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
        elif stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
        if stanza == GlobalGameVar.dictStanze["selvaArida1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["stradaPerSelvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida7"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida10"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida12"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida5"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida14"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida6"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida5"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida7"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida10"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida8"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida1"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida9"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida2"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida10"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida11"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida11"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida12"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida14"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida13"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida4"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida14"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["selvaArida5"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida15"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
        elif stanza == GlobalGameVar.dictStanze["selvaArida16"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        if stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["selvaArida16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["avampostoDiRod3"]])
        elif stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["avampostoDiRod3"]])
        elif stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["avampostoDiRod1"]])
    elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
        if stanza == GlobalGameVar.dictStanze["labirinto1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto3"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto6"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto7"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto7"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto8"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto9"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto10"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto10"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto11"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto11"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto10"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto12"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto13"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto14"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto15"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto15"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto14"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto16"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto17"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto18"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto19"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto19"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto23"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto23"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto23"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto23"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto23"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto18"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto20"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto21"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto22"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto22"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto22"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto23"]])
        elif stanza == GlobalGameVar.dictStanze["labirinto23"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["labirinto22"]])
    elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]:
        if stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["labirinto20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello3"]])
        elif stanza == GlobalGameVar.dictStanze["esternoCastello3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello2"]])
        elif stanza == GlobalGameVar.dictStanze["esternoCastello4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
        elif stanza == GlobalGameVar.dictStanze["esternoCastello5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
        if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["esternoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
        elif stanza == GlobalGameVar.dictStanze["internoCastello2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
        elif stanza == GlobalGameVar.dictStanze["internoCastello3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 13, 0, +GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello6"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello7"]])
        elif stanza == GlobalGameVar.dictStanze["internoCastello7"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello8"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["tunnelSubacqueo1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello9"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello10"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello11"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello11"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello12"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello13"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello12"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello14"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello13"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 5, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello15"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 6, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello14"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 11, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello16"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello15"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello17"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello16"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello18"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello17"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, +GlobalHWVar.gpx, 0, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello19"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello18"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello20"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello21"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["internoCastello2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, -1])
        elif stanza == GlobalGameVar.dictStanze["internoCastello20"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"]:
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["internoCastello19"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, -1])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, -1])
    elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        if stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["esternoCastello1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]])
        elif stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
    elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
        if stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["città10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano2"]])
        elif stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano1"]])
    elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
        if stanza == GlobalGameVar.dictStanze["passoMontano1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["stradaPerPassoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano6"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano3"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 12, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano4"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano4"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano9"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano6"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano1"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano7"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano6"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano8"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano7"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano9"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano8"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano5"]])
        elif stanza == GlobalGameVar.dictStanze["passoMontano10"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["passoMontano9"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod1"]])
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["bussatoAlPalazzoDiRodConDialogo"]:
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod2"]])
                entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 5, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["passoMontano10"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["caverna1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["caverna1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["caverna1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["caverna1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["caverna1"]])
        elif stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 10, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 3, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod4"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["palazzoDiRod4"]])
        elif stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 12, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["palazzoDiRod5"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod2"]])
        elif stanza == GlobalGameVar.dictStanze["tunnelDiRod2"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod1"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod3"]])
        elif stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["tunnelDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])
            entrateStanza.extend([GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["avampostoDiRod2"]])

    return entrateStanza


def controlloOstacoli(x, y, nx, ny, stanza, carim, porte, cofanetti, avanzamentoStoria, escludiPorte=False, escludiOggettiBassi=False):
    cambiosta = False

    if x < 0 or y < 0 or x >= GlobalHWVar.gsx or y >= GlobalHWVar.gsy:
        return x, y, stanza, carim, cambiosta

    entrateStanza = getEntrateStanze(stanza, avanzamentoStoria)
    andandoVersoUscitaStanza = False
    i = 0
    while i < len(entrateStanza):
        if x == entrateStanza[i] and y == entrateStanza[i + 1] and nx == entrateStanza[i + 2] and ny == entrateStanza[i + 3] and not escludiPorte:
            stanza = entrateStanza[i + 4]
            cambiosta = True
            carim = True
            andandoVersoUscitaStanza = True
        elif x == entrateStanza[i] + entrateStanza[i + 2] and y == entrateStanza[i + 1] + entrateStanza[i + 3] and not escludiPorte:
            nx = 0
            ny = 0
            andandoVersoUscitaStanza = True
        i += 5

    if not andandoVersoUscitaStanza and not (nx == 0 and ny == 0) and not cambiosta:
        if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliSogno.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliCasa.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliForestaCadetta.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliStradaPerCitta.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliCitta.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliCasaUfficiale.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliBiblioteca.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliStradaPerSelvaArida.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliSelvaArida.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliAvampostoDiRod.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliLabirinto.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliEsternoCastello.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliInternoCastello.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliScorciatoiaLabirinto.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliStradaPerPassoMontano.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliPassoMontano.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliPalazzoDiRod.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)
        elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliTunnelDiRod.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi, avanzamentoStoria)

        # controllo se le porte sono chiuse o aperte
        if not (nx == 0 and ny == 0):
            i = 0
            while i < len(porte):
                if not porte[i + 3]:
                    if UtilityOstacoliContenutoCofanetti.oggetto(porte[i + 1], porte[i + 2], GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                        nx = 0
                        ny = 0
                        break
                i = i + 4
        # controllo cofanetti
        if not (nx == 0 and ny == 0):
            i = 0
            while i < len(cofanetti):
                if UtilityOstacoliContenutoCofanetti.oggetto(cofanetti[i + 1], cofanetti[i + 2], GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                    break
                i = i + 4

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, cambiosta


def aperturacofanetto(stanza, cx, cy, dati):
    avanzamentoStoria = dati[0]
    numFrecceOttenute = 1
    numMoneteOttenute = 50

    tesoro = -1
    # 11-30 -> tecniche(20) / 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(10) / 81-100 -> condizioni(20) / 1000 -> celle di memoria(1) / 131 -> monete / 132 -> frecce
    # ordine tecniche => [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesta++]
    # ordine condizioni => [pv<80, pv<50, pv<30, avvelenato, surriscaldato, pe<80, pe<50, pe<30, sempreSara, sempreImpo, nemico casuale, nemico vicino, nemico lontano, pvNemico<80, pvNemico<50, pvNemico<30, pvNemicoMinori, nemici>1, nemici>4, nemici>7]
    if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
        if stanza == GlobalGameVar.dictStanze["sognoSara1"]:
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 10:
                tesoro = 31
                avanzamentoStoria += 1
        if stanza == GlobalGameVar.dictStanze["sognoSara2"]:
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 5:
                tesoro = 31
            # ottieni medicina
            if cx == GlobalHWVar.gpx * 28 and cy == GlobalHWVar.gpy * 7:
                tesoro = 33
        if stanza == GlobalGameVar.dictStanze["sognoSara3"]:
            # ottieni bomba
            if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 13:
                tesoro = 36
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        if stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
            # ottieni armatura (pelle)
            if cx == GlobalHWVar.gpx * 23 and cy == GlobalHWVar.gpy * 13:
                tesoro = 52
                avanzamentoStoria += 1
            # ottieni spada (ferro)
            if cx == GlobalHWVar.gpx * 24 and cy == GlobalHWVar.gpy * 15:
                tesoro = 42
                avanzamentoStoria += 1
            # ottieni scudo (pelle)
            if cx == GlobalHWVar.gpx * 27 and cy == GlobalHWVar.gpy * 15:
                tesoro = 57
                avanzamentoStoria += 1
            # ottieni arco (legno)
            if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 14:
                tesoro = 47
                avanzamentoStoria += 1
        if stanza == GlobalGameVar.dictStanze["casaHansSara3"]:
            # ottieni monete
            if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 10:
                tesoro = 131
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        if stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 27 and cy == GlobalHWVar.gpy * 2:
                tesoro = 31
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 15:
                tesoro = 31
            # ottieni freccia
            if cx == GlobalHWVar.gpx * 8 and cy == GlobalHWVar.gpy * 2:
                tesoro = 132
        if stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
            # ottieni bomba
            if cx == GlobalHWVar.gpx * 18 and cy == GlobalHWVar.gpy * 14:
                tesoro = 36
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 11 and cy == GlobalHWVar.gpy * 2:
                tesoro = 31
            # ottieni esca
            if cx == GlobalHWVar.gpx * 5 and cy == GlobalHWVar.gpy * 9:
                tesoro = 38
        if stanza == GlobalGameVar.dictStanze["forestaCadetta3"]:
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 20 and cy == GlobalHWVar.gpy * 2:
                tesoro = 31
            # ottieni freccia
            if cx == GlobalHWVar.gpx * 5 and cy == GlobalHWVar.gpy * 13:
                tesoro = 132
            # ottieni guanti vitali
            if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 9:
                tesoro = 62
        if stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 9:
                tesoro = 31
            # ottieni bomba
            if cx == GlobalHWVar.gpx * 10 and cy == GlobalHWVar.gpy * 2:
                tesoro = 36
        if stanza == GlobalGameVar.dictStanze["forestaCadetta6"]:
            # ottieni freccia
            if cx == GlobalHWVar.gpx * 12 and cy == GlobalHWVar.gpy * 2:
                tesoro = 132
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 2:
                tesoro = 31
        if stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            # ottieni esca
            if cx == GlobalHWVar.gpx * 26 and cy == GlobalHWVar.gpy * 15:
                tesoro = 38
            # ottieni arco di ferro
            if cx == GlobalHWVar.gpx * 2 and cy == GlobalHWVar.gpy * 4:
                tesoro = 48
        if stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
            # ottieni collana rigenerante
            if cx == GlobalHWVar.gpx * 2 and cy == GlobalHWVar.gpy * 6:
                tesoro = 67
        if stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
            # ottieni bomba veleno
            if cx == GlobalHWVar.gpx * 5 and cy == GlobalHWVar.gpy * 11:
                tesoro = 37
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
        if stanza == GlobalGameVar.dictStanze["città4"]:
            # ottieni monete
            if cx == GlobalHWVar.gpx * 17 and cy == GlobalHWVar.gpy * 5:
                tesoro = 131
        if stanza == GlobalGameVar.dictStanze["città8"]:
            # ottieni monete
            if cx == GlobalHWVar.gpx * 27 and cy == GlobalHWVar.gpy * 8:
                tesoro = 131
        if stanza == GlobalGameVar.dictStanze["città10"]:
            # ottieni monete
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 3:
                tesoro = 131
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
        if stanza == GlobalGameVar.dictStanze["selvaArida1"]:
            # ottieni batteria (Sacca Energetica discreta)
            if cx == GlobalHWVar.gpx * 6 and cy == GlobalHWVar.gpy * 5:
                tesoro = 72
            # ottieni tecnica (tempesta elettrica)
            if cx == GlobalHWVar.gpx * 6 and cy == GlobalHWVar.gpy * 12:
                tesoro = 15
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 12 and cy == GlobalHWVar.gpy * 11:
                tesoro = 1000
        if stanza == GlobalGameVar.dictStanze["selvaArida2"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 3:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida3"]:
            # ottieni tecnica (antidoto)
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 14:
                tesoro = 13
            # ottieni condizione (avvelenato)
            if cx == GlobalHWVar.gpx * 17 and cy == GlobalHWVar.gpy * 12:
                tesoro = 84
        if stanza == GlobalGameVar.dictStanze["selvaArida4"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 12 and cy == GlobalHWVar.gpy * 11:
                tesoro = 32
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 18 and cy == GlobalHWVar.gpy * 11:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida5"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 10:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida6"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 10:
                tesoro = 32
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 11 and cy == GlobalHWVar.gpy * 2:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida7"]:
            # ottieni medicina
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 2:
                tesoro = 33
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 9:
                tesoro = 32
            # ottieni condizione (pv<80)
            if cx == GlobalHWVar.gpx * 24 and cy == GlobalHWVar.gpy * 7:
                tesoro = 81
        if stanza == GlobalGameVar.dictStanze["selvaArida8"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 14 and cy == GlobalHWVar.gpy * 15:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida9"]:
            # ottieni medicina
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 15:
                tesoro = 33
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 12:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida10"]:
            # ottieni collana medicinale
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 3:
                tesoro = 68
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 9 and cy == GlobalHWVar.gpy * 2:
                tesoro = 1000
        if stanza == GlobalGameVar.dictStanze["selvaArida11"]:
            # ottieni tecnica (freccia)
            if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 13:
                tesoro = 14
            # ottieni condizione (nemico lontano)
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 14:
                tesoro = 93
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 25 and cy == GlobalHWVar.gpy * 7:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida12"]:
            # ottieni pozione
            if cx == GlobalHWVar.gpx * 15 and cy == GlobalHWVar.gpy * 2:
                tesoro = 31
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 28 and cy == GlobalHWVar.gpy * 9:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida13"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 2 and cy == GlobalHWVar.gpy * 14:
                tesoro = 32
            # ottieni condizione (nemico vicino)
            if cx == GlobalHWVar.gpx * 6 and cy == GlobalHWVar.gpy * 5:
                tesoro = 92
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 10 and cy == GlobalHWVar.gpy * 10:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida14"]:
            # ottieni medicina
            if cx == GlobalHWVar.gpx * 6 and cy == GlobalHWVar.gpy * 11:
                tesoro = 33
            # ottieni tecnica (cura)
            if cx == GlobalHWVar.gpx * 10 and cy == GlobalHWVar.gpy * 13:
                tesoro = 12
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 22 and cy == GlobalHWVar.gpy * 11:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida15"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 20 and cy == GlobalHWVar.gpy * 5:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["selvaArida16"]:
            # ottieni medicina
            if cx == GlobalHWVar.gpx * 20 and cy == GlobalHWVar.gpy * 7:
                tesoro = 33
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        if stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
            # ottieni collana Assorbilampo
            if cx == GlobalHWVar.gpx * 24 and cy == GlobalHWVar.gpy * 12:
                tesoro = 69
    elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
        if stanza == GlobalGameVar.dictStanze["labirinto2"]:
            # ottieni condizione (pe<80)
            if cx == GlobalHWVar.gpx * 10 and cy == GlobalHWVar.gpy * 6:
                tesoro = 86
        if stanza == GlobalGameVar.dictStanze["labirinto4"]:
            # ottieni condizione (nemici>1)
            if cx == GlobalHWVar.gpx * 24 and cy == GlobalHWVar.gpy * 11:
                tesoro = 98
        if stanza == GlobalGameVar.dictStanze["labirinto5"]:
            # ottieni tecnica (auto-ricarica)
            if cx == GlobalHWVar.gpx * 18 and cy == GlobalHWVar.gpy * 10:
                tesoro = 17
        if stanza == GlobalGameVar.dictStanze["labirinto9"]:
            # ottieni tecnica (attP)
            if cx == GlobalHWVar.gpx * 18 and cy == GlobalHWVar.gpy * 8:
                tesoro = 22
        if stanza == GlobalGameVar.dictStanze["labirinto11"]:
            # ottieni condizione (pvNemico<80)
            if cx == GlobalHWVar.gpx * 24 and cy == GlobalHWVar.gpy * 9:
                tesoro = 94
        if stanza == GlobalGameVar.dictStanze["labirinto14"]:
            # ottieni guanti difensivi
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 8:
                tesoro = 63
        if stanza == GlobalGameVar.dictStanze["labirinto17"]:
            # ottieni condizione (sempreSara)
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 10:
                tesoro = 89
        if stanza == GlobalGameVar.dictStanze["labirinto23"]:
            # ottieni tecnica (difP)
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 10:
                tesoro = 23
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
        if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 2 and cy == GlobalHWVar.gpy * 12:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["internoCastello2"]:
            # ottieni monete
            if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 5:
                tesoro = 131
        if stanza == GlobalGameVar.dictStanze["internoCastello3"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 27 and cy == GlobalHWVar.gpy * 8:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["internoCastello4"]:
            # ottieni bomba veleno
            if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 12:
                tesoro = 37
        if stanza == GlobalGameVar.dictStanze["internoCastello5"]:
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 8 and cy == GlobalHWVar.gpy * 6:
                tesoro = 32
            # ottieni medicina
            if cx == GlobalHWVar.gpx * 18 and cy == GlobalHWVar.gpy * 3:
                tesoro = 33
            # ottieni monete
            if cx == GlobalHWVar.gpx * 25 and cy == GlobalHWVar.gpy * 9:
                tesoro = 131
        if stanza == GlobalGameVar.dictStanze["internoCastello6"]:
            # ottieni superpozione
            if cx == GlobalHWVar.gpx * 25 and cy == GlobalHWVar.gpy * 7:
                tesoro = 34
        if stanza == GlobalGameVar.dictStanze["internoCastello7"]:
            # ottieni tecnica (scossa+)
            if cx == GlobalHWVar.gpx * 23 and cy == GlobalHWVar.gpy * 2:
                tesoro = 19
        if stanza == GlobalGameVar.dictStanze["internoCastello9"]:
            # ottieni condizione (surriscaldato)
            if cx == GlobalHWVar.gpx * 23 and cy == GlobalHWVar.gpy * 2:
                tesoro = 85
        if stanza == GlobalGameVar.dictStanze["internoCastello10"]:
            # ottieni bomba appiccicosa
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 7:
                tesoro = 39
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 26 and cy == GlobalHWVar.gpy * 13:
                tesoro = 1000
        if stanza == GlobalGameVar.dictStanze["internoCastello11"]:
            # ottieni spada (lupo)
            if cx == GlobalHWVar.gpx * 10 and cy == GlobalHWVar.gpy * 12:
                tesoro = 44
            # ottieni armatura (lupo)
            if cx == GlobalHWVar.gpx * 15 and cy == GlobalHWVar.gpy * 7:
                tesoro = 54
            # ottieni scudo (lupo)
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 7:
                tesoro = 59
            # ottieni arco (lupo)
            if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 12:
                tesoro = 49
        if stanza == GlobalGameVar.dictStanze["internoCastello12"]:
            # ottieni tecnica (raffreddamento)
            if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 2:
                tesoro = 16
        if stanza == GlobalGameVar.dictStanze["internoCastello13"]:
            # ottieni condizione (sempreImpo)
            if cx == GlobalHWVar.gpx * 15 and cy == GlobalHWVar.gpy * 3:
                tesoro = 90
        if stanza == GlobalGameVar.dictStanze["internoCastello15"]:
            # ottieni bomba appiccicosa
            if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 3:
                tesoro = 39
        if stanza == GlobalGameVar.dictStanze["internoCastello16"]:
            # ottieni caricabatterie migliorato
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 15:
                tesoro = 35
            # ottieni bomba potenziata
            if cx == GlobalHWVar.gpx * 14 and cy == GlobalHWVar.gpy * 7:
                tesoro = 40
        if stanza == GlobalGameVar.dictStanze["internoCastello17"]:
            # ottieni monete
            if cx == GlobalHWVar.gpx * 14 and cy == GlobalHWVar.gpy * 8:
                tesoro = 131
        if stanza == GlobalGameVar.dictStanze["internoCastello18"]:
            # ottieni tecnica (velocizza)
            if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 14:
                tesoro = 21
        if stanza == GlobalGameVar.dictStanze["internoCastello20"]:
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 19 and cy == GlobalHWVar.gpy * 8:
                tesoro = 1000
            # ottieni batteria (Sacca Energetica enorme)
            if cx == GlobalHWVar.gpx * 25 and cy == GlobalHWVar.gpy * 8:
                tesoro = 74
    elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
        if stanza == GlobalGameVar.dictStanze["passoMontano1"]:
            # ottieni condizione (pv<50)
            if cx == GlobalHWVar.gpx * 11 and cy == GlobalHWVar.gpy * 14:
                tesoro = 82
            # ottieni superpozione
            if cx == GlobalHWVar.gpx * 16 and cy == GlobalHWVar.gpy * 9:
                tesoro = 34
            # ottieni bomba veleno
            if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 8:
                tesoro = 37
        if stanza == GlobalGameVar.dictStanze["passoMontano2"]:
            # ottieni batteria (Sacca Energetica capiente)
            if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 3:
                tesoro = 73
            # ottieni tecnica (cura+)
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 12:
                tesoro = 18
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 6 and cy == GlobalHWVar.gpy * 4:
                tesoro = 1000
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 5:
                tesoro = 32
        if stanza == GlobalGameVar.dictStanze["passoMontano3"]:
            # ottieni superpozione
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 15:
                tesoro = 34
            # ottieni condizione (pe<50)
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 2:
                tesoro = 87
        if stanza == GlobalGameVar.dictStanze["passoMontano4"]:
            # ottieni esca
            if cx == GlobalHWVar.gpx * 11 and cy == GlobalHWVar.gpy * 2:
                tesoro = 38
        if stanza == GlobalGameVar.dictStanze["passoMontano5"]:
            # ottieni guanti offensivi
            if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 2:
                tesoro = 64
            # ottieni tecnica (freccia+)
            if cx == GlobalHWVar.gpx * 6 and cy == GlobalHWVar.gpy * 15:
                tesoro = 20
            # ottieni caricabatterie
            if cx == GlobalHWVar.gpx * 26 and cy == GlobalHWVar.gpy * 11:
                tesoro = 32
            # ottieni bomba appiccicosa
            if cx == GlobalHWVar.gpx * 28 and cy == GlobalHWVar.gpy * 13:
                tesoro = 39
        if stanza == GlobalGameVar.dictStanze["passoMontano6"]:
            # ottieni bomba potenziata
            if cx == GlobalHWVar.gpx * 18 and cy == GlobalHWVar.gpy * 2:
                tesoro = 40
        if stanza == GlobalGameVar.dictStanze["passoMontano7"]:
            # ottieni condizione (pvNemico<50)
            if cx == GlobalHWVar.gpx * 12 and cy == GlobalHWVar.gpy * 15:
                tesoro = 95
        if stanza == GlobalGameVar.dictStanze["passoMontano8"]:
            # ottieni tecnica (tempesta elettrica+)
            if cx == GlobalHWVar.gpx * 4 and cy == GlobalHWVar.gpy * 7:
                tesoro = 25
        if stanza == GlobalGameVar.dictStanze["passoMontano9"]:
            # ottieni bomba appiccicosa
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 14:
                tesoro = 39
            # ottieni condizione (nemici>4)
            if cx == GlobalHWVar.gpx * 26 and cy == GlobalHWVar.gpy * 14:
                tesoro = 99
        if stanza == GlobalGameVar.dictStanze["passoMontano10"]:
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 2:
                tesoro = 1000
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 26 and cy == GlobalHWVar.gpy * 10:
                tesoro = 1000
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if stanza == GlobalGameVar.dictStanze["tunnelDiRod2"]:
            # ottieni cella di memoria
            if cx == GlobalHWVar.gpx * 17 and cy == GlobalHWVar.gpy * 8:
                tesoro = 1000

    # assegna oggetto ottenuto
    if tesoro != -1 and tesoro != -2:
        if tesoro >= 11 and tesoro <= 30:
            dati, tesoro = UtilityOstacoliContenutoCofanetti.ottieniTecnica(dati, tesoro)
        elif tesoro >= 31 and tesoro <= 40:
            dati, tesoro = UtilityOstacoliContenutoCofanetti.ottieniOggetto(dati, tesoro, 1)
        elif tesoro >= 41 and tesoro <= 75:
            dati, tesoro = UtilityOstacoliContenutoCofanetti.ottieniArmaBatteria(dati, tesoro)
        elif tesoro >= 81 and tesoro <= 100:
            dati, tesoro = UtilityOstacoliContenutoCofanetti.ottieniCondizione(dati, tesoro)
        elif tesoro == 1000:
            dati = UtilityOstacoliContenutoCofanetti.ottieniCellaDiMemoria(dati)
        elif tesoro == 131:
            dati = UtilityOstacoliContenutoCofanetti.ottieniMonete(dati, numMoneteOttenute)
        elif tesoro == 132:
            dati[tesoro], tesoro = UtilityOstacoliContenutoCofanetti.ottieniFrecce(dati, numFrecceOttenute, tesoro)
        else:
            tesoro = -2
    return dati, tesoro, avanzamentoStoria
