import time
from colorama import Fore, Style


class Timer:
    def __init__(self, name):
        # Initialize a Timer object with a name, start time, pause time, and running state
        self.name = name
        self.start_time = None
        self.pause_time = None
        self.is_running = False

    def start(self):
        # Start the timer if it is not already running
        if self.is_running:
            return Fore.GREEN + "Timer is already running!" + Style.RESET_ALL
        self.start_time = time.time()  # Record the current time as the start time
        self.is_running = True
        return Fore.GREEN + "Timer started!" + Style.RESET_ALL

    task_time = None

    def get_time(self):
        # Get the elapsed time since the timer started, considering if it is paused or running
        if self.start_time is None:
            task_time = 0  # Timer hasn't started yet
        elif self.is_running:
            task_time = int(time.time() - self.start_time)  # Calculate running time
        else:
            task_time = int(self.pause_time - self.start_time)  # Calculate paused time
        mins, secs = divmod(task_time, 60)  # Convert time to minutes and seconds
        return f"{mins:02}:{secs:02}"  # Return formatted time string

    def pause(self):
        # Pause the timer and record the current time as pause time
        self.pause_time = time.time()  # Record the current time as pause time
        self.is_running = False
        return Fore.GREEN + f"{self.name} Paused." + Style.RESET_ALL

    def reset(self):
        # Reset the start time and set the timer as running
        self.start_time = time.time()  # Record the current time as the new start time
        self.is_running = True
        return Fore.GREEN + "Timer is Reset." + Style.RESET_ALL

    def end(self):
        # Stop the timer and return the total elapsed time
        if not self.is_running:
            return "Timer is not running."
        task_time = int(time.time() - self.start_time)  # Calculate total elapsed time
        mins, secs = divmod(task_time, 60)  # Convert time to minutes and seconds
        self.start_time = None  # Reset the start time
        self.is_running = False
        return (
            Fore.GREEN
            + f"Timer stopped. Total time: {mins:02}:{secs:02}"
            + Style.RESET_ALL
        )  # Return formatted time string
