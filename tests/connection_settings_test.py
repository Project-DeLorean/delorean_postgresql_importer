#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
from delorean_postgresql_importer.connection_settings import ConnectionSettings


DB_USER_NAME = 'john'
DB_PASSWORD = 'secret'
DB_NAME = 'my_database'


class TestConnectionSettings:

    def test_init(self):
        connection_settings = ConnectionSettings(
            DB_USER_NAME, DB_PASSWORD, DB_NAME)
        assert connection_settings.database_user_name == DB_USER_NAME
        assert connection_settings.database_password == DB_PASSWORD
        assert connection_settings.database_name == DB_NAME

    def test_init_with_user_name_missing(self):
        with pytest.raises(ValueError) as exception_info:
            ConnectionSettings(None, DB_PASSWORD, DB_NAME)
        assert str(exception_info.value) == "Database user name not set."

    def test_init_with_password_missing(self):
        with pytest.raises(ValueError) as exception_info:
            ConnectionSettings(DB_USER_NAME, None, DB_NAME)
        assert str(exception_info.value) == "Database password not set."

    def test_init_with_database_name_missing(self):
        with pytest.raises(ValueError) as exception_info:
            ConnectionSettings(DB_USER_NAME, DB_PASSWORD, None)
        assert str(exception_info.value) == "Database name not set."
