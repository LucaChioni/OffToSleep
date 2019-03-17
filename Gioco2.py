import pygame
import random
import ctypes
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
pygame.display.set_caption("gioco 2")
icona = pygame.image.load("Immagini\Icona.png")
pygame.display.set_icon(icona)

# clock
clock = pygame.time.Clock()
fps = 30
fpsanimazioni = 7
fpsmenu = 20

# colori
nero = (0, 0, 0)
grigioscu = [70, 70, 70]
grigio = [100, 100, 100]
grigiochi = [230, 230, 230]
bianco = (255, 255, 255)
rosso = (255, 0, 0)
verde = (0, 255, 0)
verdescu = (0, 120, 0)
blu = (0, 0, 255)

# suono apertura porte e cofanetti
suonoaperturacopo = pygame.mixer.Sound("Audio\Rumoriambiente\Aperturaportacofanetti.wav")
suonoaperturacopo.set_volume(0.5)

# puntatore
puntatoreorigi = pygame.image.load("Immagini\Puntatori\Puntatore.png")
puntatore = pygame.transform.scale(puntatoreorigi, (gpx, gpy))
puntatoreorigivecchio = pygame.image.load("Immagini\Puntatori\Puntatorevecchio.png")
puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx, gpy))
selsta = pygame.mixer.Sound("Audio\Rumoripuntatore\SelSta.wav")
selind = pygame.mixer.Sound("Audio\Rumoripuntatore\SelInd.wav")
spostapun = pygame.mixer.Sound("Audio\Rumoripuntatore\SpostaPun.wav")
selimp = pygame.mixer.Sound("Audio\Rumoripuntatore\SelImp.wav")
selezione = pygame.mixer.Sound("Audio\Rumoripuntatore\Selezione.wav")
rumoreattacco = pygame.mixer.Sound("Audio\Rumoripersonaggio\Attacco.wav")
rumorecamminata = pygame.mixer.Sound("Audio\Rumoripersonaggio\Camminata.wav")
rumorelevelup = pygame.mixer.Sound("Audio\Rumoripersonaggio\Levelup.wav")

# immagini personaggio
persw = pygame.image.load('Immagini\Personaggi\Personaggio4.png')
persw = pygame.transform.scale(persw, (gpx, gpy))
perswb = pygame.image.load('Immagini\Personaggi\Personaggio4b.png')
perswb = pygame.transform.scale(perswb, (gpx, gpy))
persa = pygame.image.load('Immagini\Personaggi\Personaggio3.png')
persa = pygame.transform.scale(persa, (gpx, gpy))
persab = pygame.image.load('Immagini\Personaggi\Personaggio3b.png')
persab = pygame.transform.scale(persab, (gpx, gpy))
perso = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
perss = pygame.transform.scale(perso, (gpx, gpy))
perssb = pygame.image.load('Immagini\Personaggi\Personaggio1b.png')
perssb = pygame.transform.scale(perssb, (gpx, gpy))
persd = pygame.image.load('Immagini\Personaggi\Personaggio2.png')
persd = pygame.transform.scale(persd, (gpx, gpy))
persdb = pygame.image.load('Immagini\Personaggi\Personaggio2b.png')
persdb = pygame.transform.scale(persdb, (gpx, gpy))
perssm = pygame.image.load('Immagini\Personaggi\Personaggio1mov.png')
perssm = pygame.transform.scale(perssm, (gpx, gpy))
perssmb1 = pygame.image.load('Immagini\Personaggi\Personaggio1movb1.png')
perssmb1 = pygame.transform.scale(perssmb1, (gpx, gpy))
perssmb2 = pygame.image.load('Immagini\Personaggi\Personaggio1movb2.png')
perssmb2 = pygame.transform.scale(perssmb2, (gpx, gpy))
persdm = pygame.image.load('Immagini\Personaggi\Personaggio2mov.png')
persdm = pygame.transform.scale(persdm, (gpx, gpy))
persdmb1 = pygame.image.load('Immagini\Personaggi\Personaggio2movb1.png')
persdmb1 = pygame.transform.scale(persdmb1, (gpx, gpy))
persdmb2 = pygame.image.load('Immagini\Personaggi\Personaggio2movb2.png')
persdmb2 = pygame.transform.scale(persdmb2, (gpx, gpy))
persam = pygame.image.load('Immagini\Personaggi\Personaggio3mov.png')
persam = pygame.transform.scale(persam, (gpx, gpy))
persamb1 = pygame.image.load('Immagini\Personaggi\Personaggio3movb1.png')
persamb1 = pygame.transform.scale(persamb1, (gpx, gpy))
persamb2 = pygame.image.load('Immagini\Personaggi\Personaggio3movb2.png')
persamb2 = pygame.transform.scale(persamb2, (gpx, gpy))
perswm = pygame.image.load('Immagini\Personaggi\Personaggio4mov.png')
perswm = pygame.transform.scale(perswm, (gpx, gpy))
perswmb1 = pygame.image.load('Immagini\Personaggi\Personaggio4movb1.png')
perswmb1 = pygame.transform.scale(perswmb1, (gpx, gpy))
perswmb2 = pygame.image.load('Immagini\Personaggi\Personaggio4movb2.png')
perswmb2 = pygame.transform.scale(perswmb2, (gpx, gpy))
persgra = pygame.image.load('Immagini\Disegnigraf\PersonaggioGraf3.png')
persgraf = pygame.image.load('Immagini\Disegnigraf\PersonaggioGraf.png')

# immagini robot
robow = pygame.image.load('Immagini\Personaggi\Robot4.png')
robow = pygame.transform.scale(robow, (gpx, gpy))
roboa = pygame.image.load('Immagini\Personaggi\Robot3.png')
roboa = pygame.transform.scale(roboa, (gpx, gpy))
roboo = pygame.image.load('Immagini\Personaggi\Robot1.png')
robos = pygame.transform.scale(roboo, (gpx, gpy))
robod = pygame.image.load('Immagini\Personaggi\Robot2.png')
robod = pygame.transform.scale(robod, (gpx, gpy))
robomo = pygame.image.load('Immagini\Personaggi\Robot0.png')
robomo = pygame.transform.scale(robomo, (gpx, gpy))
armrobmo = pygame.image.load('Immagini\Armrobs\Armrob00.png')
armrobmo = pygame.transform.scale(armrobmo, (gpx, gpy))
robogra = pygame.image.load('Immagini\Disegnigraf\RobotGraf.png')
robograf = pygame.image.load('Immagini\Disegnigraf\RobotGraf2.png')
robograff = pygame.image.load('Immagini\Disegnigraf\RobotGraf3.png')
robografff = pygame.image.load('Immagini\Disegnigraf\RobotGraf4.png')

# indicatori vita
indvita = pygame.image.load('Immagini\Barrevita\Indvita.png')
vitanemico = pygame.image.load('Immagini\Barrevita\Vitanemico.png')
vitapersonaggio = pygame.image.load('Immagini\Barrevita\Vitapersonaggio.png')
vitarobo = pygame.image.load('Immagini\Barrevita\Vitarobo.png')
vitaesche = pygame.image.load('Immagini\Barrevita\Vitaesca.png')

