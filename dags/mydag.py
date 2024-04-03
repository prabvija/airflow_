from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.decorators import task, dag
from datetime import datetime, timedelta



@dag(dag_id='core_dq', start_date=datetime(2021, 1, 1), tags=['test_dq'],catchup=False)
def dag_output():

    task_1 = DummyOperator(task_id='test_1')

    @task
    def extract(task_id='test_2',var=None):
        print(Variable.get("Testing_var"))
        # print(var.json.Testing_var)

    # task_2 = PythonOperator(task_id='test_2',python_callable=_extract, op_args = ['{{var.value.Testing_var}}'])

    task_1 >> extract()

dag_output()