import os
import time
import subprocess
import json
from datetime import datetime
from threading import Thread

class TaskScheduler:
    def __init__(self, config_file='tasks.json'):
        self.config_file = config_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.config_file):
            with open(self.config_file, 'w') as file:
                json.dump([], file)
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def save_tasks(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name, command, schedule_time):
        task = {
            "task_name": task_name,
            "command": command,
            "schedule_time": schedule_time
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task_name}' added.")

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task['task_name'] != task_name]
        self.save_tasks()
        print(f"Task '{task_name}' removed.")

    def run_task(self, task):
        print(f"Running task: {task['task_name']}")
        try:
            subprocess.run(task['command'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running task {task['task_name']}: {e}")

    def schedule_tasks(self):
        while True:
            now = datetime.now().strftime("%H:%M")
            for task in self.tasks:
                if task['schedule_time'] == now:
                    Thread(target=self.run_task, args=(task,)).start()
            time.sleep(60)

def main():
    scheduler = TaskScheduler()
    # Example usage
    scheduler.add_task("Backup", "echo Backup started", "13:30")
    scheduler.add_task("Cleanup", "echo Cleanup started", "14:00")
    scheduler.remove_task("Cleanup")
    scheduler.schedule_tasks()

if __name__ == "__main__":
    main()