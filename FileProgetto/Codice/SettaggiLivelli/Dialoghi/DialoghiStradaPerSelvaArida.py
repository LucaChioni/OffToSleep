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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = "Soldato"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati. Potrebbero chiedermi qualcosa sull'omicidio...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        if tipo == "OggettoCartelloSelva":
            partiDialogo = []
            nome = "OggettoCartelloSelva"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(C'è scritto: \" - <*>#bold#SELVA ARIDA<*> - Attenzione alla fauna velenosa\"...)")
            partiDialogo.append(dialogo)
        elif tipo == "AssistBiblioteca":
            if avanzamentoDialogo == 0:
                partiDialogo = []
                nome = "Sconosciuto"
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ehi, tu! Dove hai trovato quell'impo?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Scusa non ho tempo adesso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"No, aspetta! Sono seriamente interessato. Sto conducendo delle ricerche sull'inquinamento della Selva e, tra gli argomenti correlati, c'è anche la scomparsa degli impo dalla circolazione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Conosci René? Il bibliotecario...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Gliel'hai rubato?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mi ha... No! Mi ha chiesto di consegnarlo a una persona.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Devo consegnarlo a un certo Neil...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Senti... se l'avessi rubato, che senso avrebbe dirti il nome del proprietario?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È un'informazione facile da verificare. Nel caso mi sarei inventata qualcos'altro cercando di rimanere sul vago, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ok, ok. Forse hai ragione... Va beh, quindi non ne sai nulla di queste creature?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"No, quasi niente.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Va bene...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                partiDialogo = []
                nome = "Sconosciuto"
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quindi... sei riuscito a capire cosa è successo a questo posto?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Beh, è difficile da dire, ma una cosa è certa: questa non è un'evoluzione naturale della flora. Sono state gettate delle sostanze inquinanti in tutta l'area. Sostanze che tuttora non sono ancora state assorbite e smaltite dal terreno. E purtroppo una grande quantità si è poi riversata nel lago qua accanto creando gravi danni anche a tutta la fauna acquatica.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Da quanto tempo c'è questa situazione?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Da molto tempo. È così da prima che nascessi. Dicono che sia mutata repentinamente nel giro di una settimana. Nessuno sa per certo com'è successo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché qualcuno dovrebbe fare una cosa del genere?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"E chi lo sa... nessuno sembra averne tratto beneficio. Forse si è trattato di un incidente.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> ho sentito che c'è una guerra in corso... ne sai qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non iniziare con queste cose! Anch'io li ho sentiti. Sono solo complottisti che si inventano delle teorie per farsi ascoltare da qualcuno. Non fidarti di quelli.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dici? Sarebbe una spiegazione valida...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Certo...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                partiDialogo = []
                nome = "Sconosciuto"
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Se inizi a credere a tutte le dicerie cittadine, penserai che tra qualche giorno finirà il mondo e moriremo tutti.")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
