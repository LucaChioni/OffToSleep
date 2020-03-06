# -*- coding: utf-8 -*-

import ctypes
import pygame
# i suoi vengono velocizzati: metti 0,8 in velocità di audacity per risolvere
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
#pygame.mixer.init(44100, -16, 1, 512)
#pygame.mixer.init(22100, -16, 2, 64)
pygame.init()

# adattamento schermo
ctypes.windll.user32.SetProcessDPIAware()
gsx = ctypes.windll.user32.GetSystemMetrics(0)
gsy = ctypes.windll.user32.GetSystemMetrics(1)
opzioni_schermo = pygame.FULLSCREEN | pygame.HWSURFACE
print (gsx, gsy)
if gsx % 32 != 0 or gsy % 18 != 0:
    while gsx % 32 != 0:
        gsx = gsx - 1
    while gsy % 18 != 0:
        gsy = gsy - 1
if gsx // 16 < gsy // 9:
    print("altezza piu grande")
    gsy = gsx * 9 // 16
elif gsx // 16 > gsy // 9:
    print("larghezza piu grande")
    gsx = gsy * 16 // 9
schermo = pygame.display.set_mode((gsx, gsy), opzioni_schermo)
print (gsx, gsy)

# dimensione personaggio
gpx = gsx // 32
gpy = gsy // 18

# nome-icona
pygame.display.set_caption("Gioco 2")
icona = pygame.image.load("Immagini/Icona.png")
pygame.display.set_icon(icona)

# clock
clockAttacco = pygame.time.Clock()
clockAnimazioni = pygame.time.Clock()
clockVideo = pygame.time.Clock()
clockMenu = pygame.time.Clock()
clockFadeToBlack = pygame.time.Clock()
fpsAnimazioni = 30
fpsInquadra = 20
fpsVideo = 12
fpsMenu = 20
fpsFadeToBlack = 30

# colori
nero = (0, 0, 0)
grigioscu = (50, 50, 50)
grigio = (80, 80, 80)
grigiochi = (230, 230, 230)
bianco = (255, 255, 255)
rosso = (255, 130, 0)
verde = (130, 255, 0)
verdescu = (0, 120, 0)
blu = (0, 0, 255)

# puntatore
puntatoreorigi = pygame.image.load("Immagini/Puntatori/Puntatore.png")
puntatore = pygame.transform.scale(puntatoreorigi, (gpx, gpy))
puntatoreorigivecchio = pygame.image.load("Immagini/Puntatori/Puntatorevecchio.png")
puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx, gpy))
puntatIn = pygame.image.load('Immagini/Puntatori/InquadraCVin.png')
puntatIn = pygame.transform.scale(puntatIn, (gpx, gpy))
puntatOut = pygame.image.load('Immagini/Puntatori/InquadraCVout.png')
puntatOut = pygame.transform.scale(puntatOut, (gpx, gpy))
puntatDif = pygame.image.load('Immagini/Oggetti/Difesa.png')
puntatDif = pygame.transform.scale(puntatDif, (gpx, gpy))
puntatAtt = pygame.image.load('Immagini/Oggetti/Attacco.png')
puntatAtt = pygame.transform.scale(puntatAtt, (gpx, gpy))
puntatArc = pygame.image.load('Immagini/Oggetti/AttaccoDistanza.png')
puntatArc = pygame.transform.scale(puntatArc, (gpx, gpy))
puntatPor = pygame.image.load('Immagini/Oggetti/ApriChiudiPorta.png')
puntatPor = pygame.transform.scale(puntatPor, (gpx, gpy))
puntatCof = pygame.image.load('Immagini/Oggetti/ApriCofanetto.png')
puntatCof = pygame.transform.scale(puntatCof, (gpx, gpy))
puntatSpinta = pygame.image.load('Immagini/Oggetti/SpingiColco.png')
puntatSpinta = pygame.transform.scale(puntatSpinta, (gpx, gpy))
puntatBom = pygame.image.load('Immagini/Oggetti/Oggetto6Ico.png')
puntatBom = pygame.transform.scale(puntatBom, (gpx, gpy))
puntatBoV = pygame.image.load('Immagini/Oggetti/Oggetto7Ico.png')
puntatBoV = pygame.transform.scale(puntatBoV, (gpx, gpy))
puntatEsc = pygame.image.load('Immagini/Oggetti/Oggetto8Ico.png')
puntatEsc = pygame.transform.scale(puntatEsc, (gpx, gpy))
puntatBoA = pygame.image.load('Immagini/Oggetti/Oggetto9Ico.png')
puntatBoA = pygame.transform.scale(puntatBoA, (gpx, gpy))
puntatBoP = pygame.image.load('Immagini/Oggetti/Oggetto10Ico.png')
puntatBoP = pygame.transform.scale(puntatBoP, (gpx, gpy))
scorriSu = pygame.image.load("Immagini/Puntatori/ScorriOggettiSu.png")
scorriSu = pygame.transform.scale(scorriSu, (gpx, gpy))
scorriGiu = pygame.image.load("Immagini/Puntatori/ScorriOggettiGiu.png")
scorriGiu = pygame.transform.scale(scorriGiu, (gpx, gpy))
puntatDialoghi = pygame.image.load('Immagini/Oggetti/IcoDialogo.png')
puntatDialoghi = pygame.transform.scale(puntatDialoghi, (gpx, gpy))
puntatoreInquadraNemici = pygame.image.load("Immagini/Puntatori/InquadraNemicoSelezionato.png")
puntatoreInquadraNemici = pygame.transform.scale(puntatoreInquadraNemici, (gpx, gpy))

