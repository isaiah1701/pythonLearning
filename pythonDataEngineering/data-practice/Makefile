export PATH := $(HOME)/.local/bin:$(PATH)

UV ?= uv
AIRFLOW_HOME := $(CURDIR)/.airflow
AIRFLOW_HOST := 127.0.0.1
AIRFLOW_PORT := 8080
AIRFLOW_DAGS_FOLDER := $(CURDIR)
AIRFLOW_USER := user
AIRFLOW_PASSWORD := pass
AIRFLOW_PASSWORDS_FILE := $(AIRFLOW_HOME)/simple_auth_manager_passwords.json

.PHONY: airflow airflow-ui airflow-check airflow-trigger airflow-trigger-cleaning

airflow: airflow-ui

airflow-ui:
	@command -v "$(UV)" >/dev/null || { echo "uv is required but was not found on PATH."; exit 1; }
	@mkdir -p "$(AIRFLOW_HOME)"
	@printf '{"$(AIRFLOW_USER)":"$(AIRFLOW_PASSWORD)"}\n' > "$(AIRFLOW_PASSWORDS_FILE)"
	@echo "Starting Apache Airflow at http://$(AIRFLOW_HOST):$(AIRFLOW_PORT) (username: $(AIRFLOW_USER), password: $(AIRFLOW_PASSWORD))"
	AIRFLOW_HOME="$(AIRFLOW_HOME)" AIRFLOW__API__HOST="$(AIRFLOW_HOST)" AIRFLOW__API__PORT="$(AIRFLOW_PORT)" AIRFLOW__CORE__DAGS_FOLDER="$(AIRFLOW_DAGS_FOLDER)" AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION="False" AIRFLOW__CORE__LOAD_EXAMPLES="False" AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_USERS="$(AIRFLOW_USER):admin" AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_ALL_ADMINS="False" AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_PASSWORDS_FILE="$(AIRFLOW_PASSWORDS_FILE)" "$(UV)" run airflow standalone

airflow-check:
	@curl --fail --silent --show-error --output /dev/null --write-out "Airflow returned HTTP %{http_code}\\n" "http://$(AIRFLOW_HOST):$(AIRFLOW_PORT)/"

airflow-trigger:
	AIRFLOW_HOME="$(AIRFLOW_HOME)" AIRFLOW__CORE__DAGS_FOLDER="$(AIRFLOW_DAGS_FOLDER)" AIRFLOW__CORE__LOAD_EXAMPLES="False" "$(UV)" run airflow dags unpause practice_pipeline
	AIRFLOW_HOME="$(AIRFLOW_HOME)" AIRFLOW__CORE__DAGS_FOLDER="$(AIRFLOW_DAGS_FOLDER)" AIRFLOW__CORE__LOAD_EXAMPLES="False" "$(UV)" run airflow dags trigger practice_pipeline

airflow-trigger-cleaning:
	AIRFLOW_HOME="$(AIRFLOW_HOME)" AIRFLOW__CORE__DAGS_FOLDER="$(AIRFLOW_DAGS_FOLDER)" AIRFLOW__CORE__LOAD_EXAMPLES="False" "$(UV)" run airflow dags unpause cleaning_dataset_pipeline
	AIRFLOW_HOME="$(AIRFLOW_HOME)" AIRFLOW__CORE__DAGS_FOLDER="$(AIRFLOW_DAGS_FOLDER)" AIRFLOW__CORE__LOAD_EXAMPLES="False" "$(UV)" run airflow dags trigger cleaning_dataset_pipeline
