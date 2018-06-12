#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:46:15 2017

@author: Orlandy Ariel Sánchez A.
"""
import itertools
import math
from Bio import SeqIO


class Utilidades:
    '''
    Clase que contiene métodos de utilidades
    '''
    def tanto_por_ciento(self, a_num, a_num_total):
        '''
        Método que calcula el porcentaje
        '''
        a_num = float(a_num)
        a_num_total = float(a_num_total)
        porcentaje = '{0:.2f}'.format((a_num / a_num_total * 100))
        return float(porcentaje)

    def permutaciones(self, cadena):
        '''
        Método que calcula las permutaciones que existen dada una cadena.
        '''
        num_repe = len(cadena)
        total_perm = []
        itrtool = itertools.permutations(cadena, num_repe)
        for i in itrtool:
            temp = "".join(i)
            total_perm.append(temp)
        return total_perm

    def porcentaje_inverso(self, a_porcentaje, a_num_total):
        '''
        Método que calcula, a partir del porcentaje, el número de secuencias.
        '''
        a_porcentaje = float(a_porcentaje)
        a_num_total = (a_num_total)
        return math.ceil((a_porcentaje*a_num_total)/100)

    def guardar_sec_fichero(self, nom_fichero, formato, array_secuencia):
        '''
        Método que guarda en fichero un array de secuencias.
        '''
        SeqIO.write(array_secuencia, nom_fichero, formato)
        
    def convertidor_formatos (self, fichero_entrada,
                              formato_entrada,
                              fichero_salida,
                              formato_salida):
        '''
        Método que realizará una conversión de formato
        '''
        SeqIO.convert(fichero_entrada,
                      formato_entrada,
                      fichero_salida,
                      formato_salida)