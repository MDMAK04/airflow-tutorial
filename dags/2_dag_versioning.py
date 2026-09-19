from airflow.sdk import dag, task

@dag(
    dag_id = "dag_versioning"
)

def dag_versioning():
    @task.python
    def first_dag():
        print("This is the first task")

    @task.python
    def second_dag():
        print("This is the second task")

    @task.python
    def third_dag():
        print("This is the third task")
    
    @task.python
    def versioning_dag():
        print("versioning dag .....")
    
    first = first_dag()
    second = second_dag()
    third = third_dag()
    virsioning = versioning_dag()

    first >> second >> third >> virsioning

dag_versioning()