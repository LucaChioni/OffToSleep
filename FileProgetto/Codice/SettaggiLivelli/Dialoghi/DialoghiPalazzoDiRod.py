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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rodEntratoNelPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rod!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... È casa sua?")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPortaPalazzoDiRod":
            partiDialogo = []
            nome = "OggettoPortaPalazzoDiRod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoRodEntrareNelPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rod?")
                partiDialogo.append(dialogo)
        elif tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreBussataPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Rod?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Chi è?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rod, sono io, Sara.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sara? Ma che...?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Posso entrare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehm... no.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dai Rod, si congela qua fuori.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Perché sei venuta fin qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Devo parlarti di... una cosa. Mi manda Neil.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        if tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInPalazzoDiRod"]:
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
                dialogo.append(u"Mamma mia, c'è un casino incredibile qua dentro. E un sacco di polvere ovunque...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Hai incontrato Neil?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sì. Era davvero interessato a Impo, ma gli mancano degli strumenti per studiarlo. Mi ha mandata da te per chiederteli.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Che...? Lavori per lui adesso?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, noi stiamo... collaborando.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ahhh state collaborando, certo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, collaboriamo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo... e collaborerete finché la persecuzione di tuo fratello non sarà conclusa, immagino.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non è una... va beh... non gli ho detto di Hans. Alla fine ho pensato che fosse meglio lasciarlo andare dove vuole... come dicevi te...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Oh...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Comunque ti dicevo degli strumenti che servono a Neil... questa è la lista.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ok, vediamo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Perché pensa che io abbia questa roba...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Non ce li hai?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmmh...<*> avete parlato di impo, ovvio...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa c'è?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Niente. Non importa, ce li ho gli strumenti.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rodArrivatoAlTavoloDegliStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sono questi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Esattamente. Fanno " + str(GlobalGameVar.monetePerGliStumentiPerNeil) + u" monete.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cosa?! Ma dai, ne hai un sacco di questi affari, come fanno a costare così tanto?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È il loro valore... tu non ti preoccupare, lascia che il vecchio trombone sganci le sue monete.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma non... <*>#italic#uff...<*> non mi ha lasciato monete... sicuramente sapeva che sarebbero servite... e ne avrà a palate lui... perché non me le ha date...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh, se ne ha così tante un motivo ci sarà...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma ormai puoi occupartene tu, no? Sono sicuro che se tu farai bene la tua parte di collaborazione, lui ricambierà con altrettanto impegno.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ma perché mi volete fregare?! Che vi ho fatto?! State collaborando voi due per prendermi più monete possibili?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Tsk,<*> \"collaborare\"... faccio solo i miei interessi, come tutti. Come te, che se potessi avere questi strumenti alla metà del prezzo, li prenderesti subito senza fare domande.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma che c'entra?! Non ti starei fregando in quel caso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, mi staresti solo <*>#italic#convincendo<*> a pagare di meno.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non è la stessa cosa! Se ci fosse una scorciatoia per evitare un labirinto, io non ti farei pagare una mappa per attraversarlo, dicendoti che non ci sono strade alternative!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Vero Rod!? O dovrei dire <*>#italic#Rodolfo!?<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, non... non dovresti. E per quanto riguarda la scorciatoia, non potevo dirtelo-")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Certo, <*>#italic#Rodolfo,<*> non potevi!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Quella è una strada di Neil e vuole che rimanga segreta. Ti avrebbero uccisa se ti avessero vista passare di lì. E probabilmente avrebbero ucciso anche me per avertelo detto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Poi sei liberissima di rifiutare le mie offerte se non ti vanno bene, te l'ho già detto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mh...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... E, la prossima volta che dovrai passare per il mio avamposto, evita almeno di rovistare tra le mie cose.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mi serviva la chiave per uscire, non me ne frega niente della tua roba!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiesteMonetePerGliStrumenti"]:
                if monetePossedute < GlobalGameVar.monetePerGliStumentiPerNeil:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non ho abbastanza monete, e questo caprone non abbasserà il prezzo per me...)")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = "Strumenti di Rod"
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ecco le tue schifosissime monete!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Rimarrai arrabbiata per sempre adesso?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"No, solo finché ne ho voglia <*>#italic#Rodolfo.<*>")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Bene...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Cosa c'è? Ti dà fastidio il tuo nome completo, <*>#italic#Olfo?<*> Ti posso chiamare solo \"Olfo\" se vuoi.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Oh santo cielo...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"<*>#italic#Uff...<*> che stupida, scusa...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Cos'è questo cambio d'umore adesso?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Niente... mi sono ascoltata per un attimo e...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Ah... figurati chi deve ascoltarti sempre...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Senti <*>#italic#Olfo,<*> è stato solo un momento... non so perchè, mi sono innervosita per... è sicuramente colpa tua.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Certo, ovviamente... Prendi pure gli strumenti, <*>#italic#collaboratrice,<*> e torna dal tuo <*>#italic#collaboratore,<*> che sicuramente non vede l'ora di riprendere la <*>#italic#collaborazione.<*>")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Va bene... e tu torna dai tuoi <*>#italic#confratelli,<*> <*>#italic#confratello,<*> che sicuramente non vedono l'ora di riprendere la... <*>#italic#confratellanza.<*>")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"<*>#italic#Mmmh...<*> \"confraternita\", non \"confratellanza\"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sì, quello che è...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... E non è una cosa da \"riprendere\", esiste sempre.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Certo Rod, certo... ah, a proposito, ho visto dei pappagalli in giro che vendono la tua merce... sono tuoi confratelli anche loro o ti stanno fregando la roba?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Quelli non sono semplici pappagalli, sono PappaLibriSonori. Si usano per registrare...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Oh... e come... come fai a fargli sapere quali frasi ripetere?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Basta suscitargli i ricordi giusti.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Oh... assurdo...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Già... ho rubato l'idea a un corso per pirati... Ahhh... mi manca il mio vecchio compagno di corso Sangue Al Naso...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Un corso... per pirati?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Comunque... se vuoi fare più in fretta per tornare, puoi usare il mio tunnel. Porta direttamente all'avamposto. Lo trovi sul retro...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Ok.")
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sono molto occupato adesso. Se ti serve qualcosa, prendilo e lasciami alle mie questioni.")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniPalazzoRodA":
            partiDialogo = []
            nome = "OggettoScatoloniPalazzoRodA"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono un sacco di scatoloni impolverati...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniPalazzoRodB":
            partiDialogo = []
            nome = "OggettoScatoloniPalazzoRodB"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Altri scatoloni impolverati... quanta roba ha?)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiInElaborazioneRod":
            partiDialogo = []
            nome = "OggettoAppuntiInElaborazioneRod"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoUscitoDalPalazzoDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti su... non so, forse... una specie di mappa o degli schemi incasinati...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sta scrivendo con una foga assurda... è impossibile capirci qualcosa, le frasi sono tutte storte e si incrociano tra loro... come farà a rileggere?)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaInquinanteFaseA":
            partiDialogo = []
            nome = "OggettoAppuntiArmaInquinanteFaseA"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sono appunti su un progetto di Rod... sembrano dei metodi per estrarre qualcosa dagli ImpoFrutti... tipo un liquido...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono dei disegni che mostrano l'interno degli ImpoFrutti... sono parecchio strani...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaInquinanteFaseB":
            partiDialogo = []
            nome = "OggettoAppuntiArmaInquinanteFaseB"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sono appunti su un progetto di Rod... non capisco bene cosa sia, sembra una specie di rubinetto gigante...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono alcune formule che simulano la traiettoria di un getto d'acqua spruzzato a varie velocità e angolazioni rispetto al terreno...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(A cosa dovrebbe servire una roba del genere?)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ecco il tunnel.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oddio, quel coso arriva fin qui?!")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoTuboPalazzoRod":
            partiDialogo = []
            nome = "OggettoTuboPalazzoRod"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È una specie di tubo molliccio. Sembra fatto con pelle di serpente...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Dev'essere opera di Rod...)")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
