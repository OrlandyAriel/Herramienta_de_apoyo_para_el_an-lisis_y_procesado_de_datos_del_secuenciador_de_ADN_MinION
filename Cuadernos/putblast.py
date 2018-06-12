# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:31:26 2018

@author: Orlandy Ariel Sánchez Acosta
"""


import urllib.request as request
import bs4 as bs

class PeticionPUTBlast:
    '''
    Esta clase construye y realiza una petición put a BLAST
    '''
    def __init__(self):
        self.__url_blast = "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=%s&PROGRAM=%s&DATABASE=%s&QUERY=%s"
        self.__cmd = "Put"
        self.program = "blastn&MEGABLAST=on" #Por defecto
        self.database = "nr" #Por defecto
        self.query = ""
        self.peticion = None
        self.rid = None

    def construir_peticion(self,
                           query,
                           database,
                           program):
        '''
        Este método será el encargardo de constrir la consulta
        según los parámetros que a este se le indiquen.
        '''
        self.program = program
        self.database = database
        self.query = query

        self.peticion = self.__url_blast %(self.__cmd,
                                           self.program,
                                           self.database,
                                           self.query)

    def realizar_peticion(self):
        '''
        Una vez creada la petición, se podrá proceder a realizar la petición,
        devolverá un string, RID, es el identificador por el cual luego
        se puede consultar el resultado de la petición.
        '''
        try:
            page = request.urlopen(self.peticion, timeout = 60)
            soup = bs.BeautifulSoup(page, 'html.parser')
            self.rid = soup.find('input', {'id': 'rid'}).attrs['value']
        except AttributeError as err:
            print("No se ha CREADO la petición. NOTA:puede que la petición no",
                  "se haya creado aun, vea el método construirPeticion.",
                  " Otra ayuda: ", err)

        #return self.rid
