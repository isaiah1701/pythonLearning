from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def first():
    print("running first task")


def second():
    print("running second task")


def third():
    print("running third task")


with DAG(
    dag_id="practice_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 2},
) as dag:
    a = PythonOperator(task_id="first", python_callable=first)
    b = PythonOperator(task_id="second", python_callable=second)
    c = PythonOperator(task_id="third", python_callable=third)

    a >> b >> c
