import os
import subprocess

gurobi_keys = {"ava01": "",
"ava04": "",
"ava07": "",
"ava14": "",
"ava15": "",
"ava16": "",
"ava17": "",
"ava18": "",
"ava19": "99006d14-b24a-4080-9eb8-0a2f72246acd",
"ava20": "9396f859-c6ef-4819-95ad-09b35b261404",
"ava21": "c533f38d-1df0-4ce0-affe-e39568851572",
"ava22": "",
"cfp01": "",
"cfp02": "",
"cfp03": "",
"cfp05": "",
"cfp06": "",
"cfpsmall02": "",
"cfpsmall03": "",
"cfpsmall05": "",
"cfpsmall06": "",
"cfpsmall07": "",
"cfpsmall08": "",
"cfpsmall09": "",
"cfpsmall10": "",
"demec02": "",
"demec03": "",
"demec04": "",
"demec06": ""}

curr_machine = os.getenv('HOSTNAME')
 
if curr_machine not in gurobi_keys.keys():
    exit(1)
else:
    if os.path.join(os.path.expanduser("~"), "gurobi_lic", curr_machine):
        pass
    else:
        subprocess.run(["bash", "~/gurobi1300/linux64/bin/grbgetkey", gurobi_keys[curr_machine]])
        os.mkdir(os.path.join("gurobi_lic", curr_machine))
        os.rename("gurobi.lic", os.path.join("gurobi_lic", curr_machine, "gurobi.lic"))
