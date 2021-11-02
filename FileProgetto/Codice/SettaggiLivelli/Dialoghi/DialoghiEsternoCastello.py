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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if tipo == "ServoLancia":
            partiDialogo = []
            nome = "Soldato con lancia"
            if tipoId == "ServoLancia-0":
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ehi, salve. Devo parlare con Neil, puoi aprirmi il cancello?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Ferma dove sei! Chi sei? E cosa vuoi?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Sono Lucy e... vorrei parlare con Neil.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Neil non ha tempo da perdere, se non hai un invito puoi anche andartene.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ce l'ho l'invito.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Bene. Mostralo alle guardie che sorvegliano l'entrata allora.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non è questa l'entrata?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Questa è un'uscita. L'entrata è da quella parte.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Oh... ok.")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Mostra il tuo invito alle guardie che sorvegliano l'entrata e ti lasceranno entrare.")
                    partiDialogo.append(dialogo)
            elif tipoId == "ServoLancia-1":
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Cosa vuoi?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Salve... sto cercando un certo Neil, abita qui?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"... Non aspetta ospiti. Questo è il suo castello, ma senza un invito non ti è concesso entrare.")
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Neil è impegnato. Senza un invito non ti riceverà.")
                    partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello2"]:
        if tipo == "ServoLancia":
            partiDialogo = []
            nome = "Soldato con lancia"
            if tipoId == "ServoLancia-2":
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Dovrei entrare.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"<*>#italic#Tsk!<*> Non credo proprio. Hai un invito?")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Certo.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"<*>#italic#Mh.<*> Fammi vedere.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Ehm... Ecco, tieni.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"Ok... Ah, \"Certificato di residenza\"... Che strano invito, eh?")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Sì... me l'hanno dato così...")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"<*>#italic#Hahaha...<*> Levati di torno.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Senti... scusa, non volevo... Sono venuta per-")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"Levati di torno!")
                        partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"(Non ho tanta voglia di disturbarlo di nuovo... Come mi è venuto in mente di dargli il certificato di residenza?!)")
                        partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    if avanzamentoDialogo == 1:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"Questa è l'entrata del castello. A te è concesso l'ingresso.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Sì... Scusa se ti ho mentito prima.")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"<*>#italic#Mmh...<*>")
                        partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"Questa è l'entrata del castello. A te è concesso l'ingresso.")
                        partiDialogo.append(dialogo)
            elif tipoId == "ServoLancia-3":
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSecondaStanzaEsternoCastello"]:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"È questa l'entrata del castello?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Chi sei? E perché sei qui?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Mi chiamo Lucy. Devo incontrare Neil.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Mostrami l'invito.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Non ho nessun invito. Devo consegnare questo Impo a Neil per conto di René, il bibliotecario cittadino.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"<*>#italic#Mh.<*> Da questa parte.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Seguimi.")
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Il padrone ha ordinato di lascirti libero accesso.")
                    partiDialogo.append(dialogo)
        elif tipo == "OggettoCancelloCastello":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È chiuso.")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello5"]:
        if tipo == "ServoLancia":
            partiDialogo = []
            nome = "Soldato con lancia"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non puoi entrare armata!")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
