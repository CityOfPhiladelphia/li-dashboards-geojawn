# Metabase
This is a simple Flask Application that embeds Metabase dashboards. We built it specifically for GeoJawn 2019.
It's a subset of the internal L&I dashboards: https://github.com/CityOfPhiladelphia/li-metabase


## Requirements
- Python 3.6+
- Pip
- Connections to all of L+I's databases in the form of the li_dbs Python package

## Installation
```bash
$ pip install -r requirements.txt
```
- Get the config.py file from me and replace li_metabase/sample_config.py with it

### Development Web Server
```bash
$ export FLASK_APP=li_metabase
$ export FLASK_ENV=development
$ flask run
```

### Production Web Server
```bash
$ export FLASK_APP=wsgi
$ flask run
```

## ETL
The ETL is structured so that data is queried from our other databases and then dumped to a temporary pickle file. This pickle file is then read and loaded into the cloud database. This setup minimizes how long database connections are open, which had caused a lot of issues previously. This also allows us to look at the data in the pickle file if something fails and understand if the issue was caused due to the data itself.

Run the etl process for all queries 
```bash
$ cd etl
$ python main.py
```
Run the etl process for one dashboard 

```bash
$ cd etl
$ python cli.py -n dashboard_table_name
``` 
Run the etl process for multiple specified dashboards 
```bash
$ cd etl
$ python cli.py -n dashboard_table_name1 -n dashboard_table_name2
``` 
