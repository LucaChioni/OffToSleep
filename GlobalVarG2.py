# -*- coding: utf-8 -*-

import ctypes
import pygame
pygame.mixer.init(44100, -16, 1, 512)
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
fpsAnimazioni = 30
fpsInquadra = 20
fpsVideo = 12

# colori
nero = (0, 0, 0)
grigioscu = (50, 50, 50)
grigio = (80, 80, 80)
grigiochi = (230, 230, 230)
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
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
puntatPor = pygame.image.load('Immagini/Oggetti/ApriChiudiPorta.png')
puntatPor = pygame.transform.scale(puntatPor, (gpx, gpy))
puntatCof = pygame.image.load('Immagini/Oggetti/ApriCofanetto.png')
puntatCof = pygame.transform.scale(puntatCof, (gpx, gpy))
puntatSpinta = pygame.image.load('Immagini/Oggetti/SpingiColco.png')
puntatSpinta = pygame.transform.scale(puntatSpinta, (gpx, gpy))
puntatBom = pygame.image.load('Immagini/Oggetti/Bomba.png')
puntatBom = pygame.transform.scale(puntatBom, (gpx, gpy))
puntatBoV = pygame.image.load('Immagini/Oggetti/BombaVeleno.png')
puntatBoV = pygame.transform.scale(puntatBoV, (gpx, gpy))
puntatEsc = pygame.image.load('Immagini/Oggetti/Esca.png')
puntatEsc = pygame.transform.scale(puntatEsc, (gpx, gpy))
puntatBoA = pygame.image.load('Immagini/Oggetti/BombaAppiccicosa.png')
puntatBoA = pygame.transform.scale(puntatBoA, (gpx, gpy))
puntatBoP = pygame.image.load('Immagini/Oggetti/BombaPotenziata.png')
puntatBoP = pygame.transform.scale(puntatBoP, (gpx, gpy))
scorriSu = pygame.image.load("Immagini/Puntatori/ScorriOggettiSu.png")
scorriSu = pygame.transform.scale(scorriSu, (gpx, gpy))
scorriGiu = pygame.image.load("Immagini/Puntatori/ScorriOggettiGiu.png")
scorriGiu = pygame.transform.scale(scorriGiu, (gpx, gpy))

# immagini personaggio
persw = pygame.image.load('Immagini/Personaggi/Personaggio4.png')
persw = pygame.transform.scale(persw, (gpx, gpy))
perswb = pygame.image.load('Immagini/Personaggi/Personaggio4b.png')
perswb = pygame.transform.scale(perswb, (gpx, gpy))
persa = pygame.image.load('Immagini/Personaggi/Personaggio3.png')
persa = pygame.transform.scale(persa, (gpx, gpy))
persab = pygame.image.load('Immagini/Personaggi/Personaggio3b.png')
persab = pygame.transform.scale(persab, (gpx, gpy))
perso = pygame.image.load('Immagini/Personaggi/Personaggio1.png')
perss = pygame.transform.scale(perso, (gpx, gpy))
persob = pygame.image.load('Immagini/Personaggi/Personaggio1b.png')
perssb = pygame.transform.scale(persob, (gpx, gpy))
persd = pygame.image.load('Immagini/Personaggi/Personaggio2.png')
persd = pygame.transform.scale(persd, (gpx, gpy))
persdb = pygame.image.load('Immagini/Personaggi/Personaggio2b.png')
persdb = pygame.transform.scale(persdb, (gpx, gpy))
perssm = pygame.image.load('Immagini/Personaggi/Personaggio1mov.png')
perssm = pygame.transform.scale(perssm, (gpx, gpy))
perssmb1 = pygame.image.load('Immagini/Personaggi/Personaggio1movb1.png')
perssmb1 = pygame.transform.scale(perssmb1, (gpx, gpy))
perssmb2 = pygame.image.load('Immagini/Personaggi/Personaggio1movb2.png')
perssmb2 = pygame.transform.scale(perssmb2, (gpx, gpy))
persdm = pygame.image.load('Immagini/Personaggi/Personaggio2mov.png')
persdm = pygame.transform.scale(persdm, (gpx, gpy))
persdmb1 = pygame.image.load('Immagini/Personaggi/Personaggio2movb1.png')
persdmb1 = pygame.transform.scale(persdmb1, (gpx, gpy))
persdmb2 = pygame.image.load('Immagini/Personaggi/Personaggio2movb2.png')
persdmb2 = pygame.transform.scale(persdmb2, (gpx, gpy))
persam = pygame.image.load('Immagini/Personaggi/Personaggio3mov.png')
persam = pygame.transform.scale(persam, (gpx, gpy))
persamb1 = pygame.image.load('Immagini/Personaggi/Personaggio3movb1.png')
persamb1 = pygame.transform.scale(persamb1, (gpx, gpy))
persamb2 = pygame.image.load('Immagini/Personaggi/Personaggio3movb2.png')
persamb2 = pygame.transform.scale(persamb2, (gpx, gpy))
perswm = pygame.image.load('Immagini/Personaggi/Personaggio4mov.png')
perswm = pygame.transform.scale(perswm, (gpx, gpy))
perswmb1 = pygame.image.load('Immagini/Personaggi/Personaggio4movb1.png')
perswmb1 = pygame.transform.scale(perswmb1, (gpx, gpy))
perswmb2 = pygame.image.load('Immagini/Personaggi/Personaggio4movb2.png')
perswmb2 = pygame.transform.scale(perswmb2, (gpx, gpy))
perswmbAttacco = pygame.image.load('Immagini/Personaggi/Personaggio4movbAttacco.png')
perswmbAttacco = pygame.transform.scale(perswmbAttacco, (gpx, gpy))
persambAttacco = pygame.image.load('Immagini/Personaggi/Personaggio3movbAttacco.png')
persambAttacco = pygame.transform.scale(persambAttacco, (gpx, gpy))
perssmbAttacco = pygame.image.load('Immagini/Personaggi/Personaggio1movbAttacco.png')
perssmbAttacco = pygame.transform.scale(perssmbAttacco, (gpx, gpy))
persdmbAttacco = pygame.image.load('Immagini/Personaggi/Personaggio2movbAttacco.png')
persdmbAttacco = pygame.transform.scale(persdmbAttacco, (gpx, gpy))
persmbDifesa = pygame.image.load('Immagini/Personaggi/PersonaggiomovbDifesa.png')
persmbDifesa = pygame.transform.scale(persmbDifesa, (gpx, gpy))
persAvvele = pygame.image.load('Immagini/Personaggi/PersonaggioAvvelenato.png')
persAvvele = pygame.transform.scale(persAvvele, (gpx, gpy))
persGrafMenu = pygame.image.load('Immagini/Disegnigraf/PersonaggioGrafMenu.png')
persGrafInizio = pygame.image.load('Immagini/Disegnigraf/PersonaggioGrafInizio.png')

