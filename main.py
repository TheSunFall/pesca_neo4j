from db.setup import SetupDB

if __name__ == "__main__":
    setup = SetupDB("bolt://localhost:7687", "neo4j", "12345678")
    setup.aniadir_consumo(nombre="Harina de pescado", c_interno=36.8, exportaciones=1191.0, tipo="CHI")
    setup.aniadir_consumo(nombre="Enlatado", c_interno=65.3, exportaciones=19.6, tipo="CHD")
    setup.aniadir_consumo(nombre="Congelado", c_interno=117.3, exportaciones=528.1, tipo="CHD")
    setup.aniadir_consumo(nombre="Curado", c_interno=10.6, exportaciones=51.2, tipo="CHD")
    # Departamentos
    setup.aniadir_dpto(nombre="Áncash", vab=0.20)
    # Especies
    setup.aniadir_especie(nombre="Anchoveta", desembarque=5269216,
                          consumos={"Harina de pescado": 5170189, "Enlatado": 51178, "Congelado": 20176,
                                    "Curado": 27004})
    setup.aniadir_especie(nombre="Pota", desembarque=517710, consumos={"Enlatado": 710, "Congelado": 477367})
    setup.aniadir_especie(nombre="Jurel", desembarque=118096,
                          consumos={"Enlatado": 16945, "Congelado": 54867, "Curado": 489})
    setup.aniadir_especie(nombre="Caballa", desembarque=98785,
                          consumos={"Enlatado": 36027, "Congelado": 27783, "Curado": 2397})
    setup.aniadir_especie(nombre="Bonito", desembarque=94158,
                          consumos={"Enlatado": 29724, "Congelado": 3341, "Curado": 369})
    setup.aniadir_especie(nombre="Perico", desembarque=61017,
                          consumos={"Enlatado": 16945, "Congelado": 54867, "Curado": 489})
    setup.aniadir_especie(nombre="Concha de abanico", desembarque=54944, consumos={"Congelado": 54070})
    setup.aniadir_especie(nombre="Merluza", desembarque=46753, consumos={"Congelado": 33524, "Curado": 62})
    setup.aniadir_especie(nombre="Langostino", desembarque=37351, consumos={"Congelado": 34012})
    # Puertos
    setup.aniadir_puerto(nombre="Chimbote", dpto="Áncash", desembarque=1251806,
                         consumos={"Harina de pescado": 1130424, "Enlatado": 67032, "Congelado": 23622,
                                   "Curado": 12664})
    setup.close()
