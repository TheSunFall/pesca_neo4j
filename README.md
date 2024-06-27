# Estudio de la pesca en Perú utilizando Neo4j

## Descripción del proyecto

Neo4j es una base de datos basada en grafos, relaciones y propiedades los cuales almacena en nodos, 
lo que permite una mayor flexibilidad y eficiencia en el análisis de datos complejos. Utiliza un 
lenguaje de consulta llamado Cypher, similar a SQL pero optimizado para el uso de relaciones. 
Entre sus ventajas se encuentran:
- Escalabilidad.- Permite manejar grandes cantidades de datos y relaciones.
- Adaptabilidad.- Ofrece un entorno fácilmente moldeable a la necesidad de o los usuarios.
- Velocidad.- Realiza consultas de datos a velocidades nunca antes posibles.
- Flexibilidad.- Permite definir nodos, etiquetas y propiedades según las necesidades específicas de la aplicación.
- Seguridad.- Ofrece una estructura de seguridad robusta para proteger los datos.

Es posible integrar Cypher con lenguajes de programación según las necesidades y conocimientos de los usuarios, como 
Python o Java.

En este estudio, se construirán relaciones y propiedades acerca de la pesca en el Perú, con la información recopilada 
de distintas fuentes gubernamentales, con la finalidad de comprender el comportamiento de esta industria en distintos 
sectores y bajo un mismo periodo de tiempo, para comprender la relevancia de la pesca en el país y explicar las 
estadísticas obtenidas.

## Instalación
### Requisitos previos
Para ejecutar la base de datos localmente, se tiene los siguientes requisitos:
- Python 3.7 o superior. Se puede descargar desde el siguiente enlace: https://www.python.org/downloads/
- Driver de Neo4j para Python instalado. Se puede instalar con el comando `pip install neo4j` (requiere Python instalado) 
o si se usa el IDE PyCharm, se puede instalar desde la sección de "Python Packages" buscando la clave "neo4j".
- Paquete `python-tabulate` para mostrar las consultas. Se puede instalar con el comando `pip install tabulate` (requiere Python instalado) 
o si se usa el IDE PyCharm, se puede instalar desde la sección de "Python Packages" buscando la clave "tabulate".
- (Opcional, para clonar el repositorio) Git. Se puede descargar desde el siguiente enlace: https://git-scm.com/downloads

Adicionalmente, si no dispone de una instancia de AuraDB, necesitará una base de datos local en Neo4j Desktop.
- Neo4j Desktop. Se puede descargar desde el siguiente enlace: https://neo4j.com/download/

### Procedimiento
1. Crear una base de datos en Neo4j Desktop o en AuraDB e iniciarla.
   - Si se ha creado la base de datos en AuraDB, asegúrese de guardar el archivo .txt que se le brindará.
   - Si se ha creado localmente, guarde la contraseña utilizada. 
2. Clonar el repositorio (`git clone https://github.com/TheSunFall/pesca_neo4j.git`) o descargar el código fuente 
a través de GitHub.
3. Ejecutar el archivo main.py. Asegúrese de tener todos los archivos y en las mismas carpetas que en el repositorio.
   - En un IDE de Python, simplemente abra el archivo main.py y use el botón de Ejecutar
   - Si utiliza la consola del sistema operativo, ubíquese en la carpeta donde se encuentra el código fuente y escriba 
`python main.py` o `python3 main.py` (puede variar según su sistema operativo) 
4. Ingresar los datos solicitados
   - En Neo4j Desktop (base de datos local) la URL y usuario normalmente serán `bolt://localhost:7687` y `neo4j` 
respectivamente (puede verificar accediendo a Neo4j Browser y escribiendo `:server status`).
   - Para AuraDB, utilize los datos en el archivo .txt descargado durante la creación. En la URL, reemplaze `neo4j+s://`
   por `neo4j+ssc://`, caso contrario obtendrá un error
5. Una vez creada la base de datos, desde AuraDB o Neo4j Desktop, puede utilizar las consultas del proyecto ejecutando 
el archivo query.py e introduciendo los mismos datos, o puede realizar las suyas propias desde Neo4j Browser 
(ej.`MATCH (n1)-[r]->(n2) RETURN n1,r,n2`).
