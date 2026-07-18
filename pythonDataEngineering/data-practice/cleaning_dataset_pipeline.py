"""Expose the cleaning exercise DAG to Airflow's configured DAG folder."""

from __future__ import annotations

import importlib.util
from pathlib import Path


EXERCISE_MAIN = (
    Path(__file__).resolve().parents[1] / "clean-feature-dataset-exercise" / "main.py"
)
module_spec = importlib.util.spec_from_file_location("cleaning_exercise", EXERCISE_MAIN)

if module_spec is None or module_spec.loader is None:
    raise RuntimeError(f"Could not load cleaning exercise from {EXERCISE_MAIN}")

module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
dag = module.dag

if dag is None:
    raise RuntimeError("Airflow is required to create cleaning_dataset_pipeline")
