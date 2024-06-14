# Estudio de la pesca en Perú utilizando Neo4j

## Descripción del proyecto

Neo4j es una base de datos basada en grafos y relaciones. Ayudenme a meter floro pls

## Instalación
### Requisitos previos
Para ejecutar la base de datos localmente, se tiene los siguientes requisitos:
- Python 3 o superior. Se puede descargar desde el siguiente enlace: https://www.python.org/downloads/
- Driver de Neo4j para Python instalado. Se puede instalar con el comando `pip install neo4j` (requiere Python instalado)
- Neo4j Desktop. Se puede descargar desde el siguiente enlace: https://neo4j.com/download/
### Procedimiento
1. Crear una base de datos local en Neo4j Desktop e iniciarla (para más información, véase https://neo4j.com/docs/desktop-manual/current/operations/create-dbms/).
2. Clonar el repositorio (`git clone https://github.com/TheSunFall/pesca_neo4j.git`) o descargar el código fuente
3. En el archivo db/creardb.py, en la siguiente línea

    `dv = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))`

    Reemplazar el segundo campo de "auth" con la contraseña utilizada durante la creación

4. Ejecutar el archivo. 