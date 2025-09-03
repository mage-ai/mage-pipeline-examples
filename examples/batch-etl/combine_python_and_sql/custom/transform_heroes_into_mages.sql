SELECT 
    a.* 
    , b.intelligence
    , b.intelligence_mean
    , b.intelligence_max
    , b.intelligence_min
    , b.intelligence_median
    , b.strength
    , b.strength_mean
    , b.strength_max
    , b.strength_min
    , b.strength_median
    , b.speed
    , b.speed_mean
    , b.speed_max
    , b.speed_min
    , b.speed_median
    , b.durability
    , b.durability_mean
    , b.durability_max
    , b.durability_min
    , b.durability_median
    , b.power_mean
    , b.power_max
    , b.power_min
    , b.power_median
    , b.combat
    , b.combat_mean
    , b.combat_max
    , b.combat_min
    , b.combat_median
FROM {{ df_2 }} AS a
INNER JOIN {{ df_1 }} AS b
ON a.id = b.id