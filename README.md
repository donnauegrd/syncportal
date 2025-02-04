# SyncPortal

SyncPortal is a lightweight Python-based task scheduler designed to automate running scripts or programs at specified times on Windows. It allows you to add, remove, and manage scheduled tasks effortlessly.

## Features

- Schedule tasks to run at specific times.
- Add or remove tasks dynamically.
- Run commands or scripts as scheduled.
- Lightweight and easy to configure.

## Requirements

- Python 3.x
- Windows OS

## Installation

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/yourusername/syncportal.git
    ```

2. Navigate to the project directory:
    ```
    cd syncportal
    ```

3. Install necessary dependencies (if any). This script uses standard Python libraries, so no external packages are required.

## Usage

1. **Add a Task**
   - Modify the `main()` function in `syncportal.py` to add a new task using `add_task(task_name, command, schedule_time)`.
   - `task_name`: A unique name for the task.
   - `command`: The command or script to run.
   - `schedule_time`: The time the task should run in `HH:MM` format (24-hour).

2. **Remove a Task**
   - Use `remove_task(task_name)` to remove an existing task.

3. **Run the Scheduler**
   - Execute the script to start the task scheduler:
     ```
     python syncportal.py
     ```

## Example

```python
scheduler.add_task("Backup", "echo Backup started", "13:30")
scheduler.add_task("Cleanup", "echo Cleanup started", "14:00")
```

## Notes

- Ensure the system time is correctly set on your Windows machine for accurate scheduling.
- You can edit the `tasks.json` file directly to manage tasks, but ensure it is correctly formatted as JSON.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*This project is developed for educational and personal use. Contributions are welcome!*