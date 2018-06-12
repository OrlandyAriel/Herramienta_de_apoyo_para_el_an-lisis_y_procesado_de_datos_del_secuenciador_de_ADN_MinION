#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:53:44 2017
@author: Orlandy Ariel Sánchez A.
"""

import plotly.graph_objs as go
import UtilidadesParaArrays


class GraficoDePuntos:
    '''
    Esta clase es utilizada para crear un gráfico de puntos.
    '''
    def __init__(self):
        self.ult_array = UtilidadesParaArrays.UtilidadesParaArrays()
        self.it_confianza = 0
        self._array_x_buenos = []
        self._array_y_buenos = []
        self._array_x_malos = []
        self._array_y_malos = []
        self._array_lim_sup = []
        self._array_lim_inf = []
        self._array_media = []

    def _construir_arrays(self, dic_buenos, dic_malos):
        '''
        Método que se encarga de inicializar los arrays a partir de
        diccionarios.
        '''
        self._array_x_buenos = self.ult_array.obtener_claves_dic(dic_buenos)
        self._array_y_buenos = self.ult_array.obtener_claves_dic(dic_buenos,
                                                                 False)

        self._array_x_malos = self.ult_array.obtener_claves_dic(dic_malos)
        self._array_y_malos = self.ult_array.obtener_claves_dic(dic_malos,
                                                                False)

    def _crear_linea_graf(self,
                          array_x,
                          array_linea,
                          titulo,
                          color):
        '''
        Método que se encarga de crear una línea en las coordenadas indicadas,
        además, añade un título y un color a esta. El método retornará la
        línea configurada y lista para añadirla a un gráfico.
        '''
        trace = go.Scatter(
                           x = array_x,
                           y = array_linea,
                           mode = 'lines',
                           name = titulo,
                           line = dict(
                                       color = 'rgb%s' % color,
                                       width = 4)
                           )
        return trace

    def _crear_punto_graf(self,
                          array_x,
                          array_y,
                          titulo,
                          color):
        '''
        Método que se encarga de crear los puntos de un gráfico de puntos,
        partiendo de sus coordenadas, pasadas como arrays, además se añadirá
        un título y un color. Retornará los puntos configurados en el gráfico.
        '''
        trace = go.Scatter(
                           x = array_x,
                           y = array_y,
                           mode = 'markers',
                           name = titulo,
                           marker = dict(
                                size = 10,
                                color = 'rgb%s' % color,
                                line = dict(
                                    width = 1)
                                )
                        )
        return trace
    
    '''
    Método que configura la barra del gráfico, permite elegir que botones 
    eliminar. 
    La configuración que está establecida únicamente deja el botón para que se pueda
    descargar la imagen del gráfico generado.
    '''
    def eliminar_btn_barra(self):
        config = {'modeBarButtonsToRemove':[
                     'hoverClosestPie',
                     'sendDataToCloud',
                     'autoScale2d',
                     'hoverClosestCartesian',
                     'hoverCompareCartesian', 
                     'lasso2d',
                     'selected2d',
                     'zoom2d', 
                     'zoomIn2d', 
                     'zoomOut2d', 
                     'pan2d', 
                     'resetScale2d',
                     'toggleSpikelines',
                     'select2d'],
                'displaylogo': False,
                'showTips': False,
                'showLink':False,
                'linkText':''}
        return config
    
    def crear_grafico_puntos(self,
                             dic_buenos,
                             dic_malos,
                             titulo_graf,
                             titulo_x,
                             titulo_y,
                             tam,
                             med,
                             it_confianza,
                             lim_inf,
                             lim_sup = None):
        '''
        Método encargado de configurar todas las partes del gráfico. Retornará
        el gráfico perfectamente configurado y listo para ser mostrado.
        '''
        titulo_lim_inf = "Límite inferior"
        self.it_confianza = it_confianza
        self._construir_arrays(dic_buenos, dic_malos)
        self._array_lim_inf = self.ult_array.construir_array_univalor(
                                                                      lim_inf,
                                                                      tam)
        datos = []
        # Creación de gráfico.
        datos.append(self._crear_punto_graf(self._array_x_buenos,
                                            self._array_y_buenos,
                                            'Lectura buena',
                                            '(27, 246, 246)'))
        datos.append(self._crear_punto_graf(self._array_x_malos,
                                            self._array_y_malos,
                                            'Lectura mala',
                                            '(253, 0, 0 )'))
        # Si lim_sup tiene el valor None es que no necesita poner la media ni
        # el límite superior
        if(lim_sup is not None):
            self._array_lim_sup = self.ult_array.construir_array_univalor(
                                                                      lim_sup,
                                                                      tam)
            datos.append(self._crear_linea_graf(self._array_x_buenos,
                                                self._array_lim_sup,
                                                "Límite superior(x̄ + %0.02F * σ)" % (it_confianza),
                                                "(27, 103, 246)"))
            self._array_media = self.ult_array.construir_array_univalor(
                                                                        med,
                                                                        tam)
            datos.append(self._crear_linea_graf(
                                                self._array_x_buenos,
                                                self._array_media,
                                                "Media de todas las lecturas (x̄)",
                                                "(246, 90, 27)"))
            titulo_lim_inf = "Límite inferior(x̄ - %0.02F * σ)" % (it_confianza)

        datos.append(self._crear_linea_graf(self._array_x_buenos,
                                            self._array_lim_inf,
                                            titulo_lim_inf,
                                            "(246, 200, 27)"))

        layout = go.Layout(
                           title = titulo_graf,
                           xaxis = dict(
                                    title = titulo_x
                                    ),
                           yaxis = dict(
                                    title = titulo_y
                                    )
                            )
        grafico = go.Figure(data = datos, layout = layout)
        return grafico
