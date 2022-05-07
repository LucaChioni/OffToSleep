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
    if GlobalGameVar.dictStanze["sognoSara1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["sognoSara4"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizio"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Oh cavolo! Dove sono adesso?!)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Mi sono persa, lo sapevo...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMovimento"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Dovrei aprire quel baule prima di andare...?)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ok, Hans dovrebbe essere passato di qua...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoSara2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Perché sono venuta qui...?)")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        if (GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and ((x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 3) or (x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 7)):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non si apre...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 3):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Devo seguire Hans...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and y == GlobalHWVar.gpy * 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non voglio tornare indietro...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and y == GlobalHWVar.gpy * 16:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Devo parlare con Hans...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 3 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non voglio farmi scoprire e se entro i miei genitori si sveglieranno. O forse sono ancora svegli...? Non importa, basta che non mi faccia vedere...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"] and (x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Prima devo portare l'acqua a Sara, così si riaddormenterà e non si accorgerà che sono uscito...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(... Mi ha portato l'acqua ma non è tornato a letto...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Provo a vedere se è ancora qua fuori da qualche parte...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRisveglioSara"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Aspetta! Prima di andare devo prendere la mia mappa e il diario. Dovrei poter documentare qualcosa di interessante...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Fuori è troppo pericoloso di notte, devo preparami prima di uscire...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Nel ripostiglio di mio padre ci dovrebbe essere qualcosa di utile...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and (x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Fuori è pericoloso! Devo prepararmi meglio prima di uscire...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Nel ripostiglio di mio padre ci dovrebbe essere qualcosa di utile...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(No, merda! Non si apre...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(La chiave deve essere qui da qualche parte...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Devo trovare la chiave per entrare...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonno4"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Bene! Quest'armatura mi entra perfettamente. Sono pronta per andare adesso...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15 or x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(I miei genitori non se la staranno passando bene, ma non posso tornare finché non scopro dov'è andato Hans...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15 or x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non mi va di tornare adesso...)")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Bene, dall'altra parte della foresta c'è la città...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialDifesa"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Pant pant...<*> dovrei essere quasi dall'altra parte...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Porca miseria! Quei lupi...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Un momento... c'è un soldato...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and ((x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16) or (x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 8)) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Prima di procedere, potrei chiedere a quel soldato quale di queste strade porta alla città...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Meglio prendere la legna e accamparsi qui per la notte...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialSeppellireCadaveri"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Hans? HAAANS?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Cavolo...!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadettaSara"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ehi, c'è un accampamento qui...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and ((x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16) or (x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 8)) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Dovrei guardare bene l'accampamento per capire se Hans è stato qui...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non sarà facile passare qua in mezzo...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(C'è un uomo a terra e... ok, prima di tutto mi devo occupare di quel bestione...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sotterratoSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = "Equipaggiamento soldato"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ecco fatto...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Forse non avrei dovuto prendere le sue cose, ma... non credo che gli servissero ancora...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimessaMusicaDopoTombaSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta9"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Finalmente l'uscita!)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansFuoriCasaSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and y == GlobalHWVar.gpy * 8:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ehi, in quel cespuglio...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and y == GlobalHWVar.gpy * 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non voglio tornare indietro...)")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and (y == GlobalHWVar.gpy * 16 or x == GlobalHWVar.gpx * 30):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(C'è qualcosa incastrato in quel cespuglio...)")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ultimaStanzaForesta"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Perfetto, adesso mi basterà seguire la strada e arriverò in città. Hans sarà sicuramente là da qualche parte...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoAllaPortaDellaCittà"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
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
                dialogo.append(u"(Non so dove andare, devo seguire David...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Meglio seguire David...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 13 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non credo di poter entrare in queste abitazioni...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 13 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Meglio seguire David...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non ho voglia di tornare lì. Poi è pieno di guardie... meglio evitare...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non ho voglia di tornare lì...)")
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Meglio seguire David...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoAlzatoDalLetto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ok, devo cercare Hans negli alloggi profughi... che non ho idea di dove siano...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(<*>#italic#Uff...<*> è difficile pensare ad altro...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 11 or x == GlobalHWVar.gpx * 12):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non entrerò adesso... i soldati mi accuseranno dell'omicidio...)")
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
                dialogo.append(u"Devo andarmene da qui...")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 11 or x == GlobalHWVar.gpx * 12) and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città5"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non credo di poter entrare in queste abitazioni...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Potrei chiedere a qualcuno qui intorno per gli alloggi profughi... se inizio ad andare a caso, potrei impiegare molto tempo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Il cuore mi dice che sto sbagliando strada, la sinistra è dall'altra parte...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Qua ci sono tante persone che potrebbero aver visto Hans. Devo parlare con tutti prima di continuare a esplorare la città...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città6"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 17 or x == GlobalHWVar.gpx * 18):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso. Forse questi soldati possono aiutarmi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 17 or x == GlobalHWVar.gpx * 18):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Quello dovrebbe essere lo stabile che ospita gli alloggi profughi...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città7"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 15 and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non credo di poter entrare in queste abitazioni...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 15 and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
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
                dialogo.append(u"... <*>#italic#Pant pant...<*> c-che faccio ora?")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non voglio tornare indietro...)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 5 and (x == GlobalHWVar.gpx * 18 or x == GlobalHWVar.gpx * 19):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Il sangue sulle mie armi... non dovrei tenerle addosso...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città8"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non credo che lascino entrare persone come me o Hans...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città9"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 28 and (y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non credo di poter entrare in queste abitazioni...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 28 and (y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Devo cercare meglio in città prima di andarmene...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città10"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 2 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non credo di poter entrare in queste abitazioni...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 2 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Devo cercare meglio in città prima di andarmene...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(La Selva Arida non è da questa parte...)")
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"] and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ha senso andare in giro per la città adesso. Avrò tutto il tempo per cercare Hans domani...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non seguirò David. Meglio andare a letto, mi resta poco tempo per riposare...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Mi ha detto di aspettarlo qui...)")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and (x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 5):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non posso andarmene. Devo prendere il certificato prima...)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(C'è un terrazzo enorme con una bella vista...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Cavolo! Quest'acqua riscaldata... vorrei rimanere lì dentro per sempre...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Perfetto. Questi andranno bene...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Yaaawn...<*> che sonno...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"] and x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Mi devo ancora cambiare i vestiti. Credo che me li abbiano lasciati nella mia camera...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 14 and y == GlobalHWVar.gpy * 14) or (x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 8) or (x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 14) or (x == GlobalHWVar.gpx * 28 and y == GlobalHWVar.gpy * 8):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
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
                dialogo.append(u"(È chiuso a chiave...)")
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
                    dialogo.append(u"(Il bibliotecario mi sta aspettando...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Devo controllare i registri prima di andare...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(René mi sta aspettando. Devo prendere la marce da consegnare a Neil prima di andare...)")
                    partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
            if x == GlobalHWVar.gpx * 3 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["arrivoAvampostoDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non credo che questa sia la direzione giusta... forse Rod può aiutarmi...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Senza una mappa mi perderei di sicuro...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["copiataMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio dare un'occhiata alla mappa prima...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Se mi segnassi il percorso da seguire, sarebbe molto più facile attraversare il labirinto...)")
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Facco prima usando la scorciatoia...)")
                    partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 19 or x == GlobalHWVar.gpx * 20 or x == GlobalHWVar.gpx * 21 or x == GlobalHWVar.gpx * 22 or x == GlobalHWVar.gpx * 23 or x == GlobalHWVar.gpx * 24) and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non voglio perdere tempo, devo parlare con Sara adesso...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
            if (x == GlobalHWVar.gpx * 6 or x == GlobalHWVar.gpx * 7 or x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10) and y == GlobalHWVar.gpy * 3:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(È una grotta... bloccata da delle sbarre. Cosa ci sarà là dentro?)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Rod deve aver richiuso...)")
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
            if x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non si apre... forse la chiave è qui da qualche parte...)")
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["esternoCastello5"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ecco il passaggio per la scorciatoia. Adesso il cancello è aperto...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodDecisoDiParlareConSara"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ci sono soldati?)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 1:
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non voglio perdere tempo, devo parlare con Sara adesso...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Posso passare per la scorciatoia adesso...)")
                    partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["internoCastello21"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodArrivoAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo è... sangue? Che è successo qui...?)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo soldato si è messo prorio davanti alla porta e non mi fa passare...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodNotatoSangueNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh, il piano ascensore è aperto...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 13 or x == GlobalHWVar.gpx * 14) and y == GlobalHWVar.gpy * 15:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non si apre...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello3"]:
            if x == GlobalHWVar.gpx * 29 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 25 and y == GlobalHWVar.gpy * 5) or (x == GlobalHWVar.gpx * 25 and y == GlobalHWVar.gpy * 7):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello4"]:
            if x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello5"]:
            if x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 23 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 23 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 28 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 4) or (x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 4):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello7"]:
            if x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"] and x == GlobalHWVar.gpx * 25:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È qui che... cioè, è per me quel posto a tavola?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSalaDaPranzoCastello"] and ((x == GlobalHWVar.gpx * 1) or (x == GlobalHWVar.gpx * 30) or (y == GlobalHWVar.gpy * 1) or (y == GlobalHWVar.gpy * 16)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Mi sta venendo mal di testa per la fame... poi quel soldato ha detto che la cena è servita al primo piano e questo è il primo piano, quindi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioCenaAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ok... mangio qualcosa e vado a letto...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Anche se non ho visto letti in giro... potrei dormire su uno di quei divanetti...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Chidere ai soldati, non credo serva a qualcosa... stanno fermi immobili tutto il tempo, senza emettere un fiato...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Quello là sembra sempre fissarmi quando non lo guardo... a cosa starà pensando?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... A qualcosa starà sicuramente pensando... voglio dire, il pensiero è fondamentale per la vita, no? Se un essere non pensa, non lo si può definire vivo, giusto?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Oddio, forse non sono vivi... ma li ho visti muoversi! Per fare dei movimenti devi prima pensarli...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... No, aspetta! Non tutti i movimenti che faccio, li penso prima. Alcuni li faccio senza pensare... quindi anch'io non...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ok, non importa, devo mangiare questo... brodo adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Questa brodaglia non sa di niente... non odora di niente... sembra aria. È fredda, sa di aria fredda... fredda come questo castello, come queste persone...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non c'è nutrimento in questo brodo... come non c'è vita in queste persone...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Continuano a fissarmi quando non li guardo... dovrei provare a prenderli di sorpresa... dovrei provare a...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#WAAA!<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["urloDuranteCenaAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oddio, l'ho fatto davvero? Non si sono mossi... come se non fosse successo nulla... rimangono immobili, non reagiscono agli stimoli esterni...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non sembrano neanche preoccupati del mio urlo folle... sembra che se lo aspettassero... non sono sorpresi neanche un po'...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Cavolo... mi sento già sazia... ne ho mangiato solo un cucchiaio... cosa penseranno se non finisco di mangiare...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Niente, non penseranno niente... non mi considerano neanche...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Oddio mi sta appesantendo un sacco... meglio smetterla qui... oh cazzo, mi sta venendo sonno... mi si chiudono gli occhi... hanno messo qualcosa in questa brodaglia, lo sapevo che non dovevo fidarmi...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ok, calma! CALMA! Non avrebbe senso drogarmi! È solo un pasto pesante e mi sto abbioccando... un pasto d'aria fredda inaspettatamente pesante...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Cazzo, non riesco a tenere gli occhi aperti!)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Devo... devo fare due passi...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello8"]:
            if x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 15:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non si apre... dev'esserci qualcosa qua sotto...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello9"]:
            if x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 23 and y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 30) or (x == GlobalHWVar.gpx * 7 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13 or y == GlobalHWVar.gpy * 14)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
                    dialogo.append(u"(Non mi reggo in piedi... la mia stanza dovrebbe essere su questo piano...)")
                else:
                    dialogo.append(u"(Penso che Neil sia di sopra, dove mi hanno fermata ieri...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaUscitoDaSalaPranzoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo è il secondo piano, ma non so quale sia la stanza... devo trovarla prima di crollare dal sonno...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello10"]:
            if x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 14 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Trovata!)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Uh?!<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ma... quanto ho dormito? Che ore sono?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non capisco se è giorno o se è ancora notte. In questo posto ci sono pochissime finestre...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ora che ci penso, come arriva la luce in queste stanze? I candelabri sono sempre spenti... e non ci sono ombre...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello11"]:
            if x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 10:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 10:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(u"(La chiave non gira... devo provare un'altra porta...)")
                else:
                    dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello12"]:
            if x == GlobalHWVar.gpx * 4 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 11:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello13"]:
            if x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 15:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello14"]:
            if x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello15"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAlzatoDalLettoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non ce la faccio più con tutte queste scale... che senso ha abitare in un posto così grande?)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 2 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello16"]:
            if x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 4) or (x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 6):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpy * 5) or (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpy * 7):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello17"]:
            if x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 10:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 4 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 3) or (x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 3):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello18"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoStanza15CastelloSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È aperta adesso...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non si apre... quel soldato ha preso Impo e si è chiuso la porta alle spalle. Ha detto che la cena è servita al primo piano...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 11:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"] and x == GlobalHWVar.gpx * 26 and (y == GlobalHWVar.gpy * 6 or y == GlobalHWVar.gpy * 7 or y == GlobalHWVar.gpy * 8):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Devo rileggere un attimo quel libro di Neil sul tempo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoApprofondimentoParadossiTempoBloccato"] and x == GlobalHWVar.gpx * 26 and (y == GlobalHWVar.gpy * 6 or y == GlobalHWVar.gpy * 7 or y == GlobalHWVar.gpy * 8):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Prendo il piano ascensore...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRipresoImpoDaNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ok... Neil è... credo che abbia fatto tutte le operazioni descritte in quel libro direttamente su se stesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaStudioDiNeil"] and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh, è quello il piano ascansore?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello21ConRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPostLetturaAppuntiNeilSuRatti"] and (y == GlobalHWVar.gpy * 1 or ((x == GlobalHWVar.gpx * 10 or x == GlobalHWVar.gpx * 11) and y == GlobalHWVar.gpy * 3)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Forse nella stanza in cui mi sono risvegliata posso trovare qualcosa che mi aiuti a capire cos'è successo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"] and (x == GlobalHWVar.gpx * 10 or x == GlobalHWVar.gpx * 11) and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Devo rileggere un attimo quel libro di Neil sul tempo...)")
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 10 or x == GlobalHWVar.gpx * 11) and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non si apre...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 25 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 13:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Devo aspettare che mi chiamino. Potrei leggere qualcosa nel frattempo...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non voglio tornare indietro...)")
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"]:
            if x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Devo parlare con Neil adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Un corridoio... non so perché, ma credo sia chiaro quale sia la porta da aprire...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello20"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh... forse avrei dovuto bussare?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oddio! La sua faccia...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["voltatoBibliotecarioDopoIlDialogoPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Uh?!<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ma che cavolo...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh, posso... posso muovermi...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non voglio tornare indietro...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Uh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oddio, ma che...?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDalTavoloLaboratorioCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ahi! Gli occhi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Le mie mani...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostRimozioneBendeCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh cazzo...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["girataDavantiAlloSpecchioPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... OH CAZZO!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sono...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ok, ok...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Calma...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoTentataLuciditaPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Oh mio Dio!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sono diventata...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRatti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
            if y == GlobalHWVar.gpy * 4:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Un'altra grotta bloccata da delle sbarre...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Forse da qui si raggiunge l'interno della montagna...)")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Queste sbarre le ha messe sicuramente Rod. Dev'esserci una leva da qualche parte...)")
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non hanno un cervello, come possono pensare? Forse non ne hanno bisogno... usano gli impoFogli per quello...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Gli impoFogli sono dei pensieri già compiuti... ma compiuti da chi? Nessun'altra specie animale li usa o li produce...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Nessuna specie animale ha qualcosa in comune con gli impo. Nessuna specie conosciuta, quantomeno...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Magari non sono gli unici a vivere nella caverna, chi produce gli impoFogli magari vive con loro...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... \"Vive\"? Possiamo dire per certo che sono vivi? Chi gli materializza i pensieri probabilmente lo è...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Qualcuno abbastanza intelligente per farlo...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Un umano? Che sia opera del Nemico? Vorrebbe dire che stanno costruendo dei tunnel per attraversare la catena montuosa e attaccare da ovest...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ma sono anni che esiste questa caverna, perché avrebbero dovuto aspettare così tanto?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Forse sto andando fuori strada. Ogni volta che ci penso finisco per perdere un sacco di tempo, devo finire l'armatura e andare là dentro...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Il tempo non è certo dalla mia parte...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... La nuova recluta è riuscita ad avere un impo ancora vivo, ma ha deciso bene di collaborare con Neil. E Neil giungerà presto alle mie stesse scoperte. Tutti i miei progetti e i miei studi diventerano immediatamente obsoleti...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... E cosa risolverebbe entrare in quella maledetta grotta? Perché sto facendo tutto questo?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Smettila! Non è certo il momento di dubitare questo...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Devo reclutare qualcuno che possa aiutarmi...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Come se fosse facile trovare qualcuno tanto incosciente che voglia anche solo attraversare il Passo Montano...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... L'ultima volta che qualcuno è venuto qua su...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Aspetta...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodSuImpoNonVivi"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sara!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodCercandoSaraAlPalazzo1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sara?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Se n'è già andata?)")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Devo prendere gli strumenti prima di andarmene...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(È bloccata... devo chiedere a Rod di aprirla...)")
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Faccio prima passando dal tunnel...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Posso usare il Tunnel di Rod per tornare...)")
                    partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 7 and (y == GlobalHWVar.gpy * 3 or y == GlobalHWVar.gpy * 4)) or ((x == GlobalHWVar.gpx * 4 or x == GlobalHWVar.gpx * 5) and y == GlobalHWVar.gpy * 11):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non voglio perdere tempo, devo parlare con Sara adesso...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod3"]:
            if (x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 5) or (x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 12):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
            if x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È chiuso a chiave...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodCercandoSaraAlPalazzo2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Forse riesco a raggiungerla prima che arrivi da Neil...)")
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
            if y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(C'è l'avamposto di Rod dall'altra parte. Devo capire come abbassare queste sbarre...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Devo tirare la leva se voglio passare...)")
                    partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["vulcano1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["vulcano3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano3"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoDagliImpoTorri"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Uh?!<*>")
                partiDialogo.append(dialogo)
    else:
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"...")
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
