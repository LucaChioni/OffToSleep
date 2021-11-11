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
    if tipoId == "OggettoQuadro-1":
        partiDialogo = []
        nome = "Quadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"Sembra una parete piena di crepe...")
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
        dialogo.append(u"Una città che si affaccia su un mare in tempesta... credo...")
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
        dialogo.append(u"Un castello con una torre imponente nel mezzo.")
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
        dialogo.append(u"Una donna triste con un vestito enorme.")
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
        dialogo.append(u"Un paesino a valle di una montagna.")
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
        dialogo.append(u"Una semplice foresta, direi...")
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
        dialogo.append(u"Un uomo nudo su una conchiglia. Quei lunghi capelli non si addicono molto al suo volto...")
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
        dialogo.append(u"Un albero dal tronco bianco in mezzo a un paesaggio macabro...")
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
        dialogo.append(u"Un vaso con dei fiori.")
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
        dialogo.append(u"Un porto con diverse barche.")
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
        dialogo.append(u"Una nave da guerra. Voglio dire, non so perché, ma dall'aspetto sembra... aggressiva.")
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
        dialogo.append(u"Un uomo fatto di frutta e verdura. Questo quadro... boh...")
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
        dialogo.append(u"Una bambina che raccoglie dei fiori.")
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
        dialogo.append(u"Pesche...")
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
        dialogo.append(u"Sembra il riflesso di un castello nell'acqua.")
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
        dialogo.append(u"Un albero in un... prato, credo... non so, l'unica cosa a fuoco è l'albero, il resto e sfocato.")
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
        dialogo.append(u"Una montagna innevata.")
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
        dialogo.append(u"Un lago all'alba. C'è una sfera luminosa sopra una montagna.")
        partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"]:
        if tipoId == "ServoLancia-3":
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
                dialogo.append(u"Ehm... ok...")
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
                dialogo.append(u"Ehi...")
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
                dialogo.append("personaggio")
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
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un sacco di libri sull'ambiente, la natura e gli animali...")
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
        elif tipoId == "OggettoLavandinoCastello-0":
            partiDialogo = []
            nome = "OggettoLavandinoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questi sistemi per portare l'acqua in casa, sono più comuni di quel che pensavo...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoGabinettoCastello-0":
            partiDialogo = []
            nome = "OggettoGabinettoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È da un po' che non vado in bagno, ma ora non ho tempo per pensare ai miei problemi digestivi.")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoVascaCastello-0":
            partiDialogo = []
            nome = "OggettoVascaCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Una vasca enorme. Chissà se anche qui c'è l'acqua riscaldata...")
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
                dialogo.append(u"(Chissà a cosa stanno pensando... tipo: \"Se mi muovo non ho fatto bene il mio lavoro\"?)")
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
                dialogo.append(u"Tu fai la guardia al tavolo?")
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
                dialogo.append(u"(Perché questi tizi non fanno niente?)")
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
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Ci si potrebbe divertire un sacco con queste guardie...)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoCaminoCastello-0":
            partiDialogo = []
            nome = "OggettoCaminoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Un camino praticamente nuovo...")
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
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E un altro vaso... ma che hanno di così bello da dover essere presenti ovunque?")
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
                dialogo.append(u"(Queste guardie sono ovunque, ma nel castello non c'è nessuno... Si sorvegliano tra loro?)")
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
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo letto è morbidissimo.")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoArmadioCastello-0":
            partiDialogo = []
            nome = "OggettoArmadioCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo armadio è vuoto")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoComodinoCastello-0":
            partiDialogo = []
            nome = "OggettoComodinoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Su questo comodino c'è solo una lanterna. I cassetti sono vuoti.")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLavandinoCastello-1":
            partiDialogo = []
            nome = "OggettoLavandinoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Anche da qui esce acqua riscaldata.")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoVascaCastello-1":
            partiDialogo = []
            nome = "OggettoVascaCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non ho tempo per farmi un bagno adesso.")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoGabinettoCastello-1":
            partiDialogo = []
            nome = "OggettoGabinettoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non sento il bisogno di andare in bagno... forse dovrei sedermi e aspettare un po', ma non ho tempo da perdere adesso.")
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
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello12"]:
        if tipoId == "ServoArco-6":
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
                dialogo.append(u"Sto per sputare sul pavimento...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Lo sto per fare... proprio su questo tappeto...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Sto caricando la saliva...")
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
                dialogo.append(u"(Forse se gli sputassi in faccia... No, meglio di no.)")
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoBarcaCastello-0":
            partiDialogo = []
            nome = "OggettoBarcaCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E un altro modellino di una barca... Neil deve esserne proprio appassionato.")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello14"]:
        if tipoId == "ServoSpada-4":
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
        if tipoId == "ServoLancia-9":
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
                dialogo.append(u"Ehi, ciao. Mi chiamo Lucy. Possiamo conoscerci se ti va...")
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
                dialogo.append(u"<*>#italic#Mh...<*>")
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
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello17"]:
        if tipoId == "ServoSpada-6":
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
                dialogo.append(u"(Forse non hanno bisogno di mangiare...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello18"]:
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
                dialogo.append(u"(La porta è aperta ma ci sono due soldati di guardia...)")
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
        elif tipoId == "OggettoLibreriaCastello-1":
            partiDialogo = []
            nome = "Libro (Sulla coscienza Vol.1 - Etica)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sulla coscienza Vol.1 - Etica\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... La cultura (di cui l'etica fa parte) si crea e si evolve negli esseri viventi quando questi crescono e fanno esperienza. Tanto più due animali sono in contatto, tanto più la loro esperienza (e quindi anche la loro cultura) è comune...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Nel momento in cui le circostanze impongono una convivenza tra animali con culture diverse, è necessario che nasca una nuova cultura, e talvolta una nuova etica, come frutto dell'unione delle precedenti. Spesso però, l'impegno nell'adattarsi a una cultura con un'etica molto differente, può richiedere sforzi che non vogliono essere accettati. Sono questi i casi in cui possono nascere scontri...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Nel pensiero di alcuni, nel momento in cui esisterà una sola cultura condivisa da tutti, sarà finalmente chiaro quale sarà la giusta etica. È scopo di questi fanatici esportare le proprie credenze presso gli altri, anche attraverso l'uso della forza...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Ponendoci come osservatori esterni a uno scontro tra due fazioni contrapposte, la domanda \"quale delle due ha ragione?\" risulta irrilevante e insensata: ognuna delle due parti è nel giusto, nel momento in cui viene giudicata attraverso la propria etica...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Non può esistere conciliazione tra culture inconciliabili. Non esiste un'etica oggettivamente giusta, e non esisterà neanche nel momento in cui ne rimarrà una: quella che risulterà vincente, dovrà la sua sopravvivenza all'aggressività dei suoi sostenitori, non alla sua oggettività.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*>")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-2":
            partiDialogo = []
            nome = "Libro (Sulla coscienza Vol.2 - Libero arbitrio)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sulla coscienza Vol.2 - Libero arbitrio\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Per discutere sul libero arbitrio è innanzitutto necessario distinguere due possibilità: la prima è quella in cui si ritiene che tutto ciò che esiste è costituito da materia; la seconda, invece, è quella in cui cosidera possibile l'esistenza di elementi non materiali, tra cui rientrerebbe l'anima, come motore di ogni essere vivente...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Decidendo di percorrere la prima ipotesi, è chiaro che non può esserci libero arbitrio: allo stesso modo in cui è possibile calcolare \"azioni\" di oggetti inanimati, sarà possibile calcolare le azioni degli esseri animati. L'unica differenza tra le due categorie rimarrebbe la presenza, nel secondo raggruppamento, della coscienza, a cui la parola \"vita\" ridurrebbe tutto il suo significato.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Percorrendo la seconda ipotesi, invece, è vero che l'anima non sarebbe governata dalle stesse leggi della materia, ma da queste leggi comunque dipenderebbe, anche se in maniera indiretta. Il comportamento degli individui, così come il loro pensiero, viene plasmato dall'esperienza che gli stessi compiono sul mondo materiale. L'anima verrebbe in questo modo influenzata e \"corrotta\" dalla materia, risultando quindi non più libera.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*> In sostanza, le cose di cui mi ha parlato René...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-3":
            partiDialogo = []
            nome = "Libro (Sulla coscienza Vol.3 - Tempo)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sulla coscienza Vol.3 - Tempo\"...")
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
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Assurdo...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-4":
            partiDialogo = []
            nome = "Libro (Sulla coscienza Vol.4 - Realtà)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sulla coscienza Vol.4 - Realtà\"...")
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
            dialogo.append(u"... In entrambi i casi la realtà viene immaginata, ma, se nel primo caso i sensi impongono dei pensieri e delle reazioni, nel secondo, la coscienza è \"libera\" di concentrarsi su ciò che più gli interessa, senza distrazioni. Una mia vecchia conoscenza direbbe: la vera libertà la si può sperimentare solo sognando.")
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
            dialogo.append(u"... Seguendo la seconda ipotesi, in cui si sostiene che la realtà è contenuta nell'immaginazione, deduciamo che è la coscienza a produrre la realtà. Ciò che sta \"fuori di noi\", sarebbe una sorta di lista di ricordi che costruiremmo attraverso l'immaginazione. E, dato che la realtà si evolve in modo deterministico, dovremmo pensare che le leggi fisiche che la governano, siano in verità i meccanismi con cui la coscienza sviluppa i sui pensieri.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Non so... sembra assurdo, ma...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-5":
            partiDialogo = []
            nome = "Libro (Sull'evoluzione)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sull'evoluzione\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... La frequenza di campionamento della realtà, da parte di un soggetto, varia al variarie della sua età. L'invecchiamento degli organi che influenzano le abilità cognitive, fa sì che la presa di coscienza degli eventi, e dei pensieri, sia sempre meno frequente...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Se a questo aggiungiamo che gli eventi, accumulati come ricordi nel cervello, vengono dimenticati sempre più rapidamente, risulterà chiaro che, invecchiando, varierà anche la percezione del tempo: il tempo passerà sempre più velocemente rispetto al passato...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Per evitare questo lento degrado, è possibile fare delle operazioni sugli organi, non solo mantenerli giovani, ma anche per potenziarli. Usando materiali che sopportano carichi di lavoro più intensi e che non si degradano nel tempo, si possono ottenere organi, che integrino quelli già esistenti o che li sostituiscano del tutto, che permettono di invertire quella tendenda \"naturale\" di percezione del tempo precedentemente descritta...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Occorre innanzitutto sostituire diverse componenti di alcuni organi sensoriali: completa sostituzione del nervo ottico e della retina, ...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, qua inizia una lunga lista di organi di cui non capisco niente... nervi ottici, bulbi olfattivi, membrana timpanica, derma, terminazioni nervose... sostituzione del midollo spinale... ci sono anche diverse cose sulla corteccia celebrale e... altre cose sul cervello...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Quindi è possibile alterare e \"potenziare\" le nostre capacità... è possibile che questi soldati... ?")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-6":
            partiDialogo = []
            nome = "Libro (Sul conflitto)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sul conflitto\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Non sono note le ragioni del conflitto e i tentativi di riappacificazione vengono sistematicamene respinti. Impossibile stabilire il dialogo. Il \"nemico\", di cui ci è noto ben poco, parrebbe aver insediato e colonizzato tutte le regioni circostanti la nostra. Ci è infatti impossibile l'esplorazione ad est, nord e sud. Le spedizioni verso ovest, invece, sono sempre risultante problematiche per via delle catene montuose e la fauna che le popola...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Ciò che sappiamo sul \"nemico\" sono le loro forme umanoidi e alcune delle loro tecnologie belliche. Non ci è nota la loro anatomia esatta, le loro forme di comunicazione, la loro cultura e i loro intenti. Sappiamo solo che vogliono combatterci...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Non si sa quando sia iniziato il conflitto. Il più vecchio reperto che ce ne testimonia l'esistenza, risale a qualche migliaio di anni fa. Negli ultimi centosettant'anni (unico periodo di cui ho esperienza diretta) abbiamo perso molti territori, nonostante gli enormi sviluppi tecnologici che siamo riusciti ad ottenere...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Centosettant'anni di esperienza diretta?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Negli ultimi cinquant'anni, in particolare, gli attacchi si sono intensificati. Dopo una serie successi della nostra difensa, hanno iniziato ad attaccare su tutti i fronti orientali contemporaneamente e in maniera massiccia. Nel momento in cui pensavamo di avere un vantaggio, ci hanno sorpreso conquistando quasi tutti gli avamposti. I pochi sopravvissuti parlano di armi esplosive tecnologicamente avanzate...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, quindi... c'è una guerra che stiamo perdendo... e chi ha scritto questo libro (Neil?) ha centosettant'anni... <*>#italic#Mmh...<*> non so quanto siano affidabili questi libri...")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"]:
        if tipoId == "ServoLancia-11":
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
                dialogo.append(u"Attento, hai un ragno sulla spalla!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oddio, è enorme! Adesso ti sta camminando sul collo...")
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
                dialogo.append(u"(Non hanno paura dei ragni.)")
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-8":
            partiDialogo = []
            nome = "Soldato con spada"
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
                dialogo.append(u"(Questo non è Neil, ma... almeno è qualcuno?!)")
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
            dialogo.append(u"Siamo parecchio in alto...")
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"]:
        if tipoId == "OggettoTavoloVuotoCastello-0":
            partiDialogo = []
            nome = "OggettoTavoloVuotoCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Su questo tavolo non c'è niente...")
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
            dialogo.append(u"È un tavolo da lavoro presumo...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiNeilCastello-0":
            partiDialogo = []
            nome = "Appunti di Neil"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ci sono un sacco di appunti e diagrammi disorganizzati...")
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-7":
            partiDialogo = []
            nome = "Libro (Sugli Impo)"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo libro s'intitola: \"Sugli Impo\"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... ")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Mmh...<*>")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