# immagini personaggio
persw = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio4.png')
persw = pygame.transform.scale(persw, (gpx, gpy))
perswb = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio4b.png')
perswb = pygame.transform.scale(perswb, (gpx, gpy))
persa = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio3.png')
persa = pygame.transform.scale(persa, (gpx, gpy))
persab = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio3b.png')
persab = pygame.transform.scale(persab, (gpx, gpy))
perso = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio1.png')
perss = pygame.transform.scale(perso, (gpx, gpy))
persob = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio1b.png')
perssb = pygame.transform.scale(persob, (gpx, gpy))
persd = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio2.png')
persd = pygame.transform.scale(persd, (gpx, gpy))
persdb = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio2b.png')
persdb = pygame.transform.scale(persdb, (gpx, gpy))
perssm = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio1mov.png')
perssm = pygame.transform.scale(perssm, (gpx, gpy))
perssmb1 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio1movb1.png')
perssmb1 = pygame.transform.scale(perssmb1, (gpx, gpy))
perssmb2 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio1movb2.png')
perssmb2 = pygame.transform.scale(perssmb2, (gpx, gpy))
persdm = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio2mov.png')
persdm = pygame.transform.scale(persdm, (gpx, gpy))
persdmb1 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio2movb1.png')
persdmb1 = pygame.transform.scale(persdmb1, (gpx, gpy))
persdmb2 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio2movb2.png')
persdmb2 = pygame.transform.scale(persdmb2, (gpx, gpy))
persam = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio3mov.png')
persam = pygame.transform.scale(persam, (gpx, gpy))
persamb1 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio3movb1.png')
persamb1 = pygame.transform.scale(persamb1, (gpx, gpy))
persamb2 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio3movb2.png')
persamb2 = pygame.transform.scale(persamb2, (gpx, gpy))
perswm = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio4mov.png')
perswm = pygame.transform.scale(perswm, (gpx, gpy))
perswmb1 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio4movb1.png')
perswmb1 = pygame.transform.scale(perswmb1, (gpx, gpy))
perswmb2 = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio4movb2.png')
perswmb2 = pygame.transform.scale(perswmb2, (gpx, gpy))
perswmbAttacco = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio4movbAttacco.png')
perswmbAttacco = pygame.transform.scale(perswmbAttacco, (gpx, gpy))
persambAttacco = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio3movbAttacco.png')
persambAttacco = pygame.transform.scale(persambAttacco, (gpx, gpy))
perssmbAttacco = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio1movbAttacco.png')
perssmbAttacco = pygame.transform.scale(perssmbAttacco, (gpx, gpy))
persdmbAttacco = pygame.image.load('Immagini/Personaggi/Rallo/Personaggio2movbAttacco.png')
persdmbAttacco = pygame.transform.scale(persdmbAttacco, (gpx, gpy))
persmbDifesa = pygame.image.load('Immagini/Personaggi/Rallo/PersonaggiomovbDifesa.png')
persmbDifesa = pygame.transform.scale(persmbDifesa, (gpx, gpy))
persAvvele = pygame.image.load('Immagini/Personaggi/Rallo/PersonaggioAvvelenato.png')
persAvvele = pygame.transform.scale(persAvvele, (gpx, gpy))
persGrafMenu = pygame.image.load('Immagini/Disegnigraf/PersonaggioGrafMenu.png')
persGrafInizio = pygame.image.load('Immagini/Disegnigraf/PersonaggioGrafInizio.png')

# immagini robot
robow = pygame.image.load('Immagini/Personaggi/Colco/Robot4.png')
robow = pygame.transform.scale(robow, (gpx, gpy))
roboa = pygame.image.load('Immagini/Personaggi/Colco/Robot3.png')
roboa = pygame.transform.scale(roboa, (gpx, gpy))
roboo = pygame.image.load('Immagini/Personaggi/Colco/Robot1.png')
robos = pygame.transform.scale(roboo, (gpx, gpy))
robod = pygame.image.load('Immagini/Personaggi/Colco/Robot2.png')
robod = pygame.transform.scale(robod, (gpx, gpy))
robomo = pygame.image.load('Immagini/Personaggi/Colco/Robot0.png')
robomo = pygame.transform.scale(robomo, (gpx, gpy))
robodp = pygame.image.load('Immagini/Personaggi/Colco/Robot2p.png')
robodp = pygame.transform.scale(robodp, (gpx, gpy))
roboap = pygame.image.load('Immagini/Personaggi/Colco/Robot3p.png')
roboap = pygame.transform.scale(roboap, (gpx, gpy))
armrobmo = pygame.image.load('Immagini/EquipRobo/Batteria00.png')
armrobmo = pygame.transform.scale(armrobmo, (gpx, gpy))
roboSurrisc = pygame.image.load('Immagini/Personaggi/Colco/RobotSurriscaldato.png')
roboSurrisc = pygame.transform.scale(roboSurrisc, (gpx, gpy))
robogra = pygame.image.load('Immagini/Disegnigraf/RobotGraf.png')
robograf = pygame.image.load('Immagini/Disegnigraf/RobotGraf2.png')
robograff = pygame.image.load('Immagini/Disegnigraf/RobotGraf3.png')
robografff = pygame.image.load('Immagini/Disegnigraf/RobotGraf4.png')
robograffff = pygame.image.load('Immagini/Disegnigraf/RobotGrafsalva.png')

