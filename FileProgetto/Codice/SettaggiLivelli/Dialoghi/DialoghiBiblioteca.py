# -*- coding: utf-8 -*-

import random
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
    if tipo == "AssistBiblioteca" or tipo == "OggettoAssistBiblioteca":
        partiDialogo = []
        nome = "Assistente bibliotecario"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosse300Monete"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ehi, tu! Devi fornire un documento per entrare!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Eh...? Io non ho nessun documento...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mi serve per certificare la t... Non puoi non averlo. Ne viene assegnato uno a tutti quando entrano in città. L'hai perso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, non mi hanno dato nessun documento quando sono arrivata. Chi me lo avrebbe dovuto dare?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se non sei residente, ti viene assegnato un certificato di permanenza quando arrivi agli alloggi profughi. Era in mezzo agli altri fogli che hai ricevuto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Oh, perfetto... quando sono arrivata mi è stato detto che non c'era più posto negli alloggi. Quindi David, il comandante della guardia notturna, si è offerto di ospitarmi per la notte.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Addirittura... ospitata da David? Beh, allora chiedi a lui di rilasciarti la certificazione. Altrimenti non posso lasciarti passare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene, ma in realtà avrei soltanto bisogno di sapere se mio fratello è passato di qua oggi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non posso darti questo genere di informazioni. Gli accessi alla biblioteca vengono inseriti in dei registri che solo il bibliotecario può consultare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ah... allora posso chiedere al bibliotecario?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, certo. Ma non sarò certo io a disturbarlo. Lui... non ha molta pazienza per queste cose...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E come...? Posso passare solo per parlare con lui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mi spiace, devi per forza avere un documeto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E va bene...")
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ehi! Devi fornire un documento per entrare!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene, va bene. Lo richiederò a David.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Ecco il certificato...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto. Ti do la benvenuta nella biblioteca. Al piano terra troverai tutti gli scritti riguardanti...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Salve, sai dirmi dove posso trovare il bibliotecario?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Senti, ragazzina! È consuetudine esporre l'organizzazione dei reparti ai nuovi arrivati! Prima di fare le tue domande dovresti almeno avere la cortesia di rispettare e ascoltare chi hai di fronte!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mi stai ascoltando!?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Sì, ma... io ho bisogno di parlare col bibliotecario...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Come ti pare! È al primo piano ma di sicuro non vorrà essere diturbato.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa, dove hai detto che si trova il bibliotecario?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Primo piano.")
            partiDialogo.append(dialogo)
    if tipo == "Bibliotecario":
        partiDialogo = []
        nome = u"René"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa, sei tu il bibliotecario?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, adesso sono molto occupato quindi, per cortesia...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Volevo sapere se mio fratello fosse passato di qui oggi... è un po' più alto di me e ha...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Fermati, fermati! Non ho tempo per queste cose adesso! Prendi un appuntamento e ripassa più tardi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Aveva i capelli neri e si chiamava... si chiamava... si chiama...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Si chiama Hans...")
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
            dialogo.append(u"... Smettila di fissarmi! Ti ho detto di ripassare più tardi, ho da fare adesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Io...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Io ho...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Cosa!? Cos'hai?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... I-io ho...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Uff... Ok, mi sembri abbastanza sconvolta. Vieni, ti faccio controllare i registri così poi te ne vai...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Eccoci. Questo è il mio studio. Non toccare niente per favore.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioArrivoNelloStudio"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Allora, il registro di stamani... ecco!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Io...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoRegistroBibliotecaSullaScrivania"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ok, vediamo... Chi stavi cercando?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Io ho...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPreVomito1"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... I-io...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Che hai...?")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Oddio...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Ok...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Non... non preoccuparti. Ci penso io a pulire... tu siediti un attimo e riprenditi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... O-ok...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Uff! Perché non viene via? ...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripulitoVomito"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Va beh, non importa...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioVenutoVersoDiTe"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusami, non volevo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non preoccuparti. Ti senti meglio ora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Perché sei così sconvolta? Che ti è successo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... N-niente...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mh, ok... come ti chiami ragazza?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Lucy...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Lucy, sei in pericolo per qualcosa? Hai problemi famigliari o economici?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Va bene... Senti, sei ancora giovane e ogni problema ti può sembrare la fine del mondo. Da piccoli tendiamo ad ingigantire i problemi fino a farli diventare dei drammi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma esiste un modo per tranquillizzarsi e superarli, qualunque sia il problema, grande o piccolo che sia. Ovvero: rivolgersi alla scienza e alla ragione.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Certo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Davvero. Tu adesso sei sconvolta perché ti è successo qualcosa di... sconvolgente, immagino. Bene: è successo un evento che adesso ti sta provocando disturbi e problemi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma di per se un evento è solo un evento, un momento nel tempo in cui qualcosa accade. Nel mondo succedono un sacco di eventi e non c'è nessun problema in questo. I \"problemi\" non derivano dagli eventi, ma dai soggetti che li percepiscono.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mh...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mi spiego meglio: se tu non avessi visto l'evento che ti ha sconvolta, adesso non avresti il problema che ti sta affliggendo, giusto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Beh, se non mi fosse successo... no, starei bene.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto. Quindi se l'evento accade ma non ne sei a conoscenza, non ne può derivare un problema. Ma adesso siamo nel caso opposto, ossia: hai percepito l'evento e ti ha scaturito un problema, ok?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Quindi la domanda da porsi è: perché la percezione di un evento ti può provocare un problema?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La prima risposta che viene in mente è: perché non volevi che quell'evento accadesse. Ma non è la risposta corretta. In realtà ciò che ti attanaglia è il rimpianto di non aver agito diversamente. Hai fatto qualcosa di sbagliato quando potevi scegliere di compiere un'azione \"giusta\".")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma a questo punto interviene la scienza. Dimmi Lucy, se potessi tornare indietro nel tempo ma senza ricordare cosa è successo dopo aver preso la tua scelta \"sbagliata\", cosa faresti?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Senza ricordare?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, intendo tornare indietro nel tempo anche con i ricordi. In questo caso esisterebbe la possibilità per te di prendere una decisione diversa da quella che hai preso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Beh, sì. Anche se non so cosa sarebbe successo, ci sarebbero state comunque infinite possibilità, no?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questo è quello che tutti normalmente pensano. Ma prova a prendere in considerazione un evento alla volta: torni indietro nel tempo e sei nel momento immediatamente prima a quello in cui prendi la decisione \"sbagliata\". Ogni cosa è identica a com'era e tu stai pensando esattamente a quello che pensavi in quel momento... Dimmi, è possibile che tu possa fare qualcosa di diverso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Beh... tutto quello che ho fatto e pensato sono la causa della mia decisione...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto! Sono la <*>#italic#causa<*>. Ed è assurdo pensare che da un dato evento possano scaturire effetti diversi e contrastanti.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Eh?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sarebbe come pensare che se lascio cadere una palla, questa a volte vada verso l'alto, a volte verso il basso e a volte a sinistra o a destra. È totalmente illogico!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Mi sono persa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"No, hai capito, è molto semplice. Seguimi, te lo dimostro con un semplice esperimento.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Eccomi, ehm... bibliotecario.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Bibliotecario? Chiamami René, per favore. Vediamo... ah, ecco fatto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Allora, volendo sintetizzare in una frase quello che abbiamo detto prima, potrei dire: se l'evento evento <*>#italic#E2<*> avviene a causa dell'evento <*>#italic#E1<*>, non è possibile che dall'evento <*>#italic#E1<*> siano causati eventi diversi da <*>#italic#E2<*>. In pratica stiamo dicendo che non si può cambiare un evento passato...  piuttosto banale...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma se l'evento <*>#italic#E1<*> si dovesse ripetere in futuro, io saprei che successivamente avverrà <*>#italic#E2<*>. Mi segui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Più o meno...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ok. Te lo spiego con un piccolo esperimento: su questo tavolo inclinato è incastonata una molla che permette di spingere delle palline lungo questo piccolo canale. Quelle linee disegnate sul tavolo servono per segnare la distanza dalla molla.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se io adesso spingessi una palla caricando la molla circa a metà...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La palla è arrivata fino alla quinta linea. Mettiamo che il momento in cui abbiamo caricato la molla è il nostro momento <*>#italic#E1<*>, mentre il momento in cui la palla si ferma è il momento <*>#italic#E2<*>. Ti faccio questa domanda: se ripeto l'esperimento allo stesso modo, fino a dove pensi che arriverà la palla prima di fermarsi e tornare indietro?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sempre alla quinta linea, direi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto. In altre parole mi stai dicendo che dall'evento <*>#italic#E1<*> scaturirà inevitabilmente <*>#italic#E2<*>. È tanto ovvio quanto incredibile: sei appena riuscita a prevedere un evento futuro!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Partendo da questo presupposto, sono stati fatti diversi studi che permettono di prevedere molti tipi di eventi diversi tramite delle formule matematiche. Questa è una situazione molto semplice da prevedere e da calcolare. Semplicemente mostrandoti i passaggi potresti calcolarla anche tu adesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mh...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non ci credi? Prova! Ti scrivo qua i passaggi e i dati di partenza. Tu prova a calcolare quanto spazio percorre la pallina prima di tornare indietro.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["scrittiDatiEnigmaBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se hai difficoltà a comprendere qualcosa, puoi consultare i libri su quella libreria. Trovi delle semplici spiegazioni nella sezione \"Moto rettilineo uniformemente accelerato\".")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = random.randint(1, 4)
            velPalla = GlobalGameVar.datiEnigmaBibliotecario["velocità"]
            soluzione = GlobalGameVar.datiEnigmaBibliotecario["soluzione"]
            vettoreRisposteFalse = [GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"], GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"], GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"]]

            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("???DOMANDA???")
            dialogo.append(u"Dimmi, quanto spazio percorre la pallina prima di fermarsi se la faccio partire con una velocità di " + str(velPalla) + u" m/s?")
            i = 1
            while i <= 4:
                if i == scelta:
                    dialogo.append(str(soluzione))
                else:
                    dialogo.append(str(vettoreRisposteFalse.pop(0)))
                i += 1
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("!!!RISPOSTA!!!")
            i = 1
            while i <= 4:
                if i == scelta:
                    dialogo.append("Esatto")
                else:
                    dialogo.append("Sbagliato")
                i += 1
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
