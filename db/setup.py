from neo4j import GraphDatabase


class SetupDB:
    def __init__(self, uri, user, passwd):
        self.driver = GraphDatabase.driver(uri, auth=(user, passwd))

    def close(self):
        self.driver.close()

    def aniadir_especie(self, nombre, desembarque, consumos):
        self.driver.execute_query("CREATE(e:Especie {name:$nm,desembarque:$ds})", nm=nombre, ds=desembarque)
        for key, value in consumos.items():
            self.driver.execute_query("""MATCH(e:Especie) MATCH(c:Consumo) WHERE (e.name = $nm AND c.name = $consumo) 
            CREATE(e)-[:USO {cantidad: $cant}]->(c)""", nm=nombre, consumo=key, cant=value)

    def aniadir_consumo(self, nombre, c_interno, exportaciones, tipo):
        self.driver.execute_query("CREATE (c:Consumo { name:$n,venta_interna:$i,exportacion:$exp,tipo:$t})", n=nombre,
                                  i=c_interno, exp=exportaciones, t=tipo)

    def aniadir_puerto(self, nombre, dpto, desembarque, consumos):
        self.driver.execute_query("""MATCH (d:Departamento) WHERE (d.name=$dp)
                                  CREATE (p:Puerto {name:$nm,desembarque:$ds})
                                  CREATE (p)-[:UBICACION]->(d)""", nm=nombre, ds=desembarque, dp=dpto)
        for key, value in consumos.items():
            self.driver.execute_query("""MATCH(p:Puerto) MATCH(c:Consumo) WHERE (p.name = $nm AND c.name = $consumo)
                                      CREATE(p)-[:PRODUCCION {cantidad: $cant}]->(c) """, nm=nombre, consumo=key,
                                      cant=value)

    def aniadir_dpto(self, nombre, vab):
        self.driver.execute_query("CREATE (d:Departamento {name:$nm,val_agregado_bruto:$v})", nm=nombre, v=vab)

