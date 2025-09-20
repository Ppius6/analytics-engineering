WITH product_base AS (
    SELECT 
        id AS product_id,
        name AS product_name,
        category AS product_category,
        brand AS product_brand,
        department AS product_department,
        sku AS product_sku,
        cost AS product_cost,
        retail_price AS product_retail_price,
        distribution_center_id
    FROM {{ ref('stg_looker__products') }}
)

, inventory_items AS (
    SELECT 
        product_id,
        SUM(CASE WHEN sold_at is NOT NULL THEN cost END) AS cost_of_goods_sold
    FROM {{ ref('stg_looker__inventory_items') }}
    -- WHERE sold_at IS NULL
    GROUP BY 1
)

, order_items AS (
    SELECT 
        product_id,
        SUM(sale_price) AS sales_amount
    FROM {{ ref('stg_looker__order_items') }}
    GROUP BY 1    
)

SELECT 
    pb.product_id,
    -- product dimensions
    pb.product_name,
    pb.product_category,
    pb.product_brand,
    pb.product_department,
    pb.product_sku,
    pb.distribution_center_id,
    -- pricing information
    pb.product_cost,
    pb.product_retail_price,
    -- financial metrics
    COALESCE(oi.sales_amount, 0) AS total_sales_amount,
    COALESCE(ii.cost_of_goods_sold, 0) AS total_cost_of_goods_sold,
    COALESCE(oi.sales_amount, 0) - COALESCE(ii.cost_of_goods_sold, 0) AS total_profit,
    -- margin calculations
    CASE 
        WHEN COALESCE(oi.sales_amount, 0) > 0 
        THEN (COALESCE(oi.sales_amount, 0) - COALESCE(ii.cost_of_goods_sold, 0)) / oi.sales_amount 
        ELSE 0 
    END AS profit_margin
FROM product_base pb 
LEFT JOIN inventory_items ii 
    ON pb.product_id = ii.product_id 
LEFT JOIN order_items oi 
    ON pb.product_id = oi.product_id