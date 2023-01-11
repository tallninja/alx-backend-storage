-- SQL
SELECT band_name, (IFNULL(split, 2023) - formed) AS lifespan
FROM metal_bands
WHERE style='Glam rock'
ORDER BY formed DESC;
