# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipo, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo):
    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = True
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if tipo == "OggettoLettoLucy":
        partiDialogo = []
        nome = "Lucy"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("... Uh!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehi, hai fatto un brutto sogno?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("No, io stavo... stavo andando... ehm... non lo so, non importa.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perché sei sveglio?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Stavo andando in bagno, è tutto ok?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, sì... mi porti un bicchiere d'acqua quando torni?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok...")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Yaaawn... Sto ancora aspettando la mia acqua.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, sto andando.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Dai Hans... mi hai portato un bicchiere vuoto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ah, lo volevi con l'acqua?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Mmh...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Lucy... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Zzz...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Si è già riaddormentata... Posso partire adesso allora, prima che qualcun altro si svegli.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Zzz...")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non mi rimetterò a dormire.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLavandinoCucina" or tipo == "OggettoLavandinoBagno":
        partiDialogo = []
        nome = "OggettoLavandino"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Devo prendere un bicchiere prima.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
            oggettoDato = "Bicchiere con acqua"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok, ho riempito il bicchiere.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non ho più bisogno di acqua.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non ho bisogno di acqua.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoScaffaleBicchieri"):
        partiDialogo = []
        nome = "OggettoScaffaleBicchieri"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
            oggettoDato = "Bicchiere"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ecco un bicchiere, ora devo riempirlo d'acqua.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non mi servono altri bicchieri.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non ho bisogno di queste cose.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoLucy":
        partiDialogo = []
        nome = "OggettoComodinoLucy"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questa è la roba di Lucy. C'è il suo diario e... un foglio arrotolato?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non importa, non prenderò queste cose.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ho messo qua il bicchiere con l'acqua.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
            oggettoDato = "Mappa e Diario"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok, mappa e diario presi.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non c'è nient'altro di importante da prendere qui.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoHans":
        partiDialogo = []
        nome = "OggettoComodinoHans"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non tengo niente di utile qui.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È il comodino di Hans. Non c'è niente di interessante... solo una piccola lanterna.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoFinestra"):
        partiDialogo = []
        nome = "OggettoFinestra"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È notte fonda, devo partire adesso.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Hans stava guardando fuori dalla finestra quando mi sono svegliata... spero che sia ancora qua fuori e che ci stia ripensando.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLettoHans":
        partiDialogo = []
        nome = "OggettoLettoHans"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non posso rimettermi a dormire. Non voglio rimandare ancora, sono pronto.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È il letto di Hans e lui non c'è...")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoVasca"):
        partiDialogo = []
        nome = "OggettoVasca"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È una specie di fontana che abbiamo fatto io e il babbo per poterci lavare senza dover uscire di casa.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"La parte più difficile e faticosa è stata senza dubbio costruire il canale per l'acqua... ma una volta fatto quello abbiamo potuto pensare di fare anche le altre fontanelle.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È la fontana che usiamo per lavarci. È molto comodo averla dentro casa.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoGabinetto"):
        partiDialogo = []
        nome = "OggettoGabinetto"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non ho bisogno di usare il gabinetto adesso.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non mi scappa la pipì.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoCamino"):
        partiDialogo = []
        nome = "OggettoCamino"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È un camino che usiamo per riscaldare la casa e cucinare.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È il camino che usiamo sempre io e la mamma per cucinare.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoScaffaleCucina"):
        partiDialogo = []
        nome = "OggettoScaffaleCucina"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È lo scaffale dove conserviamo gli alimenti... niente bicchieri qui!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È lo scaffale dove conserviamo gli alimenti.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non ho bisogno di cibo, non ho fame adesso.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTavolinoFiori":
        partiDialogo = []
        nome = "OggettoTavolinoFiori"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È un tavolino con dei fiori... lo hanno voluto mettere perchè sembrava uno spazio troppo vuoto.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ci sono dei bellissimi fiori che sarebbero già morti se non ci fossi io ad innaffiarli.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = "Chiave ripostiglio"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Sono i miei bellissimi fiori... ma...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehi, sotto il vaso c'è una chiave!")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Sotto questo vaso era nascosta la chiave del ripostiglio... come ho fatto a non accorgermene per tutto questo tempo?")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoMamma":
        partiDialogo = []
        nome = "OggettoComodinoMamma"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È il comodino della mamma... niente di interessante.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Niente, la chiave non è qui...")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non c'è niente di utile per me qui.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoBabbo":
        partiDialogo = []
        nome = "OggettoComodinoBabbo"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È il comodino del babbo... niente di interessante qui, solo un po' di roba puzzolente.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Avrei giurato che la chiave fosse qui... devo cercare in un posto più insolito.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non c'è niente di utile per me qui.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoLettoGenitori"):
        partiDialogo = []
        nome = "OggettoLettoGenitori"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Devo fare piano, non voglio svegliarli.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non credo che tengano la chiave del ripostiglio nel letto!")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Stanno dormento profondamente, non devo fare rumore.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoCancellettoCasa"):
        partiDialogo = []
        nome = "OggettoCancellettoCasa"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non voglio andare nei campi adesso.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non credo che Hans sia andato nei campi a quest'ora.")
            partiDialogo.append(dialogo)
    elif tipo == "CaneCasa":
        partiDialogo = []
        nome = "Agglomerato"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ciao Agglo, cosa stai cercando in questi cespugli?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Deve aver fiutato qualcosa...")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehi Agglo, hai visto Hans andare da quella parte?")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoCanaleCasa"):
        partiDialogo = []
        nome = "OggettoCanaleCasa"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È il canale che abbiamo costruito per portare l'acqua del fiume nelle fontane in casa.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Qua dentro scorre l'acqua del fiume!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È stata un'idea geniale costruire questo tunnel: adesso possiamo utilizzare l'acqua direttamente in casa!")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
