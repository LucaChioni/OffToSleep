# -*- coding: utf-8 -*-

import random
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
            dialogo.append(u"... Sei tu il bibliotecario?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, adesso sono molto occupato quindi, per cortesia...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Volevo sapere se mio fratello fosse passato di qui oggi... era un po' più alto di me e aveva...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Fermati, fermati! Non ho tempo per queste cose adesso! Prendi un appuntamento e ripassa più tardi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Aveva i capelli neri e si chiamava... si chiama... si chiama...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Hans...")
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
            dialogo.append(u"... ?")
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
            dialogo.append(u"... <*>#italic#Uff...<*> Ok, mi sembri abbastanza sconvolta. Seguimi, ti faccio controllare i registri...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
            nome = "Bibliotecario"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questo è il mio studio. Non toccare niente per favore.")
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
            dialogo.append(u"... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... I-io...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Che hai?")
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
            dialogo.append(u"... Perché non viene via!?")
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
            dialogo.append(u"<*>#italic#Mh,<*> ok... come ti chiami ragazza?")
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
            dialogo.append(u"Va bene... Senti, qualunque sia il tuo problema, lo puoi risolvere molto semplicemente con la scienza e la ragione. Mi spiego subito: tu adesso sei sconvolta perché hai assistito ad un evento... sconvolgente, immagino. Ma di per se un evento è solo un momento nel tempo in cui qualcosa accade. I \"problemi\" non derivano dagli eventi, ma dai soggetti che li percepiscono.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì... Certo, certo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"So che sembra una stupidaggine ma lasciami finire.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mh.<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Quando un evento accade ma non lo si percepisce, non può far emergere un problema. Quindi bisogna chiedersi che cos'è che provoca disturbo nell'osservare un evento. Sei d'accordo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Certo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ciò che crea fastidio è il rimpianto di non aver agito diversamente. Di aver fatto qualcosa di \"sbagliato\" quando potevi scegliere di compiere un'azione \"giusta\".")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma è qui che deve intervenire la ragione. Dimmi Lucy, se potessi tornare indietro nel tempo ma senza ricordare quello che è successo dopo aver preso la tua scelta \"sbagliata\", cosa faresti?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ma di che stai parlando?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Di carriole, Lucy... Ascolta, mi hai appena vomitato sul paviento e io sto cercando di aiutarti, puoi almeno seguire il ragionamento? Non ci vorrà molto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, ok... tornare indietro senza ricordare quello che è successo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, intendo tornare indietro nel tempo anche con i ricordi. In questo caso, esisterebbe la possibilità per te di prendere una decisione diversa da quella che hai preso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Beh, sì. Anche se non so cosa sarebbe successo, ci sarebbero state comunque infinite possibilità, no?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questo è quello che tutti normalmente pensano. Ma prova a considerare un evento alla volta: torni indietro nel tempo e sei nel momento immediatamente prima a quello in cui prendi la decisione \"sbagliata\". Ogni cosa è identica a com'era e tu stai pensando esattamente a quello che pensavi in quel momento... Dimmi, è possibile che tu faccia qualcosa di diverso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Beh... tutto quello che ho fatto e pensato sono la causa della mia decisione...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto! Sono la <*>#italic#causa.<*> Ed è assurdo pensare che da un dato evento possano scaturire effetti diversi e contrastanti.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Eh?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sarebbe come pensare che, se lasciassi cadere una palla, questa andrebbe a volte verso l'alto, a volte verso il basso e a volte a sinistra o a destra. È totalmente illogico!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mi sono persa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"No, non è difficile. Seguimi, te lo dimostro con un semplice esperimento.")
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
            dialogo.append(u"Chiamami René, per favore... Vediamo... ah, ecco fatto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Allora, volendo sintetizzare in una frase quello che abbiamo detto prima, potrei dire: se l'evento evento <*>#italic#E2<*> avviene a causa dell'evento <*>#italic#E1,<*> non è possibile che dall'evento <*>#italic#E1<*> siano causati eventi diversi da <*>#italic#E2.<*> In pratica stiamo dicendo che non si può cambiare un evento passato...  piuttosto banale...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma se l'evento <*>#italic#E1<*> si dovesse ripetere in futuro, io saprei che successivamente avverrà <*>#italic#E2.<*> Mi segui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Più o meno...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ok, te lo spiego con un piccolo esperimento. Su questo tavolo inclinato è incastonata una molla che permette di spingere una palla lungo questo piccolo canale. Quelle linee disegnate sul tavolo servono per segnare la distanza dalla molla.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se io adesso spingessi la palla caricando un po' la molla...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La palla è arrivata fino alla linea che segna un metro. Mettiamo che il momento in cui abbiamo caricato la molla è il nostro momento <*>#italic#E1,<*> mentre il momento in cui la palla si ferma prima di tornare indietro è il momento <*>#italic#E2.<*> Se adesso ripetessi l'esperimento allo stesso modo, fino a dove pensi che arriverebbe la palla prima di fermarsi e tornare indietro?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sempre a un metro, direi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto. In altre parole mi stai dicendo che dall'evento <*>#italic#E1<*> scaturirà inevitabilmente <*>#italic#E2.<*> Ebbene, sei appena riuscita a prevedere l'evento che sta per accadere...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Partendo da questo presupposto, sono stati fatti diversi studi che permettono di prevedere molti tipi di eventi tramite delle formule matematiche. Questa è una situazione molto facile da prevedere e da calcolare. Semplicemente mostrandoti i passaggi potresti calcolarla anche tu adesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mh...<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non scherzo, prova! Ti scrivo qua i passaggi e i dati di partenza. Tu prova a calcolare quanto spazio percorre la palla prima di tornare indietro se parte con una velocità di 3 m/s.")
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
            if GlobalGameVar.datiEnigmaBibliotecario["velocità"] < 5:
                velProssimaPalla = GlobalGameVar.datiEnigmaBibliotecario["velocità"] + 1
            else:
                velProssimaPalla = 1
            soluzione = GlobalGameVar.datiEnigmaBibliotecario["soluzione"]
            vettoreRisposteFalse = [GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"], GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"], GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"]]

            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("???DOMANDA???")
            dialogo.append(u"Dimmi, quanto spazio percorre la palla prima di fermarsi se la faccio partire con una velocità di " + str(velPalla) + u" m/s?")
            i = 1
            while i <= 4:
                if i == scelta:
                    dialogo.append(str(soluzione) + " m.")
                else:
                    dialogo.append(str(vettoreRisposteFalse.pop(0)) + " m.")
                i += 1
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("!!!RISPOSTA!!!")
            i = 1
            while i <= 4:
                if i == scelta:
                    dialogo.append("Seguendo i calcoli, esattamente " + str(soluzione) + " m. E questo risultato corrisponde ad un evento non ancora avvenuto...")
                else:
                    dialogo.append(u"<*>#italic#Mmh...<*> no, devi aver sbagliato dei calcoli. Riprova con una velocità di " + str(velProssimaPalla) + " m/s. La risposta giusta era " + str(soluzione) + " m, ti faccio vedere.")
                i += 1
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitaVerificaRisultatoEnigma"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Quello che abbiamo appena fatto dimostra una cosa molto importante: la materia che compone la realtà segue delle regole ben precise. Ora, se con \"materia\" intendiamo tutto ciò che è percepibile, esiste una ragione per cui gli esseri viventi, essendo anch'essi percepibili e fatti di materia, non dovrebbero seguire le stesse regole?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Beh, un essere vivente può fare qualcosa. Può pensare, prendere decisioni... Ha qualcosa in più rispetto alla materia normale. Qualcosa che lo rende \"vivente\".")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Tipo un'anima.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, tipo... qualcosa del genere...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Certo, ha senso ma il ragionamento non cambia. È possibile che esista \"un'anima\" non materiale. Però il modo in cui questa si evolve e interagisce con la realtà è determinato da specifiche regole.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Nonostante non sia possibile dimostrarlo, ciò che lo fa sembrare ovvio è che gli umani sono in grado di spiegare il motivo delle loro azioni. E, se ci sono dei motivi, vuol dire che, anche potendo tornare indietro nel tempo, l'azione compiuta sarebbe sempre la stessa. Ossia quella che il soggetto reputava migliore per la situazione.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mh...<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Qualunque cosa tu abbia fatto o detto nella tua vita, non è per colpa o merito tuo. Semplicemente succedono degli eventi che ti impongono delle reazioni. Prima, ad esempio, eri scossa per qualcosa. Ma punirti per quello che hai fatto, sarebbe come punire questa palla perché qualcuno pensa che si ferma troppo presto o troppo tardi prima di tornare indietro. Se le condizioni di partenza sono le stesse, i risultati non cambieranno.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Vuol dire che nessuno è responsabile di quello che fa... perché una persona dovrebbe impegnarsi a fare qualcosa? Cioè, se non esiste la possibilità di prendere decisioni, il futuro è invariabile... statico come il passato... non ci sarebbe motivo di... cioè...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, infatti. Per questo è comodo che le persone pensino di avere libero arbitrio. Le porta ad impegnarsi per degli obiettivi, a dare importanza alle loro azioni, a responsabilizzarsi, a seguire le regole. Le rende punibili quando \"sbagliano\", cosicché si pentano e si evolvano secondo la visione che gli si vuole imporre. Le porta ad obbedire. Se così non fosse, sarebbe un problema organizzare delle società...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Beh, e tu? Pur sapendo queste cose non crei problemi, no?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Io sono consapevole e agisco di conseguenza. Mi metto comodo, continuo i miei studi e osservo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, non hai risposto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Vuoi sentire qualcosa che ti faccia sentire meno in colpa per quello che hai fatto prima di venire qui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Tu sai... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Beh, considerando la chiazza di vomito, sicuramente non hai fatto una passeggiata tranquilla...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Io... ho ucciso due persone...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Due persone che mi volevano stuprare... poi sono scappata...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Ok... ti hanno vista?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, non credo. Qualcuno avrebbe urlato...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Va bene... ma perché non sei fuggita dalla città anziché venire qui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Per... mio fratello. È scappato di casa ieri notte. Da un po' di tempo diceva di voler venire in città, quindi l'ho seguito. Ho chiesto in giro e mi è stato detto che potrebbe essere stato qui.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Va bene. Giusto per chiarire: se salta fuori qualcosa, io non sapevo niente.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto. Comunque, se tuo fratello è stato qui lo vedremo subito dai registri...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConclusivoEnigmaBibliotecario"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Il registro di stamani è sulla mia scrivania. Se mi fai passare, vado a controllare.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioArrivatoAlRegistro"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Il nome?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Hans.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Hans... no... non c'è nessun Hans qui. Potrebbe essersi presentato con un nome diverso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non credo... perché avrebbe dovuto... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Tuo fratello è scappato di casa senza dire niente, non credo che voglia essere seguito. La cosa migliore sarebbe lascialo andare per la sua strada. Magari un giorno vi rincontrerete.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, ma è da solo... se si trovasse in difficoltà o in pericolo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Tu ti sei trovata in pericolo. Sei tu che non dovresti stare da sola.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Sai a chi altro potrei chiedere?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Come vuoi... In effetti qualcuno c'è. E mi faresti anche un bel favore se ci andassi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Chi?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Devo fare una consegna ad un mio vecchio amico. Vive a sud oltre la Selva Arida. Si chiama Neil, è una persona molto potente che ha notizia di tutti gli spostamenti che avvengono in questo territorio. Da quello che ho capito, è possibile che tuo fratello non sia in questa città, quindi se c'è una persona a cui dovresti chiedere è senza dubbio Neil.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E lui vorrà aiutarmi?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sarà molto felice di ricevere ciò che gli consegnerai. Se sarà di buon umore e ti dimostrerai una persona valida, non ci saranno problemi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mh...<*> Cosa dovrei consegnare?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ti faccio vedere...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoACercareImpo"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... L'avevo messo qua da qualche parte...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricercaImpoDiBibliotecario1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Era qui...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Ah! Trovato.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
            oggettoDato = "PietraImpo"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ecco qui.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Cos'è?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questa è un'antica creatura delle montagne occidentali. Appartiene ad una specie che si è estinta da molto tempo. Ma sono riuscito a conservarne un esemplare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ma... è vivo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, certo. Queste bestie sono praticamente immortali. Sono in grado di \"congelarsi\" per moltissimi anni finché non trovano nutrimento.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ah, ok. E come hanno fatto ad estinguersi allora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questa è una bella domanda. Sono spariti tutti in una notte di circa cinquant'anni fa. Di colpo non se ne sono più visti in giro. Un episodio piuttosto strano che molti videro come naturale conseguenza dell'inaridimento della selva e della putrefazione del lago avvenuti qualche anno prima. In realtà questa fu una delle poche specie a non soffrire per niente di quei disastri...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Per questo diversi studiosi non accettarono quelle motivazioni ed iniziarono delle ricerche autonome per saperne di più. Io ero tra loro. Sono partito alla ricerca di spiegazioni verso ovest e sono riuscito a trovare questo piccolo impo incastrato in una roccia. Così l'ho preso e ho iniziato a studiarlo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Impo? Si chiama così?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, è il nome della specie. Gli è stato dato dal loro scopritore perché molti esemplari portavano una specie di incisione sulla pelle che formava quella scritta... Molto bizzarro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un'incisione sulla pelle che dice \"Impo\"... ?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto. Comunque, io l'ho osservato abbastanza e non saprei cos'altro ricavarne. Neil era molto appassionato di queste creature, se glielo lasciassi studiare potrebbe dedurne qualcosa che a me è sfuggito.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene. Ma come lo trasporto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non devi trasportarlo. Ti seguirà se attivi questa pietra...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoDalBibliotecario"]:
            oggettoDato = "ImpoFrutto piccolo"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Si è svegliato?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, l'ho appena alimentato ma non ti preoccupare, non è aggressivo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok. Quindi adesso mi seguirà?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Segue sempre la pietra che ti ho dato quando è attiva. Ma ciò che rende veramente interessante questa creatura è il suo comportamento quando la pietra è spenta.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Adesso è spenta e non sta facendo niente...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Gli impo sono degli animali molto metodici. Svolgono diverse attività che ritengono assolutamente prioritarie rispetto a tutto il resto, anche rispetto alla loro stessa vita. Lo fanno finché non esauriscono le energie, a quel punto di fermano e aspettano il nutrimento. Adesso, sembrerà strano, ma la priorità di questo impo è rimanere fermo. E ci resterà finché qualcuno non gli dirà di fare qualcos'altro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Cioè possiamo dirgli cosa fare?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esattamente. Puoi dirgli che azione compiere in quale situazione e lui la eseguirà ogni volta senza batter ciglio.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*> non ho mai sentito niente del genere. Possimo provare anche adesso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì ma non sente la tua voce. L'unico modo per comunicargli cosa fare è inserirgli degli ImpoFogli nell'apertura che ha dietro la testa. Queste aperture vengono chiamate \"celle di memoria\" e lui ne ha solo una al momento, quindi puoi fargli fare solo un'azione alla volta. Ma non preoccuparti, anche se sono molto rare, credo che ne troverai delle altre durante il viaggio.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok... e cos'è un \"ImpoFoglio\"?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"È una specie di foglio non molto spesso ma fatto di un materiale molto più rigido e resistente della carta normale. Tutti gli ImpoFogli sono diversi tra loro e si dividono in due categorie: \"Condizio-ImpoFogli\" che indicano una condizione e \"Azio-ImpoFogli\" che indicano un'azione da compiere.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Per dare un'istruzione ad un impo devi inserire un Condizio-ImpoFoglio e un Azio-ImpoFoglio nella cella di memoria. L'impo, ogni volta che deve decidere cosa fare, legge la condizione e l'azione nella cella e, se valuta di trovarsi nella situazione adatta, esegue l'istruzione.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, sembra abbastanza complicato.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non lo è. Se vuoi dare un'occhiata, in biblioteca ci sono diversi libri che parlano più dettagliatamente del loro funzionamento. Ma sono sicuro che imparearai in fretta facendo qualche prova. In totale io ho solo due ImpoFogli che potrai usare da subito. Ma anche di questi, seppure molto raramente, ne potrai trovare altri in giro fuori città.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E lui cosa potrebbe fare adesso con i tuoi ImpoFogli?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Beh, ti saranno sicuramente d'aiuto se incontrerai altri stupratori o bestie durante il tragitto. Questo Condizio-ImpoFoglio individua una situazione in cui qualcuno vuole aggredirti, mentre questo Azio-ImpoFoglio gli fa fare un attacco che folgora il bersaglio.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Wow!<*> Possiamo farglielo fare ora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"No, non in città e soprattutto non nel mio studio. Poi adesso devo tornare a lavoro. Lo potrai vedere direttamente sul campo quando ne avrai bisogno. Ti faciliterà il viaggio, la Selva Arida è una zona parecchio ostile per gli umani ma con un impo non avrai problemi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene. La Selva Arida si trova a sud, giusto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto. Dopo averla attraversata, procedi ancora verso sud costeggiando il lago e arriverai al castello di Neil.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok: selva e poi lago. Ti lascio al tuo lavoro adesso. Grazie mille per avermi aiutata.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non c'è di che. Ah, dimenticavo, prendi questo... è un ImpoFrutto, un frutto che nasce nelle montagne occidentali di cui si nutrono gli impo. Daglielo quando vedi che sta esaurendo le energie.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un \"ImpoFrutto\"? Sembra più un <*>#italic#ImpoSasso...<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Già... ne avevo altri ma non li trovo più... devo averli già usati... In ogni caso, buona fortuna per il viaggio ragazza.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa René, hai detto che ci sono dei libri in biblioteca che parlano di Impo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, li puoi trovare tutti nelle librerie al piano di sopra. Sono tutti colorari di nero, non puoi sbagliarti.")
            partiDialogo.append(dialogo)

    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca1"]:
        if tipo == "AssistBiblioteca" or tipo == "OggettoAssistBiblioteca":
            partiDialogo = []
            nome = "Assistente bibliotecario"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosse200Monete"]:
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
                dialogo.append(u"Eh? Io non ho nessun documento...")
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
                dialogo.append(u"E come... ? Posso passare solo per parlare con lui?")
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
                dialogo.append(u"... Sì ma... io ho bisogno di parlare col bibliotecario...")
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
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ho niente da chiedergli...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, lui è dall'altra perte di questi scaffali adesso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Che c'è?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Dall'altra parte?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Sì...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, ti ho detto che non sono io! Lui è dall'altra parte di questi scaffali.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
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
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Dovrebbe essere al piano di sopra al momento.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No... tutto bene?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Perché mi fissi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No... non sono io il bibliotecario...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
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
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca2"]:
        if tipo == "Ragazzo1":
            partiDialogo = []
            nome = "Sconosciuto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Che vuoi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Niente...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, non sono io!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No. È quel signore con la barba laggiù... tra le due colonne...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Quel signore...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, È quel signore un po' anziano laggiù...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non sono io... il bibliotecario...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sei tu il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
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
        elif tipo == "OggettoLibriImpo":
            partiDialogo = []
            nome = "Libro"
            if x == GlobalHWVar.gpx * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questo libro si intitola: \"Scopo degli impo\".")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Come già spiegato in precedenza, ciò che spinge gli impo ad agire è determinato dagli ImpoFogli. Tuttavia esistono due casi eccezionali in cui l'azione compiuta è dovuta ad altre ragioni...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il primo caso in cui gli ImpoFogli non vengono eseguiti si presenta quando la PietraImpo è attiva. A quel punto, l'impo proprietario della pietra, inizierà ad avvicinarsi ad essa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il secondo caso si presenta quando nessun ImpoFoglio può essere eseguito ma è stato soddisfatto un Condizio-ImpoFoglio in precedenza che ha un obiettivo che non è più nel campo visivo. In questo caso, l'impo memorizzerà la posizione in cui ha visto l'obiettivo e, se avrà abbastanza energia per eseguire l'Azio-ImpoFoglio, si muoverà in quella direzione finché non eseguirà l'azione o raggiungerà la posizione...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questo libro si intitola: \"Sacche Energetiche\".")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... L'energia degli impo viene conservata in delle sacche dette \"Sacche Energetiche\"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Queste sacche, a seconda della dimensione, possono contenere più o meno energia...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... In uno degli ultimi studi, si è scoperto che le Sacche Energetiche sono responsabili anche dell'efficienza del sistema difensivo: alcune sacche permettono di resistere alle aggressioni spendendo meno energia...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questo libro si intitola: \"Gestione dell'ImpoForza\".")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... L'energia degli impo, detta anche \"ImpoForza\", può essere gestita solo in parte dagli umani...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Gli impo hanno infatti un'istinto di sopravvivenza che permette loro di difendersi dagli attacchi nemici sfruttando la propria energia. Più è violenta l'aggressione, più energia verrà consumata...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Anche se relativamente poco influente, questo loro comportamento non può essere alterato da agenti esterni...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 25:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Questo libro si intitola: \"ImpoMalus\".")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Gli impo soffrono negli ambienti troppo caldi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Quando un impo supera la propria temperatura massima inizia a perdere energia...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Gli impo sono in grado di tornare autonomamente alle loro temperature ideali. Ma per farlo rallentano i propri movimenti per un po' di tempo...")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"]:
        if tipo == "OggettoLibreriaStudioBibliotecario":
            partiDialogo = []
            nome = "Libro"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ci sono un sacco di libri...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Allora, ha detto di vedere il \"Moto rettilineo uniformemente accelerato\"... Oh, trovato! Vediamo se c'è una spiegazione comprensibile...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"In questa lezione inizieremo a trattare il modello del moto uniformemente accelerato... <br> Un \"moto rettilineo uniformemente accelerato\" è un tipo di moto in cui un corpo si muove lungo una linea retta con accelerazione costante.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Le formule che si usano per calcolare gli esiti di questi tipi di moto vengono chiamate \"leggi orarie del moto rettilineo uniformemente accelerato\" e sono principalmente due: <br> <*>#italic#Vf = Vi + AT<*> <br> <*>#italic#S = Vi×T + (1/2)×A×T²<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dove: <*>#italic#Vf<*> è la velocità del corpo (in metri al secondo) nell'evento finale; <*>#italic#Vi<*> è la velocità del corpo (in metri al secondo) nell'evento iniziale; <*>#italic#A<*> è l'accelerazione (in metri al secondo quadrato) che il corpo mantiene tra l'evento iniziale e l'evento finale; <*>#italic#T<*> è il tempo che passa (in secondi) tra l'evento iniziale e l'evento finale; <*>#italic#S<*> è lo spazio percorso dal corpo (in metri) tra l'evento iniziale e l'evento finale.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Osservazioni sulle formule del moto uniformemente accelerato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"La prima equazione determina qual è la relazione tra velocità, accelerazione e tempo: la differenza di velocità tra l'evento iniziale e quello finale dipende da quant'è l'accelerazione e per quanto tempo essa viene applicata. La seconda formula invece esprime la distanza percorsa da un corpo in un determinato lasso di tempo in cui viene impressa un'accelerazione costante.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Esempi sul moto rettilineo uniformemente accelerato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Vediamo se ce n'è uno simile alla mia situazione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Un carro di cavalli viaggia a 6 m/s. Se il carro rallenta con una decelerazione (accelerazione negativa) costante di 2 m/s², quanto spazio percorre prima di fermarsi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"La velocità iniziale del carro è: <*>#italic#Vi = 6 m/s.<*> <br> La velocità finale, dato che si deve fermare, è: <*>#italic#Vf = 0 m/s.<*> <br> L'accelerazione, dato che è contraria alla direzione del carro, è negativa: <*>#italic#A = -2 m/s².<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Prima di tutto, è necessario ricavare il tempo che impiega il carro per fermarsi. <br> Dalla relazione <*>#italic#Vf = Vi + A×T,<*> si ottiene: <*>#italic#T = (Vf - Vi) / A.<*> <br> Sostituendo con i dati che abbiamo: <*>#italic#T = (0 - 6) / (-2) = 3.<*> <br> Per fermarsi il carro impiega 3 secondi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ora che sappiamo quanto tempo serve per azzerare la velocità, possiamo calcolare quanta distanza percorre il carro prima di fermarsi tramite la relazione: <*>#italic#S = Vi×T + (1/2)×A×T².<*> <br> Ossia: <*>#italic#S = 6×3 + (1/2)×(-2)×3² = 9.<*> <br> Il carro si ferma dopo 9 metri.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> non so se ho capito tutto... ma, da quello che ho capito, basta sostituire i dati nelle formule e dovrebbe andare... credo...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi va di leggere altre spiegazioni di formule che non capisco...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoRegistroBiblioteca":
            partiDialogo = []
            nome = "OggettoRegistroBiblioteca"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmmh...<*> non capisco niente di come è organizzato. Meglio chiedere al bibliotecario.")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Hans non è stato segnato su questo registro.")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLibreriaRegistri":
            partiDialogo = []
            nome = "OggettoLibreriaRegistri"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sono i registri della biblioteca. Quello di oggi è sulla scrivania.")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoTavoloEnigmaBiblioteca":
            partiDialogo = []
            nome = "OggettoTavoloEnigmaBiblioteca"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario1"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ci sono dei fogli e una penna... Spero che non servano per \"l'esperimento\"...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi metterò a fare altri calcoli adesso.")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoMocio":
            partiDialogo = []
            nome = "OggettoMocio"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non è bastato per pulire...")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
