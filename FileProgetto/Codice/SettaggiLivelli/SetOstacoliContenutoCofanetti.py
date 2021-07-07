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
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy3"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy4"]])
    elif stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, 0, +GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
    elif stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, GlobalGameVar.dictStanze["casaHansLucy2"]])
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
    elif stanza == GlobalGameVar.dictStanze["città1"]:
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
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, 0, -GlobalHWVar.gpy, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, -GlobalHWVar.gpx, 0, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, -GlobalHWVar.gpx, 0, -1])
        entrateStanza.extend([GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, -GlobalHWVar.gpx, 0, -1])
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
    elif stanza == GlobalGameVar.dictStanze["casaDavid1"]:
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
    elif stanza == GlobalGameVar.dictStanze["biblioteca1"]:
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
    elif stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
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
    elif stanza == GlobalGameVar.dictStanze["selvaArida1"]:
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
        if GlobalGameVar.dictStanze["sognoLucy1"] <= stanza <= GlobalGameVar.dictStanze["sognoLucy4"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliSogno.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliCasa.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliForestaCadetta.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliStradaPerCitta.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliCitta.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliCasaUfficiale.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliBiblioteca.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliStradaPerSelvaArida.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)
        elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
            stanza, x, y, nx, ny, escludiOggettiBassi = OstacoliSelvaArida.setOstacoli(stanza, x, y, nx, ny, escludiOggettiBassi)

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
        # ottieni monete
        if cx == GlobalHWVar.gpx * 21 and cy == GlobalHWVar.gpy * 10:
            tesoro = 131
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
        # ottieni monete
        if cx == GlobalHWVar.gpx * 29 and cy == GlobalHWVar.gpy * 9:
            tesoro = 131
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
    if stanza == GlobalGameVar.dictStanze["selvaArida1"]:
        # ottieni batteria
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
            dati[tesoro] = UtilityOstacoliContenutoCofanetti.ottieniMonete(dati, numMoneteOttenute)
        elif tesoro == 132:
            dati[tesoro], tesoro = UtilityOstacoliContenutoCofanetti.ottieniFrecce(dati, numFrecceOttenute, tesoro)
        else:
            tesoro = -2
    return dati, tesoro, avanzamentoStoria
