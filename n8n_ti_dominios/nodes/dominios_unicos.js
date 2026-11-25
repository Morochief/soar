// Modo: una vez para todos. Un ítem por dominio aceptado (ya deduplicado).
return $input.first().json.dominios.map(d => ({ json: d, pairedItem: { item: 0 } }));
