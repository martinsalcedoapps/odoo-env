#encoding: utf-8
import os

port = '50VV'
db_user = 'odooVV'
db_pass = 'odooVV'
name = "db%s" %(port)
localpath = os.path.abspath(".")

print("STOP DOCKER CONTAINER")
os.system("docker stop %s" %(name))

print("REMOVE DOCKER CONTAINER")
os.system("docker rm %s" %(name))

print("PREPARING DOCKER DB SERVER")
print("PORT: ", port)

cmd  = "docker run --name db%s " %(port)
cmd += "-e POSTGRES_USER=%s " %(db_user)
cmd += "-e POSTGRES_PASSWORD=%s " %(db_pass)
cmd += "-e POSTGRES_DB=postgres "
cmd += "-e PGDATA=/mnt/postgres "
cmd += "-v %s/%s/:/mnt/postgres/ " %(localpath, name)
cmd += "-p %s:5432 " %(port)
cmd += "--restart=always "
cmd += "--shm-size=256m "
cmd += "-d "
cmd += "postgres:15 "

print(cmd)
os.system(cmd)
