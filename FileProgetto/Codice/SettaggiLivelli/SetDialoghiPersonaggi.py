# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.SettaggiLivelli.Dialoghi.DialoghiNessuno as DialoghiNessuno
import Codice.SettaggiLivelli.Dialoghi.DialoghiTutorial as DialoghiTutorial
import Codice.SettaggiLivelli.Dialoghi.DialoghiCasa as DialoghiCasa
import Codice.SettaggiLivelli.Dialoghi.DialoghiForestaCadetta as DialoghiForestaCadetta
import Codice.SettaggiLivelli.Dialoghi.DialoghiStradaPerCitta as DialoghiStradaPerCitta
import Codice.SettaggiLivelli.Dialoghi.DialoghiCitta as DialoghiCitta
import Codice.SettaggiLivelli.Dialoghi.DialoghiCasaUfficiale as DialoghiCasaUfficiale
import Codice.SettaggiLivelli.Dialoghi.DialoghiBiblioteca as DialoghiBiblioteca


def caricaDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]
    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False

    # se c'è una scelta la variabile scelta conterrà il numero corrispondente a quella giusta (se ce n'è più di una giusta, la variabile conterrà i numeri di queste una dopo l'altra (es. 12, 134))
    # i dialoghi che iniziano con "???DOMANDA???" contengono 6 frasi in totale (ossia => "???DOMANDA???", la domanda posta, opzione 1, opzione 2, opzione 3, opzione 4)
    # i dialoghi che iniziano con "!!!RISPOSTA!!!" contengono 5 frasi in totale (ossia => "!!!RISPOSTA!!!", risposta opzione 1, risposta opzione 2, risposta opzione 3, risposta opzione 4)
    if tipo == "test":
        partiDialogo = []
        nome = "Bob"
        if avanzamentoStoria == 0:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = True
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Ciao, ecco la merce")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Ecco la merceee")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == 1:
            oggettoDato = "oggetto speciale"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ciao, la merce è finita")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È finita?")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = 3
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Ti sto per fare una domanda")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("???DOMANDA???")
            dialogo.append("Quanto fa 2+3?")
            dialogo.append("Che schifo di domanda!")
            dialogo.append("(cambia discorso parlando di carote)")
            dialogo.append("Almeno 3")
            dialogo.append("(mettilo a disagio fingendo di non aver sentito)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("!!!RISPOSTA!!!")
            dialogo.append("Scusa...")
            dialogo.append("Scusa, non mi interessano le carote")
            dialogo.append(u"Mmh... è giusto...")
            dialogo.append("2+3? ... mi scusi signore ... 2+3? ...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non ho più merce")
            partiDialogo.append(dialogo)

    if tipo == "Nessuno":
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiNessuno.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif tipo == "Tutorial":
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiTutorial.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["casaHansLucy1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansLucy4"]:
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCasa.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiForestaCadetta.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiStradaPerCitta.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["città1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["città10"]:
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCitta.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCasaUfficiale.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["biblioteca3"]:
        partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiBiblioteca.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


def gestisciRisposteSbagliate(avanzamentoStoria):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
        GlobalGameVar.datiEnigmaBibliotecario["reset"] = True
