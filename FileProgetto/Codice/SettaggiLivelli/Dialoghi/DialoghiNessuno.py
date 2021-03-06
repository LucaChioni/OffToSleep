# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipo, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo):
    partiDialogo = []
    nome = "Nessuno"
    oggettoDato = False
    avanzaStoria = True
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
            dialogo.append(u"Perché sono venuta qui...?")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 3 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non voglio farmi scoprire e se entro il babbo e la mamma si sveglieranno. O forse sono ancora svegli?")
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
            dialogo.append("Dovevo immaginarlo che partiva stanotte... di certo non posso dirlo al babbo: si arrabbierebbe troppo e mi vieterebbe di uscire.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mmh... provo a vedere se è ancora qua fuori da qualche parte.")
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
            dialogo.append(u"Fuori è troppo pericoloso a quest'ora: devo preparami prima di uscire.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Nel ripostiglio del babbo ci dovrebbe essere qualcosa di utile.")
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
            dialogo.append("Nel ripostiglio del babbo e la mamma ci dovrebbe essere qualcosa di utile.")
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
            dialogo.append(u"Forse non avrei dovuto prendere le sue cose, ma... non credo che gli servissero ancora...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoTombaSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta8"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Uff... ma quanto è grande questa foresta!?")
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
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("...")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and (x == GlobalHWVar.gpx * 30 or x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16)):
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
                    dialogo.append(u"Non ha senso andare in giro per la città a quest'ora. Avrò tutto il tempo per cercare Hans domani.")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non seguirò David. Meglio andare a letto, mi restano poche ore per dormire.")
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
            if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Yaaawn... che sonno...")
                partiDialogo.append(dialogo)
            elif (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and (x == GlobalHWVar.gpx * 30 or x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Non posso gironzolare per tutta la casa, credo che darei fastidio...")
                partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and (x == GlobalHWVar.gpx * 30 or x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente di interessante da quella parte.")
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
