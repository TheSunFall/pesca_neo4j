# Estudio de la pesca en Perú utilizando Neo4j

## Descripción del proyecto

Neo4j es una base de datos basada en grafos y relaciones. Ayudenme a meter floro pls

## Instalación
### Requisitos previos
Para ejecutar la base de datos localmente, se tiene los siguientes requisitos:
- Python 3 o superior. Se puede descargar desde el siguiente enlace: https://www.python.org/downloads/
- Driver de Neo4j para Python instalado. Se puede instalar con el comando `pip install neo4j` (requiere Python instalado)
- (Opcional) Git. Se puede descargar desde el siguiente enlace: https://git-scm.com/downloads

Adicionalmente, si no dispone de una instancia de AuraDB, necesitará una base de datos local en Neo4j Desktop
- Neo4j Desktop (se puede descargar desde el siguiente enlace: https://neo4j.com/download/).

### Procedimiento
1. Crear una base de datos en Neo4j Desktop o en AuraDB e iniciarla.
   - Si se ha creado la base de datos en AuraDB, asegúrese de guardar el archivo .txt que se le brindará.
   - Si se ha creado localmente, guarde la contraseña utilizada. La URL y usuario normalmente serán "bolt://localhost:7687" y "neo4j", respectivamente.
2. Clonar el repositorio (`git clone https://github.com/TheSunFall/pesca_neo4j.git`) o descargar el código fuente
3. Ejecutar el archivo main.py (`python main.py` o `python3 main.py`, puede variar según su sistema) e ingresar los datos solicitados.
    - Para AuraDB, la URL, usuario y contraseña estarán en el archivo .txt

Una vez creada la base de datos, puede verificar su funcionamiento accediendo a ella desde Neo4j Browser.