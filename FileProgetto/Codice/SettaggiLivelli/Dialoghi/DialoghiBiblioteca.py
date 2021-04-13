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
    if tipo == "AssistBiblioteca":
        partiDialogo = []
        nome = "Assistente bibliotecario"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosse100Monete"]:
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
            dialogo.append(u"No, non mi è stato dato nessun documento quando sono arrivata. Chi è che me lo avrebbe dovuto dare?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Se non sei residente, ti viene assegnato il certificato di permanenza quando arrivi agli alloggi profughi. Era in mezzo agli altri fogli che ti hanno dato...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Oh, perfetto... quando sono arrivata mi è stato detto che non c'era più posto negli alloggi. Quindi David, il capitano della guardia notturna, si è offerto di ospitarmi per la notte.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Addirittura... ospitata da David? Beh, allora chiedi a lui di rilasciarti la certificazione. Altrimenti non posso lasciarti passare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene, chiederò a lui.")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
