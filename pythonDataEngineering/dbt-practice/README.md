# sales_project

A beginner dbt project that builds a customer order summary from a CSV seed in
a local DuckDB database.

## Prerequisites

Install [uv](https://docs.astral.sh/uv/) and run every command below from this
directory (`pythonDataEngineering/dbt-practice`).

## Profile configuration

dbt looks for connection profiles in `~/.dbt/profiles.yml`. This project uses
the `sales_project` profile below. It has also been created locally for you.

```yml
sales_project:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: dev.duckdb
      schema: main
      threads: 4
```

`dev.duckdb` is created in this project directory the first time dbt connects.
If you need to recreate the profile, copy `profiles.yml.example` to
`~/.dbt/profiles.yml`.

## Run the project

```sh
uv sync
uv run dbt debug
uv run dbt seed
uv run dbt run
uv run dbt test
uv run dbt build
```

`dbt seed` loads `seeds/raw_orders.csv`. `dbt run` builds the `stg_orders` view
and the `customer_order_summary` table. `dbt build` runs the models and their
data tests together.
