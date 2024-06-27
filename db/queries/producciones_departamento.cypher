MATCH (p:Puerto)-[u:UBICACION]->(d:Departamento)
MATCH (p)-[r:PRODUCCION]->(c:Consumo)
WITH d.name AS dpto, c.name AS consumo, SUM(r.cantidad) AS totalCantidad ORDER BY totalCantidad DESC
WITH dpto, collect([consumo, totalCantidad]) AS producciones
RETURN dpto AS Departamento, producciones AS `Produccion (ton)` ORDER BY dpto DESC
