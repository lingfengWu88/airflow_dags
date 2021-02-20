from airflow import DAG

from datetime import datetime
from airflow.operators.python import PythonOperator
from random import randint

default_args={
    'start_date': datetime(2021,2,2)
}

def _getRandom_(ti):
    curNum = randint(5, 10)
    ti.xcom_push(key='current_float',value=curNum)
    print('get random {}'.format(curNum))


def _doubleValue_(ti):
    #xcom_pull return list
    preNum=ti.xcom_pull(key='current_float',task_ids=['push_xcom'])
    doubleNum=int(preNum[0])*2
    print('previous number is {}, current number is {}'.format(preNum,doubleNum))




with DAG(dag_id='my_python_xcom_dag',schedule_interval='@daily',default_args=default_args,catchup=False) as dag:
    push_xcom = PythonOperator(
        task_id = 'push_xcom',
        python_callable=_getRandom_
    )

    pull_xcom = PythonOperator(
        task_id = 'pull_xcom',
        python_callable=_doubleValue_
    )

    push_xcom >> pull_xcom