# immagini robot
robow = pygame.image.load('Immagini/Personaggi/Robot4.png')
robow = pygame.transform.scale(robow, (gpx, gpy))
roboa = pygame.image.load('Immagini/Personaggi/Robot3.png')
roboa = pygame.transform.scale(roboa, (gpx, gpy))
roboo = pygame.image.load('Immagini/Personaggi/Robot1.png')
robos = pygame.transform.scale(roboo, (gpx, gpy))
robod = pygame.image.load('Immagini/Personaggi/Robot2.png')
robod = pygame.transform.scale(robod, (gpx, gpy))
robomo = pygame.image.load('Immagini/Personaggi/Robot0.png')
robomo = pygame.transform.scale(robomo, (gpx, gpy))
robodp = pygame.image.load('Immagini/Personaggi/Robot2p.png')
robodp = pygame.transform.scale(robodp, (gpx, gpy))
roboap = pygame.image.load('Immagini/Personaggi/Robot3p.png')
roboap = pygame.transform.scale(roboap, (gpx, gpy))
armrobmo = pygame.image.load('Immagini/EquipRobo/Batteria00.png')
armrobmo = pygame.transform.scale(armrobmo, (gpx, gpy))
roboSurrisc = pygame.image.load('Immagini/Personaggi/RobotSurriscaldato.png')
roboSurrisc = pygame.transform.scale(roboSurrisc, (gpx, gpy))
robogra = pygame.image.load('Immagini/Disegnigraf/RobotGraf.png')
robograf = pygame.image.load('Immagini/Disegnigraf/RobotGraf2.png')
robograff = pygame.image.load('Immagini/Disegnigraf/RobotGraf3.png')
robografff = pygame.image.load('Immagini/Disegnigraf/RobotGraf4.png')
robograffff = pygame.image.load('Immagini/Disegnigraf/RobotGrafsalva.png')

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
sfondosta = pygame.image.load('Immagini/Status/Sfondosta.png')
sfondomo = pygame.transform.scale(sfondosta, (gpx, gpy))
sfondosta = pygame.transform.scale(sfondosta, ((gpx // 3 * 4) + (gpx // 4), gpy // 3 * 2))
sfondostapers = pygame.transform.scale(sfondosta, ((gpx // 3 * 6) + (gpx // 4), gpy // 3 * 2))
sfondoStartBattaglia = pygame.image.load('Immagini/Oggetti/SfondoStartBattaglia.png')
sfondoStartBattaglia = pygame.transform.scale(sfondoStartBattaglia, (gpx * 7, gpy * 7))
sfondoStatAumentata = pygame.image.load('Immagini/Levelup/SfondoStatisticaAumentata.png')
sfondoStatAumentata = pygame.transform.scale(sfondoStatAumentata, (gpx * 7, gpy * 7))

# status
appiccicosoo = pygame.image.load('Immagini/Status/Appiccicoso.png')
appiccicoso = pygame.transform.scale(appiccicosoo, (gpx // 3 * 2, gpy // 3 * 2))
avvelenatoo = pygame.image.load('Immagini/Status/Avvelenato.png')
avvelenato = pygame.transform.scale(avvelenatoo, (gpx // 3 * 2, gpy // 3 * 2))
surriscaldatoo = pygame.image.load('Immagini/Status/Surriscaldato.png')
surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx // 3 * 2, gpy // 3 * 2))
attaccopiuo = pygame.image.load('Immagini/Status/Attaccopiu.png')
attaccopiu = pygame.transform.scale(attaccopiuo, (gpx // 3 * 2, gpy // 3 * 2))
difesapiuo = pygame.image.load('Immagini/Status/Difesapiu.png')
difesapiu = pygame.transform.scale(difesapiuo, (gpx // 3 * 2, gpy // 3 * 2))
velocitapiuo = pygame.image.load('Immagini/Status/Velocitapiu.png')
velocitapiu = pygame.transform.scale(velocitapiuo, (gpx // 3 * 2, gpy // 3 * 2))
efficienzapiuo = pygame.image.load('Immagini/Status/Efficienzapiu.png')
efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx // 3 * 2, gpy // 3 * 2))
occhioape = pygame.image.load('Immagini/Status/OcchioAperto.png')
occhioape = pygame.transform.scale(occhioape, (gpx, gpy))
occhiochiu = pygame.image.load('Immagini/Status/OcchioChiuso.png')
occhiochiu = pygame.transform.scale(occhiochiu, (gpx, gpy))

# chiave robo
chiaveroboacc = pygame.image.load('Immagini/Oggetti/ChiaveColcoAcc.png')
chiaveroboacc = pygame.transform.scale(chiaveroboacc, (gpx * 2, gpy * 2))
chiaverobospe = pygame.image.load('Immagini/Oggetti/ChiaveColcoSpe.png')
chiaverobospe = pygame.transform.scale(chiaverobospe, (gpx * 2, gpy * 2))
sfochiaveocchio = pygame.image.load("Immagini/Oggetti/SfondoOcchioChiave.png")
sfochiaveocchio = pygame.transform.scale(sfochiaveocchio, (gpx * 5, gpy * 2))

# oggetti lanciati
esche = pygame.image.load("Immagini/Oggetti/Esca.png")
esche = pygame.transform.scale(esche, (gpx, gpy))
sacchettoDenaroStart = pygame.image.load('Immagini/Oggetti/SacchettoDenaro.png')
sacchettoDenaroStart = pygame.transform.scale(sacchettoDenaroStart, (gpx * 4, gpy * 4))
sacchettoDenaroo = pygame.image.load('Immagini/Oggetti/SacchettoDenaroIco.png')
sacchettoDenaro = pygame.transform.scale(sacchettoDenaroo, (gpx, gpy))

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
saliliv3 = pygame.image.load('Immagini/Levelup/Saliliv3.png')
saliliv3 = pygame.transform.scale(saliliv3, (gpx, gpy))

# canali / volume (0-1)
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
selsta = pygame.mixer.Sound("Audio/Rumoripuntatore/SelSta.wav")
selind = pygame.mixer.Sound("Audio/Rumoripuntatore/SelInd.wav")
spostapun = pygame.mixer.Sound("Audio/Rumoripuntatore/SpostaPun.wav")
selimp = pygame.mixer.Sound("Audio/Rumoripuntatore/SelImp.wav")
selezione = pygame.mixer.Sound("Audio/Rumoripuntatore/Selezione.wav")

# suoni effetti
rumoreattacco = pygame.mixer.Sound("Audio/Rumoripersonaggio/Attacco.wav")
rumorecamminata = pygame.mixer.Sound("Audio/Rumoripersonaggio/Camminata.wav")
rumorelevelup = pygame.mixer.Sound("Audio/Rumoripersonaggio/Levelup.wav")
suonoaperturacofanetti = pygame.mixer.Sound("Audio/Rumoriambiente/Aperturaportacofanetti.wav")
suonoaperturaporte = pygame.mixer.Sound("Audio/Rumoriambiente/Aperturaportacofanetti.wav")

# suoni canzoni
c11 = pygame.mixer.Sound("Audio/Canzoni/Canzone11.wav")
c27 = pygame.mixer.Sound("Audio/Canzoni/Canzone27.wav")

# dati tecniche di Colco [scossa, cura, antidoto, freccia, tempesta, raffred, ricarica, cura+, scossa+, freccia+, velocizza, attP, difP, efficienza, tempesta+, cura++, ricarica+, scossa++, freccia++, tempesa++]
costoTecniche = [5, 10, 10, 5, 10, 10, 1, 20, 10, 10, 15, 20, 20, 30, 20, 30, 1, 20, 20, 40]
dannoTecniche = [40, 30, 0, 30, 20, 0, 150, 120, 160, 130, 15, 10, 10, 15, 100, 250, 300, 320, 260, 200]
