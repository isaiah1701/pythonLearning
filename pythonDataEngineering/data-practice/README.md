# Data Practice

## Apache Airflow

### Run it in your browser

From this directory, start Airflow and keep this terminal open:

```sh
make airflow
```

Then open [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser and
sign in:

| Field | Value |
| --- | --- |
| Username | `user` |
| Password | `pass` |

Airflow may take a few seconds to start. When the **DAGs** page appears:

1. Click `practice_pipeline`.
2. Click **Trigger** and confirm the run.
3. Open the **Grid** view to watch `first`, `second`, and `third` finish.

The DAG is enabled automatically on a new local Airflow database. Stop the
server with <kbd>Ctrl</kbd>+<kbd>C</kbd> in the terminal where `make airflow`
is running.

The `practice_pipeline` DAG is loaded from this directory. Once Airflow is
running, you can also trigger it without the browser from a second terminal:

```sh
make airflow-trigger
```

The `cleaning_dataset_pipeline` DAG runs the four stages in
`clean-feature-dataset-exercise/main.py`: read, clean, feature engineering,
and customer summary. Trigger it in the Airflow UI or with:

```sh
make airflow-trigger-cleaning
```

In a second terminal, verify it is responding:

```sh
make airflow-check
```

Airflow's database and logs are kept in `.airflow/`.
