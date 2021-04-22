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
        nome = "Bibliotecario"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"]:
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
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Uff! Perché non viene via? ...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripulitoVomito"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Va beh, non importa...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioVenutoVersoDiTe"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
