# -*- coding: utf-8 -*-

import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


class ImageClass(object):

    def __init__(self, path, xScale, yScale, aumentaRisoluzione, canale_alpha=True, imgImpenetrabile=False, forceLoad=False):
        self.path = path
        self.xScale = xScale
        self.yScale = yScale
        self.aumentaRisoluzione = aumentaRisoluzione
        self.canale_alpha = canale_alpha
        self.imgImpenetrabile = imgImpenetrabile
        if forceLoad:
            self.image = forceLoad(path, xScale, yScale, aumentaRisoluzione, canale_alpha, imgImpenetrabile)
        else:
            self.image = False

    def get(self):
        if not self.image:
            self.image = CaricaFileProgetto.loadImage(self.path, self.xScale, self.yScale, self.aumentaRisoluzione, self.canale_alpha, self.imgImpenetrabile)
        return self.image
