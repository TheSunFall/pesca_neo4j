MATCH(p:Puerto)-[r:PRODUCCION]->(c:Consumo)
MATCH(p)-[:UBICACION]->(d:Departamento)
RETURN d.name AS Departamento, SUM(r.cantidad) AS `Desembarque (ton)` ORDER BY `Desembarque (ton)` DESC