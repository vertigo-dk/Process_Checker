## Process_checker
By Frederik Tollund Juutilainen for Obscura/Vertigo.

General purpose of process_checker as used in Sukkerkor_Watchdog and Wave_ProcessChecker. Reads a json file of process names and folder locations of apps. If a process of the given name is not running, the appropriate app is opened.

### Process_list.json

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
