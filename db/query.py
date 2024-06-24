from neo4j import GraphDatabase
from tabulate import tabulate


class QueryDB:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()

    def query(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                query = archivo.read()
        except FileNotFoundError:
            return "El archivo de consulta no se encontró."
        except IOError:
            return "Hubo un error al leer el archivo."
        result, summary, keys = self.driver.execute_query(query_=query)
        return result


def mostrar(data):
    print(tabulate(data, headers='keys') + '\n')


if __name__ == '__main__':
    db = QueryDB()
    mostrar(db.query("queries/mayor_consumo_especie.cypher"))
    mostrar(db.query("queries/desembarque_total_especie.cypher"))
