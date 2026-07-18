# Clean feature dataset exercise

`data/raw_orders_dirty_5000.csv` is a deliberately messy 5,000-row retail
orders dataset for data-cleaning practice.

It has these columns:

```text
order_id, customer_id, product, quantity, price, order_date
```

The data includes 150 exact duplicate rows, missing values in several columns,
inconsistent product casing and whitespace, and dates stored as mixed text
formats. Some dates are blank or contain `unknown`.

Regenerate the same dataset at any time with:

```sh
uv run python generate_dataset.py
```

Run the complete cleaning pipeline locally with:

```sh
uv run python main.py
```

It writes `data/clean_orders.csv`, `data/orders_with_features.csv`, and
`data/customer_order_summary.csv`. The same four stages are available in the
Airflow DAG named `cleaning_dataset_pipeline`.
