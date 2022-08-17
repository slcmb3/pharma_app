import os
import subprocess


def set_task_schedule(freq, time):
    main_path = os.path.abspath(os.getcwd() + '\\main.py')
    frequency = freq    # -Once, -Daily, -Weekly, -Monthly, etc.
    set_time = time     # 11am etc.
    # action = f'$action = New-ScheduledTaskAction -Execute {main_path} -Argument auto_download;'
    # trigger = f'$trigger = New-ScheduledTaskTrigger ${frequency} -At ${set_time};'
    # command = 'Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath "medCSV" -TaskName "medical csv download" -Description "download csv"'
    # result = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command", action, "-Command", trigger, "-Command", command], capture_output=True)

    full_command = f'Register-ScheduledTask -Action New-ScheduledTaskAction -Execute ${main_path}; ' \
                   f'-Trigger New-ScheduledTaskTrigger ${frequency} -At ${set_time}; -TaskPath "medCSV" -TaskName ' \
                   f'"medical csv download" -Description "download csv"'
    result = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-Command", full_command],
                            capture_output=True)

    print(result)


set_task_schedule("-Once", "4pm")




