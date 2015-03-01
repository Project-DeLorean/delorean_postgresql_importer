#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


__all__ = ["ImportSettings"]


class ImportSettings(object):
    """
    Encapsulates import settings.
    """

    def __init__(
        self,
        encoding,
        shapefile,
        import_sql_file,
        database_table_name,
        post_import_sql_file
    ):
        """
        Constructor

        Parameters
        ----------
        encoding : String
            Character encoding of the Shapefile.
        shapefile : String
            Shapefile which contains the data. Specify the .shp file here.
        import_sql_file : String
            SQL file to execute the actual database import.
        database_table_name : String
            Name of the target database table.
        post_import_sql_file : String
            SQL file to execute after the import finished.
        """
        self.encoding = encoding
        self.shapefile = shapefile
        self.import_sql_file = import_sql_file
        self.database_table_name = database_table_name
        self.post_import_sql_file = post_import_sql_file

        self.validate_settings()

    def validate_settings(self):
        """
        Test if settings are actually present.
        Tests if external files used in the script exist.
        Raises an exception if a file is missing.
        """
        if not self.encoding:
            raise ValueError("Encoding not set.")

        if not self.shapefile:
            raise ValueError("Shapefile not set.")
        if not os.path.exists(self.shapefile):
            raise IOError("Shapefile not found: {0}"
                          .format(self.shapefile))

        if not self.import_sql_file:
            raise ValueError("SQL file for import not set.")
        if not os.path.exists(self.import_sql_file):
            raise IOError("SQL file for import not found: {0}"
                          .format(self.import_sql_file))

        if not self.database_table_name:
            raise ValueError("Database table name not set.")

        if not self.post_import_sql_file:
            raise ValueError("SQL file for post import not set.")
        if not os.path.exists(self.post_import_sql_file):
            raise IOError("SQL file for post import not found: {0}"
                          .format(self.post_import_sql_file))

    @classmethod
    def create(klass, config, database_table_name, post_import_sql_file):
        """
        Returns an instance for the class.

        Parameters
        ----------
        config : ConfigParser
            Configuration object compiled with ConfigParser.
        database_table_name : String
            Name of the target database table.
        post_import_sql_file : String
            SQL file to execute after the import finished.
        """
        encoding = config.get("ImportSettings", "encoding")
        shapefile = os.path.abspath(config.get("ImportSettings", "shapefile"))
        import_sql_file = os.path.abspath(
            config.get("ImportSettings", "import_sql_file"))
        return ImportSettings(
            encoding,
            shapefile,
            import_sql_file,
            database_table_name,
            post_import_sql_file
        )
