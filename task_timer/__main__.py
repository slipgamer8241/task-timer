import os  # Provides a way of using operating system dependent functionality like clearing the terminal screen
import time  # Provides various time-related functions
import csv  # Provides functionality to read from and write to CSV files
from tabulate import tabulate  # Used to create nicely formatted tables in the terminal
import click  # A package for creating command-line interfaces
from task_timer.timer import Timer  # Import the Timer class from the timer module
from colorama import Fore, Style  # Import color and style utilities from colorama to colorize terminal output

# List to hold all timer instances
all_timers = []

def csv_write(filename, timers):
    """Write a list of dictionaries to a CSV file."""
    if timers == []:
        # If there are no timers, print a message and return
        click.echo(Fore.RED + "No data to write!" + Style.RESET_ALL)
        return

    # Write the list of timers to a CSV file
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=timers[0].keys())  # Use the keys from the first dictionary as CSV headers
        writer.writeheader()
        writer.writerows(timers)  # Write all timer dictionaries as rows in the CSV file

def get_timer_obj(name):
    """Get a timer object by name. Returns tuple (object, index) or (None, -1) if not found."""
    for index, obj in enumerate(all_timers):
        if name == obj.name:
            return obj, index  # Return the timer object and its index if found
    return None, -1  # Return None and -1 if not found

def obj_list_to_dict_list(timers, export=False):
    """Convert a list of timer objects to a list of dictionaries for display or export."""
    new_list = []
    for i in timers:
        if export:
            timer_dict = {
                'Task Name':  i.name,
                'Timer': str(i.get_time())  # Convert time to string for CSV export
            }
        else:
            timer_dict = {
                'Task Name': Fore.BLUE + i.name + Style.RESET_ALL,
                'Timer': Fore.GREEN + str(i.get_time()) + Style.RESET_ALL if i.is_running else
                Fore.RED + str(i.get_time()) + Style.RESET_ALL  # Colorize based on running state
            }
        new_list.append(timer_dict)
    return new_list

@click.group(invoke_without_command=True)
def timer():
    """A constantly running Timer CLI."""
    pass

@timer.command()
@click.argument("name", required=False, default="task")
def start(name: str):
    """Start a new timer with the given name."""
    timer_obj = Timer(name)
    all_timers.append(timer_obj)
    click.echo(timer_obj.start())  # Start the timer and print the start message

@timer.command()
@click.argument("name", required=True)
def pause(name: str):
    """Pause a running timer."""
    timer_obj, index = get_timer_obj(name)
    if timer_obj:
        click.echo(timer_obj.pause())  # Call the pause method on the timer
    else:
        click.echo(Fore.RED + f"No timer found with the name '{name}'." + Style.RESET_ALL)

@timer.command()
def get_time():
    """Continuously display the elapsed time for all timers."""
    try:
        while True:
            timers = obj_list_to_dict_list(all_timers)
            table = Fore.WHITE + tabulate(timers, headers='keys', tablefmt="github") + Style.RESET_ALL
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            click.echo(Fore.WHITE + "Press Ctrl+C to stop showing the timer/get out of the tasks." + Style.RESET_ALL)
            click.echo(table)
            time.sleep(1)  # Refresh every second
    except KeyboardInterrupt:
        click.echo(Fore.WHITE + "\nStopped showing the timer." + Style.RESET_ALL)

@timer.command()
@click.argument("name", required=True)
def end(name):
    """Stop and remove a timer."""
    timer_obj, index = get_timer_obj(name)
    if timer_obj:
        click.echo(timer_obj.end())  # Call the end method on the timer
        all_timers.pop(index)  # Remove the timer from the list
    else:
        click.echo(Fore.RED + f"No timer found with the name '{name}'." + Style.RESET_ALL)

@timer.command()
@click.argument("name", required=True)
def reset(name: str):
    """Reset a timer's elapsed time."""
    timer_obj, index = get_timer_obj(name)
    if timer_obj:
        click.echo(timer_obj.reset())  # Call the reset method on the timer
    else:
        click.echo(Fore.RED + f"No timer found with the name '{name}'." + Style.RESET_ALL)

@timer.command()
@click.option("--filename", required=False, default="TimeSheet.csv", help="Name your TimeSheet (outputs a .csv)")
def csv_time(filename):
    """Export all timers to a CSV file."""
    timer_list = obj_list_to_dict_list(all_timers, export=True)
    csv_write(filename, timer_list)
    click.echo(Fore.GREEN + "Timesheet has been Exported!" + Style.RESET_ALL)

def main():
    """The main function to start the Timer CLI."""
    click.echo("Timer CLI started! Type 'exit' to quit.")
    while True:
        try:
            command = input(Fore.LIGHTYELLOW_EX + "task_timer> " + Style.RESET_ALL)
            if command.strip() == "exit":
                click.echo(Fore.CYAN + "Exiting Timer CLI. Goodbye!" + Style.RESET_ALL)
                break
            if command.strip():
                timer.main(args=command.split(), standalone_mode=False)  # Process command-line input
        except Exception as e:
            click.echo(Fore.RED + f"Error: {e}" + Style.RESET_ALL)  # Catch errors and display message
        except KeyboardInterrupt:
            click.echo(Fore.CYAN + "Exiting Timer CLI. Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()  # Start the CLI when the script is executed