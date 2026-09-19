from airflow.sdk import dag, task 
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

FES_TIMEZONE = "Africa/Casablanca"

@dag(
    dag_id="cron_schedule_dag_fes",
    start_date=datetime(year=2026, month=9, day=1, tz=FES_TIMEZONE),
    schedule=CronTriggerTimetable("0 16 * * MON-FRI", timezone=FES_TIMEZONE),
    end_date=datetime(year=2026, month=9, day=30, tz=FES_TIMEZONE),
    is_paused_upon_creation=False,
    catchup=True
)
def cron_schedule_dag():

    @task.python
    def first_task():
        print("Première tâche exécutée à l'heure de Fès !")

    @task.python
    def second_task():
        print("Deuxième tâche en cours...")
    
    @task.python
    def third_task():
        print("Troisième tâche terminée. DAG complet !")
    
    # Définition des dépendances
    first = first_task()
    second = second_task()
    third = third_task()
    
    first >> second >> third

# Instanciation du DAG
cron_schedule_dag()