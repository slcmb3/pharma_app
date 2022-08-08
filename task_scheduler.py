# from rocketry import Rocketry
# pywin32 / rocketry /
import subprocess

def set_task_schedule(freq, time):
    exe_path = 'C:\\Users\\nathh\\PycharmProjects\\pharma_app\\main.py'
    arg = ""
    frequency = freq    # -Once, -Daily, -Weekly, -Monthly, etc.
    set_time = time     # 11am etc.
    action = f'$action = New-ScheduledTaskAction -Execute ${exe_path}'  # -Argument {arg}'
    trigger = f'$trigger = New-ScheduledTaskTrigger ${frequency} -At ${set_time}'
    command = 'Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath "medCSV" -TaskName "medical csv download" -Description "download csv"'
    full_command = f'Register-ScheduledTask -Action New-ScheduledTaskAction -Execute ${exe_path} -Trigger New-ScheduledTaskTrigger ${frequency} -At ${set_time} -TaskPath "medCSV" -TaskName "medical csv download" -Description "download csv"'

    subprocess.run(["powershell", "-Command", action], capture_output=True)
    subprocess.run(["powershell", "-Command", trigger], capture_output=True)
    subprocess.run(["powershell", "-Command", command], capture_output=True)


def test_task():
    action = "$action = New-ScheduledTaskAction -Execute 'notepad.exe'"
    trigger = '$trigger = New-ScheduledTaskTrigger -Daily -At 4pm'
    command = 'Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath "MyTasks" -TaskName "testTask" -Description "This task opens the Notepad editor"'
    # subprocess.run(["powershell", "-Command", command], capture_output=True)


test_task()
# set_task_schedule("-Once", "4pm")




