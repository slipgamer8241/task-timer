# Task Timer
A Python-driven task timer app enables you to efficiently monitor and manage time for various tasks. It aims to boost productivity with real-time tracking, intuitive CLI commands, and task data storage in CSV format.
## Features

### **Commands**

1. **Run Program**
    <br>
    This is how you get the program started.
    <br>
    ```bash
    python -m task_timer
    ```
    <br>
2. **Help**
    <br>
    --Help shows you the commands that you can use and you can use --help with every command to see what you wanted to input
    <br>
    ```bash
    --help
    ```
    <br>
3. **Start**
    <br>
    Starts new task timer. You can give your task a name or use the default "task".
    <br>
    ```bash
    start <name>
    ```
    <br>
4. **Pause**
    <br>
    Pause stops the timer. It stops the timer at the time you paused it at.
    <br>
    ```bash
    pause <name>
    ```
    <br>
5. **Get-time**
    <br>
    Get-time displays the all tasks you have started.
    <br>
    ```bash
    get-time
    ```
    <br>
6. **End**
    <br>
    End stops the timer and removes it from the task list.
    <br>
    ```bash
    end <name>
    ```
    <br>
7. **CSV**
    <br>
    Takes all of your running/pause timers and exports them into a csv file which you can name the default is "TimeSheet.csv"
    <br>
    ```bash
    csv-timer --filename <name>
    ```
    <br>
8. **Reset**
    <br>
    Resets the timer back to now.
    <br>
    ```bash
    reset <name>
    ```
    <br>
9. **Exit**
    <br>
    Exit quits the program.
    <br>
    ```bash 
    exit
    ```
    <br>
10. **Edit**
    <br>
    Edit can edit by subtracting, adding time or Changing the Name of the timer.
    <br>
    - **Changing name**
    <br>
    ```bash 
    edit-name -name <name> -n <name> #New name
    ```
    <br>
    - **Add time**

    ```bash
    edit-add -name <name> -time <int> #Amount of seconds you want Added
    ```
    - **Subtract time**

    ```bash
    edit-sub -name <name> -time <int> #Amount of seconds you want Subtracting
    ```
## Usage

