import os
import subprocess


def set_task_schedule(freq, time):
    main_path = os.path.abspath(os.getcwd() + '\\main.py')
    frequency = freq    # -Once, -Daily, -Weekly, -Monthly, etc.
    set_time = time     # 11am etc.

    full_command = f'Register-ScheduledTask -Action New-ScheduledTaskAction -Execute ${main_path}; ' \
                   f'-Trigger New-ScheduledTaskTrigger ${frequency} -At ${set_time}; -TaskPath "medCSV" -TaskName ' \
                   f'"medical csv download" -Description "download csv"'
    result = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command", full_command],
                            capture_output=True)

    print(result)


# set_task_schedule("-Once", "4pm")




