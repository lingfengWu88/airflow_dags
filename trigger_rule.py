from airflow import DAG

from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'start_date': datetime(2021,1,1)
}

with DAG('trigger_rule',schedule_interval='@daily',default_args=default_args,catchup=False) as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='exit 1',
        do_xcom_push=False
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='exit 1',
        do_xcom_push=False
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='exit 0',
        do_xcom_push=False,
        trigger_rule=TriggerRule.NONE_FAILED_OR_SKIPPED
    )   

    [task_1, task_2] >> task_3