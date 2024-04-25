import copy
from time import time
class Model:
    def __init__(self):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []


    def risolvi_n_regine(self, N):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []
        self.ricorsione([], N)


    def ricorsione(self, parziale, N):
        self.N_iterazioni += 1
        # condizione terminale
        if len(parziale) == N:
        #    print(parziale)
            if self.soluzione_nuova(parziale):
                self.N_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row, col))
                    if self._regina_ammissibile(parziale):
                        self.ricorsione(parziale, N)
                    parziale.pop()

    def _regina_ammissibile(self, parziale):
        if len(parziale) == 1:
            return True
        ultima_regina = parziale[-1]
        for regina in parziale[ : len(parziale) - 1]:
            # controllare righe
            if ultima_regina[0] == regina[0]:           ## parziale è fatto di tuple (riga, colonna)
                return False
            # controllare colonne
            if ultima_regina[1] == regina[1]:
                return False
            # controllare diagonali
            if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                return False
            if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                return False
        return True

    def soluzione_nuova(self, soluzione_nuova):
        # per ogni soluzione
        for soluzione in self.soluzioni:
            is_nuova = False
            # per ogni regina della nuova soluzione, controllo se è una
            # configurazione vecchia o no
            for regina in soluzione_nuova:
                # se almeno una regina di soluzione_nuova non si trova nella soluzione precedente
                # la soluzione è nuova
                if regina not in soluzione:
                    is_nuova = True
            if not is_nuova:
                return is_nuova
        return True


if __name__ =="__main__":
    model = Model()
    start = time()
    model.risolvi_n_regine(4)
    end = time()
    print(f"L'algoritmo ha trovato {model.N_soluzioni} soluzioni.\n "
          f"L'algoritmo ha chiamato la funzione ricorsiva {model.N_iterazioni} volte.\n"
          f"L'algoritmo ha impiegato {end - start} secondi")
    print(model.soluzioni)