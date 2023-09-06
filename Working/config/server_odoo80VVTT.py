# encoding: utf-8
import os

port = '80VV'
name = 'odooVVTT'
dblink = 'db50VV'
localpath = os.path.abspath(".")

print("STOP DOCKER CONTAINER")
os.system("docker stop %s" % (name))

print("REMOVE DOCKER CONTAINER")
os.system("docker rm %s" % (name))

cmd = "docker run "
cmd += '--name %s ' % (name)
cmd += '-v %s/odooVVTT.conf:/etc/odoo/odoo.conf ' % (localpath)
if name.endswith("ee"):
    cmd += '-v %s/enterprise:/mnt/enterprise ' % (localpath)
cmd += '-v %s/extra-addons-py:/mnt/extra-addons ' % (localpath)
cmd += '-v %s/var_lib_odoo:/var/lib/odoo ' % (localpath)

cmd += '-p %s:8069 ' % (port)
cmd += '--link %s:db ' % (dblink)
cmd += '-t odoo:VV.0 '

vcmd = cmd
vcmd = vcmd.replace("-v ", "\n-v ")
vcmd = vcmd.replace("-p ", "\n-p ")
print(vcmd)
os.system(cmd)