# img menu mercante
mercanteGraf = pygame.image.load('Immagini/Disegnigraf/Mercante.png')
mercanteGraf = pygame.transform.scale(mercanteGraf, (gpx * 12, gpy * 9))
scorriSuGiu = pygame.image.load('Immagini/Puntatori/ScorriSuGiu.png')
scorriSuGiu = pygame.transform.scale(scorriSuGiu, (gpx, gpy))
scorriSuGiuBloccato = pygame.image.load('Immagini/Puntatori/ScorriSuGiuBloccato.png')
scorriSuGiuBloccato = pygame.transform.scale(scorriSuGiuBloccato, (gpx, gpy))
sfondoDialogoMercante = pygame.image.load('Immagini/DecorazioniMenu/SfondoDialogoMercante.png')
sfondoDialogoMercante = pygame.transform.scale(sfondoDialogoMercante, (int(gpx * 9.5), int(gpy * 4.5)))
faretra1Menu = pygame.image.load('Immagini/Oggetti/Faretra1Menu.png')
faretra1Menu = pygame.transform.scale(faretra1Menu, (gpx * 8, gpy * 8))
faretra2Menu = pygame.image.load('Immagini/Oggetti/Faretra2Menu.png')
faretra2Menu = pygame.transform.scale(faretra2Menu, (gpx * 8, gpy * 8))
faretra3Menu = pygame.image.load('Immagini/Oggetti/Faretra3Menu.png')
faretra3Menu = pygame.transform.scale(faretra3Menu, (gpx * 8, gpy * 8))
frecciaMenu = pygame.image.load('Immagini/Oggetti/FrecciaMenu.png')
frecciaMenu = pygame.transform.scale(frecciaMenu, (gpx * 8, gpy * 8))

# indicatori vita
indvita = pygame.image.load('Immagini/Barrevita/Indvita.png')
fineindvita = pygame.image.load('Immagini/Barrevita/FineIndVita.png')
vitanemico00 = pygame.image.load('Immagini/Barrevita/Vitanemico00.png')
vitanemico0 = pygame.image.load('Immagini/Barrevita/Vitanemico0.png')
vitanemico1 = pygame.image.load('Immagini/Barrevita/Vitanemico1.png')
vitanemico2 = pygame.image.load('Immagini/Barrevita/Vitanemico2.png')
vitanemico3 = pygame.image.load('Immagini/Barrevita/Vitanemico3.png')
vitanemico4 = pygame.image.load('Immagini/Barrevita/Vitanemico4.png')
vitanemico5 = pygame.image.load('Immagini/Barrevita/Vitanemico5.png')
vitanemico6 = pygame.image.load('Immagini/Barrevita/Vitanemico6.png')
vitanemico7 = pygame.image.load('Immagini/Barrevita/Vitanemico7.png')
vitanemico8 = pygame.image.load('Immagini/Barrevita/Vitanemico8.png')
vitanemico9 = pygame.image.load('Immagini/Barrevita/Vitanemico9.png')
vitapersonaggio = pygame.image.load('Immagini/Barrevita/Vitapersonaggio.png')
vitarobo = pygame.image.load('Immagini/Barrevita/Vitarobo.png')

# sfondi
sfondostax3 = pygame.image.load('Immagini/Status/Sfondostax3.png')
sfondosta = pygame.image.load('Immagini/Status/SfondoRallo.png')
sfondoRallo = pygame.transform.scale(sfondosta, (gpx * 6, gpy))
sfondosta = pygame.image.load('Immagini/Status/SfondoColco.png')
sfondoColco = pygame.transform.scale(sfondosta, (gpx * 4, gpy))
sfondosta = pygame.image.load('Immagini/Status/SfondoNemici.png')
sfondoMostro = pygame.transform.scale(sfondosta, (gpx * 3, gpy))
sfondosta = pygame.image.load('Immagini/Status/SfondoEsche.png')
sfondoEsche = pygame.transform.scale(sfondosta, (gpx, gpy))
sfondoStartBattaglia = pygame.image.load('Immagini/Oggetti/SfondoStartBattaglia.png')
sfondoStartBattaglia = pygame.transform.scale(sfondoStartBattaglia, (gpx * 7, gpy * 7))
sfondoStatAumentata = pygame.image.load('Immagini/Levelup/SfondoStatisticaAumentata.png')
sfondoStatAumentata = pygame.transform.scale(sfondoStatAumentata, (gpx * 7, gpy * 7))
sfondoTriangolinoAltoDestra = pygame.image.load('Immagini/DecorazioniMenu/TriangoloAltoDestra.png')
sfondoTriangolinoAltoDestra = pygame.transform.scale(sfondoTriangolinoAltoDestra, (gpx, gpy))
sfondoTriangolinoAltoSinistra = pygame.image.load('Immagini/DecorazioniMenu/TriangoloAltoSinistra.png')
sfondoTriangolinoAltoSinistra = pygame.transform.scale(sfondoTriangolinoAltoSinistra, (gpx, gpy))
sfondoTriangolinoBassoDestra = pygame.image.load('Immagini/DecorazioniMenu/TriangoloBassoDestra.png')
sfondoTriangolinoBassoDestra = pygame.transform.scale(sfondoTriangolinoBassoDestra, (gpx, gpy))
sfondoTriangolinoBassoSinistra = pygame.image.load('Immagini/DecorazioniMenu/TriangoloBassoSinistra.png')
sfondoTriangolinoBassoSinistra = pygame.transform.scale(sfondoTriangolinoBassoSinistra, (gpx, gpy))

