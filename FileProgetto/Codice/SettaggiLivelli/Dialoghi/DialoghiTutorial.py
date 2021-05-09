# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "Tutorial"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoLucy1"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Per muoverti usa i tasti <*>#bold#W<*>, <*>#bold#A<*>, <*>#bold#S<*> e <*>#bold#D<*> della tastiera, la <*>#bold#Croce direzionale<*> del controller oppure, utilizzando il mouse, clicca con il tasto <*>#bold#Sinistro<*> sulla casella verso cui vuoi spostarti.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Muoviti verso il baule davanti a te e prova ad aprirlo utilizzando il tasto <*>#bold#SPAZIO<*> sulla tastiera, la <*>#bold#Croce<*> sul controller oppure cliccandoci sopra con il tasto <*>#bold#Sinistro<*> del mouse.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Hai trovato una pozione. Puoi usarla dal menu a cui puoi accedere premendo <*>#bold#Esc<*> sulla tastiera, <*>#bold#Start<*> sul controller o il tasto <*>#bold#Centrale<*> del mouse.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Dal menu potrai anche accedere a \"Equipaggiamento\" dove potrai selezionare armi, protezioni e accessori da equipaggiarti.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Davanti a te c'è un nemico. Per vedere le sue informazioni passa alla modalità interazione (premi il tasto <*>#bold#E<*> della tastiera, <*>#bold#Quadrato<*> del controller o il tasto <*>#bold#Destro<*> del mouse) e inquadralo spostando il puntatore sulla sua casella.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Una volta inquadrato puoi selezionarlo e attaccarlo premendo <*>#bold#SPAZIO<*> sulla tastiera, la <*>#bold#Croce<*> sul controller o il tasto <*>#bold#Sinistro<*> del mouse (dato che al momento non hai frecce, puoi attaccarlo solo da vicino).")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Attenzione: se ci sono dei nemici presenti nella stanza, premendo <*>#bold#Esc<*>, <*>#bold#Start<*> o il tasto <*>#bold#Centrale<*> del mouse, viene aperto un menu rapido che permette di compiere meno operazioni ripetto al menu normale.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialBattaglia"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Fai attenzione a quel pipistrello: è velenoso ed attacca a distanza!")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Se vuoi ingaggiarlo assicurati di poterlo attaccare a distanza prima che ti possa vedere.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("In quel baule potrebbe esserci qualcosa che fa al caso tuo...")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"È possibile richiudere le porte utilizzando la modalità interazione.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"In modalità interazione le caselle fuori dal tuo campo visivo vengono oscurate.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Inquadrando un nemico inoltre compaiono delle crocette rosse e nere che contrassegnano le caselle che il nemico non riesce a vedere. Quando un nemico ti vede l'occhio in alto a destra nello schermo si aprirà. Viceversa, quando sei fuori dal campo visivo di tutti i nemici, l'occhio sarà chiuso.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Dato che al momento sei disarmato non ti conviene affrontare i nemici a viso aperto: prova a passare senza farti vedere!")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialCampoVisivo"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"In modalità interazione, cliccando su te stesso assumerai una posizione difensiva che ti permetterà di subire meno danni e di recuperare qualche <*>#italic#Pv.<*>")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Usala anche fuori dal combattimento per evitare di sprecare pozioni!")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("La mappa e il diario si possono aprire dal menu cliccando sulle relative voci.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"È possibile accedere alla mappa anche dal menu rapido di battaglia.")
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
