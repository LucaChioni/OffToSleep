# -*- coding: utf-8 -*-

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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Wow...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Siamo arrivati.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["esplosioneDelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"OHHH... MERDA!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostEsplosioneDelVulcano1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È... è esplosa una montagna!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Vicino al palazzo di Rod!")
                partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if tipoId == "ServoLancia-0":
                    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
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
                            dialogo.append(u"... No. L'entrata è dall'altra parte.")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Oh... ok.")
                            partiDialogo.append(dialogo)
                        elif avanzamentoDialogo == 1:
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
                            dialogo.append(u"...")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Ehi...?")
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Ehi...?")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"...")
                            partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Ehi...?")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"...")
                        partiDialogo.append(dialogo)
                elif tipoId == "ServoLancia-1":
                    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
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
                            dialogo.append(u"Salve... sto cercando un certo Neil, abita qui?")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"... Non aspetta ospiti. Senza un invito non ti è concesso entrare.")
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
                            dialogo.append(u"Senza un invito non ti è concesso entrare.")
                            partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(u"Ehi...?")
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(u"...")
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
        elif tipo == "Neil":
            partiDialogo = []
            nome = "Neil"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello2"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoEsternoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"C'è un silenzio tombale...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cioè, non che abbia qualcosa contro il silenzio, sia chiaro... è solo un po' inquietante, tutto qui...")
                partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
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
                            dialogo.append(u"... Hai un invito?")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Certo, uhm... ecco, tieni.")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"... \"Certificato di residenza\"... non è valido.")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Ma... me l'hanno dato così...")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"...")
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Perché il mio invito non è valido?")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"...")
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
                            dialogo.append(u"...")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Ehi... so che non era un invito quello di prima... scusa se ti ho mentito...")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"...")
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(u"Salve...")
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(u"...")
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
                        dialogo.append(u"Mi chiamo Sara. Devo incontrare Neil.")
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
                        dialogo.append(u"... Da questa parte.")
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
                        dialogo.append(u"Il padrone ha ordinato di lasciarti libero accesso.")
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
        elif tipo == "OggettoCancelloCastello":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È chiuso...)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilFuoriDalCastelloDuranteLaFuga"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipo == "Neil":
            partiDialogo = []
            nome = "Neil"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"N-non ti avvicinare!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Perché hai ucciso i miei soldati, Sara?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello5"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAscensore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok... adesso dobbiamo trovare Rod. Che sia sempre al suo \"avamposto\"?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoScomparsaDiNeilPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... C'è un silenzio tombale anche qua fuori...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Chissà com'è la città adesso...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E Rod... magari lui...")
                partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non puoi entrare armata.")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
