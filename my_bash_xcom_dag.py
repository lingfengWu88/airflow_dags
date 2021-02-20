from airflow import DAG

from datetime import datetime
from airflow.operators.bash import BashOperator

default_args={
    'start_date': datetime(2021,2,2)
}

with DAG(dag_id='my_bash_xcom_dag',schedule_interval='@daily',default_args=default_args,catchup=False) as dag:
    push_xcom = BashOperator(
        task_id = 'push_xcom',
        bash_command="pwd"
    )

    
    pull_xcom = BashOperator(
        task_id = 'pull_xcom',
        bash_command="echo {{ ti.xcom_pull(task_ids='push_xcom') }}"       
    )

    push_xcom >> pull_xcom