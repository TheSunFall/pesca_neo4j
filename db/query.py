from neo4j import GraphDatabase
from tabulate import tabulate


class QueryDB:
    def __init__(self, uri, usr, passwd):
        self.driver = GraphDatabase.driver(uri, auth=(usr, passwd))
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
            e = list(record[1][0].values())
            if isinstance(e[0], int):
                for d in record[1]:
                    llaves = list(d.keys())
                    subtable.append([d[llaves[1]], d[llaves[0]]])
            else:
                for d in record[1]:
                    llaves = list(d.keys())
                    subtable.append([d[llaves[0]], d[llaves[1]]])
            table.append([record[0], tabulate(subtable, tablefmt='plain')])
        print(tabulate(table, tablefmt="simple_grid", headers=data[0].keys()) + '\n')
    else:
        print(tabulate(data, tablefmt="simple_grid", headers="keys", numalign="right") + '\n')


if __name__ == '__main__':
    url = input("Ingrese URL de la base de datos (para AuraDB reemplazar \"neo4j+s://\" por \"neo4j+ssc://\"): ")
    usr = input("Ingrese nombre de usuario en la base de datos (normalmente será \"neo4j\"): ")
    passwd = input("Ingrese contraseña: ")
    db = QueryDB(url, usr, passwd)
    res2 = db.query("queries/producciones_departamento.cypher")
    mostrar(res2)
    db.close()
