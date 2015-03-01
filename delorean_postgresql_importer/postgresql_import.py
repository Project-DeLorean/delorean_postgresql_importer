#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import click
import subprocess


class PostgresqlImport(object):
    """
    Imports Shapefiles into a PostgreSQL database.
    """

    POST_IMPORT_TEMP_FILE = '/tmp/post_import.sql'

    def __init__(self, connection_settings, import_settings):
        """
        Constuctor

        Parameters
        ----------
        connection_settings : ConnectionSettings
            Object encapsulating connection settings.
        import_settings : ImportSettings
            Object encapsulating import settings.
        """
        self.connection_settings = connection_settings
        self.import_settings = import_settings
        self._compose_import_command()

    def _compose_import_command(self):
        """
        Prepares the import command.
        """
        command = 'ogr2ogr -f "PostgreSQL" \
        -lco GEOMETRY_NAME=the_geom \
        PG:"host=localhost \
        user={db_user_name} \
        port=5432 \
        dbname={db_name} \
        password={db_password}" \
        {shapefile} \
        -nln "{db_table_name}" \
        -sql "$(cat {import_sql_file})"'

        self.import_command = command.format(
            db_user_name=self.connection_settings.database_user_name,
            db_name=self.connection_settings.database_name,
            db_password=self.connection_settings.database_password,
            shapefile=self.import_settings.shapefile,
            db_table_name=self.import_settings.database_table_name,
            import_sql_file=self.import_settings.import_sql_file
        )

    def import_from_shapefiles(self):
        """
        Imports data from the Shapefiles and stores it in the database.
        """
        # Set encoding for import specific for file
        # user_defined_encoding = os.environ['PGCLIENTENCODING']
        os.environ['PGCLIENTENCODING'] = self.import_settings.encoding

        click.secho('Starting import now. Stay tuned ...', fg='yellow')
        status = os.system(self.import_command)
        if status == 0:
            click.secho('Finished import.', fg='green')
            return True
        else:
            click.secho('Import failed.', fg='red')
            return False

    def do_post_import(self):
        """
        Executes the SQL script to be run after the import successfully
        finished. Before the script can run the user defined table name
        has to be applied.
        """
        sql_file = open(self.import_settings.post_import_sql_file, 'r')
        sql = sql_file.read()
        sql = sql.replace("test.temp_import",
                          self.import_settings.database_table_name)

        with open(self.POST_IMPORT_TEMP_FILE, 'w') as temp_file:
            temp_file.write(sql)

        os.environ['PGPASSWORD'] = self.connection_settings.database_password

        click.secho('Executing post import SQL file now. \
            Stay calm ...', fg='yellow')

        subprocess.call([
            'psql',
            '-h', 'localhost',
            '-p', '5432',
            '-U', self.connection_settings.database_user_name,
            '-d', self.connection_settings.database_name,
            '-f', self.POST_IMPORT_TEMP_FILE]
        )

        click.secho('Finished post import.', fg='green')
