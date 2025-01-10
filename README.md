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
```
python3 setup.py 17 ce
```
### Odoo16 Enterprise Edition
``` 
python3 setup.py 17 ee
```
You have to copy the enterprise folder separated

# Installation description

This script creates 2 folders inside the Working.

postgres

odooXX 

The 'postgres' folder contains a db50XX, this is the postgres data folder to configure PG_DATA.

The odooXX is the odoo application server folder. Creates a var_lib_odoo for odoo data persistence.



