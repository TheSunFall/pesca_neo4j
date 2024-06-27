from neo4j import GraphDatabase
from tabulate import tabulate
from os import path, getcwd


class QueryDB:
    def __init__(self, uri, usr, passwd):
        self.driver = GraphDatabase.driver(uri, auth=(usr, passwd))
        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()

    def query(self, nombre_archivo):

        with open(path.join(path.dirname(path.realpath(__file__)), "queries",nombre_archivo)) as archivo:
            query = archivo.read()
        records, summary, keys = self.driver.execute_query(query_=query)
        return records


def mostrar(data):
    if isinstance(data[0][1], list):
        table = []
        for record in data:
            table.append([record[0], tabulate(record[1], tablefmt='plain')])
        print(tabulate(table, tablefmt="simple_grid",
              headers=data[0].keys()) + '\n')
    else:
        print(tabulate(data, tablefmt="simple_grid",
              headers="keys", numalign="right") + '\n')


if __name__ == '__main__':
    url = input(
        "Ingrese URL de la base de datos (para AuraDB reemplazar \"neo4j+s://\" por \"neo4j+ssc://\"): ")
    usr = input(
        "Ingrese nombre de usuario en la base de datos (normalmente será \"neo4j\"): ")
    passwd = input("Ingrese contraseña: ")
    
    db = QueryDB(url, usr, passwd)
    res1 = db.query("desembarque_total_especie.cypher")
    res2 = db.query("mayor_consumo_especie.cypher")
    res3 = db.query("producciones_departamento.cypher")
    mostrar(res1)
    mostrar(res2)
    mostrar(res3)
    db.close()
