# Task Timer
A Python-driven task timer app enables you to efficiently monitor and manage time for various tasks. It aims to boost productivity with real-time tracking, intuitive CLI commands, and task data storage in CSV format.
## Features

### **Commands**

1. **Run Program**
    
    This is how you get the program started.
    
    ```bash
    python -m task_timer
    ```

2. **Help**

    --Help shows you the commands that you can use and you can use --help with every command to see what you wanted to input

    ```bash
    --help
    ```

3. **Start**
    
    Starts new task timer. You can give your task a name or use the default "task".

    ```bash
    start <name>
    ```

4. **Pause**

    Pause stops the timer. It stops the timer at the time you paused it at.

    ```bash
    pause <name>
    ```

5. **Get-time**

    Get-time displays the all tasks you have started.

    ```bash
    get-time
    ```

6. **End**

    End stops the timer and removes it from the task list.
    
    ```bash
    end <name>
    ```

7. **CSV**
    
    Takes all of your running/pause timers and exports them into a csv file which you can name the default is "TimeSheet.csv"

    ```bash
    csv-timer --filename <name>
    ```

8. **Reset**

    Resets the timer back to now.

    ```bash
    reset <name>
    ```

9. **Exit**

    Exit quits the program.

    ```bash 
    exit
    ```
    
## Usage

