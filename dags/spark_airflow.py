from airflow import DAG
import airflow
from airflow.operators.python import PythonOperator 
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id='sparkinflow',
    default_args={
        "owner": "anass mouozun",
        "start_date":airflow.utils.dates.days_ago(1),
    },
    schedule_interval='@daily'
)

start = PythonOperator(
    task_id='start',
    python_callable=lambda: print('Job started'),
    dag=dag
)

python_job = SparkSubmitOperator(
    task_id='spark_job',
    conn_id='spark_conn',
    application='/opt/bitnami/spark/jobs/python/wordcountjob.py',
    dag=dag
)


end = PythonOperator(
    task_id='end',
    python_callable=lambda: print('Jpbs finished succecfully'),
    dag=dag
)

start >> python_job >> end  # Define the order of execution