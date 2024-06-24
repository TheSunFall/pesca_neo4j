from neo4j import GraphDatabase


class SetupDB:
    def __init__(self, uri, user, passwd):
        self.driver = GraphDatabase.driver(uri, auth=(user, passwd))
        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()
        print("Configuración inicial terminada")

    def aniadir_especie(self, nombre, desembarque, consumos):
        self.driver.execute_query("MERGE(e:Especie {name:$nm,desembarque:$ds})", nm=nombre, ds=desembarque)
        for key, value in consumos.items():
            self.driver.execute_query("""MATCH(e:Especie) MATCH(c:Consumo) WHERE (e.name = $nm AND c.name = $consumo) 
            MERGE(e)-[:USO {cantidad: $cant}]->(c)""", nm=nombre, consumo=key, cant=value)

    def aniadir_consumo(self, nombre, c_interno, exportaciones, tipo):
        self.driver.execute_query("MERGE (c:Consumo { name:$n,venta_interna:$i,exportacion:$exp,tipo:$t})", n=nombre,
                                  i=c_interno, exp=exportaciones, t=tipo)

    def aniadir_dpto(self, nombre, vab):
        self.driver.execute_query("MERGE (d:Departamento {name:$nm,val_agregado_bruto:$v})", nm=nombre, v=vab)

    def aniadir_puerto(self, nombre, dpto, desembarque, consumos):
        self.driver.execute_query("""MATCH (d:Departamento) WHERE (d.name=$dp)
                                  MERGE (p:Puerto {name:$nm,desembarque:$ds})-[:UBICACION]->(d)""", nm=nombre,
                                  ds=desembarque, dp=dpto)
        for key, value in consumos.items():
            self.driver.execute_query("""MATCH(p:Puerto) MATCH(c:Consumo) WHERE (p.name = $nm AND c.name = $consumo)
                                      MERGE(p)-[:PRODUCCION {cantidad: $cant}]->(c) """, nm=nombre, consumo=key,
                                      cant=value)
