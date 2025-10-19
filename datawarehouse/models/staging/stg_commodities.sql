-- import 

with source AS (
    SELECT
        "Date", 
        "Close", 
        simbolo
    FROM {{source ('dbsalesaovivo_k7lx', 'commodities')}}
),

-- renamed

renamed AS (
    SELECT 
        CAST ("Date" as date) as data, 
        "Close" AS valor_fechamento, 
        simbolo
    FROM 
        source
)

select * from renamed