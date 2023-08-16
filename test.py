# import module
import psutil

for process in psutil.process_iter(attrs=['pid', 'name']):
    if process.info['name'] == 'Taskmgr.exe':
        psutil.Process(process.info['pid']).terminate()