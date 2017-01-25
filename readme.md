## Process_checker
By Frederik Tollund Juutilainen for Obscura/Vertigo.

General purpose of process_checker as used in Sukkerkor_Watchdog and Wave_ProcessChecker. Reads a json file of process names and folder locations of apps. If a process of the given name is not running, the appropriate app is opened.

### Process_list.json
process_list.json consists of JSON objects with two values **process_name** and **app_location**. **process_name** is the name of a process running, which can be found using Activity Monitor (OSX) or something similar. **app_location** is the path of the app which should be launched if a process isn't running.

Note that sometimes processes are still running even if the program isn't visibly running. Don't know if this is an issue yet.

### Setup script
Created using python3 in a virtualenv. Create a new virtualenv and install dependencies using pip:

Setup a virtualenv using python3:

```
virtualenv -p python3 venv
```

Activate virtualenv:
```
source venv/bin/activate

```
Install requirements:
```
$ pip install -r requirements.txt
```
Run script:
```
python process_checker.py

```

#### To-do:
* Loop of processes could be more efficient.
