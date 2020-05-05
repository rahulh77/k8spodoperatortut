from __future__ import print_function

import time
from builtins import range
from pprint import pprint

from airflow.utils.dates import days_ago

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

args = {
    'owner': 'Airflow',
    'start_date': days_ago(2),
}

dag = DAG(
    dag_id='test-dynamic-tasks',
    default_args=args,
    schedule_interval=None,
    tags=['example']
)


# [START howto_operator_python]
def print_context(ds, **kwargs):
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'


run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)
# [END howto_operator_python]


# [START howto_operator_python_kwargs]
def my_sleeping_function(random_base):
    """This is a function that will run within the DAG execution"""
    time.sleep(random_base)


# Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
# for i in range(5):
#     task = PythonOperator(
#         task_id='sleep_for_' + str(i),
#         python_callable=my_sleeping_function,
#         op_kwargs={'random_base': float(i) / 10},
#         dag=dag,
#     )
for i in range(5):
    task = KubernetesPodOperator(
        namespace='default',
        image="rahulh77/pyrun",
        arguments=[str(i)],
        labels={"foo": "bar"},
        name="passing-test",
        task_id="passing-task-"+str(i),
        cluster_context='docker-desktop',
        is_delete_operator_pod=True,
        in_cluster=False,
        get_logs=True,
        dag=dag
    )


    run_this >> task
# [END howto_operator_python_kwargs]