# status
sfondostax3 = pygame.image.load('Immagini\Status\Sfondostax3.png')
sfondosta = pygame.image.load('Immagini\Status\Sfondosta.png')
sfondomo = pygame.transform.scale(sfondosta, (gpx, gpy))
sfondosta = pygame.transform.scale(sfondosta, ((gpx // 3 * 4) + (gpx // 4), gpy // 3 * 2))
sfondostapers = pygame.transform.scale(sfondosta, ((gpx // 3 * 6) + (gpx // 4), gpy // 3 * 2))
appiccicosoo = pygame.image.load('Immagini\Status\Appiccicoso.png')
appiccicoso = pygame.transform.scale(appiccicosoo, (gpx // 3 * 2, gpy // 3 * 2))
avvelenatoo = pygame.image.load('Immagini\Status\Avvelenato.png')
avvelenato = pygame.transform.scale(avvelenatoo, (gpx // 3 * 2, gpy // 3 * 2))
surriscaldatoo = pygame.image.load('Immagini\Status\Surriscaldato.png')
surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx // 3 * 2, gpy // 3 * 2))
attaccopiuo = pygame.image.load('Immagini\Status\Attaccopiu.png')
attaccopiu = pygame.transform.scale(attaccopiuo, (gpx // 3 * 2, gpy // 3 * 2))
difesapiuo = pygame.image.load('Immagini\Status\Difesapiu.png')
difesapiu = pygame.transform.scale(difesapiuo, (gpx // 3 * 2, gpy // 3 * 2))
velocitapiuo = pygame.image.load('Immagini\Status\Velocitapiu.png')
velocitapiu = pygame.transform.scale(velocitapiuo, (gpx // 3 * 2, gpy // 3 * 2))
efficienzapiuo = pygame.image.load('Immagini\Status\Efficienzapiu.png')
efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx // 3 * 2, gpy // 3 * 2))
occhioape = pygame.image.load('Immagini\Status\OcchioAperto.png')
occhioape = pygame.transform.scale(occhioape, (gpx, gpy))
occhiochiu = pygame.image.load('Immagini\Status\OcchioChiuso.png')
occhiochiu = pygame.transform.scale(occhiochiu, (gpx, gpy))

# esche
esche = pygame.image.load("Immagini\Oggetti\Esca.png")
esche = pygame.transform.scale(esche, (gpx, gpy))

# cofanetti
cofaniaper = pygame.image.load("Immagini\Oggetti\CofanettoAperto.png")
cofaniaper = pygame.transform.scale(cofaniaper, (gpx, gpy))
cofanichiu = pygame.image.load("Immagini\Oggetti\CofanettoChiuso.png")
cofanichiu = pygame.transform.scale(cofanichiu, (gpx, gpy))
sfocontcof = pygame.image.load("Immagini\Oggetti\SfondoContenutoCofanetto.png")
sfocontcof = pygame.transform.scale(sfocontcof, (gpx * 16, gpy * 3))

# freccetta invisibile
pygame.mouse.set_visible(False)


def messaggio(msg, colore, x, y, gr):
    gr = gr - 10
    y = y - (gpy // 8)
    carattere = "Gentium Book Basic"
    if gsx >= 3840 and gsy >= 2160:
        font = pygame.font.SysFont(carattere, gr * 2)
    if (gsx < 3840 and gsx > 1920) and (gsy < 2160 and gsy > 1080):
        font = pygame.font.SysFont(carattere, gr * 4 // 3)
    if gsx == 1920 and gsy == 1080:
        font = pygame.font.SysFont(carattere, gr)
    if (gsx < 1920 and gsx > 1600) and (gsy < 1080 and gsy > 900):
        font = pygame.font.SysFont(carattere, gr * 7 // 8)
    if gsx == 1600 and gsy == 900:
        font = pygame.font.SysFont(carattere, gr * 5 // 6)
    if (gsx < 1600 and gsx > 1280) and (gsy < 900 and gsy > 720):
        font = pygame.font.SysFont(carattere, gr * 3 // 4)
    if gsx == 1280 and gsy == 720:
        font = pygame.font.SysFont(carattere, gr * 2 // 3)
    if (gsx < 1280 and gsx >= 1024) and (gsy < 720 and gsy >= 576):
        font = pygame.font.SysFont(carattere, gr // 2)
    if gsx < 1024 and gsy < 576:
        font = pygame.font.SysFont(carattere, gr // 5 * 2)
    testo = font.render(msg, True, colore)
    schermo.blit(testo, (x, y))


def salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti):
    scrivi = open("Salvataggi\Salvataggio%i.txt" % n, "w")
    # conversione della posizione in caselle
    dati[2] = dati[2] // gpx
    dati[3] = dati[3] // gpy
    i = porteini
    while i <= portefin:
        j = 0
        while j < len(porte):
            if dati[i] == porte[j] and dati[i + 1] == porte[j + 1] and dati[i + 2] == porte[j + 2]:
                dati[i + 3] = porte[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // gpx
        dati[i + 2] = dati[i + 2] // gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        j = 0
        while j < len(cofanetti):
            if dati[i] == cofanetti[j] and dati[i + 1] == cofanetti[j + 1] and dati[i + 2] == cofanetti[j + 2]:
                dati[i + 3] = cofanetti[j + 3]
            j = j + 4
        dati[i + 1] = dati[i + 1] // gpx
        dati[i + 2] = dati[i + 2] // gpy
        i = i + 4

    for i in range(0, len(dati)):
        scrivi.write("%i_" % dati[i])
    scrivi.close()

    # conversione della posizione in pixel
    dati[2] = dati[2] * gpx
    dati[3] = dati[3] * gpy
    i = porteini
    while i <= portefin:
        dati[i + 1] = dati[i + 1] * gpx
        dati[i + 2] = dati[i + 2] * gpy
        i = i + 4
    i = cofaniini
    while i <= cofanifin:
        dati[i + 1] = dati[i + 1] * gpx
        dati[i + 2] = dati[i + 2] * gpy
        i = i + 4


def scegli_sal(cosa, lunghezzadati):
    # immagini salvataggi
    s1 = pygame.image.load('Immagini\Salvataggi\S1.png')
    s1 = pygame.transform.scale(s1, (gpx * 3, gpy * 3))
    s2 = pygame.image.load('Immagini\Salvataggi\S2.png')
    s2 = pygame.transform.scale(s2, (gpx * 3, gpy * 3))
    s3 = pygame.image.load('Immagini\Salvataggi\S3.png')
    s3 = pygame.transform.scale(s3, (gpx * 3, gpy * 3))

    # posizione-dimensione puntatore
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx, gpy))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx, gpy))
    xp = gsx // 32 * 6
    yp = gsy // 18 * 10

    risposta = False
    conferma = False
    primaconf = False

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 5, gsy // 18 * 7, gsx // 32 * 22, gsy // 18 * 9.5))
        if cosa == 1:
            messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
        if cosa == 2:
            messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
        if cosa == 3:
            messaggio("Salva partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
        if conferma:
            if primaconf:
                vxp = xp
                vyp = yp
                xp = gsx // 32 * 22
                yp = gsy // 18 * 6
                primaconf = False
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 18, gsy // 18 * 3.5, gsx // 32 * 9, gsy // 18 * 5))
            messaggio("Confermi?", grigiochi, gsx // 32 * 20, gsy // 18 * 4.5, 70)
            messaggio("Si", grigiochi, gsx // 32 * 20.2, gsy // 18 * 6, 70)
            messaggio("No", grigiochi, gsx // 32 * 23.2, gsy // 18 * 6, 70)
            schermo.blit(puntatorevecchio, (vxp, vyp))
        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(s1, (gsx // 32 * 8, gsy // 18 * 8))
        schermo.blit(s2, (gsx // 32 * 15, gsy // 18 * 8))
        schermo.blit(s3, (gsx // 32 * 22, gsy // 18 * 8))

        # lettura salvataggi per riconoscerli
        contasalva = 1
        while contasalva <= 3:
            leggi = open("Salvataggi\Salvataggio%i.txt" % contasalva, "r")
            leggifile = leggi.read()
            dati = leggifile.split("_")
            dati.pop(len(dati) - 1)
            if len(dati) == 0:
                if contasalva == 1:
                    messaggio("Slot vuoto", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                elif contasalva == 2:
                    messaggio("Slot vuoto", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                elif contasalva == 3:
                    messaggio("Slot vuoto", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
            else:
                errore = False
                if len(dati) != lunghezzadati:
                    errore = True
                for i in range(0, len(dati)):
                    try:
                        dati[i] = int(dati[i])
                    except ValueError:
                        errore = True
                if contasalva == 1:
                    if not errore:
                        persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                        persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                        spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                        spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                        scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                        scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                        armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                        armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                        schermo.blit(persalva, (gpx * 8, gpy * 12))
                        schermo.blit(armsalva, (gpx * 8, gpy * 12))
                        schermo.blit(scusalva, (gpx * 8, gpy * 12))
                        schermo.blit(spasalva, (gpx * 8, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                elif contasalva == 2:
                    if not errore:
                        persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                        persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                        spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                        spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                        scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                        scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                        armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                        armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                        schermo.blit(persalva, (gpx * 15, gpy * 12))
                        schermo.blit(armsalva, (gpx * 15, gpy * 12))
                        schermo.blit(scusalva, (gpx * 15, gpy * 12))
                        schermo.blit(spasalva, (gpx * 15, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                elif contasalva == 3:
                    if not errore:
                        persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                        persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                        spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                        spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                        scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                        scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                        armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                        armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                        messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                        schermo.blit(persalva, (gpx * 22, gpy * 12))
                        schermo.blit(armsalva, (gpx * 22, gpy * 12))
                        schermo.blit(scusalva, (gpx * 22, gpy * 12))
                        schermo.blit(spasalva, (gpx * 22, gpy * 12))
                    else:
                        messaggio("Dati corrotti", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
            contasalva = contasalva + 1
        leggi.close()

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if conferma:
                        selind.play()
                        xp = vxp
                        yp = vyp
                        conferma = False
                    else:
                        selind.play()
                        n = -1
                        return n
                if event.key == pygame.K_d:
                    if conferma:
                        if xp == gsx // 32 * 19:
                            spostapun.play()
                            xp = gsx // 32 * 22
                        elif xp == gsx // 32 * 22:
                            selimp.play()
                    else:
                        if xp == gsx // 32 * 6:
                            spostapun.play()
                            xp = gsx // 32 * 13
                        else:
                            if xp == gsx // 32 * 13:
                                spostapun.play()
                                xp = gsx // 32 * 20
                            else:
                                selimp.play()
                if event.key == pygame.K_a:
                    if conferma:
                        if xp == gsx // 32 * 22:
                            spostapun.play()
                            xp = gsx // 32 * 19
                        elif xp == gsx // 32 * 19:
                            selimp.play()
                    else:
                        if xp == gsx // 32 * 20:
                            spostapun.play()
                            xp = gsx // 32 * 13
                        else:
                            if xp == gsx // 32 * 13:
                                spostapun.play()
                                xp = gsx // 32 * 6
                            else:
                                selimp.play()
                if event.key == pygame.K_SPACE:
                    if conferma and xp == gsx // 32 * 19 and yp == gsy // 18 * 6:
                        selezione.play()
                        return n
                        risposta = True
                    if not conferma and yp == gsy // 18 * 10:
                        selezione.play()
                        if xp == gsx // 32 * 6:
                            conferma = True
                            primaconf = True
                            n = 1
                        if xp == gsx // 32 * 13:
                            conferma = True
                            primaconf = True
                            n = 2
                        if xp == gsx // 32 * 20:
                            conferma = True
                            primaconf = True
                            n = 3
                    if conferma and xp == gsx // 32 * 22 and yp == gsy // 18 * 6:
                        selind.play()
                        xp = vxp
                        yp = vyp
                        conferma = False

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 5, gsy // 18 * 7, gsx // 32 * 22, gsy // 18 * 9.5))
            if cosa == 1:
                messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
            if cosa == 2:
                messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
            if cosa == 3:
                messaggio("Salva partita", grigiochi, gsx // 32 * 4, gsy // 18 * 4, 90)
            if conferma:
                if primaconf:
                    vxp = xp
                    vyp = yp
                    xp = gsx // 32 * 22
                    yp = gsy // 18 * 6
                    primaconf = False
                pygame.draw.rect(schermo, grigio, (gsx // 32 * 18, gsy // 18 * 3.5, gsx // 32 * 9, gsy // 18 * 5))
                messaggio("Confermi?", grigiochi, gsx // 32 * 20, gsy // 18 * 4.5, 70)
                messaggio("Si", grigiochi, gsx // 32 * 20.2, gsy // 18 * 6, 70)
                messaggio("No", grigiochi, gsx // 32 * 23.2, gsy // 18 * 6, 70)
                schermo.blit(puntatorevecchio, (vxp, vyp))
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(s1, (gsx // 32 * 8, gsy // 18 * 8))
            schermo.blit(s2, (gsx // 32 * 15, gsy // 18 * 8))
            schermo.blit(s3, (gsx // 32 * 22, gsy // 18 * 8))

            # lettura salvataggi per riconoscerli
            contasalva = 1
            while contasalva <= 3:
                leggi = open("Salvataggi\Salvataggio%i.txt" % contasalva, "r")
                leggifile = leggi.read()
                dati = leggifile.split("_")
                dati.pop(len(dati) - 1)
                if len(dati) == 0:
                    if contasalva == 1:
                        messaggio("Slot vuoto", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        messaggio("Slot vuoto", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        messaggio("Slot vuoto", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                else:
                    errore = False
                    if len(dati) != lunghezzadati:
                        errore = True
                    for i in range(0, len(dati)):
                        try:
                            dati[i] = int(dati[i])
                        except ValueError:
                            errore = True
                    if contasalva == 1:
                        if not errore:
                            persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                            persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                            spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                            spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                            scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                            scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                            armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                            armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                            schermo.blit(persalva, (gpx * 8, gpy * 12))
                            schermo.blit(armsalva, (gpx * 8, gpy * 12))
                            schermo.blit(scusalva, (gpx * 8, gpy * 12))
                            schermo.blit(spasalva, (gpx * 8, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 7.5, gsy // 18 * 11, 60)
                    elif contasalva == 2:
                        if not errore:
                            persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                            persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                            spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                            spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                            scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                            scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                            armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                            armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                            schermo.blit(persalva, (gpx * 15, gpy * 12))
                            schermo.blit(armsalva, (gpx * 15, gpy * 12))
                            schermo.blit(scusalva, (gpx * 15, gpy * 12))
                            schermo.blit(spasalva, (gpx * 15, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 14.5, gsy // 18 * 11, 60)
                    elif contasalva == 3:
                        if not errore:
                            persalva = pygame.image.load('Immagini\Personaggi\Personaggio1.png')
                            persalva = pygame.transform.scale(persalva, (gpx * 3, gpy * 3))
                            spasalva = pygame.image.load('Immagini\Armi\Arma%is.png' % dati[6])
                            spasalva = pygame.transform.scale(spasalva, (gpx * 3, gpy * 3))
                            scusalva = pygame.image.load('Immagini\Scudi\Scudo%is.png' % dati[7])
                            scusalva = pygame.transform.scale(scusalva, (gpx * 3, gpy * 3))
                            armsalva = pygame.image.load('Immagini\Armature\Armatura%is.png' % dati[8])
                            armsalva = pygame.transform.scale(armsalva, (gpx * 3, gpy * 3))
                            messaggio("Livello: " + str(dati[4]), grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                            schermo.blit(persalva, (gpx * 22, gpy * 12))
                            schermo.blit(armsalva, (gpx * 22, gpy * 12))
                            schermo.blit(scusalva, (gpx * 22, gpy * 12))
                            schermo.blit(spasalva, (gpx * 22, gpy * 12))
                        else:
                            messaggio("Dati corrotti", grigiochi, gsx // 32 * 21.5, gsy // 18 * 11, 60)
                contasalva = contasalva + 1
            leggi.close()

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()


def menu():
    # canzone
    c11 = pygame.mixer.Sound("Audio\Canzoni\Canzone11.wav")
    c11.play(-1)

    # video
    fermavideo = False
    clock = pygame.time.Clock()
    movie = pygame.movie.Movie(r'Video\videoinizio.mpg')
    movie_screen = pygame.Surface(schermo.get_size())
    movie.set_display(movie_screen, pygame.draw.rect(schermo, nero, (0, 0, gsx, gsy), 1))
    movie.play()
    while movie.get_busy() and not fermavideo:
        schermo.blit(movie_screen, (0, 0))
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                selezione.play()
                fermavideo = True

    # attesa dopo video
    if not fermavideo:
        schermo.fill(grigioscu)
        messaggio("Premi un tasto per continuare", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 100)
        pygame.display.update()
        finevideo = True
        while finevideo:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    selezione.play()
                    finevideo = False

    puntatore = pygame.transform.scale(puntatoreorigi, (gpx, gpy))
    xp = gsx // 32 * 2
    yp = gsy // 18 * 3

    # numero per la posizione di robo all'avvio
    c = random.randint(1, 4)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        persomenuinizio = pygame.transform.scale(persgraf, (gpx * 18, gpy * 18))
        if (c == 1):
            robomenuinizio = pygame.transform.scale(robogra, (gpx * 18, gpy * 18))
        if (c == 2):
            robomenuinizio = pygame.transform.scale(robograf, (gpx * 18, gpy * 18))
        if (c == 3):
            robomenuinizio = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
        if (c == 4):
            robomenuinizio = pygame.transform.scale(robografff, (gpx * 18, gpy * 18))
        schermo.blit(persomenuinizio, (gpx * 15, 0))
        schermo.blit(robomenuinizio, (gpx * 3, 0))
        messaggio("Nuova partita", grigiochi, gsx // 32 * 4, gsy // 18 * 3, 90)
        messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 5.5, 90)
        messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 8, 90)
        messaggio("Esci", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 90)
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while True:
        # posizione porte e cofanetti nel vettore dati
        porteini = 128
        portefin = 155
        cofaniini = portefin + 1
        cofanifin = 179
        lunghezzadati = cofanifin + 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if yp != gsy // 18 * 13:
                        if yp == gsy // 18 * 3:
                            spostapun.play()
                            yp = gsy // 18 * 5.5
                        elif yp == gsy // 18 * 5.5:
                            spostapun.play()
                            yp = gsy // 18 * 8
                        elif yp == gsy // 18 * 8:
                            spostapun.play()
                            yp = gsy // 18 * 13
                    else:
                        selimp.play()
                if event.key == pygame.K_w:
                    if yp != gsy // 18 * 3:
                        if yp == gsy // 18 * 5.5:
                            spostapun.play()
                            yp = gsy // 18 * 3
                        elif yp == gsy // 18 * 8:
                            spostapun.play()
                            yp = gsy // 18 * 5.5
                        elif yp == gsy // 18 * 13:
                            spostapun.play()
                            yp = gsy // 18 * 8
                    else:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    selezione.play()

                    # nuova partita
                    if yp == gsy // 18 * 3:
                        x = gsx // 32 * 6
                        y = gsy // 18 * 2
                        # progresso - stanza - x - y - liv - pv - arma - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(10) - armi(30) - batterie(10) - condizioni(20) - gambit(20) -
                        # veleno - surriscalda - attp - difp - velp(x2) - efficienza - esperienza - porte(128-?) - cofanetti(?-?) // dimensione: 0-127 + porte e cofanetti
                        dati = [0, 1, x, y, 1, 105, 0, 0, 0, 0, 300,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                                2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                                False, 0, 0, 0, 0, 0, 0,# da qui iniziano le porte
                                2, 3, 7, False, 2, 7, 12, False, 2, 12, 11, False, 2, 15, 9, False, 2, 15, 3, False, 2, 23, 5, False, 2, 23, 12, False,# da qui iniziano i cofanetti
                                1, 3, 7, False, 1, 7, 12, False, 1, 12, 11, False, 2, 3, 5, False, 2, 5, 10, False, 2, 10, 9, False]
                        c11.stop()
                        i = porteini
                        while i <= portefin:
                            dati[i + 1] = dati[i + 1] * gpx
                            dati[i + 2] = dati[i + 2] * gpy
                            i = i + 4
                        i = cofaniini
                        while i <= cofanifin:
                            dati[i + 1] = dati[i + 1] * gpx
                            dati[i + 2] = dati[i + 2] * gpy
                            i = i + 4
                        return dati, porteini, portefin, cofaniini, cofanifin

                    # carica partita
                    if yp == gsy // 18 * 5.5:
                        n = scegli_sal(1, lunghezzadati)

                        # lettura salvataggio
                        if n != -1:
                            leggi = open("Salvataggi\Salvataggio%i.txt" % n, "r")
                            leggifile = leggi.read()
                            dati = leggifile.split("_")
                            dati.pop(len(dati) - 1)
                            if len(dati) == 0:
                                print "Slot vuoto"
                                indietro = False
                                schermo.fill(grigioscu)
                                robograsalva = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
                                schermo.blit(robograsalva, (gpx * 3, -gpy * 5))
                                messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
                                messaggio("Slot di salvataggio vuoto...", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 100)
                                pygame.display.update()
                                while not indietro:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_q:
                                                selind.play()
                                                indietro = True
                            else:
                                errore = False
                                if len(dati) == lunghezzadati:
                                    for i in range(0, len(dati)):
                                        try:
                                            dati[i] = int(dati[i])
                                        except ValueError:
                                            errore = True
                                    if not errore:
                                        # conversione della posizione in pixel
                                        dati[2] = dati[2] * gpx
                                        dati[3] = dati[3] * gpy
                                        i = porteini
                                        while i <= portefin:
                                            dati[i + 1] = dati[i + 1] * gpx
                                            dati[i + 2] = dati[i + 2] * gpy
                                            i = i + 4
                                        i = cofaniini
                                        while i <= cofanifin:
                                            dati[i + 1] = dati[i + 1] * gpx
                                            dati[i + 2] = dati[i + 2] * gpy
                                            i = i + 4

                                        print "Salvataggio: " + str(n)
                                        leggi.close()
                                        c11.stop()
                                        return dati, porteini, portefin, cofaniini, cofanifin
                                if len(dati) != lunghezzadati or errore:
                                    print "Dati corrotti: " + str(len(dati))
                                    indietro = False
                                    schermo.fill(grigioscu)
                                    robograsalva = pygame.image.load('Immagini\Disegnigraf\RobotGrafsalva.png')
                                    robograsalva = pygame.transform.scale(robograsalva, (gpx * 18, gpy * 18))
                                    schermo.blit(robograsalva, (gpx * 15, -gpy * 3))
                                    messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
                                    messaggio("I dati sono corrotti...", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 100)
                                    pygame.display.update()
                                    while not indietro:
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_q:
                                                    selind.play()
                                                    indietro = True
                            leggi.close()

                    # cancella partita
                    if yp == gsy // 18 * 8:
                        n = scegli_sal(2, lunghezzadati)
                        if n != -1:
                            leggi = open("Salvataggi\Salvataggio%i.txt" % n, "w")
                            leggi.close()

                    # esci dal gioco
                    if yp == gsy // 18 * 13:
                        pygame.quit()
                        quit()

            schermo.fill(grigioscu)
            persomenuinizio = pygame.transform.scale(persgraf, (gpx * 18, gpy * 18))
            if (c == 1):
                robomenuinizio = pygame.transform.scale(robogra, (gpx * 18, gpy * 18))
            if (c == 2):
                robomenuinizio = pygame.transform.scale(robograf, (gpx * 18, gpy * 18))
            if (c == 3):
                robomenuinizio = pygame.transform.scale(robograff, (gpx * 18, gpy * 18))
            if (c == 4):
                robomenuinizio = pygame.transform.scale(robografff, (gpx * 18, gpy * 18))
            schermo.blit(persomenuinizio, (gpx * 15, 0))
            schermo.blit(robomenuinizio, (gpx * 3, 0))
            messaggio("Nuova partita", grigiochi, gsx // 32 * 4, gsy // 18 * 3, 90)
            messaggio("Carica partita", grigiochi, gsx // 32 * 4, gsy // 18 * 5.5, 90)
            messaggio("Cancella salvataggio", grigiochi, gsx // 32 * 4, gsy // 18 * 8, 90)
            messaggio("Esci", grigiochi, gsx // 32 * 4, gsy // 18 * 13, 90)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()


def equip(dati):
    perssta = pygame.transform.scale(perso, (gpx * 8, gpy * 8))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    carim = True
    risposta = False

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 21, gsy // 18 * 12))
        # linea(dove,colore,inizio,fine,spessore)
        '''pygame.draw.line(schermo, grigioscu, (gsx // 32 * 8, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 8, (gsy // 18 * 15) + (gpy // 2)), 10)
        pygame.draw.line(schermo, grigioscu, (gsx // 32 * 15, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 15, (gsy // 18 * 15) + (gpy // 2)), 10)'''

        if carim:
            armas = pygame.image.load("Immagini\Armi\Arma%is.png" % dati[6])
            arma = pygame.transform.scale(armas, (gpx * 8, gpy * 8))
            scudos = pygame.image.load("Immagini\Scudi\Scudo%is.png" % dati[7])
            scudo = pygame.transform.scale(scudos, (gpx * 8, gpy * 8))
            armaturas = pygame.image.load("Immagini\Armature\Armatura%is.png" % dati[8])
            armatura = pygame.transform.scale(armaturas, (gpx * 8, gpy * 8))
            carim = False
        messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Armi", grigiochi, gsx // 32 * 2.5, gsy // 18 * 4.5, 60)
        if dati[41] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[42] > 0:
            messaggio("Spada di legno", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[43] > 0:
            messaggio("Spada di ferro", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[44] > 0:
            messaggio("Spadone d'acciaio", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[45] > 0:
            messaggio("Spada del toro", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[46] > 0:
            messaggio("Spada di diamante", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[47] > 0:
            messaggio("Excalibur", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[48] > 0:
            messaggio("Lykother", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[49] > 0:
            messaggio("Sinego", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[50] > 0:
            messaggio("Mendaxritas", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        messaggio("Armature", grigiochi, gsx // 32 * 9.5, gsy // 18 * 4.5, 60)
        if dati[51] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[52] > 0:
            messaggio("Armatura di pelle", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[53] > 0:
            messaggio("Armatura di ferro", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[54] > 0:
            messaggio("Armatura d'acciaio", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[55] > 0:
            messaggio("Armatura del toro", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[56] > 0:
            messaggio("Armatura di diamante", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[57] > 0:
            messaggio("Armatura leggendaria", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[58] > 0:
            messaggio("Lykodes", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[59] > 0:
            messaggio("Armatura antica", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[60] > 0:
            messaggio("Loriquam", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
        messaggio("Scudi", grigiochi, gsx // 32 * 16.5, gsy // 18 * 4.5, 60)
        if dati[61] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
        if dati[62] > 0:
            messaggio("Scudo di pelle", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
        if dati[63] > 0:
            messaggio("Scudo di ferro", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
        if dati[64] > 0:
            messaggio("Scudo d'acciaio", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
        if dati[65] > 0:
            messaggio("Scudo del toro", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
        if dati[66] > 0:
            messaggio("Scudo di diamante", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
        if dati[67] > 0:
            messaggio("Scudo leggendario", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
        if dati[68] > 0:
            messaggio("Lykethmos", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
        if dati[69] > 0:
            messaggio("Scudo antico", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
        if dati[70] > 0:
            messaggio("Clipequam", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(perssta, (gsx // 32 * 23, gsy // 18 * 4))
        schermo.blit(armatura, (gsx // 32 * 23, gsy // 18 * 4))
        schermo.blit(arma, (gsx // 32 * 23, gsy // 18 * 4))
        schermo.blit(scudo, (gsx // 32 * 23, gsy // 18 * 4))
        att = 10 + (dati[4] * 2) + (dati[6] * 10)
        dif = 10 + (dati[4] * 2) + (dati[8] * 10) + 5 + (dati[7] * 5)
        par = 3 + (dati[7] * 3)
        messaggio("Attacco: %i" % att, grigiochi, gsx // 32 * 23, gsy // 18 * 13, 45)
        messaggio("Difesa: %i" % dif, grigiochi, gsx // 32 * 23, gsy // 18 * 14, 45)
        messaggio("Probabilita' parata: %i" % par + "%", grigiochi, gsx // 32 * 23, gsy // 18 * 15, 45)
        # confronto statistiche
        # armi
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
            if dati[41] != 0:
                diff = 0 - (dati[6] * 10)
                if dati[6] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
            if dati[42] != 0:
                diff = 10 - (dati[6] * 10)
                if dati[6] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
            if dati[43] != 0:
                diff = 20 - (dati[6] * 10)
                if dati[6] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
            if dati[44] != 0:
                diff = 30 - (dati[6] * 10)
                if dati[6] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
            if dati[45] != 0:
                diff = 40 - (dati[6] * 10)
                if dati[6] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
            if dati[46] != 0:
                diff = 50 - (dati[6] * 10)
                if dati[6] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
            if dati[47] != 0:
                diff = 60 - (dati[6] * 10)
                if dati[6] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
            if dati[48] != 0:
                diff = 70 - (dati[6] * 10)
                if dati[6] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
            if dati[49] != 0:
                diff = 80 - (dati[6] * 10)
                if dati[6] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
            if dati[50] != 0:
                diff = 90 - (dati[6] * 10)
                if dati[6] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[6] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
        # armature
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
            if dati[51] != 0:
                diff = 0 - (dati[8] * 10)
                if dati[8] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
            if dati[52] != 0:
                diff = 10 - (dati[8] * 10)
                if dati[8] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
            if dati[53] != 0:
                diff = 20 - (dati[8] * 10)
                if dati[8] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
            if dati[54] != 0:
                diff = 30 - (dati[8] * 10)
                if dati[8] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
            if dati[55] != 0:
                diff = 40 - (dati[8] * 10)
                if dati[8] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
            if dati[56] != 0:
                diff = 50 - (dati[8] * 10)
                if dati[8] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
            if dati[57] != 0:
                diff = 60 - (dati[8] * 10)
                if dati[8] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
            if dati[58] != 0:
                diff = 70 - (dati[8] * 10)
                if dati[8] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
            if dati[59] != 0:
                diff = 80 - (dati[8] * 10)
                if dati[8] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
            if dati[60] != 0:
                diff = 90 - (dati[8] * 10)
                if dati[8] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[8] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        # scudi
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 6:
            if dati[61] != 0:
                diff = 0 - (dati[7] * 5)
                if dati[7] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 0 - (dati[7] * 3)
                if dati[7] > 0:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                else:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 7:
            if dati[62] != 0:
                diff = 5 - (dati[7] * 5)
                if dati[7] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 3 - (dati[7] * 3)
                if dati[7] > 1:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 1:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 1:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 8:
            if dati[63] != 0:
                diff = 10 - (dati[7] * 5)
                if dati[7] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 6 - (dati[7] * 3)
                if dati[7] > 2:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 2:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 2:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 9:
            if dati[64] != 0:
                diff = 15 - (dati[7] * 5)
                if dati[7] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 9 - (dati[7] * 3)
                if dati[7] > 3:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 3:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 3:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 10:
            if dati[65] != 0:
                diff = 20 - (dati[7] * 5)
                if dati[7] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 12 - (dati[7] * 3)
                if dati[7] > 4:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 4:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 4:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 11:
            if dati[66] != 0:
                diff = 25 - (dati[7] * 5)
                if dati[7] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 15 - (dati[7] * 3)
                if dati[7] > 5:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 5:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 5:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 12:
            if dati[67] != 0:
                diff = 30 - (dati[7] * 5)
                if dati[7] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 18 - (dati[7] * 3)
                if dati[7] > 6:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 6:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 6:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 13:
            if dati[68] != 0:
                diff = 35 - (dati[7] * 5)
                if dati[7] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 21 - (dati[7] * 3)
                if dati[7] > 7:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 7:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 7:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 14:
            if dati[69] != 0:
                diff = 40 - (dati[7] * 5)
                if dati[7] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 24 - (dati[7] * 3)
                if dati[7] > 8:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 8:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 8:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
        if xp == gsx // 32 * 15 and yp == gsy // 18 * 15:
            if dati[70] != 0:
                diff = 45 - (dati[7] * 5)
                if dati[7] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[7] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                diff = 27 - (dati[7] * 3)
                if dati[7] > 9:
                    messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] < 9:
                    messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                elif dati[7] == 9:
                    messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)

        # puntatore vecchio
        if dati[6] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
        if dati[6] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
        if dati[6] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
        if dati[6] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
        if dati[6] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
        if dati[6] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
        if dati[6] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
        if dati[6] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
        if dati[6] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
        if dati[6] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

        if dati[8] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 6))
        if dati[8] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 7))
        if dati[8] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 8))
        if dati[8] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 9))
        if dati[8] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 10))
        if dati[8] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 11))
        if dati[8] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 12))
        if dati[8] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 13))
        if dati[8] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 14))
        if dati[8] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 15))

        if dati[7] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 6))
        if dati[7] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 7))
        if dati[7] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 8))
        if dati[7] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 9))
        if dati[7] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 10))
        if dati[7] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 11))
        if dati[7] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 12))
        if dati[7] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 13))
        if dati[7] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 14))
        if dati[7] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 15))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True
                if event.key == pygame.K_s:
                    if (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    elif yp == gsy // 18 * 15:
                        spostapun.play()
                        yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if (yp != gsy // 18 * 6):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    elif yp == gsy // 18 * 6:
                        spostapun.play()
                        yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if (xp != gsx // 32 * 15):
                        spostapun.play()
                        xp = xp + gsx // 32 * 7
                    elif xp == gsx // 32 * 15:
                        spostapun.play()
                        xp = gsx // 32 * 1
                if event.key == pygame.K_a:
                    if (xp != gsx // 32 * 1):
                        spostapun.play()
                        xp = xp - gsx // 32 * 7
                    elif xp == gsx // 32 * 1:
                        spostapun.play()
                        xp = gsx // 32 * 15
                if event.key == pygame.K_SPACE:
                    carim = True
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armi
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                        if dati[41] != 0:
                            selezione.play()
                            dati[6] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                        if dati[42] != 0:
                            selezione.play()
                            dati[6] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                        if dati[43] != 0:
                            selezione.play()
                            dati[6] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                        if dati[44] != 0:
                            selezione.play()
                            dati[6] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                        if dati[45] != 0:
                            selezione.play()
                            dati[6] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                        if dati[46] != 0:
                            selezione.play()
                            dati[6] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                        if dati[47] != 0:
                            selezione.play()
                            dati[6] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                        if dati[48] != 0:
                            selezione.play()
                            dati[6] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                        if dati[49] != 0:
                            selezione.play()
                            dati[6] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                        if dati[50] != 0:
                            selezione.play()
                            dati[6] = 9
                        else:
                            selimp.play()
                    # armature
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                        if dati[51] != 0:
                            selezione.play()
                            dati[8] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                        if dati[52] != 0:
                            selezione.play()
                            dati[8] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                        if dati[53] != 0:
                            selezione.play()
                            dati[8] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                        if dati[54] != 0:
                            selezione.play()
                            dati[8] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                        if dati[55] != 0:
                            selezione.play()
                            dati[8] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                        if dati[56] != 0:
                            selezione.play()
                            dati[8] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                        if dati[57] != 0:
                            selezione.play()
                            dati[8] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                        if dati[58] != 0:
                            selezione.play()
                            dati[8] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                        if dati[59] != 0:
                            selezione.play()
                            dati[8] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                        if dati[60] != 0:
                            selezione.play()
                            dati[8] = 9
                        else:
                            selimp.play()
                    # scudi
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 6:
                        if dati[61] != 0:
                            selezione.play()
                            dati[7] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 7:
                        if dati[62] != 0:
                            selezione.play()
                            dati[7] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 8:
                        if dati[63] != 0:
                            selezione.play()
                            dati[7] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 9:
                        if dati[64] != 0:
                            selezione.play()
                            dati[7] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 10:
                        if dati[65] != 0:
                            selezione.play()
                            dati[7] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 11:
                        if dati[66] != 0:
                            selezione.play()
                            dati[7] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 12:
                        if dati[67] != 0:
                            selezione.play()
                            dati[7] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 13:
                        if dati[68] != 0:
                            selezione.play()
                            dati[7] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 14:
                        if dati[69] != 0:
                            selezione.play()
                            dati[7] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 15 and yp == gsy // 18 * 15:
                        if dati[70] != 0:
                            selezione.play()
                            dati[7] = 9
                        else:
                            selimp.play()

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 21, gsy // 18 * 12))
            # linea(dove,colore,inizio,fine,spessore)
            '''pygame.draw.line(schermo, grigioscu, (gsx // 32 * 8, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 8, (gsy // 18 * 15) + (gpy // 2)), 10)
            pygame.draw.line(schermo, grigioscu, (gsx // 32 * 15, (gsy // 18 * 4) + (gpy // 2)), (gsx // 32 * 15, (gsy // 18 * 15) + (gpy // 2)), 10)'''

            if carim:
                armas = pygame.image.load("Immagini\Armi\Arma%is.png" % dati[6])
                arma = pygame.transform.scale(armas, (gpx * 8, gpy * 8))
                scudos = pygame.image.load("Immagini\Scudi\Scudo%is.png" % dati[7])
                scudo = pygame.transform.scale(scudos, (gpx * 8, gpy * 8))
                armaturas = pygame.image.load("Immagini\Armature\Armatura%is.png" % dati[8])
                armatura = pygame.transform.scale(armaturas, (gpx * 8, gpy * 8))
                carim = False
            messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Armi", grigiochi, gsx // 32 * 2.5, gsy // 18 * 4.5, 60)
            if dati[41] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[42] > 0:
                messaggio("Spada di legno", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[43] > 0:
                messaggio("Spada di ferro", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[44] > 0:
                messaggio("Spadone d'acciaio", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[45] > 0:
                messaggio("Spada del toro", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[46] > 0:
                messaggio("Spada di diamante", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[47] > 0:
                messaggio("Excalibur", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[48] > 0:
                messaggio("Lykother", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[49] > 0:
                messaggio("Sinego", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[50] > 0:
                messaggio("Mendaxritas", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            messaggio("Armature", grigiochi, gsx // 32 * 9.5, gsy // 18 * 4.5, 60)
            if dati[51] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[52] > 0:
                messaggio("Armatura di pelle", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[53] > 0:
                messaggio("Armatura di ferro", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[54] > 0:
                messaggio("Armatura d'acciaio", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[55] > 0:
                messaggio("Armatura del toro", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[56] > 0:
                messaggio("Armatura di diamante", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[57] > 0:
                messaggio("Armatura leggendaria", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[58] > 0:
                messaggio("Lykodes", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[59] > 0:
                messaggio("Armatura antica", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[60] > 0:
                messaggio("Loriquam", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            messaggio("Scudi", grigiochi, gsx // 32 * 16.5, gsy // 18 * 4.5, 60)
            if dati[61] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 6, 40)
            if dati[62] > 0:
                messaggio("Scudo di pelle", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 7, 40)
            if dati[63] > 0:
                messaggio("Scudo di ferro", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 8, 40)
            if dati[64] > 0:
                messaggio("Scudo d'acciaio", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 9, 40)
            if dati[65] > 0:
                messaggio("Scudo del toro", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 10, 40)
            if dati[66] > 0:
                messaggio("Scudo di diamante", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 11, 40)
            if dati[67] > 0:
                messaggio("Scudo leggendario", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 12, 40)
            if dati[68] > 0:
                messaggio("Lykethmos", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 13, 40)
            if dati[69] > 0:
                messaggio("Scudo antico", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 14, 40)
            if dati[70] > 0:
                messaggio("Clipequam", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 16, gsy // 18 * 15, 40)
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(perssta, (gsx // 32 * 23, gsy // 18 * 4))
            schermo.blit(armatura, (gsx // 32 * 23, gsy // 18 * 4))
            schermo.blit(arma, (gsx // 32 * 23, gsy // 18 * 4))
            schermo.blit(scudo, (gsx // 32 * 23, gsy // 18 * 4))
            att = 10 + (dati[4] * 2) + (dati[6] * 10)
            dif = 10 + (dati[4] * 2) + (dati[8] * 10) + 5 + (dati[7] * 5)
            par = 3 + (dati[7] * 3)
            messaggio("Attacco: %i" % att, grigiochi, gsx // 32 * 23, gsy // 18 * 13, 45)
            messaggio("Difesa: %i" % dif, grigiochi, gsx // 32 * 23, gsy // 18 * 14, 45)
            messaggio("Probabilita' parata: %i" % par + "%", grigiochi, gsx // 32 * 23, gsy // 18 * 15, 45)
            # confronto statistiche
            # armi
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                if dati[41] != 0:
                    diff = 0 - (dati[6] * 10)
                    if dati[6] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                if dati[42] != 0:
                    diff = 10 - (dati[6] * 10)
                    if dati[6] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                if dati[43] != 0:
                    diff = 20 - (dati[6] * 10)
                    if dati[6] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                if dati[44] != 0:
                    diff = 30 - (dati[6] * 10)
                    if dati[6] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                if dati[45] != 0:
                    diff = 40 - (dati[6] * 10)
                    if dati[6] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                if dati[46] != 0:
                    diff = 50 - (dati[6] * 10)
                    if dati[6] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                if dati[47] != 0:
                    diff = 60 - (dati[6] * 10)
                    if dati[6] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                if dati[48] != 0:
                    diff = 70 - (dati[6] * 10)
                    if dati[6] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                if dati[49] != 0:
                    diff = 80 - (dati[6] * 10)
                    if dati[6] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                if dati[50] != 0:
                    diff = 90 - (dati[6] * 10)
                    if dati[6] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[6] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
            # armature
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                if dati[51] != 0:
                    diff = 0 - (dati[8] * 10)
                    if dati[8] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                if dati[52] != 0:
                    diff = 10 - (dati[8] * 10)
                    if dati[8] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                if dati[53] != 0:
                    diff = 20 - (dati[8] * 10)
                    if dati[8] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                if dati[54] != 0:
                    diff = 30 - (dati[8] * 10)
                    if dati[8] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                if dati[55] != 0:
                    diff = 40 - (dati[8] * 10)
                    if dati[8] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                if dati[56] != 0:
                    diff = 50 - (dati[8] * 10)
                    if dati[8] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                if dati[57] != 0:
                    diff = 60 - (dati[8] * 10)
                    if dati[8] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                if dati[58] != 0:
                    diff = 70 - (dati[8] * 10)
                    if dati[8] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                if dati[59] != 0:
                    diff = 80 - (dati[8] * 10)
                    if dati[8] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                if dati[60] != 0:
                    diff = 90 - (dati[8] * 10)
                    if dati[8] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[8] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            # scudi
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 6:
                if dati[61] != 0:
                    diff = 0 - (dati[7] * 5)
                    if dati[7] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 0 - (dati[7] * 3)
                    if dati[7] > 0:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    else:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 7:
                if dati[62] != 0:
                    diff = 5 - (dati[7] * 5)
                    if dati[7] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 3 - (dati[7] * 3)
                    if dati[7] > 1:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 1:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 1:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 8:
                if dati[63] != 0:
                    diff = 10 - (dati[7] * 5)
                    if dati[7] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 6 - (dati[7] * 3)
                    if dati[7] > 2:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 2:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 2:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 9:
                if dati[64] != 0:
                    diff = 15 - (dati[7] * 5)
                    if dati[7] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 9 - (dati[7] * 3)
                    if dati[7] > 3:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 3:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 3:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 10:
                if dati[65] != 0:
                    diff = 20 - (dati[7] * 5)
                    if dati[7] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 12 - (dati[7] * 3)
                    if dati[7] > 4:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 4:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 4:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 11:
                if dati[66] != 0:
                    diff = 25 - (dati[7] * 5)
                    if dati[7] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 15 - (dati[7] * 3)
                    if dati[7] > 5:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 5:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 5:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 12:
                if dati[67] != 0:
                    diff = 30 - (dati[7] * 5)
                    if dati[7] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 18 - (dati[7] * 3)
                    if dati[7] > 6:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 6:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 6:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 13:
                if dati[68] != 0:
                    diff = 35 - (dati[7] * 5)
                    if dati[7] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 21 - (dati[7] * 3)
                    if dati[7] > 7:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 7:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 7:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 14:
                if dati[69] != 0:
                    diff = 40 - (dati[7] * 5)
                    if dati[7] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 24 - (dati[7] * 3)
                    if dati[7] > 8:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 8:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 8:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)
            if xp == gsx // 32 * 15 and yp == gsy // 18 * 15:
                if dati[70] != 0:
                    diff = 45 - (dati[7] * 5)
                    if dati[7] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[7] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
                    diff = 27 - (dati[7] * 3)
                    if dati[7] > 9:
                        messaggio(str(diff) + "%", rosso, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] < 9:
                        messaggio("+" + str(diff) + "%", verde, gsx // 32 * 30, gsy // 18 * 15, 50)
                    elif dati[7] == 9:
                        messaggio("+" + str(diff) + "%", grigiochi, gsx // 32 * 30, gsy // 18 * 15, 50)

            # puntatore vecchio
            if dati[6] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
            if dati[6] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
            if dati[6] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
            if dati[6] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
            if dati[6] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
            if dati[6] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
            if dati[6] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
            if dati[6] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
            if dati[6] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
            if dati[6] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

            if dati[8] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 6))
            if dati[8] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 7))
            if dati[8] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 8))
            if dati[8] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 9))
            if dati[8] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 10))
            if dati[8] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 11))
            if dati[8] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 12))
            if dati[8] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 13))
            if dati[8] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 14))
            if dati[8] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * 15))

            if dati[7] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 6))
            if dati[7] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 7))
            if dati[7] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 8))
            if dati[7] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 9))
            if dati[7] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 10))
            if dati[7] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 11))
            if dati[7] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 12))
            if dati[7] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 13))
            if dati[7] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 14))
            if dati[7] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 15, gsy // 18 * 15))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati


def sceglicondiz(dati, condizione):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 4.5
    risposta = False

    # carico le scenette
    scecond = [0]
    i = 1
    while i <= 20:
        condizioneimm = pygame.image.load("Immagini\GrafCondizioni\Condizione%i.png" % i)
        scecond.append(pygame.transform.scale(condizioneimm, (gpx * 12, gpy * 9)))
        i = i + 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

        messaggio("Scegli condizione", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
            messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
            messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        if dati[81] > 0:
            messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                schermo.blit(scecond[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai pv < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[82] > 0:
            messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                schermo.blit(scecond[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai pv < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[83] > 0:
            messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                schermo.blit(scecond[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai pv < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[84] > 0:
            messaggio("Rallo con veleno", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                schermo.blit(scecond[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Rallo con veleno:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te quando hai veleno", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[85] > 0:
            messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                schermo.blit(scecond[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco surriscaldato:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha surriscaldamento", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[86] > 0:
            messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                schermo.blit(scecond[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco con pe < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha pe < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[87] > 0:
            messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                schermo.blit(scecond[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco con pe < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha pe < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[88] > 0:
            messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                schermo.blit(scecond[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Colco con pe < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco quando ha pe < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[89] > 0:
            messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                schermo.blit(scecond[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Sempre a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su di te in continuazione (se l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("quando lo status non e' attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[90] > 0:
            messaggio("Sempre a Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                schermo.blit(scecond[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Sempre a Colco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione su Colco in continuazione (se l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("quando lo status non e' attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        if dati[91] > 0:
            messaggio("Nemico piu' vicino a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                schermo.blit(scecond[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico piu' vicino a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico piu' vicino a te", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[92] > 0:
            messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                schermo.blit(scecond[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico vicino:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico piu' vicino a Colco nel", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("raggio di 3 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[93] > 0:
            messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                schermo.blit(scecond[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico lontano:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico lontano (distante di 4 o", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("piu' caselle) piu' vicino a Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[94] > 0:
            messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                schermo.blit(scecond[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con pv < 80% (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("molteplici bersagli, esegue l'azione sul nemico con", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("piu' pv tra quelli che rispettano la condizione)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[95] > 0:
            messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                schermo.blit(scecond[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con pv < 50% (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("molteplici bersagli, esegue l'azione sul nemico con", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("piu' pv tra quelli che rispettano la condizione)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[96] > 0:
            messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                schermo.blit(scecond[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con pv < 30% (in caso di", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("molteplici bersagli, esegue l'azione sul nemico con", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("piu' pv tra quelli che rispettano la condizione)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[97] > 0:
            messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                schermo.blit(scecond[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Nemico con meno pv:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione sul nemico con meno pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[98] > 0:
            messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                schermo.blit(scecond[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Numero di nemici > 1:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione quando nella stanza ci sono piu' di 1", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("nemico (in caso di azione a bersaglio singolo, l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("viene eseguita sul nemico piu' vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[99] > 0:
            messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                schermo.blit(scecond[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Numero di nemici > 4:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione quando nella stanza ci sono piu' di 4", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("nemici (in caso di azione a bersaglio singolo, l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("viene eseguita sul nemico piu' vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[100] > 0:
            messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                schermo.blit(scecond[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Numero di nemici > 7:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("esegue l'azione quando nella stanza ci sono piu' di 7", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("nemici (in caso di azione a bersaglio singolo, l'azione", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
                messaggio("viene eseguita sul nemico piu' vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16,
                          40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6
        while i <= 10:
            if condizione == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6
        while i <= 20:
            if condizione == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
            i = i + 1
            k = k + 1
        if condizione == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True

                if event.key == pygame.K_s:
                    if yp == gsy // 18 * 4.5:
                        spostapun.play()
                        yp = yp + gsy // 18 * 1.5
                    else:
                        if yp != gsy // 18 * 15:
                            spostapun.play()
                            yp = yp + gsy // 18 * 1
                        elif yp == gsy // 18 * 15:
                            if xp == gsx // 32 * 1:
                                spostapun.play()
                                yp = gsy // 18 * 4.5
                            else:
                                spostapun.play()
                                yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if yp == gsy // 18 * 6:
                        if xp == gsx // 32 * 1:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1.5
                        else:
                            spostapun.play()
                            yp = gsy // 18 * 15
                    else:
                        if yp != gsy // 18 * 4.5:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1
                        elif yp == gsy // 18 * 4.5:
                            spostapun.play()
                            yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 8:
                            spostapun.play()
                            xp = xp + gsx // 32 * 7
                        elif xp == gsx // 32 * 8:
                            spostapun.play()
                            xp = gsx // 32 * 1
                    else:
                        selimp.play()
                if event.key == pygame.K_a:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 1:
                            spostapun.play()
                            xp = xp - gsx // 32 * 7
                        elif xp == gsx // 32 * 1:
                            spostapun.play()
                            xp = gsx // 32 * 8
                    else:
                        selimp.play()

                if event.key == pygame.K_SPACE:

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
                    i = 81
                    c = 1
                    k = 6
                    while i <= 90:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                return c
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    i = 91
                    c = 11
                    k = 6
                    while i <= 100:
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                return c
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                        selezione.play()
                        return 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

            messaggio("Scegli condizione", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            if dati[81] > 0:
                messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                    schermo.blit(scecond[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai pv < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[82] > 0:
                messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                    schermo.blit(scecond[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai pv < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[83] > 0:
                messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                    schermo.blit(scecond[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai pv < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[84] > 0:
                messaggio("Rallo con veleno", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                    schermo.blit(scecond[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Rallo con veleno:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te quando hai veleno", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[85] > 0:
                messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                    schermo.blit(scecond[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco surriscaldato:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[86] > 0:
                messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                    schermo.blit(scecond[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco con pe < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha pe < 80%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[87] > 0:
                messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                    schermo.blit(scecond[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco con pe < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha pe < 50%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[88] > 0:
                messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                    schermo.blit(scecond[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Colco con pe < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco quando ha pe < 30%", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[89] > 0:
                messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                    schermo.blit(scecond[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Sempre a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su di te in continuazione (se l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("quando lo status non e' attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[90] > 0:
                messaggio("Sempre a Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                    schermo.blit(scecond[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Sempre a Colco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione su Colco in continuazione (se l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("comporta uno status alterativo, viene eseguita solo", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("quando lo status non e' attivo)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if dati[91] > 0:
                messaggio("Nemico piu' vicino a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                    schermo.blit(scecond[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico piu' vicino a Rallo:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico piu' vicino a te", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[92] > 0:
                messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                    schermo.blit(scecond[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico vicino:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico piu' vicino a Colco nel", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("raggio di 3 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[93] > 0:
                messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                    schermo.blit(scecond[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico lontano:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico lontano (distante di 4 o", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("piu' caselle) piu' vicino a Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[94] > 0:
                messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                    schermo.blit(scecond[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con pv < 80%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con pv < 80% (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("molteplici bersagli, esegue l'azione sul nemico con", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("piu' pv tra quelli che rispettano la condizione)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[95] > 0:
                messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                    schermo.blit(scecond[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con pv < 50%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con pv < 50% (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("molteplici bersagli, esegue l'azione sul nemico con", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("piu' pv tra quelli che rispettano la condizione)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[96] > 0:
                messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                    schermo.blit(scecond[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con pv < 30%:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con pv < 30% (in caso di", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("molteplici bersagli, esegue l'azione sul nemico con", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("piu' pv tra quelli che rispettano la condizione)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[97] > 0:
                messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                    schermo.blit(scecond[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Nemico con meno pv:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione sul nemico con meno pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[98] > 0:
                messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                    schermo.blit(scecond[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Numero di nemici > 1:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione quando nei paraggi ci sono piu' di 1", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("nemico (in caso di tecnica a bersaglio singolo, l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("viene eseguita sul nemico piu' vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[99] > 0:
                messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                    schermo.blit(scecond[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Numero di nemici > 4:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione quando nei paraggi ci sono piu' di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("nemici (in caso di tecnica a bersaglio singolo, l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("viene eseguita sul nemico piu' vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[100] > 0:
                messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                    schermo.blit(scecond[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Numero di nemici > 7:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("esegue l'azione quando nei paraggi ci sono piu' di 7", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("nemici (in caso di tecnica a bersaglio singolo, l'azione", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
                    messaggio("viene eseguita sul nemico piu' vicino a Colco)", grigiochi, gsx // 32 * 18, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6
            while i <= 10:
                if condizione == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6
            while i <= 20:
                if condizione == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
                i = i + 1
                k = k + 1
            if condizione == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return condizione


def sceglitecn(dati, tecnica):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 4.5
    usa = 0
    risposta = False

    # carico le scenette
    scetecn = [0]
    i = 1
    while i <= 20:
        tecnicaimm = pygame.image.load("Immagini\GrafTecniche\Tecnica%i.png" % i)
        scetecn.append(pygame.transform.scale(tecnicaimm, (gpx * 12, gpy * 9)))
        i = i + 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

        messaggio("Scegli tecnica", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
            messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
            messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        if dati[11] > 0:
            messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6 or usa == 9:
                schermo.blit(scetecn[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[12] > 0:
            messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 1:
                schermo.blit(scetecn[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("recupera un po' dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[13] > 0:
            messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 2:
                schermo.blit(scetecn[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("cura avvelenamento", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[14] > 0:
            messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9 or usa == 10:
                schermo.blit(scetecn[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[15] > 0:
            messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10 or usa == 11:
                schermo.blit(scetecn[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge danni a tutti i nemici entro il raggio di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 14,
                          40)
                messaggio("caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[16] > 0:
            messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11 or usa == 12:
                schermo.blit(scetecn[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("annulla il surriscaldamento ma richiede due turni", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[17] > 0:
            messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 3:
                schermo.blit(scetecn[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("ricarica un po' Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[18] > 0:
            messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 4:
                schermo.blit(scetecn[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("recupera molti dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[19] > 0:
            messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14 or usa == 13:
                schermo.blit(scetecn[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[20] > 0:
            messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15 or usa == 14:
                schermo.blit(scetecn[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        if dati[21] > 0:
            messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6 or usa == 15:
                schermo.blit(scetecn[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 15", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("permette a Colco, se non surriscaldato, di eseguire due", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("azioni al turno. Dopo 15 turni provoca surriscaldamento", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[22] > 0:
            messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 7) or usa == 7:
                schermo.blit(scetecn[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("incrementa il tuo attacco per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[23] > 0:
            messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 8) or usa == 8:
                schermo.blit(scetecn[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("incrementa la tua difesa per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[24] > 0:
            messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9 or usa == 16:
                schermo.blit(scetecn[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("tutte le tecniche costano la meta' dei pe per 15 turni", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("(si annulla con surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[25] > 0:
            messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10 or usa == 17:
                schermo.blit(scetecn[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge molti danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("di 5 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[26] > 0:
            messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 11) or usa == 5:
                schermo.blit(scetecn[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("recupera un enorme parte dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[27] > 0:
            messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 12) or usa == 6:
                schermo.blit(scetecn[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("ricarica di molto Colco ma richiede due turni e", grigiochi, gsx // 32 * 18, gsy // 18 * 14,
                          40)
                messaggio("provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[28] > 0:
            messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13 or usa == 18:
                schermo.blit(scetecn[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[29] > 0:
            messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14 or usa == 19:
                schermo.blit(scetecn[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[30] > 0:
            messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15 or usa == 20:
                schermo.blit(scetecn[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                messaggio("infligge enormi danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 14, 40)
                messaggio("di 6 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

        # puntatore vecchio
        i = 1
        k = 6
        while i <= 10:
            if tecnica == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
            i = i + 1
            k = k + 1
        i = 11
        k = 6
        while i <= 20:
            if tecnica == i:
                schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
            i = i + 1
            k = k + 1
        if tecnica == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True

                if event.key == pygame.K_s:
                    if yp == gsy // 18 * 4.5:
                        spostapun.play()
                        yp = yp + gsy // 18 * 1.5
                    else:
                        if yp != gsy // 18 * 15:
                            spostapun.play()
                            yp = yp + gsy // 18 * 1
                        elif yp == gsy // 18 * 15:
                            if xp == gsx // 32 * 1:
                                spostapun.play()
                                yp = gsy // 18 * 4.5
                            else:
                                spostapun.play()
                                yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if yp == gsy // 18 * 6:
                        if xp == gsx // 32 * 1:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1.5
                        else:
                            spostapun.play()
                            yp = gsy // 18 * 15
                    else:
                        if yp != gsy // 18 * 4.5:
                            spostapun.play()
                            yp = yp - gsy // 18 * 1
                        elif yp == gsy // 18 * 4.5:
                            spostapun.play()
                            yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 8:
                            spostapun.play()
                            xp = xp + gsx // 32 * 7
                        elif xp == gsx // 32 * 8:
                            spostapun.play()
                            xp = gsx // 32 * 1
                    else:
                        selimp.play()
                if event.key == pygame.K_a:
                    if yp != gsy // 18 * 4.5:
                        if xp != gsx // 32 * 1:
                            spostapun.play()
                            xp = xp - gsx // 32 * 7
                        elif xp == gsx // 32 * 1:
                            spostapun.play()
                            xp = gsx // 32 * 8
                    else:
                        selimp.play()

                if event.key == pygame.K_SPACE:

                    i = 11
                    c = 1
                    k = 6
                    while i <= 20:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                tecnica = c
                                risposta = True
                                break
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    i = 21
                    c = 11
                    k = 6
                    while i <= 30:
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * k:
                            if dati[i] != 0:
                                selezione.play()
                                tecnica = c
                                risposta = True
                                break
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1
                        k = k + 1
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                        selezione.play()
                        risposta = True
                        tecnica = 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,(posizionex,posizioney,larghezza,altezza,spessore))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 5, gsy // 18 * 2))

            messaggio("Scegli tecnica", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            messaggio("Cancella", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 45)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 4.5:
                messaggio("Cancella:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                messaggio("cancella il settaggio di Colco", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            if dati[11] > 0:
                messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 6 or usa == 9:
                    schermo.blit(scetecn[1], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[12] > 0:
                messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 1:
                    schermo.blit(scetecn[2], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("recupera un po' dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[13] > 0:
                messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 2:
                    schermo.blit(scetecn[3], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("cura avvelenamento", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[14] > 0:
                messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 9 or usa == 10:
                    schermo.blit(scetecn[4], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[15] > 0:
                messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 10 or usa == 11:
                    schermo.blit(scetecn[5], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge danni a tutti i nemici entro il raggio di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[16] > 0:
                messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 11 or usa == 12:
                    schermo.blit(scetecn[6], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("annulla il surriscaldamento ma richiede due turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[17] > 0:
                messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 3:
                    schermo.blit(scetecn[7], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("ricarica un po' Colco ma richiede due turni e provoca", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[18] > 0:
                messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 4:
                    schermo.blit(scetecn[8], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("recupera molti dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[19] > 0:
                messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 14 or usa == 13:
                    schermo.blit(scetecn[9], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[20] > 0:
                messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 15 or usa == 14:
                    schermo.blit(scetecn[10], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if dati[21] > 0:
                messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 6 or usa == 15:
                    schermo.blit(scetecn[11], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 15", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("permette a Colco, se non surriscaldato, di eseguire due", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("azioni al turno. Dopo 15 turni provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[22] > 0:
                messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 7) or usa == 7:
                    schermo.blit(scetecn[12], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("incrementa il tuo attacco per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[23] > 0:
                messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 8) or usa == 8:
                    schermo.blit(scetecn[13], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("incrementa la tua difesa per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[24] > 0:
                messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 9 or usa == 16:
                    schermo.blit(scetecn[14], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("tutte le tecniche costano la meta' dei pe per 15 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("(si annulla con surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[25] > 0:
                messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 10 or usa == 17:
                    schermo.blit(scetecn[15], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge molti danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("di 5 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[26] > 0:
                messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 11) or usa == 5:
                    schermo.blit(scetecn[16], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("recupera un enorme parte dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[27] > 0:
                messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 12) or usa == 6:
                    schermo.blit(scetecn[17], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("ricarica di molto Colco ma richiede due turni e", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[28] > 0:
                messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 13 or usa == 18:
                    schermo.blit(scetecn[18], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[29] > 0:
                messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 14 or usa == 19:
                    schermo.blit(scetecn[19], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[30] > 0:
                messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 15 or usa == 20:
                    schermo.blit(scetecn[20], (gsx // 32 * 18, gsy // 18 * 3.5))
                    messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 13, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 13, 40)
                    messaggio("infligge enormi danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18, gsy // 18 * 14, 40)
                    messaggio("di 6 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)

            # puntatore vecchio
            i = 1
            k = 6
            while i <= 10:
                if tecnica == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * k))
                i = i + 1
                k = k + 1
            i = 11
            k = 6
            while i <= 20:
                if tecnica == i:
                    schermo.blit(puntatorevecchio, (gsx // 32 * 8, gsy // 18 * k))
                i = i + 1
                k = k + 1
            if tecnica == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 4.5))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return tecnica


def equiprobo(dati):
    robosta = pygame.transform.scale(roboo, (gpx * 8, gpy * 8))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    carim = True
    risposta = False

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 6, gsy // 18 * 12))
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 8, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12))

        if carim:
            armrobs = pygame.image.load("Immagini\Armrobs\Armrob%is.png" % dati[9])
            armrob = pygame.transform.scale(armrobs, (gpx * 8, gpy * 8))
            carim = False
        messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)

        # equip batteria
        messaggio("Batterie", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 60)
        if dati[71] > 0:
            messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[72] > 0:
            messaggio("Batteria scarica", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[73] > 0:
            messaggio("Batteria piccola", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[74] > 0:
            messaggio("Batteria media", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[75] > 0:
            messaggio("Batteria grande", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[76] > 0:
            messaggio("Batteria discreta", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[77] > 0:
            messaggio("Batteria affidabile", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[78] > 0:
            messaggio("Batteria extra", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[79] > 0:
            messaggio("Batteria efficiente", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[80] > 0:
            messaggio("Batteria illimitata", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

        # programmazione Colco
        messaggio("Condizione...", grigiochi, gsx // 32 * 9, gsy // 18 * 4.5, 60)
        c = 6
        for i in range(101, 111):
            if dati[i] == -1:
                messaggio("---", grigioscu, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 0:
                messaggio("---", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 1:
                messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 2:
                messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 3:
                messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 4:
                messaggio("Rallo con veleno", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 5:
                messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 6:
                messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 7:
                messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 8:
                messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 9:
                messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 10:
                messaggio("Sempre a Colco", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 11:
                messaggio("Nemico piu' vicino a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 12:
                messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 13:
                messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 14:
                messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 15:
                messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 16:
                messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 17:
                messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 18:
                messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 19:
                messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            if dati[i] == 20:
                messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
            c = c + 1
        messaggio("...Tecnica", grigiochi, gsx // 32 * 16, gsy // 18 * 4.5, 60)
        c = 6
        for i in range(111, 121):
            if dati[i] == -1:
                messaggio("---", grigioscu, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 0:
                messaggio("---", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 1:
                messaggio("Scossa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 2:
                messaggio("Cura", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 3:
                messaggio("Antidoto", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 4:
                messaggio("Freccia elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 5:
                messaggio("Campo elettromagnetico", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 6:
                messaggio("Raffreddamento", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 7:
                messaggio("Auto-ricarica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 8:
                messaggio("Cura +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 9:
                messaggio("Scossa +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 10:
                messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 11:
                messaggio("Velocizza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 12:
                messaggio("Carica attacco", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 13:
                messaggio("Carica difesa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 14:
                messaggio("Efficienza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 15:
                messaggio("Campo elettromagnetico +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 16:
                messaggio("Cura ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 17:
                messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 18:
                messaggio("Scossa ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 19:
                messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            if dati[i] == 20:
                messaggio("Campo elettromagnetico ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
            c = c + 1

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(robosta, (gsx // 32 * 23.5, gsy // 18 * 3.5))
        schermo.blit(armrob, (gsx // 32 * 23.5, gsy // 18 * 3.5))
        entot = 300 + (dati[9] * 100)
        difro = 10 + (dati[9] * 10)
        messaggio("Pe totali: %i" % entot, grigiochi, gsx // 32 * 24, gsy // 18 * 13, 45)
        messaggio("Difesa: %i" % difro, grigiochi, gsx // 32 * 24, gsy // 18 * 14, 45)

        # mostrare differenze statistiche delle batterie
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
            if dati[71] != 0:
                diff = 0 - (dati[9] * 100)
                if dati[9] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 0 - (dati[9] * 10)
                if dati[9] > 0:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                else:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
            if dati[72] != 0:
                diff = 100 - (dati[9] * 100)
                if dati[9] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 10 - (dati[9] * 10)
                if dati[9] > 1:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 1:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 1:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
            if dati[73] != 0:
                diff = 200 - (dati[9] * 100)
                if dati[9] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 20 - (dati[9] * 10)
                if dati[9] > 2:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 2:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 2:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
            if dati[74] != 0:
                diff = 300 - (dati[9] * 100)
                if dati[9] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 30 - (dati[9] * 10)
                if dati[9] > 3:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 3:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 3:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
            if dati[75] != 0:
                diff = 400 - (dati[9] * 100)
                if dati[9] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 40 - (dati[9] * 10)
                if dati[9] > 4:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 4:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 4:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
            if dati[76] != 0:
                diff = 500 - (dati[9] * 100)
                if dati[9] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 50 - (dati[9] * 10)
                if dati[9] > 5:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 5:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 5:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
            if dati[77] != 0:
                diff = 600 - (dati[9] * 100)
                if dati[9] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 60 - (dati[9] * 10)
                if dati[9] > 6:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 6:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 6:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
            if dati[78] != 0:
                diff = 700 - (dati[9] * 100)
                if dati[9] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 70 - (dati[9] * 10)
                if dati[9] > 7:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 7:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 7:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
            if dati[79] != 0:
                diff = 800 - (dati[9] * 100)
                if dati[9] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 80 - (dati[9] * 10)
                if dati[9] > 8:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 8:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 8:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
            if dati[80] != 0:
                diff = 900 - (dati[9] * 100)
                if dati[9] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                elif dati[9] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                diff = 90 - (dati[9] * 10)
                if dati[9] > 9:
                    messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] < 9:
                    messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                elif dati[9] == 9:
                    messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)

        # puntatore vecchio
        if dati[9] == 0:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
        if dati[9] == 1:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
        if dati[9] == 2:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
        if dati[9] == 3:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
        if dati[9] == 4:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
        if dati[9] == 5:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
        if dati[9] == 6:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
        if dati[9] == 7:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
        if dati[9] == 8:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
        if dati[9] == 9:
            schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    risposta = True
                if event.key == pygame.K_s:
                    if (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    elif yp == gsy // 18 * 15:
                        spostapun.play()
                        yp = gsy // 18 * 6
                if event.key == pygame.K_w:
                    if (yp != gsy // 18 * 6):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    elif yp == gsy // 18 * 6:
                        spostapun.play()
                        yp = gsy // 18 * 15
                if event.key == pygame.K_d:
                    if (xp != gsx // 32 * 15):
                        spostapun.play()
                        xp = xp + gsx // 32 * 7
                    elif xp == gsx // 32 * 15:
                        spostapun.play()
                        xp = gsx // 32 * 1
                if event.key == pygame.K_a:
                    if (xp != gsx // 32 * 1):
                        spostapun.play()
                        xp = xp - gsx // 32 * 7
                    elif xp == gsx // 32 * 1:
                        spostapun.play()
                        xp = gsx // 32 * 15
                if event.key == pygame.K_SPACE:
                    carim = True
                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    # armrob
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                        if dati[71] != 0:
                            selezione.play()
                            dati[9] = 0
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                        if dati[72] != 0:
                            selezione.play()
                            dati[9] = 1
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                        if dati[73] != 0:
                            selezione.play()
                            dati[9] = 2
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                        if dati[74] != 0:
                            selezione.play()
                            dati[9] = 3
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                        if dati[75] != 0:
                            selezione.play()
                            dati[9] = 4
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                        if dati[76] != 0:
                            selezione.play()
                            dati[9] = 5
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                        if dati[77] != 0:
                            selezione.play()
                            dati[9] = 6
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                        if dati[78] != 0:
                            selezione.play()
                            dati[9] = 7
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                        if dati[79] != 0:
                            selezione.play()
                            dati[9] = 8
                        else:
                            selimp.play()
                    if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                        if dati[80] != 0:
                            selezione.play()
                            dati[9] = 9
                        else:
                            selimp.play()

                    # condizioni
                    i = 101
                    c = 6
                    while i <= 110:
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * c:
                            if dati[i] != -1:
                                selezione.play()
                                dati[i] = sceglicondiz(dati, dati[i])
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1

                    # tecniche
                    i = 111
                    c = 6
                    while i <= 120:
                        if xp == gsx // 32 * 15 and yp == gsy // 18 * c:
                            if dati[i] != -1:
                                selezione.play()
                                dati[i] = sceglitecn(dati, dati[i])
                            else:
                                selimp.play()
                        i = i + 1
                        c = c + 1

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione,larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 6, gsy // 18 * 12))
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 8, gsy // 18 * 4, gsx // 32 * 15, gsy // 18 * 12))

            if carim:
                armrobs = pygame.image.load("Immagini\Armrobs\Armrob%is.png" % dati[9])
                armrob = pygame.transform.scale(armrobs, (gpx * 8, gpy * 8))
                carim = False
            messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)

            # equip batteria
            messaggio("Batterie", grigiochi, gsx // 32 * 2, gsy // 18 * 4.5, 60)
            if dati[71] > 0:
                messaggio("Niente", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[72] > 0:
                messaggio("Batteria scarica", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[73] > 0:
                messaggio("Batteria piccola", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[74] > 0:
                messaggio("Batteria media", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[75] > 0:
                messaggio("Batteria grande", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[76] > 0:
                messaggio("Batteria discreta", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[77] > 0:
                messaggio("Batteria affidabile", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[78] > 0:
                messaggio("Batteria extra", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[79] > 0:
                messaggio("Batteria efficiente", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[80] > 0:
                messaggio("Batteria illimitata", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

            # programmazione Colco
            messaggio("Condizione...", grigiochi, gsx // 32 * 9, gsy // 18 * 4.5, 60)
            c = 6
            for i in range(101, 111):
                if dati[i] == -1:
                    messaggio("---", grigioscu, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 0:
                    messaggio("---", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 1:
                    messaggio("Rallo con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 2:
                    messaggio("Rallo con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 3:
                    messaggio("Rallo con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 4:
                    messaggio("Rallo con veleno", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 5:
                    messaggio("Colco surriscaldato", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 6:
                    messaggio("Colco con pe < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 7:
                    messaggio("Colco con pe < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 8:
                    messaggio("Colco con pe < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 9:
                    messaggio("Sempre a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 10:
                    messaggio("Sempre a Colco", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 11:
                    messaggio("Nemico piu' vicino a Rallo", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 12:
                    messaggio("Nemico vicino", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 13:
                    messaggio("Nemico lontano", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 14:
                    messaggio("Nemico con pv < 80%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 15:
                    messaggio("Nemico con pv < 50%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 16:
                    messaggio("Nemico con pv < 30%", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 17:
                    messaggio("Nemico con meno pv", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 18:
                    messaggio("Numero di nemici > 1", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 19:
                    messaggio("Numero di nemici > 4", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                if dati[i] == 20:
                    messaggio("Numero di nemici > 7", grigiochi, gsx // 32 * 9, gsy // 18 * c, 40)
                c = c + 1
            messaggio("...Tecnica", grigiochi, gsx // 32 * 16, gsy // 18 * 4.5, 60)
            c = 6
            for i in range(111, 121):
                if dati[i] == -1:
                    messaggio("---", grigioscu, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 0:
                    messaggio("---", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 1:
                    messaggio("Scossa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 2:
                    messaggio("Cura", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 3:
                    messaggio("Antidoto", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 4:
                    messaggio("Freccia elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 5:
                    messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 6:
                    messaggio("Raffreddamento", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 7:
                    messaggio("Auto-ricarica", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 8:
                    messaggio("Cura +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 9:
                    messaggio("Scossa +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 10:
                    messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 11:
                    messaggio("Velocizza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 12:
                    messaggio("Carica attacco", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 13:
                    messaggio("Carica difesa", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 14:
                    messaggio("Efficienza", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 15:
                    messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 16:
                    messaggio("Cura ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 17:
                    messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 18:
                    messaggio("Scossa ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 19:
                    messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                if dati[i] == 20:
                    messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 16, gsy // 18 * c, 40)
                c = c + 1

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(robosta, (gsx // 32 * 23.5, gsy // 18 * 3.5))
            schermo.blit(armrob, (gsx // 32 * 23.5, gsy // 18 * 3.5))
            entot = 300 + (dati[9] * 100)
            difro = 10 + (dati[9] * 10)
            messaggio("Pe totali: %i" % entot, grigiochi, gsx // 32 * 24, gsy // 18 * 13, 45)
            messaggio("Difesa: %i" % difro, grigiochi, gsx // 32 * 24, gsy // 18 * 14, 45)

            # mostrare differenze statistiche delle batterie
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                if dati[71] != 0:
                    diff = 0 - (dati[9] * 100)
                    if dati[9] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 0 - (dati[9] * 10)
                    if dati[9] > 0:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    else:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                if dati[72] != 0:
                    diff = 100 - (dati[9] * 100)
                    if dati[9] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 10 - (dati[9] * 10)
                    if dati[9] > 1:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 1:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 1:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                if dati[73] != 0:
                    diff = 200 - (dati[9] * 100)
                    if dati[9] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 20 - (dati[9] * 10)
                    if dati[9] > 2:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 2:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 2:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                if dati[74] != 0:
                    diff = 300 - (dati[9] * 100)
                    if dati[9] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 30 - (dati[9] * 10)
                    if dati[9] > 3:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 3:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 3:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                if dati[75] != 0:
                    diff = 400 - (dati[9] * 100)
                    if dati[9] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 40 - (dati[9] * 10)
                    if dati[9] > 4:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 4:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 4:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                if dati[76] != 0:
                    diff = 500 - (dati[9] * 100)
                    if dati[9] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 50 - (dati[9] * 10)
                    if dati[9] > 5:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 5:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 5:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                if dati[77] != 0:
                    diff = 600 - (dati[9] * 100)
                    if dati[9] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 60 - (dati[9] * 10)
                    if dati[9] > 6:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 6:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 6:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                if dati[78] != 0:
                    diff = 700 - (dati[9] * 100)
                    if dati[9] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 70 - (dati[9] * 10)
                    if dati[9] > 7:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 7:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 7:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                if dati[79] != 0:
                    diff = 800 - (dati[9] * 100)
                    if dati[9] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 80 - (dati[9] * 10)
                    if dati[9] > 8:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 8:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 8:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                if dati[80] != 0:
                    diff = 900 - (dati[9] * 100)
                    if dati[9] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 13, 50)
                    elif dati[9] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 13, 50)
                    diff = 90 - (dati[9] * 10)
                    if dati[9] > 9:
                        messaggio(str(diff), rosso, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] < 9:
                        messaggio("+" + str(diff), verde, gsx // 32 * 30, gsy // 18 * 14, 50)
                    elif dati[9] == 9:
                        messaggio("+" + str(diff), grigiochi, gsx // 32 * 30, gsy // 18 * 14, 50)

            # puntatore vecchio
            if dati[9] == 0:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 6))
            if dati[9] == 1:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 7))
            if dati[9] == 2:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 8))
            if dati[9] == 3:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 9))
            if dati[9] == 4:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 10))
            if dati[9] == 5:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 11))
            if dati[9] == 6:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 12))
            if dati[9] == 7:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 13))
            if dati[9] == 8:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 14))
            if dati[9] == 9:
                schermo.blit(puntatorevecchio, (gsx // 32 * 1, gsy // 18 * 15))

            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati


def tecniche(dati):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    usauno = False
    usa = 0
    risposta = False
    attacco = 0
    ok = True

    # carico le scenette
    scetecn = [0]
    i = 1
    while i <= 20:
        tecnica = pygame.image.load("Immagini\GrafTecniche\Tecnica%i.png" % i)
        scetecn.append(pygame.transform.scale(tecnica, (gpx * 7, gpy * 5)))
        i = i + 1

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))

        messaggio("Tecniche", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        if dati[11] > 0:
            messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 6 or usa == 1:
                schermo.blit(scetecn[1], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[12] > 0:
            messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 2:
                schermo.blit(scetecn[2], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("recupera un po' dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[13] > 0:
            messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 3:
                schermo.blit(scetecn[3], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("cura avvelenamento", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[14] > 0:
            messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 9 or usa == 4:
                schermo.blit(scetecn[4], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[15] > 0:
            messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 10 or usa == 5:
                schermo.blit(scetecn[5], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge danni a tutti i nemici entro il raggio di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 10,
                          40)
                messaggio("caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[16] > 0:
            messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 11 or usa == 6:
                schermo.blit(scetecn[6], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("annulla il surriscaldamento (in battaglia richiede", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("due turni)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[17] > 0:
            messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 7:
                schermo.blit(scetecn[7], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("ricarica un po' Colco (in battaglia richiede due turni", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("e provoca surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[18] > 0:
            messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 8:
                schermo.blit(scetecn[8], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("recupera molti dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[19] > 0:
            messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 14 or usa == 9:
                schermo.blit(scetecn[9], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[20] > 0:
            messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 1 and yp == gsy // 18 * 15 or usa == 10:
                schermo.blit(scetecn[10], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
        if dati[21] > 0:
            messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 6 or usa == 11:
                schermo.blit(scetecn[11], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 15", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("permette a Colco, se non surriscaldato, di eseguire due", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("azioni al turno. Dopo 15 turni provoca surriscaldamento", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
        if dati[22] > 0:
            messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 7) or usa == 12:
                schermo.blit(scetecn[12], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("incrementa il tuo attacco per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
        if dati[23] > 0:
            messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 8) or usa == 13:
                schermo.blit(scetecn[13], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("incrementa la tua difesa per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
        if dati[24] > 0:
            messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 9 or usa == 14:
                schermo.blit(scetecn[14], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("tutte le tecniche costano la meta' dei pe per 15 turni", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("(si annulla con surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
        if dati[25] > 0:
            messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 10 or usa == 15:
                schermo.blit(scetecn[15], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge molti danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("di 5 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
        if dati[26] > 0:
            messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 11) or usa == 16:
                schermo.blit(scetecn[16], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("recupera un enorme parte dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
        if dati[27] > 0:
            messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 8 and yp == gsy // 18 * 12) or usa == 17:
                schermo.blit(scetecn[17], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("ricarica di molto Colco (in battaglia richiede due", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("turni e provoca surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
        if dati[28] > 0:
            messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 13 or usa == 18:
                schermo.blit(scetecn[18], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
        if dati[29] > 0:
            messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 14 or usa == 19:
                schermo.blit(scetecn[19], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
        if dati[30] > 0:
            messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
            if xp == gsx // 32 * 8 and yp == gsy // 18 * 15 or usa == 20:
                schermo.blit(scetecn[20], (gsx // 32 * 23, gsy // 18 * 12))
                messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                messaggio("infligge enormi danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18,
                          gsy // 18 * 10, 40)
                messaggio("di 6 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

        # vita-status personaggio
        pvtot = 100 + (dati[4] * 5)
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 18, gsy // 18 * 5, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 18, gsy // 18 * 6, 50)
        persmen = pygame.transform.scale(persgra, (gpx * 3, gpy * 3))
        schermo.blit(persmen, (gsx // 32 * 19, (gsy // 18 * 1) + (gpy // 2)))
        schermo.blit(sfondostastart, (gsx // 32 * 18, (gsy // 18 * 7) + (gpy // 8)))
        if dati[121]:
            avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
            schermo.blit(avvelenato, (gsx // 32 * 18, gsy // 18 * 7))
        if dati[123] > 0:
            attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
            schermo.blit(attaccopiu, ((gsx // 32 * 18) + (2 * gpx // 4 * 3), gsy // 18 * 7))
        if dati[124] > 0:
            difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
            schermo.blit(difesapiu, ((gsx // 32 * 18) + (4 * gpx // 4 * 3), gsy // 18 * 7))
        # vita-status robo
        entot = 300 + (dati[9] * 100)
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 25, gsy // 18 * 5, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 25, gsy // 18 * 6, 50)
        robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
        schermo.blit(robomen, (gsx // 32 * 26, (gsy // 18 * 1) + (gpy // 2)))
        schermo.blit(sfondostastart, (gsx // 32 * 25, (gsy // 18 * 7) + (gpy // 8)))
        if dati[122] > 0:
            surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
            schermo.blit(surriscaldato, (gsx // 32 * 25, gsy // 18 * 7))
        if dati[125] > 0:
            velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
            schermo.blit(velocitapiu, ((gsx // 32 * 25) + (2 * gpx // 4 * 3), gsy // 18 * 7))
        if dati[126] > 0:
            efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
            schermo.blit(efficienzapiu, ((gsx // 32 * 25) + (4 * gpx // 4 * 3), gsy // 18 * 7))

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            ok = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if usa != 0:
                        selind.play()
                        if usa == 1:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 6
                        if usa == 2:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 7
                        if usa == 3:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 8
                        if usa == 4:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 9
                        if usa == 5:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 10
                        if usa == 6:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 11
                        if usa == 7:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 12
                        if usa == 8:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 13
                        if usa == 9:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 14
                        if usa == 10:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 15
                        if usa == 11:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 6
                        if usa == 12:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 7
                        if usa == 13:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 8
                        if usa == 14:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 9
                        if usa == 15:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 10
                        if usa == 16:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 11
                        if usa == 17:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 12
                        if usa == 18:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 13
                        if usa == 19:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 14
                        if usa == 20:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 15
                        usa = 0
                    else:
                        selind.play()
                        risposta = True

                if event.key == pygame.K_s and xp != gsx // 32 * 16 and xp != gsx // 32 * 19:
                    if (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    elif yp == gsy // 18 * 15:
                        spostapun.play()
                        yp = gsy // 18 * 6
                if event.key == pygame.K_w and xp != gsx // 32 * 16 and xp != gsx // 32 * 19:
                    if (yp != gsy // 18 * 6):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    elif yp == gsy // 18 * 6:
                        spostapun.play()
                        yp = gsy // 18 * 15
                if event.key == pygame.K_d and xp != gsx // 32 * 16 and xp != gsx // 32 * 19:
                    if (xp != gsx // 32 * 8):
                        spostapun.play()
                        xp = xp + gsx // 32 * 7
                    elif xp == gsx // 32 * 8:
                        spostapun.play()
                        xp = gsx // 32 * 1
                elif event.key == pygame.K_d and (xp == gsx // 32 * 16 or xp == gsx // 32 * 19):
                    if xp == gsx // 32 * 16:
                        spostapun.play()
                        xp = xp + gsx // 32 * 3
                    else:
                        selimp.play()
                if event.key == pygame.K_a and xp != gsx // 32 * 16 and xp != gsx // 32 * 19:
                    if (xp != gsx // 32 * 1):
                        spostapun.play()
                        xp = xp - gsx // 32 * 7
                    elif xp == gsx // 32 * 1:
                        spostapun.play()
                        xp = gsx // 32 * 8
                elif event.key == pygame.K_a and (xp == gsx // 32 * 16 or xp == gsx // 32 * 19):
                    if xp == gsx // 32 * 19:
                        spostapun.play()
                        xp = xp - gsx // 32 * 3
                    else:
                        selimp.play()

                if event.key == pygame.K_SPACE:
                    usadue = True

                    # usa?
                    if xp == gsx // 32 * 16 and yp == gsy // 18 * 14.5:
                        if usa == 1:
                            if dati[10] >= 5:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 6
                                attacco = 7
                            else:
                                ok = False
                                selimp.play()
                        if usa == 2:
                            if dati[10] >= 10:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 7
                                dati[10] = dati[10] - 10
                                dati[5] = dati[5] + 50
                                if dati[5] > pvtot:
                                    dati[5] = pvtot
                            else:
                                ok = False
                                selimp.play()
                        if usa == 3:
                            if dati[10] >= 10:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 8
                                dati[10] = dati[10] - 10
                                dati[121] = False
                            else:
                                ok = False
                                selimp.play()
                        if usa == 4:
                            if dati[10] >= 5:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 9
                                attacco = 8
                            else:
                                ok = False
                                selimp.play()
                        if usa == 5:
                            if dati[10] >= 10:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 10
                                attacco = 9
                            else:
                                ok = False
                                selimp.play()
                        if usa == 6:
                            if dati[10] >= 10:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 11
                                dati[10] = dati[10] - 10
                                dati[122] = 0
                            else:
                                ok = False
                                selimp.play()
                        if usa == 7:
                            if dati[10] >= 1:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 12
                                dati[10] = dati[10] - 1
                                dati[10] = dati[10] + 150
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                ok = False
                                selimp.play()
                        if usa == 8:
                            if dati[10] >= 20:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 13
                                dati[10] = dati[10] - 20
                                dati[5] = dati[5] + 150
                                if dati[5] > pvtot:
                                    dati[5] = pvtot
                            else:
                                ok = False
                                selimp.play()
                        if usa == 9:
                            if dati[10] >= 10:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 14
                                attacco = 10
                            else:
                                ok = False
                                selimp.play()
                        if usa == 10:
                            if dati[10] >= 10:
                                xp = gsx // 32 * 1
                                yp = gsy // 18 * 15
                                attacco = 11
                            else:
                                ok = False
                                selimp.play()
                        if usa == 11:
                            if dati[10] >= 15:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 6
                                dati[10] = dati[10] - 15
                                dati[125] = 15
                            else:
                                ok = False
                                selimp.play()
                        if usa == 12:
                            if dati[10] >= 20:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 7
                                dati[10] = dati[10] - 20
                                dati[123] = 10
                            else:
                                ok = False
                                selimp.play()
                        if usa == 13:
                            if dati[10] >= 20:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 8
                                dati[10] = dati[10] - 20
                                dati[124] = 10
                            else:
                                ok = False
                                selimp.play()
                        if usa == 14:
                            if dati[10] >= 30:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 9
                                dati[10] = dati[10] - 30
                                if dati[122] <= 0:
                                    dati[126] = 15
                            else:
                                ok = False
                                selimp.play()
                        if usa == 15:
                            if dati[10] >= 20:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 10
                                attacco = 12
                            else:
                                ok = False
                                selimp.play()
                        if usa == 16:
                            if dati[10] >= 30:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 11
                                dati[10] = dati[10] - 30
                                dati[5] = dati[5] + 300
                                if dati[5] > pvtot:
                                    dati[5] = pvtot
                            else:
                                ok = False
                                selimp.play()
                        if usa == 17:
                            if dati[10] >= 1:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 12
                                dati[10] = dati[10] - 1
                                dati[10] = dati[10] + 400
                                if dati[10] > entot:
                                    dati[10] = entot
                            else:
                                ok = False
                                selimp.play()
                        if usa == 18:
                            if dati[10] >= 20:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 13
                                attacco = 13
                            else:
                                ok = False
                                selimp.play()
                        if usa == 19:
                            if dati[10] >= 20:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 14
                                attacco = 14
                            else:
                                ok = False
                                selimp.play()
                        if usa == 20:
                            if dati[10] >= 30:
                                xp = gsx // 32 * 8
                                yp = gsy // 18 * 15
                                attacco = 15
                            else:
                                ok = False
                                selimp.play()
                        if ok:
                            selezione.play()
                            if attacco != 0:
                                risposta = True
                            usa = 0
                            usadue = False
                    elif xp == gsx // 32 * 19 and yp == gsy // 18 * 14.5:
                        selind.play()
                        if usa == 1:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 6
                        if usa == 2:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 7
                        if usa == 3:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 8
                        if usa == 4:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 9
                        if usa == 5:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 10
                        if usa == 6:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 11
                        if usa == 7:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 12
                        if usa == 8:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 13
                        if usa == 9:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 14
                        if usa == 10:
                            xp = gsx // 32 * 1
                            yp = gsy // 18 * 15
                        if usa == 11:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 6
                        if usa == 12:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 7
                        if usa == 13:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 8
                        if usa == 14:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 9
                        if usa == 15:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 10
                        if usa == 16:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 11
                        if usa == 17:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 12
                        if usa == 18:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 13
                        if usa == 19:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 14
                        if usa == 20:
                            xp = gsx // 32 * 8
                            yp = gsy // 18 * 15
                        usa = 0
                        usadue = False

                    if usadue:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                            if dati[11] != 0:
                                usa = 1
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                            if dati[12] != 0:
                                usa = 2
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                            if dati[13] != 0:
                                usa = 3
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                            if dati[14] != 0:
                                usa = 4
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                            if dati[15] != 0:
                                usa = 5
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                            if dati[16] != 0:
                                usa = 6
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                            if dati[17] != 0:
                                usa = 7
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                            if dati[18] != 0:
                                usa = 8
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                            if dati[19] != 0:
                                usa = 9
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                            if dati[20] != 0:
                                usa = 10
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 6:
                            if dati[21] != 0:
                                usa = 11
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 7:
                            if dati[22] != 0:
                                usa = 12
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 8:
                            if dati[23] != 0:
                                usa = 13
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 9:
                            if dati[24] != 0:
                                usa = 14
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 10:
                            if dati[25] != 0:
                                usa = 15
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 11:
                            if dati[26] != 0:
                                usa = 16
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 12:
                            if dati[27] != 0:
                                usa = 17
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 13:
                            if dati[28] != 0:
                                usa = 18
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 14:
                            if dati[29] != 0:
                                usa = 19
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 8 and yp == gsy // 18 * 15:
                            if dati[30] != 0:
                                usa = 20
                                usauno = True
                                selezione.play()
                            else:
                                selimp.play()

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 15, gsy // 18 * 11))

            messaggio("Tecniche", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            if dati[11] > 0:
                messaggio("Scossa", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 6 or usa == 1:
                    schermo.blit(scetecn[1], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Scossa:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[12] > 0:
                messaggio("Cura", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 2:
                    schermo.blit(scetecn[2], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Cura:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("recupera un po' dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[13] > 0:
                messaggio("Antidoto", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 3:
                    schermo.blit(scetecn[3], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Antidoto:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("cura avvelenamento", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[14] > 0:
                messaggio("Freccia elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 9 or usa == 4:
                    schermo.blit(scetecn[4], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Freccia elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 5", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[15] > 0:
                messaggio("Tempesta elettrica", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 10 or usa == 5:
                    schermo.blit(scetecn[5], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Tempesta elettrica:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge danni a tutti i nemici entro il raggio di 4", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[16] > 0:
                messaggio("Raffreddamento", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 11 or usa == 6:
                    schermo.blit(scetecn[6], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Raffreddamento:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("annulla il surriscaldamento (in battaglia richiede", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("due turni)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[17] > 0:
                messaggio("Auto-ricarica", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 7:
                    schermo.blit(scetecn[7], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Auto-ricarica:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("ricarica un po' Colco (in battaglia richiede due turni", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("e provoca surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[18] > 0:
                messaggio("Cura +", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 8:
                    schermo.blit(scetecn[8], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Cura +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("recupera molti dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[19] > 0:
                messaggio("Scossa +", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 14 or usa == 9:
                    schermo.blit(scetecn[9], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Scossa +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge molti danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[20] > 0:
                messaggio("Freccia elettrica +", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 1 and yp == gsy // 18 * 15 or usa == 10:
                    schermo.blit(scetecn[10], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Freccia elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 10", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge molti danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if dati[21] > 0:
                messaggio("Velocizza", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 6 or usa == 11:
                    schermo.blit(scetecn[11], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Velocizza:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 15", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("permette a Colco, se non surriscaldato, di eseguire due", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("azioni al turno. Dopo 15 turni provoca surriscaldamento", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 6, 40)
            if dati[22] > 0:
                messaggio("Carica attacco", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 7) or usa == 12:
                    schermo.blit(scetecn[12], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Carica attacco:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("incrementa il tuo attacco per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 7, 40)
            if dati[23] > 0:
                messaggio("Carica difesa", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 8) or usa == 13:
                    schermo.blit(scetecn[13], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Carica difesa:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("incrementa la tua difesa per 10 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 8, 40)
            if dati[24] > 0:
                messaggio("Efficienza", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 9 or usa == 14:
                    schermo.blit(scetecn[14], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Efficienza:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("tutte le tecniche costano la meta' dei pe per 15 turni", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("(si annulla con surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 9, 40)
            if dati[25] > 0:
                messaggio("Tempesta elettrica +", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 10 or usa == 15:
                    schermo.blit(scetecn[15], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Tempesta elettrica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge molti danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("di 5 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 40)
            if dati[26] > 0:
                messaggio("Cura ++", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 11) or usa == 16:
                    schermo.blit(scetecn[16], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Cura ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("recupera un enorme parte dei tuoi pv", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 11, 40)
            if dati[27] > 0:
                messaggio("Auto-ricarica +", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 8 and yp == gsy // 18 * 12) or usa == 17:
                    schermo.blit(scetecn[17], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Auto-ricarica +:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 1", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("ricarica di molto Colco (in battaglia richiede due", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("turni e provoca surriscaldamento)", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 12, 40)
            if dati[28] > 0:
                messaggio("Scossa ++", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 13 or usa == 18:
                    schermo.blit(scetecn[18], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Scossa ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge enormi danni a un nemico vicino", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 13, 40)
            if dati[29] > 0:
                messaggio("Freccia Elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 14 or usa == 19:
                    schermo.blit(scetecn[19], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Freccia Elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 20", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge enormi danni a distanza a un nemico", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 14, 40)
            if dati[30] > 0:
                messaggio("Tempesta elettrica ++", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)
                if xp == gsx // 32 * 8 and yp == gsy // 18 * 15 or usa == 20:
                    schermo.blit(scetecn[20], (gsx // 32 * 23, gsy // 18 * 12))
                    messaggio("Tempesta elettrica ++:", grigiochi, gsx // 32 * 18, gsy // 18 * 9, 40)
                    messaggio("Costo Pe: 30", grigiochi, gsx // 32 * 27, gsy // 18 * 9, 40)
                    messaggio("infligge enormi danni a tutti i nemici entro il raggio", grigiochi, gsx // 32 * 18, gsy // 18 * 10, 40)
                    messaggio("di 6 caselle", grigiochi, gsx // 32 * 18, gsy // 18 * 11, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 9, gsy // 18 * 15, 40)

            # menu conferma
            if usa != 0:
                pygame.draw.rect(schermo, grigio, (gsx // 32 * 16, gsy // 18 * 12, gsx // 32 * 6.5, gsy // 18 * 4))
                puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 3 * 2, gpy // 3 * 2))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = gsx // 32 * 19
                    yp = gsy // 18 * 14.5
                    usauno = False
                schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", grigiochi, gsx // 32 * 17, gsy // 18 * 12.5, 100)
                messaggio("Si", grigiochi, gsx // 32 * 17, gsy // 18 * 14.5, 60)
                messaggio("No", grigiochi, gsx // 32 * 20, gsy // 18 * 14.5, 60)
            else:
                puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))

            if not ok:
                messaggio("Pe insufficienti", rosso, gsx // 32 * 16, gsy // 18 * 16, 60)

            # vita-status personaggio
            pvtot = 100 + (dati[4] * 5)
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 18, gsy // 18 * 5, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 18, gsy // 18 * 6, 50)
            persmen = pygame.transform.scale(persgra, (gpx * 3, gpy * 3))
            schermo.blit(persmen, (gsx // 32 * 19, (gsy // 18 * 1) + (gpy // 2)))
            schermo.blit(sfondostastart, (gsx // 32 * 18, (gsy // 18 * 7) + (gpy // 8)))
            if dati[121]:
                avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
                schermo.blit(avvelenato, (gsx // 32 * 18, gsy // 18 * 7))
            if dati[123] > 0:
                attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
                schermo.blit(attaccopiu, ((gsx // 32 * 18) + (2 * gpx // 4 * 3), gsy // 18 * 7))
            if dati[124] > 0:
                difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
                schermo.blit(difesapiu, ((gsx // 32 * 18) + (4 * gpx // 4 * 3), gsy // 18 * 7))
            # vita-status robo
            entot = 300 + (dati[9] * 100)
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 25, gsy // 18 * 5, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 25, gsy // 18 * 6, 50)
            robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
            schermo.blit(robomen, (gsx // 32 * 26, (gsy // 18 * 1) + (gpy // 2)))
            schermo.blit(sfondostastart, (gsx // 32 * 25, (gsy // 18 * 7) + (gpy // 8)))
            if dati[122] > 0:
                surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
                schermo.blit(surriscaldato, (gsx // 32 * 25, gsy // 18 * 7))
            if dati[125] > 0:
                velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
                schermo.blit(velocitapiu, ((gsx // 32 * 25) + (2 * gpx // 4 * 3), gsy // 18 * 7))
            if dati[126] > 0:
                efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
                schermo.blit(efficienzapiu, ((gsx // 32 * 25) + (4 * gpx // 4 * 3), gsy // 18 * 7))

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati, attacco


def oggetti(dati):
    oggetton = 1
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))
    puntatorevecchio = pygame.transform.scale(puntatoreorigivecchio, (gpx // 12 * 5, gpy // 12 * 5))
    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 6
    carim = True
    usauno = False
    usa = 0
    risposta = False
    attacco = 0

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 9, gsy // 18 * 11))

        if carim:
            if dati[oggetton + 30] >= 0:
                oggetto = pygame.image.load("Immagini\Oggetti\Oggetto%i.png" % oggetton)
                oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
            else:
                oggetto = pygame.image.load("Immagini\Oggetti\Sconosciuto.png")
                oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
            carim = False

        # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
        messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
        if dati[31] >= 0:
            messaggio("Pozione x %i" % dati[31], grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 6) or usa == 1:
                messaggio("Pozione: recupera 100 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
        if dati[32] >= 0:
            messaggio("Caricabatterie x %i" % dati[32], grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 2:
                messaggio("Caricabatterie: recupera 250 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
        if dati[33] >= 0:
            messaggio("Bomba x %i" % dati[33], grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 3:
                messaggio("Bomba: infligge un po' di danni ai nemici su", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                messaggio("cui e' lanciata", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
        if dati[34] >= 0:
            messaggio("Medicina x %i" % dati[34], grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 9) or usa == 4:
                messaggio("Medicina: cura avvelenamento", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
        if dati[35] >= 0:
            messaggio("Bomba velenosa x %i" % dati[35], grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 10) or usa == 5:
                messaggio("Bomba velenosa: infligge avvelenamento a", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
        if dati[36] >= 0:
            messaggio("Esca x %i" % dati[36], grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 11) or usa == 6:
                messaggio("Esca: distrae i nemici vicini per un po'", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                messaggio("di tempo. Viene utilizzata per fuggire", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                messaggio("(Colco uscira' dalla battaglia). E' possibile", grigiochi, gsx // 32 * 20, gsy // 18 * 15,
                          40)
                messaggio("riprenderla passandoci sopra", grigiochi, gsx // 32 * 20, gsy // 18 * 16, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
        if dati[37] >= 0:
            messaggio("Super pozione x %i" % dati[37], grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 7:
                messaggio("Super pozione: recupera 300 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
        if dati[38] >= 0:
            messaggio("Caricabatterie migliorato x %i" % dati[38], grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 8:
                messaggio("Caricabatterie migliorato: recupera 600 pe", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                messaggio("di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
        if dati[39] >= 0:
            messaggio("Bomba appiccicosa x %i" % dati[39], grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 14) or usa == 9:
                messaggio("Bomba appiccicosa: dimezza la velocita' di", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
        if dati[40] >= 0:
            messaggio("Bomba potenziata x %i" % dati[40], grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
            if (xp == gsx // 32 * 1 and yp == gsy // 18 * 15) or usa == 10:
                messaggio("Bomba potenziata: infligge molti danni ai", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                messaggio("nemici su cui e' lanciata in un vasto raggio", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
        else:
            messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

        # vita-status personaggio
        pvtot = 100 + (dati[4] * 5)
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 3.5, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 4.5, 50)
        persmen = pygame.transform.scale(persgra, (gpx * 3, gpy * 3))
        schermo.blit(persmen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 3.5))
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 5.5) + (gpy // 8)))
        if dati[121]:
            avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
            schermo.blit(avvelenato, (gsx // 32 * 14, gsy // 18 * 5.5))
        if dati[123] > 0:
            attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
            schermo.blit(attaccopiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 5.5))
        if dati[124] > 0:
            difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
            schermo.blit(difesapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 5.5))
        # vita-status robo
        entot = 300 + (dati[9] * 100)
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 14, gsy // 18 * 8.5, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 9.5, 50)
        robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
        schermo.blit(robomen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 7.5))
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 10.5) + (gpy // 8)))
        if dati[122] > 0:
            surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
            schermo.blit(surriscaldato, (gsx // 32 * 14, gsy // 18 * 10.5))
        if dati[125] > 0:
            velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
            schermo.blit(velocitapiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 10.5))
        if dati[126] > 0:
            efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
            schermo.blit(efficienzapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 10.5))

        if attacco != 0:
            risposta = True

        messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
        schermo.blit(oggetto, (gsx // 32 * 20, gsy // 18 * 3))
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if usa != 0:
                        selind.play()
                        xp = gsx // 32 * 1
                        if usa == 1:
                            yp = gsy // 18 * 6
                        if usa == 2:
                            yp = gsy // 18 * 7
                        if usa == 3:
                            yp = gsy // 18 * 8
                        if usa == 4:
                            yp = gsy // 18 * 9
                        if usa == 5:
                            yp = gsy // 18 * 10
                        if usa == 6:
                            yp = gsy // 18 * 11
                        if usa == 7:
                            yp = gsy // 18 * 12
                        if usa == 8:
                            yp = gsy // 18 * 13
                        if usa == 9:
                            yp = gsy // 18 * 14
                        if usa == 10:
                            yp = gsy // 18 * 15
                        usa = 0
                    else:
                        selind.play()
                        risposta = True
                if event.key == pygame.K_s and xp != gsx // 32 * 10 and xp != gsx // 32 * 13:
                        if xp != gsx // 32 * 12 and xp != gsx // 32 * 15:
                            carim = True
                            if yp != gsy // 18 * 15:
                                spostapun.play()
                                oggetton = oggetton + 1
                                yp = yp + gsy // 18 * 1
                            elif yp == gsy // 18 * 15:
                                spostapun.play()
                                yp = gsy // 18 * 6
                                oggetton = 1
                if event.key == pygame.K_w and xp != gsx // 32 * 10 and xp != gsx // 32 * 13:
                        carim = True
                        if xp != gsx // 32 * 13:
                            if (yp != gsy // 18 * 6):
                                spostapun.play()
                                oggetton = oggetton - 1
                                yp = yp - gsy // 18 * 1
                            elif yp == gsy // 18 * 6:
                                spostapun.play()
                                yp = gsy // 18 * 15
                                oggetton = 10
                if event.key == pygame.K_a:
                    if xp == gsx // 32 * 13:
                        spostapun.play()
                        xp = xp - gsx // 32 * 3
                    elif xp == gsx // 32 * 10:
                        selimp.play()
                if event.key == pygame.K_d:
                    if xp == gsx // 32 * 10:
                        spostapun.play()
                        xp = xp + gsx // 32 * 3
                    elif xp == gsx // 32 * 13:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    carim = True
                    usadue = True

                    # usa?
                    if xp == gsx // 32 * 10 and yp == gsy // 18 * 14.5:
                        selezione.play()
                        xp = gsx // 32 * 1
                        # pozione
                        if usa == 1:
                            dati[5] = dati[5] + 100
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[31] = dati[31] - 1
                            yp = gsy // 18 * 6
                        # carica batt
                        if usa == 2:
                            dati[10] = dati[10] + 250
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[32] = dati[32] - 1
                            yp = gsy // 18 * 7
                        # bomba
                        if usa == 3:
                            attacco = 2
                            yp = gsy // 18 * 8
                        # antidoto
                        if usa == 4:
                            dati[121] = 0
                            dati[34] = dati[34] - 1
                            yp = gsy // 18 * 9
                        # bomba veleno
                        if usa == 5:
                            attacco = 3
                            yp = gsy // 18 * 10
                        # esca
                        if usa == 6:
                            attacco = 4
                            yp = gsy // 18 * 11
                        # super pozione
                        if usa == 7:
                            dati[5] = dati[5] + 300
                            if dati[5] > pvtot:
                                dati[5] = pvtot
                            dati[37] = dati[37] - 1
                            yp = gsy // 18 * 12
                        # carica migliorato
                        if usa == 8:
                            dati[10] = dati[10] + 600
                            if dati[10] > entot:
                                dati[10] = entot
                            dati[38] = dati[38] - 1
                            yp = gsy // 18 * 13
                        # bomba appiccicosa
                        if usa == 9:
                            attacco = 5
                            yp = gsy // 18 * 14
                        # bomba potenziata
                        if usa == 10:
                            attacco = 6
                            yp = gsy // 18 * 15
                        usa = 0
                        usadue = False
                    elif xp == gsx // 32 * 13 and yp == gsy // 18 * 14.5:
                        selind.play()
                        xp = gsx // 32 * 1
                        if usa == 1:
                            yp = gsy // 18 * 6
                        if usa == 2:
                            yp = gsy // 18 * 7
                        if usa == 3:
                            yp = gsy // 18 * 8
                        if usa == 4:
                            yp = gsy // 18 * 9
                        if usa == 5:
                            yp = gsy // 18 * 10
                        if usa == 6:
                            yp = gsy // 18 * 11
                        if usa == 7:
                            yp = gsy // 18 * 12
                        if usa == 8:
                            yp = gsy // 18 * 13
                        if usa == 9:
                            yp = gsy // 18 * 14
                        if usa == 10:
                            yp = gsy // 18 * 15
                        usa = 0
                        usadue = False

                    # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)
                    if usadue:
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 6:
                            if dati[31] > 0:
                                selezione.play()
                                usa = 1
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 7:
                            if dati[32] > 0:
                                selezione.play()
                                usa = 2
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 8:
                            if dati[33] > 0:
                                selezione.play()
                                usa = 3
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 9:
                            if dati[34] > 0:
                                selezione.play()
                                usa = 4
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 10:
                            if dati[35] > 0:
                                selezione.play()
                                usa = 5
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 11:
                            if dati[36] > 0:
                                selezione.play()
                                usa = 6
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 12:
                            if dati[37] > 0:
                                selezione.play()
                                usa = 7
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 13:
                            if dati[38] > 0:
                                selezione.play()
                                usa = 8
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 14:
                            if dati[39] > 0:
                                selezione.play()
                                usa = 9
                                usauno = True
                            else:
                                selimp.play()
                        if xp == gsx // 32 * 1 and yp == gsy // 18 * 15:
                            if dati[40] > 0:
                                selezione.play()
                                usa = 10
                                usauno = True
                            else:
                                selimp.play()

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 5, gsx // 32 * 9, gsy // 18 * 11))

            if carim:
                if dati[oggetton + 30] >= 0:
                    oggetto = pygame.image.load("Immagini\Oggetti\Oggetto%i.png" % oggetton)
                    oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
                else:
                    oggetto = pygame.image.load("Immagini\Oggetti\Sconosciuto.png")
                    oggetto = pygame.transform.scale(oggetto, (gpx * 10, gpy * 10))
                carim = False

            # pozione, carica batt, bomba, antidoto, bomba veleno, esca, super poz, carica migliorato, bomba pot, bomba atomica
            messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 1, 150)
            if dati[31] >= 0:
                messaggio("Pozione x %i" % dati[31], grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 6) or usa == 1:
                    messaggio("Pozione: recupera 100 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 40)
            if dati[32] >= 0:
                messaggio("Caricabatterie x %i" % dati[32], grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 7) or usa == 2:
                    messaggio("Caricabatterie: recupera 250 pe di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 40)
            if dati[33] >= 0:
                messaggio("Bomba x %i" % dati[33], grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 8) or usa == 3:
                    messaggio("Bomba: infligge un po' di danni ai nemici su", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                    messaggio("cui e' lanciata", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 40)
            if dati[34] >= 0:
                messaggio("Medicina x %i" % dati[34], grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 9) or usa == 4:
                    messaggio("Medicina: cura avvelenamento", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 40)
            if dati[35] >= 0:
                messaggio("Bomba velenosa x %i" % dati[35], grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 10) or usa == 5:
                    messaggio("Bomba velenosa: infligge avvelenamento a", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                    messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 40)
            if dati[36] >= 0:
                messaggio("Esca x %i" % dati[36], grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 11) or usa == 6:
                    messaggio("Esca: distrae i nemici vicini per un po'", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                    messaggio("di tempo. Viene utilizzata per fuggire", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
                    messaggio("(Colco uscira' dalla battaglia). E' possibile", grigiochi, gsx // 32 * 20, gsy // 18 * 15, 40)
                    messaggio("riprenderla passandoci sopra", grigiochi, gsx // 32 * 20, gsy // 18 * 16, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 11, 40)
            if dati[37] >= 0:
                messaggio("Super pozione x %i" % dati[37], grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 12) or usa == 7:
                    messaggio("Super pozione: recupera 300 pv", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 12, 40)
            if dati[38] >= 0:
                messaggio("Caricabatterie migliorato x %i" % dati[38], grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 13) or usa == 8:
                    messaggio("Caricabatterie migliorato: recupera 600 pe", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                    messaggio("di Colco", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 40)
            if dati[39] >= 0:
                messaggio("Bomba appiccicosa x %i" % dati[39], grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 14) or usa == 9:
                    messaggio("Bomba appiccicosa: dimezza la velocita' di", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                    messaggio("un nemico", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 40)
            if dati[40] >= 0:
                messaggio("Bomba potenziata x %i" % dati[40], grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)
                if (xp == gsx // 32 * 1 and yp == gsy // 18 * 15) or usa == 10:
                    messaggio("Bomba potenziata: infligge molti danni ai", grigiochi, gsx // 32 * 20, gsy // 18 * 13, 40)
                    messaggio("nemici su cui e' lanciata in un vasto raggio", grigiochi, gsx // 32 * 20, gsy // 18 * 14, 40)
            else:
                messaggio("???", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 40)

            # menu conferma
            if usa != 0:
                pygame.draw.rect(schermo, grigio, (gsx // 32 * 10, gsy // 18 * 12, gsx // 32 * 6.5, gsy // 18 * 4))
                puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 3 * 2, gpy // 3 * 2))
                # posizionare il cursore su menu usa
                if usauno:
                    xpv = xp
                    ypv = yp
                    xp = gsx // 32 * 13
                    yp = gsy // 18 * 14.5
                    usauno = False
                schermo.blit(puntatorevecchio, (xpv, ypv))
                messaggio("Usare?", grigiochi, gsx // 32 * 11, gsy // 18 * 12.5, 100)
                messaggio("Si", grigiochi, gsx // 32 * 11, gsy // 18 * 14.5, 60)
                messaggio("No", grigiochi, gsx // 32 * 14, gsy // 18 * 14.5, 60)
            else:
                puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 12 * 5, gpy // 12 * 5))

            # vita-status personaggio
            pvtot = 100 + (dati[4] * 5)
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 3.5, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 4.5, 50)
            persmen = pygame.transform.scale(persgra, (gpx * 3, gpy * 3))
            schermo.blit(persmen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 3.5))
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 5.5) + (gpy // 8)))
            if dati[121]:
                avvelenato = pygame.transform.scale(avvelenatoo, (gpx, gpy))
                schermo.blit(avvelenato, (gsx // 32 * 14, gsy // 18 * 5.5))
            if dati[123] > 0:
                attaccopiu = pygame.transform.scale(attaccopiuo, (gpx, gpy))
                schermo.blit(attaccopiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 5.5))
            if dati[124] > 0:
                difesapiu = pygame.transform.scale(difesapiuo, (gpx, gpy))
                schermo.blit(difesapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 5.5))
            # vita-status robo
            entot = 300 + (dati[9] * 100)
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 14, gsy // 18 * 8.5, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 9.5, 50)
            robomen = pygame.transform.scale(robograf, (gpx * 3, gpy * 3))
            schermo.blit(robomen, ((gsx // 32 * 10) + (gpx // 2), gsy // 18 * 7.5))
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 10.5) + (gpy // 8)))
            if dati[122] > 0:
                surriscaldato = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
                schermo.blit(surriscaldato, (gsx // 32 * 14, gsy // 18 * 10.5))
            if dati[125] > 0:
                velocitapiu = pygame.transform.scale(velocitapiuo, (gpx, gpy))
                schermo.blit(velocitapiu, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 10.5))
            if dati[126] > 0:
                efficienzapiu = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
                schermo.blit(efficienzapiu, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 10.5))

            if attacco != 0:
                risposta = True

            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(oggetto, (gsx // 32 * 20, gsy // 18 * 3))
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()
    return dati, attacco


def chiediconferma(conferma):
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx * 2, gpy * 2))
    xp = gsx // 32 * 18
    yp = gsy // 18 * 10
    schermo.fill(grigioscu)
    if conferma == 1:
        messaggio("Tornare al menu' principale?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
    elif conferma == 2:
        messaggio("Tornare a Windows?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
    messaggio("Si", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 120)
    messaggio("No", grigiochi, gsx // 32 * 21, gsy // 18 * 10, 120)
    messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
    schermo.blit(puntatore, (xp, yp))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    selind.play()
                    return False, False
                if event.key == pygame.K_a:
                    if xp == gsx // 32 * 18:
                        spostapun.play()
                        xp = gsx // 32 * 6
                    elif xp == gsx // 32 * 6:
                        selimp.play()
                if event.key == pygame.K_d:
                    if xp == gsx // 32 * 6:
                        spostapun.play()
                        xp = gsx // 32 * 18
                    elif xp == gsx // 32 * 18:
                        selimp.play()
                if event.key == pygame.K_SPACE:
                    if xp == gsx // 32 * 6:
                        selezione.play()
                        if conferma == 1:
                            return True, True
                        elif conferma == 2:
                            pygame.quit()
                            quit()
                    elif xp == gsx // 32 * 18:
                        selind.play()
                        return False, False
            schermo.fill(grigioscu)
            if conferma == 1:
                messaggio("Tornare al menu' principale?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
            elif conferma == 2:
                messaggio("Tornare a Windows?", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 120)
            messaggio("Si", grigiochi, gsx // 32 * 9, gsy // 18 * 10, 120)
            messaggio("No", grigiochi, gsx // 32 * 21, gsy // 18 * 10, 120)
            messaggio("Q: torna indietro", grigiochi, gsx // 32 * 25, gsy // 18 * 1, 50)
            schermo.blit(puntatore, (xp, yp))
            pygame.display.update()


def start(dati, nmost, porteini, portefin, cofaniini, cofanifin, porte, cofanetti, apriocchio):
    # canzone
    c16 = pygame.mixer.Sound("Audio\Canzoni\Canzone16.wav")
    c16.play(-1)
    sfondostastart = pygame.transform.scale(sfondostax3, (gpx * 4, gpy))
    perssta = pygame.transform.scale(persgra, (gpx * 10, gpy * 10))
    robosta = pygame.transform.scale(robograf, (gpx * 10, gpy * 10))
    puntatore = pygame.transform.scale(puntatoreorigi, (gpx // 2, gpy // 2))
    avvelenatosta = pygame.transform.scale(avvelenatoo, (gpx, gpy))
    surriscaldatosta = pygame.transform.scale(surriscaldatoo, (gpx, gpy))
    attaccopiusta = pygame.transform.scale(attaccopiuo, (gpx, gpy))
    difesapiusta = pygame.transform.scale(difesapiuo, (gpx, gpy))
    velocitapiusta = pygame.transform.scale(velocitapiuo, (gpx, gpy))
    efficienzapiusta = pygame.transform.scale(efficienzapiuo, (gpx, gpy))
    xp = gsx // 32 * 1
    yp = gsy // 18 * 5
    carim = True
    risposta = False
    attacco = 0
    conferma = 0

    # esperienza totale per livello
    esptot = pow(dati[4], 2) + (dati[4] * 10)

    # primo frame
    if True:
        schermo.fill(grigioscu)
        # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
        pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))
        messaggio("Menu' start", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 150)
        messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 50)
        if not apriocchio:
            messaggio("Tecniche", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
        else:
            messaggio("Tecniche", grigioscu, gsx // 32 * 2, gsy // 18 * 6, 50)
        messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 50)
        messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 50)
        messaggio("Mappa", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 50)
        messaggio("Diario", grigiochi, gsx // 32 * 2, gsy // 18 * 10, 50)
        if nmost == -1:
            messaggio("Salva", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 50)
        else:
            messaggio("Salva", grigioscu, gsx // 32 * 2, gsy // 18 * 13, 50)
        messaggio("Torna al menu' principale", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 50)
        messaggio("Torna a Windows", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 50)
        messaggio("Esc / Q: torna al gioco", grigiochi, gsx // 32 * 23, gsy // 18 * 1, 50)
        if carim:
            if dati[10] <= 0:
                robosta = robograff
                robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
            else:
                robosta = robograf
                robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
            carim = False
        # vita-status personaggio
        pvtot = 100 + (dati[4] * 5)
        if dati[5] < 0:
            dati[5] = 0
        messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 13, 50)
        messaggio("Lv:  " + str(dati[4]), grigiochi, gsx // 32 * 14, gsy // 18 * 14, 50)
        if dati[4] < 100:
            messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), grigiochi, (gsx // 32 * 16) + (gpx // 2),
                      gsy // 18 * 14, 50)
        else:
            messaggio("Esp:  -- / --", grigiochi, (gsx // 32 * 16) + (gpx // 2), gsy // 18 * 14, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 15, 50)
        schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 16) + (gpy // 8)))
        if dati[121]:
            schermo.blit(avvelenatosta, (gsx // 32 * 14, gsy // 18 * 16))
        if dati[123] > 0:
            schermo.blit(attaccopiusta, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 16))
        if dati[124] > 0:
            schermo.blit(difesapiusta, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 16))
        # vita-status robo
        entot = 300 + (dati[9] * 100)
        if dati[10] < 0:
            dati[10] = 0
        messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 23, gsy // 18 * 13, 50)
        messaggio("Status alterativi: ", grigiochi, gsx // 32 * 23, gsy // 18 * 14, 50)
        schermo.blit(sfondostastart, (gsx // 32 * 23, (gsy // 18 * 15) + (gpy // 8)))
        if dati[122] > 0:
            schermo.blit(surriscaldatosta, (gsx // 32 * 23, gsy // 18 * 15))
        if dati[125] > 0:
            schermo.blit(velocitapiusta, ((gsx // 32 * 23) + (2 * gpx // 4 * 3), gsy // 18 * 15))
        if dati[126] > 0:
            schermo.blit(efficienzapiusta, ((gsx // 32 * 23) + (4 * gpx // 4 * 3), gsy // 18 * 15))
        schermo.blit(perssta, (gsx // 32 * 12, gsy // 18 * 2))
        schermo.blit(robosta, (gsx // 32 * 21, gsy // 18 * 2))
        schermo.blit(puntatore, (xp, yp))
        pygame.display.update()

    while not risposta:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    selind.play()
                    inizio = False
                    risposta = True
                if event.key == pygame.K_s:
                    if (yp != gsy // 18 * 9) and (yp != gsy // 18 * 15):
                        spostapun.play()
                        yp = yp + gsy // 18 * 1
                    else:
                        if yp == gsy // 18 * 9:
                            spostapun.play()
                            yp = yp + gsy // 18 * 4
                        else:
                            if yp == gsy // 18 * 15:
                                spostapun.play()
                                yp = gsy // 18 * 5
                if event.key == pygame.K_w:
                    if (yp != gsy // 18 * 13) and (yp != gsy // 18 * 5):
                        spostapun.play()
                        yp = yp - gsy // 18 * 1
                    else:
                        if yp == gsy // 18 * 13:
                            spostapun.play()
                            yp = yp - gsy // 18 * 4
                        else:
                            if yp == gsy // 18 * 5:
                                spostapun.play()
                                yp = gsy // 18 * 15
                if event.key == pygame.K_SPACE:
                    if (yp == gsy // 18 * 13 and nmost > -1) or (yp == gsy // 18 * 6 and apriocchio):
                        selimp.play()
                    else:
                        selezione.play()
                    inizio = False
                    # oggetti
                    if yp == gsy // 18 * 5:
                        dati, attacco = oggetti(dati)
                        carim = True
                    # tecniche
                    """if yp == gsy // 18 * 6:
                        #if not apriocchio:
                        dati, attacco = tecniche(dati)
                        carim = True"""
                    # equip pers
                    if yp == gsy // 18 * 6:
                        dati = equip(dati)
                        carim = True
                    # equip robot
                    if yp == gsy // 18 * 7:
                        dati = equiprobo(dati)
                        carim = True
                    # mappa
                    if yp == gsy // 18 * 8:
                        print ("mappa")
                    # diario
                    if yp == gsy // 18 * 9:
                        print ("diario")
                    # salva
                    if yp == gsy // 18 * 13:
                        #if nmost == -1:
                        n = scegli_sal(3, len(dati))
                        if n != -1:
                            salvataggio(n, dati, porteini, portefin, cofaniini, cofanifin, porte, cofanetti)
                    # menu
                    if yp == gsy // 18 * 14:
                        conferma = 1
                    # chiudi
                    if yp == gsy // 18 * 15:
                        conferma = 2

            # chiedere conferma per uscire
            if conferma != 0:
                inizio, risposta = chiediconferma(conferma)
                conferma = 0

            schermo.fill(grigioscu)
            # rettangolo(dove,colore,posizione-larghezza/altezza,spessore)
            pygame.draw.rect(schermo, grigio, (gsx // 32 * 1, gsy // 18 * 4, gsx // 32 * 10, gsy // 18 * 12.5))
            messaggio("Menu' start", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 150)
            messaggio("Oggetti", grigiochi, gsx // 32 * 2, gsy // 18 * 5, 50)
            """if not apriocchio:
                messaggio("Tecniche", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
            else:
                messaggio("Tecniche", grigioscu, gsx // 32 * 2, gsy // 18 * 6, 50)"""
            messaggio("Equipaggiamento", grigiochi, gsx // 32 * 2, gsy // 18 * 6, 50)
            messaggio("Setta Colco", grigiochi, gsx // 32 * 2, gsy // 18 * 7, 50)
            messaggio("Mappa", grigiochi, gsx // 32 * 2, gsy // 18 * 8, 50)
            messaggio("Diario", grigiochi, gsx // 32 * 2, gsy // 18 * 9, 50)
            if nmost == -1:
                messaggio("Salva", grigiochi, gsx // 32 * 2, gsy // 18 * 13, 50)
            else:
                messaggio("Salva", grigioscu, gsx // 32 * 2, gsy // 18 * 13, 50)
            messaggio("Torna al menu' principale", grigiochi, gsx // 32 * 2, gsy // 18 * 14, 50)
            messaggio("Torna a Windows", grigiochi, gsx // 32 * 2, gsy // 18 * 15, 50)
            messaggio("Esc / Q: torna al gioco", grigiochi, gsx // 32 * 23, gsy // 18 * 1, 50)
            if carim:
                if dati[10] <= 0:
                    robosta = robograff
                    robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
                else:
                    robosta = robograf
                    robosta = pygame.transform.scale(robosta, (gpx * 10, gpy * 10))
                carim = False

            # vita-status personaggio
            pvtot = 100 + (dati[4] * 5)
            if dati[5] < 0:
                dati[5] = 0
            messaggio("Pv:  " + str(dati[5]) + " / " + str(pvtot), grigiochi, gsx // 32 * 14, gsy // 18 * 13, 50)
            messaggio("Lv:  " + str(dati[4]), grigiochi, gsx // 32 * 14, gsy // 18 * 14, 50)
            if dati[4] < 100:
                messaggio("Esp:  " + str(dati[127]) + " / " + str(esptot), grigiochi, (gsx // 32 * 16) + (gpx // 2), gsy // 18 * 14, 50)
            else:
                messaggio("Esp:  -- / --", grigiochi, (gsx // 32 * 16) + (gpx // 2), gsy // 18 * 14, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 14, gsy // 18 * 15, 50)
            schermo.blit(sfondostastart, (gsx // 32 * 14, (gsy // 18 * 16) + (gpy // 8)))
            if dati[121]:
                schermo.blit(avvelenatosta, (gsx // 32 * 14, gsy // 18 * 16))
            if dati[123] > 0:
                schermo.blit(attaccopiusta, ((gsx // 32 * 14) + (2 * gpx // 4 * 3), gsy // 18 * 16))
            if dati[124] > 0:
                schermo.blit(difesapiusta, ((gsx // 32 * 14) + (4 * gpx // 4 * 3), gsy // 18 * 16))
            # vita-status robo
            entot = 300 + (dati[9] * 100)
            if dati[10] < 0:
                dati[10] = 0
            messaggio("Pe:  " + str(dati[10]) + " / " + str(entot), grigiochi, gsx // 32 * 23, gsy // 18 * 13, 50)
            messaggio("Status alterativi: ", grigiochi, gsx // 32 * 23, gsy // 18 * 14, 50)
            schermo.blit(sfondostastart, (gsx // 32 * 23, (gsy // 18 * 15) + (gpy // 8)))
            if dati[122] > 0:
                schermo.blit(surriscaldatosta, (gsx // 32 * 23, gsy // 18 * 15))
            if dati[125] > 0:
                schermo.blit(velocitapiusta, ((gsx // 32 * 23) + (2 * gpx // 4 * 3), gsy // 18 * 15))
            if dati[126] > 0:
                schermo.blit(efficienzapiusta, ((gsx // 32 * 23) + (4 * gpx // 4 * 3), gsy // 18 * 15))

            if attacco != 0:
                risposta = True

            schermo.blit(perssta, (gsx // 32 * 12, gsy // 18 * 2))
            schermo.blit(robosta, (gsx // 32 * 21, gsy // 18 * 2))
            schermo.blit(puntatore, (xp, yp))
            if not risposta:
                pygame.display.update()
            else:
                schermo.fill(grigioscu)
    c16.stop()
    return dati, inizio, attacco


def oggetto(x, y, dimx, dimy, px, py, nx, ny):
    a = x
    b = y
    dimx = dimx + x
    dimy = dimy + y
    while x < dimx:
        if (ny == -gpy and py == dimy and px == x) or (ny == gpy and py == y - gpy and px == x):
            return True
        x = x + gpx
    x = a
    y = b
    while y < dimy:
        if (nx == -gpx and px == dimx and py == y) or (nx == gpx and px == x - gpx and py == y):
            return True
        y = y + gpy


def muri_porte(x, y, nx, ny, stanza, carim, muovi, mostro, robo, porte, cofanetti):
    cambiosta = False
    # prima stanza
    if (stanza == 1) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -gpy and x == gsx // 32 * 6 and y == gsy // 18 * 2 and not mostro and not robo:
            stanza = 2
            cambiosta = True
            carim = True
        else:
            # bordi stanza
            if nx == -gpx and x <= gpx * 2:
                nx = 0
            if nx == gpx and x >= gsx - (gpx * 3):
                nx = 0
            if ny == -gpy and y <= gpy * 2:
                ny = 0
            if ny == gpy and y >= gsy - (gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y    dim x    dim y    px py nx  ny
        if oggetto(gsx // 32 * 7, gsy // 18 * 11, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 18, gsy // 18 * 7, gpx * 2, gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 21, gsy // 18 * 11, gpx * 4, gpy * 4, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4
    # seconda stanza
    if (stanza == 2) and ((nx != 0) or (ny != 0)) and not cambiosta:
        # porte
        if ny == -gpy and x == gsx // 32 * 6 and y == gsy // 18 * 2 and not mostro and not robo:
            stanza = 1
            cambiosta = True
            carim = True
        else:
            # bordi stanza
            if nx == -gpx and x <= gpx * 2:
                nx = 0
            if nx == gpx and x >= gsx - (gpx * 3):
                nx = 0
            if ny == -gpy and y <= gpy * 2:
                ny = 0
            if ny == gpy and y >= gsy - (gpy * 3):
                ny = 0
        # controllo muri-oggetti
        #          posizione x    posizione y    dim x    dim y    px py nx  ny
        if oggetto(gsx // 32 * 9, gsy // 18 * 2, gpx * 1, gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 2, gsy // 18 * 7, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 4, gsy // 18 * 7, gpx * 12, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 2, gsy // 18 * 11, gpx * 6, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 7, gsy // 18 * 13, gpx * 5, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 9, gsy // 18 * 13, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 11, gsy // 18 * 11, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 13, gsy // 18 * 11, gpx * 3, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 10, gpx * 1, gpy * 2, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 4, gpx * 1, gpy * 5, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 2, gpx * 1, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 15, gsy // 18 * 6, gpx * 9, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 4, gpx * 4, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 6, gpx * 1, gpy * 6, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 23, gsy // 18 * 13, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 26, gsy // 18 * 4, gpx * 1, gpy * 3, x, y, nx, ny):
            nx = 0
            ny = 0
        if oggetto(gsx // 32 * 26, gsy // 18 * 6, gpx * 4, gpy * 1, x, y, nx, ny):
            nx = 0
            ny = 0
        # controllo se le porte sono chiuse o aperte
        i = 0
        while i < len(porte):
            if not porte[i + 3]:
                if oggetto(porte[i + 1], porte[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                    nx = 0
                    ny = 0
            i = i + 4
        # controllo cofanetti
        i = 0
        while i < len(cofanetti):
            if oggetto(cofanetti[i + 1], cofanetti[i + 2], gpx * 1, gpy * 1, x, y, nx, ny):
                nx = 0
                ny = 0
            i = i + 4

    # movimento mostri veloci
    if (mostro or robo) and muovi > 0:
        muovi = muovi - 1
    # movimento mostri lenti
    if (mostro or robo) and muovi < 0:
        muovi = muovi + 1

    # movimento personaggio
    x = x + nx
    y = y + ny

    return x, y, stanza, carim, muovi, cambiosta


def ambiente_movimento(x, y, npers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp, vx, vy, rx, ry, vrx, vry, pers,
                       stanzaa, sfondinoa, sfondinob, sfondinoc, arma, armatura, scudo, robot, armrob, nemicoa, mxa, mya, mxav, myav, nemicob, mxb, myb, mxbv, mybv,
                       nemicoc, mxc, myc, mxcv, mycv, nemicod, mxd, myd, mxdv, mydv, nemicoe, mxe, mye, mxev, myev, nemicof, mxf, myf, mxfv, myfv,
                       nemicog, mxg, myg, mxgv, mygv, nemicoh, mxh, myh, mxhv, myhv, nemicoi, mxi, myi, mxiv, myiv, nemicol, mxl, myl, mxlv, mylv,
                       mortoa, mortob, mortoc, mortod, mortoe, mortof, mortog, mortoh, mortoi, mortol, caricaini, vitaesca, porte, cofanetti, caseviste, apriocchio):
    # sfondo
    if caricaini:
        schermo.blit(stanzaa, (0, 0))
        # cofanetti
        i = 0
        while i < len(cofanetti):
            j = 0
            while j < len(caseviste):
                if ((caseviste[j] == cofanetti[i + 1] - gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + gpy)) and caseviste[j + 2]:
                    schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                    if cofanetti[i + 3]:
                        schermo.blit(cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                    else:
                        schermo.blit(cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                j = j + 3
            i = i + 4
        i = 0
        # disegno le caselle viste
        while i < len(caseviste):
            if caseviste[i + 2]:
                n = 0
                while n < 32:
                    if caseviste[i] == gpx * n:
                        m = 0
                        while m < 18:
                            if caseviste[i + 1] == gpy * m:
                                if (n + m) % 2 == 0:
                                    schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                                if (n + m) % 2 != 0:
                                    schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                            m = m + 1
                    n = n + 1
            i = i + 3

    else:
        n = 0
        while n < 32:
            if vx == gpx * n:
                m = 0
                while m < 18:
                    if vy == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (vx, vy))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (vx, vy))
                    m = m + 1
            n = n + 1
        n = 0
        while n < 32:
            if vrx == gpx * n:
                m = 0
                while m < 18:
                    if vry == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (vrx, vry))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (vrx, vry))
                    m = m + 1
            n = n + 1

    # disegnare casella sopra la vecchia posizione dei mostri
    j = 0
    while j < len(caseviste):
        if nemicoa != 0 and caseviste[j] == mxa and caseviste[j + 1] == mya and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxav == gpx * n:
                    m = 0
                    while m < 18:
                        if myav == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxav, myav))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxav, myav))
                        m = m + 1
                n = n + 1
        if nemicob != 0 and caseviste[j] == mxb and caseviste[j + 1] == myb and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxbv == gpx * n:
                    m = 0
                    while m < 18:
                        if mybv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxbv, mybv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxbv, mybv))
                        m = m + 1
                n = n + 1
        if nemicoc != 0 and caseviste[j] == mxc and caseviste[j + 1] == myc and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxcv == gpx * n:
                    m = 0
                    while m < 18:
                        if mycv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxcv, mycv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxcv, mycv))
                        m = m + 1
                n = n + 1
        if nemicod != 0 and caseviste[j] == mxd and caseviste[j + 1] == myd and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxdv == gpx * n:
                    m = 0
                    while m < 18:
                        if mydv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxdv, mydv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxdv, mydv))
                        m = m + 1
                n = n + 1
        if nemicoe != 0 and caseviste[j] == mxe and caseviste[j + 1] == mye and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxev == gpx * n:
                    m = 0
                    while m < 18:
                        if myev == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxev, myev))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxev, myev))
                        m = m + 1
                n = n + 1
        if nemicof != 0 and caseviste[j] == mxf and caseviste[j + 1] == myf and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxfv == gpx * n:
                    m = 0
                    while m < 18:
                        if myfv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxfv, myfv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxfv, myfv))
                        m = m + 1
                n = n + 1
        if nemicog != 0 and caseviste[j] == mxg and caseviste[j + 1] == myg and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxgv == gpx * n:
                    m = 0
                    while m < 18:
                        if mygv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxgv, mygv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxgv, mygv))
                        m = m + 1
                n = n + 1
        if nemicoh != 0 and caseviste[j] == mxh and caseviste[j + 1] == myh and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxhv == gpx * n:
                    m = 0
                    while m < 18:
                        if myhv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxhv, myhv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxhv, myhv))
                        m = m + 1
                n = n + 1
        if nemicoi != 0 and caseviste[j] == mxi and caseviste[j + 1] == myi and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxiv == gpx * n:
                    m = 0
                    while m < 18:
                        if myiv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxiv, myiv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxiv, myiv))
                        m = m + 1
                n = n + 1
        if nemicol != 0 and caseviste[j] == mxl and caseviste[j + 1] == myl and caseviste[j + 2]:
            n = 0
            while n < 32:
                if mxlv == gpx * n:
                    m = 0
                    while m < 18:
                        if mylv == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (mxlv, mylv))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (mxlv, mylv))
                        m = m + 1
                n = n + 1
        j = j + 3

    if apriocchio:
        schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
    else:
        schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))

    # esche: id, vita, xesca, yesca
    i = 0
    while i < len(vitaesca):
        schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
        i = i + 4

    # robo
    schermo.blit(robot, (rx, ry))
    schermo.blit(armrob, (rx, ry))

    # personaggio
    if npers == 1:
        schermo.blit(scudo, (x, y))
        schermo.blit(pers, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(persdb, (x, y))
        schermo.blit(arma, (x, y))
    if npers == 2:
        schermo.blit(arma, (x, y))
        schermo.blit(pers, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(persab, (x, y))
        schermo.blit(scudo, (x, y))
    if npers == 3:
        schermo.blit(arma, (x, y))
        schermo.blit(scudo, (x, y))
        schermo.blit(pers, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(perswb, (x, y))
    if npers == 4:
        schermo.blit(pers, (x, y))
        schermo.blit(armatura, (x, y))
        schermo.blit(perssb, (x, y))
        schermo.blit(arma, (x, y))
        schermo.blit(scudo, (x, y))

    # vita-status personaggio
    lungvitatot = (gpx // 4) * (pvtot // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
    vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
    schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 16))
    persbat = pygame.transform.scale(perso, (gpx, gpy))
    schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 16))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if attp > 0:
        schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
    if difp > 0:
        schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

    # vita-status robo
    lungentot = (gpx // 4) * (entot // 10)
    lungen = (lungentot * enrob) // entot
    if lungen < 0:
        lungen = 0
    indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
    vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
    schermo.blit(indvitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(vitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 17))
    robobat = pygame.transform.scale(roboo, (gpx, gpy))
    schermo.blit(robobat, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if surrisc > 0:
        schermo.blit(surriscaldato, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if velp > 0:
        schermo.blit(velocitapiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
    if effp > 0:
        schermo.blit(efficienzapiu, ((gsx // 32 * 1) + (gpx // 4 * 3) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))

    # disegnare i mostri
    j = 0
    while j < len(caseviste):
        if nemicoa != 0 and caseviste[j] == mxa and caseviste[j + 1] == mya and caseviste[j + 2]:
            schermo.blit(nemicoa, (mxa, mya))
        if nemicob != 0 and caseviste[j] == mxb and caseviste[j + 1] == myb and caseviste[j + 2]:
            schermo.blit(nemicob, (mxb, myb))
        if nemicoc != 0 and caseviste[j] == mxc and caseviste[j + 1] == myc and caseviste[j + 2]:
            schermo.blit(nemicoc, (mxc, myc))
        if nemicod != 0 and caseviste[j] == mxd and caseviste[j + 1] == myd and caseviste[j + 2]:
            schermo.blit(nemicod, (mxd, myd))
        if nemicoe != 0 and caseviste[j] == mxe and caseviste[j + 1] == mye and caseviste[j + 2]:
            schermo.blit(nemicoe, (mxe, mye))
        if nemicof != 0 and caseviste[j] == mxf and caseviste[j + 1] == myf and caseviste[j + 2]:
            schermo.blit(nemicof, (mxf, myf))
        if nemicog != 0 and caseviste[j] == mxg and caseviste[j + 1] == myg and caseviste[j + 2]:
            schermo.blit(nemicog, (mxg, myg))
        if nemicoh != 0 and caseviste[j] == mxh and caseviste[j + 1] == myh and caseviste[j + 2]:
            schermo.blit(nemicoh, (mxh, myh))
        if nemicoi != 0 and caseviste[j] == mxi and caseviste[j + 1] == myi and caseviste[j + 2]:
            schermo.blit(nemicoi, (mxi, myi))
        if nemicol != 0 and caseviste[j] == mxl and caseviste[j + 1] == myl and caseviste[j + 2]:
            schermo.blit(nemicol, (mxl, myl))
        j = j + 3


def movmostro(x, y, rx, ry, mx, my, stanza, tipo, muovimost, visto, dif, difro, par, dati, statom, vitaesca, porte, cofanetti):
    sposta = False
    mostro = True
    attrobo = False
    nmos = 0
    nmx = 0
    nmy = 0
    vistoesca = False
    escabersaglio = 0

    # burocrazia
    carim = False

    if visto:
        visto = False

    # caratteristiche nemici
    if tipo == "mostro":
        attlontano = True
        vistam = gpx * 5
        att = 10
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = -2
            else:
                muovimost = 0
    if tipo == "pipistrello":
        attlontano = False
        vistam = gpx * 6
        att = 5
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = 0
            else:
                muovimost = 2
    if tipo == "orco":
        attlontano = False
        vistam = gpx * 5
        att = 15
        if muovimost == 0:
            if statom == 2 or statom == 3:
                muovimost = -3
            else:
                muovimost = -2
    if tipo == 0:
        attlontano = False
        vistam = 0
        att = 0

    # movimenti verso esche o casuali
    primaesca = True
    i = 0
    while i < len(vitaesca):
        if abs(vitaesca[i + 2] - mx) <= vistam and abs(vitaesca[i + 3] - my) <= vistam:
            if primaesca:
                distminx = vitaesca[i + 2]
                distminy = vitaesca[i + 3]
                escabersaglio = i
                vistoesca = True
                primaesca = False
            if not primaesca and (abs(vitaesca[i + 2] - mx) + abs(vitaesca[i + 3] - my) < abs(distminx - mx) + abs(distminy - my)):
                distminx = vitaesca[i + 2]
                distminy = vitaesca[i + 3]
                escabersaglio = i
            # controllo caselle che si vedono
            caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == distminx and caseattactot[j + 1] == distminy and not caseattactot[j + 2]:
                    distminx = 0
                    distminy = 0
                    escabersaglio = 0
                    vistoesca = False
                    primaesca = True
                j = j + 3
        i = i + 4
    vistoprov1 = False
    vistoprov2 = False
    if not visto and not vistoesca:
        # controllo caselle che si vedono per pers e robo
        caseattactot = trovacasattaccabili(mx, my, stanza, porte, cofanetti)
        if abs(x - mx) <= vistam and abs(y - my) <= vistam and dati[5] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == x and caseattactot[j + 1] == y:
                    if not caseattactot[j + 2]:
                        vistoprov1 = False
                    else:
                        vistoprov1 = True
                    break
                j = j + 3
        if abs(rx - mx) <= vistam and abs(ry - my) <= vistam and dati[10] > 0:
            j = 0
            while j < len(caseattactot):
                if caseattactot[j] == rx and caseattactot[j + 1] == ry:
                    if not caseattactot[j + 2]:
                        vistoprov2 = False
                    else:
                        vistoprov2 = True
                    break
                j = j + 3
            if dati[10] <= 0:
                vistoprov2 = False
        if vistoprov1 or vistoprov2:
            visto = True
        if not visto:
            nmos = random.randint(1, 4)
            sposta = True

    if (visto or vistoesca) and muovimost >= -1:
        if ((abs(rx - mx) + abs(ry - my)) < (abs(x - mx) + abs(y - my)) or not vistoprov1) and vistoprov2 and dati[10] > 0 and not vistoesca:
            x = rx
            y = ry
            attrobo = True
        if vistoesca:
            x = vitaesca[escabersaglio + 2]
            y = vitaesca[escabersaglio + 3]

        # nemici che attaccano da vicino
        if not attlontano:
            if abs(x - mx) > abs(y - my):
                if mx < x:
                    nmos = 1
                if mx > x:
                    nmos = 2
                sposta = True
            if abs(y - my) > abs(x - mx):
                if my < y:
                    nmos = 3
                if my > y:
                    nmos = 4
                sposta = True
            if (abs(x - mx) == abs(y - my)) and (x != mx) and (y != my):
                c = random.randint(1, 2)
                if mx < x and c == 1:
                    nmos = 1
                if mx > x and c == 1:
                    nmos = 2
                if my < y and c == 2:
                    nmos = 3
                if my > y and c == 2:
                    nmos = 4
                sposta = True
            if (x == mx + gpx and y == my) or (x == mx - gpx and y == my) or (x == mx and y == my + gpy) or (x == mx and y == my - gpy) or ((x == mx) and (y == my)):
                if vistoesca:
                    danno = att
                    if danno < 0:
                        danno = 0
                    print ("attacco vicino", tipo, "a esca", danno)
                    vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
                else:
                    if attrobo:
                        danno = att - difro
                        if danno < 0:
                            danno = 0
                        print ("attacco vicino", tipo, "a robo", danno)
                        dati[10] = dati[10] - danno
                    else:
                        danno = att - dif
                        if danno < 0:
                            danno = 0
                        if random.randint(1, 100) <= par and dati[7] > 0:
                            danno = 0
                            print ("parato:", par)
                        print ("attacco vicino", tipo, "a rallo", danno)
                        dati[5] = dati[5] - danno
                nmos = 0
                if x == mx + gpx and y == my:
                    nmos = 1
                if x == mx - gpx and y == my:
                    nmos = 2
                if x == mx and y == my + gpy:
                    nmos = 3
                if x == mx and y == my - gpy:
                    nmos = 4
                sposta = False

        # nemici che attaccano da lontano
        if attlontano:
            if vistoesca:
                danno = att
                if danno < 0:
                    danno = 0
                print ("attacco lontano", tipo, "a esca", danno)
                vitaesca[escabersaglio + 1] = vitaesca[escabersaglio + 1] - danno
            else:
                if attrobo:
                    danno = att - difro
                    if danno < 0:
                        danno = 0
                    print ("attacco lontano", tipo, "a robo", danno)
                    dati[10] = dati[10] - danno
                else:
                    danno = att - dif
                    if danno < 0:
                        danno = 0
                    if random.randint(1, 100) <= par and dati[7] > 0:
                        danno = 0
                        print ("parato:", par)
                    print ("attacco lontano", tipo, "a rallo", danno)
                    dati[5] = dati[5] - danno
            nmos = 0
            if abs(x - mx) > abs(y - my):
                if mx < x:
                    nmos = 1
                if mx > x:
                    nmos = 2
            if abs(y - my) > abs(x - mx):
                if my < y:
                    nmos = 3
                if my > y:
                    nmos = 4
            sposta = False

    # spostamento
    if sposta:
        if nmos == 1:
            if mx + gpx == x and my == y:
                nmx = 0
                nmy = 0
            else:
                nmx = gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if mx + gpx == vitaesca[i] and my == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 2:
            if mx - gpx == x and my == y:
                nmx = 0
                nmy = 0
            else:
                nmx = -gpx
                nmy = 0
            i = 2
            while i <= len(vitaesca):
                if mx - gpx == vitaesca[i] and my == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 3:
            if mx == x and my + gpy == y:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = gpy
            i = 2
            while i <= len(vitaesca):
                if mx == vitaesca[i] and my + gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4
        if nmos == 4:
            if mx == x and my - gpy == y:
                nmx = 0
                nmy = 0
            else:
                nmx = 0
                nmy = -gpy
            i = 2
            while i <= len(vitaesca):
                if mx == vitaesca[i] and my - gpy == vitaesca[i + 1]:
                    nmx = 0
                    nmy = 0
                i = i + 4

    if muovimost < -1:
        nmos = 0

    # alcuni sono inutili!!!
    mx, my, stanza, carim, muovimost, cambiosta = muri_porte(mx, my, nmx, nmy, stanza, carim, muovimost, mostro, False, porte, cofanetti)
    return mx, my, muovimost, nmos, visto, dati, vitaesca, vistam


def movrobo(x, y, vx, vy, rx, ry, stanza, muovirob, vistorob, dati, porte, cofanetti):
    robo = True
    nrx = 0
    nry = 0

    # burocrazia
    carim = False

    nrob = 0
    sposta = False
    # movimento robot
    # no mostri
    if not vistorob:
        if abs(x - rx) > abs(y - ry):
            if rx < x:
                nrob = 1
            if rx > x:
                nrob = 2
            sposta = True
        if abs(y - ry) > abs(x - rx):
            if ry < y:
                nrob = 3
            if ry > y:
                nrob = 4
            sposta = True
        if (abs(x - rx) == abs(y - ry)) and (x != rx) and (y != ry):
            if abs(x - rx) == gpx:
                if vx == rx + gpx:
                    nrob = 1
                if vx == rx - gpx:
                    nrob = 2
                if vy == ry + gpy:
                    nrob = 3
                if vy == ry - gpy:
                    nrob = 4
            else:
                c = random.randint(1, 2)
                if rx < x and c == 1:
                    nrob = 1
                if rx > x and c == 1:
                    nrob = 2
                if ry < y and c == 2:
                    nrob = 3
                if ry > y and c == 2:
                    nrob = 4
            sposta = True
    # mostri si (gambit)
    elif vistorob and muovirob >= -1:
        # progresso-stanza-x-y-liv-pv-arma-scudo-armatura-armrob-energiarob-tecniche(20)-oggetti(50)-condizioni(20)-gambit(20) // dimensione: 0-120
        esecuzione = False
        condizione = False
        azione = False
        print ("gambit")

    # spostamento
    if sposta:
        if nrob == 1:
            if rx + gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = gpx
                nry = 0
        if nrob == 2:
            if rx - gpx == x and ry == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = -gpx
                nry = 0
        if nrob == 3:
            if rx == x and ry + gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = gpy
        if nrob == 4:
            if rx == x and ry - gpy == y:
                nrx = 0
                nry = 0
                nrob = 0
            else:
                nrx = 0
                nry = -gpy

    # alcuni sono inutili!!!
    rx, ry, stanza, carim, muovirob, cambiosta = muri_porte(rx, ry, nrx, nry, stanza, carim, muovirob, False, robo, porte, cofanetti)
    return rx, ry, muovirob, nrob, vistorob, dati


def trovacasattaccabili(x, y, stanza, porte, cofanetti):
    range = 6
    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in basso a destra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * n)
            mury = y + (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * m)
            mury = y + (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    #  caseattacbassodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a destra
    caseattacbassodestra = []
    # riempio caseattacbassodestra come se tutto il campo in basso a destra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacbassodestra.append(x + (gpx * n))
            caseattacbassodestra.append(y + (gpy * m))
            caseattacbassodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 13:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a basso-destra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 6:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 27:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 13:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 34:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 27:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 20:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 34:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 27:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 34:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 41:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 48:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b basso-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 7:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 14:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 21:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 28:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 28:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 35:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 35:
                        caseattacbassodestra[j + 2] = False
                    if posizione == 42:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 42:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b basso-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 15:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 22:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 29:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 36:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 43:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b basso-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 23:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 30:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 37:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 44:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b basso-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 31:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 38:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 45:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b basso-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 39:
                        caseattacbassodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 46:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b basso-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassodestra):
                    if posizione == 47:
                        caseattacbassodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in basso a sinistra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * n)
            mury = y + (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * m)
            mury = y + (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury + gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    #  caseattacbassosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in basso a sinistra
    caseattacbassosinistra = []
    # riempio caseattacbassosinistra come se tutto il campo in basso a sinistra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacbassosinistra.append(x - (gpx * n))
            caseattacbassosinistra.append(y + (gpy * m))
            caseattacbassosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacbassosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 13:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a basso-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 6:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 13:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 20:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 27:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 34:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 41:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 48:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b basso-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 7:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 14:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 21:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 28:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 28:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 35:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 35:
                        caseattacbassosinistra[j + 2] = False
                    if posizione == 42:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 42:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b basso-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 15:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 22:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 29:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 36:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 43:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b basso-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 23:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 30:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 37:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 44:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b basso-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 31:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 38:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 45:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b basso-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 39:
                        caseattacbassosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 46:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b basso-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y + (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacbassosinistra):
                    if posizione == 47:
                        caseattacbassosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in alto a sinistra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * n)
            mury = y - (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx - gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x - (gpx * m)
            mury = y - (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    # caseattacaltosinistra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a sinistra
    caseattacaltosinistra = []
    # riempio caseattacaltosinistra come se tutto il campo in alto a sinistra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacaltosinistra.append(x - (gpx * n))
            caseattacaltosinistra.append(y - (gpy * m))
            caseattacaltosinistra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltosinistra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 13:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a alto-sinistra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 6:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 13:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 27:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 20:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 34:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 27:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 34:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 41:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 48:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b alto-sinistra
            if caseattac[i] == x - gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 7:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 14:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 21:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 28:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 28:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 35:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 35:
                        caseattacaltosinistra[j + 2] = False
                    if posizione == 42:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 42:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b alto-sinistra
            if caseattac[i] == x - (gpx * 2) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 15:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 22:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 29:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 36:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 43:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b alto-sinistra
            if caseattac[i] == x - (gpx * 3) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 23:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 30:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 37:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 44:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b alto-sinistra
            if caseattac[i] == x - (gpx * 4) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 31:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 38:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 45:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b alto-sinistra
            if caseattac[i] == x - (gpx * 5) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 39:
                        caseattacaltosinistra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 46:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b alto-sinistra
            if caseattac[i] == x - (gpx * 6) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltosinistra):
                    if posizione == 47:
                        caseattacaltosinistra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattac[x, y, flag, ... ] -> per trovare gli ostacoli in alto a destra
    caseattac = []
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * n)
            mury = y - (gpy * m)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if murx != nmurx:
                caseattac.append(nmurx)
                caseattac.append(nmury)
                caseattac.append(True)
            else:
                caseattac.append(nmurx + gpx)
                caseattac.append(nmury)
                caseattac.append(False)
            m = m + 1
        n = n + 1
    n = -1
    while n < range:
        m = 0
        while m <= range:
            murx = x + (gpx * m)
            mury = y - (gpy * n)
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True, False, porte, cofanetti)
            if mury == nmury:
                i = 0
                while i < len(caseattac):
                    if caseattac[i] == nmurx and caseattac[i + 1] == nmury - gpy:
                        caseattac[i + 2] = False
                        break
                    i = i + 3
            m = m + 1
        n = n + 1
    # caseattacaltodestra[x, y, flag, ... ] -> per definire la visibilita' ridotta dagli ostacoli in alto a destra
    caseattacaltodestra = []
    # riempio caseattacaltosinistra come se tutto il campo in alto a destra fosse libero
    n = 0
    while n <= range:
        m = 0
        while m <= range:
            caseattacaltodestra.append(x + (gpx * n))
            caseattacaltodestra.append(y - (gpy * m))
            caseattacaltodestra.append(True)
            m = m + 1
        n = n + 1
    # imposto a False le caselle che non si vedono
    caseattacaltodestra[2] = False
    i = 0
    while i < len(caseattac):
        if not caseattac[i + 2]:
            # situazione: 1a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 9 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 2 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 3 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 4 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 13:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 5 and posizione <= 6:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5a alto-destra
            if caseattac[i] == x and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 6:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 6ab alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 8 and posizione <= 9:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 15 and posizione <= 19:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 9 and posizione <= 11:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 17 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 10 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 27:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 11 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 12 and posizione <= 13:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5a alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 13:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 11ab alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 16 and posizione <= 17:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 23 and posizione <= 25:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 17 and posizione <= 18:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 25 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 18 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 34:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 19 and posizione <= 20:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 27:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5a alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 20:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 15ab alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 24 and posizione <= 25:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 31 and posizione <= 33:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16a alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 25 and posizione <= 26:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17a alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 26 and posizione <= 27:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 34:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5a alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 27:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 18ab alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 32 and posizione <= 33:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 39 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19a alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 33 and posizione <= 34:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5a alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 34:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20ab alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione >= 40 and posizione <= 41:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 47 and posizione <= 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5a alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 41:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.75ab alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 6):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 48:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 1b alto-destra
            if caseattac[i] == x + gpx and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 7:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 14 and posizione <= 15:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 23:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 2b alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 14:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 21 and posizione <= 22:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 28 and posizione <= 29:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 3b alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 21:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 28:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 35 and posizione <= 36:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 4b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 28:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 35:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 42 and posizione <= 43:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 35:
                        caseattacaltodestra[j + 2] = False
                    if posizione == 42:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 5.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 42:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 7b alto-destra
            if caseattac[i] == x + (gpx * 2) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 15:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 22 and posizione <= 23:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 8b alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 22:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 29 and posizione <= 30:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 45:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 9b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 29:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 36 and posizione <= 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 36:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 43 and posizione <= 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 10.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - gpy:
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 43:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 12b alto-destra
            if caseattac[i] == x + (gpx * 3) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 23:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 30 and posizione <= 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 13b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 30:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 37 and posizione <= 38:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 46:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 37:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 44 and posizione <= 45:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 14.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 2):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 44:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 16b alto-destra
            if caseattac[i] == x + (gpx * 4) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 31:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 38 and posizione <= 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 38:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 45 and posizione <= 46:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 17.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 3):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 45:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19b alto-destra
            if caseattac[i] == x + (gpx * 5) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 39:
                        caseattacaltodestra[j + 2] = False
                    if posizione >= 46 and posizione <= 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 19.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 4):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 46:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
            # situazione: 20.5b alto-destra
            if caseattac[i] == x + (gpx * 6) and caseattac[i + 1] == y - (gpy * 5):
                # posizione -> per associare le caselle alle posizioni del vettore
                posizione = 0
                j = 0
                while j < len(caseattacaltodestra):
                    if posizione == 47:
                        caseattacaltodestra[j + 2] = False
                    posizione = posizione + 1
                    j = j + 3
        i = i + 3

    # caseattactot[x, y, flag, ... ] -> per definire la visibilita' ridotta da tutti gli ostacoli
    caseattactot = caseattacaltodestra + caseattacaltosinistra + caseattacbassodestra + caseattacbassosinistra

    return caseattactot


def attacca(x, y, npers, nrob, rx, ry, pers, pv, pvtot, avvele, attp, difp, enrob, entot, surrisc, velp, effp,
            stanzaa, stanza, sfondinoa, sfondinob, sfondinoc, arma, armatura, scudo, robot, armrob,
            nemicoa, mxa, mya, nemicob, mxb, myb, nemicoc, mxc, myc, nemicod, mxd, myd, nemicoe, mxe, mye,
            nemicof, mxf, myf, nemicog, mxg, myg, nemicoh, mxh, myh, nemicoi, mxi, myi, nemicol, mxl, myl,
            pvmatot, pvmbtot, pvmctot, pvmdtot, pvmetot, pvmftot, pvmgtot, pvmhtot, pvmitot, pvmltot,
            pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, statoma, statomb, statomc, statomd,
            statome, statomf, statomg, statomh, statomi, statoml, raggiovistaa, raggiovistab, raggiovistac,
            raggiovistad, raggiovistae, raggiovistaf, raggiovistag, raggiovistah, raggiovistai, raggiovistal,
            att, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio):
    if attacco <= 6:
        xp = x
        yp = y
    elif attacco > 6:
        xp = rx
        yp = ry
    nxp = 0
    nyp = 0
    risposta = False

    # modifica puntatore a seconda dell'attacco
    puntat = pygame.image.load('Immagini\Puntatori\Inquadra.png')
    puntat = pygame.transform.scale(puntat, (gpx, gpy))
    if attacco == 1:
        puntatogg = pygame.image.load('Immagini\Oggetti\Attacco.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 2:
        puntatogg = pygame.image.load('Immagini\Oggetti\Bomba.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 3:
        puntatogg = pygame.image.load('Immagini\Oggetti\BombaVeleno.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 4:
        puntatogg = pygame.image.load('Immagini\Oggetti\Esca.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 5:
        puntatogg = pygame.image.load('Immagini\Oggetti\BombaAppiccicosa.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 6:
        puntatogg = pygame.image.load('Immagini\Oggetti\BombaPotenziata.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 7:
        puntatogg = pygame.image.load('Immagini\Oggetti\Scossa.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 8:
        puntatogg = pygame.image.load('Immagini\Oggetti\Frecciaelettrica.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 10:
        puntatogg = pygame.image.load('Immagini\Oggetti\Scossa+.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 11:
        puntatogg = pygame.image.load('Immagini\Oggetti\Frecciaelettrica+.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 13:
        puntatogg = pygame.image.load('Immagini\Oggetti\Scossa++.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 14:
        puntatogg = pygame.image.load('Immagini\Oggetti\Frecciaelettrica++.png')
        puntatogg = pygame.transform.scale(puntatogg, (gpx, gpy))
    if attacco == 9 or attacco == 12 or attacco == 15:
        puntat = None
        puntatogg = None

    campoattaccabile1 = pygame.image.load('Immagini\Campiattaccabili\Campoattaccabile1.png')
    campoattaccabile1 = pygame.transform.scale(campoattaccabile1, (gpx * 3, gpy * 3))
    campoattaccabile2 = pygame.image.load('Immagini\Campiattaccabili\Campoattaccabile2.png')
    campoattaccabilemostro = pygame.image.load('Immagini\Campiattaccabili\Campoattaccabilemostro.png')
    # caselle attaccabili
    caselleattaccabilimostro = pygame.image.load('Immagini\Campiattaccabili\Caselleattaccabilimostro.png')
    caselleattaccabilimostro = pygame.transform.scale(caselleattaccabilimostro, (gpx, gpy))
    caselleattaccabili = pygame.image.load('Immagini\Campiattaccabili\Caselleattaccabili.png')
    caselleattaccabili = pygame.transform.scale(caselleattaccabili, (gpx, gpy))

    schermo.blit(stanzaa, (0, 0))
    if apriocchio:
        schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
    else:
        schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))
    # cofanetti
    i = 0
    while i < len(cofanetti):
        j = 0
        while j < len(caseviste):
            if ((caseviste[j] == cofanetti[i + 1] - gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + gpy)) and caseviste[j + 2]:
                schermo.blit(sfondinoc, (cofanetti[i + 1], cofanetti[i + 2]))
                if cofanetti[i + 3]:
                    schermo.blit(cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                else:
                    schermo.blit(cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
            j = j + 3
        i = i + 4
    i = 0
    # disegno le caselle viste
    while i < len(caseviste):
        if caseviste[i + 2]:
            n = 0
            while n < 32:
                if caseviste[i] == gpx * n:
                    m = 0
                    while m < 18:
                        if caseviste[i + 1] == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                        m = m + 1
                n = n + 1
        i = i + 3

    # ricarico immagine vitaesche
    vitaesche = pygame.image.load('Immagini\Barrevita\Vitaesca.png')

    # vita-status personaggio
    lungvitatot = (gpx // 4) * (pvtot // 5)
    lungvita = (lungvitatot * pv) // pvtot
    if lungvita < 0:
        lungvita = 0
    indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
    vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
    schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 16))
    persbat = pygame.transform.scale(perso, (gpx, gpy))
    schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 16))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if avvele:
        schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
    if attp > 0:
        schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
    if difp > 0:
        schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

    # vita-status robo
    lungentot = (gpx // 4) * (entot // 10)
    lungen = (lungentot * enrob) // entot
    if lungen < 0:
        lungen = 0
    indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
    vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
    schermo.blit(indvitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(vitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
    schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 17))
    robobat = pygame.transform.scale(roboo, (gpx, gpy))
    schermo.blit(robobat, (gsx // 32 * 0, gsy // 18 * 17))
    schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if surrisc > 0:
        schermo.blit(surriscaldato, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
    if velp > 0:
        schermo.blit(velocitapiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
    if effp > 0:
        schermo.blit(efficienzapiu, ((gsx // 32 * 1) + (gpx // 4 * 3) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))

    # tempeste elettriche
    if attacco == 9 or attacco == 12 or attacco == 15:
        infliggidanno = False
        if attacco == 9:
            infliggidanno = True
            raggio = gpx * 4
            danno = 3
        if attacco == 12:
            infliggidanno = True
            raggio = gpx * 5
            danno = 25
        if attacco == 15:
            infliggidanno = True
            raggio = gpx * 6
            danno = 50
        if (abs(mxa - rx) <= raggio and abs(mya - ry) <= raggio) and infliggidanno:
            pvma = pvma - danno
        if (abs(mxb - rx) <= raggio and abs(myb - ry) <= raggio) and infliggidanno:
            pvmb = pvmb - danno
        if (abs(mxc - rx) <= raggio and abs(myc - ry) <= raggio) and infliggidanno:
            pvmc = pvmc - danno
        if (abs(mxd - rx) <= raggio and abs(myd - ry) <= raggio) and infliggidanno:
            pvmd = pvmd - danno
        if (abs(mxe - rx) <= raggio and abs(mye - ry) <= raggio) and infliggidanno:
            pvme = pvme - danno
        if (abs(mxf - rx) <= raggio and abs(myf - ry) <= raggio) and infliggidanno:
            pvmf = pvmf - danno
        if (abs(mxg - rx) <= raggio and abs(myg - ry) <= raggio) and infliggidanno:
            pvmg = pvmg - danno
        if (abs(mxh - rx) <= raggio and abs(myh - ry) <= raggio) and infliggidanno:
            pvmh = pvmh - danno
        if (abs(mxi - rx) <= raggio and abs(myi - ry) <= raggio) and infliggidanno:
            pvmi = pvmi - danno
        if (abs(mxl - rx) <= raggio and abs(myl - ry) <= raggio) and infliggidanno:
            pvml = pvml - danno
        risposta = True
        sposta = True

    tastotempfps = 3
    tastop = 0
    danno = 0
    creaesca = False
    ricaricaschermo1 = False
    ricaricaschermo2 = False
    ricaricaschermo3 = False
    while not risposta:

        # rallenta per i 20 fps
        if tastotempfps != 0 and tastop != 0:
            tastotempfps = tastotempfps - 1
            nxp = 0
            nyp = 0
        if tastotempfps == 0 and tastop != 0:
            if tastop == pygame.K_w:
                nyp = -gpy
            if tastop == pygame.K_a:
                nxp = -gpx
            if tastop == pygame.K_s:
                nyp = gpy
            if tastop == pygame.K_d:
                nxp = gpx
            tastotempfps = 2

        xvp = xp
        yvp = yp

        n = 0
        while n < 32:
            if xvp == gpx * n:
                m = 0
                while m < 18:
                    if yvp == gpy * m:
                        if (n + m) % 2 == 0:
                            schermo.blit(sfondinoa, (xvp, yvp))
                        if (n + m) % 2 != 0:
                            schermo.blit(sfondinob, (xvp, yvp))
                    m = m + 1
            n = n + 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # esci
                if event.key == pygame.K_q:
                    risposta = True
                    sposta = False
                    selind.play()
                # movimento puntatore
                tastop = event.key
                if event.key == pygame.K_w:
                    nyp = -gpy
                if event.key == pygame.K_a:
                    nxp = -gpx
                if event.key == pygame.K_s:
                    nyp = gpy
                if event.key == pygame.K_d:
                    nxp = gpx
                # attacco
                if event.key == pygame.K_SPACE:
                    sposta = False
                    if attacco != 0:
                        infliggidanno = False
                        statom = 0
                        raggio = 0
                        # normale attacco = 1
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)):
                            infliggidanno = True
                            danno = att
                            raggio = gpx * 0
                        # bomba attacco = 2
                        if attacco == 2 and (abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 10
                                raggio = gpx * 1
                                sposta = True
                                risposta = True
                        # bomba veleno attacco = 3
                        if attacco == 3 and (abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 20
                                statom = 1
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # esca attacco = 4
                        if attacco == 4 and (abs(x - xp) <= gpx * 6 and abs(y - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                # conferma lancio esche
                                confesca = True
                                i = 2
                                while i < len(vitaesca):
                                    if vitaesca[i] == xp and vitaesca[i + 1] == yp:
                                        confesca = False
                                    i = i + 4
                                if (xp == mxa and yp == mya) or (xp == mxb and yp == myb) or (xp == mxc and yp == myc) or (xp == mxd and yp == myd) or (xp == mxe and yp == mye) or (xp == mxf and yp == myf) or (xp == mxg and yp == myg) or (xp == mxh and yp == myh) or (xp == mxi and yp == myi) or (xp == mxl and yp == myl):
                                    confesca = False
                                if confesca:
                                    infliggidanno = True
                                    danno = 0
                                    raggio = 0
                                    creaesca = True
                                    sposta = True
                                    risposta = True
                                else:
                                    selimp.play()
                        # bomba appiccicosa attacco = 5
                        if attacco == 5 and (abs(x - xp) <= gpx * 5 and abs(y - yp) <= gpy * 5):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 20
                                statom = 2
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # bomba potenziata attacco = 6
                        if attacco == 6 and (abs(x - xp) <= gpx * 4 and abs(y - yp) <= gpy * 4):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 200
                                raggio = gpx * 2
                                sposta = True
                                risposta = True
                        # scossa attacco = 7
                        if attacco == 7 and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)):
                            infliggidanno = True
                            danno = 10
                            raggio = gpx * 0
                        # freccia elettrica attacco = 8
                        if attacco == 8 and (abs(rx - xp) <= gpx * 6 and abs(ry - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 5
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # scossa+ attacco = 10
                        if attacco == 10 and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)):
                            infliggidanno = True
                            danno = 100
                            raggio = gpx * 0
                        # freccia elettrica+ attacco = 11
                        if attacco == 11 and (abs(rx - xp) <= gpx * 6 and abs(ry - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 50
                                raggio = gpx * 0
                                sposta = True
                                risposta = True
                        # scossa++ attacco = 13
                        if attacco == 13 and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)):
                            infliggidanno = True
                            danno = 200
                            raggio = gpx * 0
                        # freccia elettrica++ attacco = 14
                        if attacco == 14 and (abs(rx - xp) <= gpx * 6 and abs(ry - yp) <= gpy * 6):
                            # controllo caselle attaccabili
                            continua = True
                            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
                            i = 0
                            # disegno le caselle attaccabili
                            while i < len(caseattactot):
                                if caseattactot[i] == xp and caseattactot[i + 1] == yp and not caseattactot[i + 2]:
                                    continua = False
                                i = i + 3
                            if continua:
                                infliggidanno = True
                                danno = 100
                                raggio = gpx * 0
                                sposta = True
                                risposta = True

                        if (((abs(mxa - xp) <= raggio and abs(mya - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxa and yp == mya) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statoma == 2:
                                    statoma = 3
                                else:
                                    statoma = 1
                            if statom == 2:
                                if statoma == 1:
                                    statoma = 3
                                else:
                                    statoma = 2
                            pvma = pvma - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxb - xp) <= raggio and abs(myb - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxb and yp == myb) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomb == 2:
                                    statomb = 3
                                else:
                                    statomb = 1
                            if statom == 2:
                                if statomb == 1:
                                    statomb = 3
                                else:
                                    statomb = 2
                            pvmb = pvmb - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxc - xp) <= raggio and abs(myc - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxc and yp == myc) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomc == 2:
                                    statomc = 3
                                else:
                                    statomc = 1
                            if statom == 2:
                                if statomc == 1:
                                    statomc = 3
                                else:
                                    statomc = 2
                            pvmc = pvmc - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxd - xp) <= raggio and abs(myd - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxd and yp == myd) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomd == 2:
                                    statomd = 3
                                else:
                                    statomd = 1
                            if statom == 2:
                                if statomd == 1:
                                    statomd = 3
                                else:
                                    statomd = 2
                            pvmd = pvmd - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxe - xp) <= raggio and abs(mye - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxe and yp == mye) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statome == 2:
                                    statome = 3
                                else:
                                    statome = 1
                            if statom == 2:
                                if statome == 1:
                                    statome = 3
                                else:
                                    statome = 2
                            pvme = pvme - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxf - xp) <= raggio and abs(myf - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxf and yp == myf) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomf == 2:
                                    statomf = 3
                                else:
                                    statomf = 1
                            if statom == 2:
                                if statomf == 1:
                                    statomf = 3
                                else:
                                    statomf = 2
                            pvmf = pvmf - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxg - xp) <= raggio and abs(myg - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxg and yp == myg) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomg == 2:
                                    statomg = 3
                                else:
                                    statomg = 1
                            if statom == 2:
                                if statomg == 1:
                                    statomg = 3
                                else:
                                    statomg = 2
                            pvmg = pvmg - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxh - xp) <= raggio and abs(myh - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxh and yp == myh) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomh == 2:
                                    statomh = 3
                                else:
                                    statomh = 1
                            if statom == 2:
                                if statomh == 1:
                                    statomh = 3
                                else:
                                    statomh = 2
                            pvmh = pvmh - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxi - xp) <= raggio and abs(myi - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxi and yp == myi) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statomi == 2:
                                    statomi = 3
                                else:
                                    statomi = 1
                            if statom == 2:
                                if statomi == 1:
                                    statomi = 3
                                else:
                                    statomi = 2
                            pvmi = pvmi - danno
                            sposta = True
                            risposta = True
                        if (((abs(mxl - xp) <= raggio and abs(myl - yp) <= raggio) and attacco != 1) or (
                                    (xp == mxl and yp == myl) and attacco == 1)) and infliggidanno:
                            if statom == 1:
                                if statoml == 2:
                                    statoml = 3
                                else:
                                    statoml = 1
                            if statom == 2:
                                if statoml == 1:
                                    statoml = 3
                                else:
                                    statoml = 2
                            pvml = pvml - danno
                            sposta = True
                            risposta = True

                        # attacco normale se c'e' il mostro
                        if attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and sposta and risposta:
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                            rumoreattacco.play()
                        # attacco normale se non c'e' il mostro
                        elif attacco == 1 and ((xp == x + gpx and yp == y) or (xp == x - gpx and yp == y) or (xp == x and yp == y + gpy) or (xp == x and yp == y - gpy)) and not sposta and not risposta:
                            if xp == x + gpx and yp == y:
                                npers = 1
                            if xp == x - gpx and yp == y:
                                npers = 2
                            if xp == x and yp == y + gpy:
                                npers = 4
                            if xp == x and yp == y - gpy:
                                npers = 3
                            sposta = True
                            risposta = True
                        # scossa se c'e' il mostro
                        if (attacco == 7 or attacco == 10 or attacco == 13) and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)) and sposta and risposta:
                            if xp == rx + gpx and yp == ry:
                                nrob = 1
                            if xp == rx - gpx and yp == ry:
                                nrob = 2
                            if xp == rx and yp == ry + gpy:
                                nrob = 3
                            if xp == rx and yp == ry - gpy:
                                nrob = 4
                            rumoreattacco.play()
                        # scossa se non c'e' il mostro
                        elif (attacco == 7 or attacco == 10 or attacco == 13) and ((xp == rx + gpx and yp == ry) or (xp == rx - gpx and yp == ry) or (xp == rx and yp == ry + gpy) or (xp == rx and yp == ry - gpy)) and not sposta and not risposta:
                            if xp == rx + gpx and yp == ry:
                                nrob = 1
                            if xp == rx - gpx and yp == ry:
                                nrob = 2
                            if xp == rx and yp == ry + gpy:
                                nrob = 3
                            if xp == rx and yp == ry - gpy:
                                nrob = 4
                            rumoreattacco.play()
                            sposta = True
                            risposta = True

                        if not risposta:
                            selimp.play()
            if event.type == pygame.KEYUP:
                tastop = 0
                tastotempfps = 5
                nxp = 0
                nyp = 0

        if ricaricaschermo1:
            ricaricaschermo2 = True
        elif not ricaricaschermo1 and ricaricaschermo2:
            ricaricaschermo3 = True

        if ricaricaschermo3:
            schermo.blit(stanzaa, (0, 0))
            # cofanetti
            i = 0
            while i < len(cofanetti):
                j = 0
                while j < len(caseviste):
                    if ((caseviste[j] == cofanetti[i + 1] - gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] + gpx and caseviste[j + 1] == cofanetti[i + 2]) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] - gpy) or (caseviste[j] == cofanetti[i + 1] and caseviste[j + 1] == cofanetti[i + 2] + gpy)) and caseviste[j + 2]:
                        if cofanetti[i + 3]:
                            schermo.blit(cofaniaper, (cofanetti[i + 1], cofanetti[i + 2]))
                        else:
                            schermo.blit(cofanichiu, (cofanetti[i + 1], cofanetti[i + 2]))
                    j = j + 3
                i = i + 4
            if apriocchio:
                schermo.blit(occhioape, (gsx - (gpx * 4 // 3), gpy // 3))
            else:
                schermo.blit(occhiochiu, (gsx - (gpx * 4 // 3), gpy // 3))
            # fai vedere stanze visitate
            # caseviste[x, y, flag, ... ] -> riempito come se non vedessi niente
            i = 0
            # disegno le caselle viste
            while i < len(caseviste):
                if caseviste[i + 2]:
                    n = 0
                    while n < 32:
                        if caseviste[i] == gpx * n:
                            m = 0
                            while m < 18:
                                if caseviste[i + 1] == gpy * m:
                                    if (n + m) % 2 == 0:
                                        schermo.blit(sfondinoa, (caseviste[i], caseviste[i + 1]))
                                    if (n + m) % 2 != 0:
                                        schermo.blit(sfondinob, (caseviste[i], caseviste[i + 1]))
                                m = m + 1
                        n = n + 1
                i = i + 3
            ricaricaschermo1 = False
            ricaricaschermo2 = False
            ricaricaschermo3 = False

        # visualizza campo attaccabile
        if attacco == 1:
            schermo.blit(campoattaccabile1, (x - gpx, y - gpy))
            # controllo caselle attaccabili
            caseattactot = [x + gpx, y, True, x - gpx, y, True, x, y + gpy, True, x, y - gpy, True]
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[2] = False
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[5] = False
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[8] = False
            murx = x
            mury = y
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True ,False, porte, cofanetti)
            if nmury == mury:
                caseattactot[11] = False
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2]:
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 2:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (x - (gpx * 6), y - (gpy * 6)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 6 and caseattactot[i + 1] <= y + gpy * 6 and caseattactot[i] >= x - gpx * 6 and caseattactot[i + 1] >= y - gpy * 6 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 3:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 11, gpy * 11))
            schermo.blit(campoattaccabile3, (x - (gpx * 5), y - (gpy * 5)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 5 and caseattactot[i + 1] <= y + gpy * 5 and caseattactot[i] >= x - gpx * 5 and caseattactot[i + 1] >= y - gpy * 5 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 4:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (x - (gpx * 6), y - (gpy * 6)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 6 and caseattactot[i + 1] <= y + gpy * 6 and caseattactot[i] >= x - gpx * 6 and caseattactot[i + 1] >= y - gpy * 6 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 5:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 11, gpy * 11))
            schermo.blit(campoattaccabile3, (x - (gpx * 5), y - (gpy * 5)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 5 and caseattactot[i + 1] <= y + gpy * 5 and caseattactot[i] >= x - gpx * 5 and caseattactot[i + 1] >= y - gpy * 5 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 6:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 9, gpy * 9))
            schermo.blit(campoattaccabile3, (x - (gpx * 4), y - (gpy * 4)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(x, y, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= x + gpx * 4 and caseattactot[i + 1] <= y + gpy * 4 and caseattactot[i] >= x - gpx * 4 and caseattactot[i + 1] >= y - gpy * 4 and not (caseattactot[i] == x and caseattactot[i + 1] == y)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 7 or attacco == 10 or attacco == 13:
            schermo.blit(campoattaccabile1, (rx - gpx, ry - gpy))
            # controllo caselle attaccabili
            caseattactot = [rx + gpx, ry, True, rx - gpx, ry, True, rx, ry + gpy, True, rx, ry - gpy, True]
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[2] = False
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, stanza, False, 0, True, False, porte, cofanetti)
            if nmurx == murx:
                caseattactot[5] = False
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, stanza, False, 0, True, False, porte, cofanetti)
            if nmury == mury:
                caseattactot[8] = False
            murx = rx
            mury = ry
            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, stanza, False, 0, True ,False, porte, cofanetti)
            if nmury == mury:
                caseattactot[11] = False
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2]:
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
        if attacco == 8 or attacco == 11 or attacco == 14:
            campoattaccabile3 = pygame.transform.scale(campoattaccabile2, (gpx * 13, gpy * 13))
            schermo.blit(campoattaccabile3, (rx - (gpx * 6), ry - (gpy * 6)))
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(rx, ry, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= rx + gpx * 6 and caseattactot[i + 1] <= ry + gpy * 6 and caseattactot[i] >= rx - gpx * 6 and caseattactot[i + 1] >= ry - gpy * 6 and not (caseattactot[i] == rx and caseattactot[i + 1] == ry)):
                    schermo.blit(caselleattaccabili, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3

        # movimento inquadra (ultimi 4 inutili)
        xp, yp, stanza, carim, muovi, cambiosta = muri_porte(xp, yp, nxp, nyp, stanza, False, 0, True, False, porte, cofanetti)

        # esche: id, vita, xesca, yesca
        i = 0
        while i < len(vitaesca):
            schermo.blit(esche, (vitaesca[i + 2], vitaesca[i + 3]))
            i = i + 4

        # robo
        schermo.blit(robot, (rx, ry))
        schermo.blit(armrob, (rx, ry))
        # personaggio
        if not risposta:
            if npers == 1:
                schermo.blit(scudo, (x, y))
                schermo.blit(pers, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(persdb, (x, y))
                schermo.blit(arma, (x, y))
            if npers == 2:
                schermo.blit(arma, (x, y))
                schermo.blit(pers, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(persab, (x, y))
                schermo.blit(scudo, (x, y))
            if npers == 3:
                schermo.blit(arma, (x, y))
                schermo.blit(scudo, (x, y))
                schermo.blit(pers, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(perswb, (x, y))
            if npers == 4:
                schermo.blit(pers, (x, y))
                schermo.blit(armatura, (x, y))
                schermo.blit(perssb, (x, y))
                schermo.blit(arma, (x, y))
                schermo.blit(scudo, (x, y))

        # disegnare i mostri
        j = 0
        while j < len(caseviste):
            if nemicoa != 0 and caseviste[j] == mxa and caseviste[j + 1] == mya and caseviste[j + 2]:
                schermo.blit(nemicoa, (mxa, mya))
            if nemicob != 0 and caseviste[j] == mxb and caseviste[j + 1] == myb and caseviste[j + 2]:
                schermo.blit(nemicob, (mxb, myb))
            if nemicoc != 0 and caseviste[j] == mxc and caseviste[j + 1] == myc and caseviste[j + 2]:
                schermo.blit(nemicoc, (mxc, myc))
            if nemicod != 0 and caseviste[j] == mxd and caseviste[j + 1] == myd and caseviste[j + 2]:
                schermo.blit(nemicod, (mxd, myd))
            if nemicoe != 0 and caseviste[j] == mxe and caseviste[j + 1] == mye and caseviste[j + 2]:
                schermo.blit(nemicoe, (mxe, mye))
            if nemicof != 0 and caseviste[j] == mxf and caseviste[j + 1] == myf and caseviste[j + 2]:
                schermo.blit(nemicof, (mxf, myf))
            if nemicog != 0 and caseviste[j] == mxg and caseviste[j + 1] == myg and caseviste[j + 2]:
                schermo.blit(nemicog, (mxg, myg))
            if nemicoh != 0 and caseviste[j] == mxh and caseviste[j + 1] == myh and caseviste[j + 2]:
                schermo.blit(nemicoh, (mxh, myh))
            if nemicoi != 0 and caseviste[j] == mxi and caseviste[j + 1] == myi and caseviste[j + 2]:
                schermo.blit(nemicoi, (mxi, myi))
            if nemicol != 0 and caseviste[j] == mxl and caseviste[j + 1] == myl and caseviste[j + 2]:
                schermo.blit(nemicol, (mxl, myl))
            j = j + 3

        # puntatore
        schermo.blit(puntat, (xp, yp))
        schermo.blit(puntatogg, (xp, yp))
        if risposta:
            n = 0
            m = 0
            while n < 32:
                if xp == gpx * n:
                    while m < 18:
                        if yp == gpy * m:
                            if (n + m) % 2 == 0:
                                schermo.blit(sfondinoa, (xp, yp))
                            if (n + m) % 2 != 0:
                                schermo.blit(sfondinob, (xp, yp))
                        m = m + 1
                n = n + 1

        # disegna vita-status-raggio visivo mostri
        if xp == mxa and yp == mya and nemicoa != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxa, mya, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxa + raggiovistaa and caseattactot[i + 1] <= mya + raggiovistaa and caseattactot[i] >= mxa - raggiovistaa and caseattactot[i + 1] >= mya - raggiovistaa and not (caseattactot[i] == mxa and caseattactot[i + 1] == mya)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistaa * 2) + gpx, (raggiovistaa * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxa - raggiovistaa, mya - raggiovistaa))
            lungvita = (gpx * 8 * pvma) // pvmatot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statoma == 1 or statoma == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statoma == 2 or statoma == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicoa, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxb and yp == myb and nemicob != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxb, myb, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxb + raggiovistab and caseattactot[i + 1] <= myb + raggiovistab and caseattactot[i] >= mxb - raggiovistab and caseattactot[i + 1] >= myb - raggiovistab and not (caseattactot[i] == mxb and caseattactot[i + 1] == myb)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistab * 2) + gpx, (raggiovistab * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxb - raggiovistab, myb - raggiovistab))
            lungvita = (gpx * 8 * pvmb) // pvmbtot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomb == 1 or statomb == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomb == 2 or statomb == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicob, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxc and yp == myc and nemicoc != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxc, myc, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxc + raggiovistac and caseattactot[i + 1] <= myc + raggiovistac and caseattactot[i] >= mxc - raggiovistac and caseattactot[i + 1] >= myc - raggiovistac and not (caseattactot[i] == mxc and caseattactot[i + 1] == myc)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistac * 2) + gpx, (raggiovistac * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxc - raggiovistac, myc - raggiovistac))
            lungvita = (gpx * 8 * pvmc) // pvmctot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomc == 1 or statomc == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomc == 2 or statomc == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicoc, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxd and yp == myd and nemicod != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxd, myd, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxd + raggiovistad and caseattactot[i + 1] <= myd + raggiovistad and caseattactot[i] >= mxd - raggiovistad and caseattactot[i + 1] >= myd - raggiovistad and not (caseattactot[i] == mxd and caseattactot[i + 1] == myd)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistad * 2) + gpx, (raggiovistad * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxd - raggiovistad, myd - raggiovistad))
            lungvita = (gpx * 8 * pvmd) // pvmdtot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomd == 1 or statomd == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomd == 2 or statomd == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicod, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxe and yp == mye and nemicoe != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxe, mye, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxe + raggiovistae and caseattactot[i + 1] <= mye + raggiovistae and caseattactot[i] >= mxe - raggiovistae and caseattactot[i + 1] >= mye - raggiovistae and not (caseattactot[i] == mxe and caseattactot[i + 1] == mye)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistae * 2) + gpx, (raggiovistae * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxe - raggiovistae, mye - raggiovistae))
            lungvita = (gpx * 8 * pvme) // pvmetot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statome == 1 or statome == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statome == 2 or statome == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicoe, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxf and yp == myf and nemicof != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxf, myf, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxf + raggiovistaf and caseattactot[i + 1] <= myf + raggiovistaf and caseattactot[i] >= mxf - raggiovistaf and caseattactot[i + 1] >= myf - raggiovistaf and not (caseattactot[i] == mxf and caseattactot[i + 1] == myf)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistaf * 2) + gpx, (raggiovistaf * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxf - raggiovistaf, myf - raggiovistaf))
            lungvita = (gpx * 8 * pvmf) // pvmftot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomf == 1 or statomf == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomf == 2 or statomf == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicof, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxg and yp == myg and nemicog != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxg, myg, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxg + raggiovistag and caseattactot[i + 1] <= myg + raggiovistag and caseattactot[i] >= mxg - raggiovistag and caseattactot[i + 1] >= myg - raggiovistag and not (caseattactot[i] == mxg and caseattactot[i + 1] == myg)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistag * 2) + gpx, (raggiovistag * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxg - raggiovistag, myg - raggiovistag))
            lungvita = (gpx * 8 * pvmg) // pvmgtot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomg == 1 or statomg == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomg == 2 or statomg == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicog, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxh and yp == myh and nemicoh != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxh, myh, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxh + raggiovistah and caseattactot[i + 1] <= myh + raggiovistah and caseattactot[i] >= mxh - raggiovistah and caseattactot[i + 1] >= myh - raggiovistah and not (caseattactot[i] == mxh and caseattactot[i + 1] == myh)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistah * 2) + gpx, (raggiovistah * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxh - raggiovistah, myh - raggiovistah))
            lungvita = (gpx * 8 * pvmh) // pvmhtot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomh == 1 or statomh == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomh == 2 or statomh == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicoh, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxi and yp == myi and nemicoi != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxi, myi, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxi + raggiovistai and caseattactot[i + 1] <= myi + raggiovistai and caseattactot[i] >= mxi - raggiovistai and caseattactot[i + 1] >= myi - raggiovistai and not (caseattactot[i] == mxi and caseattactot[i + 1] == myi)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistai * 2) + gpx, (raggiovistai * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxi - raggiovistai, myi - raggiovistai))
            lungvita = (gpx * 8 * pvmi) // pvmitot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomi == 1 or statomi == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statomi == 2 or statomi == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicoi, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if xp == mxl and yp == myl and nemicol != 0:
            # controllo caselle attaccabili
            caseattactot = trovacasattaccabili(mxl, myl, stanza, porte, cofanetti)
            i = 0
            # disegno le caselle attaccabili
            while i < len(caseattactot):
                if not caseattactot[i + 2] and (caseattactot[i] <= mxl + raggiovistal and caseattactot[i + 1] <= myl + raggiovistal and caseattactot[i] >= mxl - raggiovistal and caseattactot[i + 1] >= myl - raggiovistal and not (caseattactot[i] == mxl and caseattactot[i + 1] == myl)):
                    schermo.blit(caselleattaccabilimostro, (caseattactot[i], caseattactot[i + 1]))
                i = i + 3
            campoattaccabile3 = pygame.transform.scale(campoattaccabilemostro, ((raggiovistal * 2) + gpx, (raggiovistal * 2) + gpy))
            schermo.blit(campoattaccabile3, (mxl - raggiovistal, myl - raggiovistal))
            lungvita = (gpx * 8 * pvml) // pvmltot
            if lungvita < 0:
                lungvita = 0
            schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
            schermo.blit(sfondosta, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statoml == 1 or statoml == 3:
                schermo.blit(avvelenato, (gsx // 32 * 2, (gpy // 3) + (gpy // 4)))
            if statoml == 2 or statoml == 3:
                schermo.blit(appiccicoso, ((gsx // 32 * 2) + (gpx // 4 * 3), (gpy // 3) + (gpy // 4)))
            schermo.blit(nemicol, (gsx // 32 * 1, gpy // 3))
            indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
            vitanem = pygame.transform.scale(vitanemico, (lungvita, gpy // 4))
            schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
            schermo.blit(vitanem, (gsx // 32 * 2, gpy // 3))
            ricaricaschermo1 = True
        if not ((xp == mxa and yp == mya and nemicoa != 0) or (xp == mxb and yp == myb and nemicob != 0) or (xp == mxc and yp == myc and nemicoc != 0) or (xp == mxd and yp == myd and nemicod != 0) or (xp == mxe and yp == mye and nemicoe != 0) or (xp == mxf and yp == myf and nemicof != 0) or (xp == mxg and yp == myg and nemicog != 0) or (xp == mxh and yp == myh and nemicoh != 0) or (xp == mxi and yp == myi and nemicoi != 0) or (xp == mxl and yp == myl and nemicol != 0)):
            ricaricaschermo1 = False

        # disegna vita esche
        i = 0
        while i < len(vitaesca):
            if xp == vitaesca[i + 2] and yp == vitaesca[i + 3]:
                lungvita = (gpx * 8 * vitaesca[i + 1]) // 100
                if lungvita < 0:
                    lungvita = 0
                schermo.blit(sfondomo, (gsx // 32 * 1, gpy // 3))
                schermo.blit(esche, (gsx // 32 * 1, gpy // 3))
                indvitamost = pygame.transform.scale(indvita, (gpx * 8, gpy // 4))
                vitaesche = pygame.transform.scale(vitaesche, (lungvita, gpy // 4))
                schermo.blit(indvitamost, (gsx // 32 * 2, gpy // 3))
                schermo.blit(vitaesche, (gsx // 32 * 2, gpy // 3))
                ricaricaschermo1 = True
            i = i + 4

        # vita-status personaggio
        lungvitatot = (gpx // 4) * (pvtot // 5)
        lungvita = (lungvitatot * pv) // pvtot
        if lungvita < 0:
            lungvita = 0
        indvitapers = pygame.transform.scale(indvita, (lungvitatot, gpy // 4))
        vitaral = pygame.transform.scale(vitapersonaggio, (lungvita, gpy // 4))
        schermo.blit(indvitapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
        schermo.blit(vitaral, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 4 * 3)))
        schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 16))
        persbat = pygame.transform.scale(perso, (gpx, gpy))
        schermo.blit(persbat, (gsx // 32 * 0, gsy // 18 * 16))
        schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
        if avvele:
            schermo.blit(avvelenato, (gsx // 32 * 1, (gsy // 18 * 16) + (gpy // 8)))
        if attp > 0:
            schermo.blit(attaccopiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 16) + (gpy // 8)))
        if difp > 0:
            schermo.blit(difesapiu, ((gsx // 32 * 1) + (gpx // 4 * 6), (gsy // 18 * 16) + (gpy // 8)))

        # vita-status robo
        lungentot = (gpx // 4) * (entot // 10)
        lungen = (lungentot * enrob) // entot
        if lungen < 0:
            lungen = 0
        indvitarob = pygame.transform.scale(indvita, (lungentot, gpy // 4))
        vitarob = pygame.transform.scale(vitarobo, (lungen, gpy // 4))
        schermo.blit(indvitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
        schermo.blit(vitarob, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 4 * 3)))
        schermo.blit(sfondomo, (gsx // 32 * 0, gsy // 18 * 17))
        robobat = pygame.transform.scale(roboo, (gpx, gpy))
        schermo.blit(robobat, (gsx // 32 * 0, gsy // 18 * 17))
        schermo.blit(sfondostapers, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
        if surrisc > 0:
            schermo.blit(surriscaldato, (gsx // 32 * 1, (gsy // 18 * 17) + (gpy // 8)))
        if velp > 0:
            schermo.blit(velocitapiu, ((gsx // 32 * 1) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))
        if effp > 0:
            schermo.blit(efficienzapiu, ((gsx // 32 * 1) + (gpx // 4 * 3) + (gpx // 4 * 3), (gsy // 18 * 17) + (gpy // 8)))

        if not risposta:
            pygame.display.update()
        clock.tick(fpsmenu)

    return pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, sposta, creaesca, xp, yp, statoma, statomb, statomc, statomd, statome, statomf, statomg, statomh, statomi, statoml, npers, nrob


def aperturacofanetto(stanza, cx, cy, dati):
    # 11-30 -> tecniche(20) / 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-80 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20)
    if stanza == 1:
        if cx == gpx * 3 and cy == gpy * 7:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
    if stanza == 1:
        if cx == gpx * 7 and cy == gpy * 12:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
    if stanza == 1:
        if cx == gpx * 12 and cy == gpy * 11:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
    if stanza == 2:
        if cx == gpx * 3 and cy == gpy * 5:
            c = 0
            i = 101
            while i <= 120:
                if dati[i] == -1:
                    tesoro = i
                    break
                if c == 0:
                    c = 1
                    i = i + 10
                elif c == 1:
                    c = 0
                    i = i - 9
    if stanza == 2:
        if cx == gpx * 5 and cy == gpy * 10:
            tesoro = 11
    if stanza == 2:
        if cx == gpx * 10 and cy == gpy * 9:
            tesoro = 81
    if dati[tesoro] <= -1 and (tesoro >= 31 and tesoro <= 40):
        dati[tesoro] = dati[tesoro] + 2
    else:
        dati[tesoro] = dati[tesoro] + 1
    return dati, tesoro


def gameloop():
    # aumento livello
    saliliv = pygame.image.load('Immagini\Levelup\Saliliv.png')
    saliliv = pygame.transform.scale(saliliv, (gpx, gpy))
    saliliv1 = pygame.image.load('Immagini\Levelup\Saliliv1.png')
    saliliv1 = pygame.transform.scale(saliliv1, (gpx, gpy))
    saliliv2 = pygame.image.load('Immagini\Levelup\Saliliv2.png')
    saliliv2 = pygame.transform.scale(saliliv2, (gpx, gpy))
    saliliv3 = pygame.image.load('Immagini\Levelup\Saliliv3.png')
    saliliv3 = pygame.transform.scale(saliliv3, (gpx, gpy))

    inizio = True
    while True:
        if inizio:
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
            primadifesa = True
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
            difesa = False
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

            # mostri
            if dati[1] == 1 and cambiosta:
                # posizione personaggio e robot al cambio stanza
                if not inizio:
                    npers = 4
                    nrob = 3
                    x = gsx // 32 * 6
                    y = gsy // 18 * 2
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y
                    pers = perss
                    robot = robos
                    agg = 3

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
                pvmatot = 50
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
                    npers = 4
                    nrob = 3
                    x = gsx // 32 * 6
                    y = gsy // 18 * 2
                    vx = x
                    vy = y
                    rx = x
                    ry = y
                    vrx = x
                    vry = y
                    pers = perss
                    robot = robos
                    agg = 3

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
                # definire la cornice
                murx = x
                mury = y
                # imposto l'inizio del percorso
                arrivato = False
                while not arrivato:
                    nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
                    if mury != nmury:
                        mury = nmury
                    else:
                        arrivato = True
                inimurx = murx
                inimury = mury
                andare = "d"
                finito = False
                c = 5
                while not finito:
                    if c == 0:
                        finito = True
                    if inimurx == murx and inimury == mury:
                        c = c - 1
                    if andare == "d":
                        # vado a destra
                        nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                        if murx != nmurx:
                            i = 0
                            while i < len(caseviste):
                                if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                    caseviste[i + 2] = True
                                    murx = nmurx
                                    break
                                i = i + 3
                        else:
                            andare = "s"
                        if andare == "d":
                            andare = "w"
                    if andare == "s":
                        # vado in basso
                        nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, numstanza, False, 0, True, False, porte, cofanetti)
                        if mury != nmury:
                            i = 0
                            while i < len(caseviste):
                                if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                    caseviste[i + 2] = True
                                    mury = nmury
                                    break
                                i = i + 3
                        else:
                            andare = "a"
                        if andare == "s":
                            andare = "d"
                    if andare == "a":
                        # vado a sinistra
                        nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                        if murx != nmurx:
                            i = 0
                            while i < len(caseviste):
                                if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                    caseviste[i + 2] = True
                                    murx = nmurx
                                    break
                                i = i + 3
                        else:
                            andare = "w"
                        if andare == "a":
                            andare = "s"
                    if andare == "w":
                        # vado in alto
                        nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
                        if mury != nmury:
                            i = 0
                            while i < len(caseviste):
                                if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                    caseviste[i + 2] = True
                                    mury = nmury
                                    break
                                i = i + 3
                        else:
                            andare = "d"
                        if andare == "w":
                            andare = "a"
                casevisteprov = caseviste
                i = 0
                while i < len(caseviste):
                    n = -1
                    fine1 = False
                    fine2 = False
                    while n <= 28:
                        if not fine1 and caseviste[i + 2]:
                            murx = casevisteprov[i] + (gpx * n)
                            mury = casevisteprov[i + 1]
                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                            if murx != nmurx:
                                j = 0
                                while j < len(casevisteprov):
                                    if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                        casevisteprov[j + 2] = True
                                        break
                                    j = j + 3
                            else:
                                fine1 = True
                        if not fine2 and caseviste[i + 2]:
                            murx = casevisteprov[i] - (gpx * n)
                            mury = casevisteprov[i + 1]
                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                            if murx != nmurx:
                                j = 0
                                while j < len(casevisteprov):
                                    if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                        casevisteprov[j + 2] = True
                                        break
                                    j = j + 3
                            else:
                                fine2 = True
                        n = n + 1
                    n = 0
                    fine1 = False
                    fine2 = False
                    while n <= 14:
                        if not fine1 and caseviste[i + 2]:
                            murx = casevisteprov[i]
                            mury = casevisteprov[i + 1] + (gpy * n)
                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, numstanza, False, 0, True, False, porte, cofanetti)
                            if mury != nmury:
                                j = 0
                                while j < len(casevisteprov):
                                    if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                        casevisteprov[j + 2] = True
                                        break
                                    j = j + 3
                            else:
                                fine1 = True
                        if not fine2 and caseviste[i + 2]:
                            murx = casevisteprov[i]
                            mury = casevisteprov[i + 1] - (gpy * n)
                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
                            if mury != nmury:
                                j = 0
                                while j < len(casevisteprov):
                                    if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                        casevisteprov[j + 2] = True
                                        break
                                    j = j + 3
                            else:
                                fine2 = True
                        n = n + 1
                    i = i + 3
                caseviste = casevisteprov

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
        '''if not primopas and tastotempfps != 0 and premuti == 1:
            tastotempfps = tastotempfps - 1
            nx = 0
            ny = 0
        if not primopas and tastotempfps == 0 and premuti == 1:
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
        if primopas and tastotemp != 0 and premuti == 1:
            tastotemp = tastotemp - 1
            nx = 0
            ny = 0
        if primopas and tastotemp == 0 and premuti == 1:
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

        # catturare gli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                premuti = premuti + 1
                if premuti > 1:
                    premuti = 1
                # movimanti
                if premuti == 1:
                    tastop = event.key
                    # movimenti personaggio
                    if event.key == pygame.K_w:
                        npers = 3
                        pers = persw
                        arma = armaw
                        armatura = armaturaw
                        scudo = scudow
                        ny = -gpy
                        nx = 0
                        primopas = True
                    if event.key == pygame.K_a:
                        npers = 2
                        pers = persa
                        arma = armaa
                        armatura = armaturaa
                        scudo = scudoa
                        nx = -gpx
                        ny = 0
                        primopas = True
                    if event.key == pygame.K_s:
                        npers = 4
                        pers = perss
                        arma = armas
                        armatura = armaturas
                        scudo = scudos
                        ny = gpy
                        nx = 0
                        primopas = True
                    if event.key == pygame.K_d:
                        npers = 1
                        pers = persd
                        arma = armad
                        armatura = armaturad
                        scudo = scudod
                        nx = gpx
                        ny = 0
                        primopas = True
                    if event.key == pygame.K_e:
                        nx = 0
                        ny = 0
                        attacco = 1
                    if event.key == pygame.K_r:
                        nx = 0
                        ny = 0
                        primadifesa = True
                    if event.key == pygame.K_SPACE:
                        # apertura porte
                        k = 0
                        while k < len(porte):
                            if porte[k] == dati[1] and ((porte[k + 1] == x + gpx and porte[k + 2] == y and npers == 1) or (porte[k + 1] == x - gpx and porte[k + 2] == y and npers == 2) or (porte[k + 1] == x and porte[k + 2] == y + gpy and npers == 4) or (porte[k + 1] == x and porte[k + 2] == y - gpy and npers == 3)) and not porte[k + 3]:
                                suonoaperturacopo.play()
                                porte[k + 3] = True
                                # scoprire caselle viste
                                if True:
                                    # definire la cornice
                                    murx = x
                                    mury = y
                                    # imposto l'inizio del percorso
                                    arrivato = False
                                    while not arrivato:
                                        nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
                                        if mury != nmury:
                                            mury = nmury
                                        else:
                                            arrivato = True
                                    inimurx = murx
                                    inimury = mury
                                    andare = "d"
                                    finito = False
                                    c = 5
                                    while not finito:
                                        if c == 0:
                                            finito = True
                                        if inimurx == murx and inimury == mury:
                                            c = c - 1
                                        if andare == "d":
                                            # vado a destra
                                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                                            if murx != nmurx:
                                                i = 0
                                                while i < len(caseviste):
                                                    if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                                        caseviste[i + 2] = True
                                                        murx = nmurx
                                                        break
                                                    i = i + 3
                                            else:
                                                andare = "s"
                                            if andare == "d":
                                                andare = "w"
                                        if andare == "s":
                                            # vado in basso
                                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, numstanza, False, 0, True, False, porte, cofanetti)
                                            if mury != nmury:
                                                i = 0
                                                while i < len(caseviste):
                                                    if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                                        caseviste[i + 2] = True
                                                        mury = nmury
                                                        break
                                                    i = i + 3
                                            else:
                                                andare = "a"
                                            if andare == "s":
                                                andare = "d"
                                        if andare == "a":
                                            # vado a sinistra
                                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                                            if murx != nmurx:
                                                i = 0
                                                while i < len(caseviste):
                                                    if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                                        caseviste[i + 2] = True
                                                        murx = nmurx
                                                        break
                                                    i = i + 3
                                            else:
                                                andare = "w"
                                            if andare == "a":
                                                andare = "s"
                                        if andare == "w":
                                            # vado in alto
                                            nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
                                            if mury != nmury:
                                                i = 0
                                                while i < len(caseviste):
                                                    if caseviste[i] == nmurx and caseviste[i + 1] == nmury:
                                                        caseviste[i + 2] = True
                                                        mury = nmury
                                                        break
                                                    i = i + 3
                                            else:
                                                andare = "d"
                                            if andare == "w":
                                                andare = "a"
                                    casevisteprov = caseviste
                                    i = 0
                                    while i < len(caseviste):
                                        n = -1
                                        fine1 = False
                                        fine2 = False
                                        while n <= 28:
                                            if not fine1 and caseviste[i + 2]:
                                                murx = casevisteprov[i] + (gpx * n)
                                                mury = casevisteprov[i + 1]
                                                nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                                                if murx != nmurx:
                                                    j = 0
                                                    while j < len(casevisteprov):
                                                        if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                                            casevisteprov[j + 2] = True
                                                            break
                                                        j = j + 3
                                                else:
                                                    fine1 = True
                                            if not fine2 and caseviste[i + 2]:
                                                murx = casevisteprov[i] - (gpx * n)
                                                mury = casevisteprov[i + 1]
                                                nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, -gpx, 0, numstanza, False, 0, True, False, porte, cofanetti)
                                                if murx != nmurx:
                                                    j = 0
                                                    while j < len(casevisteprov):
                                                        if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                                            casevisteprov[j + 2] = True
                                                            break
                                                        j = j + 3
                                                else:
                                                    fine2 = True
                                            n = n + 1
                                        n = 0
                                        fine1 = False
                                        fine2 = False
                                        while n <= 14:
                                            if not fine1 and caseviste[i + 2]:
                                                murx = casevisteprov[i]
                                                mury = casevisteprov[i + 1] + (gpy * n)
                                                nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, gpy, numstanza, False, 0, True, False, porte, cofanetti)
                                                if mury != nmury:
                                                    j = 0
                                                    while j < len(casevisteprov):
                                                        if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                                            casevisteprov[j + 2] = True
                                                            break
                                                        j = j + 3
                                                else:
                                                    fine1 = True
                                            if not fine2 and caseviste[i + 2]:
                                                murx = casevisteprov[i]
                                                mury = casevisteprov[i + 1] - (gpy * n)
                                                nmurx, nmury, stanza, carim, muovi, cambiosta = muri_porte(murx, mury, 0, -gpy, numstanza, False, 0, True, False, porte, cofanetti)
                                                if mury != nmury:
                                                    j = 0
                                                    while j < len(casevisteprov):
                                                        if casevisteprov[j] == nmurx and casevisteprov[j + 1] == nmury:
                                                            casevisteprov[j + 2] = True
                                                            break
                                                        j = j + 3
                                                else:
                                                    fine2 = True
                                            n = n + 1
                                        i = i + 3
                                    caseviste = casevisteprov
                                caricaini = True
                                # aggiornare vettore tutteporte
                                j = 0
                                while j < len(tutteporte):
                                    if tutteporte[j] == porte[k] and tutteporte[j + 1] == porte[k + 1] and tutteporte[j + 2] == porte[k + 2]:
                                        tutteporte[j + 3] = True
                                    j = j + 4
                            k = k + 4
                        # apertura cofanetti
                        i = 0
                        while i < len(cofanetti):
                            if cofanetti[i] == dati[1] and ((cofanetti[i + 1] == x + gpx and cofanetti[i + 2] == y and npers == 1) or (cofanetti[i + 1] == x - gpx and cofanetti[i + 2] == y and npers == 2) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y + gpy and npers == 4) or (cofanetti[i + 1] == x and cofanetti[i + 2] == y - gpy and npers == 3)) and not cofanetti[i + 3]:
                                suonoaperturacopo.play()
                                dati, tesoro = aperturacofanetto(cofanetti[i], cofanetti[i + 1], cofanetti[i + 2], dati)
                                cofanetti[i + 3] = True
                                caricaini = True
                                # aggiornare vettore tutticofanetti
                                j = 0
                                while j < len(tutticofanetti):
                                    if tutticofanetti[j] == cofanetti[i] and tutticofanetti[j + 1] == cofanetti[i + 1] and tutticofanetti[j + 2] == cofanetti[i + 2]:
                                        tutticofanetti[j + 3] = True
                                    j = j + 4
                            i = i + 4

                # menu start
                if event.key == pygame.K_ESCAPE:
                    startf = True

            if event.type == pygame.KEYUP:
                if premuti > 0:
                    premuti = premuti - 1
                if premuti == 0:
                    nx = 0
                    ny = 0
                    primopas = False
                    tastotemp = 5
                    tastotempfps = 5
                    tastop = 0

        # statistiche personaggio e robo (liv + arm + scu)
        # se modifichi -> modifica anche equip, equiprobo e ovunque si presenta pvtot
        if True:
            esptot = pow(dati[4], 2) + (dati[4] * 10)
            pvtot = 100 + (dati[4] * 5)
            entot = 300 + (dati[9] * 100)
            att = 10 + (dati[4] * 2) + (dati[6] * 10)
            dif = 10 + (dati[4] * 2) + (dati[8] * 10) + 5 + (dati[7] * 5)
            difro = 10 + (dati[9] * 10)
            par = 3 + (dati[7] * 3)

        # ripristina vita e status dopo lv up
        if aumentoliv:
            dati[5] = pvtot
            dati[121] = False
            aumentoliv = False

        # togliere il rumore della camminata
        if ((tastop != pygame.K_w) and (tastop != pygame.K_a) and (tastop != pygame.K_s) and (tastop != pygame.K_d)) or (dati[5] <= 0):
            rumorecamminata.stop()
            primopasso = True

        # menu start
        if startf == True and attacco != 1:
            selsta.play()
            dati[2] = x
            dati[3] = y
            dati, inizio, attacco = start(dati, nmost, porteini, portefin, cofaniini, cofanifin, tutteporte, tutticofanetti, apriocchio)
            if attacco != 0:
                contattogg = 1
            carim = True
            startf = False

        # morte tua e di robo
        if dati[5] <= 0:
            schermo.fill(grigioscu)
            messaggio("Sei morto", grigiochi, gsx // 32 * 3, gsy // 18 * 13, 150)
            pygame.display.update()
            continua = False
            while continua == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        selind.play()
                        continua = True
            inizio = True
        if dati[10] <= 0:
            morterob = True
            dati[122] = 0
            dati[125] = 0
            dati[126] = 0
        else:
            morterob = False

        # movimento-azioni personaggio
        if (nx != 0 or ny != 0) and muovimosta <= 0 and muovimostb <= 0 and muovimostc <= 0 and muovimostd <= 0 and muovimoste <= 0 and muovimostf <= 0 and muovimostg <= 0 and muovimosth <= 0 and muovimosti <= 0 and muovimostl <= 0 and muovirob <= 0:
            # progresso - stanza - x - y - liv - pv - arma - scudo - armatura - armrob - energiarob - tecniche(20) - oggetti(50) - condizioni(20) - gambit(20) - veleno - surriscalda // dimensione: 0-122
            vx = x
            vy = y
            sposta = True
            x, y, dati[1], carim, inutile, cambiosta = muri_porte(x, y, nx, ny, dati[1], carim, 0, False, False, porte, cofanetti)
        # gestione attacchi
        if attacco != 0 and attacco <= 6 and contattogg == 0:
            pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, sposta, creaesca, xesca, yesca, statoma, statomb, statomc, statomd, statome, statomf, statomg, statomh, statomi, statoml, npers, nrob = attacca(x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126],
                                                                                                                                                                                                                  stanzaa, dati[1], sfondinoa, sfondinob, sfondinoc, arma, armatura, scudo, robot, armrob,
                                                                                                                                                                                                                  nemicoa, mxa, mya, nemicob, mxb, myb, nemicoc, mxc, myc, nemicod, mxd, myd, nemicoe, mxe, mye,
                                                                                                                                                                                                                  nemicof, mxf, myf, nemicog, mxg, myg, nemicoh, mxh, myh, nemicoi, mxi, myi, nemicol, mxl, myl,
                                                                                                                                                                                                                  pvmatot, pvmbtot, pvmctot, pvmdtot, pvmetot, pvmftot, pvmgtot, pvmhtot, pvmitot, pvmltot,
                                                                                                                                                                                                                  pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, statoma, statomb, statomc, statomd,
                                                                                                                                                                                                                  statome, statomf, statomg, statomh, statomi, statoml, raggiovistaa, raggiovistab, raggiovistac,
                                                                                                                                                                                                                  raggiovistad, raggiovistae, raggiovistaf, raggiovistag, raggiovistah, raggiovistai, raggiovistal,
                                                                                                                                                                                                                  att, attacco, vitaesca, porte, cofanetti, caseviste, apriocchio)
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
        difesa = False
        if tastop == pygame.K_r and not sposta:
            difesa = True
        if difesa:
            par = par * 2
            dif = dif + dif // 2
            if primadifesa:
                sposta = True
                primadifesa = False
                dati[5] = dati[5] + 3
                if dati[5] > pvtot:
                    dati[5] = pvtot
        # gestione att+, dif+
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
            dati[125] = 0
            dati[126] = 0
        if rx == x and ry == y:
            x = vx
            y = vy
        if ((sposta and muovirob <= 0) or muovirob > 0) and not morterob:
            if vistoa or vistob or vistoc or vistod or vistoe or vistof or vistog or vistoh or vistoi or vistol:
                vistorob = True
            else:
                vistorob = False
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
                if muovirob == 1 or muovirob == -1:
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
            rx, ry, muovirob, nrob, vistorob, dati = movrobo(x, y, vx, vy, rx, ry, dati[1], muovirob, vistorob, dati, porte, cofanetti)

            if muovirob < 0:
                rx = vrx
                ry = vry
                nrob = 0
            if (rx == mxa and ry == mya) or (rx == mxb and ry == myb) or (rx == mxc and ry == myc) or (rx == mxd and ry == myd) or (rx == mxe and ry == mye) or (rx == mxf and ry == myf) or (rx == mxg and ry == myg) or (rx == mxh and ry == myh) or (rx == mxi and ry == myi) or (rx == mxl and ry == myl):
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
            pvma, pvmb, pvmc, pvmd, pvme, pvmf, pvmg, pvmh, pvmi, pvml, sposta, creaesca, xesca, yesca, statoma, statomb, statomc, statomd, statome, statomf, statomg, statomh, statomi, statoml, npers, nrob = attacca(
                x, y, npers, nrob, rx, ry, pers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122],
                dati[125], dati[126],
                stanzaa, dati[1], sfondinoa, sfondinob, arma, armatura, scudo, robot, armrob,
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
            # controlli mostri per personaggio durante il cammino
            if mxa == x and mya == y:
                x = vx
                y = vy
            if mxb == x and myb == y:
                x = vx
                y = vy
            if mxc == x and myc == y:
                x = vx
                y = vy
            if mxd == x and myd == y:
                x = vx
                y = vy
            if mxe == x and mye == y:
                x = vx
                y = vy
            if mxf == x and myf == y:
                x = vx
                y = vy
            if mxg == x and myg == y:
                x = vx
                y = vy
            if mxh == x and myh == y:
                x = vx
                y = vy
            if mxi == x and myi == y:
                x = vx
                y = vy
            if mxl == x and myl == y:
                x = vx
                y = vy
            # controlli personaggio per robo durante il cammino
            if rx == x and ry == y:
                rx = vrx
                ry = vry
            # controlli mostri per robo durante il cammino
            if mxa == rx and mya == ry:
                rx = vrx
                ry = vry
            if mxb == rx and myb == ry:
                rx = vrx
                ry = vry
            if mxc == rx and myc == ry:
                rx = vrx
                ry = vry
            if mxd == rx and myd == ry:
                rx = vrx
                ry = vry
            if mxe == rx and mye == ry:
                rx = vrx
                ry = vry
            if mxf == rx and myf == ry:
                rx = vrx
                ry = vry
            if mxg == rx and myg == ry:
                rx = vrx
                ry = vry
            if mxh == rx and myh == ry:
                rx = vrx
                ry = vry
            if mxi == rx and myi == ry:
                rx = vrx
                ry = vry
            if mxl == rx and myl == ry:
                rx = vrx
                ry = vry
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
            if ((muovimosta > 0 or (sposta and muovimosta <= 0)) and pvma > 0) or (primociclo and nemicoa):
                mxav = mxa
                myav = mya
                if primociclo:
                    mxaprimociclo = mxa
                    myaprimociclo = mya
                    muovimostaprimociclo = muovimosta
                    datiprimociclo = dati
                mxa, mya, muovimosta, nmos, vistoa, dati, vitaesca, raggiovistaa = movmostro(x, y, rx, ry, mxa, mya, dati[1], tipoa, muovimosta, vistoa, dif, difro, par, dati, statoma, vitaesca, porte, cofanetti)
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
                mxa = 0
                mya = 0
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
            if ((muovimostb > 0 or (sposta and muovimostb <= 0)) and pvmb > 0) or (primociclo and nemicob):
                mxbv = mxb
                mybv = myb
                if primociclo:
                    mxbprimociclo = mxb
                    mybprimociclo = myb
                    muovimostbprimociclo = muovimostb
                    datiprimociclo = dati
                mxb, myb, muovimostb, nmos, vistob, dati, vitaesca, raggiovistab = movmostro(x, y, rx, ry, mxb, myb, dati[1], tipob, muovimostb, vistob, dif, difro, par, dati, statomb, vitaesca, porte, cofanetti)
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
                mxb = 0
                myb = 0
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
            if ((muovimostc > 0 or (sposta and muovimostc <= 0)) and pvmc > 0) or (primociclo and nemicoc):
                mxcv = mxc
                mycv = myc
                if primociclo:
                    mxcprimociclo = mxc
                    mycprimociclo = myc
                    muovimostcprimociclo = muovimostc
                    datiprimociclo = dati
                mxc, myc, muovimostc, nmos, vistoc, dati, vitaesca, raggiovistac = movmostro(x, y, rx, ry, mxc, myc, dati[1], tipoc, muovimostc, vistoc, dif, difro, par, dati, statomc, vitaesca, porte, cofanetti)
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
                mxc = 0
                myc = 0
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
            if ((muovimostd > 0 or (sposta and muovimostd <= 0)) and pvmd > 0) or (primociclo and nemicod):
                mxdv = mxd
                mydv = myd
                if primociclo:
                    mxdprimociclo = mxd
                    mydprimociclo = myd
                    muovimostdprimociclo = muovimostd
                    datiprimociclo = dati
                mxd, myd, muovimostd, nmos, vistod, dati, vitaesca, raggiovistad = movmostro(x, y, rx, ry, mxd, myd, dati[1], tipod, muovimostd, vistod, dif, difro, par, dati, statomd, vitaesca, porte, cofanetti)
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
                mxd = 0
                myd = 0
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
            if ((muovimoste > 0 or (sposta and muovimoste <= 0)) and pvme > 0) or (primociclo and nemicoe):
                mxev = mxe
                myev = mye
                if primociclo:
                    mxeprimociclo = mxe
                    myeprimociclo = mye
                    muovimosteprimociclo = muovimoste
                    datiprimociclo = dati
                mxe, mye, muovimoste, nmos, vistoe, dati, vitaesca, raggiovistae = movmostro(x, y, rx, ry, mxe, mye, dati[1], tipoe, muovimoste, vistoe, dif, difro, par, dati, statome, vitaesca, porte, cofanetti)
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
                mxe = 0
                mye = 0
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
            if ((muovimostf > 0 or (sposta and muovimostf <= 0)) and pvmf > 0) or (primociclo and nemicof):
                mxfv = mxf
                myfv = myf
                if primociclo:
                    mxfprimociclo = mxf
                    myfprimociclo = myf
                    muovimostfprimociclo = muovimostf
                    datiprimociclo = dati
                mxf, myf, muovimostf, nmos, vistof, dati, vitaesca, raggiovistaf = movmostro(x, y, rx, ry, mxf, myf, dati[1], tipof, muovimostf, vistof, dif, difro, par, dati, statomf, vitaesca, porte, cofanetti)
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
                mxf = 0
                myf = 0
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
            if ((muovimostg > 0 or (sposta and muovimostg <= 0)) and pvmg > 0) or (primociclo and nemicog):
                mxgv = mxg
                mygv = myg
                if primociclo:
                    mxgprimociclo = mxg
                    mygprimociclo = myg
                    muovimostgprimociclo = muovimostg
                    datiprimociclo = dati
                mxg, myg, muovimostg, nmos, vistog, dati, vitaesca, raggiovistag = movmostro(x, y, rx, ry, mxg, myg, dati[1], tipog, muovimostg, vistog, dif, difro, par, dati, statomg, vitaesca, porte, cofanetti)
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
                mxg = 0
                myg = 0
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
            if ((muovimosth > 0 or (sposta and muovimosth <= 0)) and pvmh > 0) or (primociclo and nemicoh):
                mxhv = mxh
                myhv = myh
                if primociclo:
                    mxhprimociclo = mxh
                    myhprimociclo = myh
                    muovimosthprimociclo = muovimosth
                    datiprimociclo = dati
                mxh, myh, muovimosth, nmos, vistoh, dati, vitaesca, raggiovistah = movmostro(x, y, rx, ry, mxh, myh, dati[1], tipoh, muovimosth, vistoh, dif, difro, par, dati, statomh, vitaesca, porte, cofanetti)
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
                mxh = 0
                myh = 0
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
            if ((muovimosti > 0 or (sposta and muovimosti <= 0)) and pvmi > 0) or (primociclo and nemicoi):
                mxiv = mxi
                myiv = myi
                if primociclo:
                    mxiprimociclo = mxi
                    myiprimociclo = myi
                    muovimostiprimociclo = muovimosti
                    datiprimociclo = dati
                mxi, myi, muovimosti, nmos, vistoi, dati, vitaesca, raggiovistai = movmostro(x, y, rx, ry, mxi, myi, dati[1], tipoi, muovimosti, vistoi, dif, difro, par, dati, statomi, vitaesca, porte, cofanetti)
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
                mxi = 0
                myi = 0
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
            if ((muovimostl > 0 or (sposta and muovimostl <= 0)) and pvml > 0) or (primociclo and nemicol):
                mxlv = mxl
                mylv = myl
                if primociclo:
                    mxlprimociclo = mxl
                    mylprimociclo = myl
                    muovimostlprimociclo = muovimostl
                    datiprimociclo = dati
                mxl, myl, muovimostl, nmos, vistol, dati, vitaesca, raggiovistal = movmostro(x, y, rx, ry, mxl, myl, dati[1], tipol, muovimostl, vistol, dif, difro, par, dati, statoml, vitaesca, porte, cofanetti)
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
                mxl = 0
                myl = 0
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

        # aggiorna vista dei mostri e metti l'occhio se ti vedono
        if True:
            if nemicoa != 0:
                inutile, inutile, inutile, inutile, vistoa, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxa, mya,
                                                                                                  dati[1], tipoa, -5,
                                                                                                  vistoa, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicob != 0:
                inutile, inutile, inutile, inutile, vistob, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxb, myb,
                                                                                                  dati[1], tipob, -5,
                                                                                                  vistob, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicoc != 0:
                inutile, inutile, inutile, inutile, vistoc, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxc, myc,
                                                                                                  dati[1], tipoc, -5,
                                                                                                  vistoc, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicod != 0:
                inutile, inutile, inutile, inutile, vistod, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxd, myd,
                                                                                                  dati[1], tipod, -5,
                                                                                                  vistod, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicoe != 0:
                inutile, inutile, inutile, inutile, vistoe, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxe, mye,
                                                                                                  dati[1], tipoe, -5,
                                                                                                  vistoe, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicof != 0:
                inutile, inutile, inutile, inutile, vistof, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxf, myf,
                                                                                                  dati[1], tipof, -5,
                                                                                                  vistof, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicog != 0:
                inutile, inutile, inutile, inutile, vistog, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxg, myg,
                                                                                                  dati[1], tipog, -5,
                                                                                                  vistog, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicoh != 0:
                inutile, inutile, inutile, inutile, vistoh, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxh, myh,
                                                                                                  dati[1], tipoh, -5,
                                                                                                  vistoh, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicoi != 0:
                inutile, inutile, inutile, inutile, vistoi, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxi, myi,
                                                                                                  dati[1], tipoi, -5,
                                                                                                  vistoi, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
            if nemicol != 0:
                inutile, inutile, inutile, inutile, vistol, inutile, inutile, inutile = movmostro(x, y, rx, ry, mxl, myl,
                                                                                                  dati[1], tipol, -5,
                                                                                                  vistol, dif, difro, par,
                                                                                                  dati, 0, vitaesca,
                                                                                                  porte, cofanetti)
        if vistoa or vistob or vistoc or vistod or vistoe or vistof or vistog or vistoh or vistoi or vistol:
            apriocchio = True
        else:
            apriocchio = False

        # aumentare di livello
        if dati[127] >= esptot and dati[4] < 100 and not carim and not inizio:
            dati[4] = dati[4] + 1
            dati[127] = dati[127] - esptot
            aumentoliv = True

        # animazione camminata personaggio
        if sposta and not inizio:
            # le animazioni fanno un frame in piu' all'inizio per stabilizzare il framerate
            # mentre ci si sposta
            if x != vx or y != vy:
                if primopasso and not cambiosta:
                    rumorecamminata.play(-1)
                    primopasso = False
                # camminata quando si entra in una stanza
                if cambiosta:
                    fineanimaz = 1
                    while fineanimaz > 0:
                        n = 0
                        while fineanimaz == 1 and n < 32:
                            if x == gpx * n:
                                m = 0
                                while m < 18:
                                    if y == gpy * m:
                                        if (n + m) % 2 == 0:
                                            schermo.blit(sfondinob, (vx, vy))
                                        if (n + m) % 2 != 0:
                                            schermo.blit(sfondinoa, (vx, vy))
                                    m = m + 1
                            n = n + 1
                        if fineanimaz == 1:
                            rumorecamminata.stop()
                            rumorecamminata.play()
                            if npers == 1:
                                schermo.blit(scudo, (vx + (gpx // 3), y))
                                schermo.blit(persdm, (vx + (gpx // 3), y))
                                schermo.blit(armatura, (vx + (gpx // 3), y))
                                schermo.blit(persdmb1, (vx + (gpx // 3), y))
                                schermo.blit(arma, (vx + (gpx // 3), y))
                            if npers == 2:
                                schermo.blit(arma, (vx - (gpx // 3), y))
                                schermo.blit(persam, (vx - (gpx // 3), y))
                                schermo.blit(armatura, (vx - (gpx // 3), y))
                                schermo.blit(persamb1, (vx - (gpx // 3), y))
                                schermo.blit(scudo, (vx - (gpx // 3), y))
                            if npers == 3:
                                schermo.blit(arma, (x, vy - (gpy // 3)))
                                schermo.blit(scudo, (x, vy - (gpy // 3)))
                                schermo.blit(perswm, (x, vy - (gpy // 3)))
                                schermo.blit(armatura, (x, vy - (gpy // 3)))
                                schermo.blit(perswmb1, (x, vy - (gpy // 3)))
                            if npers == 4:
                                schermo.blit(perssm, (x, vy + (gpy // 3)))
                                schermo.blit(armatura, (x, vy + (gpy // 3)))
                                schermo.blit(perssmb1, (x, vy + (gpy // 3)))
                                schermo.blit(arma, (x, vy + (gpy // 3)))
                                schermo.blit(scudo, (x, vy + (gpy // 3)))
                        fineanimaz = fineanimaz - 1
                        pygame.display.update()
                        clock.tick(fpsanimazioni)
                        pygame.display.update()
                # camminata quando non si entra in una stanza
                if not cambiosta:
                    fineanimaz = 2
                    while fineanimaz != 0:
                        n = 0
                        while fineanimaz <= 2 and n < 32:
                            if x == gpx * n:
                                m = 0
                                while m < 18:
                                    if y == gpy * m:
                                        if (n + m) % 2 == 0:
                                            schermo.blit(sfondinoa, (x, y))
                                            schermo.blit(sfondinob, (vx, vy))
                                        if (n + m) % 2 != 0:
                                            schermo.blit(sfondinob, (x, y))
                                            schermo.blit(sfondinoa, (vx, vy))
                                    m = m + 1
                            n = n + 1
                        if npers == 1:
                            if fineanimaz == 2:
                                schermo.blit(scudo, (vx + (gpx // 3), y))
                                schermo.blit(persdm, (vx + (gpx // 3), y))
                                schermo.blit(armatura, (vx + (gpx // 3), y))
                                schermo.blit(persdmb1, (vx + (gpx // 3), y))
                                schermo.blit(arma, (vx + (gpx // 3), y))
                            if fineanimaz == 1:
                                schermo.blit(scudo, (vx + (gpx * 2 // 3), y))
                                schermo.blit(persdm, (vx + (gpx * 2 // 3), y))
                                schermo.blit(armatura, (vx + (gpx * 2 // 3), y))
                                schermo.blit(persdmb2, (vx + (gpx * 2 // 3), y))
                                schermo.blit(arma, (vx + (gpx * 2 // 3), y))
                        if npers == 2:
                            if fineanimaz == 2:
                                schermo.blit(arma, (vx - (gpx // 3), y))
                                schermo.blit(persam, (vx - (gpx // 3), y))
                                schermo.blit(armatura, (vx - (gpx // 3), y))
                                schermo.blit(persamb1, (vx - (gpx // 3), y))
                                schermo.blit(scudo, (vx - (gpx // 3), y))
                            if fineanimaz == 1:
                                schermo.blit(arma, (vx - (gpx * 2 // 3), y))
                                schermo.blit(persam, (vx - (gpx * 2 // 3), y))
                                schermo.blit(armatura, (vx - (gpx * 2 // 3), y))
                                schermo.blit(persamb2, (vx - (gpx * 2 // 3), y))
                                schermo.blit(scudo, (vx - (gpx * 2 // 3), y))
                        if npers == 3:
                            if fineanimaz == 2:
                                schermo.blit(arma, (x, vy - (gpy // 3)))
                                schermo.blit(scudo, (x, vy - (gpy // 3)))
                                schermo.blit(perswm, (x, vy - (gpy // 3)))
                                schermo.blit(armatura, (x, vy - (gpy // 3)))
                                schermo.blit(perswmb1, (x, vy - (gpy // 3)))
                            if fineanimaz == 1:
                                schermo.blit(arma, (x, vy - (gpy * 2 // 3)))
                                schermo.blit(scudo, (x, vy - (gpy * 2 // 3)))
                                schermo.blit(perswm, (x, vy - (gpy * 2 // 3)))
                                schermo.blit(armatura, (x, vy - (gpy * 2 // 3)))
                                schermo.blit(perswmb2, (x, vy - (gpy * 2 // 3)))
                        if npers == 4:
                            if fineanimaz == 2:
                                schermo.blit(perssm, (x, vy + (gpy // 3)))
                                schermo.blit(armatura, (x, vy + (gpy // 3)))
                                schermo.blit(perssmb1, (x, vy + (gpy // 3)))
                                schermo.blit(arma, (x, vy + (gpy // 3)))
                                schermo.blit(scudo, (x, vy + (gpy // 3)))
                            if fineanimaz == 1:
                                schermo.blit(perssm, (x, vy + (gpy * 2 // 3)))
                                schermo.blit(armatura, (x, vy + (gpy * 2 // 3)))
                                schermo.blit(perssmb2, (x, vy + (gpy * 2 // 3)))
                                schermo.blit(arma, (x, vy + (gpy * 2 // 3)))
                                schermo.blit(scudo, (x, vy + (gpy * 2 // 3)))
                        pygame.display.update()
                        clock.tick(fpsanimazioni)
                        fineanimaz = fineanimaz - 1
                    n = 0
                    while n < 32:
                        if x == gpx * n:
                            m = 0
                            while m < 18:
                                if y == gpy * m:
                                    if (n + m) % 2 == 0:
                                        schermo.blit(sfondinoa, (x, y))
                                        schermo.blit(sfondinob, (vx, vy))
                                    if (n + m) % 2 != 0:
                                        schermo.blit(sfondinob, (x, y))
                                        schermo.blit(sfondinoa, (vx, vy))
                                m = m + 1
                        n = n + 1
            # mentre non ci si sposta
            elif attacco == 0 and not difesa:
                if primopasso:
                    rumorecamminata.play(-1)
                    primopasso = False
                fineanimaz = 2
                while fineanimaz != 0:
                    n = 0
                    while fineanimaz <= 2 and n < 32:
                        if x == gpx * n:
                            m = 0
                            while m < 18:
                                if y == gpy * m:
                                    if (n + m) % 2 == 0:
                                        schermo.blit(sfondinoa, (x, y))
                                    if (n + m) % 2 != 0:
                                        schermo.blit(sfondinob, (x, y))
                                m = m + 1
                        n = n + 1
                    if npers == 1:
                        if fineanimaz == 2:
                            schermo.blit(scudo, (vx, y))
                            schermo.blit(persdm, (vx, y))
                            schermo.blit(armatura, (vx, y))
                            schermo.blit(persdmb1, (vx, y))
                            schermo.blit(arma, (vx, y))
                        if fineanimaz == 1:
                            schermo.blit(scudo, (vx, y))
                            schermo.blit(persdm, (vx, y))
                            schermo.blit(armatura, (vx, y))
                            schermo.blit(persdmb2, (vx, y))
                            schermo.blit(arma, (vx, y))
                    if npers == 2:
                        if fineanimaz == 2:
                            schermo.blit(arma, (vx, y))
                            schermo.blit(persam, (vx, y))
                            schermo.blit(armatura, (vx, y))
                            schermo.blit(persamb1, (vx, y))
                            schermo.blit(scudo, (vx, y))
                        if fineanimaz == 1:
                            schermo.blit(arma, (vx, y))
                            schermo.blit(persam, (vx, y))
                            schermo.blit(armatura, (vx, y))
                            schermo.blit(persamb2, (vx, y))
                            schermo.blit(scudo, (vx, y))
                    if npers == 3:
                        if fineanimaz == 2:
                            schermo.blit(arma, (x, vy))
                            schermo.blit(scudo, (x, vy))
                            schermo.blit(perswm, (x, vy))
                            schermo.blit(armatura, (x, vy))
                            schermo.blit(perswmb1, (x, vy))
                        if fineanimaz == 1:
                            schermo.blit(arma, (x, vy))
                            schermo.blit(scudo, (x, vy))
                            schermo.blit(perswm, (x, vy))
                            schermo.blit(armatura, (x, vy))
                            schermo.blit(perswmb2, (x, vy))
                    if npers == 4:
                        if fineanimaz == 2:
                            schermo.blit(perssm, (x, vy))
                            schermo.blit(armatura, (x, vy))
                            schermo.blit(perssmb1, (x, vy))
                            schermo.blit(arma, (x, vy))
                            schermo.blit(scudo, (x, vy))
                        if fineanimaz == 1:
                            schermo.blit(perssm, (x, vy))
                            schermo.blit(armatura, (x, vy))
                            schermo.blit(perssmb2, (x, vy))
                            schermo.blit(arma, (x, vy))
                            schermo.blit(scudo, (x, vy))
                    pygame.display.update()
                    clock.tick(fpsanimazioni)
                    fineanimaz = fineanimaz - 1

        sposta = False

        # disegnare gli sfondi e personaggi
        if not carim and not inizio:
            ambiente_movimento(x, y, npers, dati[5], pvtot, dati[121], dati[123], dati[124], dati[10], entot, dati[122], dati[125], dati[126], vx, vy, rx, ry, vrx, vry, pers,
                               stanzaa, sfondinoa, sfondinob, sfondinoc, arma, armatura, scudo, robot, armrob, nemicoa, mxa, mya, mxav, myav, nemicob, mxb, myb, mxbv, mybv,
                               nemicoc, mxc, myc, mxcv, mycv, nemicod, mxd, myd, mxdv, mydv, nemicoe, mxe, mye, mxev, myev, nemicof, mxf, myf, mxfv, myfv,
                               nemicog, mxg, myg, mxgv, mygv, nemicoh, mxh, myh, mxhv, myhv, nemicoi, mxi, myi, mxiv, myiv, nemicol, mxl, myl, mxlv, mylv,
                               mortoa, mortob, mortoc, mortod, mortoe, mortof, mortog, mortoh, mortoi, mortol, caricaini, vitaesca, porte, cofanetti, caseviste, apriocchio)

        # animazione aumento di livello
        if aumentoliv and not carim and not inizio:
            rumorecamminata.stop()
            rumorelevelup.play()
            # le animazioni fanno un frame in piu' all'inizio per stabilizzare il framerate
            fineanimaz = 4
            while fineanimaz != -1:
                n = 0
                while fineanimaz <= 3 and n < 32:
                    if x == gpx * n:
                        m = 0
                        while m < 18:
                            if y == gpy * m:
                                if (n + m) % 2 == 0:
                                    schermo.blit(sfondinoa, (x, y))
                                if (n + m) % 2 != 0:
                                    schermo.blit(sfondinob, (x, y))
                            m = m + 1
                    n = n + 1
                if npers == 1:
                    schermo.blit(scudo, (x, y))
                    schermo.blit(pers, (x, y))
                    schermo.blit(armatura, (x, y))
                    schermo.blit(persdb, (x, y))
                    schermo.blit(arma, (x, y))
                    if fineanimaz == 0:
                        schermo.blit(saliliv, (x, y))
                    if fineanimaz == 1:
                        schermo.blit(saliliv1, (x, y))
                    if fineanimaz == 2:
                        schermo.blit(saliliv2, (x, y))
                    if fineanimaz == 3:
                        schermo.blit(saliliv3, (x, y))
                if npers == 2:
                    schermo.blit(arma, (x, y))
                    schermo.blit(pers, (x, y))
                    schermo.blit(armatura, (x, y))
                    schermo.blit(persab, (x, y))
                    schermo.blit(scudo, (x, y))
                    if fineanimaz == 0:
                        schermo.blit(saliliv, (x, y))
                    if fineanimaz == 1:
                        schermo.blit(saliliv1, (x, y))
                    if fineanimaz == 2:
                        schermo.blit(saliliv2, (x, y))
                    if fineanimaz == 3:
                        schermo.blit(saliliv3, (x, y))
                if npers == 3:
                    schermo.blit(arma, (x, y))
                    schermo.blit(scudo, (x, y))
                    schermo.blit(pers, (x, y))
                    schermo.blit(armatura, (x, y))
                    schermo.blit(perswb, (x, y))
                    if fineanimaz == 0:
                        schermo.blit(saliliv, (x, y))
                    if fineanimaz == 1:
                        schermo.blit(saliliv1, (x, y))
                    if fineanimaz == 2:
                        schermo.blit(saliliv2, (x, y))
                    if fineanimaz == 3:
                        schermo.blit(saliliv3, (x, y))
                if npers == 4:
                    schermo.blit(pers, (x, y))
                    schermo.blit(armatura, (x, y))
                    schermo.blit(perssb, (x, y))
                    schermo.blit(arma, (x, y))
                    schermo.blit(scudo, (x, y))
                    if fineanimaz == 0:
                        schermo.blit(saliliv, (x, y))
                    if fineanimaz == 1:
                        schermo.blit(saliliv1, (x, y))
                    if fineanimaz == 2:
                        schermo.blit(saliliv2, (x, y))
                    if fineanimaz == 3:
                        schermo.blit(saliliv3, (x, y))
                pygame.display.update()
                clock.tick(fpsanimazioni)
                if fineanimaz == 0:
                    pygame.time.wait(1000)
                fineanimaz = fineanimaz - 1

        caricaini = False

        # animazione apertura cofanetto
        if tesoro != -1:
            schermo.blit(sfocontcof, (gsx // 32 * 0, gsy // 18 * 0))
            # 31-40 -> oggetti(10) / 41-70 -> armi(30) / 71-80 -> batterie(10) / 81-100 -> condizioni(20) / 101-120 -> gambit (=celle di memoria)(20)
            if tesoro >= 11 and tesoro <= 30:
                messaggio("Hai trovato: Una nuova tecnica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 31:
                messaggio("Hai trovato: Pozione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 32:
                messaggio("Hai trovato: Caricabatterie", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 33:
                messaggio("Hai trovato: Bomba", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 34:
                messaggio("Hai trovato: Medicina", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 35:
                messaggio("Hai trovato: Bomba velenosa", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 36:
                messaggio("Hai trovato: Esca", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 37:
                messaggio("Hai trovato: Superpozione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 38:
                messaggio("Hai trovato: Caricabatterie migliorato", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 39:
                messaggio("Hai trovato: Bomba appiccicosa", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 40:
                messaggio("Hai trovato: Bomba potenziata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 41:
                messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 42:
                messaggio("Hai trovato: Spada di legno", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 43:
                messaggio("Hai trovato: Spada di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 44:
                messaggio("Hai trovato: Spadone d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 45:
                messaggio("Hai trovato: Spada del toro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 46:
                messaggio("Hai trovato: Spada di diamante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 47:
                messaggio("Hai trovato: Excalibur", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 48:
                messaggio("Hai trovato: Lykother", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 49:
                messaggio("Hai trovato: Sinego", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 50:
                messaggio("Hai trovato: Mendaxritas", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 51:
                messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 52:
                messaggio("Hai trovato: Armatura di pelle", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 53:
                messaggio("Hai trovato: Armatura di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 54:
                messaggio("Hai trovato: Armatura d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 55:
                messaggio("Hai trovato: Armatura del toro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 56:
                messaggio("Hai trovato: Armatura di diamante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 57:
                messaggio("Hai trovato: Armatura leggendaria", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 58:
                messaggio("Hai trovato: Lykodes", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 59:
                messaggio("Hai trovato: Armatura antica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 60:
                messaggio("Hai trovato: Loriquam", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 61:
                messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 62:
                messaggio("Hai trovato: Scudo di pelle", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 63:
                messaggio("Hai trovato: Scudo di ferro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 64:
                messaggio("Hai trovato: Scudo d'acciaio", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 65:
                messaggio("Hai trovato: Scudo del toro", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 66:
                messaggio("Hai trovato: Scudo di diamante", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 67:
                messaggio("Hai trovato: Scudo leggentario", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 68:
                messaggio("Hai trovato: Lykethmos", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 69:
                messaggio("Hai trovato: Scudo antico", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 70:
                messaggio("Hai trovato: Clipequam", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 71:
                messaggio("Hai trovato: Niente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 72:
                messaggio("Hai trovato: Batteria scarica", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 73:
                messaggio("Hai trovato: Batteria piccola", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 74:
                messaggio("Hai trovato: Batteria media", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 75:
                messaggio("Hai trovato: Batteria grande", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 76:
                messaggio("Hai trovato: Batteria discreta", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 77:
                messaggio("Hai trovato: Batteria affidabile", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 78:
                messaggio("Hai trovato: Batteria extra", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 79:
                messaggio("Hai trovato: Batteria efficiente", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro == 80:
                messaggio("Hai trovato: Batteria illimitata", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro >= 81 and tesoro <= 100:
                messaggio("Hai trovato: Una nuova condizione", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            if tesoro >= 101 and tesoro <= 120:
                messaggio("Hai trovato: Cella di memoria", grigiochi, gsx // 32 * 1, gsy // 18 * 1, 60)
            pygame.display.update()
            pygame.time.wait(500)
            risposta = False
            while not risposta:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            selezione.play()
                            risposta = True
            caricaini = True
            tesoro = -1

        vx = x
        vy = y
        if contattogg != 1:
            attacco = 0

        # togiere la morte ai mostri
        if True:
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
