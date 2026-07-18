select
    customer_name,
    count(*) as number_of_orders,
    sum(quantity) as total_items,
    sum(total_amount) as total_spent
from {{ ref('stg_orders') }}
group by customer_name
