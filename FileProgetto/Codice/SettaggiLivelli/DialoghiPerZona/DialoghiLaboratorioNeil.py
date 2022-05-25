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

    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if tipo == "OggettoCellaNeil":
            partiDialogo = []
            nome = "Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoCellaDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Neil?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Neil!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Neil...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(C'è Neil qua dentro, ma non risponde...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È Neil...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLetteraInvitoReneLaboratorio":
            partiDialogo = []
            nome = "Lettera di Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È una lettera di Neil per René...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"René, ti mando i miei ringraziamenti per le risorse speditemi. Le ricerche sull'impo si sono avviate non appena è stato possibile e sono felice di comunicarti che stanno già dando ottimi risultati. Tanto che mi hanno permesso di sbloccare un fronte di ricerca che avevo ormai abbandonato da anni, ossia l'incremento di frequenza di campinamento percettivo e cognitivo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Da quel che ho potuto osservare fin'ora, gli impo possiedono tecnologie che permettono loro di elaborare informazioni a una frequenza talmente elevata da superare addirittura la frequenza con cui gli eventi reali si susseguono. Ciò vuol dire che, se la tecnologia venisse riadattata per noi esseri umani, sarebbe possibile rimanere coscienti, o addirittuara muoverci, in quei frangenti di tempo in cui il tempo stesso non scorre.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(L'apparecchio cerebrale... l'ha ricavato dall'impo...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Potremmo essere vicini a scoperte inimmaginabili, e di questo ti ringrazio infinitamente. Ti confesso di non aver ben compreso quali siano le tue pretese in cambio, il messaggero è stato un po' vago: ha richiesto informazioni sulla situazione geopolitica corrente e l'accesso illimitato a tutti i miei studi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non ho esitato ad accettare, sappiamo entrambi che l'intervento del Costruttore è imminente e non possiamo permetterci perdite di tempo. Soprattutto se questo è il suo livello tecnologico...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Il \"Costruttore\"...?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Per questo colgo l'occasione non solo per darti accesso alle mie ricerche, ma anche per invitarti a fare altrettanto, in un'ottica collaborativa e di condivisione dei nostri risultati, per prepararci al meglio alla prossima intromissione del Costruttore. Ti invito dunque a un periodo di ricerca cooperativa nei laboratori del mio castello.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Se decidessi di accettare, presentati il prima possibile al mio castello. Consegna questa lettera alle guardie e ti lasceranno entrare. Neil.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Era qui per questo René...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È un invito al castello per René...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"René, ti mando i miei ringraziamenti per le risorse speditemi. Le ricerche sull'impo si sono avviate non appena è stato possibile e sono felice di comunicarti che stanno già dando ottimi risultati. Tanto che mi hanno permesso di sbloccare un fronte di ricerca che avevo ormai abbandonato da anni, ossia l'incremento di frequenza di campinamento percettivo e cognitivo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Da quel che ho potuto osservare fin'ora, gli impo possiedono tecnologie che permettono loro di elaborare informazioni a una frequenza talmente elevata da superare addirittura la frequenza con cui gli eventi reali si susseguono. Ciò vuol dire che, se la tecnologia venisse riadattata per noi esseri umani, sarebbe possibile rimanere coscienti, o addirittuara muoverci, in quei frangenti di tempo in cui il tempo stesso non scorre.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Potremmo essere vicini a scoperte inimmaginabili, e di questo ti ringrazio infinitamente. Ti confesso di non aver ben compreso quali siano le tue pretese in cambio, il messaggero è stato un po' vago: ha richiesto informazioni sulla situazione geopolitica corrente e l'accesso illimitato a tutti i miei studi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non ho esitato ad accettare, sappiamo entrambi che l'intervento del Costruttore è imminente e non possiamo permetterci perdite di tempo. Soprattutto se questo è il suo livello tecnologico...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Per questo colgo l'occasione non solo per darti accesso alle mie ricerche, ma anche per invitarti a fare altrettanto, in un ottica collaborativa e di condivisione dei nostri risultati, per prepararci al meglio alla prossima intromissione del Costruttore. Ti invito dunque a un periodo di ricerca cooperativa nei laboratori del mio castello.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Se decidessi di accettare, presentati il prima possibile al mio castello. Consegna questa lettera alle guardie e ti lasceranno entrare. Neil.")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È l'invito per René...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiIstruzioniCalcolatoreLaboratorio":
            partiDialogo = []
            nome = "Istruzioni per il Calcolatore Di Eventi"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["creatoPersonaggioOggettoIstruzioniCalcolatoreLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È una lista d'istruzioni per il... \"Calcolatore di eventi\"...?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Posiziona il casco: occhi paralleli all'orizzonte, occhi chiusi <br> Comando d'avvio: <*>#italic#Navigazione<*> <br> Progresso temporale: <*>#italic#Procedi *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti<*> <br> Regresso temporale: <*>#italic#Regredisci *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Aspetta... posso...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(\"Calcolatore di eventi\"... non dirmi che...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Credo che siano dei comandi per questo casco qua accanto...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Posiziona il casco: occhi paralleli all'orizzonte, occhi chiusi <br> Comando d'avvio: <*>#italic#Navigazione<*> <br> Progresso temporale: <*>#italic#Procedi *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti<*> <br> Regresso temporale: <*>#italic#Regredisci *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti<*>")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono i comandi per utilizzare il calcolatore di eventi...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenericiLaboratorio":
            partiDialogo = []
            nome = "Appunti di Neil"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci sono degli appunti... non si capisce granché, è pieno di formule e calcoli incomprensibili...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non c'è traccia di alcuna spiegazione... neanche due righe comprensibili...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Oh, delle parole leggibili... \"Singolarità\"... \"Onniscienza\"... \"Segnali cerebrali\"... \"Proiezioni cerebrali\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Boh...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Forse è meglio iniziare da cose più... facili...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci sono poche parole comprensibili... \"Singolarità\"... \"Onniscienza\"... \"Segnali cerebrali\"... \"Proiezioni cerebrali\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Il resto sono formule e calcoli... credo sarebbe meglio iniziare da cose più... leggibili...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Neil... da qui si capisce come abbia fatto a renderlo infinitamente più veloce ed efficiente del calcolatore nel vulcano: non considera l'esistenza di agenti esterni... gli eventi futuri che ho visto sono ciò che succederebbe se il Costruttore e i suoi impo non influensassero più la realtà...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCalcolatoreEventi":
            partiDialogo = []
            nome = "Macchinario"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiIstruzioniCalcolatoreLaboratorio"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È una sedia con una specie di... casco...?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiIstruzioniCalcolatoreLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Quindi... mi siedo qui...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È il calcolatore di eventi...)")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
