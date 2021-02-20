# -*- coding: utf-8 -*-

import GlobalHWVar
import GlobalGameVar
import UtilityOstacoliContenutoCofanetti


def getEntrateStanze(stanza, avanzamentoStoria):
    entrateStanza = []

    if stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoLucy2"]])
    elif stanza == GlobalGameVar.dictStanze["sognoLucy2"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoLucy1"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 3, +GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["sognoLucy3"]])
    elif stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, -GlobalHWVar.gpx, 0, GlobalGameVar.dictStanze["sognoLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoLucy4"]])
    elif stanza == GlobalGameVar.dictStanze["sognoLucy4"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["sognoLucy3"]])
    elif stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
    elif stanza == GlobalGameVar.dictStanze["casaHansLucy2"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy1"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy1"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 3, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 4, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
    elif stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
    elif stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta1"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["forestaCadetta1"]])
    elif stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
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
    elif stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
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
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
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
    elif stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 11, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaDavid2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["città3"]])
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
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, +GlobalHWVar.gpx, 0, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, +GlobalHWVar.gpx, 0, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, +GlobalHWVar.gpx, 0, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, +GlobalHWVar.gpx, 0, -1])
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
        if stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["sognoLucy2"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["sognoLucy4"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 13, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["casaHansLucy2"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 28, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 16, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 10, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 10, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 9, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 7, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 9, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 14, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta3"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 14, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 14, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 8, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 9, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta6"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 5, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
            # bordi stanza
            if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                nx = 0
                ny = 0
            elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                nx = 0
                ny = 0
            elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                nx = 0
                ny = 0
            elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                nx = 0
                ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 6, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                nx = 0
                ny = 0
            elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
        if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 13, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["stradaPerCittà2"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 30, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 4, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 9, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 9, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 10, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
        if stanza == GlobalGameVar.dictStanze["casaDavid3"]:
            # bordi stanza
            if not escludiOggettiBassi:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 2:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 3):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 2:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 3):
                    nx = 0
                    ny = 0
            else:
                if nx == -GlobalHWVar.gpx and x <= GlobalHWVar.gpx * 1:
                    nx = 0
                    ny = 0
                elif nx == GlobalHWVar.gpx and x >= GlobalHWVar.gsx - (GlobalHWVar.gpx * 2):
                    nx = 0
                    ny = 0
                elif ny == -GlobalHWVar.gpy and y <= GlobalHWVar.gpy * 1:
                    nx = 0
                    ny = 0
                elif ny == GlobalHWVar.gpy and y >= GlobalHWVar.gsy - (GlobalHWVar.gpy * 2):
                    nx = 0
                    ny = 0
            # controllo muri-oggetti
            # oggetto(posizione x, posizione y, dim x, dim y, px, py, nx,  ny)
            if not (nx == 0 and ny == 0):
                if UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 1, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 6, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 6, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 16, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 31, GlobalHWVar.gsy // 18 * 15, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 4, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, GlobalHWVar.gpx * 10, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 2, GlobalHWVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 2, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 3, GlobalHWVar.gpy * 3, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, GlobalHWVar.gpx * 21, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 3, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 4, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 13, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
                elif not escludiOggettiBassi and UtilityOstacoliContenutoCofanetti.oggetto(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 9, GlobalHWVar.gpx * 1, GlobalHWVar.gpy * 5, x, y, nx, ny):
                    nx = 0
                    ny = 0

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
    # 11-30 -> tecniche(20) / 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-75 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20) / 131 -> monete / 132 frecce
    if stanza == -1:
        # ottieni pozione
        if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 7:
            tesoro = 31
        # ottieni cella di memoria
        if cx == GlobalHWVar.gpx * 7 and cy == GlobalHWVar.gpy * 12:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
            if tesoro == -1:
                tesoro = -2

    if stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        # ottieni pozione
        if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 10:
            tesoro = 31
            avanzamentoStoria += 1
    if stanza == GlobalGameVar.dictStanze["sognoLucy2"]:
        # ottieni pozione
        if cx == GlobalHWVar.gpx * 13 and cy == GlobalHWVar.gpy * 5:
            tesoro = 31
        # ottieni medicina
        if cx == GlobalHWVar.gpx * 28 and cy == GlobalHWVar.gpy * 7:
            tesoro = 33
    if stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
        # ottieni bomba
        if cx == GlobalHWVar.gpx * 3 and cy == GlobalHWVar.gpy * 13:
            tesoro = 36
    if stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        # ottieni armatura
        if cx == GlobalHWVar.gpx * 23 and cy == GlobalHWVar.gpy * 13:
            tesoro = 52
            avanzamentoStoria += 1
        # ottieni spada
        if cx == GlobalHWVar.gpx * 24 and cy == GlobalHWVar.gpy * 15:
            tesoro = 42
            avanzamentoStoria += 1
        # ottieni scudo
        if cx == GlobalHWVar.gpx * 27 and cy == GlobalHWVar.gpy * 15:
            tesoro = 57
            avanzamentoStoria += 1
        # ottieni arco
        if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 14:
            tesoro = 47
            avanzamentoStoria += 1
    if stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
        # ottieni pozione
        if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 10:
            tesoro = 31
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
        # ottieni esca
        if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 2:
            tesoro = 38
    if stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        # ottieni pozione
        if cx == GlobalHWVar.gpx * 26 and cy == GlobalHWVar.gpy * 15:
            tesoro = 31
        # ottieni collana rigenerante
        if cx == GlobalHWVar.gpx * 2 and cy == GlobalHWVar.gpy * 4:
            tesoro = 48
    if stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
        # ottieni arco di ferro
        if cx == GlobalHWVar.gpx * 2 and cy == GlobalHWVar.gpy * 6:
            tesoro = 67
    if stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        # ottieni bomba veleno
        if cx == GlobalHWVar.gpx * 5 and cy == GlobalHWVar.gpy * 11:
            tesoro = 37

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
        elif tesoro >= 101 and tesoro <= 120:
            dati = UtilityOstacoliContenutoCofanetti.ottieniCellaDiMemoria(dati, tesoro)
        elif tesoro == 131:
            dati[tesoro] = UtilityOstacoliContenutoCofanetti.ottieniMonete(dati, numMoneteOttenute)
        elif tesoro == 132:
            dati[tesoro], tesoro = UtilityOstacoliContenutoCofanetti.ottieniFrecce(dati, numFrecceOttenute, tesoro)
        else:
            tesoro = -2
    return dati, tesoro, avanzamentoStoria
