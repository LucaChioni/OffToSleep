# -*- coding: utf-8 -*-

import random
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizInterfaccia as LI


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
            nome = LI.BIBLIOTECARIO
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
            dialogo.append(u"Volevo sapere se mio fratello fosse passato di qui oggi... era un po' più alto di me e av-")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Fermati, fermati! Non ho tempo per queste cose adesso! Prendi un appuntamento e ripassa più tardi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Aveva i capelli neri e si chiamava... si chiama...")
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
            dialogo.append(u"...?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Io ho...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Cosa?! Cos'hai?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... I-io ho...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"<*>#italic#Porc-...<*> e va bene seguimi, ti faccio controllare i registri...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Questo è il mio studio. Non toccare niente per favore.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioArrivoNelloStudio"]:
            nome = LI.BIBLIOTECARIO
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
            nome = LI.BIBLIOTECARIO
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
            nome = LI.BIBLIOTECARIO
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
            dialogo.append(u"... Che hai?")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
            nome = LI.BIBLIOTECARIO
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
            dialogo.append(u"... Non... non preoccuparti. Ci penso io a pulire, tu siediti un attimo e riprenditi.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"O-ok...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Perché non viene via?")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripulitoVomito"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Va beh, non importa...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioVenutoVersoDiTe"]:
            nome = LI.BIBLIOTECARIO
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
            dialogo.append(u"Non preoccuparti, ti senti meglio ora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perché sei così sconvolta? Che ti è successo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... No, niente...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Va bene... come ti chiami ragazza?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Sara...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sara, sei in pericolo per qualcosa? Hai problemi famigliari, economici...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... No, non...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Ok. Seguimi... seguimi, ti faccio fare un piccolo esperimento.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Cosa...?")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Eccomi, uhm... bibliotecario.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì... chiamami René, per favore. Vediamo... ah, ecco fatto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Allora, concentrati e cerca di seguire questo piccolo ragionamento: se un evento, che chiameremo <*>#italic#E2,<*> è avvenuto (in passato) a causa dell'evento <*>#italic#E1,<*> è impossibile che dall'evento <*>#italic#E1<*> fossero causati eventi diversi da <*>#italic#E2.<*> In altre parole, un evento accaduto nel passato è determinato e invariabile... Ma se l'evento <*>#italic#E1<*> si dovesse ripetere in futuro, io saprei che successivamente avverrà <*>#italic#E2.<*> Mi segui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Più o meno...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Facciamo questo piccolo esperimento. Su questo tavolo inclinato è incastonata una molla che permette di spingere una palla lungo questo canale. Quelle linee disegnate sul tavolo servono per segnare la distanza dalla molla.")
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
            dialogo.append(u"La palla è arrivata fino alla linea che segna un metro. Mettiamo che il momento in cui abbiamo caricato la molla è il nostro evento <*>#italic#E1,<*> mentre il momento in cui la palla si ferma prima di tornare indietro è l'evento <*>#italic#E2.<*> Se adesso ripetessi l'esperimento allo stesso modo, fino a dove pensi che arriverebbe la palla prima di fermarsi e tornare indietro?")
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
            dialogo.append(u"Partendo da questo presupposto, sono stati fatti diversi studi che permettono di prevedere molti tipi di eventi tramite delle formule matematiche. Questa è una situazione molto facile da prevedere e da calcolare, semplicemente mostrandoti i passaggi potresti calcolarla anche tu adesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mh...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non sto scherzando! Ti scrivo qua i passaggi e i dati di partenza, tu prova a calcolare quanto spazio percorre la palla prima di tornare indietro se parte con una velocità di 3 m/s. Per i calcoli utilizza pure i fogli su questo tavolino.")
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
                    dialogo.append("Seguendo i calcoli, esattamente " + str(soluzione) + " m. E questo risultato corrisponde a un evento non ancora avvenuto...")
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
            dialogo.append(u"Beh... un essere vivente ha qualcosa in più rispetto alla materia normale. Può fare qualcosa. Può pensare, prendere decisioni... ha qualcosa che lo rende \"vivente\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Tipo un'anima?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, tipo... una cosa del genere...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Certo, può aver senso, ma il ragionamento non cambia. È possibile che esista \"un'anima\" non materiale, anche se molto improbabile, però il modo in cui questa si evolve e interagisce con la realtà è determinato da specifiche regole...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Nonostante non sia possibile dimostrarlo, ciò che lo fa sembrare ovvio è che gli umani sono in grado di spiegare il motivo delle loro azioni. E, se ci sono dei motivi, vuol dire che, anche potendo tornare indietro nel tempo, le azioni compiute sarebbero sempre le stesse.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Facciamo finta che sia possibile tornare indietro nel tempo. Torni a una sitazione in cui hai preso una scelta. Una scelta qualsiasi. Però facendolo, perdi anche i ricordi che hai accumulato nel tempo che stai riavvolgendo, d'accordo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok ma... devo immaginarmi una situazione specifica o...?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"No, non importa... va beh, facciamo che torni a una situazione che vorresti cambiare. Un episodio dove hai compiuto una scelta \"sbagliata\". Adesso hai l'occasione di tornare indietro e sistemare le cose. Però facendolo scorderai tutto quello che è successo dopo aver preso quella scelta.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene, torno indietro anche con i ricordi quindi...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDiPensareASceltaPassataNelDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmmh...<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Allora...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Una cosa qualunque...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, sto pensando. Non posso sprecare quest'occasione...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Non succederà veramente...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Aspetta, ci sono quasi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Va bene, ci sono!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ok. Mi raccomando, hai perso i ricordi che hai accumulato da quel momento fino ad adesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, sì. Ci sono.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto. Sei in quella situazione. Nel momento immediatamente prima a quello in cui prendi la tua decisione. Ogni cosa è identica a com'era, tu stai pensando esattamente a quello che pensavi in quel momento e non sai cosa succederà... Dimmi, è possibile che tu faccia qualcosa di diverso? Che tu agisca in maniera incoerente rispetto a quei processi mentali che ti hanno portata ad agire come hai agito la prima volta?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Avrei potuto... avrei potuto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Beh, se pensavo alle stesse cose... non so, tutto quello che ho fatto e pensato sono la causa della mia decisione, quindi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Esatto. Sono la <*>#italic#causa.<*> E sarebbe assurdo pensare che dalle medesime condizioni di partenza possano essere scaturiti effetti diversi tra loro!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sono la causa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non hai meriti o colpe di qualunque cosa tu abbia fatto, detto o pensato nella tua vita. Semplicemente succedono degli eventi che ti impongono delle reazioni. Punirti per cose che hai fatto o che ti sono successe, sarebbe come punire questa palla perché qualcuno pensa che si fermi troppo presto o troppo tardi prima di tornare indietro. Se le condizioni di partenza sono le stesse, i risultati non cambieranno.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["pensatoASceltaPassataNelDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ma aspetta... così però nessuno sarebbe responsabile delle proprie azioni... se ogni scelta dipende da quello che ci succede... non sono vere scelte. Perché dovrei impegnarmi a... cioè, non ci sarebbe motivo di... cioè...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, infatti. Per questo è comodo che le persone pensino di avere libero arbitrio. Le porta a impegnarsi per degli obiettivi, a dare importanza alle loro azioni, a responsabilizzarsi, a seguire le regole. Le rende punibili quando \"sbagliano\", cosicché si pentano e si evolvano secondo la visione che gli si vuole imporre. Le porta a obbedire. Se così non fosse, sarebbe un problema organizzare delle società.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Beh, e tu? Pur sapendo queste cose non sei un problema per la società, no?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Io accetto le convenzioni finché mi portano vantaggi. Per quanto mi riguarda, è molto meglio convivere con lavoratori stanchi che con organismi istintivi e bestiali, \"liberati\" dal loro arbitrio. Mi metto comodo, continuo i miei studi e osservo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, ma quindi... tu ti consideri un \"organismo istintivo e bestiale, liberato dal tuo arbitrio\"?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Beh... quando ci penso... ma finché non penso, o pensano gli altri, sono un individuo responsabile.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Ok... ma non mi sembri molto \"istintivo\" o \"bestiale\" ora che ci stai pensando...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sara... lo sono io e lo sei tu tanto quanto lo sono le api, le formiche e i castori quando costruiscono alveari, formicai e dighe... io posso costruire edifici, disegnare immagini e scrivere libri... questo dovrebbe rendermi \"non istintivo\"? Siamo una specie animale tra tante altre. La differenza tra naturale e artificiale serve solo a noi per innalzare il nostro lavoro, per renderlo più nobile, più importante...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Mh...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Comunque, a proposito di lavoro, dovrei tornare al mio adesso. Dicevi di essere venuta per sapere di tuo fratello...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Sì... sì, mio fratello! Volevo sapere se fosse passato di qui. È scappato di casa ieri notte. Da un po' di tempo diceva di voler venire in città, quindi l'ho seguito. Ho chiesto in giro e mi è stato detto di controllare in biblioteca...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se tuo fratello è passato di qui, lo vedremo subito dai registri...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripartitaMusicaDopoPensatoASceltaPassataNelDialogoBibliotecario"]:
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
            dialogo.append(u"Non credo... perché avrebbe dovuto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se n'è andato senza dire niente, non credo che volesse essere seguito... Non mi ostinerei troppo fossi in te. Magari un giorno vi rincontrerete.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì... sai a chi altro potrei chiedere?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Come vuoi... In effetti qualcuno c'è. E mi faresti anche un bel favore se ci andassi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Devo fare una consegna a un mio vecchio amico. Vive a sud oltre la Selva Arida. Si chiama Neil, è una persona molto potente che ha notizia di tutti gli spostamenti che avvengono in questo territorio. Da quello che ho capito, è possibile che tuo fratello non sia in città, quindi se c'è una persona a cui dovresti chiedere è senza dubbio Neil.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*> non penso se ne sia andato dalla città... rischio di perdere solo tempo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non sai nemmeno se ci è mai stato in città, magari è adesso che stai perdendo tempo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Uff...<*> e questo Neil vorrà aiutarmi?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Certo, sarà molto felice di ricevere ciò che gli consegnerai.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... E cosa dovrei consegnare?")
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
            oggettoDato = LI.IMPOPIETRA
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
            dialogo.append(u"Questa è un'antica creatura delle montagne occidentali. Appartiene a una specie che si è estinta da diversi anni ormai, ma sono riuscito a conservarne un esemplare.")
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
            dialogo.append(u"Ah... e come hanno fatto a estinguersi allora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questa è una bella domanda. Sono spariti tutti in una notte di circa dieci anni fa. Di colpo non se ne sono più visti in giro. Un episodio piuttosto strano che è stato ignorato da molti per via dei disastri avvenuti nella selva e nel lago qualche giorno dopo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Per questo solo pochi studiosi si interessarono alla questione. Ma io ero tra quelli. Sono partito alla ricerca di una qualche spiegazione verso ovest e sono riuscito a trovare questo piccolo impo incastrato in una roccia. Così l'ho preso e ho iniziato a studiarlo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Impo? Si chiama così?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"\"Impo\" è il nome della specie. Gli è stato dato perché portano un'incisione sulla nuca che forma quella scritta...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un'incisione che dice \"Impo\"...?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Comunque io l'ho osservato abbastanza e non saprei cos'altro ricavarne. Neil stava iniziando a interessarsene, ma, da quello che so, non ne ha mai potuto osservare uno da vicino. Se glielo lasciassi studiare potrebbe dedurne qualcosa in più.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Va bene. Come lo trasporto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non devi trasportarlo, ti seguirà quando attivi questa pietra...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoDalBibliotecario"]:
            oggettoDato = LI.IMPOFRUTTO_PICCOLO
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Si è svegliato?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"L'ho appena alimentato. Non ti preoccupare, non è aggressivo.")
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
            dialogo.append(u"Gli impo sono molto razionali e metodici. Eseguono sempre l'azione che ritengono prioritaria per le circostanze. Lo fanno finché non esauriscono le energie, a quel punto si fermano e aspettano il nutrimento. Adesso, sembrerà strano, ma la priorità di questo impo è rimanere fermo. E ci resterà finché qualcuno non gli dirà di fare qualcos'altro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Qualcuno...? Possiamo... posso dirgli cosa fare?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Puoi dirgli che azione compiere a seconda della situazione e lui la eseguirà ogni volta senza batter ciglio. Ma, per comunicargli queste informazioni, devi inserirgli degli impofogli nell'apertura che ha dietro la testa. Queste aperture vengono chiamate \"celle di memoria\" e lui ne ha solo una al momento, quindi puoi fargli fare solo un'azione alla volta.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ah... e cos'è un \"Impofoglio\"?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"L'impofoglio è una specie di foglio non molto spesso ma fatto di un materiale molto più rigido e resistente della carta normale. Tutti gli impofogli sono diversi tra loro e si dividono in due categorie: \"Condizio-Impofogli\", che indicano delle condizioni, e \"Azio-ImpoFogli\", che indicano delle azioni da compiere...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Per dare un'istruzione a un impo devi inserire un Condizio-Impofoglio e un Azio-Impofoglio nella cella di memoria. L'impo, ogni volta che deve decidere cosa fare, legge la condizione e l'azione nella cella e, se valuta di trovarsi nella situazione adatta, esegue l'istruzione, altrimenti sta fermo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, sembra abbastanza complicato.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Certo... Se vuoi dare un'occhiata, in biblioteca ci sono diversi libri che parlano più dettagliatamente del loro funzionamento, ma sono sicuro che imparerai in fretta facendo qualche prova. Al momento io ho solo questi due di impofogli: questo Condizio-Impofoglio individua una situazione in cui qualcuno vuole aggredirti, mentre questo Azio-Impofoglio fa eseguire un attacco folgorante.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Wow! Possiamo farglielo fare ora?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"No! Non in città e soprattutto non nel mio studio! Poi adesso devo tornare a lavoro. Lo potrai vedere direttamente sul campo quando ne avrai bisogno. Ti faciliterà il viaggio, la Selva Arida è una zona parecchio ostile per gli umani, ma con un impo non avrai problemi. L'unica cosa...  portati delle medicine e cerca di evitare gli scorpioni. Non dovresti incontrarli ma, nel caso, stagli alla larga.")
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
            dialogo.append(u"Ok: selva, evita gli scorpioni e poi lago... Grazie mille per l'aiuto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non c'è di che, Sara. Ah, dimenticavo! Prendi questo... è un impofrutto, un frutto che nasce nelle montagne occidentali di cui si nutrono gli impo. Daglielo quando vedi che sta esaurendo le energie.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un \"Impofrutto\"? Non sembra affatto un frutto...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Già... ne avevo altri ma non li trovo più... devo averli usati... In ogni caso, buona fortuna per il viaggio, ragazza.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
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
            dialogo.append(u"Sì, li puoi trovare negli scaffali al piano di sopra. Sono tutti colorari di nero, non puoi sbagliarti.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi René...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Sara, che ci fai qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ho portato Impo a Neil e mi ha detto che servono questi strumenti per studiarlo... tu li hai?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ti ha detto di chiederli a me?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, in realtà no, ma se li avessi tu, sarebbe molto più semplice...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*> c'è un mercante che dovrebbe avere questo genere di arnesi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Un certo Rod. Lo conosci?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì... sì, lo conosco, l'ho già incontrato qualche volta...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dovresti rivolgerti a lui, credo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"René, a proposito di Rod, sai dove posso trovarlo adesso?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non ne ho idea ragazza, quel tipo è sempre in viaggio. L'ho visto spesso arrivare dalle montagne occidentali, però non so se sia una buona idea cercarlo là...")
                partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi René...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Sara, che ci fai qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Passavo per un saluto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Oh... sei andata da Neil?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, mi ha chiesto di prendere degli strumenti per studiare Impo e ci sto tornando adesso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ah... degli strumenti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì. Non so che intenzioni abbia...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... <*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Tu... cosa pensi che voglia fargli?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Beh, penso che voglia studiarlo. Non gli farà del male se è quello che ti preoccupa. Gli impo sono praticamente immortali, te l'ho già detto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> ok...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Va bene... devo tornare a lavoro adesso.")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"René...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sara, sono impegnato al momento. Ripassa più tardi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
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
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"] and (tipo.startswith("Ragazz") or tipo == "OggettoAssistBiblioteca"):
        partiDialogo = []
        if tipo.startswith("Ragazzo"):
            nome = LI.SCONOSCIUTO
        elif tipo.startswith("Ragazza"):
            nome = LI.SCONOSCIUTA
        elif tipo == "OggettoAssistBiblioteca":
            nome = LI.ASSISTENTE_BIBLIOTECARIO
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non ho niente da chiedergli...)")
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

    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca1"]:
        if tipo == "AssistBiblioteca":
            partiDialogo = []
            nome = LI.ASSISTENTE_BIBLIOTECARIO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"]:
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
                dialogo.append(u"Mi serve per certificare la t... non puoi non averlo. Ne viene assegnato uno a tutti quando entrano in città. L'hai perso?")
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
                dialogo.append(u"Sì, certo, ma non sarò certo io a disturbarlo. Lui non ha molta pazienza per queste cose...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E come...? Posso passare solo per parlare con lui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mi spiace, devi per forza avere un documeto.")
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
                dialogo.append(u"Perfetto, ti do la benvenuta nella biblioteca. Al piano terra troverai tutti gli scritti riguardan-")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ecco il certificato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perfetto, ti do la benvenuta nella biblioteca. Al piano terra troverai tutti gli scritti riguardan-")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAssistBiblioteca":
            partiDialogo = []
            nome = LI.ASSISTENTE_BIBLIOTECARIO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dov'è il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Senti, ragazzina! È consuetudine esporre l'organizzazione dei reparti ai nuovi arrivati! Prima di fare le tue domande, dovresti almeno avere la decenza di rispettare e ascoltare chi hai di fronte!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Mi stai ascoltando?!")
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
                dialogo.append(u"Come ti pare! È al primo piano, ma di sicuro non vorrà essere disturbato.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dov'è il bibliotecario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Primo piano, ti ho detto.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ho niente da chiedergli...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non sono rimasta in buoni rapporti con lui... non credo voglia aiutarmi...)")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
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
                dialogo.append(u"No, lui è dall'altra parte di questi scaffali adesso.")
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
            nome = LI.SCONOSCIUTO
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
                dialogo.append(u"... Dovrebbe essere al piano di sopra adesso.")
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
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, scusi il disturbo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Shhh!<*> Non si parla in biblioteca.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sì, ma una dom-")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Shhh!<*>")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
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
            nome = LI.SCONOSCIUTO
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
            nome = LI.SCONOSCIUTO
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
                dialogo.append(u"No, è quel signore un po' anziano laggiù...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di parlare con le altre persone adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusi il disturbo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Shhh!<*> Silenzio in biblioteca!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Una domand-")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Shhh!<*>")
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
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
            nome = LI.LIBRO
            if x == GlobalHWVar.gpx * 12:
                nome = LI.LIBRO_SCOPO_DEGLI_IMPO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Scopo degli impo\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Come già spiegato in precedenza, ciò che spinge gli impo ad agire è determinato dagli impofogli. Tuttavia esistono due casi eccezionali in cui l'azione compiuta è dovuta ad altre ragioni...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il primo caso in cui gli impofogli non vengono eseguiti si presenta quando l'impopietra è attiva. A quel punto, l'impo proprietario della pietra, inizierà ad avvicinarsi a essa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il secondo caso si presenta quando nessun impofoglio può essere eseguito ma è stato soddisfatto un Condizio-Impofoglio in precedenza che ha un obiettivo che non è più nel campo visivo. In questo caso, l'impo memorizzerà la posizione in cui ha visto l'obiettivo e, se avrà abbastanza energia per eseguire l'Azio-Impofoglio, si muoverà in quella direzione finché non eseguirà l'azione o raggiungerà la posizione...")
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18:
                nome = LI.LIBRO_SACCHE_ENERGETICHE
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sacche Energetiche\"...)")
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
                nome = LI.LIBRO_GESTIONE_DELL_IMPOFORZA
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Gestione dell'impo-forza\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... L'energia degli impo può essere gestita solo in parte dagli umani...")
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
                nome = LI.LIBRO_IMPOMALUS
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Impo-malus\"...)")
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
                dialogo.append(u"... Gli impo sono in grado di tornare autonomamente alle loro temperature ideali, ma per farlo rallentano i propri movimenti per un po' di tempo...")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"]:
        if tipo == "OggettoLibreriaStudioBibliotecario":
            partiDialogo = []
            nome = LI.LIBRO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci sono un sacco di libri...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"]:
                nome = LI.LIBRO_MOT_RET_UNI_ACC
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Allora, ha detto di vedere il \"Moto rettilineo uniformemente accelerato\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Oh, trovato! Vediamo se c'è una spiegazione comprensibile...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"In questa lezione inizieremo a trattare il modello del moto uniformemente accelerato... <br> Un \"moto rettilineo uniformemente accelerato\" è un tipo di moto in cui un corpo si muove lungo una linea retta con accelerazione costante.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Le formule che si usano per calcolare gli esiti di questi tipi di moto vengono chiamate \"leggi orarie del moto rettilineo uniformemente accelerato\" e sono principalmente due: <br> <*>#italic#Vf = Vi + A×T<*> <br> <*>#italic#S = Vi×T + (1/2)×A×T²<*>")
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
                dialogo.append(u"(Vediamo se ce n'è uno simile alla mia situazione...)")
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
                dialogo.append(u"(<*>#italic#Mmh...<*> non so se ho capito tutto, ma... sostituendo i dati nelle formule, dovrebbe andare... credo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi va di leggere altre spiegazioni di formule che non capisco...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Libri di René...)")
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
                dialogo.append(u"(<*>#italic#Mmmh...<*> non capisco niente di come è organizzato...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Hans non è stato segnato su questo registro...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un registro della biblioteca...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLibreriaRegistri":
            partiDialogo = []
            nome = "OggettoLibreriaRegistri"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono i registri della biblioteca. Quello di oggi è sulla scrivania...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono i registri della biblioteca...)")
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
                dialogo.append(u"(Ci sono dei fogli e una penna...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non mi metterò a fare altri calcoli adesso...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Fogli di René...)")
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
            dialogo.append(u"(Non è bastato per pulire...)")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
