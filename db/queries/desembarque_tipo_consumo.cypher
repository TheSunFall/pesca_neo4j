MATCH(c:Consumo)
RETURN c.tipo AS Tipo, SUM(c.exportacion) + SUM(c.venta_interna) AS `Cantidad (ton)`