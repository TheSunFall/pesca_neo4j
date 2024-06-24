MATCH (e:Especie)-[u:USO]->(c:Consumo)
WITH e,u,c
  ORDER BY u.cantidad DESC
WITH e, collect({consumo:c, cantidad: u.cantidad}) AS consumos
RETURN e.name AS Especie, consumos[0].consumo.name AS `Uso principal`, (consumos[0].cantidad) AS `Cantidad (ton)`