# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:40:07 2017

@author: Orlandy Ariel Sáchez Acosta
"""
import numpy as np


class UtilidadesParaArrays:
    '''
    Clase que contendrá funciones para trabajar con arrays
    '''
    def igualar_arrays(self, a_array1, a_array2):
        '''
        Método que iguala los arrays que se le pasan por parámetros
        de manera que las posiciones que le falte a uno se rellenan con un '-'
        devuelve un array con 2 posiciones, con los arrays bien colocados
        y con la misma longitud
        '''
        array1 = sorted(np.concatenate((a_array1, a_array2), 0))
        array2 = sorted(np.concatenate((a_array1, a_array2), 0))

        for i, val in enumerate(array1):
            if(not(val in a_array1)):
                array1[i] = '-'

        for j, val in enumerate(array2):
            if val not in a_array2:
                array2[j] = '-'

        array1 = self.eliminar_duplicado(array1)
        array2 = self.eliminar_duplicado(array2)

        for i, x in enumerate(array1):
            if(x == '-' and array2[i] == '-'):
                array1.pop(i)
                array2.pop(i)

        return [array1, array2]

    def coicidencias(self, a_array1, a_array2):
        '''
        Método que dados dos arrays devuelve en número de
        elementos comunes a ambos.
        '''
        result_coincide = []
        for i in a_array1:
            if(i in a_array2 and not(i == '-')):
                result_coincide.append(i)

        return result_coincide

    def eliminar_duplicado(self, array):
        '''
        Este método elimina los datos duplicados en un array, siempre y
        cuando este dato no sea '-'
        '''
        array_sin_dupli = []
        for i in array:
            if i is not '-':
                if i not in array_sin_dupli:
                    array_sin_dupli.append(i)
            else:
                array_sin_dupli.append(i)

        return array_sin_dupli

    def coicidencias_color(self, valor, a_array1, a_array2):
        '''
        Método que dado un dato verifica que está en los arrays que
        se le pasa como parametro.
        '''
        pos1 = -1
        pos2 = -1
        if valor in a_array1:
            pos1 = a_array1.index(valor)
        if valor in a_array2:
            pos2 = a_array2.index(valor)

        return (pos1 == pos2)

    '''
    Método que devuelve un array con las secuencias que coincidan en array_pos
    '''
    def obtener_array_sec(self, array_todas_sec, array_pos):
        array_result = []
        for i, sec_cal in enumerate(array_todas_sec):
                for j in array_pos:
                    if(i == j):
                        array_result.append(sec_cal)

        return array_result

    def obtener_claves_dic(self, diccionario, clave = True):
        '''
        Método que devuelve las claves de un diccionario.
        '''
        array_result = []
        for clve, valor in diccionario.items():
            if(clave):
                array_result.append(clve)
            else:
                array_result.append(valor)

        return array_result

    def construir_array_univalor(self, num, n):
        '''
        Método que crea un array con un unioco valor repetidos n veces.
        '''
        return np.repeat(num, n)
