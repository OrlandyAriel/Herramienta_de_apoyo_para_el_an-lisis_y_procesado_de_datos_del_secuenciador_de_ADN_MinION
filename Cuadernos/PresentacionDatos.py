# -*- coding: utf-8 -*-
"""
Created on Fri May 26 17:06:55 2017

@author: Orlandy Ariel Sánchez Acosta
"""
import UtilidadesParaArrays as arrUtile
from IPython.display import Markdown, display


class PresentacionDatos:
    '''
    Clase que contiene método para la repersentación de datos sin gráficos
    '''
    def colores_tabla(self, val, array1, array2):
        '''
        Método que, dependediendo de si hay o no coincidencias,
        devuelve un color para poner el fondo de una celda de un dataframe.
        '''
        c_arrays_utile = arrUtile.UtilidadesParaArrays()
        coincidencia = c_arrays_utile.coicidencias_color(val, array1, array2)

        if coincidencia:
            color = '#55DEFA'
        if not coincidencia:
            color = 'red'
        if val == '-':
            color = '#EBEBEB'

        return 'background-color: %s' % color

    def printmd(self, string):
        '''
        Método que permite imprimir en una celda con formato
        Markdown desde python.
         '''
        display(Markdown(string))
