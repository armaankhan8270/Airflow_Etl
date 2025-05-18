
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract_news
from scripts.transform import transform_news
from scripts.load import load_to_db

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'news_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_news',
        python_callable=extract_news,
    )

    transform_task = PythonOperator(
        task_id='transform_news',
        python_callable=transform_news,
    )

    load_task = PythonOperator(
        task_id='load_news_to_db',
        python_callable=load_to_db,
    )

    extract_task >> transform_task >> load_task
