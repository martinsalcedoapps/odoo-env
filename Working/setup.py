import os
import sys
import shutil

allparams = True
if len(sys.argv) != 3:
    print("Missing Parameters <odoo_version> or <odoo_type> ")
    allparams = False

if allparams:
    odoo_version = str(sys.argv[1])
    odoo_type = str(sys.argv[2]).lower()


class Setup(object):

    def initialize(self):
        print("odoo_version: %s" % odoo_version)
        print("odoo_type   : %s" % odoo_type)
        if not (odoo_version in ("14", "15", "16")):
            print("Odoo Version not prepared yet")
            return False
        if not (odoo_type in ("ce", "ee")):
            print("Odoo Version Type not prepared yet")
            return False
        print(odoo_version)
        os.makedirs("postgres/db50%s" % odoo_version, exist_ok=True)
        os.makedirs("odoo%s/var_lib_odoo" % odoo_version, exist_ok=True)

        conf_file = f"odoo{odoo_version}{odoo_type}.conf"
        conf_file_path = f"odoo{odoo_version}/{conf_file}"
        odoo_file = f"server_odoo80{odoo_version}{odoo_type}.py"
        odoo_file_path = f"odoo{odoo_version}/{odoo_file}"
        post_file = f"server_db50{odoo_version}.py"
        post_file_path = f"postgres/{post_file}"

        os.system("sudo chmod -R 777 postgres/ odoo%s/" % odoo_version)
        os.system(f"cp config/odooVVTT.conf %s" % conf_file_path)
        os.system(f"cp config/server_odoo80VVTT.py %s " % odoo_file_path)
        os.system(f"cp config/server_db50VV.py %s" %post_file_path )

        conf_file_obj = open(conf_file_path, "r")
        conf_lines = []
        for line in conf_file_obj:
            if line.startswith("dbfilter = odooVVdemo"):
                line = line.replace("odooVVdemo", f"odoo{odoo_version}demo")
            if line.startswith("db_password = odooVV"):
                line = line.replace("odooVV", f"odoo{odoo_version}")
            if line.startswith("db_user = odooVV"):
                line = line.replace("odooVV", f"odoo{odoo_version}")
            conf_lines.append(line)
        conf_file_obj = open(conf_file_path, "w")
        conf_file_obj.writelines(conf_lines)
        conf_file_obj.close()

        odoo_file_obj = open(odoo_file_path, "r")
        odoo_lines = []
        for line in odoo_file_obj:
            if line.startswith("port = '80VV'"):
                line = line.replace("80VV", f"80{odoo_version}")
            if line.startswith("name = 'odooVVTT'"):
                line = line.replace("odooVVTT", f"80{odoo_version}{odoo_type}")
            if line.startswith("dblink = 'db50VV'"):
                line = line.replace("db50VV", f"db50{odoo_version}")
            if line.startswith("cmd += '-v %s/odooVVTT.conf:/etc/odoo/odoo.conf ' % (localpath)"):
                line = line.replace("odooVVTT", f"odoo{odoo_version}{odoo_type}")
            if line.startswith("cmd += '-t odoo:VV.0 '"):
                line = line.replace("odoo:VV.0", f"odoo:{odoo_version}.0")
            odoo_lines.append(line)
        odoo_file_obj = open(odoo_file_path, "w")
        odoo_file_obj.writelines(odoo_lines)
        odoo_file_obj.close()

        post_file_obj = open(post_file_path, "r")
        post_lines = []
        for line in post_file_obj:
            if line.startswith("port = '50VV'"):
                line = line.replace("50VV", f"50{odoo_version}")
            if line.endswith("'odooVV'\n"):
                line = line.replace("odooVV", f"odoo{odoo_version}")
            post_lines.append(line)
        post_file_obj = open(post_file_path, "w")
        post_file_obj.writelines(post_lines)
        post_file_obj.close()


if allparams:
    setup = Setup()
    setup.initialize()
