from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.decorators import task, dag


@dag(dag_id='dependencies')
def my_dag():

	t1 = DummyOperator(task_id='t1')
	t2 = DummyOperator(task_id='t2')
	t3 = DummyOperator(task_id='t3')
	t4 = DummyOperator(task_id='t4')

	t1 >> t2 >> t3 >> t4

my_dag()