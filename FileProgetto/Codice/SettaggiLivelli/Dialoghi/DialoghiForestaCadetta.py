# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if tipo == "OggettoSiepe":
        partiDialogo = []
        nome = "OggettoSiepe"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"C'è un cinghiale incastrato in questo cespuglio...?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Sta facendo degli strani lamenti e sta perdendo sangue. Cosa stava cercando di fare? Forse inseguiva qualcosa?...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Credo che mi attaccherebbe se lo liberassi, quindi... sono costretta a lasciarlo qui e sperare che riesca a cavarsela in qualche modo.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mi attaccherebbe se lo liberassi, quindi lo lascerò qui sperando che riesca farcela da solo.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo cinghiale non è riuscito a liberarsi... almeno ha smesso di fare quegli strazianti lamenti...")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoFuoco":
        partiDialogo = []
        nome = "OggettoFuoco"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sembra allestito per fare un piccolo falò.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Qui è dove Sam ha intezione di accendere il fuoco per la notte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo falò è stato usato di recente...")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Probabilmente questo accampamento era stato allestito da quel soldato che ho trovato morto in questa foresta.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCibo":
        partiDialogo = []
        nome = "OggettoCibo"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È una tavoletta di legno con una tovaglietta sopra.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Presumo che Sam voglia mettere qua il cibo che raccoglierà.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sam ha raccolto un bel po' di carne.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mi domando cosa abbia cacciato... le ossa sembrano piccole ma molto robuste...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Qua sopra c'è della carne fresca. Delle gocce di sangue stanno ancora colando per terra.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ma Hans non sa cacciare... che ci sia qualcun altro nel bosco?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok ok, calma! Starà sicuramente bene.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"C'è della carne su questa tavoletta e non è di Hans...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Credo che sia stato quel soldato ad essersi procurato questa carne.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Qualche animale dev'essersi divorato tutto.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoMucchioLegna":
        partiDialogo = []
        nome = "OggettoMucchioLegna"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È un mucchietto di legna.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna2"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non c'è ancora abbastanza legna per la notte.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Devo raccoglierne altra.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, ho raccolto abbastanza legna adesso.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È un mucchio di legna da bruciare.")
            partiDialogo.append(dialogo)
    elif tipo == "FiglioUfficiale":
        partiDialogo = []
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"]:
            nome = "Soldato"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm... salve...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Uh!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Stai lontano ragazzo!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("No, non voglio causarti problemi. Fai parte dell'esercito cittadino, vero?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Il mio nome è Sam e sto affrontando l'ultima prova per diventare ufficiale dell'esercito cittadino. Non ti conviene provare a derubarmi ragazzo: di solito non mi batto al di fuori degli allenamenti, ma nel caso ti avverto che sono armato e ben addestrato!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Non voglio derubarti, se avessi voluto di certo non mi sarei fatto notare in questo modo!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Mmh... cosa ci fai in mezzo alla foresta di notte senza neanche un'arma?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sto cercando di attraversarla per arrivare alla città e... sono disarmato perché mi aspettavo meno pericoli... e comunque me la posso cavare lo stesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Mmh... certo. Senti ragazzo se mi aiuterai a finire di allestire l'accampamento, potrai passare qua la notte e continuare domani il tuo cammino.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non chiamarmi <*>#italic#ragazzo<*>, se stai affrontando questa prova vuol dire che hai più o meno la mia età!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non è una questione di età <*>#italic#ragazzo<*> ma di esperienza!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se vuoi sopravvivere stanotte vai a raccogliere la legna che ho tagliato ad est di qui. Altrimenti, se vuoi andare da solo, procedi verso sud e troverai la città.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Va bene, va bene... vado a prendere la legna.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Allora fai in fretta, tra poco sarà molto più pericoloso! Nel frattempo io mi procurerò del cibo.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["legnaDepositata"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Dove hai detto che posso trovare della legna?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ho già tagliato la legna ad est di qui, devi solo prenderla e metterla accanto al falò.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["legnaDepositata"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ho portato tutta la legna che ho trovato.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mmh... sì, dovrebbe bastare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Vieni, accendiamo il fuoco e organizziamo i turni per la notte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehm... è buona questa carne... che cos'è?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("... cinghiale...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Cinghiale!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Voglio dire il sapore è quello ma... queste ossa mi sembrano troppo piccole per un cinghiale!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Mmh...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm ehm... da quanto sei in questa foresta?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Da cinque giorni.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("E quanto ci devi rimanere ancora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"In totale la prova è di due settimane, quindi... altri nove giorni.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("E cosa succede se torni prima o se non torni affatto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Beh... non supero la prova.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ah beh certo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ma, scusa se te lo chiedo: tecnicamente non dovrebbe essere vietato l'aiuto di altre persone?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mi è concesso sfruttare tutto ciò che mi viene messo a disposizione dalla natura... tu non ne fai parte ragazzo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Mah... senz'altro <*>#italic#ragazzo<*>...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mmh... e tu invece perché stai andando tutto solo verso la città?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non lo so... faccio il contadino da tutta la vita e mi ero un po' stufato... e poi... diciamo che vorrei usare il mio tempo per cose più interessanti di ...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"OH CAZZO, ATTENTO!!!")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoLegna"):
        partiDialogo = []
        nome = "OggettoLegna"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna1"] and avanzamentoDialogo == 0:
            oggettoDato = "Legna"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Credo che sia questa la legna tagliata da Sam... di sicuro non basterà per la notte.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Qui intorno ce ne dovrebbe essere dell'altra.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna2"] and avanzamentoDialogo == 0:
            oggettoDato = "Legna"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ecco dell'altra legna! Ancora un po' e posso tornare indietro.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"] and avanzamentoDialogo == 0:
            oggettoDato = "Legna"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok, ho preso abbastanza legna. Adesso devo portarla all'accampamento.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non c'è più legna da prendere qui.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ci sono dei bastoncini di legno per terra.")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCinghiale":
        partiDialogo = []
        nome = "Cinghiale"
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("<*>#italic#GRUNT GRUNT!!!<*>")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoPersonaCadavereSam":
        partiDialogo = []
        nome = "Soldato"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Devo liberare la zona prima di occuparmi di lui.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Soldat...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ohh... cazzo...")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTombaSam":
        partiDialogo = []
        nome = "OggettoTombaSam"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Credo che stesse cercando di scappare da quel cinghiale e...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("... forse stava cacciando... che sia stato lui ad allestire quell'accampamento?")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Hanno messo una lapide. C'è scritto solo \"Sam\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... È il figlio di David... era...")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
