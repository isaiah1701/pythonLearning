"""Clean, enrich, and summarise the deliberately messy orders dataset."""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path

import pandas as pd

try:
    from airflow import DAG
    from airflow.providers.standard.operators.python import PythonOperator
except ModuleNotFoundError:
    # This keeps `uv run python main.py` usable in the cleaning project, whose
    # own virtual environment does not need Airflow installed.
    DAG = None
    PythonOperator = None


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"
RAW_ORDERS_PATH = DATA_DIR / "raw_orders_dirty_5000.csv"
CLEAN_ORDERS_PATH = DATA_DIR / "clean_orders.csv"
FEATURE_ORDERS_PATH = DATA_DIR / "orders_with_features.csv"
SUMMARY_PATH = DATA_DIR / "customer_order_summary.csv"


def read_orders() -> None:
    """Read the raw CSV and report its initial shape and missing values."""
    df = pd.read_csv(RAW_ORDERS_PATH)
    logger.info("Read %s rows and %s columns from %s", *df.shape, RAW_ORDERS_PATH.name)
    logger.info("Missing values before cleaning: %s", df.isna().sum().to_dict())


def clean_orders() -> None:
    """Clean data types, missing values, text fields, dates, and duplicates."""
    df = pd.read_csv(RAW_ORDERS_PATH)
    source_rows = len(df)

    df["customer_id"] = df["customer_id"].astype("string").str.strip()
    df["product"] = df["product"].astype("string").str.strip().str.lower()
    df = df.dropna(subset=["customer_id", "product"])

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df = df[df["quantity"].gt(0)]
    df["quantity"] = df["quantity"].astype("int64")

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["price"] = df["price"].fillna(df["price"].median())

    df["order_date"] = pd.to_datetime(
        df["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )
    df = df.dropna(subset=["order_date"])
    df = df.drop_duplicates().reset_index(drop=True)

    df.to_csv(CLEAN_ORDERS_PATH, index=False)
    logger.info(
        "Cleaned %s source rows into %s rows and wrote %s",
        source_rows,
        len(df),
        CLEAN_ORDERS_PATH.name,
    )


def engineer_features() -> None:
    """Create reusable order-value, month, and large-order features."""
    df = pd.read_csv(CLEAN_ORDERS_PATH, parse_dates=["order_date"])
    df["order_value"] = df["quantity"] * df["price"]
    df["month"] = df["order_date"].dt.month
    df["is_large_order"] = df["order_value"] > 400

    df.to_csv(FEATURE_ORDERS_PATH, index=False)
    logger.info("Added features to %s rows and wrote %s", len(df), FEATURE_ORDERS_PATH.name)


def summarise_orders() -> None:
    """Create and save a customer-level revenue summary."""
    df = pd.read_csv(FEATURE_ORDERS_PATH)
    summary = (
        df.groupby("customer_id", as_index=False)
        .agg(
            number_of_orders=("order_id", "count"),
            total_items=("quantity", "sum"),
            total_spent=("order_value", "sum"),
        )
        .sort_values("total_spent", ascending=False)
    )
    summary.to_csv(SUMMARY_PATH, index=False)

    logger.info("Total revenue: £%.2f", df["order_value"].sum())
    logger.info("Large orders: %s", int(df["is_large_order"].sum()))
    logger.info("Wrote %s customer summaries to %s", len(summary), SUMMARY_PATH.name)


def main() -> None:
    read_orders()
    clean_orders()
    engineer_features()
    summarise_orders()


if DAG is not None and PythonOperator is not None:
    with DAG(
        dag_id="cleaning_dataset_pipeline",
        start_date=datetime(2024, 1, 1),
        schedule=None,
        catchup=False,
        default_args={"retries": 2},
        tags=["pandas", "data-cleaning"],
    ) as dag:
        read = PythonOperator(task_id="read_orders", python_callable=read_orders)
        clean = PythonOperator(task_id="clean_orders", python_callable=clean_orders)
        features = PythonOperator(
            task_id="engineer_features", python_callable=engineer_features
        )
        summarise = PythonOperator(task_id="summarise_orders", python_callable=summarise_orders)

        read >> clean >> features >> summarise


if __name__ == "__main__":
    main()
