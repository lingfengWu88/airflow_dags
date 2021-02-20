from airflow import DAG 
from airflow.utils.task_group import TaskGroup
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args={
    'start_date':datetime(2021,2,1)

}

with DAG('parallel_dag',schedule_interval='@daily',default_args=default_args,catchup=False) as dag:
    task_1=BashOperator(
        task_id='task_1',
        bash_command='sleep 3'
    )

    with TaskGroup("section_1") as section_1:
        task_2=BashOperator(
            task_id='task_2',
            bash_command='sleep 3'        
        )

        task_3=BashOperator(
            task_id='task_3',
            bash_command='sleep 3'        
        )

    task_4=BashOperator(
        task_id='task_4',
        bash_command='sleep 3'        
    )

    task_1>> section_1 >>task_4