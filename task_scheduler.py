import os
import subprocess


def set_task_schedule(freq, time):
    exe_path = os.path.abspath(os.getcwd() + '\\main.py')
    arg = ""
    frequency = freq    # -Once, -Daily, -Weekly, -Monthly, etc.
    set_time = time     # 11am etc.
    action = f'$action = New-ScheduledTaskAction -Execute ${exe_path};'  # -Argument {arg}'
    trigger = f'$trigger = New-ScheduledTaskTrigger ${frequency} -At ${set_time};'
    command = 'Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath "medCSV" -TaskName "medical csv download" -Description "download csv"'
    result = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command", action, "-Command", trigger, "-Command", command], capture_output=True)

    # full_command = f'Register-ScheduledTask -Action New-ScheduledTaskAction -Execute ${exe_path}; -Trigger New-ScheduledTaskTrigger ${frequency} -At ${set_time}; -TaskPath "medCSV" -TaskName "medical csv download" -Description "download csv"'
    # result = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command", full_command], capture_output=True)

    print(result)


set_task_schedule("-Once", "4pm")




