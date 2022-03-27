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
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoFreddoNonPercepitoPassoMontanoPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Siamo abbastanza vicini alla montagna adesso, ma non si sente nessun rumore...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Speriamo solo che non ci siano altre esplosioni...)")
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
                dialogo.append(u"Sì, sì... e collaborerete finché la persecuzione di tuo fratello non sarà conclusa, immagino.")
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
                dialogo.append(u"Ok, vediamo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perché pensa che io abbia questa roba...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Non ce li hai?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Gli hai detto che fai parte della confraternita?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*> ok, ce li ho...")
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
                dialogo.append(u"Ma perché mi volete fregare?! Che vi ho fatto?! State collaborando voi due per prendermi più monete possibili?!")
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
                    dialogo.append(u"Rimarrai arrabbiata per sempre adesso?")
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
                    dialogo.append(u"Ah, figurati chi ti ascolta sempre...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Senti <*>#italic#Olfo,<*> è stato solo un momento... non so perchè, mi sono innervosita per... è sicuramente colpa tua.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Certo, ovviamente... Prendi gli strumenti, <*>#italic#collaboratrice,<*> e torna dal tuo <*>#italic#collaboratore,<*> che sicuramente non vede l'ora di riprendere la <*>#italic#collaborazione.<*>")
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Va bene, e tu torna dai tuoi <*>#italic#confratelli,<*> <*>#italic#confratello,<*> che sicuramente non vedono l'ora di riprendere la... <*>#italic#confratellanza.<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"\"Confraternita\"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, quello che è...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"E non è una cosa da \"riprendere\", esiste sempre.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Certo Rod, certo... ah, a proposito, ho visto dei pappagalli in giro che vendono la tua merce... sono tuoi confratelli anche loro o ti stanno solo fregando la roba?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quelli non sono semplici pappagalli, sono PappaLibriSonori. Si usano per registrare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh... e come... come fai a fargli sapere quali frasi ripetere?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Parlano in base a quello che gli passa per la testa. In pratica basta suscitargli i ricordi giusti...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh, geniale...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Già... ho rubato l'idea a un corso per pirati...")
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
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodDopoAverPresoStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Che ci fai ancora qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rod, volevo chiederti... tu sai qualcosa sulle ricerche di Neil?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ho letto qualcosa, sì.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh... che cosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cose su... la vita, la realtà... roba strana.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E cosa ne pensi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa ne devo pensare? Sono teorie sensate, ma... solo teorie...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Tu cosa pensi che sia la vita? Cioè... fisicamente, intendo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non credo che nessuno sia mai riuscito a darne una definizione esaustiva. Se dovessi definirla in base a come siamo fatti, direi tipo... il pezzo di cervello dove c'è la coscienza. Ma le piante non ce l'hanno neanche un cervello, quindi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> forse le piante non sono vive.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"E come crescono? Con la magia?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dire che crescono grazie alla \"vita\", non è meno assurdo... forse si muovo e basta, come fa il vento, il mare e... tutto ciò che non ha un cervello...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non credo sia prorpio la stessa cosa... e poi neanche gli impo hanno un cervello...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Davvero? Impo non ha il cervello?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Com'è possibile...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non lo so. Adesso devo tornare a lavoro, Sara.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Aspetta, la porta sul retro è bloccata, non si apre...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah già...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Fatto. Adesso lasciami alle mie questioni.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh, come...? Aspetta mi servirebbero delle cose, posso dare un'occhiata al catalogo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, sbrigati...")
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
        elif tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoPalazzo1PostEsplosioneVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Rod?")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPappaLibroSonoroMercante":
            partiDialogo = []
            nome = "Pappagallo"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa desideri, oh mio Signore Supremo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> niente per il momento. Torna a riposo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, mio Signore Supremo.")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Io... prendo un attimo delle cose...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniPalazzoRodA":
            partiDialogo = []
            nome = "OggettoScatoloniPalazzoRodA"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi serve niente di questa roba adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci sono un sacco di scatoloni impolverati...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Degli scatoloni...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniPalazzoRodB":
            partiDialogo = []
            nome = "OggettoScatoloniPalazzoRodB"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi serve niente di questa roba adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Altri scatoloni impolverati... quanta roba ha?)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Degli scatoloni...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiInElaborazioneRod":
            partiDialogo = []
            nome = "OggettoAppuntiInElaborazioneRod"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti su... non so, forse è una specie di mappa... o degli schemi incasinati...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sta scrivendo con una foga assurda... è impossibile capirci qualcosa, le frasi sono tutte storte e si incrociano tra loro... come farà a rileggere?)")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono i miei appunti... poi li metterò da qualche parte...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Rod...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaInquinanteFaseA":
            partiDialogo = []
            nome = "OggettoAppuntiArmaInquinanteFaseA"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh, i miei vecchi appunti sull'estrazione dell'olio di ImpoFrutto...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
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
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Rod...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaInquinanteFaseB":
            partiDialogo = []
            nome = "OggettoAppuntiArmaInquinanteFaseB"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(I miei appunti sulle maxi pompe idrauliche... la prossima volta non ci saranno intoppi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
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
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Rod...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoEntrataPalazzoDiRodConTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ma che cavolo...?")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiApprendimentoPappagalli":
            partiDialogo = []
            nome = "Appunti di Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoStanzaPappagalliPalazzoDiRod"]:
                oggettoDato = "Chiave seminterrato"
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono degli appunti di Rod... incasinati come al solito...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Problemi di apprendimento con la nuova mandata... ci mancava...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il PappaLibro n.22 non fa che ripetere \"NALA NALAAA\", ma che significa?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Avevano detto \"set nuovo\"... forse ci sono stati problemi durante la spedizione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... È assurdo, non riescono più ad associare i volti alle frasi... proverò con ritratti più realistici...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh... quindi è a questo che servono...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh, c'è anche una chiave qua in mezzo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti di Rod in cui si lamenta dell'apprendimento di alcuni pappagalli...)")
                partiDialogo.append(dialogo)
        elif tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Stava dipingendo me... come sono adesso...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Quindi ha già visto come sono diventata...)")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sta mettendo molti dettagli nel volto...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Forse cercava di rendermi in qualche modo riconoscibile rispetto a... a chiunque sia stato operato in quel modo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sta dipingendo me...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloni":
            partiDialogo = []
            nome = "OggettoScatoloni"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Scatoloni...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaturaDiRod":
            partiDialogo = []
            nome = "Appunti di Rod"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono dei progetti di un'armatura...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... I materiali sono finalmente sufficienti...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... L'armatura è quasi completa e presto potrò testarla direttamente sul campo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... La raccolta di impoFrutti verrà notevolmente incrementata, il vecchio trombone la smettarà di lamentarsi della scarsità...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Che c'entra l'armatura con gli impoFrutti...?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... E poi... ha un traffico di impoFrutti con Neil...?)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono dei progetti di Rod per un'armatura...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLetteraStopTrattamentiEstetici":
            partiDialogo = []
            nome = "Lettera di Neil"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(C'è una lettera di Neil qua...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Rod, ti informo che i trattamenti estetici su Sara da te suggeriti sono stati sospesi in consegueza a delle anomalie comportamentali del soggetto in fase di ricostruzione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ti invito a rivedere e correggere la terapia e di testarla su soggetti non cruciali. Rimango in attesa di novità, Neil...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Rod...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È una lettera di Neil in cui dice di aver sospeso dei \"trattamenti estetici\" durante la mia rianimazione...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoQuadroSara":
            partiDialogo = []
            nome = "OggettoQuadroSara"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sono io... com'ero prima...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoQuadroSaraRianimata":
            partiDialogo = []
            nome = "OggettoQuadroSaraRianimata"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sono io... come sono adesso...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoPappaLibroSonoroApprendista":
            partiDialogo = []
            nome = "OggettoPappaLibroSonoroApprendista"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono un sacco di pappagalli qui...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È qui che li addestra?)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presoChiavePianoInterratoPalazzoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Una leva...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Si sono abbassate le sbarre.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Forse posso entrare nella caverna qua fuori adesso...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoMucchioImpo":
            partiDialogo = []
            nome = "Mucchio di Impo"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma...?")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ma che...?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Li ha... li ha presi lui, non Neil...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(E li ha uccisi...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Hanno tutti un buco dietro la testa...)")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono tutti morti...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLevaPalazzo":
            partiDialogo = []
            nome = "OggettoLevaPalazzo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoLevaNelPalazzoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Vediamo che succede...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È una leva...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoSbarreCaverna":
            partiDialogo = []
            nome = "OggettoSbarreCaverna"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sono delle sbarre...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiPazzoNellaCaverna":
            partiDialogo = []
            nome = "Appunti di Rod"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Rod...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Dev'essere lui, quel Pazzo Montano, che continua ad aggirarsi intorno all'ingersso della caverna...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Adesso era proprio qua sopra, spero non sia riuscito a entrare prima che chiudessi le sbarre...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non l'ho più visto né sentito in giro... spero di non trovarlo morto in un cunicolo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Il \"Pazzo Montano\"...?)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti in cui Rod parla un \"Pazzo Montano\" che si aggirava intorno all'ingersso della caverna...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiRaccoltaImpo":
            partiDialogo = []
            nome = "Appunti di Rod"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Rod...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il trombone ha iniziato a interessarsi agli impo, potrei guadagnarci qualcosa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Li ho presi tutti, non ce ne sono più in giro. Adesso ho tutto il tempo per capire come sfruttare la situazione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ho dato un'occhiata a come sono fatti. Hanno un bel po' di liquido energetico nella testa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ho iniziato il prelievo, sto ricavando una quantità incredibile di liquido. Ogni impo vale più di trenta impoFrutti... con queste quantità posso testare seriamente la mia nuova pompa idraulica...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Dio santo, ma è pazzo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono gli appunti di Rod in cui spiega come ha quasi sterminato gli Impo...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiMacchinarioIdraulico":
            partiDialogo = []
            nome = "Appunti di Rod"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Appunti di Rod su una \"pompa idraulica\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Costruzione terminata, la pompa idraulica ha passato tutti i test senza intoppi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Finalmente ho abbastanza liquido per mostrare seriamente cosa è in grado di fare la pompa. Neil ne vorrà sapere di più quando vedrà il getto proiettarsi direttamente sulle linee nemiche orientali...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Dimostrazione conclusa: la giuntura n.19 non ha retto, il sistema ha continuato a pompare e l'erogatore è esploso. Nella selva sta succedendo un macello, nel giro di qualche giorno sarà tutto distrutto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Merda, dovevo rifare tutti i test col liquido energetico, come ho fatto a non pensarci?! <br> RICORDA ROD: ACQUA ≠ LIQUIDO ENERGETICO...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ma quindi è stato Rod a fare quel casino... assurdo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono gli appunti di Rod in cui spiega come ha inquinato la Selva Arida...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoVascaMacchinario":
            partiDialogo = []
            nome = "OggettoVascaMacchinario"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(C'è uno strano liquido qua dentro...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoMacchinario":
            partiDialogo = []
            nome = "OggettoMacchinario"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non so cosa sia...)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConclusivoRodAlPalazzo"]:
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
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Il tubo è a posto...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
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
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È un tubo...)")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
