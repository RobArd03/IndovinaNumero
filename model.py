import random

import self


class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 5
        self._T = self._TMax
        self._segreto = None

    def reset(self):
        # Questo metodo resetta il gioco in qualsiasi momento
        self._segreto = random.randint(0, self._NMax)
        self._T = self._TMax
        print("segreto: ", self._segreto)

    def play(self, guess):
        """
        Funzione che esegue uno step del gioco
        :param guess: int
        :return:0 se vinto, +-1 se è piu grande o piu piccolo,
                    2 se ho finito le vite
        """
        # ci arriva un tentativo, confrontiamo il tentativo con il segreto

        self._T -= 1

        if guess == self._segreto:
            return 0 # ho vinto!!!

        if self._T == 0:
            return 2 # ho perso definitivamente

        if guess > self._segreto:
            return -1 # il segreto è piu piccolo

        return 1 # il segreto è piu grande


    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(80))