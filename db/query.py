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
        records, summary, keys = self.driver.execute_query(query_=query)
        return records


def mostrar(data):
    if isinstance(data[0][1], list):
        table = []
        for record in data:
            subtable = []
            for d in record[1]:
                llaves = list(d.keys())
                subtable.append([d[llaves[1]], d[llaves[0]]])
            table.append([record[0], tabulate(subtable, tablefmt='plain')])
        print(tabulate(table, tablefmt="simple_grid",headers=res[0].keys()) + '\n')
    else:
        print(tabulate(data, headers="keys") + '\n')


if __name__ == '__main__':
    db = QueryDB()
    res0 = db.query("queries/mayor_consumo_especie.cypher")
    res = db.query("queries/producciones_departamento.cypher")
    mostrar(res0)
    mostrar(res)
