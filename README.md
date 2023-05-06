# Requestly

Requestly to made up to two parts: 
- requestly.py
    - a volumetric & cache busting DDoS simulator 
- background_traffic.py
    - a tool to generate low RPS background traffic over hours. 
## Setup - Local
- Make sure Python 3.10 + is installed 
- Run Pipenv update 

# Setup - Ansible
- confirm the host group and user the playbook will run on and as.
- Run `setup-server.yml` against the group configured in the playbook 
- If you need to update the repo, run the `update_rep.yml` playbook. 

# RunTime Arguments 

## Requestly.py

### Local
```
--host : The hostname of the site to run against
--path : The path to target 
-m : can be either GET or POST
-t : time in seconds to run for
-ty : type of attack volumetric or cache-bust

```
### Via Ansible Playbook 
Use `run-requestly.yml`

```
--extra-vars="host=<host> path=<path> method=<method> time=<time> type=<type>" 
```

## background_traffic 
configure the paths to run against in the file `lists.py`

### Local

```
--host : The hostname of the site to run against
-t : time in hours to run for
```
### Via Ansible Playbook
Use `run-background-traffic.yml`

```
--extra-vars="host=<host> path=<path> method=<method> time=<time> type=<type>" 
```
