from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


'''
O calculo da Aliquota do IPI (percentual do imposto) leva em conta
se existe "aliquota_adicional".
Se existir aliquota_adicional, a aliquota e aumentada em 10%.
Por exemplo, se a aliquota informada no construtor for 10.0
e existe "aliquota_adicional", entao a aliquota calculada sera de 11.0.
'''


class IPI(Imposto):
    def __init__(self, aliquota:float, incidencia_importo:IncidenciaImposto, aliquota_adicional:bool):
        super().__init__(aliquota, incidencia_importo)
        self.__aliquota_inicial = aliquota
        self.__aliquota_adicional = aliquota_adicional

    def calcula_aliquota(self) -> float:
        if self.__aliquota_adicional:
           self.__aliquota = (self.__aliquota_inicial * 1.1) / 100
        else:
           self.__aliquota = self.__aliquota_inicial / 100
        return self.__aliquota
            