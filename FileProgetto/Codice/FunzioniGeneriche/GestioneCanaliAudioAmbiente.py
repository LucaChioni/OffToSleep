# -*- coding: utf-8 -*-

import pygame


class CanaliAudioAmbiente(object):

    def __init__(self, maxCanaliAudio, numCanaleAudioAttuale):
        self.maxCanaliAudio = maxCanaliAudio
        self.numUltimoCanaleAudioUsato = numCanaleAudioAttuale
        self.numCanali = 0
        self.vetCanali = []
        self.volume = 0

    def riproduci(self, listaTracce):
        self.numCanali = len(listaTracce)
        self.vetCanali = []
        if self.numCanali > self.maxCanaliAudio:
            raise Exception("Numero canali audio non suffecienti.")
        numCanaleDiPartenza = self.numUltimoCanaleAudioUsato + 1
        i = 0
        while i < self.numCanali:
            self.vetCanali.append(pygame.mixer.Channel(numCanaleDiPartenza + i))
            self.vetCanali[i].set_volume(self.volume)
            self.vetCanali[i].play(listaTracce[i], -1)
            i += 1

    def arresta(self):
        i = 0
        while i < self.numCanali:
            self.vetCanali[i].stop()
            i += 1

    def settaVolume(self, volume):
        self.volume = volume
        i = 0
        while i < self.numCanali:
            self.vetCanali[i].set_volume(self.volume)
            i += 1

    def getBusy(self):
        audioInEsecuzione = False
        i = 0
        while i < self.numCanali:
            if self.vetCanali[i].get_busy():
                audioInEsecuzione = True
                break
            i += 1
        return audioInEsecuzione
