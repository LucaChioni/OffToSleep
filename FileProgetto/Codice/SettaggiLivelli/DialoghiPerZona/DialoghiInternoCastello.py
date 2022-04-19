# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalImgVar as GlobalImgVar
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

    if tipo.startswith("OggettoDictCofanetto"):
        nome = "Cofanetto"
        if tipo == "OggettoDictCofanettoAperto":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Bauli aperti e svuotati... allora non deruba solo me...)")
            partiDialogo.append(dialogo)
        elif tipo == "OggettoDictCofanettoChiuso":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Roba di Neil, non m'interessa...)")
            partiDialogo.append(dialogo)
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and (tipo in GlobalImgVar.vettoreNomiNemici or tipo == "ServoSpada" or tipo == "ServoArco" or tipo == "ServoLancia" or tipo.startswith("OggettoQuadro")):
        if tipo in GlobalImgVar.vettoreNomiNemici:
            partiDialogo = []
            if tipo == "ServoLancia":
                nome = "Soldato con lancia"
            elif tipo == "ServoArco":
                nome = "Soldato con arco"
            elif tipo == "ServoSpada":
                nome = "Soldato con spada"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
        elif tipo == "ServoSpada":
            partiDialogo = []
            nome = "Soldato con spada"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È immobile...)")
            partiDialogo.append(dialogo)
        elif tipo == "ServoArco":
            partiDialogo = []
            nome = "Soldato con arco"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È immobile...)")
            partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = "Soldato con lancia"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È immobile...)")
            partiDialogo.append(dialogo)
        elif tipo.startswith("OggettoQuadro"):
            partiDialogo = []
            nome = "Quadro"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Un quadro...)")
            partiDialogo.append(dialogo)
    elif tipoId.startswith("OggettoQuadro") and GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        partiDialogo = []
        nome = "Quadro"
        if tipoId == "OggettoQuadro-7":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ok, questo... è un bel quadro...)")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Un quadro di Neil... non so quale sia il suo significato e non ho voglia di pensarci...)")
            partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-1":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Sembra una parete piena di crepe...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-2":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una città che si affaccia su un mare in tempesta... credo...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-3":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un castello con una torre imponente nel mezzo...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-4":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una donna con un vestito enorme accasciata su un letto...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-5":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un paesino a valle di una montagna...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-6":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una semplice foresta, direi...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-7":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un uomo nudo su una conchiglia. Quindi è così che sono fatti... sembra scomodo...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-8":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un albero dal tronco bianco in mezzo a un paesaggio macabro...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-9":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un vaso con dei fiori...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-10":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un porto con diverse barche...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-11":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una nave da guerra. Voglio dire, non so perché, ma dall'aspetto sembra... aggressiva...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-12":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un uomo fatto di frutta e verdura. Ok...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-13":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una bambina che raccoglie dei fiori...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-14":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Pesche...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-15":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Il riflesso di un castello nell'acqua...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-16":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un albero in un... prato, credo... non so, l'unica cosa a fuoco è l'albero, il resto e sfocato...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-17":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una montagna innevata...)")
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-18":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un lago all'alba...)")
        partiDialogo.append(dialogo)
    elif tipoId.startswith("OggettoDictCadavereSoldatoCastello"):
        partiDialogo = []
        nome = "Cadavere soldato"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"]:
            oggettoDato = "Chiave ufficio di Neil"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Oh cazzo...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok... l-la chiave...")
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
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["saraCamminatoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Wow... ma guarda dove ti ho portato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoScomparsaDiNeilPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E poi che dovrei fare io di preciso?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non mi hanno spiegato niente... cioè, potevano almeno dirmi con calma tutto quello che stavano studiando e poi spiegarmi a modo cosa fare...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Più nel dettaglio, dico...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dovrei cercare qualcosa? Dovrei andare da qualche parte? Dovrei solo aspettare? E per quanto tempo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Uff...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Oppure mi sta solo usando per... testare l'\"apparecchio cerebrale\"...?")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-3":
            partiDialogo = []
            nome = "Soldato con lancia"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaEntratoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Aspetta qui.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Neil sa già che lo stiamo aspettando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ok...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Scusa, dovrei uscire un attimo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-4":
            partiDialogo = []
            nome = "Soldato con lancia"
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
                dialogo.append(u"(È immobile e guarda fisso davanti a sé...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-0":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Salve...")
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
                dialogo.append(u"(Mi sta ignorando completamente...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello2"]:
        if tipoId == "ServoSpada-0":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Neil è da questa parte?")
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
                dialogo.append(u"(Non hanno tanta voglia di parlare...)")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerImpoNonBloccatoPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E poi Neil dov'è andato?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È scomparso appena prima che il tempo si \"bloccasse\"... ha usato un... teletrasporto?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Mentre René è rimasto lì... e poi perché Renè era lì?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Probabilmente era interessato alle ricerche di Neil... o forse l'ha chiamato Neil per velocizzare le sue ricerche su di te...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmmh...<*>")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello3"]:
        if tipoId == "ServoArco-1":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Salve...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ti... ti piace quel quadro?")
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
                dialogo.append(u"(Sta fissando quel quadro... deve averlo colpito particolarmente...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-0":
            partiDialogo = []
            nome = "OggettoLibreriaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Libri sull'ambiente...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un sacco di libri sull'ambiente, la natura e gli animali...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Libri di Neil...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello4"]:
        if tipoId == "ServoLancia-5":
            partiDialogo = []
            nome = "Soldato con lancia"
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
                dialogo.append(u"... Dalla tua lancia sta colando uno strano liquido viola...")
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
                dialogo.append(u"(È immobile... sembra che non stia neanche respirando...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoSpecchioCastello-0":
            partiDialogo = []
            nome = "OggettoSpecchioCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Oh, uno specchio. È proprio quello che mi serviva. Non credo che qualcuno noterebbe la sua assenza...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non si stacca... aspetta, continua dentro il muro... continua lungo tutta la parete... perché mettere uno specchio dentro il muro?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ehi, uno specchio! Cavolo mi sono lavata ieri e guarda qua... mi servirebbe un altro bagno...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLavandinoCastello-0":
            partiDialogo = []
            nome = "OggettoLavandinoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ah, utilizza ancora il mio vecchio modello di schema idraulico... quanta inefficienza...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questi sistemi per portare l'acqua in casa sono più comuni di quel che pensavo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un lavandino...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoGabinettoCastello-0":
            partiDialogo = []
            nome = "OggettoGabinettoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non devo andare in bagno adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È da un po' che non vado in bagno, ma ora non ho tempo per pensare ai miei problemi digestivi...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un gabinetto...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoVascaCastello-0":
            partiDialogo = []
            nome = "OggettoVascaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Vasca idromassaggio con acqua riscaldata... troppa comodità...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Una vasca enorme. Chissà se anche qui c'è l'acqua riscaldata...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Una vasca...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello5"]:
        if tipoId == "ServoArco-2":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Come fate a rimanere in piedi immobili per così tanto tempo?")
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
                dialogo.append(u"(Forse sono solo sordi...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello6"]:
        if tipoId == "ServoSpada-1":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"... Cosa stai facendo tu qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non c'è niente a cui fare la guardia...")
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
                dialogo.append(u"(Chissà a cosa stanno pensando... tipo: \"Se mi muovo, non ho fatto bene il mio lavoro\"?)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello7"]:
        if tipoId == "ServoLancia-6":
            partiDialogo = []
            nome = "Soldato con lancia"
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
                dialogo.append(u"Se sei citrullo, rimani fermo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ah ah, fregato.")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci si potrebbe divertire un sacco con queste guardie...)")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Voi avete già cenato?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Potremmo mangiare insieme... sai, parlando un po'...")
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
                dialogo.append(u"(Non insisterò... magari sono solo molto stanchi e non hanno voglia di starmi a sentire...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-3":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Tu fai la guardia al tavolo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Perché questi tizi non fanno niente?)")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... È per me la cena?")
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
                dialogo.append(u"(Chi tace acconsente, direi... ora che ci penso, potrei chiudere un sacco di affari con queste guardie...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-13":
            partiDialogo = []
            nome = "Soldato con lancia"
            oggettoDato = "Chiave stanza"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"OH...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Sara, la tua camera da letto è al secondo piano.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ah... ok...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoCaminoCastello-0":
            partiDialogo = []
            nome = "OggettoCaminoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo camino è completamente inutile con il pavimento radiante...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un camino... sembra non essere mai stato utilizzato...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un camino...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoSediaCastello-0":
            partiDialogo = []
            nome = "OggettoSediaCastello"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sembra non esserci nessun altro... dovrei sedermi qui?)")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoCarrelloCiboCastello-0":
            partiDialogo = []
            nome = "OggettoSediaCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono dei vassoi vuoti...)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello8"]:
        if tipoId == "ServoArco-4":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Salve, tu per caso sai parlare?")
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
                dialogo.append(u"(Forse parlano un'altra lingua?)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoVasoCastello-0":
            partiDialogo = []
            nome = "OggettoVasoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questi vasi emanano strani odori...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(E un altro vaso... ma che hanno di così bello da dover essere presenti ovunque?)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un vaso...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello9"]:
        if tipoId == "ServoLancia-7":
            partiDialogo = []
            nome = "Soldato con lancia"
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
                dialogo.append(u"Ehi, ti ho già visto al piano di sotto! Eri tu?")
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
                dialogo.append(u"(Questi tizi sono tutti uguali...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello10"]:
        if tipoId == "ServoLancia-8":
            partiDialogo = []
            nome = "Soldato con lancia"
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
                dialogo.append(u"A cosa bisogna fare la guardia qui? Potrebbero entrare dei piccioni?")
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
                dialogo.append(u"(Queste guardie sono ovunque, ma nel castello non c'è nessuno... si sorvegliano tra loro?)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-5":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Tu sorvegli quella porta...")
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
                dialogo.append(u"(Magari vengono pagati bene...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLettoCastello-0":
            partiDialogo = []
            nome = "OggettoLettoCastello"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAperturaCameraDaLettoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ce l'ho fatta... un altro passo e sarei crollata...)")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Dev'essere un letto per gli ospiti...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo letto è morbidissimo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Il mio letto...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoArmadioCastello-0":
            partiDialogo = []
            nome = "OggettoArmadioCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = False
                if not GlobalGameVar.cambiataAlCastello[0]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append("???DOMANDA???")
                    dialogo.append(u"Ci sono dei vestiti... dovrei cambiarmi?")
                    dialogo.append(u"Sì.")
                    dialogo.append(u"Forse...")
                    dialogo.append(u"No.")
                    dialogo.append(u"Non so se mi starebbe bene questo violetto...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append("!!!RISPOSTA!!!")
                    dialogo.append(u"Aspetta... ma che sto facendo?!")
                    dialogo.append(u"<*>#italic#Mmh...<*>")
                    dialogo.append(u"Non ha neanche il cappuccio...")
                    dialogo.append(u"Allora no...")
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Oh, ci sono i vecchi vestiti di Sara... deve aver alloggiato qui. Profumano di sapone e un po' di sudore...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append("???DOMANDA???")
                    dialogo.append(u"Potrei provarli...?")
                    dialogo.append(u"Sì...?")
                    dialogo.append(u"Forse...")
                    dialogo.append(u"No.")
                    dialogo.append(u"Non so se mi entrano...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append("!!!RISPOSTA!!!")
                    dialogo.append(u"Aspetta... ma che sto facendo?!")
                    dialogo.append(u"<*>#italic#Mmh...<*>")
                    dialogo.append(u"Meglio di no.")
                    dialogo.append(u"Lasciamo stare...")
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("???DOMANDA???")
                if not GlobalGameVar.cambiataAlCastello[0]:
                    dialogo.append(u"Ci sono dei vestiti... dovrei cambiarmi?")
                else:
                    dialogo.append(u"Ci sono i miei vecchi vestiti... dovrei cambiarmi?")
                dialogo.append(u"Sì.")
                dialogo.append(u"Forse...")
                dialogo.append(u"No.")
                dialogo.append(u"Dovrei pensare a opzioni diverse da \"sì\" e \"no\"?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("!!!RISPOSTA!!!")
                dialogo.append(u"Ok...")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                dialogo.append(u"Questi vestiti vanno più che bene.")
                dialogo.append(u"Direi di no... quindi?")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                if not GlobalGameVar.cambiataAlCastello[0]:
                    dialogo.append(u"(Ci sono dei vestiti... non mi entrano...)")
                else:
                    dialogo.append(u"(Ci sono i miei vecchi vestiti... non mi entrano più...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoComodinoCastello-0":
            partiDialogo = []
            nome = "OggettoComodinoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(I cassetti sono vuoti...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Su questo comodino c'è solo una lanterna. I cassetti sono vuoti...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un comodino...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLavandinoCastello-1":
            partiDialogo = []
            nome = "OggettoLavandinoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ah, utilizza ancora il mio vecchio modello di schema idraulico... quanta inefficienza...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Anche da qui uscirà acqua riscaldata?)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un lavandino...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoVascaCastello-1":
            partiDialogo = []
            nome = "OggettoVascaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Vasca idromassaggio con acqua riscaldata... troppa comodità...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ho tempo per farmi un bagno adesso...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Una vasca...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoGabinettoCastello-1":
            partiDialogo = []
            nome = "OggettoGabinettoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non devo andare in bagno adesso...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non sento il bisogno di andare in bagno... forse dovrei sedermi e aspettare un po', ma non ho tempo da perdere adesso...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Un gabinetto...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello11"]:
        if tipoId == "ServoSpada-2":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Non credo che questa parete costituisca una minaccia, non occorre... va beh...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non so se riuscirei a fare il loro lavoro...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-3":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Ehi, non c'è bisogno di sorvegliare la parete, lo sta già facendo quel soldato laggiù...")
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
                dialogo.append(u"(Due soldati per una sola parete. Chi è l'incompetente che organizza la guardia?!)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoFinestraCastello-0":
            partiDialogo = []
            nome = "OggettoFinestraCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È mattina...)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello12"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoServoLanciaEntrataNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Tu e questi tizi avete diverse cose in comune...")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-6":
            partiDialogo = []
            nome = "Soldato con arco"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sai cosa faceva uno sputo su una scala?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Saliva.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Se non reagiscono a quella della saliva, non so più che fare...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello13"]:
        if tipoId == "ServoArco-7":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Ehi, soldato... guarda un po' cosa sto per fare...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sto per sputare sul pavimento...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Lo sto per fare... proprio su questo tappeto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sto caricando la saliva...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Puh!<*>")
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
                dialogo.append(u"(Forse se gli sputassi in faccia... No, meglio di no...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoBarcaCastello-0":
            partiDialogo = []
            nome = "OggettoBarcaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Perché ha questi modellini sparsi ovunque?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(E un altro modellino di una barca... Neil deve esserne proprio appassionato...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Una barca...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello14"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello12"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Dove stiamo andando?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Tu continui a seguirmi, ma...")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-4":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Perché sto ancora provando a parlarvi?")
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
                dialogo.append(u"(Potrebbero essere statue?)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello15"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello14"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Quanti piani ci sono ancora?")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-9":
            partiDialogo = []
            nome = "Soldato con lancia"
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
                dialogo.append(u"Ehi, ma... sono io il problema?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ho fatto qualcosa di male? Vi sto antipatica?")
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
                dialogo.append(u"(Forse ho mancato di rispetto in qualche modo...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello16"]:
        if tipoId == "ServoSpada-5":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Sei a guardia di una porta che tutti possono attraversare?")
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
                dialogo.append(u"(La porte sono aperte, ma ci sono comunque dei soldati di guardia...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-6":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Ehi, ciao. Mi chiamo Sara. Possiamo conoscerci se ti va...")
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
                dialogo.append(u"(Forse sono solo poco interessante...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-10":
            partiDialogo = []
            nome = "Soldato con lancia"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehi, sei tu quello che mi ha aperto il cancello?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Mh...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questi soldati sono tutti uguali...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoFinestraCastello-0":
            partiDialogo = []
            nome = "OggettoFinestraCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È mattina...)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello17"]:
        if tipoId == "ServoSpada-7":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"Ehi, lo chef vuole sapere cosa vuoi per cena...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Niente? Sicuro?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, aveva delle bistecche succulente, ma se non hai fame...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Forse non hanno bisogno neanche di mangiare...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello18"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello15"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Le guardie non ci stanno bloccando... possiamo andare dove vogliamo?")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["giratoVersoImpoPerDarloAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, Impo... starai con loro fino a domani...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Non ti faranno niente, tranquillo... sono solo un po' inquietanti, ma sono innocui...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ok, forse sono io quella che devrebbe preoccuparsi, tu sai difenderti piuttosto bene anche da solo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ma starò bene, non preoccuparti per me...")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-12":
            partiDialogo = []
            nome = "Soldato con lancia"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello18"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Sara. Verrai ricevuta domani. Lascia qua l'impo, la cena è servita al primo piano.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... La cena? Perché domani?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Potrai alloggiare qui per la notte.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma che ore sono?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Non voglio lasciarvi il mio Impo!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E non ho fame.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"La cena è servita al primo piano. Non puoi circolare con l'impo nel castello.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"L'ho fatto fin'ora... e poi perché non posso parlare con Neil adesso?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Neil è occupato. Puoi andartene e tornare domani, se vuoi tenere l'impo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... No...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Uff...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E va bene, starò qui per la notte.")
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
        elif tipoId == "ServoArco-8":
            partiDialogo = []
            nome = "Soldato con arco"
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
                dialogo.append(u"Neil ha detto che puoi staccare prima oggi, se sei stanco.")
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
                dialogo.append(u"(Se imparassi a imitare la voce di Neil...)")
                partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if tipoId == "OggettoLibreriaCastello-1":
                partiDialogo = []
                nome = "Libro (Sulla coscienza Vol.1 - Etica)"
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sulla coscienza Vol.1 - Etica\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... La cultura, di cui l'etica è fondamento, si crea e si evolve negli esseri viventi quando questi crescono e fanno esperienza. Tanto più due animali sono in contatto, tanto più la loro esperienza, e quindi anche la loro cultura, è comune...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Nel momento in cui le circostanze impongono una convivenza tra animali con culture diverse, è necessario che nasca una nuova cultura, e talvolta una nuova etica, come frutto dell'unione delle precedenti. Spesso però, l'impegno nell'adattarsi a una cultura con un'etica molto differente, può richiedere sforzi che non vogliono essere accettati. Sono questi i casi in cui possono nascere scontri...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Nel pensiero di alcuni, nel momento in cui esisterà una sola cultura condivisa da tutti, sarà finalmente chiaro quale sia la giusta etica. È scopo di questi fanatici esportare le proprie credenze presso gli altri, anche attraverso l'uso della forza...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Osservando uno scontro tra due fazioni contrapposte, risulta irrilevante e insensato domandarsi quale delle due abbia torto: ognuna è il male dell'altra, poiché ognuna è giudicata tramite le regole etiche dell'altra...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non può esistere conciliazione tra culture inconciliabili, quindi non può esistere un'etica oggettivamente giusta. E non esisterà neanche nel momento in cui ne rimarrà una: quella che risulterà vincente, dovrà la sua sopravvivenza all'aggressività dei suoi sostenitori, non alla sua oggettività.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*> si potrebbe fare lo stesso ragionamento su un sacco di altre cose...")
                partiDialogo.append(dialogo)
            elif tipoId == "OggettoLibreriaCastello-2":
                partiDialogo = []
                nome = "Libro (Sulla coscienza Vol.2 - Libero arbitrio)"
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sulla coscienza Vol.2 - Libero arbitrio\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Per discutere sul libero arbitrio è innanzitutto necessario distinguere due possibilità: la prima è quella in cui si ritiene che tutto ciò che esiste è costituito da materia; la seconda, invece, è quella in cui si cosidera possibile l'esistenza di elementi non materiali, tra cui rientrerebbe l'anima, come motore di ogni essere vivente...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Decidendo di percorrere la prima ipotesi, è chiaro che non può esserci libero arbitrio: allo stesso modo in cui è possibile calcolare \"azioni\" di oggetti inanimati, sarà possibile calcolare le azioni degli esseri animati. L'unica differenza tra le due categorie rimarrebbe la presenza, nel secondo raggruppamento, della coscienza, a cui la parola \"vita\" ridurrebbe tutto il suo significato.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Percorrendo la seconda ipotesi, invece, è vero che l'anima non sarebbe governata dalle stesse leggi della materia, ma da queste leggi comunque dipenderebbe, anche se in maniera indiretta. Il comportamento degli individui, così come il loro pensiero, viene plasmato dall'esperienza che gli stessi compiono sul mondo materiale. L'anima verrebbe in questo modo influenzata e \"corrotta\" dalla materia, risultando quindi non più libera.")
                partiDialogo.append(dialogo)
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Più ci penso, più sembra assurdo...)")
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"<*>#italic#Mmh...<*> In sostanza, le cose di cui mi ha parlato René...")
                    partiDialogo.append(dialogo)
            elif tipoId == "OggettoLibreriaCastello-3":
                partiDialogo = []
                nome = "Libro (Sulla coscienza Vol.3 - Tempo)"
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sulla coscienza Vol.3 - Tempo\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Sviluppando l'ipotesi per cui la realtà si evolve in modo deterministico, viene spontaneo chiedersi in che modo il tempo scorra in avanti. Potremmo considerare due possibilità: il tempo è composto da un susseguirsi di eventi determinati e separati tra loro, oppure da un \"flusso\" infinito di eventi indistinguibili e inseparabili tra loro.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Prendendo la prima ipotesi, in cui gli eventi sono distinti e separati, dovremmo ipotizzare che, tra un evento e l'altro, ci sia un \"momento\" in cui nessun evento accade, ma in cui avviene un qualcosa che fa andare avanti la serie di eventi. Dovremmo ipotizzare che, in quei lassi di tempo (non più considerabili \"tempo\"), ci sia un \"Motore Immobile\" che, senza essere mosso o \"causato\" da altri eventi, muova in avanti il tempo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Seguendo la seconda ipotesi, in cui gli eventi sono inseparabili e indistinguibili, non si presenta un fenomeno di causa-effetto tra gli eventi. Gli eventi sono, in questo caso, un unico blocco che esiste \"sempre\". La percezione \"temporale\" del tempo risulta, quindi, propria degli esseri viventi: una percezione simile alla lettura di un libro che, pur esistendo per intero, viene compreso parzialmente in diversi momenti del tempo.")
                partiDialogo.append(dialogo)
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Questa è roba di anni fa. Mi domando quanto sia riuscito ad approfondire...)")
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Assurdo...")
                    partiDialogo.append(dialogo)
            elif tipoId == "OggettoLibreriaCastello-4":
                partiDialogo = []
                nome = u"Libro (Sulla coscienza Vol.4 - Realtà)"
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sulla coscienza Vol.4 - Realtà\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Cosa distingue la realtà dall'immaginazione? La realtà che sentiamo, viene catturata da dei sensori, che abbiamo sparsi nel corpo, e poi inviata al cervello tramite impulsi nervosi. Il cervello poi, che si trova al buio dentro un cranio, interpreta e immagina ciò che sta al di fuori di lui, \"ispirato\" da quegli impulsi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... La coscienza, tuttavia, non ha modo di verificare la veridicità di quei segnali, dato che quelli sono l'unica fonte di informazione che ha a disposizione...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... È lecito pensare che tutto ciò che risiede al di fuori della coscienza, potrebbe non essere reale. In questo senso, le differenze tra una vita vissuta tramite i filtri dei sensi e una vissuta tramite i filtri dei sogni, sarebbero quasi nulle...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... In entrambi i casi la realtà viene immaginata, ma, se nel primo caso i sensi impongono dei pensieri e delle reazioni, nel secondo, la coscienza è \"libera\" di concentrarsi su ciò che più gli interessa, senza distrazioni. In questo senso alcuni sostengono che la vera libertà la si può sperimentare solo sognando.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ma ciò che avviene quando si è \"liberi\" di immaginare una realtà, ad esempio sognando, non differsce molto da ciò che percepiamo attraverso i sensi. Ciò dovrebbe indurci a pensare che, o l'immaginazione è creata e plasmata dalla realtà esterna, oppure che, in qualche modo, nell'immaginazione è già contenuta la realtà...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Conseguenza del primo caso è l'inesistenza del pensiero se non come prodotto della realtà. In questo modo, un individuo privo di sensi che non ha mai fatto esperienza della realtà, non potrebbe produrre alcun pensiero. L'individuo esisterebbe senza essere cosciente (e forse, senza essere vivente). La coscienza, dunque, nascerebbe e si evolverebbe solo nel momento in cui entra in contatto con ciò che sta al di fuori di lei.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Seguendo la seconda ipotesi, in cui si sostiene che la realtà è contenuta nell'immaginazione, deduciamo che è la coscienza a produrre la realtà. Ciò che sta \"fuori di noi\", sarebbe una sorta di lista di ricordi che costruiremmo attraverso l'immaginazione. E, data l'evoluzione deterministica della realtà, dovremmo pensare che le leggi fisiche che la governano, siano in verità i meccanismi con cui la coscienza sviluppa i sui pensieri.")
                partiDialogo.append(dialogo)
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Ma come fa ad avere così tante monete se non fa altro che pensare a questa roba? Come fa a convertire in denaro?)")
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non so... sembrano assurde entrambe le ipotesi...)")
                    partiDialogo.append(dialogo)
            elif tipoId == "OggettoLibreriaCastello-5":
                partiDialogo = []
                nome = "Libro (Sull'evoluzione)"
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sull'evoluzione\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... La frequenza di campionamento della realtà, da parte di un soggetto, varia al variarie della sua età. L'invecchiamento degli organi che influenzano le abilità cognitive, fa sì che la presa di coscienza degli eventi e dei pensieri, sia sempre meno frequente...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Se a questo aggiungiamo che gli eventi, accumulati come ricordi nel cervello, vengono dimenticati sempre più rapidamente, risulterà chiaro che, invecchiando, varierà anche la percezione del tempo: il tempo passerà sempre più velocemente rispetto al passato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Per evitare questo lento degrado, è possibile fare delle operazioni sugli organi non solo per mantenerli giovani, ma anche per potenziarli. Usando materiali che sopportano carichi di lavoro più intensi e che non si degradano nel tempo, si possono ottenere organi che permettono di invertire quella tendenza \"naturale\" di percezione del tempo precedentemente descritta...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Occorre innanzitutto sostituire diverse componenti di alcuni organi sensoriali: completa sostituzione del nervo ottico e della retina, ...")
                partiDialogo.append(dialogo)
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Ah, ecco come fa... quanti complessi si sarà fatto prima di accettare questi interventi su di sé?)")
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ok, qua inizia una lunga lista di organi di cui non capisco niente... nervi ottici, bulbi olfattivi, membrana timpanica, derma, terminazioni nervose... sostituzione del midollo spinale... ci sono anche diverse cose sulla corteccia celebrale e... altre cose sul cervello... poi continua con alimentazione, respirazione e... illuminazione...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Quindi è possibile che questi soldati...?)")
                    partiDialogo.append(dialogo)
            elif tipoId == "OggettoLibreriaCastello-6":
                partiDialogo = []
                nome = "Libro (Sul conflitto)"
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Questo libro s'intitola: \"Sul conflitto\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non sono note le ragioni del conflitto e i tentativi di riappacificazione vengono sistematicamente respinti. Impossibile stabilire il dialogo. Il Nemico, di cui ci è noto ben poco, parrebbe aver insediato e colonizzato tutte le regioni circostanti la nostra. Ci è infatti impossibile l'esplorazione ad est, nord e sud. Le spedizioni verso ovest, invece, sono sempre risultate problematiche per via delle catene montuose e la fauna che le popola...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ciò che sappiamo sul Nemico sono le loro forme umanoidi e alcune delle loro tecnologie belliche. Non ci è nota la loro anatomia esatta, le loro forme di comunicazione, la loro cultura e né tantomeno i loro intenti. Sappiamo solo che vogliono combatterci...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Non si sa quando sia iniziato il conflitto. Il più vecchio reperto che ce ne testimonia l'esistenza risale a qualche migliaio di anni fa. Negli ultimi centosettant'anni (unico periodo di cui ho esperienza diretta) abbiamo perso diversi territori nonostante gli enormi sviluppi tecnologici che siamo riusciti a compiere...")
                partiDialogo.append(dialogo)
                if not (GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]):
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Centosettant'anni di esperienza diretta?!)")
                    partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Negli ultimi cinquant'anni, in particolare, gli attacchi si sono intensificati. Dopo una serie di successi della nostra difensa, hanno iniziato ad attaccare su tutti i fronti orientali contemporaneamente e in maniera massiccia. Nel momento in cui pensavamo di avere un vantaggio, ci hanno sorpreso conquistando quasi tutti gli avamposti. I pochi sopravvissuti parlano di armi esplosive tecnologicamente avanzate...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ancora nessun segnale del Costruttore, ma il suo intervento dovrebbe essere imminente...")
                partiDialogo.append(dialogo)
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(... L'intervento del... \"Costruttore\"? Che significa?)")
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Ok, quindi c'è una guerra che stiamo perdendo, chi ha scritto questo libro ha centosettant'anni e sta per intervenire un... \"Costruttore\"?)")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Che significa?)")
                    partiDialogo.append(dialogo)
        elif tipo.startswith("OggettoLibreriaCastello"):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Libri di Neil...)")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Merda...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAccantoABibliotecarioBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quindi sono tutti bloccati adesso...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Non che questi soldati non lo fossero anche prima...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostLetturaAppuntiNeilSuRatti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma, aspetta... se il tempo è bloccato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Perché tu ti muovi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E perché l'aria si sposta quando camminiamo? Non dovrebbe rimanere tutto immobile? Gli eventi non si stanno succedendo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E anche il mio corpo e i ratti di prima dovrebbero rimanere immobili. Se io mi muovo, sto tipo... facendo una successione di eventi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Se degli eventi stanno scorrendo, vuol dire che anche il tempo sta scorrendo, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Forse... forse ci sono tipo... diversi \"livelli\" temporali?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Forse c'è qualcun altro che vive in questi... momenti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmmh...<*>")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-11":
            partiDialogo = []
            nome = "Soldato con lancia"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sei tu Neil?")
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
                dialogo.append(u"(Questo non è Neil, ma almeno... è qualcuno?)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-8":
            partiDialogo = []
            nome = "Soldato con spada"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["letto6LibriCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Neil non può ancora riceverti.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quanto devo aspettare ancora?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(<*>#italic#Uff...<*> potrei leggere qualcosa nel frattempo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Entra, Neil può riceverti adesso.")
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
        elif tipoId == "OggettoFinestraCastello-0":
            partiDialogo = []
            nome = "OggettoFinestraCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                dialogo = []
                dialogo.append("tu")
                if GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"]:
                    dialogo.append(u"(È mattina...)")
                else:
                    dialogo.append(u"(Siamo parecchio in alto...)")
                partiDialogo.append(dialogo)
            else:
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"]:
        if tipoId == "Neil-0":
            partiDialogo = []
            nome = "Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bussatoPortaStudioDiNeil"]:
                nome = "Sconosciuto"
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Permesso...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Entra.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sei tu Neil?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sì, entra.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"]:
                oggettoDato = "Lista strumenti"
                avanzaStoria = True
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
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... <*>#italic#Ehm ehm...<*> allora... hai capito cos'ha di speciale questo Impo rispetto agli altri?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Agli altri?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, cioè... sono morti tutti dopo l'inquinamento della selva, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Morti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì... mi hanno detto che li hai presi tu dopo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Oh... e chi te l'ha detto?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Uhm... una... persona...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Conosci Rod?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... S-sì, ma-")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Va bene. Allora Sara, cosa richiede René in cambio dell'impo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ah... non... cioè... servono delle informazioni su una...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Servono... servono informazioni sulla guerra in corso...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"\"Servono\"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... E cosa \"serve\" in particolare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ehm... non so... tutto quello che si sa...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ne abbiamo già discusso e gli ho già mandato il manoscritto in cui descrivo la situazione.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ah... hai scritto tu quel libro?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Cosa ti serve sapere da me esattamente?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Come fai ad avere centosettant'anni?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... È questo che vuoi sapere?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, cioè... vorrei sapere tutto... tutto quello che sai tu... Vorrei poter studiare le tue ricerche.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Tutto quello che so io... vale molto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì... a-anche il mio Impo...")
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
                dialogo.append(u"... Potremmo collaborare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, collaborare...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quali sono i tuoi titoli di studio?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non... nessuno, credo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Hai detto di essere qui per conto di René...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, ma l'ho conosciuto ieri...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Però ho letto alcuni dei tuoi libri prima, mentre aspettavo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... <*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Posso comunque rendermi utile in qualche modo mentre mi metto in pari con gli studi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Conosci Rod...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sì, conosco Rod...  e faccio anche parte della sua confraternita!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Va bene.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Davvero?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sarai il nostro aggancio con Rod. Ogni tanto ti chiederò di contattarlo per commerciare con lui. A partire da oggi. Per studiare questo impo sono necessari degli strumenti, sono abbastanza sicuro che lui ce li potrà fornire.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Degli strumenti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Questa è la lista. Puoi usare la scorciatoia sulle montagne per evitare il labirinto.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoListaStrumentiDaNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Il passaggio sulle montagne lo raggiungi passando dal cancello accanto all'ingresso del labirinto, le guardie ti lasceranno passare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok, però... credo di aver bisogno di Impo per il viaggio...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... <*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... D'accordo. Sarà l'ultima volta che potrai averlo. Quando tornerai, me lo restituirai con gli strumenti, e tu avrai i miei studi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Abbiamo un accordo. Al secondo piano puoi trovare delle armi, se ne hai bisogno. Usa il piano ascensore per tornare all'ingresso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Parti adesso, così potrai tornare in giornata.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Neil, ho alcune doman-")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Abbiamo un accordo, Sara. Quando tornerai avrai tutte le tue risposte.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sara, hai gli strumenti?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... S-sì.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Ottimo. Lasciali sul tavolo.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riprodottoSuonoStrumentiSulTavoloDiNeil"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Metti gli strumenti sul tavolo, devo vedere se vanno bene.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riprodottoSuonoStrumentiSulTavoloDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Metti l'impo sul tavolo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Che cosa vuoi fargli?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Mettilo sul tavolo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tentatoDiAndarteneDaNeilConImpoPietra"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tentatoDiAndarteneDaNeilConImpoPietra"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sara, l'impoPietra.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dammi l'impoPietra dell'impo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Dimmi cosa vuoi fargli.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Devo studiarlo, Sara. Mi serve l'impoPietra.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Lo ucciderai?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... No.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Gli impo non sono esseri viventi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dammi l'impoPietra, Sara.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sdraiataSulTavoloPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Neil... cosa vuoi farmi?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConBibliotecarioPostRianimazione2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cosa volete farmi?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Niente, solo un piccolo test.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Perché sono... così?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perché l'acqua del lago ti ha corrosa. È penetrata nell'armatura e ti ha logorato l'apparato digerente, il cuore, un polmone, quasi tutti i muscoli, i bulbi oculari, i canali olfattivi e uditivi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Il cervello e il sistema nervoso sono rimasti per lo più intatti. Le ossa hanno retto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Perché non riesco muovermi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Tornerai autonoma tra poco.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Dobbiamo fare degli esperimenti adesso. Ho sviluppato nuovi apparecchi cerebrali e li dovrai testare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... No...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Avrai notato che quei libri che hai letto nella mia libreria propongono alcune teorie sulla consequenzialità degli eventi. Ebbene, una di quelle teorie si è dimostrata corretta. Gli eventi si susseguono l'un l'altro con un principio di causalità, e vengono intervallati da dei momenti di pausa con una precisa frequenza. Adesso, ciò che dovrai fare tu, è capire cos'è che scandisce quella frequenza.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Il tuo cervello ora dovrebbe essere in grado di prendere coscienza della realtà a una frequenza molto superiore rispetto alla frequenza con cui gli eventi si susseguono.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Quindi riuscirai a percepire per molto tempo tra un evento e l'altro, così da poter notare ciò che avviene più nel dettaglio. Poi tornerai per fare rapporto.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"E... perché non lo fai tu?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Perché non l'ho ancora testato su un essere umano.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... No, io... io voglio tornare come prima...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Bene, possiamo procedere.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Aspetta! René...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Impooo... va tutto bene?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Sembri a posto.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDalloStudioDiNeilConImpo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Merda... andiamocene da qui.")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDaTavoloPostBloccoTempo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Impo!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostTempoBloccato"]:
                oggettoDato = "ImpoPietra"
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Dove...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh, eccola!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh, grazie a Dio, tu sei ancora a posto!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non preoccuparti per me, sono un po'... ma forse tornerò come prima col tempo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"L'importante è che siamo vivi entrambi...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok... forse qua intorno c'è qualcosa che potrebbe farmi capire meglio cosa mi hanno fatto...")
                partiDialogo.append(dialogo)
        elif tipo == "Bibliotecario":
            partiDialogo = []
            nome = u"René"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello19PostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... René...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConNeilPostRianimazione1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... René?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"René, aiutami...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Lo stiamo facendo, Sara.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConImpoPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"René?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoBibliotecarioBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"René?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"È bloccato...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Quindi sono già...?")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Stava scrivendo qualcosa...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non si capisce molto, ma sembrano studi su Impo...)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-9":
            partiDialogo = []
            nome = "Soldato con spada"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
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
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Uh?!<*>")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sara, lascia l'impo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... S-stai lontano!")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoTavoloVuotoCastelloA-0":
            partiDialogo = []
            nome = "OggettoTavoloVuotoCastello"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
                    dialogo.append(u"(È senza energie... perché non lo sta nutrendo?!)")
                else:
                    dialogo.append(u"(Non c'è niente su questo tavolo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilPreConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ok, li metto qui...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono gli strumenti di Rod...)")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(I miei strumenti...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non c'è niente...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoTavoloVuotoCastelloB-0":
            partiDialogo = []
            nome = "OggettoTavoloVuotoCastello"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoNeilPostConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
                    dialogo.append(u"(Non c'è niente su questa parte del tavolo...)")
                else:
                    dialogo.append(u"(Non c'è niente su questo tavolo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilPostConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ok Impo... non succederà niente...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Non preoccuparti, non succederà niente...")
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non c'è niente su questa parte del tavolo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non c'è niente...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoTavoloAttrezziCastello-0":
            partiDialogo = []
            nome = "OggettoTavoloAttrezziCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È un tavolo da lavoro...)")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiNeilCastello-0":
            partiDialogo = []
            nome = "Appunti di Neil"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono degli scarabocchi di Neil...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci sono un sacco di appunti e grafici...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Progetti di Neil su dei macchinari... è pieno di formule complesse...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoPortaCastelloChiusa-0":
            partiDialogo = []
            nome = "OggettoPortaCastelloChiusa"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presaChiaveSoldatoInternoCastello20"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
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
                dialogo.append(u"(È chiuso. Quel soldato deve avere la chiave...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"]:
        if tipoId == "Neil-0":
            partiDialogo = []
            nome = "Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodNotatoPianoAscensoreAperto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Neil...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Che vuoi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Che sta succedendo qui?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non ho tempo adesso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Dov'è Sara?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Dentro.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ha ucciso metà dai miei uomini. Poi si è gettata nel lago mentre cercava di scappare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rientratoInInternoCastello21ConRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Rivoglio l'impo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Vattene, Rod.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Lei era nella confraternita, quindi è la confraternita che deve ereditarlo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Su questo potrà esprimersi lei stessa quando si sveglierà.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Cosa?!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Hai distrutto tutti gli impo che hai trovato per ricavarne del liquido energetico con cui hai inquinato mezza regione. Perché dovremmo affidare a te l'ultimo esemplare?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Questo non c'entra! Non spetta a te decidere a chi deve essere affidato. Se lo vuoi, dovrai pagarlo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... L'impo è proprietà della confraternita.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"E infatti continuerà ad appartenere a un suo membro... rimarrà dove è stato lasciato soltanto finché il suo proprietario non si sveglierà.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"LEI È MORTA!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil4"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Povero Rod. Non sai nemmeno tu se disperarti di più per le tue prospettive economiche o per quelle sentimentali.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma stai zitto, vecchio <*>#italic#trombone.<*> Non parlarmi di prospettive, ti sei rinchiuso in questo castello per decenni passando metà del tempo a pentirti di come ti sei mutilato e l'altra metà a studiare dei modi per rimediare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil5"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Mi serve, Neil.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Devo andare nel vulcano. Credo che ci sia qualcuno là dentro. Qualcuno che li fabbrica...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non serve che tu ti metta a investigare, quel fabbro agisce in autonomia. È già intervenuto in passato e interverrà nuovamente a breve, anche senza le mediazioni di un isterico ragazzino impulsivo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... C-che ne sai tu?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Vattene, Rod.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E sai per certo che vorrà aiutarci...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Lui non vuole \"aiutarci\", vuole solo mantenere il conflitto aperto e in equilibrio.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Ma queste sono faccende che non ti riguardano. Tornatene al tuo palazzo e continua la tua tranquilla e spensierata vita di sempre, Rod. Avrai il tuo compenso per l'impo e i nostri scambi per gli impoFrutti continueranno come prima.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil6"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... E Sara? Diventerà come voi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non ci sono molte alternative. Ma se può esserti di conforto, le saranno riservate condizioni privilegiate. Ho degli accordi da rispettare dopotutto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-14":
            partiDialogo = []
            nome = "Soldato con lancia"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione4"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Seguimi.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa mi avete fatto?!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["allontanatoSoldatoPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Perché...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa mi avete fatto?!")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Dove mi state portando?!")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoSpecchio-0":
            partiDialogo = []
            nome = "Specchio"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["liberatoDaiControllori"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Però sono tipo immortale come Neil adesso... certo, con un \"apparecchio cerebrale\" nel cervello mai testato prima, ma... perlomeno non sono morta... non ancora almeno... credo...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoValvolaMacchinario-0":
            partiDialogo = []
            nome = "Valvola"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non ho idea di cosa sia...)")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoCapsulaMacchinario-0":
            partiDialogo = []
            nome = "Capsula"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sembra una porta, ma non si apre...)")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoArmadioRatti-0":
            partiDialogo = []
            nome = "Ratto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRatti"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci sono degli strani ratti qua...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Alcuni si muovono! Ma... com'è possibile)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono degli strani ratti...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Deve aver testato anche su di loro l'\"apparecchio cerebrale\"...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Alcuni camminano lentamente in tondo, altri stanno sdraiati e respirano a malapena. Ma sembrano tutti molto... stanchi...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiRatti-0":
            partiDialogo = []
            nome = "Appunti di Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["creatoOggettoAppuntiRattiNeilInternoCastello21"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti di Neil su degli esperimenti su questi ratti...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(A quanto pare alcuni di questi sono vivi da più di settecento... SETTECENTO MILIARDI DI SECOLI?!)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ma come cavolo...?!)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Però accanto c'è scritto che sono nati solo qualche ora fa...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Forse... forse sta considerando anche il tempo di... adesso. Perché vivono anche mentre il tempo è bloccato...?)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Settecento miliardi di secoli in sette ore... vuol dire che io rimarrò bloccata per... per...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ok, dev'esserci un altro modo, non mi lascerebbero... non mi...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Non mi...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti di Neil su degli esperimenti su questi ratti...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(A quanto pare ha testato anche su di loro l'\"apparecchio cerebrale\" che ha messo anche a me...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiRianimazioneSara-0":
            partiDialogo = []
            nome = "Appunti di Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoQtaSoldatiCastelloPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti di Neil sul mio processo di guarigione...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Sono passate diciotto ore e il soggetto si sta comportando meglio del previsto. Di questo passo, il processo di rianimazione sarà completato in meno di due settimane...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il processo di rianimazione si è concluso leggermente in anticipo. Il soggetto ha ripreso a respirare, il battito cardiaco è regolare e l'attività cerebrale è perfettamente nella norma. L'installazione del prototipo potrà iniziare tra tre giorni...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... La fase di riposo è terminata nei tempi previsti. Procedura d'installazione del prototipo avviata...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Il soggetto ha inaspettatamente ripreso coscienza per pochi secondi durante la fase conclusiva dell'installazione: rischio di collasso del sistema elevato. I trattamenti estetici di Rod verranno sospesi fino alla conclusione dei test...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... L'installazione si è conclusa con successo, nessun elemento dell'ospite è stato danneggiato. I test sul prototipo inizieranno non appena il soggetto tornerà operativo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Quindi ero morta...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(E adesso ho un \"prototipo\" installato...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Sono appunti di Neil sul mio processo di guarigione...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(C'è scritto che sono stata rianimata con un processo durato due settimane. E poi mi è stato intallato un \"prototipo\"... credo si tratti dell'\"apparecchio cerebrale\" di cui mi parlava Neil...)")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
