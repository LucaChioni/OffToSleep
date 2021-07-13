# -*- coding: utf-8 -*-

import GlobalHWVar
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
    if tipo == "PadreUfficialeServizio":
        partiDialogo = []
        nome = "Soldato"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Chi sei e cosa vuoi?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sono... ehm... mi chiamo Lucy e sto cercando mio fratello. Si chiama Hans e ha più o meno la mia età. Dovrebbe essere passato di qui non molto tempo fa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Sei da sola?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"<*>#italic#Mmh...<*> Se tuo fratello è in città, è stato allocato in uno degli alloggi profughi. E al momento gli alloggi sono tutti occupati... potrebbe aver preso uno degl'ultimi posti disponibili.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questo però vuol dire che non c'è più spazio per nessun altro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Posso dividere la stanza con lui!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"<*>#italic#Tsk,<*> sì certo! Non credo proprio. Ogni stanza ha una ventina di letti e ogni letto ospita almeno tre o quattro persone: se un alloggio è al completo significa che non c'è più spazio neanche per entrare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Oh... e come...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La tua armatura d'acciaio... dove l'hai presa?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Era... l'ho trovata su un cadavere di un soldato nella foresta e... ho pensato che mi poteva essere utile per arrivare in città...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"E... il soldato che la indossava?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"L'ho sepolto perché non venisse divorato dai lupi e dai cinghiali...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Senti... per stanotte potrai essere mia ospite: ti farò preparare una stanza. Ma da domani dovrai togliere il disturbo perché, come avrai già intuito, siamo un po' al limite con le risorse.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("V-va bene, grazie ma... chi sei tu?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Il mio nome è David. Sono ex ufficiale dell'esercito cittadino, ora a comando della guardia notturna.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Vado a predisporre la guardia per la mia assenza e andiamo.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoDavid"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Seguimi, casa mia è da questa parte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Da questa parte.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non manca molto.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Siamo arrivati.")
            partiDialogo.append(dialogo)
    elif tipo == "Mercante":
        partiDialogo = []
        nome = "Rod"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavid"]:
            nome = "Sconosciuto"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Chiedo scusa, signore. Sto cercando gli alloggi profughi, sai dirmi dove si trovano?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Eh!? Io stavo... Ehm ehm, gli alloggi? Sono in un edificio che si affaccia su quella strada che va verso ovest.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Verso ovest?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, ovest... a sinistra.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehm... ok...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sinistra... sai distinguere destra e sinistra?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì sì, certo... lo so...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Dio santo! Non ci credo... ok, provo a spiegartelo, vediamo... Mettiti entrambe le mani sul petto. La mano sinistra è quella con cui senti battere il cuore. Adesso devi seguire quella direzione, ragazza. Segui il tuo cuore e troverai la tua strada.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene, va bene. Ho capito. Non c'è bisogno di prendermi in giro... adesso lo so.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto, arrivederci.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"]:
            nome = "Sconosciuto"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa se ti disturbo di nuovo. Potresti ripetermi dove si trovano gli alloggi profughi?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"A sinistra, s-i-n-i-s-t-r-a! Dove ti batte il cuore. Se fai fatica a ricordarlo, puoi tenere le mani sul petto durante il tragitto e... cioè... no, questo forse è meglio di no. Qualcuno potrebbe fraintendere...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene, va bene. Me lo ricordo.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["resettatoAvanzamentoDialoghiCittadiniACuiChiediInfo"]:
            nome = "Sconosciuto"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa nuovamente il disturbo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ancora tu? Se mi chiedi di nuovo da che parte è la sinistra, impazzisco.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È dove batte il cuore, ho capito. Senti, volevo chiederti se... ma perché continui a guardarti attorno!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perché... no, sto solo osservando in giro... come prosegue la vita cittadina... nessuno in particolare, solo il movimento delle persone in generale...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì... di sicuro non stai fissando quella ragazza con i capelli rossi laggiù...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Cosa!? Nessuno in particolare, ho detto! Poi non posso fissare qualcuno se continuo a girarmi, no?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Certo, certo... Comunque... tu che osservi così tanto \"il movimento delle persone in generale\", hai per caso visto passare da queste parti un ragazzo più o meno della mia età, un po' più alto di me, con i capelli neri... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"<*>#italic#Tsk!<*> Non rivelo informazioni di questo tipo senza nessun tipo di compenso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Cosa?... Sto solo cercando mio fratello...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Non parlerò senza compenso. Sono " + str(GlobalGameVar.monetePerEntrareNellaConfraternita) + u" monete.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(str(GlobalGameVar.monetePerEntrareNellaConfraternita) + u" monete!? Per rispondere a una domanda!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì... diciamo che in realtà questa è una piccola quota necessaria per... per entrare nella confraternita. Una volta dentro ti verranno confidate le informazioni che richiederai. Per non parlare di tutte le altre risorse a cui potrai avere accesso concedendo dei piccoli sostegni economici...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Nella \"confraternita\"? Suona proprio come una truffa.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Noo, non lo è. Giuro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Senti, non mi interessa della confraternita. Posso pagare di meno solo per questa domanda?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mi dispiace, non posso rivelare informazioni a chi non è nella cofraternita... vorrei tanto, giuro. Ma non posso proprio, è una delle regole...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Certo, sono sicura che tu non te lo sia appena inventato... " + str(GlobalGameVar.monetePerEntrareNellaConfraternita) + u" monete per avere l'opportunità di spendere altre monete per delle \"risorse\"... Non mi sento per niente truffata, anzi sembra un'opportunità da prendere al volo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Lo è. Non mi capita spesso di offrire questa opportunità. Sei stata fortunata.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Certo...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerEntrareInConfraternita"]:
            if monetePossedute < GlobalGameVar.monetePerEntrareNellaConfraternita:
                nome = "Sconosciuto"
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Senti, mi potresti dire dove hai visto mio fratello come favore? Poi valuterei molto più seriamente di entrare nella confraternita.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo, sono " + str(GlobalGameVar.monetePerEntrareNellaConfraternita) + u" monete.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Tieni le " + str(GlobalGameVar.monetePerEntrareNellaConfraternita) + u" monete... ehm... non so ancora il tuo nome...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perfetto! Ti do il benvenuto nella confraternita. Io sono... ehm... Rod.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rod... piacere, io sono Lucy... Quindi? Dove hai visto mio fratello?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Allora... hai chiesto di un ragazzo della tua età, un po' più alto di te e con i capelli neri... Se devo essere sincero, non ho visto nessuno in città che corrispode a queste descrizioni...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cosa?! Con che faccia hai avuto il coraggio di chiedermi delle monete, allora!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh, ti sto comunque dando delle informazioni. E hai tutti i vantaggi di essere nella confraternita... Tra l'altro, ora che ci penso, non ho mai visto neanche te da queste parti. Siete arrivati oggi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Uff!<*> Assurdo... Siamo arrivati durante la notte. Mio fratello è arrivato prima di me e gli è stato assegnato un alloggio che, a quanto pare, era l'ultimo rimasto. Perciò io sono stata ospite di David, il comandante della guardia notturna.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Addirittura... Va beh, quindi non siete arrivati insieme e non l'hai neanche mai visto in città... Beh, buona fortuna.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Aspetta! Cosa dovrei fare, allora?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa ne so io!? Tornatene a casa e aspettalo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Senti, non lo so... La biblioteca è frequentata da molti ragazzi della vostra età. Magari il gestore saprà dirti qualcosa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, biblioteca. Che si trova... ?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Nella strada che porta ad est.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah, aspetta... ehm... Lucy. Ora che sei nella confraternita hai diritto ad accedere al catalogo di risorse disponibili. Quando ti serve qualcosa, ti farò dare un'occhiata.")
                partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = True
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehi Rod, cosa dicevi riguardo alle \"risorse\" della confraternita? Posso prendere qualcosa?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Certo. Dai pure un'occhiata.")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi Rod, tra le tue risorse hai per caso un documento o qualcosa del genere che possa farmi entrare in biblioteca?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non sono le <*>#italic#mie<*> risorse. Comunque non c'è bisogno di scomodare la confraternita per queste cose. Per avere un documento di residenza basta richiederlo a chi ti ha ospitata...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mh...<*> un po' deludenti le possibilità di questa confraternita...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Guarda che anche tu ne fai parte! Potresti contribuire al posto di lamentarti.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sono appena arrivata... piuttosto potrei valutare di andarmene in un'altra, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Come vuoi. Sono " + str(GlobalGameVar.monetePerLasciareLaConfraternita) + u" monete per lasciare la confraternita.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Ah ah,<*> certo...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi Rod, che risorse offre oggi la confraternita?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dai un'occhiata e prendi quello che ti serve.")
                partiDialogo.append(dialogo)

    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = "Soldato"
            if y == GlobalHWVar.gpy * 2:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Vai con il comandante, qua ci pensiamo noi.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Chiedo scusa, dovrei passare.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Questa zona è accessibile solo ai mercanti. Tu non sei un mercante.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sì che sono un mercante.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Benissimo, mostrami la licenza allora.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ehm... l'ho dimenticata...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Questa zona è accessibile solo ai mercanti.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 15:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Che ci fa una ragazzina tutta sola nel bel mezzo della notte, eh? Non lo sai che è pericoloso?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sì. So badare a me stessa.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"<*>#italic#Tsk!<*> Certo certo...")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non viaggiare mai da sola, ragazzina!")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non puoi passare di qua, ragazzina!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Perché no?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Perché io ti ho detto che non puoi!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"E chi sei tu?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"No, aspetta aspetta! Ho esagerato... Va bene, non passerò di qua.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Sarà meglio!")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Smamma ragazzina!")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 5:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non ti consiglio di procedere per questa direzione, ragazza. La fuori è pericoloso.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"C'è una guerra in corso?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"No, parlo della foresta. È popolata da bestie molto aggressive.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"La foresta è popolata da bestie molto aggressive.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 12:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Se fossi in te non uscirei dalla città adesso. La foresta è un posto pericoloso per una ragazzina come te.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Questa strada porta solo alla foresta?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Sì. Non è permesso spingersi oltre.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"La foresta è un posto pericoloso per una ragazzina come te.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa signore...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, grazie non m'interessa.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"(Questo tizio non vuole parlarmi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Si sposti signorina, non vede che sto scegliendo le arance!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, volevo chiereti un'inform...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Si sposti, per cortesia. Non mi interessano le vostre iniziative!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(A quanto pare questo tizio è troppo impegnato a scegliere le arance...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma guarda te come sono brutti questi pomodori!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Posso chiedere un'informazione?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Marci! Tutti marci! Dovrebbero costare la metà!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E non li prendere. Ci sono altre bancarelle con dei pomodori...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Mi sta ignorando...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Questi pomodori sono tutti marci! Dovrebbero costare la metà!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Continua a lamentersi di questi pomodori... Perché non va in un'altra bancarella...?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Arance e pomodori, arance e pomodori. Cosa c'è di meglio di un buon pranzo con arance e pomodori?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Con arance e pomodori... ?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Con arance e pomodori!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non so, non li ho mai mangiati insieme.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Neanch'io. Mi stavo giusto chiedendo se fosse il caso...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi sembra una bella accoppiata.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non puoi saperlo finché non lo provi, ragazza!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Arance e pomodori... Cosa ci può essere di meglio... ?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
        if tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Qua mancano dei cavoli!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, tu lavori qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, mi dica. Ha bisogno di qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Come mai c'è così tanta merce oggi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non è più del normale, ragazza. Se vieni qui troverai sempre frutta e verdura in abbondanza e a prezzi scontati!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sempre!? È richiesta così tanta roba tutti i giorni!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehm... No, non è richiesta. Ma più ne metti e più ne comprano.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E cosa fate con quella che rimane? Cioè, non marcisce?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh, molta rimane e la buttiamo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma come fate a guadagnarci se la buttate?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non ti preoccupare. Se mostri più merce, la gente compra molto di più.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, ok. Ma da quella che butti non guadagni niente, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Credimi, non lo faremmo se non fosse vantaggioso.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Là mancano dei cavoli e là dell'uva!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quest'uva è strana...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Uva? Queste sono melanzane.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma che vai dicendo? Le melanzane sono gialle. Questa è chiaramente uva!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Non è uva. Poi i meloni sono gialli, non le melanzane!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma sei completamente impazzita!? Ho trent'anni, vuoi venirmi a insegnare te i colori della frutta!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Certo, questa non è... Va beh, non importa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah, sarà meglio!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Da quando le carote sono così stondate?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Spostati, spostati! Fai largo, devo passare!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Va bene, va bene...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non le parlerò di nuovo. Qua le persone sembrano molto scortesi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, non ho tempo adesso!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché siete tutti così di fretta?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Levati, ho detto! Devo tornare a casa, mio figlio mi sta aspettando!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non voglio prendermi altri urli da questa!)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
        if tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Oddio, ho lasciato i documenti in casa!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah, no. Ce li ho qui...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Signore...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Aspetta! Le chiavi!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Per caso sai...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah, no. Sono in tasca...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi ascolta...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                avanzaColDialogo = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cavolo! Dovrei tornare in casa e controllare se ho preso tutto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa, signore...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ho chiuso i rubinetti!?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Salve bella ragazza. Hai bisogno di qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehm... Sì, sto cercando gli alloggi profughi. Sai dirmi dove sono?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Gli alloggi? Perché una bella ragazza come te dovrebbe andare in un posto simile?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sto cercando una persona...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Chiunque sia, se vive in quel posto, non merita di averti. Io posso portarti a vivere nelle migliori ville cittadine se lo desideri.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, grazie. Devo andare agli alloggi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh, come ti pare... Io non ti accompagnerò in quelle miserabili abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Io non ti accompagnerò in quelle miserabili abitazioni.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa signore... hai per caso visto da queste parti un ragazzo di nome Hans?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Spiacente, la mia attenzione è solo per le ragazze. Se è un compagno quello che cerchi, sappi che io non ti lascerei sola neanche un momento. Non come quel <*>#italic#Hons<*> che vai cercando.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Si chiama <*>#italic#Hans<*> ed è mio fratello.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Tuo fratello? E che bisogno c'è di un fratello quando puoi avere me?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non... Senti, non importa. Lo cerco da sola.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non ho visto nessuno <*>#italic#Hounts<*> passare di qua. Ma ci sono io se lo desideri.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"C-ciao, serve qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sto cercando gli alloggi profughi. Sai da che parte devo andare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Gli alloggi... mi sembra a nord-est di qui... no, forse era nord-ovest? Non mi ricordo bene...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok. Intanto vado verso nord, poi chiedo in giro. Grazie mille.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"D-di niente.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non mi ricordo bene dove siano gli alloggi... forse nord-ovest?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa... hai visto un ragazzo di nome Hans da queste parti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, non conosco nessun Hans.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non conosco nessun Hans.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ciao, signora. Sai dirmi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Signora!?<*> Ma chi ti credi di essere!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Scusa... ?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma vai a chiedere scusa a qualcun altro! Maleducata! <*>#italic#Signora!<*> Ma come si permette!?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Smettila di disturbarmi! Altrimenti chiamo le guardie!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
        if tipo == "OggettoFinestraCasaDavid":
            partiDialogo = []
            nome = "OggettoFinestraCasaDavid"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Da questa finestra si vede l'interno della casa. Sembra enorme...")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa, sai dirmi dove posso trovare gli alloggi profughi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo, bellezza. Conosco anche dei posti migliori in cui potremmo alloggiare e divertirci per bene.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, non... io ho solo bisogno di andare agli alloggi profughi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Eddai! Ti offro la birra!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Senti, non importa. Faccio da sola.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa, per caso hai visto una persona di nome Hans con...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, ho visto te, bambolina, e questo mi basta. Ti va di unirti a noi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, non... volevo solo sapere se...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Eddai! Ti offro la birra!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Senti, non importa. Faccio da sola.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questi due sono parecchio ubriachi... meglio evitare.)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehi, bellezza! Dove vai così di fretta?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Eh?... Sto andando... hai bisogno di qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perché giri tutta sola intorno alla villa del comandante? Sei la sua nuova puttana, per caso?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cosa...!? No, mi ha ospitata per... cioè, sono arrivata ieri notte in città e gli alloggi profughi erano pieni, quindi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quel maiale! Le prende sempre più piccole, eh? <*>#italic#Hahaha...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, non... scusa sono di fretta, devo andare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dove vuoi andare!? Hai avuto tutta la notte per David, ora non hai un po' di tempo per me!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Lasciami passare!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehi, datti una calmata! Io e il mio amico volevamo solo parlare un po' con te, non possiamo? Non siamo abbastanza ricchi per essere degni di una conversazione, <*>#italic#puttana!?<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dove credi di andare!? Vieni qui!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Vieni qui, troia!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Brutta troia schifosa! L'hai ucciso!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... S-stai lontano...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Vieni qui, schifosa puttana!")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Salve signore, per caso sai dirmi dove devo andare per gli alloggi profughi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma salve, bellezza. Vuoi venire a divertirti con noi? La prima birra te la offro io!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, non voglio birra... Gli alloggi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Tieni bevi un po'!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa ora devo andare...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Salve signore, sapresti dirmi se un certo Hans è passato di qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma salve, bellezza. Vuoi venire a divertirti con noi? La prima birra te la offro io!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, non voglio birra... Sto cercando...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Tieni bevi un po'!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa ora devo andare...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo non mi sente neanche... come fa ad essere ubriaco già a quest'ora?!)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, va tutto bene?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo bambolina. E tu?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"S-sì... tutto bene.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ottimo! <*>#italic#Hahaha...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPersonaCittadino1Cadavere" or tipo == "OggettoPersonaCittadino3Cadavere":
            partiDialogo = []
            nome = "Cadavere"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città5"]:
        if tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusate...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Smack... Mwah...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ehi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi sentono neanche.)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Posso aspettare quanto voglio, questi due non finiranno mai di baciarsi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Com'è possibile che siano ancora qui a baciarsi?)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusate...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non adesso! Siamo molto occupati!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non adesso! Siamo molto occupati!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Chiedo scusa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No! Levatevi dai piedi voi! Con le vostre \"opportunità imperdibili\"!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma non voglio...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Basta! Togliti di torno!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"(Questo tizio non vuole parlarmi. Sembra anche molto arrabbiato.)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Posso interrompervi un attimo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Smack... Mwah...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ehi... ?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi sentono neanche.)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Posso aspettare quanto voglio, questi due non finiranno mai di baciarsi...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Com'è possibile che siano ancora qui a baciarsi?)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza2":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusami. Mi hanno detto che in città ci sono degli alloggi per i profughi. Sai dirmi da che parte sono?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehm... no, non saprei. Vivo qui da poco, scusami. Potresti provare a chiedere a quel ragazzo laggiù. Ci ho parlato una volta, sembra sapere tutto di questa città.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quel tipo losco col cappuccio che ci sta fissando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì... dici che ci sta guardando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ogni tanto si gira da un'altra parte, ma poi guarda nuovamente in questa direzione. Forse è solo una mia impressione ma io starei attenta a non farmi seguire...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma no, non è un pazzo. L'ho conosciuto, è stato molto gentile con me. Di sicuro saprà aiutare anche te.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> Va bene, tanto vale provare...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusami. Sto cercando un ragazzo di nome Hans. L'hai per caso visto passare da queste parti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, non ho conosciuto nessun Hans. Vivo qui da poco, scusami. Potresti provare a chiedere a quel ragazzo laggiù. Ci ho parlato una volta, sembra sapere tutto di questa città.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quel tipo losco col cappuccio che ci sta fissando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì... dici che ci sta guardando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ogni tanto si gira da un'altra parte, ma poi guarda nuovamente in questa direzione. Forse è solo una mia impressione ma io starei attenta a non farmi seguire...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma no, non è un pazzo. L'ho conosciuto, è stato molto gentile con me. Di sicuro saprà aiutare anche te.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> Va bene, tanto vale provare...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Prova a chiedere a quel tizio laggiù. L'ho conosciuto, è stato molto gentile con me. Di sicuro saprà aiutare anche te.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Chiedo scusa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, per favore! Stiamo affrontando una conversazione importante.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Stiamo affrontando una conversazione importante. Non interromperci per favore.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città6"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = "Soldato"
            if x == GlobalHWVar.gpx * 16:
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoAlloggiProfughi"]:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Chiedo scusa soldato, è possibile entrare negli alloggi?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non è concesso l'accesso a quest'ora!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Va bene... sto cercando un ragazzo che ha più o meno la mia età e...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Gli alloggi sono vuoti al momento. Vengono sgomberati tutte le mattine, se hai bisogno ripassa stasera e te ne verrà assegnato uno.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"No, non ho bisogno di un alloggio. Sto cercando un ragazzo di nome Hans, è mio...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"È vietato fornire informazioni sui residenti. I registri sono già stati prelevati e non è permesso consultarli per scopi di interesse privato.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Cosa?... Volevo solo sapere se mio fratello...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"I registri sono già stati prelevati!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ok, ok...")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(È inutile parlare con questo soldato, continuerà a dirmi: \"<*>#italic#I registri sono stati prelevati!<*>\"...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Questo soldato non ha intenzione di dirmi niente.)")
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 19:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Salve, mi stavo chiedendo se fosse possibile entrare negli alloggi...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Entrare negli alloggi?... A quest'ora?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sì... non lo so, te lo sto chiedendo...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Me lo stai chiedendo?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Sì.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Sì?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Ehm... sì, ti sto chiedendo se posso entrare negli alloggi... adesso...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Adesso?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Sì, adesso. È possibile?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Ehm... sì.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sì?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Sì?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ok, ok: <*>#bold#sì!<*> Però non riesco ad aprire, credo che sia chiuso a chiave...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Credi che sia chiuso a chiave?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sì, potresti aprirmi?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Potrei aprirti?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... La porta intendo...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"La porta?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Hai la chiave per aprire questa porta!?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Ehm... sì.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Perfetto! Allora puoi aprirmi la porta <*>#italic#per favore?<*>")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Ehm... non ho la chiave...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Cos-? Va bene, va bene. Chiedo al tuo collega!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Chiedi al mio collega?")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non ho intenzione di riaprire una conversazione con questo...)")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Questo soldato non mi sarà d'aiuto.)")
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ciao, hai per caso incontrato un ragazzo di nome Hans negli alloggi ieri notte?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Spiacente, non conosco nessuno con quel nome. A meno che non fosse nuovo e non l'abbia visto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, è nuovo. Dovrebbe essere arrivato ieri notte sul tardi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh... mi addormento abbastanza velocemente, ci sta che non l'abbia visto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mi sono addormentato abbastanza presto ieri notte, ci sta che il tuo Hans sia arrivato più tardi.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ciao, ragazzi. Vivete negli alloggi profughi voi due?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, quando c'è posto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Avete per caso incontrato un ragazzo di nome Hans ieri notte?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Hans? No, non c'era nessuno di nuovo ieri.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sicuro?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh... non al cento per cento... ma io non ho incontrato nessuno con quel nome.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non c'è nessuno negli alloggi che si chiami Hans.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa... perché continui a fare avanti e indietro?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa? Beh, perché... guarda quel soldato, non è irresistibile?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... No...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È così bello e sensibile! Devo andare a parlargli ma non so cosa dire...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Beh, vai e basta. Presentati e guarda cosa succede.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Va bene, vado! No, aspetta! Devo prima pensare a qualcosa da dirgli, sennò sembrerò una pazza sfigata.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ci sono! Vado! ... No, no... devo prepararmi qualcosa...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa crede di fare quella troietta!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Di che stai parlando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Di quella troietta bionda laggiù! Pensa di poterci provare col mio ragazzo! Lui è mio, le troiette come lei non si devono neanche azzardare a guardarlo.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa crede di fare quella troietta!?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città7"]:
        if tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Se vuoi posso aiutarti per... Sì?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ciao, siete degli studenti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, e... cosa state studiando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Hai bisogno di qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, è che non sono mai stata una studentessa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah. Beata te! Almeno ti eviti tutto questo inutile stress!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Stress? Studiare non è una cosa tranquilla? Cioè, te ne stai lì col tuo libro senza che nessuno ti dica niente...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, sarebbe bellissimo se nessuno ti dicesse niente... Purtroppo andare a scuola non significa semplicemente studiare. Significa apprendere più cose possibili in meno tempo possibile. Una specie di corsa contro il tempo per qualunque argomento ti venga assegnato, che ti piaccia o no.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh... ci sono dei limiti di tempo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ci sono dei programmi da rispettare e professori che si vogliono vantare con altri professori... Credimi, la scuola non è un bel posto in cui \"studiare\". Purtroppo però è anche l'unico per i ragazzi della mia età...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Beh, ha senso che ci siano dei programmi, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non quando si richiede di comprendere tutto il sapere di Platone o Aristotele in qualche giorno! A quel punto per poter tenere il passo ti limiti a leggere e ripetere, leggere e ripetere, finché non sei pronto per l'interrogazione. Non ti rimane tempo per riflettere o per approfondire gli argomenti. Devi seguire quello che ti dicono nei tempi che ti dicono. Come può essere piacevole o rilassante!?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh... quindi a nessuno piace studiare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Studiare è una cosa ben diversa da quello che si fa a scuola. Leggere e ripetere non vuol dire studiare!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, allora la domanda è: a nessuno piace la scuola?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Esatto. Cioè, alla maggior parte almeno... C'è chi ignora tutto questo e va avanti senza pensarci e chi invece è addirittura felice di eseguire gli ordini e soddisfare i professori. Ma non li biasimo, credono che sia quello il modo \"giusto\" di crescere. Chi sono io per dire che sbagliano...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E perché tu continui ad andarci allora?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perché altrimenti mio padre mi caccerebbe di casa. E non sono ancora pronto per avere una mia indipendenza. Un giorno magari mi metterò in proprio e farò qualcosa per conto mio... non vedo l'ora...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beata te che non devi andare a scuola!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Domani ho due interrogazioni... Ehm... ciao...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ciao. Cosa fate qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Stiamo andando a studiare. Nel nostro gruppo non c'è spazio per altre persone. E ora non abbiamo tempo da perdere, dobbiamo concentrarci per lo studio.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Avete un gruppo per studiare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, siamo solo noi due ma è già abbastanza così.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, ho capito...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Nel nostro gruppo non c'è spazio per altre persone. E ora non abbiamo tempo da perdere, dobbiamo concentrarci per lo studio.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città8"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = "Soldato"
            if x == GlobalHWVar.gpx * 9:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Salve soldato. Da quanto tempo sei qui?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Non disturbare i soldati in servizio, ragazzina!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Va bene, dimmelo pure quando disturbo e me ne vado.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Da quanto tempo sei qui?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Da stamani...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ok.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Vuoi sapere altro?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"No, solo quello.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Se non serve, evita di disturbare i soldati in servizio.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 12:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Chiedo scusa soldato, dovrei attraversare questa porta...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Chi sei?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Sono... Lucy.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... E perché devi passare?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Beh, perché... non lo so, volevo vedere cosa c'è dietro questa porta...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Volevo vedere il castello...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non è permesso l'accesso ai civili.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ah menomale. Non li sopporto quelli...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"<*>#italic#Ah ah.<*> Va bene, hai spirito. Mi dispiace ma non posso lasciarti passare.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non è permesso l'accesso ai civili.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 19:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Perché sorvegliate questa porta?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"È la porta del castello. Dobbiamo assicurarci che non ci siano accessi indesiderati.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"È il tuo castello?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... È il castello del Re.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"E perché sei tu a sorvegliarlo?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Il Re ha altro a cui pensare. Non può certo mettersi di guardia al suo castello.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... E a cosa deve pensare?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Cosa?! Chi credi che gestisca la città? Tutti i servizi, il controllo dei territori, le guardie che garantiscono la sicurazza in città...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Il Re gestisce tutto questo? E ha abbastanza soldi per mantenere tutti?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Certo, è supportato da tutto il popolo che lo segue e lo adora.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Perché il popolo dovrebbe \"supportare\" dei soldati che hanno il compito di non far entrare nel castello il popolo stesso? Voglio dire: è grazie al popolo se il Re può permettersi di mantenere un castello, quindi perché non dovrebbe essere accessibile a tutti?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Perché questo non è il castello di tutti, è il <*>#italic#suo<*> castello. E Sua Maestà sa cos'è meglio per il suo castello e per il suo popolo.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Beh, io so che sarei felice di entrare nel castello...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Vuoi mettere in discussione le decisioni del Re?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"No, no! Ho chiesto solo per cercare di avvicinarmi al suo sapere... Il mio intento era quello di comprenderlo non di offenderlo.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Bene!")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non ti è permesso entrare nel castello, se è quello che vuoi sapere.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Cos'hai da guardare?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Niente.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... E allora smettila di fissarmi!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Potrei avere anch'io un'armatura come la tua?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Eh... ? Sono armature fabbricate per la guardia cittadina. È vietato portarle se non ne fai parte.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Queste armature vengono fabbricate esclusivamente per la guardia cittadina. È vietato portarle se non ne fai parte.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Salve signore, sai per caso...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Aspetta solo un secondo... devo riuscire...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Forse da questa angolazione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Che stai facendo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*> No...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Stai guardando la torre?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Un po' più a destra...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Eh sì. È proprio una bella torre. Sarebbe un peccato perdersi la sua magnificienza anche solo per un attimo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Eh?! Lo credi anche tu?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Certo. Soprattutto la punta. È qualcosa di incredibile!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Vero! Gli architetti hanno pensato a qualcosa di veramente geniale per la parte più alta!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sarebbe proprio un peccato se qualcuno non potesse vederla.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Già, proprio per quello l'hanno messa in alto. Così tutti possono vederla.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È vero. Hanno pensato proprio a tutto... e a <*>#italic#tutti.<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Gli architetti hanno pensato a qualcosa di veramente geniale per la parte più alta!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Che state cercando di fare con quella scala?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Proprio un bel niente! Dei calabroni hanno fatto il nido sul tetto e la scala è troppo bassa per arrivarci.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E non potete lasciarli stare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo che no! Ogni volta che apro la finestra, me li ritrovo in casa che svolazzano facendo un rumore terrificante.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Tieni le finestre chiuse, allora.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah, certo. Eccola la soluzione! Come avevo fatto a non pensarci!? Ti ringrazio davvero molto!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Va bene, scusa. Volevo essere d'aiuto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ogni volta che apro la finestra, mi ritrovo in casa quei calabroni che svolazzano in giro facendo un rumore terrificante.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Serve una mano con quella scala?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, credo che lasceremo perdere. È troppo corta per arrivare al tetto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sicuro? Secondo me con un piccolo salto alla fine... cioè, non manca molto per arrivare...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Un piccolo salto? Vuoi provare te?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, no... era solo un'idea...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Questa maledetta scala è troppo corta per arrivare al tetto. Potremmo provare a rialzarla... ma con cosa?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quei due sono le persone più impacciate che abbia mai visto!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché li stai guardando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mi godo lo spettacolo. Prima o poi proveranno qualcosa di folle per salire sul tetto! <*>#italic#Hahaha...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché non vai ad aiutarli anziché stare qui a deriderli?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehi, non è mica il tetto di casa mia quello! Poi quel tipo con i capelli biondi sembra sul punto di esplodere da un momento all'altro. Non me lo voglio perdere!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quel tipo sembra sul punto di esplodere da un momento all'altro. Non me lo voglio perdere per niente al mondo!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città9"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = "Soldato"
            if x == GlobalHWVar.gpx * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Questa uscita dove porta?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Beh, essendo un'uscita, porta esattamente fuori dalla città.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Intendevo dire: dove porta questa questa strada?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Certo, <*>#italic#hahaha...<*> Procedendo verso sud arrivi alla Selva Arida.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Procedendo verso sud arrivi alla Selva Arida.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ehi soldato...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Serve aiuto?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"No. Che stai facendo?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Sono in servizio...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Oh... e in che servizio sei?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Cosa!? Sono in servizio... sono di guardia all'uscita sud. Non disturbare i soldati se non necessiti di aiuto.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Va bene, scusa.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non disturbare i soldati se non necessiti di aiuto.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehi, ragazza. Sei venuta a fregarmi la frutta migliore?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cosa? No, stavo solo passando di qui...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Hahaha...<*> Non preoccuparti stavo scherzando. In pochi lo sanno ma qua c'è la frutta migliore di tutto il mercato.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh. E tu come lo hai saputo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ho guardato. Gli altri vanno sempre dall'altra parte e pensano di dover arrivare prima per avere le cose migliori. In realtà basta venire qui e hai tutta la roba migliore in qualunque momento.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E in cosa questa frutta è meglio dell'altra?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quando le persone scelgono le cose, le toccano, le stringono e le rimettono sulla bancarella. In questo modo la frutta si rovina. Ma qui non viene nessuno a rovinare queste belle mele. È un bel vantaggio, eh?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Certo...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Qua non viene nessuno a rovinare queste belle mele. È un bel vantaggio, eh?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città10"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = "Soldato"
            if y == GlobalHWVar.gpy * 7:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Dove porta questa strada?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Al Passo Montano. Non troverai niente di buono là.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"È distante da qui?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non dovresti avventurarti da quelle parti. È pieno di bestie alate che ti piombano addosso a velocità estremamente elevate per attaccarti coi loro affilatissimi artigli. Senza una dovuta preparazione, è morte certa.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"È anche più pericoloso della Foresta Cadetta?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"<*>#italic#Tsk!<*> La foresta è uno scherzo a confronto. È il posto peggiore in cui qualcuno possa andare.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Il Passo Montano è il posto più pericoloso in cui un essere umano possa andare.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 11:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Ragazza! Ti sconsiglio vivamente di proseguire per questa strada.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Perché?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non è sicuro. Nonostante siano state fatte diverse spedizioni, il territorio è ancora largamente inesplorato e quel poco che è conosciuto è abbastanza per convincerci di non indagare oltre.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Non avventurarti nel Passo Montano. Quel territorio non è sicuro.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Stai cercando qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, sono rimasto chiuso fuori di casa. Devo aspettare che mia madre torni.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Tua madre?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, ha preso lei le chiavi. Aveva detto che sarebbe rimasta a casa, invece ha pensato bene di uscire senza dirmi niente.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Magari è in casa ma non ti sente perché sta facendo... qualcosa di rumoroso...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, è sicuramente andata al mercato. Ci va sempre anche quando non gli serve niente.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Uff!<*> Ma quando arriva!?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = "Sconosciuta"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*> queste case hanno qualcosa che non va...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Parli dei muri storti che convergono verso l'alto?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dei muri che <*>#italic#sembrano<*> storti! Credo si tratti della prospettiva...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dici? A me sembrano ugualmente storti da qualunque prospettiva...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Queste case hanno qualcosa che non va...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
