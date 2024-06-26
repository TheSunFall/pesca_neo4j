from db.setup import SetupDB

if __name__ == "__main__":
    url = input("Ingrese URL de la base de datos (para AuraDB reemplazar \"neo4j+s://\" por \"neo4j+ssc://\"): ")
    usr = input("Ingrese nombre de usuario en la base de datos (normalmente será \"neo4j\"): ")
    passwd = input("Ingrese contraseña: ")
    setup = SetupDB(uri=url, user=usr, passwd=passwd)
    setup.aniadir_consumo(nombre="Harina de pescado", c_interno=36.8, exportaciones=1191.0, tipo="CHI")
    setup.aniadir_consumo(nombre="Enlatado", c_interno=65.3, exportaciones=19.6, tipo="CHD")
    setup.aniadir_consumo(nombre="Congelado", c_interno=117.3, exportaciones=528.1, tipo="CHD")
    setup.aniadir_consumo(nombre="Curado", c_interno=10.6, exportaciones=51.2, tipo="CHD")
    setup.aniadir_consumo(nombre="Fresco", c_interno=495.6, exportaciones=0, tipo="CHD")

    # Departamentos

    setup.aniadir_dpto(nombre="Áncash", vab=0.20)
    setup.aniadir_dpto(nombre="La Libertad", vab=0.072)
    setup.aniadir_dpto(nombre="Lima", vab=0.224)
    setup.aniadir_dpto(nombre="Piura", vab=0.265)
    setup.aniadir_dpto(nombre="Ica", vab=0.059)
    setup.aniadir_dpto(nombre="Tumbes", vab=0.047)
    setup.aniadir_dpto(nombre="Arequipa", vab=0.09)
    setup.aniadir_dpto(nombre="Moquegua", vab=0.026)

    # Especies

    setup.aniadir_especie(nombre="Anchoveta", desembarque=5269216,
                          consumos={"Harina de pescado": 5170189, "Fresco": 129, "Enlatado": 51178, "Congelado": 20176,
                                    "Curado": 27004})
    setup.aniadir_especie(nombre="Pota", desembarque=517710,
                          consumos={"Fresco": 39633, "Enlatado": 710, "Congelado": 477367})
    setup.aniadir_especie(nombre="Jurel", desembarque=118096,
                          consumos={"Fresco": 45795, "Enlatado": 16945, "Congelado": 54867, "Curado": 489})
    setup.aniadir_especie(nombre="Caballa", desembarque=98785,
                          consumos={"Fresco": 32578, "Enlatado": 36027, "Congelado": 27783, "Curado": 2397})
    setup.aniadir_especie(nombre="Bonito", desembarque=94158,
                          consumos={"Fresco": 60724, "Enlatado": 29724, "Congelado": 3341, "Curado": 369})
    setup.aniadir_especie(nombre="Perico", desembarque=61017,
                          consumos={"Fresco": 19917, "Enlatado": 16945, "Congelado": 54867, "Curado": 489})
    setup.aniadir_especie(nombre="Vegetales (algas)", desembarque=50486, consumos={"Fresco": 1880, "Curado": 48606})
    setup.aniadir_especie(nombre="Concha de abanico", desembarque=54944, consumos={"Fresco": 874, "Congelado": 54070})
    setup.aniadir_especie(nombre="Merluza", desembarque=46753,
                          consumos={"Fresco": 13167, "Congelado": 33524, "Curado": 62})
    setup.aniadir_especie(nombre="Langostino", desembarque=37351, consumos={"Fresco": 3339, "Congelado": 34012})
    setup.aniadir_especie(nombre="Barrilete", desembarque=22082,
                          consumos={"Fresco": 368, "Enlatado": 16948, "Congelado": 4766})
    setup.aniadir_especie(nombre="Lisa", desembarque=17280, consumos={"Fresco": 16050, "Congelado": 3, "Curado": 1227})
    setup.aniadir_especie(nombre="Pejerrey", desembarque=8365, consumos={"Fresco": 6647, "Congelado": 1718})
    setup.aniadir_especie(nombre="Tiburón", desembarque=7901, consumos={"Fresco": 7844, "Congelado": 57})
    setup.aniadir_especie(nombre="Atún", desembarque=5078, consumos={"Fresco": 86, "Enlatado": 1770, "Congelado": 3552})
    setup.aniadir_especie(nombre="Pez volador", desembarque=4851, consumos={"Fresco": 4848, "Congelado": 2})
    setup.aniadir_especie(nombre="Otras especies", desembarque=149286,
                          consumos={"Fresco": 141264, "Enlatado": 1304, "Congelado": 3280, "Curado": 958})
    # Puertos

    setup.aniadir_puerto(nombre="Chimbote", dpto="Áncash", desembarque=1251806,
                         consumos={"Harina de pescado": 1130424, "Fresco": 18063, "Enlatado": 67032, "Congelado": 23622,
                                   "Curado": 12664})
    setup.aniadir_puerto(nombre="Chicama", dpto="La Libertad", desembarque=1213964,
                         consumos={"Harina de pescado": 1213563, "Fresco": 401})
    setup.aniadir_puerto(nombre="Callao", dpto="Lima", desembarque=638949,
                         consumos={"Harina de pescado": 567910, "Fresco": 11896, "Enlatado": 17146, "Congelado": 41907})
    setup.aniadir_puerto(nombre="Coishco", dpto="Áncash", desembarque=556088,
                         consumos={"Harina de pescado": 526974, "Fresco": 205, "7806": 17146, "Congelado": 21103})
    setup.aniadir_puerto(nombre="Paita", dpto="Piura", desembarque=495711,
                         consumos={"Harina de pescado": 52, "Fresco": 22621, "Enlatado": 23020, "Congelado": 447701,
                                   "Curado": 2317})
    setup.aniadir_puerto(nombre="Pisco", dpto="Ica", desembarque=302582,
                         consumos={"Harina de pescado": 252118, "Enlatado": 7256, "Congelado": 35174, "Curado": 8034})
    setup.aniadir_puerto(nombre="Tambo de Mora", dpto="Ica", desembarque=262325,
                         consumos={"Harina de pescado": 243748, "Fresco": 297, "Congelado": 18280})
    setup.aniadir_puerto(nombre="Chancay", dpto="Lima", desembarque=237603,
                         consumos={"Harina de pescado": 236626, "Fresco": 974, "Enlatado": 2})
    setup.aniadir_puerto(nombre="Supe - Puerto Chico", dpto="Lima", desembarque=212707,
                         consumos={"Harina de pescado": 211281, "Fresco": 1213, "Enlatado": 214})
    setup.aniadir_puerto(nombre="Végueta", dpto="Lima", desembarque=202426,
                         consumos={"Harina de pescado": 202269, "Fresco": 157})
    setup.aniadir_puerto(nombre="Ilo", dpto="Moquegua", desembarque=194845,
                         consumos={"Harina de pescado": 159834, "Fresco": 27349, "Enlatado": 5997, "Congelado": 1542,
                                   "Curado": 122})
    setup.aniadir_puerto(nombre="Bayóvar", dpto="Piura", desembarque=158400,
                         consumos={"Harina de pescado": 138609, "Enlatado": 6980, "Congelado": 12811})
    setup.aniadir_puerto(nombre="Carquín - Huacho", dpto="Lima", desembarque=149156,
                         consumos={"Harina de pescado": 138373, "Fresco": 8200, "Enlatado": 2070, "Congelado": 514})
    setup.aniadir_puerto(nombre="Sanmanco", dpto="Áncash", desembarque=69055,
                         consumos={"Harina de pescado": 65142, "Fresco": 1376, "Enlatado": 61, "Congelado": 2476})
    setup.aniadir_puerto(nombre="Matarani", dpto="Arequipa", desembarque=67409,
                         consumos={"Harina de pescado": 37295, "Fresco": 16142, "Enlatado": 4124, "Congelado": 9847})
    setup.aniadir_puerto(nombre="Parachique", dpto="Piura", desembarque=53912,
                         consumos={"Fresco": 13500, "Enlatado": 1250, "Congelado": 37106, "Curado": 2056})
    setup.aniadir_puerto(nombre="Puerto Pizarro", dpto="Tumbes", desembarque=49697,
                         consumos={"Fresco": 36849, "Enlatado": 1266, "Congelado": 11583})
    setup.aniadir_puerto(nombre="Atico", dpto="Arequipa", desembarque=38348,
                         consumos={"Harina de pescado": 17726, "Fresco": 11241, "Enlatado": 2637, "Congelado": 1643,
                                   "Curado": 5128})
    setup.aniadir_puerto(nombre="Caleta La Cruz", dpto="Tumbes", desembarque=37923,
                         consumos={"Fresco": 18804, "Enlatado": 154, "Congelado": 18965})
    setup.aniadir_puerto(nombre="Mollendo", dpto="Arequipa", desembarque=27539,
                         consumos={"Harina de pescado": 27447, "Enlatado": 93})
    setup.aniadir_puerto(nombre="San Nicolás - San Juan", dpto="Áncash", desembarque=21298,
                         consumos={"Fresco": 1514, "Enlatado": 14, "Congelado": 55, "Curado": 19712})
    setup.aniadir_puerto(nombre="San Andrés", dpto="Ica", desembarque=19682,
                         consumos={"Fresco": 18125, "Enlatado": 1436, "Congelado": 122})
    setup.aniadir_puerto(nombre="Pucusana", dpto="Lima", desembarque=21298,
                         consumos={"Fresco": 1514, "Enlatado": 14, "Congelado": 55, "Curado": 19712})

    setup.aniadir_puerto(nombre="Otros puertos/ubicaciones", dpto="N/A", desembarque=301934,
                         consumos={"Harina de pescado": 799, "Fresco": 186156, "Enlatado": 6049, "Congelado": 77787,
                                   "Curado": 31144})

    setup.close()
