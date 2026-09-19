from airflow.sdk import dag, task

@dag(
    dag_id = "first_dag"
)

def firt_dag():
    @task.python
    def first_dag():
        print("This is the first task")

    @task.python
    def second_dag():
        print("This is the second task")

    @task.python
    def third_dag():
        print("This is the third task")
    
    first = first_dag()
    second = second_dag()
    third = third_dag()

    first >> second >> third

firt_dag()