import subprocess
import os


def set_task_schedule(freq, time):
    exe_path = os.path.abspath(os.getcwd()+'\\main.py')
    arg = ""
    frequency = freq    # -Once, -Daily, -Weekly, -Monthly, etc.
    set_time = time     # 11am etc.
    action = f'$action = New-ScheduledTaskAction -Execute ${exe_path}'  # -Argument {arg}'
    trigger = f'$trigger = New-ScheduledTaskTrigger ${frequency} -At ${set_time}'
    command = 'Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath "medCSV" -TaskName "medical csv download" -Description "download csv"'

    subprocess.run(["powershell", "-Command", action], capture_output=True)
    subprocess.run(["powershell", "-Command", trigger], capture_output=True)
    subprocess.run(["powershell", "-Command", command], capture_output=True)





