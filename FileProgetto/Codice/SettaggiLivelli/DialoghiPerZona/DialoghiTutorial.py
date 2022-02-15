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
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoSara1"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Per muoverti usa i tasti <*>#bold#W,<*> <*>#bold#A,<*> <*>#bold#S<*> e <*>#bold#D<*> della tastiera, la <*>#bold#Croce direzionale<*> del controller oppure, utilizzando il mouse, clicca con il tasto <*>#bold#Sinistro<*> sulla casella verso cui vuoi spostarti.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Muoviti verso il baule davanti a te e prova ad aprirlo utilizzando il tasto <*>#bold#SPAZIO<*> della tastiera, la <*>#bold#Croce<*> del controller oppure cliccandoci sopra con il tasto <*>#bold#Sinistro<*> del mouse.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Hai trovato una pozione. Puoi usarla dal menu a cui puoi accedere premendo <*>#bold#Esc<*> sulla tastiera, <*>#bold#Start<*> del controller o il tasto <*>#bold#Centrale<*> del mouse.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Dal menu potrai accedere anche a \"Equipaggiamento\", dove potrai selezionare armi, protezioni e accessori da equipaggiarti.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Davanti a te c'è un nemico. Per vedere le sue informazioni, passa alla modalità interazione (premendo il tasto <*>#bold#E<*> della tastiera, <*>#bold#Quadrato<*> del controller o il tasto <*>#bold#Destro<*> del mouse) e inquadralo spostando il puntatore sulla sua casella.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Una volta inquadrato, puoi selezionarlo e attaccarlo premendo <*>#bold#SPAZIO<*> sulla tastiera, la <*>#bold#Croce<*> del controller o il tasto <*>#bold#Sinistro<*> del mouse (dato che al momento non hai frecce, puoi attaccarlo solo da vicino). <br> Per deselezionare l'obiettivo, premi <*>#bold#Q<*> sulla tastiera, <*>#bold#Cerchio<*> del controller o il tasto <*>#bold#Destro<*> del mouse sul suo stato (in alto a sinistra dello schermo).")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Attenzione: se ci sono dei nemici presenti nella stanza, premendo <*>#bold#Esc,<*> <*>#bold#Start<*> o il tasto <*>#bold#Centrale<*> del mouse, viene aperto un menu rapido che permette di compiere meno operazioni ripetto al menu normale.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialBattaglia"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Fai attenzione a quel pipistrello: è velenoso e attacca a distanza!")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Se vuoi ingaggiarlo, assicurati di poterlo attaccare a distanza prima che ti possa vedere. In quel baule potrebbe esserci qualcosa che fa al caso tuo...")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append("Oppure puoi semplicemente evitarlo aspettando il momento giusto per passare. Per saltare un turno, premi il tasto <*>#bold#0<*> della tastiera, <*>#bold#Select<*> del controller oppure clicca con il tasto <*>#bold#Sinistro<*> del mouse sulla relativa icona in alto a destra dello schermo.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara1"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"È possibile richiudere le porte utilizzando la modalità interazione.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"In modalità interazione, le caselle fuori dal tuo campo visivo vengono oscurate.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Inquadrando un nemico, inoltre, verranno oscurate in rosso le caselle che lui non riesce a vedere. Quando un nemico ti vede, l'occhio in alto a destra dello schermo si aprirà. Viceversa, quando sei fuori dal campo visivo di tutti i nemici, l'occhio sarà chiuso.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Dato che al momento sei disarmato, non ti conviene affrontare i nemici a viso aperto. Prova a passare senza farti vedere.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialCampoVisivo"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"In modalità interazione, cliccando su te stesso assumerai una posizione difensiva che ti permetterà di subire meno danni. Facendolo in un luogo sicuro, invece, ti permetterà di riposare e recuperare tutti i <*>#italic#Pv.<*>")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Assumendo la posizione difensiva in luoghi sicuri, recupererai tutti i <*>#italic#Pv.<*>")
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["introduzioneImpoDalBibliotecario"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Per attivare e disattivare la ImpoPietra usa il tasto <*>#bold#SHIFT<*> della tastiera, il <*>#bold#Triangolo<*> del controller oppure clicca sulla sua icona in alto a destra dello schermo con il tasto <*>#bold#Sinistro<*> del mouse.")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Nel menu è apparsa la voce \"Setta Impo\". Selezionala per gestire gli equipaggiamenti di Impo. <br> Attenzione: è possibile accedervi solo se Impo si trova in una casella raggiungibile da Sara.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaBibliotecaDirettoVersoNeil"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Cliccando su Impo in modalità interazione, potrai vedere la sua prossima mossa. <br> Ma fai attenzione: il movimento di Sara può interferire e annullare le condizioni prese in considerazione nella previsione.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoSelvaArida"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Durante la battaglia puoi usare gli ImpoFrutti solo se Impo è in una casella adiacente a quella di Sara. Per usarli fuori dal combattimento invece è sufficiente che Impo sia in una casella raggiungibile.")
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostRisoluzioneEnigma"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(u"Finché sei nel labirinto, premendo il tasto <*>#bold#Esc<*> della tastiera, <*>#bold#Start<*> del controller o il tasto <*>#bold#Centrale<*> del mouse, andrai direttamente alla mappa. Da lì potrai spostarti normalmente nel menu.")
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
