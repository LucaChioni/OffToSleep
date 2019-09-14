# -*- coding: utf-8 -*-

from MenuG2 import *
from EnvPrintG2 import *
from MovNemiciRobG2 import *
from AnimazioniG2 import *


# freccetta invisibile
pygame.mouse.set_visible(False)


def gameloop():
    inizio = True
    while True:
        if inizio:
            raffredda = -1
            autoRic1 = -1
            autoRic2 = -1
            spingiColco = False
            apriChiudiPorta = [False, 0, 0]
            apriCofanetto = [False, 0, 0]
            stanzaVecchia = 0
            chiamarob = True
            tesoro = -1
            apriocchio = False
            mostristanze = []
            sposta = False
            nmost = 0
            agg = 0
            primopas = False
            tastotemp = 5
            tastotempfps = 5
            tastop = 0
            startf = False
            aumentoliv = False
            primopasso = True
            contaesca = 0
            xesca = 0
            yesca = 0
            creaesca = False
            vitaesca = []
            premuti = 0
            contattogg = 0
            attacco = 0
            # difesa e' grigio perche' viene impostato a ogni ciclo
            difesa = 0
            # 1->d , 2->a , 3->w , 4->s
            npers = 4
            # 1->d , 2->a , 3->s , 4->w
            nrob = 3
            nx = 0
            ny = 0
            pers = perss
            robot = robos
            dati, porteini, portefin, cofaniini, cofanifin = menu()
            print (dati)

            # creare vettore porte -> porte[stanza, x, y, True/False, ...]
            porte = []
            tutteporte = []
            i = porteini
            while i <= portefin:
                tutteporte.append(dati[i])
                tutteporte.append(dati[i + 1])
                tutteporte.append(dati[i + 2])
                tutteporte.append(dati[i + 3])
                i = i + 4

            # creare vettore cofanetti -> cofanetti[stanza, x, y, True/False, ...]
            cofanetti = []
            tutticofanetti = []
            i = cofaniini
            while i <= cofanifin:
                tutticofanetti.append(dati[i])
                tutticofanetti.append(dati[i + 1])
                tutticofanetti.append(dati[i + 2])
                tutticofanetti.append(dati[i + 3])
                i = i + 4

            x = dati[2]
            y = dati[3]
            vx = x
            vy = y
            rx = x
            ry = y
            vrx = vx
            vry = vy
            nemicoa = 0
            mxa = 0
            mya = 0
            mxav = 0
            myav = 0
            nemicob = 0
            mxb = 0
            myb = 0
            mxbv = 0
            mybv = 0
            nemicoc = 0
            mxc = 0
            myc = 0
            mxcv = 0
            mycv = 0
            nemicod = 0
            mxd = 0
            myd = 0
            mxdv = 0
            mydv = 0
            nemicoe = 0
            mxe = 0
            mye = 0
            mxev = 0
            myev = 0
            nemicof = 0
            mxf = 0
            myf = 0
            mxfv = 0
            myfv = 0
            nemicog = 0
            mxg = 0
            myg = 0
            mxgv = 0
            mygv = 0
            nemicoh = 0
            mxh = 0
            myh = 0
            mxhv = 0
            myhv = 0
            nemicoi = 0
            mxi = 0
            myi = 0
            mxiv = 0
            myiv = 0
            nemicol = 0
            mxl = 0
            myl = 0
            mxlv = 0
            mylv = 0
            carim = True
            cambiosta = True

        # caricare gli oggetti
        if carim:
            premuti = 0
            contattogg = 0
            if pers == persw:
                agg = 1
            if pers == persa:
                agg = 2
            if pers == perss:
                agg = 3
            if pers == persd:
                agg = 4
            # stanza
            stanzaa = pygame.image.load("Immagini\Paesaggi\Stanza%ia.png" % dati[1]).convert()
            stanzaa = pygame.transform.scale(stanzaa, (gsx, gsy))
            sfondinoa = pygame.image.load("Immagini\Paesaggi\Sfondino%ia.png" % dati[1]).convert()
            sfondinoa = pygame.transform.scale(sfondinoa, (gpx, gpy))
            sfondinob = pygame.image.load("Immagini\Paesaggi\Sfondino%ib.png" % dati[1]).convert()
            sfondinob = pygame.transform.scale(sfondinob, (gpx, gpy))
            sfondinoc = pygame.image.load("Immagini\Paesaggi\Sfondino%ic.png" % dati[1]).convert()
            sfondinoc = pygame.transform.scale(sfondinoc, (gpx, gpy))
            portaVert = pygame.image.load("Immagini\Paesaggi\PortaV%i.png" % dati[1])
            portaVert = pygame.transform.scale(portaVert, (gpx, gpy))
            portaOriz = pygame.image.load("Immagini\Paesaggi\PortaO%i.png" % dati[1])
            portaOriz = pygame.transform.scale(portaOriz, (gpx, gpy))

            # mostri
            if dati[1] == 1 and cambiosta:
                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 2:
                        npers = 4
                        nrob = 3
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        pers = perss
                        robot = robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

                # formalita'
                if True:
                    mostroaw = 0
                    mostroaa = 0
                    mostroas = 0
                    mostroad = 0
                    mostrobw = 0
                    mostroba = 0
                    mostrobs = 0
                    mostrobd = 0
                    mostrocw = 0
                    mostroca = 0
                    mostrocs = 0
                    mostrocd = 0
                    mostrodw = 0
                    mostroda = 0
                    mostrods = 0
                    mostrodd = 0
                    mostroew = 0
                    mostroea = 0
                    mostroes = 0
                    mostroed = 0
                    mostrofw = 0
                    mostrofa = 0
                    mostrofs = 0
                    mostrofd = 0
                    mostrogw = 0
                    mostroga = 0
                    mostrogs = 0
                    mostrogd = 0
                    mostrohw = 0
                    mostroha = 0
                    mostrohs = 0
                    mostrohd = 0
                    mostroiw = 0
                    mostroia = 0
                    mostrois = 0
                    mostroid = 0
                    mostrolw = 0
                    mostrola = 0
                    mostrols = 0
                    mostrold = 0

                giavisitata = False

                nmost = 5
                mxa = gsx // 32 * 29
                mya = gsy // 18 * 15
                mxb = gsx // 32 * 3
                myb = gsy // 18 * 3
                mxc = gsx // 32 * 8
                myc = gsy // 18 * 7
                mxd = gsx // 32 * 15
                myd = gsy // 18 * 14
                mxe = gsx // 32 * 23
                mye = gsy // 18 * 4
                mxf = gsx // 32 * 0
                myf = gsy // 18 * 0
                mxg = gsx // 32 * 0
                myg = gsy // 18 * 0
                mxh = gsx // 32 * 0
                myh = gsy // 18 * 0
                mxi = gsx // 32 * 0
                myi = gsy // 18 * 0
                mxl = gsx // 32 * 0
                myl = gsy // 18 * 0
                pvmatot = 16000
                pvmbtot = 50
                pvmctot = 20
                pvmdtot = 50
                pvmetot = 20
                pvmftot = 0
                pvmgtot = 0
                pvmhtot = 0
                pvmitot = 0
                pvmltot = 0
                tipoa = "orco"
                tipob = "orco"
                tipoc = "pipistrello"
                tipod = "orco"
                tipoe = "pipistrello"
                tipof = ""
                tipog = ""
                tipoh = ""
                tipoi = ""
                tipol = ""
                espma = 10
                espmb = 10
                espmc = 5
                espmd = 10
                espme = 5
                espmf = 0
                espmg = 0
                espmh = 0
                espmi = 0
                espml = 0

                mostroaw = pygame.image.load("Immagini\Mostri\Orcow.png")
                mostroaw = pygame.transform.scale(mostroaw, (gpx, gpy))
                mostroaa = pygame.image.load("Immagini\Mostri\Orcoa.png")
                mostroaa = pygame.transform.scale(mostroaa, (gpx, gpy))
                mostroas = pygame.image.load("Immagini\Mostri\Orcos.png")
                mostroas = pygame.transform.scale(mostroas, (gpx, gpy))
                mostroad = pygame.image.load("Immagini\Mostri\Orcod.png")
                mostroad = pygame.transform.scale(mostroad, (gpx, gpy))

                mostrobw = pygame.image.load("Immagini\Mostri\Orcow.png")
                mostrobw = pygame.transform.scale(mostrobw, (gpx, gpy))
                mostroba = pygame.image.load("Immagini\Mostri\Orcoa.png")
                mostroba = pygame.transform.scale(mostroba, (gpx, gpy))
                mostrobs = pygame.image.load("Immagini\Mostri\Orcos.png")
                mostrobs = pygame.transform.scale(mostrobs, (gpx, gpy))
                mostrobd = pygame.image.load("Immagini\Mostri\Orcod.png")
                mostrobd = pygame.transform.scale(mostrobd, (gpx, gpy))

                mostrocw = pygame.image.load("Immagini\Mostri\Pipistrellow.png")
                mostrocw = pygame.transform.scale(mostrocw, (gpx, gpy))
                mostroca = pygame.image.load("Immagini\Mostri\Pipistrelloa.png")
                mostroca = pygame.transform.scale(mostroca, (gpx, gpy))
                mostrocs = pygame.image.load("Immagini\Mostri\Pipistrellos.png")
                mostrocs = pygame.transform.scale(mostrocs, (gpx, gpy))
                mostrocd = pygame.image.load("Immagini\Mostri\Pipistrellod.png")
                mostrocd = pygame.transform.scale(mostrocd, (gpx, gpy))

                mostrodw = pygame.image.load("Immagini\Mostri\Orcow.png")
                mostrodw = pygame.transform.scale(mostrodw, (gpx, gpy))
                mostroda = pygame.image.load("Immagini\Mostri\Orcoa.png")
                mostroda = pygame.transform.scale(mostroda, (gpx, gpy))
                mostrods = pygame.image.load("Immagini\Mostri\Orcos.png")
                mostrods = pygame.transform.scale(mostrods, (gpx, gpy))
                mostrodd = pygame.image.load("Immagini\Mostri\Orcod.png")
                mostrodd = pygame.transform.scale(mostrodd, (gpx, gpy))

                mostroew = pygame.image.load("Immagini\Mostri\Pipistrellow.png")
                mostroew = pygame.transform.scale(mostroew, (gpx, gpy))
                mostroea = pygame.image.load("Immagini\Mostri\Pipistrelloa.png")
                mostroea = pygame.transform.scale(mostroea, (gpx, gpy))
                mostroes = pygame.image.load("Immagini\Mostri\Pipistrellos.png")
                mostroes = pygame.transform.scale(mostroes, (gpx, gpy))
                mostroed = pygame.image.load("Immagini\Mostri\Pipistrellod.png")
                mostroed = pygame.transform.scale(mostroed, (gpx, gpy))
                # mostri in piu'
                '''mostrofw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrofw = pygame.transform.scale(mostrofw, (gpx, gpy))
                mostrofa = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostrofa = pygame.transform.scale(mostrofa, (gpx, gpy))
                mostrofs = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrofs = pygame.transform.scale(mostrofs, (gpx, gpy))
                mostrofd = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrofd = pygame.transform.scale(mostrofd, (gpx, gpy))

                mostrogw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrogw = pygame.transform.scale(mostrogw, (gpx, gpy))
                mostroga = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostroga = pygame.transform.scale(mostroga, (gpx, gpy))
                mostrogs = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrogs = pygame.transform.scale(mostrogs, (gpx, gpy))
                mostrogd = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrogd = pygame.transform.scale(mostrogd, (gpx, gpy))

                mostrohw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrohw = pygame.transform.scale(mostrohw, (gpx, gpy))
                mostroha = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostroha = pygame.transform.scale(mostroha, (gpx, gpy))
                mostrohs = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrohs = pygame.transform.scale(mostrohs, (gpx, gpy))
                mostrohd = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrohd = pygame.transform.scale(mostrohd, (gpx, gpy))

                mostroiw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostroiw = pygame.transform.scale(mostroiw, (gpx, gpy))
                mostroia = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostroia = pygame.transform.scale(mostroia, (gpx, gpy))
                mostrois = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrois = pygame.transform.scale(mostrois, (gpx, gpy))
                mostroid = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostroid = pygame.transform.scale(mostroid, (gpx, gpy))

                mostrolw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrolw = pygame.transform.scale(mostrolw, (gpx, gpy))
                mostrola = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostrola = pygame.transform.scale(mostrola, (gpx, gpy))
                mostrols = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrols = pygame.transform.scale(mostrols, (gpx, gpy))
                mostrold = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrold = pygame.transform.scale(mostrold, (gpx, gpy))'''

                nemicoa = mostroaw
                nemicob = mostroba
                nemicoc = mostrocd
                nemicod = mostrods
                nemicoe = mostroed
                nemicof = 0
                nemicog = 0
                nemicoh = 0
                nemicoi = 0
                nemicol = 0

                # mostristanze: id stanza, mostroa, mostrob, ... , mostrol, (rinizia per tutte le stanze visitate)
                if len(mostristanze) - 1 >= 11:
                    i = 0
                    while i <= len(mostristanze) - 1:
                        if mostristanze[i] == dati[1]:
                            giavisitata = True
                            nmost = 10
                            j = i + 1
                            while j <= i + 10:
                                if not mostristanze[j]:
                                    if j == i + 1:
                                        mostroaw = 0
                                        mostroaa = 0
                                        mostroas = 0
                                        mostroad = 0
                                        mxa = gsx // 32 * 0
                                        mya = gsy // 18 * 0
                                        pvmatot = 0
                                        tipoa = ""
                                        espma = 0
                                        nemicoa = 0
                                        nmost = nmost - 1
                                    if j == i + 2:
                                        mostrobw = 0
                                        mostroba = 0
                                        mostrobs = 0
                                        mostrobd = 0
                                        mxb = gsx // 32 * 0
                                        myb = gsy // 18 * 0
                                        pvmbtot = 0
                                        tipob = ""
                                        espmb = 0
                                        nemicob = 0
                                        nmost = nmost - 1
                                    if j == i + 3:
                                        mostrocw = 0
                                        mostroca = 0
                                        mostrocs = 0
                                        mostrocd = 0
                                        mxc = gsx // 32 * 0
                                        myc = gsy // 18 * 0
                                        pvmctot = 0
                                        tipoc = ""
                                        espmc = 0
                                        nemicoc = 0
                                        nmost = nmost - 1
                                    if j == i + 4:
                                        mostrodw = 0
                                        mostroda = 0
                                        mostrods = 0
                                        mostrodd = 0
                                        mxd = gsx // 32 * 0
                                        myd = gsy // 18 * 0
                                        pvmdtot = 0
                                        tipod = ""
                                        espmd = 0
                                        nemicod = 0
                                        nmost = nmost - 1
                                    if j == i + 5:
                                        mostroew = 0
                                        mostroea = 0
                                        mostroes = 0
                                        mostroed = 0
                                        mxe = gsx // 32 * 0
                                        mye = gsy // 18 * 0
                                        pvmetot = 0
                                        tipoe = ""
                                        espme = 0
                                        nemicoe = 0
                                        nmost = nmost - 1
                                    if j == i + 6:
                                        mostrofw = 0
                                        mostrofa = 0
                                        mostrofs = 0
                                        mostrofd = 0
                                        mxf = gsx // 32 * 0
                                        myf = gsy // 18 * 0
                                        pvmftot = 0
                                        tipof = ""
                                        espmf = 0
                                        nemicof = 0
                                        nmost = nmost - 1
                                    if j == i + 7:
                                        mostrogw = 0
                                        mostroga = 0
                                        mostrogs = 0
                                        mostrogd = 0
                                        mxg = gsx // 32 * 0
                                        myg = gsy // 18 * 0
                                        pvmgtot = 0
                                        tipog = ""
                                        espmg = 0
                                        nemicog = 0
                                        nmost = nmost - 1
                                    if j == i + 8:
                                        mostrohw = 0
                                        mostroha = 0
                                        mostrohs = 0
                                        mostrohd = 0
                                        mxh = gsx // 32 * 0
                                        myh = gsy // 18 * 0
                                        pvmhtot = 0
                                        tipoh = ""
                                        espmh = 0
                                        nemicoh = 0
                                        nmost = nmost - 1
                                    if j == i + 9:
                                        mostroiw = 0
                                        mostroia = 0
                                        mostrois = 0
                                        mostroid = 0
                                        mxi = gsx // 32 * 0
                                        myi = gsy // 18 * 0
                                        pvmitot = 0
                                        tipoi = ""
                                        espmi = 0
                                        nemicoi = 0
                                        nmost = nmost - 1
                                    if j == i + 10:
                                        mostrolw = 0
                                        mostrola = 0
                                        mostrols = 0
                                        mostrold = 0
                                        mxl = gsx // 32 * 0
                                        myl = gsy // 18 * 0
                                        pvmltot = 0
                                        tipol = ""
                                        espml = 0
                                        nemicol = 0
                                        nmost = nmost - 1
                                j = j + 1
                        i = i + 11

                # aggiorna la stanza come "visitata"
                if not giavisitata:
                    mostristanze.append(dati[1])
                    i = 1
                    while i <= nmost:
                        mostristanze.append(True)
                        i = i + 1
                    i = nmost + 1
                    while i <= 10:
                        mostristanze.append(False)
                        i = i + 1

                muovirob = 0
                muovimosta = 0
                muovimostb = 0
                muovimostc = 0
                muovimostd = 0
                muovimoste = 0
                muovimostf = 0
                muovimostg = 0
                muovimosth = 0
                muovimosti = 0
                muovimostl = 0
                mxav = mxa
                myav = mya
                mxbv = mxb
                mybv = myb
                mxcv = mxc
                mycv = myc
                mxdv = mxd
                mydv = myd
                mxev = mxe
                myev = mye
                mxfv = mxf
                myfv = myf
                mxgv = mxg
                mygv = myg
                mxhv = mxh
                myhv = myh
                mxiv = mxi
                myiv = myi
                mxlv = mxl
                mylv = myl
                pvma = pvmatot
                pvmb = pvmbtot
                pvmc = pvmctot
                pvmd = pvmdtot
                pvme = pvmetot
                pvmf = pvmftot
                pvmg = pvmgtot
                pvmh = pvmhtot
                pvmi = pvmitot
                pvml = pvmltot
                # 1:veleno / 2:lentezza / 3:veleno-lentezza
                statoma = 0
                statomb = 0
                statomc = 0
                statomd = 0
                statome = 0
                statomf = 0
                statomg = 0
                statomh = 0
                statomi = 0
                statoml = 0
                mortoa = 0
                mortob = 0
                mortoc = 0
                mortod = 0
                mortoe = 0
                mortof = 0
                mortog = 0
                mortoh = 0
                mortoi = 0
                mortol = 0
                vistoa = False
                vistob = False
                vistoc = False
                vistod = False
                vistoe = False
                vistof = False
                vistog = False
                vistoh = False
                vistoi = False
                vistol = False
                raggiovistaa = 0
                raggiovistab = 0
                raggiovistac = 0
                raggiovistad = 0
                raggiovistae = 0
                raggiovistaf = 0
                raggiovistag = 0
                raggiovistah = 0
                raggiovistai = 0
                raggiovistal = 0
            if dati[1] == 2 and cambiosta:
                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    if stanzaVecchia == 1:
                        npers = 4
                        nrob = 3
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        pers = perss
                        robot = robos
                        agg = 3
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y

                # formalita'
                if True:
                    mostroaw = 0
                    mostroaa = 0
                    mostroas = 0
                    mostroad = 0
                    mostrobw = 0
                    mostroba = 0
                    mostrobs = 0
                    mostrobd = 0
                    mostrocw = 0
                    mostroca = 0
                    mostrocs = 0
                    mostrocd = 0
                    mostrodw = 0
                    mostroda = 0
                    mostrods = 0
                    mostrodd = 0
                    mostroew = 0
                    mostroea = 0
                    mostroes = 0
                    mostroed = 0
                    mostrofw = 0
                    mostrofa = 0
                    mostrofs = 0
                    mostrofd = 0
                    mostrogw = 0
                    mostroga = 0
                    mostrogs = 0
                    mostrogd = 0
                    mostrohw = 0
                    mostroha = 0
                    mostrohs = 0
                    mostrohd = 0
                    mostroiw = 0
                    mostroia = 0
                    mostrois = 0
                    mostroid = 0
                    mostrolw = 0
                    mostrola = 0
                    mostrols = 0
                    mostrold = 0

                giavisitata = False

                nmost = 5
                mxa = gsx // 32 * 29
                mya = gsy // 18 * 15
                mxb = gsx // 32 * 0
                myb = gsy // 18 * 0
                mxc = gsx // 32 * 0
                myc = gsy // 18 * 0
                mxd = gsx // 32 * 0
                myd = gsy // 18 * 0
                mxe = gsx // 32 * 0
                mye = gsy // 18 * 0
                mxf = gsx // 32 * 0
                myf = gsy // 18 * 0
                mxg = gsx // 32 * 0
                myg = gsy // 18 * 0
                mxh = gsx // 32 * 0
                myh = gsy // 18 * 0
                mxi = gsx // 32 * 0
                myi = gsy // 18 * 0
                mxl = gsx // 32 * 0
                myl = gsy // 18 * 0
                pvmatot = 50
                pvmbtot = 0
                pvmctot = 0
                pvmdtot = 0
                pvmetot = 0
                pvmftot = 0
                pvmgtot = 0
                pvmhtot = 0
                pvmitot = 0
                pvmltot = 0
                tipoa = "orco"
                tipob = ""
                tipoc = ""
                tipod = ""
                tipoe = ""
                tipof = ""
                tipog = ""
                tipoh = ""
                tipoi = ""
                tipol = ""
                espma = 10
                espmb = 0
                espmc = 0
                espmd = 0
                espme = 0
                espmf = 0
                espmg = 0
                espmh = 0
                espmi = 0
                espml = 0

                mostroaw = pygame.image.load("Immagini\Mostri\Orcow.png")
                mostroaw = pygame.transform.scale(mostroaw, (gpx, gpy))
                mostroaa = pygame.image.load("Immagini\Mostri\Orcoa.png")
                mostroaa = pygame.transform.scale(mostroaa, (gpx, gpy))
                mostroas = pygame.image.load("Immagini\Mostri\Orcos.png")
                mostroas = pygame.transform.scale(mostroas, (gpx, gpy))
                mostroad = pygame.image.load("Immagini\Mostri\Orcod.png")
                mostroad = pygame.transform.scale(mostroad, (gpx, gpy))

                # mostri in piu'
                '''mostrobw = pygame.image.load("Immagini\Mostri\Orcow.png")
                mostrobw = pygame.transform.scale(mostrobw, (gpx, gpy))
                mostroba = pygame.image.load("Immagini\Mostri\Orcoa.png")
                mostroba = pygame.transform.scale(mostroba, (gpx, gpy))
                mostrobs = pygame.image.load("Immagini\Mostri\Orcos.png")
                mostrobs = pygame.transform.scale(mostrobs, (gpx, gpy))
                mostrobd = pygame.image.load("Immagini\Mostri\Orcod.png")
                mostrobd = pygame.transform.scale(mostrobd, (gpx, gpy))

                mostrocw = pygame.image.load("Immagini\Mostri\Pipistrellow.png")
                mostrocw = pygame.transform.scale(mostrocw, (gpx, gpy))
                mostroca = pygame.image.load("Immagini\Mostri\Pipistrelloa.png")
                mostroca = pygame.transform.scale(mostroca, (gpx, gpy))
                mostrocs = pygame.image.load("Immagini\Mostri\Pipistrellos.png")
                mostrocs = pygame.transform.scale(mostrocs, (gpx, gpy))
                mostrocd = pygame.image.load("Immagini\Mostri\Pipistrellod.png")
                mostrocd = pygame.transform.scale(mostrocd, (gpx, gpy))

                mostrodw = pygame.image.load("Immagini\Mostri\Orcow.png")
                mostrodw = pygame.transform.scale(mostrodw, (gpx, gpy))
                mostroda = pygame.image.load("Immagini\Mostri\Orcoa.png")
                mostroda = pygame.transform.scale(mostroda, (gpx, gpy))
                mostrods = pygame.image.load("Immagini\Mostri\Orcos.png")
                mostrods = pygame.transform.scale(mostrods, (gpx, gpy))
                mostrodd = pygame.image.load("Immagini\Mostri\Orcod.png")
                mostrodd = pygame.transform.scale(mostrodd, (gpx, gpy))

                mostroew = pygame.image.load("Immagini\Mostri\Pipistrellow.png")
                mostroew = pygame.transform.scale(mostroew, (gpx, gpy))
                mostroea = pygame.image.load("Immagini\Mostri\Pipistrelloa.png")
                mostroea = pygame.transform.scale(mostroea, (gpx, gpy))
                mostroes = pygame.image.load("Immagini\Mostri\Pipistrellos.png")
                mostroes = pygame.transform.scale(mostroes, (gpx, gpy))
                mostroed = pygame.image.load("Immagini\Mostri\Pipistrellod.png")
                mostroed = pygame.transform.scale(mostroed, (gpx, gpy))

                mostrofw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrofw = pygame.transform.scale(mostrofw, (gpx, gpy))
                mostrofa = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostrofa = pygame.transform.scale(mostrofa, (gpx, gpy))
                mostrofs = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrofs = pygame.transform.scale(mostrofs, (gpx, gpy))
                mostrofd = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrofd = pygame.transform.scale(mostrofd, (gpx, gpy))

                mostrogw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrogw = pygame.transform.scale(mostrogw, (gpx, gpy))
                mostroga = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostroga = pygame.transform.scale(mostroga, (gpx, gpy))
                mostrogs = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrogs = pygame.transform.scale(mostrogs, (gpx, gpy))
                mostrogd = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrogd = pygame.transform.scale(mostrogd, (gpx, gpy))

                mostrohw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrohw = pygame.transform.scale(mostrohw, (gpx, gpy))
                mostroha = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostroha = pygame.transform.scale(mostroha, (gpx, gpy))
                mostrohs = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrohs = pygame.transform.scale(mostrohs, (gpx, gpy))
                mostrohd = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrohd = pygame.transform.scale(mostrohd, (gpx, gpy))

                mostroiw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostroiw = pygame.transform.scale(mostroiw, (gpx, gpy))
                mostroia = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostroia = pygame.transform.scale(mostroia, (gpx, gpy))
                mostrois = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrois = pygame.transform.scale(mostrois, (gpx, gpy))
                mostroid = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostroid = pygame.transform.scale(mostroid, (gpx, gpy))

                mostrolw = pygame.image.load("Immagini\Mostri\Mostro1w.png")
                mostrolw = pygame.transform.scale(mostrolw, (gpx, gpy))
                mostrola = pygame.image.load("Immagini\Mostri\Mostro1a.png")
                mostrola = pygame.transform.scale(mostrola, (gpx, gpy))
                mostrols = pygame.image.load("Immagini\Mostri\Mostro1s.png")
                mostrols = pygame.transform.scale(mostrols, (gpx, gpy))
                mostrold = pygame.image.load("Immagini\Mostri\Mostro1d.png")
                mostrold = pygame.transform.scale(mostrold, (gpx, gpy))'''

                nemicoa = mostroaw
                nemicob = 0
                nemicoc = 0
                nemicod = 0
                nemicoe = 0
                nemicof = 0
                nemicog = 0
                nemicoh = 0
                nemicoi = 0
                nemicol = 0

                # controllo mostri uccisi
                if len(mostristanze) - 1 >= 11:
                    i = 0
                    while i <= len(mostristanze) - 1:
                        if mostristanze[i] == dati[1]:
                            giavisitata = True
                            nmost = 10
                            j = i + 1
                            while j <= i + 10:
                                if not mostristanze[j]:
                                    if j == i + 1:
                                        mostroaw = 0
                                        mostroaa = 0
                                        mostroas = 0
                                        mostroad = 0
                                        mxa = gsx // 32 * 0
                                        mya = gsy // 18 * 0
                                        pvmatot = 0
                                        tipoa = ""
                                        espma = 0
                                        nemicoa = 0
                                        nmost = nmost - 1
                                    if j == i + 2:
                                        mostrobw = 0
                                        mostroba = 0
                                        mostrobs = 0
                                        mostrobd = 0
                                        mxb = gsx // 32 * 0
                                        myb = gsy // 18 * 0
                                        pvmbtot = 0
                                        tipob = ""
                                        espmb = 0
                                        nemicob = 0
                                        nmost = nmost - 1
                                    if j == i + 3:
                                        mostrocw = 0
                                        mostroca = 0
                                        mostrocs = 0
                                        mostrocd = 0
                                        mxc = gsx // 32 * 0
                                        myc = gsy // 18 * 0
                                        pvmctot = 0
                                        tipoc = ""
                                        espmc = 0
                                        nemicoc = 0
                                        nmost = nmost - 1
                                    if j == i + 4:
                                        mostrodw = 0
                                        mostroda = 0
                                        mostrods = 0
                                        mostrodd = 0
                                        mxd = gsx // 32 * 0
                                        myd = gsy // 18 * 0
                                        pvmdtot = 0
                                        tipod = ""
                                        espmd = 0
                                        nemicod = 0
                                        nmost = nmost - 1
                                    if j == i + 5:
                                        mostroew = 0
                                        mostroea = 0
                                        mostroes = 0
                                        mostroed = 0
                                        mxe = gsx // 32 * 0
                                        mye = gsy // 18 * 0
                                        pvmetot = 0
                                        tipoe = ""
                                        espme = 0
                                        nemicoe = 0
                                        nmost = nmost - 1
                                    if j == i + 6:
                                        mostrofw = 0
                                        mostrofa = 0
                                        mostrofs = 0
                                        mostrofd = 0
                                        mxf = gsx // 32 * 0
                                        myf = gsy // 18 * 0
                                        pvmftot = 0
                                        tipof = ""
                                        espmf = 0
                                        nemicof = 0
                                        nmost = nmost - 1
                                    if j == i + 7:
                                        mostrogw = 0
                                        mostroga = 0
                                        mostrogs = 0
                                        mostrogd = 0
                                        mxg = gsx // 32 * 0
                                        myg = gsy // 18 * 0
                                        pvmgtot = 0
                                        tipog = ""
                                        espmg = 0
                                        nemicog = 0
                                        nmost = nmost - 1
                                    if j == i + 8:
                                        mostrohw = 0
                                        mostroha = 0
                                        mostrohs = 0
                                        mostrohd = 0
                                        mxh = gsx // 32 * 0
                                        myh = gsy // 18 * 0
                                        pvmhtot = 0
                                        tipoh = ""
                                        espmh = 0
                                        nemicoh = 0
                                        nmost = nmost - 1
                                    if j == i + 9:
                                        mostroiw = 0
                                        mostroia = 0
                                        mostrois = 0
                                        mostroid = 0
                                        mxi = gsx // 32 * 0
                                        myi = gsy // 18 * 0
                                        pvmitot = 0
                                        tipoi = ""
                                        espmi = 0
                                        nemicoi = 0
                                        nmost = nmost - 1
                                    if j == i + 10:
                                        mostrolw = 0
                                        mostrola = 0
                                        mostrols = 0
                                        mostrold = 0
                                        mxl = gsx // 32 * 0
                                        myl = gsy // 18 * 0
                                        pvmltot = 0
                                        tipol = ""
                                        espml = 0
                                        nemicol = 0
                                        nmost = nmost - 1
                                j = j + 1
                        i = i + 11
                if not giavisitata:
                    # aggiorna la stanza come "visitata"
                    mostristanze.append(dati[1])
                    i = 1
                    while i <= nmost:
                        mostristanze.append(True)
                        i = i + 1
                    i = nmost + 1
                    while i <= 10:
                        mostristanze.append(False)
                        i = i + 1

                muovirob = 0
                muovimosta = 0
                muovimostb = 0
                muovimostc = 0
                muovimostd = 0
                muovimoste = 0
                muovimostf = 0
                muovimostg = 0
                muovimosth = 0
                muovimosti = 0
                muovimostl = 0
                mxav = mxa
                myav = mya
                mxbv = mxb
                mybv = myb
                mxcv = mxc
                mycv = myc
                mxdv = mxd
                mydv = myd
                mxev = mxe
                myev = mye
                mxfv = mxf
                myfv = myf
                mxgv = mxg
                mygv = myg
                mxhv = mxh
                myhv = myh
                mxiv = mxi
                myiv = myi
                mxlv = mxl
                mylv = myl
                pvma = pvmatot
                pvmb = pvmbtot
                pvmc = pvmctot
                pvmd = pvmdtot
                pvme = pvmetot
                pvmf = pvmftot
                pvmg = pvmgtot
                pvmh = pvmhtot
                pvmi = pvmitot
                pvml = pvmltot
                # 1:veleno / 2:lentezza / 3:veleno-lentezza
                statoma = 0
                statomb = 0
                statomc = 0
                statomd = 0
                statome = 0
                statomf = 0
                statomg = 0
                statomh = 0
                statomi = 0
                statoml = 0
                mortoa = 0
                mortob = 0
                mortoc = 0
                mortod = 0
                mortoe = 0
                mortof = 0
                mortog = 0
                mortoh = 0
                mortoi = 0
                mortol = 0
                vistoa = False
                vistob = False
                vistoc = False
                vistod = False
                vistoe = False
                vistof = False
                vistog = False
                vistoh = False
                vistoi = False
                vistol = False
                raggiovistaa = 0
                raggiovistab = 0
                raggiovistac = 0
                raggiovistad = 0
                raggiovistae = 0
                raggiovistaf = 0
                raggiovistag = 0
                raggiovistah = 0
                raggiovistai = 0
                raggiovistal = 0

            if cambiosta:
                stanza = dati[1]
                # fermare la camminata dopo il cambio stanza
                nx = 0
                ny = 0
                primopas = False
                tastotemp = 5
                tastotempfps = 5
                tastop = 0
                # per inizializzare i mostri
                primociclo = True

                # carica i cofanetti nella stanza (svuoto e riempio il vettore)
                i = 0
                while i < len(cofanetti):
                    del cofanetti[i + 3]
                    del cofanetti[i + 2]
                    del cofanetti[i + 1]
                    del cofanetti[i]
                i = 0
                while i < len(tutticofanetti):
                    if tutticofanetti[i] == dati[1]:
                        cofanetti.append(tutticofanetti[i])
                        cofanetti.append(tutticofanetti[i + 1])
                        cofanetti.append(tutticofanetti[i + 2])
                        cofanetti.append(tutticofanetti[i + 3])
                    i = i + 4

                # carica le porte nella stanza (svuoto e riempio il vettore)
                i = 0
                while i < len(porte):
                    del porte[i + 3]
                    del porte[i + 2]
                    del porte[i + 1]
                    del porte[i]
                i = 0
                while i < len(tutteporte):
                    if tutteporte[i] == dati[1]:
                        porte.append(tutteporte[i])
                        porte.append(tutteporte[i + 1])
                        porte.append(tutteporte[i + 2])
                        porte.append(tutteporte[i + 3])
                    i = i + 4

                # fai vedere stanze visitate
                # caseviste[x, y, flag, ... ] -> riempito come se non vedessi niente
                numstanza = dati[1]
                caseviste = []
                n = 1
                while n <= 28:
                    m = 1
                    while m <= 14:
                        caseviste.append(gpx + (gpx * n))
                        caseviste.append(gpy + (gpy * m))
                        caseviste.append(False)
                        m = m + 1
                    n = n + 1
                # scoprire caselle viste
                caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)

                # eliminare tutte le esche
                i = 1
                while i < len(vitaesca):
                    del vitaesca[i + 2]
                    del vitaesca[i + 1]
                    del vitaesca[i]
                    del vitaesca[i - 1]

                # cambiosta viene cambiato sopra !!!!!!!!!!!!
                cambiosta = False

            # arma
            armaw = pygame.image.load("Immagini\Armi\Arma%iw.png" % dati[6])
            armaw = pygame.transform.scale(armaw, (gpx, gpy))
            armaa = pygame.image.load("Immagini\Armi\Arma%ia.png" % dati[6])
            armaa = pygame.transform.scale(armaa, (gpx, gpy))
            armas = pygame.image.load("Immagini\Armi\Arma%is.png" % dati[6])
            armas = pygame.transform.scale(armas, (gpx, gpy))
            armad = pygame.image.load("Immagini\Armi\Arma%id.png" % dati[6])
            armad = pygame.transform.scale(armad, (gpx, gpy))
            # armatura
            armaturaw = pygame.image.load("Immagini\Armature\Armatura%iw.png" % dati[8])
            armaturaw = pygame.transform.scale(armaturaw, (gpx, gpy))
            armaturaa = pygame.image.load("Immagini\Armature\Armatura%ia.png" % dati[8])
            armaturaa = pygame.transform.scale(armaturaa, (gpx, gpy))
            armaturas = pygame.image.load("Immagini\Armature\Armatura%is.png" % dati[8])
            armaturas = pygame.transform.scale(armaturas, (gpx, gpy))
            armaturad = pygame.image.load("Immagini\Armature\Armatura%id.png" % dati[8])
            armaturad = pygame.transform.scale(armaturad, (gpx, gpy))
            # scudo
            scudow = pygame.image.load("Immagini\Scudi\Scudo%iw.png" % dati[7])
            scudow = pygame.transform.scale(scudow, (gpx, gpy))
            scudoa = pygame.image.load("Immagini\Scudi\Scudo%ia.png" % dati[7])
            scudoa = pygame.transform.scale(scudoa, (gpx, gpy))
            scudos = pygame.image.load("Immagini\Scudi\Scudo%is.png" % dati[7])
            scudos = pygame.transform.scale(scudos, (gpx, gpy))
            scudod = pygame.image.load("Immagini\Scudi\Scudo%id.png" % dati[7])
            scudod = pygame.transform.scale(scudod, (gpx, gpy))
            # armatura robot
            armrobw = pygame.image.load("Immagini\Armrobs\Armrob%iw.png" % dati[9])
            armrobw = pygame.transform.scale(armrobw, (gpx, gpy))
            armroba = pygame.image.load("Immagini\Armrobs\Armrob%ia.png" % dati[9])
            armroba = pygame.transform.scale(armroba, (gpx, gpy))
            armrobs = pygame.image.load("Immagini\Armrobs\Armrob%is.png" % dati[9])
            armrobs = pygame.transform.scale(armrobs, (gpx, gpy))
            armrobd = pygame.image.load("Immagini\Armrobs\Armrob%id.png" % dati[9])
            armrobd = pygame.transform.scale(armrobd, (gpx, gpy))
            if agg == 1:
                arma = armaw
                armatura = armaturaw
                scudo = scudow
            if agg == 2:
                arma = armaa
                armatura = armaturaa
                scudo = scudoa
            if agg == 3:
                arma = armas
                armatura = armaturas
                scudo = scudos
            if agg == 4:
                arma = armad
                armatura = armaturad
                scudo = scudod
            if nrob != 0:
                if nrob == 1:
                    robot = robod
                    armrob = armrobd
                if nrob == 2:
                    robot = roboa
                    armrob = armroba
                if nrob == 3:
                    robot = robos
                    armrob = armrobs
                if nrob == 4:
                    robot = robow
                    armrob = armrobw

            caricaini = True
            carim = False
            tastotemp = 10
            tastotempfps = 5

        if inizio:
            arma = armas
            armatura = armaturas
            scudo = scudos
            robot = robos
            armrob = armrobs
            inizio = False
            primociclo = True

        # rallenta per i 30 fps
        '''if not primopas and tastotempfps != 0 and premuti >= 1:
            tastotempfps = tastotempfps - 1
            nx = 0
            ny = 0
        if not primopas and tastotempfps == 0 and premuti >= 1:
            if tastop == pygame.K_w:
                ny = -gpy
            if tastop == pygame.K_a:
                nx = -gpx
            if tastop == pygame.K_s:
                ny = gpy
            if tastop == pygame.K_d:
                nx = gpx
            tastotempfps = 5'''

        # controllo primo passo
        if primopas and tastotemp != 0 and premuti >= 1:
            tastotemp = tastotemp - 1
            nx = 0
            ny = 0
        if primopas and tastotemp == 0 and premuti >= 1:
            if tastop == pygame.K_w:
                ny = -gpy
            if tastop == pygame.K_a:
                nx = -gpx
            if tastop == pygame.K_s:
                ny = gpy
            if tastop == pygame.K_d:
                nx = gpx
            primopas = False
            tastotemp = 5

        tastoTrovato = False
        # catturare gli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and not aumentoliv:
                # movimanti
                tastop = event.key
                # movimenti personaggio
                if event.key == pygame.K_w and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 3
                    pers = persw
                    arma = armaw
                    armatura = armaturaw
                    scudo = scudow
                    ny = -gpy
                    nx = 0
                    primopas = True
                if event.key == pygame.K_a and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 2
                    pers = persa
                    arma = armaa
                    armatura = armaturaa
                    scudo = scudoa
                    nx = -gpx
                    ny = 0
                    primopas = True
                if event.key == pygame.K_s and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 4
                    pers = perss
                    arma = armas
                    armatura = armaturas
                    scudo = scudos
                    ny = gpy
                    nx = 0
                    primopas = True
                if event.key == pygame.K_d and not tastoTrovato:
                    tastoTrovato = True
                    premuti += 1
                    npers = 1
                    pers = persd
                    arma = armad
                    armatura = armaturad
                    scudo = scudod
                    nx = gpx
                    ny = 0
                    primopas = True

                if event.key == pygame.K_e and not tastoTrovato and muovirob <= 0 and muovimosta <= 0 and muovimostb <= 0 and muovimostc <= 0 and muovimostd <= 0 and muovimoste <= 0 and muovimostf <= 0 and muovimostg <= 0 and muovimosth <= 0 and muovimosti <= 0 and muovimostl <= 0:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    attacco = 1
                if event.key == pygame.K_x and not tastoTrovato and muovirob <= 0 and muovimosta <= 0 and muovimostb <= 0 and muovimostc <= 0 and muovimostd <= 0 and muovimoste <= 0 and muovimostf <= 0 and muovimostg <= 0 and muovimosth <= 0 and muovimosti <= 0 and muovimostl <= 0:
                    tastoTrovato = True
                    nx = 0
                    ny = 0
                    if chiamarob:
                        chiamarob = False
                    else:
                        chiamarob = True

                if event.key == pygame.K_SPACE and not tastoTrovato and muovirob <= 0 and muovimosta <= 0 and muovimostb <= 0 and muovimostc <= 0 and muovimostd <= 0 and muovimoste <= 0 and muovimostf <= 0 and muovimostg <= 0 and muovimosth <= 0 and muovimosti <= 0 and muovimostl <= 0:
                    tastoTrovato = True
                    # apertura porte
                    k = 0
                    while k < len(porte):
                        if porte[k] == dati[1] and ((porte[k + 1] == x + gpx and porte[k + 2] == y and npers == 1) or (
                                porte[k + 1] == x - gpx and porte[k + 2] == y and npers == 2) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y + gpy and npers == 4) or (
                                                            porte[k + 1] == x and porte[
                                                        k + 2] == y - gpy and npers == 3)) and not porte[k + 3]:
                            sposta = True
                            suonoaperturacopo.play()
                            porte[k + 3] = True
                            # scoprire caselle viste
                            caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)
                            caricaini = True
                            # aggiornare vettore tutteporte
                            j = 0
                            while j < len(tutteporte):
                                if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[
                                    j + 2] == porte[k + 2]:
                                    tutteporte[j + 3] = True
                                j = j + 4
                        k = k + 4
                    # apertura cofanetti
                    i = 0
                    while i < len(cofanetti):
                        if cofanetti[i] == dati[1] and (
                                (cofanetti[i + 1] == x + gpx and cofanetti[i + 2] == y and npers == 1) or (
                                cofanetti[i + 1] == x - gpx and cofanetti[i + 2] == y and npers == 2) or (
                                        cofanetti[i + 1] == x and cofanetti[i + 2] == y + gpy and npers == 4) or (
                                        cofanetti[i + 1] == x and cofanetti[i + 2] == y - gpy and npers == 3)) and not \
                        cofanetti[i + 3]:
                            suonoaperturacopo.play()
                            sposta = True
                            dati, tesoro = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                            cofanetti[i + 3] = True
                            caricaini = True
                            # aggiornare vettore tutticofanetti
                            j = 0
                            while j < len(tutticofanetti):
                                if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and \
                                        tutticofanetti[j + 2] == cofanetti[i + 2]:
                                    tutticofanetti[j + 3] = True
                                j = j + 4
                        i = i + 4

                if event.key == pygame.K_ESCAPE and not tastoTrovato and muovirob <= 0 and muovimosta <= 0 and muovimostb <= 0 and muovimostc <= 0 and muovimostd <= 0 and muovimoste <= 0 and muovimostf <= 0 and muovimostg <= 0 and muovimosth <= 0 and muovimosti <= 0 and muovimostl <= 0:
                    tastoTrovato = True
                    startf = True

            if event.type == pygame.KEYUP:
                if tastop == pygame.K_w or tastop == pygame.K_a or tastop == pygame.K_s or tastop == pygame.K_d:
                    premuti -= 1
                    if event.key == tastop:
                        premuti = 0
                else:
                    premuti = 0
                if premuti == 0:
                    nx = 0
                    ny = 0
                    primopas = False
                    tastotemp = 5
                    tastotempfps = 5
                    tastop = 0

        # statistiche personaggio e robo (liv + arm + scu)
        # se modifichi -> modifica anche equip, equiprobo e ovunque si presenta pvtot
        esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati, difesa)

        # ripristina vita e status dopo lv up
        if aumentoliv:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = False

        # menu start
        if startf and attacco != 1:
            selsta.play()
            dati[2] = x
            dati[3] = y
            if not apriocchio:
                dati, inizio, attacco = start(dati, nmost, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, apriocchio)
            else:
                dati, attacco, sposta = startBattaglia(dati)
            if attacco != 0:
                contattogg = 1
            carim = True
            startf = False

        # morte tua e di robo
        inizio = controllaMorteRallo(dati[5], inizio)
        morterob, dati, muovirob = controllaMorteColco(dati, muovirob)

        # movimento-azioni personaggio
        if (nx != 0 or ny != 0) and muovimosta <= 0 and muovimostb <= 0 and muovimostc <= 0 and muovimostd <= 0 and muovimoste <= 0 and muovimostf <= 0 and muovimostg <= 0 and muovimosth <= 0 and muovimosti <= 0 and muovimostl <= 0 and muovirob <= 0:
            # progresso - stanza - x - y - liv - pv - arma - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(50) - condizioni(20) - gambit(20) - veleno - surriscalda // dimensione: 0-122
            vx = x
            vy = y
            sposta = True
            stanzaVecchia = dati[1]
            x, y, dati[1], carim, inutile, cambiosta = muri_porte(x, y, nx, ny, dati[1], carim, 0, False, False, porte, cofanetti)
            if (x == rx and y == ry) or (x == mxa and y == mya) or (x == mxb and y == myb) or (x == mxc and y == myc) or (x == mxd and y == myd) or (x == mxe and y == mye) or (x == mxf and y == myf) or (x == mxg and y == myg) or (x == mxh and y == myh) or (x == mxi and y == myi) or (x == mxl and y == myl):
                x = vx
                y = vy
        # gestione attacchi
        if attacco != 0 and attacco <= 6 and contattogg == 0:
            pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, sposta, creaesca, xesca, yesca, statoma, statomb, statomc, statomd, statome, statomf, statomg, statomh, statomi, statoml, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126],
                                                                                                                                                                                                                  stanzaa, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob,
                                                                                                                                                                                                                  nemicoa, mxa, mya, nemicob, mxb, myb, nemicoc, mxc, myc, nemicod, mxd, myd, nemicoe, mxe, mye,
                                                                                                                                                                                                                  nemicof, mxf, myf, nemicog, mxg, myg, nemicoh, mxh, myh, nemicoi, mxi, myi, nemicol, mxl, myl,
                                                                                                                                                                                                                  pvmatot, pvmbtot, pvmctot, pvmdtot, pvmetot, pvmftot, pvmgtot, pvmhtot, pvmitot, pvmltot,
                                                                                                                                                                                                                  pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, statoma, statomb, statomc, statomd,
                                                                                                                                                                                                                  statome, statomf, statomg, statomh, statomi, statoml, raggiovistaa, raggiovistab, raggiovistac,
                                                                                                                                                                                                                  raggiovistad, raggiovistae, raggiovistaf, raggiovistag, raggiovistah, raggiovistai, raggiovistal,
                                                                                                                                                                                                                  att, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob)
            caricaini = True
            # cambiare posizione dopo l'attacco
            if npers == 3:
                pers = persw
                arma = armaw
                armatura = armaturaw
                scudo = scudow
            if npers == 2:
                pers = persa
                arma = armaa
                armatura = armaturaa
                scudo = scudoa
            if npers == 4:
                pers = perss
                arma = armas
                armatura = armaturas
                scudo = scudos
            if npers == 1:
                pers = persd
                arma = armad
                armatura = armaturad
                scudo = scudod
            # decrementa oggetto utilizzato
            if sposta:
                # bomba attacco = 2
                if attacco == 2:
                    dati[33] = dati[33] - 1
                # bomba veleno attacco = 3
                if attacco == 3:
                    dati[35] = dati[35] - 1
                # esca attacco = 4
                if attacco == 4:
                    dati[36] = dati[36] - 1
                # bomba appiccicosa attacco = 5
                if attacco == 5:
                    dati[39] = dati[39] - 1
                # bomba potenziata attacco = 6
                if attacco == 6:
                    dati[40] = dati[40] - 1
        # gestione difesa
        if sposta:
            difesa = 0
        if difesa != 0 and not sposta:
            sposta = False
            esptot, pvtot, entot, att, dif, difro, par = getStatistiche(dati, difesa)
            if difesa == 2:
                difesa = 1
                sposta = True
                dati[5] = dati[5] + 3
                if dati[5] > pvtot:
                    dati[5] = pvtot
        # gestione att+ e dif+
        if dati[123] > 0:
            att = att + att // 4
            if sposta:
                dati[123] = dati[123] - 1
        if dati[124] > 0:
            dif = dif + dif // 4
            if sposta:
                dati[124] = dati[124] - 1
        # veleno
        if dati[121] and sposta:
            dati[5] = dati[5] - 3
            if dati[5] < 0:
                dati[5] = 0
        # apertura/chiusura porte
        if apriChiudiPorta[0]:
            k = 0
            while k < len(porte):
                if porte[k] == dati[1] and porte[k + 1] == apriChiudiPorta[1] and porte[k + 2] == apriChiudiPorta[2]:
                    suonoaperturacopo.play()
                    if porte[k + 3]:
                        porte[k + 3] = False
                    else:
                        porte[k + 3] = True
                    # scoprire caselle viste
                    caseviste = scopriCaselleViste(x, y, rx, ry, numstanza, porte, cofanetti, caseviste)
                    # aggiornare vettore tutteporte
                    j = 0
                    while j < len(tutteporte):
                        if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                            tutteporte[j + 3] = porte[k + 3]
                        j = j + 4
                k = k + 4
            apriChiudiPorta = [False, 0, 0]
        # apertura cofanetti
        if apriCofanetto[0]:
            i = 0
            while i < len(cofanetti):
                if cofanetti[i] == dati[1] and cofanetti[i + 1] == apriCofanetto[1] and cofanetti[i + 2] == apriCofanetto[2] and not cofanetti[i + 3]:
                    suonoaperturacopo.play()
                    dati, tesoro = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                    cofanetti[i + 3] = True
                    # aggiornare vettore tutticofanetti
                    j = 0
                    while j < len(tutticofanetti):
                        if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                            tutticofanetti[j + 3] = True
                        j = j + 4
                i = i + 4
            apriCofanetto = [False, 0, 0]
        # scambia posizione con Colco
        if spingiColco:
            xProv = x
            yProv = y
            x = rx
            y = ry
            rx = xProv
            ry = yProv
            spingiColco = False

        # lancio esche
        if creaesca:
            contaesca = contaesca + 1
            # id, vita, xesca, yesca
            vitaesca.append(contaesca)
            vitaesca.append(100)
            vitaesca.append(xesca)
            vitaesca.append(yesca)
            creaesca = False
        # morte esca
        i = 1
        while i < len(vitaesca):
            cancellata = False
            if vitaesca[i] <= 0:
                n = 0
                while n < 32:
                    if vitaesca[i + 1] == gpx * n:
                        m = 0
                        while m < 18:
                            if vitaesca[i + 2] == gpy * m:
                                if (n + m) % 2 == 0:
                                    schermo.blit(sfondinoa, (vitaesca[i + 1], vitaesca[i + 2]))
                                if (n + m) % 2 != 0:
                                    schermo.blit(sfondinob, (vitaesca[i + 1], vitaesca[i + 2]))
                            m = m + 1
                    n = n + 1
                del vitaesca[i + 2]
                del vitaesca[i + 1]
                del vitaesca[i]
                del vitaesca[i - 1]
                cancellata = True
            if not cancellata:
                i = i + 4
        # riprendere le esche
        i = 1
        while i < len(vitaesca):
            if vitaesca[i + 1] == x and vitaesca[i + 2] == y:
                del vitaesca[i + 2]
                del vitaesca[i + 1]
                del vitaesca[i]
                del vitaesca[i - 1]
                dati[36] = dati[36] + 1
            i = i + 4

        # movimento-azioni robo
        if dati[122] > 0:
            # se surriscaldato toglie vel+ e efficienza
            dati[125] = 0
            dati[126] = 0
        if ((sposta and muovirob <= 0) or muovirob > 0) and not morterob and not cambiosta:
            vrx = rx
            vry = ry

            # surriscalda
            if dati[122] > 0:
                dati[122] = dati[122] - 1
                dati[10] = dati[10] - 3
                if muovirob == 0:
                    muovirob = -2

            # efficienza
            if dati[126] > 0:
                if dati[125] > 0:
                    if muovirob == 1 or muovirob == -1:
                        dati[126] = dati[126] - 1
                else:
                    dati[126] = dati[126] - 1

            # vel+
            if dati[125] > 0:
                if muovirob == 1 or muovirob == -1:
                    dati[125] = dati[125] - 1
                if dati[125] == 0:
                    dati[122] = 10
                if muovirob == 0:
                    muovirob = 2

            # movimento - gambit
            vetDatiNemici = [pvma, mxa, mya, pvmatot, statoma, pvmb, mxb, myb, pvmbtot, statomb, pvmc, mxc, myc, pvmctot, statomc, pvmd, mxd, myd, pvmdtot, statomd, pvme, mxe, mye, pvmetot, statome, pvmf, mxf, myf, pvmftot, statomf, pvmg, mxg, myg, pvmgtot, statomg, pvmh, mxh, myh, pvmhtot, statomh, pvmi, mxi, myi, pvmitot, statomi, pvml, mxl, myl, pvmltot, statoml]
            rx, ry, muovirob, nrob, dati, vetDatiNemici, raffreddamento, ricarica1, ricarica2 = movrobo(x, y, vx, vy, rx, ry, dati[1], muovirob, chiamarob, dati, porte, cofanetti, vetDatiNemici, nmost, difesa)
            pvma = vetDatiNemici[0]
            statoma = vetDatiNemici[4]
            pvmb = vetDatiNemici[5]
            statomb = vetDatiNemici[9]
            pvmc = vetDatiNemici[10]
            statomc = vetDatiNemici[14]
            pvmd = vetDatiNemici[15]
            statomd = vetDatiNemici[19]
            pvme = vetDatiNemici[20]
            statome = vetDatiNemici[24]
            pvmf = vetDatiNemici[25]
            statomf = vetDatiNemici[29]
            pvmg = vetDatiNemici[30]
            statomg = vetDatiNemici[34]
            pvmh = vetDatiNemici[35]
            statomh = vetDatiNemici[39]
            pvmi = vetDatiNemici[40]
            statomi = vetDatiNemici[44]
            pvml = vetDatiNemici[45]
            statoml = vetDatiNemici[49]

            # effetto di raffreddamento
            if True:
                if raffreddamento:
                    muovirob = -2
                    raffredda = 1
                if raffredda == 0:
                    dati[122] = 0
                if raffredda >= 0:
                    raffredda -= 1
            # effetto auto-ricarica
            if True:
                if ricarica1:
                    muovirob = -2
                    autoRic1 = 1
                if autoRic1 == 0:
                    dati[10] += dannoTecniche[6]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
                if autoRic1 >= 0:
                    autoRic1 -= 1
            # effetto auto-ricarica+
            if True:
                if ricarica2:
                    muovirob = -2
                    autoRic2 = 1
                if autoRic2 == 0:
                    dati[10] += dannoTecniche[16]
                    if dati[10] > entot:
                        dati[10] = entot
                    dati[122] = 10
                if autoRic2 >= 0:
                    autoRic2 -= 1

            if muovirob < 0:
                rx = vrx
                ry = vry
                nrob = 0
            if (rx == x and ry == y) or (rx == mxa and ry == mya) or (rx == mxb and ry == myb) or (rx == mxc and ry == myc) or (rx == mxd and ry == myd) or (rx == mxe and ry == mye) or (rx == mxf and ry == myf) or (rx == mxg and ry == myg) or (rx == mxh and ry == myh) or (rx == mxi and ry == myi) or (rx == mxl and ry == myl):
                rx = vrx
                ry = vry
                nrob = 0
            if nrob != 0:
                if nrob == 1:
                    robot = robod
                    armrob = armrobd
                if nrob == 2:
                    robot = roboa
                    armrob = armroba
                if nrob == 3:
                    robot = robos
                    armrob = armrobs
                if nrob == 4:
                    robot = robow
                    armrob = armrobw
        # gestione tecniche
        if attacco != 0 and attacco > 6 and contattogg == 0:
            pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, sposta, creaesca, xesca, yesca, statoma, statomb, statomc, statomd, statome, statomf, statomg, statomh, statomi, statoml, npers, nrob, difesa, apriChiudiPorta, apriCofanetto, spingiColco = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122],
                                                                                                                                                                                                                        dati[125], dati[126], stanzaa, dati[1], sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob,
                                                                                                                                                                                                                        nemicoa, mxa, mya, nemicob, mxb, myb, nemicoc, mxc, myc, nemicod, mxd, myd, nemicoe, mxe, mye,
                                                                                                                                                                                                                        nemicof, mxf, myf, nemicog, mxg, myg, nemicoh, mxh, myh, nemicoi, mxi, myi, nemicol, mxl, myl,
                                                                                                                                                                                                                        pvmatot, pvmbtot, pvmctot, pvmdtot, pvmetot, pvmftot, pvmgtot, pvmhtot, pvmitot, pvmltot,
                                                                                                                                                                                                                        pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, statoma, statomb, statomc, statomd,
                                                                                                                                                                                                                        statome, statomf, statomg, statomh, statomi, statoml, raggiovistaa, raggiovistab, raggiovistac,
                                                                                                                                                                                                                        raggiovistad, raggiovistae, raggiovistaf, raggiovistag, raggiovistah, raggiovistai, raggiovistal,
                                                                                                                                                                                                                        att, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio)
            caricaini = True
            # cambiare posizione dopo l'attacco
            if nrob != 0:
                if nrob == 1:
                    robot = robod
                    armrob = armrobd
                if nrob == 2:
                    robot = roboa
                    armrob = armroba
                if nrob == 3:
                    robot = robos
                    armrob = armrobs
                if nrob == 4:
                    robot = robow
                    armrob = armrobw
            # diminuisci pe
            if sposta:
                # scossa attacco = 7
                if attacco == 7:
                    dati[10] = dati[10] - 5
                # freccia elettrica attacco = 8
                if attacco == 8:
                    dati[10] = dati[10] - 5
                # tempesta elettrica attacco = 9
                if attacco == 9:
                    dati[10] = dati[10] - 10
                # scossa + attacco = 10
                if attacco == 10:
                    dati[10] = dati[10] - 10
                # freccia elettrica + attacco = 11
                if attacco == 11:
                    dati[10] = dati[10] - 10
                # tempesta elettrica + attacco = 12
                if attacco == 12:
                    dati[10] = dati[10] - 20
                # scossa ++ attacco = 13
                if attacco == 13:
                    dati[10] = dati[10] - 20
                # freccia elettrica ++ attacco = 14
                if attacco == 14:
                    dati[10] = dati[10] - 20
                # tempesta elettrica ++ attacco = 15
                if attacco == 15:
                    dati[10] = dati[10] - 30
        if morterob:
            robot = robomo
            armrob = armrobmo

        # movimento-azioni mostri
        if (nmost > 0 and (sposta or muovimosta > 0 or muovimostb > 0 or muovimostc > 0 or muovimostd > 0 or muovimoste > 0 or muovimostf > 0 or muovimostg > 0 or muovimosth > 0 or muovimosti > 0 or muovimostl > 0) and not cambiosta) or primociclo:
            vetDatiNemici = [pvma, mxa, mya, pvmatot, pvmb, mxb, myb, pvmbtot, pvmc, mxc, myc, pvmctot, pvmd, mxd, myd,
                             pvmdtot, pvme, mxe, mye, pvmetot, pvmf, mxf, myf, pvmftot, pvmg, mxg, myg, pvmgtot, pvmh,
                             mxh, myh, pvmhtot, pvmi, mxi, myi, pvmitot, pvml, mxl, myl, pvmltot]
            # veleno mostri
            if (statoma != 0 or statomb != 0 or statomc != 0 or statomd != 0 or statome != 0 or statomf != 0 or statomg != 0 or statomh != 0 or statomi != 0 or statoml != 0) and sposta:
                if statoma == 1 or statoma == 3:
                    pvma = pvma - 3
                if statomb == 1 or statomb == 3:
                    pvmb = pvmb - 3
                if statomc == 1 or statomc == 3:
                    pvmc = pvmc - 3
                if statomd == 1 or statomd == 3:
                    pvmd = pvmd - 3
                if statome == 1 or statome == 3:
                    pvme = pvme - 3
                if statomf == 1 or statomf == 3:
                    pvmf = pvmf - 3
                if statomg == 1 or statomg == 3:
                    pvmg = pvmg - 3
                if statomh == 1 or statomh == 3:
                    pvmh = pvmh - 3
                if statomi == 1 or statomi == 3:
                    pvmi = pvmi - 3
                if statoml == 1 or statoml == 3:
                    pvml = pvml - 3
            # movimento mostri
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxa and caseviste[i + 1] == mya:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimosta > 0 or (sposta and muovimosta <= 0)) and pvma > 0 and incasevista) or (primociclo and nemicoa):
                mxav = mxa
                myav = mya
                if primociclo:
                    mxaprimociclo = mxa
                    myaprimociclo = mya
                    muovimostaprimociclo = muovimosta
                    datiprimociclo = dati
                mxa, mya, muovimosta, nmos, vistoa, dati, vitaesca, raggiovistaa = movmostro(x, y, rx, ry, mxa, mya, dati[1], tipoa, muovimosta, vistoa, dif, difro, par, dati, statoma, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxa = mxaprimociclo
                    mya = myaprimociclo
                    muovimosta = muovimostaprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimosta < 0:
                    mxa = mxav
                    mya = myav
                if nmos == 1:
                    nemicoa = mostroad
                elif nmos == 2:
                    nemicoa = mostroaa
                if nmos == 3:
                    nemicoa = mostroas
                elif nmos == 4:
                    nemicoa = mostroaw
                if (mxa == x and mya == y) or (mxa == rx and mya == ry) or (mxa == mxb and mya == myb) or (mxa == mxc and mya == myc) or (mxa == mxd and mya == myd) or (mxa == mxe and mya == mye) or (mxa == mxf and mya == myf) or (mxa == mxg and mya == myg) or (mxa == mxh and mya == myh) or (mxa == mxi and mya == myi) or (mxa == mxl and mya == myl):
                    mxa = mxav
                    mya = myav
            elif pvma <= 0 and nemicoa != 0:
                nmost = nmost - 1
                pvmatot = 0
                tipoa = ""
                nemicoa = 0
                statoma = 0
                vistoa = False
                muovimosta = 0
                mxav = 0
                myav = 0
                mortoa = 1
                dati[127] = dati[127] + espma
                espma = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 1
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxb and caseviste[i + 1] == myb:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimostb > 0 or (sposta and muovimostb <= 0)) and pvmb > 0 and incasevista) or (primociclo and nemicob):
                mxbv = mxb
                mybv = myb
                if primociclo:
                    mxbprimociclo = mxb
                    mybprimociclo = myb
                    muovimostbprimociclo = muovimostb
                    datiprimociclo = dati
                mxb, myb, muovimostb, nmos, vistob, dati, vitaesca, raggiovistab = movmostro(x, y, rx, ry, mxb, myb, dati[1], tipob, muovimostb, vistob, dif, difro, par, dati, statomb, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxb = mxbprimociclo
                    myb = mybprimociclo
                    muovimostb = muovimostbprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimostb < 0:
                    mxb = mxbv
                    myb = mybv
                if nmos == 1:
                    nemicob = mostrobd
                elif nmos == 2:
                    nemicob = mostroba
                if nmos == 3:
                    nemicob = mostrobs
                elif nmos == 4:
                    nemicob = mostrobw
                if (mxb == x and myb == y) or (mxb == rx and myb == ry) or (mxb == mxa and myb == mya) or (mxb == mxc and myb == myc) or (mxb == mxd and myb == myd) or (mxb == mxe and myb == mye) or (mxb == mxf and myb == myf) or (mxb == mxg and myb == myg) or (mxb == mxh and myb == myh) or (mxb == mxi and myb == myi) or (mxb == mxl and myb == myl):
                    mxb = mxbv
                    myb = mybv
            elif pvmb <= 0 and nemicob != 0:
                nmost = nmost - 1
                pvmbtot = 0
                tipob = ""
                nemicob = 0
                statomb = 0
                vistob = False
                muovimostb = 0
                mxbv = 0
                mybv = 0
                mortob = 1
                dati[127] = dati[127] + espmb
                espmb = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 2
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxc and caseviste[i + 1] == myc:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimostc > 0 or (sposta and muovimostc <= 0)) and pvmc > 0 and incasevista) or (primociclo and nemicoc):
                mxcv = mxc
                mycv = myc
                if primociclo:
                    mxcprimociclo = mxc
                    mycprimociclo = myc
                    muovimostcprimociclo = muovimostc
                    datiprimociclo = dati
                mxc, myc, muovimostc, nmos, vistoc, dati, vitaesca, raggiovistac = movmostro(x, y, rx, ry, mxc, myc, dati[1], tipoc, muovimostc, vistoc, dif, difro, par, dati, statomc, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxc = mxcprimociclo
                    myc = mycprimociclo
                    muovimostc = muovimostcprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimostc < 0:
                    mxc = mxcv
                    myc = mycv
                if nmos == 1:
                    nemicoc = mostrocd
                elif nmos == 2:
                    nemicoc = mostroca
                if nmos == 3:
                    nemicoc = mostrocs
                elif nmos == 4:
                    nemicoc = mostrocw
                if (mxc == x and myc == y) or (mxc == rx and myc == ry) or (mxc == mxa and myc == mya) or (mxc == mxb and myc == myb) or (mxc == mxd and myc == myd) or (mxc == mxe and myc == mye) or (mxc == mxf and myc == myf) or (mxc == mxg and myc == myg) or (mxc == mxh and myc == myh) or (mxc == mxi and myc == myi) or (mxc == mxl and myc == myl):
                    mxc = mxcv
                    myc = mycv
            elif pvmc <= 0 and nemicoc != 0:
                nmost = nmost - 1
                pvmctot = 0
                tipoc = ""
                nemicoc = 0
                statomc = 0
                vistoc = False
                muovimostc = 0
                mxcv = 0
                mycv = 0
                mortoc = 1
                dati[127] = dati[127] + espmc
                espmc = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 3
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxd and caseviste[i + 1] == myd:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimostd > 0 or (sposta and muovimostd <= 0)) and pvmd > 0 and incasevista) or (primociclo and nemicod):
                mxdv = mxd
                mydv = myd
                if primociclo:
                    mxdprimociclo = mxd
                    mydprimociclo = myd
                    muovimostdprimociclo = muovimostd
                    datiprimociclo = dati
                mxd, myd, muovimostd, nmos, vistod, dati, vitaesca, raggiovistad = movmostro(x, y, rx, ry, mxd, myd, dati[1], tipod, muovimostd, vistod, dif, difro, par, dati, statomd, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxd = mxdprimociclo
                    myd = mydprimociclo
                    muovimostd = muovimostdprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimostd < 0:
                    mxd = mxdv
                    myd = mydv
                if nmos == 1:
                    nemicod = mostrodd
                elif nmos == 2:
                    nemicod = mostroda
                if nmos == 3:
                    nemicod = mostrods
                elif nmos == 4:
                    nemicod = mostrodw
                if (mxd == x and myd == y) or (mxd == rx and myd == ry) or (mxd == mxa and myd == mya) or (mxd == mxb and myd == myb) or (mxd == mxc and myd == myc) or (mxd == mxe and myd == mye) or (mxd == mxf and myd == myf) or (mxd == mxg and myd == myg) or (mxd == mxh and myd == myh) or (mxd == mxi and myd == myi) or (mxd == mxl and myd == myl):
                    mxd = mxdv
                    myd = mydv
            elif pvmd <= 0 and nemicod != 0:
                nmost = nmost - 1
                pvmdtot = 0
                tipod = ""
                nemicod = 0
                statomd = 0
                vistod = False
                muovimostd = 0
                mxdv = 0
                mydv = 0
                mortod = 1
                dati[127] = dati[127] + espmd
                espmd = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 4
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxe and caseviste[i + 1] == mye:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimoste > 0 or (sposta and muovimoste <= 0)) and pvme > 0 and incasevista) or (primociclo and nemicoe):
                mxev = mxe
                myev = mye
                if primociclo:
                    mxeprimociclo = mxe
                    myeprimociclo = mye
                    muovimosteprimociclo = muovimoste
                    datiprimociclo = dati
                mxe, mye, muovimoste, nmos, vistoe, dati, vitaesca, raggiovistae = movmostro(x, y, rx, ry, mxe, mye, dati[1], tipoe, muovimoste, vistoe, dif, difro, par, dati, statome, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxe = mxeprimociclo
                    mye = myeprimociclo
                    muovimoste = muovimosteprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimoste < 0:
                    mxe = mxev
                    mye = myev
                if nmos == 1:
                    nemicoe = mostroed
                elif nmos == 2:
                    nemicoe = mostroea
                if nmos == 3:
                    nemicoe = mostroes
                elif nmos == 4:
                    nemicoe = mostroew
                if (mxe == x and mye == y) or (mxe == rx and mye == ry) or (mxe == mxa and mye == mya) or (mxe == mxb and mye == myb) or (mxe == mxc and mye == myc) or (mxe == mxd and mye == myd) or (mxe == mxf and mye == myf) or (mxe == mxg and mye == myg) or (mxe == mxh and mye == myh) or (mxe == mxi and mye == myi) or (mxe == mxl and mye == myl):
                    mxe = mxev
                    mye = myev
            elif pvme <= 0 and nemicoe != 0:
                nmost = nmost - 1
                pvmetot = 0
                tipoe = ""
                nemicoe = 0
                statome = 0
                vistoe = False
                muovimoste = 0
                mxev = 0
                myev = 0
                mortoe = 1
                dati[127] = dati[127] + espme
                espme = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 5
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxf and caseviste[i + 1] == myf:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimostf > 0 or (sposta and muovimostf <= 0)) and pvmf > 0 and incasevista) or (primociclo and nemicof):
                mxfv = mxf
                myfv = myf
                if primociclo:
                    mxfprimociclo = mxf
                    myfprimociclo = myf
                    muovimostfprimociclo = muovimostf
                    datiprimociclo = dati
                mxf, myf, muovimostf, nmos, vistof, dati, vitaesca, raggiovistaf = movmostro(x, y, rx, ry, mxf, myf, dati[1], tipof, muovimostf, vistof, dif, difro, par, dati, statomf, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxf = mxfprimociclo
                    myf = myfprimociclo
                    muovimostf = muovimostfprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimostf < 0:
                    mxf = mxfv
                    myf = myfv
                if nmos == 1:
                    nemicof = mostrofd
                elif nmos == 2:
                    nemicof = mostrofa
                if nmos == 3:
                    nemicof = mostrofs
                elif nmos == 4:
                    nemicof = mostrofw
                if (mxf == x and myf == y) or (mxf == rx and myf == ry) or (mxf == mxa and myf == mya) or (mxf == mxb and myf == myb) or (mxf == mxc and myf == myc) or (mxf == mxd and myf == myd) or (mxf == mxe and myf == mye) or (mxf == mxg and myf == myg) or (mxf == mxh and myf == myh) or (mxf == mxi and myf == myi) or (mxf == mxl and myf == myl):
                    mxf = mxfv
                    myf = myfv
            elif pvmf <= 0 and nemicof != 0:
                nmost = nmost - 1
                pvmftot = 0
                tipof = ""
                nemicof = 0
                statomf = 0
                vistof = False
                muovimostf = 0
                mxfv = 0
                myfv = 0
                mortof = 1
                dati[127] = dati[127] + espmf
                espmf = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 6
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxg and caseviste[i + 1] == myg:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimostg > 0 or (sposta and muovimostg <= 0)) and pvmg > 0 and incasevista) or (primociclo and nemicog):
                mxgv = mxg
                mygv = myg
                if primociclo:
                    mxgprimociclo = mxg
                    mygprimociclo = myg
                    muovimostgprimociclo = muovimostg
                    datiprimociclo = dati
                mxg, myg, muovimostg, nmos, vistog, dati, vitaesca, raggiovistag = movmostro(x, y, rx, ry, mxg, myg, dati[1], tipog, muovimostg, vistog, dif, difro, par, dati, statomg, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxg = mxgprimociclo
                    myg = mygprimociclo
                    muovimostg = muovimostgprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimostg < 0:
                    mxg = mxgv
                    myg = mygv
                if nmos == 1:
                    nemicog = mostrogd
                elif nmos == 2:
                    nemicog = mostroga
                if nmos == 3:
                    nemicog = mostrogs
                elif nmos == 4:
                    nemicog = mostrogw
                if (mxg == x and myg == y) or (mxg == rx and myg == ry) or (mxg == mxa and myg == mya) or (mxg == mxb and myg == myb) or (mxg == mxc and myg == myc) or (mxg == mxd and myg == myd) or (mxg == mxe and myg == mye) or (mxg == mxf and myg == myf) or (mxg == mxh and myg == myh) or (mxg == mxi and myg == myi) or (mxg == mxl and myg == myl):
                    mxg = mxgv
                    myg = mygv
            elif pvmg <= 0 and nemicog != 0:
                nmost = nmost - 1
                pvmgtot = 0
                tipog = ""
                nemicog = 0
                statomg = 0
                vistog = False
                muovimostg = 0
                mxgv = 0
                mygv = 0
                mortog = 1
                dati[127] = dati[127] + espmg
                espmg = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 7
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxh and caseviste[i + 1] == myh:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimosth > 0 or (sposta and muovimosth <= 0)) and pvmh > 0 and incasevista) or (primociclo and nemicoh):
                mxhv = mxh
                myhv = myh
                if primociclo:
                    mxhprimociclo = mxh
                    myhprimociclo = myh
                    muovimosthprimociclo = muovimosth
                    datiprimociclo = dati
                mxh, myh, muovimosth, nmos, vistoh, dati, vitaesca, raggiovistah = movmostro(x, y, rx, ry, mxh, myh, dati[1], tipoh, muovimosth, vistoh, dif, difro, par, dati, statomh, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxh = mxhprimociclo
                    myh = myhprimociclo
                    muovimosth = muovimosthprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimosth < 0:
                    mxh = mxhv
                    myh = myhv
                if nmos == 1:
                    nemicoh = mostrohd
                elif nmos == 2:
                    nemicoh = mostroha
                if nmos == 3:
                    nemicoh = mostrohs
                elif nmos == 4:
                    nemicoh = mostrohw
                if (mxh == x and myh == y) or (mxh == rx and myh == ry) or (mxh == mxa and myh == mya) or (mxh == mxb and myh == myb) or (mxh == mxc and myh == myc) or (mxh == mxd and myh == myd) or (mxh == mxe and myh == mye) or (mxh == mxf and myh == myf) or (mxh == mxg and myh == myg) or (mxh == mxi and myh == myi) or (mxh == mxl and myh == myl):
                    mxh = mxhv
                    myh = myhv
            elif pvmh <= 0 and nemicoh != 0:
                nmost = nmost - 1
                pvmhtot = 0
                tipoh = ""
                nemicoh = 0
                statomh = 0
                vistoh = False
                muovimosth = 0
                mxhv = 0
                myhv = 0
                mortoh = 1
                dati[127] = dati[127] + espmh
                espmh = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 8
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxi and caseviste[i + 1] == myi:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimosti > 0 or (sposta and muovimosti <= 0)) and pvmi > 0 and incasevista) or (primociclo and nemicoi):
                mxiv = mxi
                myiv = myi
                if primociclo:
                    mxiprimociclo = mxi
                    myiprimociclo = myi
                    muovimostiprimociclo = muovimosti
                    datiprimociclo = dati
                mxi, myi, muovimosti, nmos, vistoi, dati, vitaesca, raggiovistai = movmostro(x, y, rx, ry, mxi, myi, dati[1], tipoi, muovimosti, vistoi, dif, difro, par, dati, statomi, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxi = mxiprimociclo
                    myi = myiprimociclo
                    muovimosti = muovimostiprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimosti < 0:
                    mxi = mxiv
                    myi = myiv
                if nmos == 1:
                    nemicoi = mostroid
                elif nmos == 2:
                    nemicoi = mostroia
                if nmos == 3:
                    nemicoi = mostrois
                elif nmos == 4:
                    nemicoi = mostroiw
                if (mxi == x and myi == y) or (mxi == rx and myi == ry) or (mxi == mxa and myi == mya) or (mxi == mxb and myi == myb) or (mxi == mxc and myi == myc) or (mxi == mxd and myi == myd) or (mxi == mxe and myi == mye) or (mxi == mxf and myi == myf) or (mxi == mxg and myi == myg) or (mxi == mxh and myi == myh) or (mxi == mxl and myi == myl):
                    mxi = mxiv
                    myi = myiv
            elif pvmi <= 0 and nemicoi != 0:
                nmost = nmost - 1
                pvmitot = 0
                tipoi = ""
                nemicoi = 0
                statomi = 0
                vistoi = False
                muovimosti = 0
                mxiv = 0
                myiv = 0
                mortoi = 1
                dati[127] = dati[127] + espmi
                espmi = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 9
                        mostristanze[j] = False
                    i = i + 11
            incasevista = False
            i = 0
            while i < len(caseviste):
                if caseviste[i + 2] and caseviste[i] == mxl and caseviste[i + 1] == myl:
                    incasevista = True
                    break
                i = i + 3
            if ((muovimostl > 0 or (sposta and muovimostl <= 0)) and pvml > 0 and incasevista) or (primociclo and nemicol):
                mxlv = mxl
                mylv = myl
                if primociclo:
                    mxlprimociclo = mxl
                    mylprimociclo = myl
                    muovimostlprimociclo = muovimostl
                    datiprimociclo = dati
                mxl, myl, muovimostl, nmos, vistol, dati, vitaesca, raggiovistal = movmostro(x, y, rx, ry, mxl, myl, dati[1], tipol, muovimostl, vistol, dif, difro, par, dati, statoml, vitaesca, porte, cofanetti, vetDatiNemici)
                if primociclo:
                    mxl = mxlprimociclo
                    myl = mylprimociclo
                    muovimostl = muovimostlprimociclo
                    nmos = 0
                    dati = datiprimociclo
                if muovimostl < 0:
                    mxl = mxlv
                    myl = mylv
                if nmos == 1:
                    nemicol = mostrold
                elif nmos == 2:
                    nemicol = mostrola
                if nmos == 3:
                    nemicol = mostrols
                elif nmos == 4:
                    nemicol = mostrolw
                if (mxl == x and myl == y) or (mxl == rx and myl == ry) or (mxl == mxa and myl == mya) or (mxl == mxb and myl == myb) or (mxl == mxc and myl == myc) or (mxl == mxd and myl == myd) or (mxl == mxe and myl == mye) or (mxl == mxf and myl == myf) or (mxl == mxg and myl == myg) or (mxl == mxh and myl == myh) or (mxl == mxi and myl == myi):
                    mxl = mxlv
                    myl = mylv
            elif pvml <= 0 and nemicol != 0:
                nmost = nmost - 1
                pvmltot = 0
                tipol = ""
                nemicol = 0
                statoml = 0
                vistol = False
                muovimostl = 0
                mxlv = 0
                mylv = 0
                mortol = 1
                dati[127] = dati[127] + espml
                espml = 0
                i = 0
                while i <= len(mostristanze) - 1:
                    if mostristanze[i] == dati[1]:
                        j = i + 10
                        mostristanze[j] = False
                    i = i + 11

        # aumentare di livello
        if dati[127] >= esptot and dati[4] < 100 and not carim and not inizio:
            dati[4] = dati[4] + 1
            dati[127] = dati[127] - esptot
            aumentoliv = True

        # aggiorna vista dei mostri e metti l'occhio se ti vedono
        if True:
            if nemicoa != 0:
                inutile, inutile, inutile, inutile, vistoa, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxa, mya,
                                                                                                  dati[1], tipoa, -5,
                                                                                                  vistoa, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicob != 0:
                inutile, inutile, inutile, inutile, vistob, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxb, myb,
                                                                                                  dati[1], tipob, -5,
                                                                                                  vistob, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicoc != 0:
                inutile, inutile, inutile, inutile, vistoc, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxc, myc,
                                                                                                  dati[1], tipoc, -5,
                                                                                                  vistoc, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicod != 0:
                inutile, inutile, inutile, inutile, vistod, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxd, myd,
                                                                                                  dati[1], tipod, -5,
                                                                                                  vistod, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicoe != 0:
                inutile, inutile, inutile, inutile, vistoe, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxe, mye,
                                                                                                  dati[1], tipoe, -5,
                                                                                                  vistoe, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicof != 0:
                inutile, inutile, inutile, inutile, vistof, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxf, myf,
                                                                                                  dati[1], tipof, -5,
                                                                                                  vistof, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicog != 0:
                inutile, inutile, inutile, inutile, vistog, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxg, myg,
                                                                                                  dati[1], tipog, -5,
                                                                                                  vistog, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicoh != 0:
                inutile, inutile, inutile, inutile, vistoh, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxh, myh,
                                                                                                  dati[1], tipoh, -5,
                                                                                                  vistoh, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicoi != 0:
                inutile, inutile, inutile, inutile, vistoi, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxi, myi,
                                                                                                  dati[1], tipoi, -5,
                                                                                                  vistoi, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
            if nemicol != 0:
                inutile, inutile, inutile, inutile, vistol, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxl, myl,
                                                                                                  dati[1], tipol, -5,
                                                                                                  vistol, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti, vetDatiNemici)
        if vistoa or vistob or vistoc or vistod or vistoe or vistof or vistog or vistoh or vistoi or vistol:
            apriocchio = True
        else:
            apriocchio = False

        # fai tutte le animazioni del turno
        primopasso, caricaini, tesoro = anima(sposta, inizio, x, y, vx, vy, rx, ry, vrx, vry, pers, robot, npers, nrob, primopasso, cambiosta, sfondinoa, sfondinob, scudo, armatura, arma, armrob, dati, attacco, difesa, tastop, tesoro, sfondinoc, aumentoliv, carim, mortoa, mxa, mya, mortob, mxb, myb, mortoc, mxc, myc, mortod, mxd, myd, mortoe, mxe, mye, mortof, mxf, myf, mortog, mxg, myg, mortoh, mxh, myh, mortoi, mxi, myi, mortol, mxl, myl, caricaini, caseviste)

        sposta = False

        # disegnare gli sfondi e personaggi
        if not carim and not inizio:
            ambiente_movimento(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers,
                               stanzaa, sfondinoa, sfondinob, sfondinoc, portaVert, portaOriz, arma, armatura, scudo, robot, armrob, nemicoa, mxa, mya, mxav, myav, nemicob, mxb, myb, mxbv, mybv,
                               nemicoc, mxc, myc, mxcv, mycv, nemicod, mxd, myd, mxdv, mydv, nemicoe, mxe, mye, mxev, myev, nemicof, mxf, myf, mxfv, myfv,
                               nemicog, mxg, myg, mxgv, mygv, nemicoh, mxh, myh, mxhv, myhv, nemicoi, mxi, myi, mxiv, myiv, nemicol, mxl, myl, mxlv, mylv,
                               caricaini, vitaesca, porte, cofanetti, caseviste, apriocchio, chiamarob, stanza)

        if not aumentoliv:
            caricaini = False

        vx = x
        vy = y
        vrx = rx
        vry = ry
        if contattogg != 1:
            attacco = 0

        # togiere la morte ai mostri
        if True:
            if mortoa == 1:
                mxa = 0
                mya = 0
                mortoa = 0
            if mortob == 1:
                mxb = 0
                myb = 0
                mortob = 0
            if mortoc == 1:
                mxc = 0
                myc = 0
                mortoc = 0
            if mortod == 1:
                mxd = 0
                myd = 0
                mortod = 0
            if mortoe == 1:
                mxe = 0
                mye = 0
                mortoe = 0
            if mortof == 1:
                mxf = 0
                myf = 0
                mortof = 0
            if mortog == 1:
                mxg = 0
                myg = 0
                mortog = 0
            if mortoh == 1:
                mxh = 0
                myh = 0
                mortoh = 0
            if mortoi == 1:
                mxi = 0
                myi = 0
                mortoi = 0
            if mortol == 1:
                mxl = 0
                myl = 0
                mortol = 0

        if primociclo:
            primociclo = False

        # mostra il framerate
        #if clock.get_fps() < 27:
        #    print (clock.get_fps())

        pygame.display.update()
        clock.tick(fps)

