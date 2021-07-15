# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "Nessuno"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if GlobalGameVar.dictStanze["sognoLucy1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["sognoLucy4"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizio"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Oh cavolo! Dove sono adesso!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Mi sono persa... lo sapevo...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMovimento"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Dovrei aprire quel baule prima di andare... ?")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok, Hans dovrebbe essere passato di qua... credo...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoLucy2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Perché sono venuta qui... ?")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 3 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non voglio farmi scoprire e se entro i miei genitori si sveglieranno. O forse sono ancora svegli... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("... Non lo voglio sapere... basta che non mi faccia vedere.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] and (x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Prima devo portare l'acqua a Lucy, così si riaddormenterà di nuovo e non si accorgerà che sono uscito.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Mi ha portato l'acqua ma non è tornato a letto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Dovevo immaginarlo che partiva stanotte... di certo non posso dirlo a mio padre: si arrabbierebbe troppo e mi vieterebbe di uscire.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*> provo a vedere se è ancora qua fuori da qualche parte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRisveglioLucy"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Aspetta! Prima di andare devo prendere la mia mappa e il diario.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Dovrei poter documentare qualcosa di interessante.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Fuori è troppo pericoloso di notte: devo preparami prima di uscire.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Nel ripostiglio di mio padre ci dovrebbe essere qualcosa di utile.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and (x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Fuori è pericoloso! Devo prepararmi meglio prima di uscire.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Nel ripostiglio dei miei genitori ci dovrebbe essere qualcosa di utile.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, merda! Non si apre.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("La chiave deve essere qui da qualche parte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Devo trovare la chiave per entrare!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonno4"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Bene! Quest'armatura mi entra perfettamente. Sono pronta per andare adesso.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15 or x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"I miei genitori non se la staranno passando bene, ma non posso tornare finché non scopro dov'è andato Hans.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15 or x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non mi va di tornare a casa adesso... prima devo capire come uscire da questa situazione.")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Bene, dall'altra parte della foresta c'è la città.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialDifesa"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Pant pant...<*> non mi sono mai spinto fino a questo punto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Dovrei essere quasi dall'altra parte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un attimo, c'è qualcuno più avanti!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Credo che dovrei parlargli, magari possiamo aiutarci per superare la notte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and ((x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16) or (x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 8)) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Prima di procedere potrei chiedere a quel soldato da che parte si trova la città.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Meglio prendere la legna e accamparsi qui per la notte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Hans? HAAANS? ... Cavolo! È pieno di bestie selvatiche qui!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadettaLucy"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehi, c'è un accampamento qui!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and ((x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16) or (x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 8)) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Dovrei guardare bene l'accampamento per capire se Hans è stato qui.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non sarà facile passare qua in mezzo...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"C'è un uomo a terra e... ok, prima di tutto mi devo occupare di quel bestione.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sotterratoSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = "Armatura d'acciaio"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ecco fatto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Forse non avrei dovuto prendere le sue cose ma... non credo che gli serviranno ancora...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoTombaSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta8"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Uff...<*> ma quanto è grande questa foresta!?")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["penultimaStanzaForesta"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta9"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Finalmente l'uscita!!!")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ultimaStanzaForesta"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Perfetto, adesso mi basterà seguire la strada e arriverò in città. Hans sarà sicuramente là da qualche parte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoAllaPortaDellaCittà"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("...")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["città1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["città10"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non so dove andare, devo seguire David.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Meglio seguire David.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 13 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo di poter entrare in queste abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 13 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile in queste case.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Meglio seguire David.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non ho per niente voglia di tornare lì. Poi è pieno di guardie... meglio evitare.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Meglio seguire David.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoAlzatoDalLetto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok... devo cercare Hans negli alloggi dei profughi... che non ho idea di dove siano...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Uff...<*> è difficile pensare ad altro...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 11 or x == GlobalHWVar.gpx * 12):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"N-non entrerò adesso... i soldati mi accuseranno dell'omicidio.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... ODDIO...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Devo andarmene da qui...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo ci sia niente di interessante da quella parte.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città5"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo di poter entrare in queste abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile in queste case.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Potrei chiedere a qualcuno qui intorno dove sono gli alloggi profughi... se inizio ad andare a caso potrei impiegare molto tempo...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Il cuore mi dice che sto sbagliando strada... la sinistra è dall'altra parte...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Qua ci sono tante persone che potrebbero aver visto Hans. Devo parlare con tutti prima di continuare ad esplorare la città.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città6"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 17 or x == GlobalHWVar.gpx * 18):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È chiuso. Forse questi soldati possono aiutarmi.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 17 or x == GlobalHWVar.gpx * 18):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È chiuso.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quello dovrebbe essere lo stabile che ospita gli alloggi profughi.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città7"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 15 and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo di poter entrare in queste abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 15 and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile in queste case.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà7"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Pant pant...<*> cazzo... che cos'ho fatto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Pant pant...<*> c-che faccio ora? ...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non voglio tornare indietro...")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 5 and (x == GlobalHWVar.gpx * 18 or x == GlobalHWVar.gpx * 19):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Il sangue sulle mie armi... non dovrei tenerle addosso.")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 6 and (x == GlobalHWVar.gpx * 18 or x == GlobalHWVar.gpx * 19):
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, per andare da Neil devo procedere verso sud.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città8"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo che lascino entrare persone come me o Hans.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo ci sia niente di utile nel castello.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città9"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 28 and (y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo di poter entrare in queste abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 28 and (y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile in queste case.")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Devo cercare meglio in città prima di andarmene.")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città10"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 2 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non credo di poter entrare in queste abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 2 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di utile in queste case.")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Devo cercare meglio in città prima di andarmene.")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"La Selva Arida non è da questa parte.")
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and (x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16)):
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append("Non posso gironzolare per tutta la casa, mi stanno aspettando per la cena.")
                    partiDialogo.append(dialogo)
                else:
                    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and GlobalHWVar.gpx * 8 <= x <= GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 1:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"... Non credo che Sara voglia parlare con me...")
                        partiDialogo.append(dialogo)
                    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and y == GlobalHWVar.gpy * 16:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"C'è un terrazzo enorme con una bella vista.")
                        partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Non credo ci sia niente di interessante da quella parte.")
                        partiDialogo.append(dialogo)
            elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non ha senso andare in giro per la città adesso. Avrò tutto il tempo per cercare Hans domani.")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non seguirò David. Meglio andare a letto, mi resta poco tempo per riposare.")
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 9 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È chiuso a chiave.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cavolo! Quest'acqua riscaldata... vorrei rimanere lì dentro per sempre!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perfetto. Questi andranno bene.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"] and x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mi devo ancora cambiare i vestiti. Credo che me li abbiano lasciati nella mia camera.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
                if y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 10):
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non credo di poter andare, stanno indagando sull'accaduto...")
                    partiDialogo.append(dialogo)
                elif y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 19 or x == GlobalHWVar.gpx * 20 or x == GlobalHWVar.gpx * 21):
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Mi ha detto di aspettarlo qui...")
                    partiDialogo.append(dialogo)
                elif x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16 or y == GlobalHWVar.gpy * 5:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non posso andarmene. Devo prendere la certificazione prima.")
                    partiDialogo.append(dialogo)
            elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Yaaawn... che sonno...")
                partiDialogo.append(dialogo)
            elif (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and (x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non posso gironzolare per tutta la casa, credo che darei fastidio...")
                partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and (x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di interessante da quella parte.")
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["biblioteca3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca2"]:
            if x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 11:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Chiuso a chiave...")
                partiDialogo.append(dialogo)
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPreVomito2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Puah!<*>")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 9:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Il bibliotecario mi sta aspettando...")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Devo controllare i registri prima di andare...")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"René mi sta aspettando. Devo prendere la marce da consegnare a Neil prima di andare.")
                    partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["selvaArida16"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo posto è un casino...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Però ci sono queste tracce per terra... dovrei seguirle?")
            partiDialogo.append(dialogo)
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida16"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Ohh...<*> l'uscita.")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelva"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, dopo la Selva devo costeggiare il lago... che non è qui. Perfetto, ho sbagliato strada.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, ma quello è... Rod?")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 3 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È chiusa a chiave...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["arrivoAvampostoDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non credo che questa sia la direzione giusta... forse Rod può aiurami.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Senza una mappa mi perderei di sicuro...")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["copiataMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Meglio dare un'occhiata alla mappa prima...")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Se mi segnassi il percorso da seguire, sarebbe molto più facile attraversare il labirinto...")
                    partiDialogo.append(dialogo)
    else:
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append("...")
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
