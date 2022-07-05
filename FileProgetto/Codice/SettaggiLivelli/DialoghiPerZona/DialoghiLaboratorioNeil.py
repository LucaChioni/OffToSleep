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
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostTrasformazioneLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È... ha...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Come...?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostTrasformazioneLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Prima che io mi risvegliassi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Neil è sempre qua dentro...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È scomparso nello stesso momento in cui sono scomparsa anch'io...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ma nella realtà è ancora qui dentro...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Neil non c'è...")
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
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Forse tornerà prima o poi...)")
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
                dialogo.append(u"(È l'invito per René... Neil ha colto l'occasione per velocizzare le sue ricerche...)")
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
                dialogo.append(u"(È una lista di comandi... \"Comandi cerebrali del Calcolatore di eventi\"...?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Comandi cerebrali del Calcolatore di eventi (posiziona il casco: occhi chiusi e paralleli all'orizzonte): <br> Comando di accensione: <*>#italic#Navigazione<*> <br> Comando d'avvio sequenza di eventi: <*>#italic#Avvia sequenza<*> <br> Comando d'arresto sequenza di eventi: <*>#italic#Stop<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Comando progresso temporale: <*>#italic#Progredisci *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti, *x* secondi<*> <br> Comando regresso temporale: <*>#italic#Regredisci *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti, *x* secondi<*> <br> Comando movimento: <*>#italic#Movimento spaziale in *inserisci luogo*<*> <br> Il sistema proietterà gli eventi nella mente dell'utente.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ecco a te tutta la mia conoscenza.")
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
                dialogo.append(u"Comandi cerebrali del Calcolatore di eventi (posiziona il casco: occhi chiusi e paralleli all'orizzonte): <br> Comando di accensione: <*>#italic#Navigazione<*> <br> Comando d'avvio sequenza di eventi: <*>#italic#Avvia sequenza<*> <br> Comando d'arresto sequenza di eventi: <*>#italic#Stop<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Comando progresso temporale: <*>#italic#Progredisci *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti, *x* secondi<*> <br> Comando regresso temporale: <*>#italic#Regredisci *x* anni, *x* mesi, *x* giorni, *x* ore, *x* minuti, *x* secondi<*> <br> Comando movimento: <*>#italic#Movimento spaziale in *inserisci luogo*<*> <br> Il sistema proietterà gli eventi nella mente dell'utente.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ecco a te tutta la mia conoscenza.")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono i comandi per utilizzare il calcolatore di eventi... me li ha lasciati Neil...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici0Laboratorio":
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
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sono seduta qua in questo momento... nella realtà...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Neil deve averlo costruito mentre era bloccato tra due momenti...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È rimasto qui per più di sette anni...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ho voglia adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici1Laboratorio":
            partiDialogo = []
            nome = "Appunti di Neil"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Neil... qua spiega nel dettaglio il funzionamento del sistema usato dal Costruttore per creare la realtà: quella \"roccia\" in mezzo alla lava del vulcano è un calcolatore, mentre gli impo sono operai. In patica, da quel che ho capito, il calcolatore elabora gli eventi in maniera simile al calcolatore di Neil, e gli impo producono...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ho controllato mille volte, ma, dal calcolatore di Neil, non si vede come è stato costruito. All'inizio di tutto, negli eventi più lontani nel passato a cui è possibile accedere, il sistema è semplicemente già presente... insieme al Costruttore e a qualche impo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Neil in cui descrive il funzionamento del sistema usato dal Costruttore per creare gli eventi reali... dal calcolatore di Neil non si vede come è stato costruito... è semplicemente sempre esistito...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici2Laboratorio":
            partiDialogo = []
            nome = "Appunti di Neil"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Neil... qua ci sono tutte le spiegazioni di come ha fatto a rendere il suo calcolatore infinitamente più veloce ed efficiente di quello del Costruttore nel vulcano...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Principalmente per due ragioni, la prima: l'output è più immediato e sfrutta le capacità cerebrali dell'utente che lo utilizza, la seconda: non considera l'esistenza di agenti esterni... tutti coloro che sono stati fuori dalla serie di eventi, vengono cancellati dal sistema...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Questo vuol dire che il futuro che ho visto non sarà identico a quello che avverrà realmente... io sarò da qualche parte a fare qualcosa... poi Rod potrà vedere il Costruttore morto nel vulcano e magari farà qualcosa di diverso... potrà leggere il mio messaggio... potrà venire qui...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Appunti di Neil in cui descrive il funzionamento del calcolatore di eventi... io non sono considerata nelle previsioni, quindi potrei ancora cambiare qualcosa... poi farò delle prove, dovrò solo aspettare qualche miliardo di anni per controllare i risultati...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici3Laboratorio":
            partiDialogo = []
            nome = "Appunti di Neil"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Neil in cui spiega del sistema del Costruttore per \"evadere da questa dimensione\". Si riferisce alla cella nel vulcano dove ho trovato il suo cadavere. Non ho ancora capito come funziona, ma a quanto pare permette di andare in un posto in cui \"sarà finalmente possibile comprendere la realtà\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Neil gliel'ha copiata e ne ha ricostruita una qui nel suo laboratorio. Ma, dopo diversi test, ha scoperto che non è possibile utilizzarla finché almeno un'altra persona è già \"fuori\". Si può uscire solo uno alla volta... il motivo non lo spiega. Non lo sa...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Comunque sarebbe bastato far tornare il Costruttore e prendere il suo posto... come? Semplice: manda nel vulcano una ragazzina che non ha niente da fare e fai scattare qualche allarme...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Il Costruttore... credo che alla fine ci abbia voluto provare comunque ad usare la sua cella, ma... non poteva...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Neil in cui spiega il funzionamento del macchinario che permette di \"evadere da questa dimensione\"...)")
                partiDialogo.append(dialogo)
        elif tipo == "Bibliotecario" or tipo == "OggettoBibliotecarioCalcolatore" or tipo == "BibliotecarioOperato":
            partiDialogo = []
            nome = u"René"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Che diavolo...?!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... C-Come...?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Merda...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo3RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo4RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Si è operato...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpoFermo":
            partiDialogo = []
            nome = "Impo"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non mi serve...)")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
