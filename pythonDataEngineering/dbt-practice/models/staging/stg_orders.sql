select
    order_id,
    trim(customer_name) as customer_name,
    lower(product) as product,
    quantity,
    price,
    quantity * price as total_amount
from {{ ref('raw_orders') }}
