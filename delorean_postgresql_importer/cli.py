#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import ConfigParser
import click
from connection_settings import *
from import_settings import *
from postgresql_import import PostgresqlImport


@click.command()
@click.option(
    '--db_connection_file',
    prompt='Database connection file',
    default=os.path.expanduser('~/.delorean/db_connection.cfg'),
    help='The database connection settings.'
)
@click.option(
    '--import_config_file',
    prompt='Import configuration file',
    default=os.path.join(os.getcwd(), '../../import_config.ini'),
    help='The config file for this city.'
)
@click.option(
    '--db_table_name',
    prompt='Database table name',
    default='test.temp_import',
    help='Target database table name.'
)
@click.option(
    '--post_import_sql_file',
    required=False,
    prompt='Post import SQL file',
    default=os.path.join(os.getcwd(), '../../post_import.sql'),
    help='SQL file to execute after the import finished.'
)
def import_shapefiles(
    db_connection_file,
    import_config_file,
    db_table_name,
    post_import_sql_file
):
    """
    Runs the Shapefile import.
    """

    config = ConfigParser.ConfigParser()
    config.read([db_connection_file, import_config_file])
    connection_settings = ConnectionSettings.create(config)
    import_settings = ImportSettings.create(
        config, db_table_name, post_import_sql_file)

    # print(connection_settings.__dict__)
    # print(import_settings.__dict__)

    postgresql_import = PostgresqlImport(connection_settings, import_settings)
    # print(postgresql_import.import_command)
    if postgresql_import.import_from_shapefiles():
        postgresql_import.do_post_import()


if __name__ == '__main__':
    import_shapefiles()
