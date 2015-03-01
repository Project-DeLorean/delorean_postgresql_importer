import pytest
import os


@pytest.fixture(scope='module')
def toilets_shapefile_path():
    return os.path.abspath("tests/data/toilets.shp")


@pytest.fixture(scope='module')
def import_toilets_sql_file_path():
    return os.path.abspath("tests/data/import_toilets.sql")


@pytest.fixture(scope='module')
def post_import_toilets_sql_file_path():
    return os.path.abspath("tests/data/post_import_toilets.sql")
