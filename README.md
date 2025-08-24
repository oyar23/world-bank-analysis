Análisis de la Economía de América Latina con la API del Banco Mundial

Este proyecto es un análisis exploratorio de datos (EDA) centrado en indicadores económicos clave de países de América Latina. Utiliza la API del Banco Mundial (wbgapi) para consumir datos en tiempo real 
y realizar visualizaciones para entender la evolución de la población, el PIB, las exportaciones y las importaciones a lo largo del tiempo.


Contenido del Repositorio

    notebooks/: Contiene el EDA (EDA_WgbAPI.ipynb) donde se explora la API y se generan los gráficos.

    data/: Esta carpeta se crea automáticamente y almacena los archivos CSV generados por el script de ETL.

    etl_data.py: Un script que simula una pipeline de ETL (Extract, Transform, Load), descargando datos de la API del Banco Mundial, transformándolos y guardándolos como archivos CSV limpios.

    requirements.txt: Lista de librerías necesarias para ejecutar el proyecto.

ETL y Pipeline de Datos

El script etl_data.py automatiza el proceso de extracción de datos de la API del Banco Mundial. Extrae datos para los siguientes indicadores y países (Argentina, Estados Unidos, Chile, Brasil y Uruguay) y los transforma a un formato tabular (.csv) listo para el análisis:

    PIB per cápita (NY.GDP.PCAP.CD)

    Exportaciones de bienes y servicios (BX.KLT.DINV.CD.WD)

    Importaciones de bienes y servicios (BM.GSR.TOTL.CD)

Puedes ejecutar este script desde tu terminal para actualizar los datos en la carpeta data/:

Requisitos:

Para ejecutar el proyecto, necesitarás tener Python instalado. Las dependencias se pueden instalar fácilmente usando pip y el archivo requirements.txt:
Bash

pip install -r requirements.txt

Autor

    Lautaro Oyarzún - GitHub
