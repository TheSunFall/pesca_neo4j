from neo4j import GraphDatabase


def aniadir_especie(driver, nombre, desembarque, consumos):
    driver.execute_query("CREATE(e:Especie {name:$nm,desembarque:$ds})", nm=nombre, ds=desembarque)
    for key, value in consumos.items():
        driver.execute_query("MATCH(e:Especie) MATCH(c:Consumo) WHERE (e.name = $nm AND c.name = $consumo)"
                             "CREATE(e)-[:USO {cantidad: $cant}]->(c) ", nm=nombre, consumo=key, cant=value)


def aniadir_consumo(driver, nombre, c_interno, exportaciones, tipo):
    driver.execute_query("CREATE (c:Consumo { name:$n,venta_interna:$i,exportacion:$exp,tipo:$t})", n=nombre,
                         i=c_interno, exp=exportaciones, t=tipo)


def aniadir_puerto(driver, nombre, dpto, desembarque, consumos):
    driver.execute_query("MATCH (d:Departamento) WHERE (d.name=$dp)"
                         "CREATE (p:Puerto {name:$nm,desembarque:$ds})"
                         "CREATE (p)-[:UBICACION]->(d)", nm=nombre, ds=desembarque, dp=dpto)
    for key, value in consumos.items():
        driver.execute_query("MATCH(p:Puerto) MATCH(c:Consumo) WHERE (p.name = $nm AND c.name = $consumo)"
                             "CREATE(p)-[:PRODUCCION {cantidad: $cant}]->(c) ", nm=nombre, consumo=key, cant=value)


def aniadir_dpto(driver, nombre, vab):
    driver.execute_query("CREATE (d:Departamento {name:$nm,val_agregado_bruto:$v})", nm=nombre, v=vab)


def limpiar(driver):
    record, summary, keys = driver.execute_query("MATCH(n)"
                                                 "RETURN COUNT(n) AS c")
    conteo = record[0]["c"]
    if conteo != 0:
        driver.execute_query("MATCH(n)"
                             "DETACH DELETE(n)")


if __name__ == "__main__":
    dv = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
    limpiar(driver=dv)
    # Tipos de consumo
    aniadir_consumo(driver=dv, nombre="Harina de pescado", c_interno=36.8, exportaciones=1191.0, tipo="CHI")
    aniadir_consumo(driver=dv, nombre="Enlatado", c_interno=65.3, exportaciones=19.6, tipo="CHD")
    aniadir_consumo(driver=dv, nombre="Congelado", c_interno=117.3, exportaciones=528.1, tipo="CHD")
    aniadir_consumo(driver=dv, nombre="Curado", c_interno=10.6, exportaciones=51.2, tipo="CHD")
    # Departamentos
    aniadir_dpto(driver=dv, nombre="Áncash", vab=0.20)
    # Especies
    aniadir_especie(driver=dv, nombre="Anchoveta", desembarque=5269216,
                    consumos={"Harina de pescado": 5170189, "Enlatado": 51178, "Congelado": 20176, "Curado": 27004})
    aniadir_especie(driver=dv, nombre="Pota", desembarque=517710, consumos={"Enlatado": 710, "Congelado": 477367})
    aniadir_especie(driver=dv, nombre="Jurel", desembarque=118096,
                    consumos={"Enlatado": 16945, "Congelado": 54867, "Curado": 489})
    aniadir_especie(driver=dv, nombre="Caballa", desembarque=98785,
                    consumos={"Enlatado": 36027, "Congelado": 27783, "Curado": 2397})
    aniadir_especie(driver=dv, nombre="Bonito", desembarque=94158,
                    consumos={"Enlatado": 29724, "Congelado": 3341, "Curado": 369})
    aniadir_especie(driver=dv, nombre="Perico", desembarque=61017,
                    consumos={"Enlatado": 16945, "Congelado": 54867, "Curado": 489})
    aniadir_especie(driver=dv, nombre="Concha de abanico", desembarque=54944, consumos={"Congelado": 54070})
    aniadir_especie(driver=dv, nombre="Merluza", desembarque=46753, consumos={"Congelado": 33524, "Curado": 62})
    aniadir_especie(driver=dv, nombre="Langostino", desembarque=37351, consumos={"Congelado": 34012})
    # Puertos
    aniadir_puerto(driver=dv, nombre="Chimbote", dpto="Áncash", desembarque=1251806,
                   consumos={"Harina de pescado": 1130424, "Enlatado": 67032, "Congelado": 23622, "Curado": 12664})

    dv.close()
