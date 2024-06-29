MATCH(p:Puerto)-[r:PRODUCCION]->(:Consumo)
MATCH(p)-[:UBICACION]->(d:Departamento)
RETURN d.name AS Departamento,round(d.val_agregado_bruto*100,2) AS `Valor Agregado Bruto (%)`, SUM(r.cantidad) AS `Desembarque (ton)`
  ORDER BY `Desembarque (ton)` DESC