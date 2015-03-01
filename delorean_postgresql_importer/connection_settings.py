#!/usr/bin/env python
# -*- coding: utf-8 -*-


__all__ = ["ConnectionSettings"]


class ConnectionSettings(object):
    """
    Encapsulates database connection settings.
    """

    def __init__(self, database_user_name, database_password, database_name):
        """
        Constructor

        Parameters
        ----------
        database_user_name : String
            User name to access the database.
        database_password : String
            Password to access the database.
        database_name : String
            Name of the database.
        """
        self.database_user_name = database_user_name
        self.database_password = database_password
        self.database_name = database_name

        self.validate_settings()

    def validate_settings(self):
        """
        Tests if settings are actually present.
        Raises exception is any setting is missing.
        """
        if not self.database_user_name:
            raise ValueError("Database user name not set.")
        if not self.database_password:
            raise ValueError("Database password not set.")
        if not self.database_name:
            raise ValueError("Database name not set.")

    @classmethod
    def create(klass, config):
        """
        Returns an instance for the class.

        Parameters
        ----------
        config : ConfigParser
            Configuration object create with a ConfigParser.
        """
        db_user_name = config.get("ConnectionSettings", "db_user_name")
        db_password = config.get("ConnectionSettings", "db_password")
        db_name = config.get("ConnectionSettings", "db_name")
        return ConnectionSettings(db_user_name, db_password, db_name)
