class Padre(object):

    def __init__(self, passato):

    	self.COSTANTE = "COSTANTE"
        self.passato = passato


class Figlio(Padre):

    def __init__(self,passato_sotto):

        super(Figlio, self).__init__(passato_sotto)


nuovoFiglio = Figlio('passato')
print nuovoFiglio.passato
print nuovoFiglio.COSTANTE

