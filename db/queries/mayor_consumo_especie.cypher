MATCH (e:Especie)-[u:USO]->(c:Consumo)
WITH e,u,c
  ORDER BY u.cantidad DESC
WITH e, collect([c.name, u.cantidad]) AS consumos
RETURN e.name AS Especie, consumos[0][0] AS `Uso principal`, consumos[0][1] AS `Cantidad (ton)`