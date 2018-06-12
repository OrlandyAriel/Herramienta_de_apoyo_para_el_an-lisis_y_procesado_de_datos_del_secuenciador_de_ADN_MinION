# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:19:13 2018

@author: Orlandy Ariel Sánchez Acosta.
"""
import urllib.request as request
import bs4 as bs


class PeticionGETBlast:
    '''
    Esta clase construye y realiza una petición put a BLAST
    '''
    def __init__(self):
        self.__url_blast = 'https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=%s&FORMAT_TYPE=%s&RID=%s'
        self.__cmd = "Get"
        self.format_type = "Text"
        self.peticion = None
        self.rid = ""
        self.result = False

    def construir_peticion(self, rid):
        '''
        Método encargado de crear la petición, recibe como parámetro el RID,
        es decir, un identificador de la búsqueda.
        '''
        self.rid = rid
        self.peticion = self.__url_blast %(self.__cmd,
                                           self.format_type,
                                           self.rid)

    def realizar_peticion(self):
        '''
        Una vez creada la petición, se podrá proceder a realizar la petición,
        devolverá True o False dependiendo si encuentra similitud o no.
        Para todo esto se necesita un RID, identificador de la búsqueda de la
        secuencia que se pretende mirar si hay o no similitud.
        '''
        try:
            page = request.urlopen(self.peticion, timeout = 60)
            soup = bs.BeautifulSoup(page, 'html.parser')

            parrafo = soup.p
            parrafo = parrafo.text
            self.result = ("No significant similarity" in parrafo)

        except AttributeError as err:
            print("No se ha CREADO la petición. NOTA:puede que la petición no",
                  "se haya creado aun, vea el método construir_peticion.",
                  " Otra ayuda: ", err)

        return self.result
