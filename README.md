# Odoo Environment Fast Creation
## Download

Clone the repository or download the Working folder.

## Usage

Entering terminal mode, inside the Working folder execute the following command 

```
python3 setup.py <odoo_version> <odoo_type>
```

## Examples
### Odoo16 Community Edition
``` bash
\e[32muser@machine:\e[34m~/Working$\e[0m python3 setup.py 17 ce
```
### Odoo16 Enterprise Edition
``` bash
user@machine:~/Working$ python3 setup.py 17 ee
```
You have to copy the enterprise folder separated

# Installation description

```
Working
   \__ postgres
          \__ db5017
          \__ server_db5017.py
    \__ odoo17
          \__ var_lib_odoo 
          \__ odoo17cece.conf
          \__ server_odoo8017ce.py
```
This script creates 2 folders inside the Working.

`postgres`

`odoo17`

The `postgres` folder contains a `db5017`, this is the postgres data folder to configure PG_DATA.

The `odoo17` is the odoo application server folder. Creates a `var_lib_odoo` for odoo data persistence.

The file `server_db5017.py` contains the docker run command for the container remove / creation / execution

# Running postgres

```bash
user@machine:~/Working/odoo17$ python3 server_db5017.py
```

# Running odoo17
```bash
user@machine:~/Working/postgres$ python3 server_odoo17ce.py
```