gameloop()

'''pygame.draw.rect(schermo, grigioscu, (gsx // 32 * 0, gsy // 18 * 0, gpx * 16, gpy * 3))
                    messaggio("Aumento Lv: Pv +", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                    messaggio("Aumento Lv: Attacco +", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                    messaggio("Aumento Lv: Difesa +", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
                    pygame.display.update()
                    pygame.time.wait(500)
                    risposta = False
                    while not risposta:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    selezione.play()
                                    risposta = True
                    caricaini = True
                    tesoro = -1'''

'''if esc:
    schermo.fill(grigioscu)
    messaggio("Fine", grigiochi, gsx // 32 * 14, gsy // 18 * 8, 150)
    pygame.display.update()
    pygame.time.wait(500)
    pygame.quit()
    quit()'''
'''# linea(dove,colore,inizio,fine,spessore)
pygame.draw.line(schermo, verde, (0, 0), (gsx, gsy), 10)
# cerchio(dove,colore,centro,raggio,spessore)
pygame.draw.circle(schermo, blu, (300, 100), 5)
# rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
pygame.draw.rect(schermo, rosso, (200, 100, 30, 40), 5)'''
'''# canzone
c1 = pygame.mixer.Sound("Audio\Canzone11.wav")
c1.play(-1))'''
