from airflow import DAG
from datetime import datetime
from airflow.operators.email import EmailOperator

default_args={
    'start_date':datetime(2021,1,1)
}
with DAG(dag_id='my_send_email',default_args=default_args,catchup=False) as dag:
    send_email=EmailOperator(
        task_id='send_to_icloud',
        #to
        to=['xxxxx@xxxx.com'],
        #cc
        cc=['xxxxxx@xxxx.com'],
        #subject
        subject='my send email',
        #content
        html_content='''
        Test email at {}
        '''.format(datetime.now())
        #attachedment
    )

    send_email