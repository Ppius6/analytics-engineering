WITH customer_base AS (
    SELECT 
        user_id,
        -- Take the first gender value for each user (they should be consistent)
        MIN(gender) AS customer_gender
    FROM {{ ref('stg_looker__users')}}
    WHERE user_id IS NOT NULL
    GROUP BY user_id
)

, order_items AS (
    SELECT 
        user_id,
        SUM(sale_price) AS total_amount_spent,
        COUNT(DISTINCT id) AS total_items_purchased,
        MIN(created_at) AS first_order_completed_at,
        MAX(created_at) AS last_order_completed_at
    FROM {{ ref('stg_looker__order_items') }}
    WHERE status = 'Complete'
    GROUP BY 1
)

, orders AS (
    SELECT 
        user_id,
        COUNT(DISTINCT order_id) AS num_orders,
        COUNT(DISTINCT 
            CASE WHEN status = 'Shipped'
            THEN order_id
            END) AS num_orders_shipped,
        COUNT(DISTINCT 
            CASE WHEN status = 'Complete'
            THEN order_id
            END) AS num_orders_complete,
        COUNT(DISTINCT 
            CASE WHEN status = 'Processing'
            THEN order_id
            END) AS num_orders_processing,
        COUNT(DISTINCT 
            CASE WHEN status = 'Cancelled'
            THEN order_id
            END) AS num_orders_cancelled,
        COUNT(DISTINCT 
            CASE WHEN status = 'Returned'
            THEN order_id
            END) AS num_orders_returned
    FROM {{ ref('stg_looker__orders') }}
    GROUP BY 1
)

, web_traffic AS (
    SELECT 
        user_id,
        COUNT(DISTINCT session_id) AS num_web_sessions
    FROM {{ ref('stg_looker__events') }}
    WHERE user_id IS NOT NULL
    GROUP BY 1
)

SELECT
    cb.user_id,
    -- dimensions
    cb.customer_gender,
    -- facts 
    COALESCE(oi.total_amount_spent, 0) AS total_amount_spent,
    COALESCE(oi.total_items_purchased, 0) AS total_items_purchased,
    oi.first_order_completed_at,
    oi.last_order_completed_at,
    COALESCE(o.num_orders, 0) AS num_orders,
    COALESCE(o.num_orders_shipped, 0) AS num_orders_shipped,
    COALESCE(o.num_orders_complete, 0) AS num_orders_complete,
    COALESCE(o.num_orders_processing, 0) AS num_orders_processing,
    COALESCE(o.num_orders_cancelled, 0) AS num_orders_cancelled,
    COALESCE(o.num_orders_returned, 0) AS num_orders_returned,
    COALESCE(wt.num_web_sessions, 0) AS num_web_sessions
FROM customer_base cb
LEFT JOIN order_items oi 
    ON cb.user_id = oi.user_id
LEFT JOIN orders o
    ON cb.user_id = o.user_id 
LEFT JOIN web_traffic wt 
    ON cb.user_id = wt.user_id
