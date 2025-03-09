class Temperatura:
    def __init__(self):
        self._medias = []
        self._maximas = []
        self._minimas = []
        
    def adicionar_temperatura(self, temperatura):
        self._medias.append(temperatura)
        self._maximas.append(temperatura)
        self._minimas.append(temperatura)
        
    @property
    def media(self):
        return sum(self._medias) / len(self._medias)
    
    @property
    def maxima(self):
        return max(self._maximas)
    
    @property
    def minima(self):
        return min(self._minimas)
    
temperatura = Temperatura()
while True:
    temparatura = input('Informe a temperatura (ou "sair" para finalizar): ')
    if temparatura.lower() == 'sair':
        break
    temperatura.adicionar_temperatura(float(temparatura))

print(f'Temperatura média: {temperatura.media}')
print(f'Temperatura máxima: {temperatura.maxima}')
print(f'Temperatura mínima: {temperatura.minima}')

