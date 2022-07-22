# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizInterfaccia as LI


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if tipo in GlobalImgVar.vettoreNomiNemici:
        partiDialogo = []
        if tipo == "GufoMarrone":
            nome = LI.GUFO_MARRONE
        elif tipo == "GufoBianco":
            nome = LI.GUFO_BIANCO
        elif tipo == "Struzzo":
            nome = LI.STRUZZO
        elif tipo == "Casuario":
            nome = LI.CASUARIO
        elif tipo == "Falco":
            nome = LI.FALCO
        elif tipo == "Aquila":
            nome = LI.AQUILA
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"...")
        partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoDict"):
        partiDialogo = []
        if tipo.startswith("OggettoDictCadavereGufoMarrone"):
            nome = LI.GUFO_MARRONE
        elif tipo.startswith("OggettoDictCadavereGufoBianco"):
            nome = LI.GUFO_BIANCO
        elif tipo.startswith("OggettoDictCadavereStruzzo"):
            nome = LI.STRUZZO
        elif tipo.startswith("OggettoDictCadavereCasuario"):
            nome = LI.CASUARIO
        elif tipo.startswith("OggettoDictCadavereFalco"):
            nome = LI.FALCO
        elif tipo.startswith("OggettoDictCadavereAquila"):
            nome = LI.AQUILA
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = True
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"...")
        partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["passoMontano1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInCitta5CercandoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Porca miseria, che freddo!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSilenzioCittàPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma... sono bloccati a mezz'aria...")
                partiDialogo.append(dialogo)
        elif tipo.startswith("Pazzo"):
            partiDialogo = []
            nome = "Rallo"
            if avanzamentoDialogo == 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rallo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Relei?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Come sei arrivato qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Vaga un Pazzo Montano da queste parti. Meglio fare attenzione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Un pazzo montano?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*> uno... due... tre...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Che stai-")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"QUARTA DOMANDA!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("???DOMANDA???")
                dialogo.append(u"QUARTA DOMANDA: dove sei?")
                dialogo.append(u"Sono davanti a te.")
                dialogo.append(u"Sono nel Passo Montano.")
                dialogo.append(u"Sono sulla terra.")
                dialogo.append(u"Non lo so.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("!!!RISPOSTA!!!")
                dialogo.append(u"Davanti...")
                dialogo.append(u"Nel... Pazzo Montano...")
                dialogo.append(u"Su della terra...")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mi stai mentendo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... No... perché dovrei?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non lo sai...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rallo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Tu ti fidi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Di cosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("???DOMANDA???")
                dialogo.append(u"QUINTA DOMANDA: ti fidi di quello che vedi e racconti?")
                dialogo.append(u"Certo, tu no?")
                dialogo.append(u"Di cosa dovrei fidarmi se non di quello?")
                dialogo.append(u"Non dovrei fidarmi di quello che vedo?")
                dialogo.append(u"Non lo so.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append("!!!RISPOSTA!!!")
                dialogo.append(u"Io sono il capo di questa percezione. Quello che vedo ha fede in me.")
                dialogo.append(u"Di Frrelloww, <*>#italic#capo<*> di questa percezione.")
                dialogo.append(u"Io non lo farei...")
                dialogo.append(u"<*>#italic#Mmh...<*> pazzo... Pazzo Montano...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["passoMontano7"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoPassoMontano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sto congelando...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma quello è ghiaccio? Dio santo, che cavolo ci faccio qui?!")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["passoMontano8"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNemiciBloccatiPassoMontano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non è freddo come mi ricordavo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"L'aria è fredda, ma non si sente quasi per niente... si riscalda subito...")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
