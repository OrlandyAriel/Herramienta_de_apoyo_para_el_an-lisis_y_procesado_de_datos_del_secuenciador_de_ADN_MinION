# Trabajo de Fin de Grado

# Herramientas de apoyo para el análisis y procesado de datos del secuenciador de ADN MinION.

### Autor: [Orlandy Ariel Sánchez Acosta](https://github.com/OrlandyAriel)

### [Leer Memoria](https://github.com/OrlandyAriel/Herramienta_de_apoyo_para_el_an-lisis_y_procesado_de_datos_del_secuenciador_de_ADN_MinION/blob/master/Herramientas%20de%20apoyo%20para%20el%20an%C3%A1lisis%20y%20procesado%20de%20datos%20del%20secuenciador%20de%20ADN%20MinION.pdf)
      

Este proyecto se lleva a cabo en Jupyter-notebook, es indispensable que se encuentre instalado en la máquina para poder ejecutar y ver la herramienta.



Jupyter-Notebook es una aplicación web que permite crear y compartir documentos que contienen código, el cual se puede ejecutar en tiempo real. Este soporta más de 40 lenguajes de programación, entre los que incluye Python que es con el lenguaje que trabajaremos.[Más información](http://jupyter.org/)



Existen varias maneras de instalar Jupyter-notebook, a continuación, se dará información sobre la instalación de dos de ellas (las que han probado en el desarrollo del proyecto).

[Anaconda](https://www.continuum.io/downloads), anaconda es una plataforma para que incluye Python y R, se puede instalar tanto en Windows como en Linux, en este caso se optó por instalar Anaconda en Windows.

## Instalación en Windows



* Primero se deberá descargar el instalador de [Anaconda](https://www.continuum.io/downloads).

* Ejecutar e instalar Anaconda siguiendo las instrucciones de la página de descarga.

* Para lanzar Jupyter-notebook deberá abrir una consola (CMD) y lanzar el comando:

>jupyter-notebook



* También se puede lanzar yendo a la menú de inicio y buscar la carpeta Anaconda->jupyter-notebook



##Para la instalación el Linux y OS X



Se deberá instalar previamente Python, para el proyecto se usa Python 3.

> * pip3 install ––upgrade pip

> * pip3 install jupyter



Una vez instalado se lanza igual que en Windows, con el comando:

> jupyter-notebook



## Librerías utilizadas

* [Biopython](http://biopython.org/wiki/Documentation)

* [Plotly](https://plot.ly/python/)

* [Iteratools](https://docs.python.org/2/library/itertools.html)

* [IPython](https://ipython.readthedocs.io/en/stable/install/install.html)

* [Pandas](http://pandas.pydata.org/)

* [NumPy](http://www.numpy.org/)

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* [URLLib](https://docs.python.org/3/howto/urllib2.html)

* [Time](https://docs.python.org/2/library/time.html)

* [Búsqueda BLAST](https://github.com/OrlandyAriel/BusquedaBLAST)



### Otras cuestiones

En caso de que se desee instalar el Kernels IPython sigua el siguiente [enlace](http://ipython.readthedocs.io/en/stable/install/kernel_install.html).



Tener en cuenta que para el correcto funcionamiento deberá tener las librerías instaladas en el equipo que se va a correr la herramienta. Para instalar librerías se puede hacer de la siguiente manera:

* Linux y OS X:

> pip3 install nombre librería



* Windows:

	* Método 1:

	> conda install nombre librería.

	> **NOTA:** no todas las librerías son soportadas por Anaconda, para este proyecto si están todas.

	* Método 2:

	> Buscar en el menú de Windows: Anaconda Navigator

	> Aquí podrá navegar y buscar las librerías que necesite e instalarlas, sólo saldrán las librerías soportadas por Anaconda.







