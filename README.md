# Estudio de la pesca en Perú utilizando Neo4j

## Descripción del proyecto

Neo4j es una base de datos basada en grafos, relaciones y propiedades los cuales almacena en nodos, lo que permite una mayor flexibilidad y eficiencia en el análisis de datos complejos. Utiliza un lenguaje de consulta llamado Cypher, similar a SQL pero optimizado para el uso de relaciones. 
Entre sus ventajas se encuentran:
- Escalabilidad.- Permite manejar grandes cantidades de datos y relaciones.
- Adaptabilidad.- Ofrece un entorno fácilmente moldeable a la necesidad de o los usuarios.
- Velocidad.- Realiza consultas de datos a velocidades nunca antes posibles.
- Flexibilidad.- Permite definir nodos, etiquetas y propiedades según las necesidades específicas de la aplicación.
- Seguridad.- Ofrece una estructura de seguridad robusta para proteger los datos.

Es posible integrar Cypher con lenguajes de programación según las necesidades y conocimientos de los usuarios, como Python o Java.

En este estudio, se construirán relaciones y propiedades acerca de la pesca en el Perú, con la información recopilada de distintas fuentes estadísticas de prestigio, con la finalidad de comprender el comportamiento de esta industria en distintos sectores y bajo un mismo periodo de tiempo, para comprender la relevancia de la pesca en el país y explicar las estadísticas obtenidas.

## Instalación
### Requisitos previos
Para ejecutar la base de datos localmente, se tiene los siguientes requisitos:
- Python 3 o superior. Se puede descargar desde el siguiente enlace: https://www.python.org/downloads/
- Driver de Neo4j para Python instalado. Se puede instalar con el comando `pip install neo4j` (requiere Python instalado) o si se usa una IDE como PyCharm, se puede instalar desde la sección de "Python Packages" buscando la clave "neo4j".
- GIT (para clonar el repositorio). Se puede descargar desde el siguiente enlace: https://git-scm.com/downloads

Adicionalmente, si no dispone de una instancia de AuraDB, necesitará una base de datos local en Neo4j Desktop.
- Neo4j Desktop. Se puede descargar desde el siguiente enlace: https://neo4j.com/download/

### Procedimiento
1. Crear una base de datos en Neo4j Desktop o en AuraDB e iniciarla.
   - Si se ha creado la base de datos en AuraDB, asegúrese de guardar el archivo .txt que se le brindará.
   - Si se ha creado localmente, guarde la contraseña utilizada. La URL y usuario normalmente serán "bolt://localhost:7687" y "neo4j".
2. Clonar el repositorio (`git clone https://github.com/TheSunFall/pesca_neo4j.git`) o descargar el código fuente a través de este medio.
3. Ejecutar el archivo main.py dentro de una IDE de Python importando el repositorio (ubicado en C:\User\"nombre_de_usuario") o desde la consola del sistema operativo (`python main.py` o `python3 main.py`, puede variar según su sistema) e ingresar los datos solicitados, su usuario normalmente será "neo4j" y su URL de host local será "bolt://localhost:7687". 
Para AuraDB, la URL, usuario y contraseña estarán en el archivo .txt almacenado en su dispositivo.
4. Una vez creada la base de datos, desde AuraDB o Neo4j Desktop inicie la base de datos local que creó y abra Neo4j Browser, puede asegurar el correcto funcionamiento de esta con el comando "MATCH (n) RETURN (n)".