# status
appiccicosoo = pygame.image.load('Immagini/Status/Appiccicoso.png')
appiccicoso = pygame.transform.scale(appiccicosoo, (gpx * 3 // 4, gpy * 3 // 4))
avvelenatoo = pygame.image.load('Immagini/Status/Avvelenato.png')
avvelenato = pygame.transform.scale(avvelenatoo, (gpx * 3 // 4, gpy * 3 // 4))
surriscaldatoo = pygame.image.load('Immagini/Status/Surriscaldato.png')
surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx * 3 // 4, gpy * 3 // 4))
attaccopiuo = pygame.image.load('Immagini/Status/Attaccopiu.png')
attaccopiu = pygame.transform.scale(attaccopiuo, (gpx * 3 // 4, gpy * 3 // 4))
difesapiuo = pygame.image.load('Immagini/Status/Difesapiu.png')
difesapiu = pygame.transform.scale(difesapiuo, (gpx * 3 // 4, gpy * 3 // 4))
velocitapiuo = pygame.image.load('Immagini/Status/Velocitapiu.png')
velocitapiu = pygame.transform.scale(velocitapiuo, (gpx * 3 // 4, gpy * 3 // 4))
efficienzapiuo = pygame.image.load('Immagini/Status/Efficienzapiu.png')
efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx * 3 // 4, gpy * 3 // 4))
imgNumFrecce = pygame.image.load('Immagini/Status/NumFrecce.png')
imgNumFrecce = pygame.transform.scale(imgNumFrecce, (gpx * 3 // 4, gpy * 3 // 4))

# menu alto destra
sfochiaveocchio = pygame.image.load("Immagini/Oggetti/SfondoOcchioChiave.png")
sfochiaveocchio = pygame.transform.scale(sfochiaveocchio, (gpx * 5, gpy * 2))
occhioape = pygame.image.load('Immagini/Status/OcchioAperto.png')
occhioape = pygame.transform.scale(occhioape, (gpx, gpy))
occhiochiu = pygame.image.load('Immagini/Status/OcchioChiuso.png')
occhiochiu = pygame.transform.scale(occhiochiu, (gpx, gpy))
chiaveroboacc = pygame.image.load('Immagini/Oggetti/ChiaveColcoAcc.png')
chiaveroboacc = pygame.transform.scale(chiaveroboacc, (gpx * 2, gpy * 2))
chiaverobospe = pygame.image.load('Immagini/Oggetti/ChiaveColcoSpe.png')
chiaverobospe = pygame.transform.scale(chiaverobospe, (gpx * 2, gpy * 2))

# oggetti sulla schermata
esche = pygame.image.load("Immagini/Oggetti/Oggetto8Ico.png")
esche = pygame.transform.scale(esche, (gpx, gpy))
sacchettoDenaroStart = pygame.image.load('Immagini/Oggetti/SacchettoDenaroSinistra.png')
sacchettoDenaroStart = pygame.transform.scale(sacchettoDenaroStart, (gpx * 4, gpy * 4))
sacchettoDenaroMercante = pygame.image.load('Immagini/Oggetti/SacchettoDenaroDestra.png')
sacchettoDenaroMercante = pygame.transform.scale(sacchettoDenaroMercante, (gpx * 4, gpy * 4))
faretraFrecceStart0 = pygame.image.load('Immagini/EquipRallo/Faretre/Faretra0Menu.png')
faretraFrecceStart0 = pygame.transform.scale(faretraFrecceStart0, (gpx * 4, gpy * 4))
faretraFrecceStart1 = pygame.image.load('Immagini/EquipRallo/Faretre/Faretra1Menu.png')
faretraFrecceStart1 = pygame.transform.scale(faretraFrecceStart1, (gpx * 4, gpy * 4))
faretraFrecceStart2 = pygame.image.load('Immagini/EquipRallo/Faretre/Faretra2Menu.png')
faretraFrecceStart2 = pygame.transform.scale(faretraFrecceStart2, (gpx * 4, gpy * 4))
faretraFrecceStart3 = pygame.image.load('Immagini/EquipRallo/Faretre/Faretra3Menu.png')
faretraFrecceStart3 = pygame.transform.scale(faretraFrecceStart3, (gpx * 4, gpy * 4))
sacchettoDenaroo = pygame.image.load('Immagini/Oggetti/SacchettoDenaroIco.png')
sacchettoDenaro = pygame.transform.scale(sacchettoDenaroo, (gpx, gpy))
imgFrecciaLanciata = pygame.image.load('Immagini/Oggetti/Freccia.png')
imgFrecciaLanciata = pygame.transform.scale(imgFrecciaLanciata, (gpx, gpy))

# cofanetti
cofaniaper = pygame.image.load("Immagini/Oggetti/CofanettoAperto.png")
cofaniaper = pygame.transform.scale(cofaniaper, (gpx, gpy))
cofanichiu = pygame.image.load("Immagini/Oggetti/CofanettoChiuso.png")
cofanichiu = pygame.transform.scale(cofanichiu, (gpx, gpy))
sfocontcof = pygame.image.load("Immagini/Oggetti/SfondoContenutoCofanetto.png")
sfocontcof = pygame.transform.scale(sfocontcof, (gpx * 16, gpy * 3))

# immagini salvataggi
s1 = pygame.image.load('Immagini/Salvataggi/S1.png')
s1 = pygame.transform.scale(s1, (gpx * 3, gpy * 3))
s2 = pygame.image.load('Immagini/Salvataggi/S2.png')
s2 = pygame.transform.scale(s2, (gpx * 3, gpy * 3))
s3 = pygame.image.load('Immagini/Salvataggi/S3.png')
s3 = pygame.transform.scale(s3, (gpx * 3, gpy * 3))

# caselle attaccabili
campoattaccabile1 = pygame.image.load('Immagini/Campiattaccabili/Campoattaccabile1.png')
campoattaccabile1 = pygame.transform.scale(campoattaccabile1, (gpx * 3, gpy * 3))
campoattaccabile2 = pygame.image.load('Immagini/Campiattaccabili/Campoattaccabile2.png')
campoattaccabileRobo = pygame.image.load('Immagini/Campiattaccabili/Campoattaccabile3.png')
campoattaccabileRobo = pygame.transform.scale(campoattaccabileRobo, (gpx * 6, gpy * 6))
caselleattaccabiliRobo = pygame.image.load('Immagini/Campiattaccabili/CaselleattaccabiliRobo.png')
caselleattaccabiliRobo = pygame.transform.scale(caselleattaccabiliRobo, (gpx, gpy))
campoattaccabilemostro = pygame.image.load('Immagini/Campiattaccabili/Campoattaccabilemostro.png')
caselleattaccabilimostro = pygame.image.load('Immagini/Campiattaccabili/Caselleattaccabilimostro.png')
caselleattaccabilimostro = pygame.transform.scale(caselleattaccabilimostro, (gpx, gpy))
caselleattaccabili = pygame.image.load('Immagini/Campiattaccabili/Caselleattaccabili.png')
caselleattaccabili = pygame.transform.scale(caselleattaccabili, (gpx, gpy))

# aumento livello
saliliv = pygame.image.load('Immagini/Levelup/Saliliv.png')
saliliv = pygame.transform.scale(saliliv, (gpx, gpy))
saliliv1 = pygame.image.load('Immagini/Levelup/Saliliv1.png')
saliliv1 = pygame.transform.scale(saliliv1, (gpx, gpy))
saliliv2 = pygame.image.load('Immagini/Levelup/Saliliv2.png')
saliliv2 = pygame.transform.scale(saliliv2, (gpx, gpy))

# img equipaggiamento, condizioni, tecniche, oggetti
sfondoOggettoMenu = pygame.image.load("Immagini/EquipRallo/SfondoOggetto.png")
sconosciutoEquipMenu = pygame.image.load("Immagini/Oggetti/SconosciutoEquip.png")
sconosciutoOggettoMenu = pygame.image.load("Immagini/Oggetti/Sconosciuto.png")
sconosciutoOggettoIcoMenu = pygame.image.load("Immagini/Oggetti/SconosciutoIco.png")
vetImgSpadeMenu = []
vetImgArchiMenu = []
vetImgArmatureMenu = []
vetImgScudiMenu = []
vetImgGuantiMenu = []
vetImgCollaneMenu = []
contatoreGlobale = 0
while contatoreGlobale < 5:
    vetImgSpadeMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRallo/Spade/Spada%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
    vetImgArchiMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRallo/Archi/Arco%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
    vetImgArmatureMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRallo/Armature/Armatura%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
    vetImgScudiMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
    vetImgGuantiMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
    vetImgCollaneMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRallo/Collane/Collana%iMenu.png" % contatoreGlobale), (int(gpx * 2), int(gpy * 2))))
    contatoreGlobale += 1
vetImgCondizioniMenu = [0]
contatoreGlobale = 1
while contatoreGlobale <= 20:
    vetImgCondizioniMenu.append(pygame.transform.scale(pygame.image.load("Immagini/GrafCondizioni/Condizione%i.png" % contatoreGlobale), (gpx * 12, gpy * 9)))
    contatoreGlobale += 1
vetImgTecnicheMenu = [0]
contatoreGlobale = 1
while contatoreGlobale <= 20:
    vetImgTecnicheMenu.append(pygame.transform.scale(pygame.image.load("Immagini/GrafTecniche/Tecnica%i.png" % contatoreGlobale), (gpx * 12, gpy * 9)))
    contatoreGlobale += 1
vetImgBatterieMenu = []
vetIcoBatterieMenu = []
contatoreGlobale = 0
while contatoreGlobale < 5:
    vetImgBatterieMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRobo/Batteria%is.png" % contatoreGlobale), (gpx * 5, gpy * 5)))
    vetIcoBatterieMenu.append(pygame.transform.scale(pygame.image.load("Immagini/EquipRobo/Batteria%iMenu.png" % contatoreGlobale), (gpx * 2, gpy * 2)))
    contatoreGlobale += 1
vetImgOggettiMenu = []
vetImgOggettiMercante = []
vetImgOggettiStart = []
vetIcoOggettiMenu = []
contatoreGlobale = 1
while contatoreGlobale <= 10:
    vetImgOggettiMenu.append(pygame.transform.scale(pygame.image.load("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale), (gpx * 10, gpy * 10)))
    vetImgOggettiMercante.append(pygame.transform.scale(pygame.image.load("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale), (gpx * 8, gpy * 8)))
    vetImgOggettiStart.append(pygame.transform.scale(pygame.image.load("Immagini/Oggetti/Oggetto%i.png" % contatoreGlobale), (gpx * 4, gpy * 4)))
    vetIcoOggettiMenu.append(pygame.transform.scale(pygame.image.load("Immagini/Oggetti/Oggetto%iIco.png" % contatoreGlobale), (gpx, gpy)))
    contatoreGlobale += 1
# costo oggetti => costoOggetti[frecce, faretra1, faretra2, faretra3, pozione, caricabatterie, medicina, superpozione, caricabatterie migliorato, bomba, bomba veleno, esca, bomba appiccicosa, bomba potenziata]
costoOggetti = [1, 5, 5, 7, 20, 20, 10, 15, 30, 50, 50, 10, 50, 250]

# img equipaggiamento pixellato
vetImgSpadePixellate = []
vetImgArchiPixellate = []
vetImgArmaturePixellate = []
vetImgScudiPixellate = []
vetImgGuantiPixellate = []
vetImgCollanePixellate = []
contatoreGlobale = 0
while contatoreGlobale < 5:
    vetImgSpadePixellate.append(pygame.image.load("Immagini/EquipRallo/Spade/Spada%is.png" % contatoreGlobale))
    vetImgArchiPixellate.append(pygame.image.load("Immagini/EquipRallo/Archi/Arco%is.png" % contatoreGlobale))
    vetImgArmaturePixellate.append(pygame.image.load("Immagini/EquipRallo/Armature/Armatura%is.png" % contatoreGlobale))
    vetImgScudiPixellate.append(pygame.image.load("Immagini/EquipRallo/Scudi/Scudo%is.png" % contatoreGlobale))
    vetImgGuantiPixellate.append(pygame.image.load("Immagini/EquipRallo/Guanti/Guanti%is.png" % contatoreGlobale))
    vetImgCollanePixellate.append(pygame.image.load("Immagini/EquipRallo/Collane/Collana%is.png" % contatoreGlobale))
    contatoreGlobale += 1

# img animazioni oggetti
imgAnimaBomba = pygame.image.load('Immagini/AnimazioniOggetti/Bomba.png')
imgAnimaBomba = pygame.transform.scale(imgAnimaBomba, (gpx * 3, gpy * 3))
imgAnimaBombaVeleno = pygame.image.load('Immagini/AnimazioniOggetti/BombaVeleno.png')
imgAnimaBombaVeleno = pygame.transform.scale(imgAnimaBombaVeleno, (gpx, gpy))
imgAnimaBombaAppiccicosa = pygame.image.load('Immagini/AnimazioniOggetti/BombaAppiccicosa.png')
imgAnimaBombaAppiccicosa = pygame.transform.scale(imgAnimaBombaAppiccicosa, (gpx, gpy))
imgAnimaBombaPotenziata = pygame.image.load('Immagini/AnimazioniOggetti/BombaPotenziata.png')
imgAnimaBombaPotenziata = pygame.transform.scale(imgAnimaBombaPotenziata, (gpx * 5, gpy * 5))
imgAnimaPozione1 = pygame.image.load('Immagini/AnimazioniOggetti/Pozione1.png')
imgAnimaPozione1 = pygame.transform.scale(imgAnimaPozione1, (gpx, gpy))
imgAnimaPozione2 = pygame.image.load('Immagini/AnimazioniOggetti/Pozione2.png')
imgAnimaPozione2 = pygame.transform.scale(imgAnimaPozione2, (gpx, gpy))
imgAnimaMedicina1 = pygame.image.load('Immagini/AnimazioniOggetti/Medicina1.png')
imgAnimaMedicina1 = pygame.transform.scale(imgAnimaMedicina1, (gpx, gpy))
imgAnimaMedicina2 = pygame.image.load('Immagini/AnimazioniOggetti/Medicina2.png')
imgAnimaMedicina2 = pygame.transform.scale(imgAnimaMedicina2, (gpx, gpy))
imgAnimaCaricabatterie = pygame.image.load('Immagini/AnimazioniOggetti/Caricabatterie.png')
imgAnimaCaricabatterie = pygame.transform.scale(imgAnimaCaricabatterie, (gpx, gpy))

# img animazioni tecniche
imgDanneggiamentoColco = pygame.image.load('Immagini/AnimazioniTecniche/Danneggiamento.png')
imgDanneggiamentoColco = pygame.transform.scale(imgDanneggiamentoColco, (gpx, gpy))
vetAnimazioniTecniche = []
nomiTecniche = ["scossa", "scossa+", "scossa++", "freccia", "freccia+", "freccia++", "tempesta", "tempesta+", "tempesta++", "cura", "cura+", "cura++", "antidoto", "attP", "difP", "ricarica", "ricarica+", "raffred", "velocizza", "efficienza"]
for contatoreGlobale in nomiTecniche:
    vetAnimazioniTecniche.append(contatoreGlobale)
    vetAnimaImgTecniche = []
    if contatoreGlobale.startswith("scossa") or contatoreGlobale.startswith("freccia") or contatoreGlobale.startswith("cura") or contatoreGlobale == "antidoto" or contatoreGlobale == "attP" or contatoreGlobale == "difP":
        if contatoreGlobale.startswith("freccia"):
            contatoreGlobale = "freccia"
        img1 = pygame.image.load("Immagini/AnimazioniTecniche/%swAnima1.png" % contatoreGlobale)
        img2 = pygame.image.load("Immagini/AnimazioniTecniche/%swAnima2.png" % contatoreGlobale)
        img1 = pygame.transform.scale(img1, (gpx, gpy * 2))
        img2 = pygame.transform.scale(img2, (gpx, gpy * 2))
        vetAnimaImgTecniche.append(img1)
        vetAnimaImgTecniche.append(img2)
        img1 = pygame.image.load("Immagini/AnimazioniTecniche/%saAnima1.png" % contatoreGlobale)
        img2 = pygame.image.load("Immagini/AnimazioniTecniche/%saAnima2.png" % contatoreGlobale)
        img1 = pygame.transform.scale(img1, (gpx * 2, gpy))
        img2 = pygame.transform.scale(img2, (gpx * 2, gpy))
        vetAnimaImgTecniche.append(img1)
        vetAnimaImgTecniche.append(img2)
        img1 = pygame.image.load("Immagini/AnimazioniTecniche/%ssAnima1.png" % contatoreGlobale)
        img2 = pygame.image.load("Immagini/AnimazioniTecniche/%ssAnima2.png" % contatoreGlobale)
        img1 = pygame.transform.scale(img1, (gpx, gpy * 2))
        img2 = pygame.transform.scale(img2, (gpx, gpy * 2))
        vetAnimaImgTecniche.append(img1)
        vetAnimaImgTecniche.append(img2)
        img1 = pygame.image.load("Immagini/AnimazioniTecniche/%sdAnima1.png" % contatoreGlobale)
        img2 = pygame.image.load("Immagini/AnimazioniTecniche/%sdAnima2.png" % contatoreGlobale)
        img1 = pygame.transform.scale(img1, (gpx * 2, gpy))
        img2 = pygame.transform.scale(img2, (gpx * 2, gpy))
        vetAnimaImgTecniche.append(img1)
        vetAnimaImgTecniche.append(img2)
    elif contatoreGlobale.startswith("ricarica") or contatoreGlobale == "raffred" or contatoreGlobale == "velocizza" or contatoreGlobale == "efficienza":
        img1 = pygame.image.load("Immagini/AnimazioniTecniche/%sAnima.png" % contatoreGlobale)
        img1 = pygame.transform.scale(img1, (gpx, gpy))
        vetAnimaImgTecniche.append(img1)
    elif contatoreGlobale.startswith("tempesta"):
        img1 = pygame.image.load("Immagini/AnimazioniTecniche/%sAnima1.png" % contatoreGlobale)
        img2 = pygame.image.load("Immagini/AnimazioniTecniche/%sAnima2.png" % contatoreGlobale)
        img1 = pygame.transform.scale(img1, (gpx * 17, gpy * 17))
        img2 = pygame.transform.scale(img2, (gpx * 17, gpy * 17))
        vetAnimaImgTecniche.append(img1)
        vetAnimaImgTecniche.append(img2)
    vetAnimazioniTecniche.append(vetAnimaImgTecniche)
imgFrecciaEletttricaLanciata = pygame.image.load('Immagini/AnimazioniTecniche/FrecciaLanciata.png')
imgFrecciaEletttricaLanciata = pygame.transform.scale(imgFrecciaEletttricaLanciata, (gpx, gpy))
imgFrecciaEletttricaLanciataP = pygame.image.load('Immagini/AnimazioniTecniche/FrecciaLanciata+.png')
imgFrecciaEletttricaLanciataP = pygame.transform.scale(imgFrecciaEletttricaLanciataP, (gpx, gpy))
imgFrecciaEletttricaLanciataPP = pygame.image.load('Immagini/AnimazioniTecniche/FrecciaLanciata++.png')
imgFrecciaEletttricaLanciataPP = pygame.transform.scale(imgFrecciaEletttricaLanciataPP, (gpx, gpy))

# img sfondi dialoghi
sfondoDialoghiSopra = pygame.image.load('Immagini/Dialoghi/SfondoSopra.png')
sfondoDialoghiSopra = pygame.transform.scale(sfondoDialoghiSopra, (gsx, gsy // 3))
sfondoDialoghiSotto = pygame.image.load('Immagini/Dialoghi/SfondoSotto.png')
sfondoDialoghiSotto = pygame.transform.scale(sfondoDialoghiSotto, (gsx, gsy // 3))

# canali audio / volume (0-1)
volumeCanzoni = 0
volumePuntatore = 0
volumeEffetti = 0
pygame.mixer.set_num_channels(8)
canaleSoundCanzone = pygame.mixer.Channel(0)
canaleSoundCanzone.set_volume(volumeCanzoni)
canaleSoundPuntatore = pygame.mixer.Channel(1)
canaleSoundPuntatore.set_volume(volumePuntatore)
canaleSoundPassiRallo = pygame.mixer.Channel(2)
canaleSoundPassiRallo.set_volume(volumeEffetti)
canaleSoundPassiColco = pygame.mixer.Channel(3)
canaleSoundPassiColco.set_volume(volumeEffetti)
canaleSoundPassiNemico = pygame.mixer.Channel(4)
canaleSoundPassiNemico.set_volume(volumeEffetti)
canaleSoundLvUp = pygame.mixer.Channel(5)
canaleSoundLvUp.set_volume(volumeEffetti)
canaleSoundInterazioni = pygame.mixer.Channel(6)
canaleSoundInterazioni.set_volume(volumeEffetti)
canaleSoundAttacco = pygame.mixer.Channel(7)
canaleSoundAttacco.set_volume(volumeEffetti)

# suoni puntatore
selsta = pygame.mixer.Sound("Audio/RumoriPuntatore/SelSta.wav")
selind = pygame.mixer.Sound("Audio/RumoriPuntatore/SelInd.wav")
spostapun = pygame.mixer.Sound("Audio/RumoriPuntatore/SpostaPun.wav")
selimp = pygame.mixer.Sound("Audio/RumoriPuntatore/SelImp.wav")
selezione = pygame.mixer.Sound("Audio/RumoriPuntatore/Selezione.wav")
spostaPunBattaglia = pygame.mixer.Sound("Audio/RumoriPuntatore/SpostaPunBattaglia.wav")
selObbiettivo = pygame.mixer.Sound("Audio/RumoriPuntatore/SelObbiettivo.wav")

# suoni personaggio
rumoreAttaccoSpada = pygame.mixer.Sound("Audio/RumoriPersonaggio/AttaccoSpada.wav")
rumoreLancioFreccia = pygame.mixer.Sound("Audio/RumoriPersonaggio/LancioFreccia.wav")
rumoreAttaccoArco = pygame.mixer.Sound("Audio/RumoriPersonaggio/AttaccoArco.wav")
rumoreParata = pygame.mixer.Sound("Audio/RumoriPersonaggio/ParataConScudo.wav")
rumorecamminata = pygame.mixer.Sound("Audio/RumoriPersonaggio/Camminata.wav")
rumorelevelup = pygame.mixer.Sound("Audio/RumoriPersonaggio/Levelup.wav")

# suoni apertura-chiusura cofanetti-porte
suonoaperturacofanetti = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaCofanetto.wav")
suonoaperturaporte1 = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaPorta1.wav")
suonoaperturaporte2 = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaPorta2.wav")
suonoaperturaporte3 = pygame.mixer.Sound("Audio/RumoriAmbiente/AperturaPorta3.wav")
suonochiusuraporte1 = pygame.mixer.Sound("Audio/RumoriAmbiente/ChiusuraPorta1.wav")
suonochiusuraporte2 = pygame.mixer.Sound("Audio/RumoriAmbiente/ChiusuraPorta2.wav")
suonochiusuraporte3 = pygame.mixer.Sound("Audio/RumoriAmbiente/ChiusuraPorta3.wav")

# souno raccolta esca - monete
suonoRaccoltaEsca = pygame.mixer.Sound("Audio/RumoriAmbiente/RaccoltaEsca.wav")
suonoRaccoltaMonete = pygame.mixer.Sound("Audio/RumoriAmbiente/RaccoltaMonete.wav")
rumoreAcquisto = pygame.mixer.Sound("Audio/RumoriAmbiente/Acquisto.wav")

# suoni robo
rumoreCamminataColco = pygame.mixer.Sound("Audio/RumoriColco/Camminata.wav")
rumoreScossaFreccia = pygame.mixer.Sound("Audio/RumoriColco/ScossaFreccia.wav")
rumoreTempestaElettrica = pygame.mixer.Sound("Audio/RumoriColco/TempestaElettrica.wav")
rumoreCuraRobo = pygame.mixer.Sound("Audio/RumoriColco/Cura.wav")
rumoreAntidoto = pygame.mixer.Sound("Audio/RumoriColco/Antidoto.wav")
rumoreAttPDifP = pygame.mixer.Sound("Audio/RumoriColco/AttPDifP.wav")
rumoreAutoricarica = pygame.mixer.Sound("Audio/RumoriColco/Autoricarica.wav")
rumoreRaffreddamento = pygame.mixer.Sound("Audio/RumoriColco/Raffreddamento.wav")
rumoreVelocizzaEfficienza = pygame.mixer.Sound("Audio/RumoriColco/VelocizzaEfficienza.wav")

# suono oggetti
suonoTeleColco = pygame.mixer.Sound("Audio/RumoriOggetti/TeleColco.wav")
suonoLancioOggetti = pygame.mixer.Sound("Audio/RumoriOggetti/LancioOggetti.wav")
suonoUsoPozione = pygame.mixer.Sound("Audio/RumoriOggetti/Pozione.wav")
suonoUsoCaricabatterie = pygame.mixer.Sound("Audio/RumoriOggetti/Caricabatterie.wav")
suonoUsoMedicina = pygame.mixer.Sound("Audio/RumoriOggetti/Medicina.wav")
suonoUsoBomba = pygame.mixer.Sound("Audio/RumoriOggetti/Bomba.wav")
suonoUsoBombaVeleno = pygame.mixer.Sound("Audio/RumoriOggetti/BombaVeleno.wav")
suonoUsoEsca = pygame.mixer.Sound("Audio/RumoriOggetti/Esca.wav")
suonoUsoBombaAppiccicosa = pygame.mixer.Sound("Audio/RumoriOggetti/BombaAppiccicosa.wav")
suonoUsoBombaPotenziata = pygame.mixer.Sound("Audio/RumoriOggetti/BombaPotenziata.wav")

# suoni canzoni
c11 = pygame.mixer.Sound("Audio/Canzoni/Canzone11.wav")
c27 = pygame.mixer.Sound("Audio/Canzoni/Canzone27.wav")

# dati tecniche di Colco [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesa++]
costoTecniche = [5, 10, 10, 5, 10, 10, 1, 20, 10, 10, 15, 20, 20, 30, 20, 30, 1, 20, 20, 40]
dannoTecniche = [40, 30, 0, 30, 20, 0, 150, 120, 160, 130, 15, 10, 10, 15, 100, 250, 300, 320, 260, 200]
