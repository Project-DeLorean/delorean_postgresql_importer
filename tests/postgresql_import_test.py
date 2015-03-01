#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
from delorean_postgresql_importer.connection_settings import ConnectionSettings
from delorean_postgresql_importer.import_settings import ImportSettings
from delorean_postgresql_importer.postgresql_import import PostgresqlImport


DB_USER_NAME = 'john'
DB_PASSWORD = 'secret'
DB_NAME = 'my_database'
ENCODING = 'latin1'
DATABASE_TABLE_NAME = 'staging.toilets'


@pytest.mark.usefixtures(
    "toilets_shapefile_path",
    "import_toilets_sql_file_path",
    "post_import_toilets_sql_file_path")
class TestPostgresqlImport:

    def test_init(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        connection_settings = ConnectionSettings(
            DB_USER_NAME,
            DB_PASSWORD,
            DB_NAME
        )
        import_settings = ImportSettings(
            ENCODING,
            toilets_shapefile_path,
            import_toilets_sql_file_path,
            DATABASE_TABLE_NAME,
            post_import_toilets_sql_file_path
        )
        postgresql_import = PostgresqlImport(
            connection_settings, import_settings
        )
        command = postgresql_import.import_command
        assert command is not None
        assert toilets_shapefile_path in command
        assert "user={0}".format(DB_USER_NAME) in command
        assert "password={0}".format(DB_PASSWORD) in command
        assert "dbname={0}".format(DB_NAME) in command
        assert "-nln \"{0}\"".format(DATABASE_TABLE_NAME) in command
