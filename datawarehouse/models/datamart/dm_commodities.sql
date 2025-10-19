with 

commodities AS (
    SELECT  
        * 
    FROM {{ ref ('stg_commodities')}}
)

SELECT 
* 
FROM commodities
