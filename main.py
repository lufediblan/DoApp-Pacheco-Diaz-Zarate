from task_model import TaskModel

def main():
    task_model = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_completed()
    print(f"Tarea completada: {task.is_completed()}")

    task = TaskModel ("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")

    task.set_done()
    print(f"Tarea completada: {task.is_done()}")

    task.remove_task()
    print(f"Tarea eliminada: {task.get_task_name()}")

if __name__ == "_main_":
    main()