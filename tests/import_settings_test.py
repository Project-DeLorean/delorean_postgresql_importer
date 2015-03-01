#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
from delorean_postgresql_importer.import_settings import ImportSettings


ENCODING = 'latin1'
DATABASE_TABLE_NAME = 'staging.toilets'


@pytest.mark.usefixtures(
    "toilets_shapefile_path",
    "import_toilets_sql_file_path",
    "post_import_toilets_sql_file_path")
class TestImportSettings:

    def test_init(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        import_setting = ImportSettings(
            ENCODING,
            toilets_shapefile_path,
            import_toilets_sql_file_path,
            DATABASE_TABLE_NAME,
            post_import_toilets_sql_file_path)
        assert import_setting.encoding == ENCODING
        assert import_setting.shapefile == toilets_shapefile_path
        assert import_setting.import_sql_file == import_toilets_sql_file_path
        assert import_setting.database_table_name == DATABASE_TABLE_NAME
        assert import_setting.post_import_sql_file == \
            post_import_toilets_sql_file_path

    def test_init_with_encoding_missing(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(ValueError) as exception_info:
            ImportSettings(
                None,
                toilets_shapefile_path,
                import_toilets_sql_file_path,
                DATABASE_TABLE_NAME,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == "Encoding not set."

    def test_init_with_shapefile_missing(
        self,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(ValueError) as exception_info:
            ImportSettings(
                ENCODING,
                None,
                import_toilets_sql_file_path,
                DATABASE_TABLE_NAME,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == "Shapefile not set."

    def test_init_with_shapefile_not_in_path(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(IOError) as exception_info:
            toilets_shapefile_path += ".wrong"
            ImportSettings(
                ENCODING,
                toilets_shapefile_path,
                import_toilets_sql_file_path,
                DATABASE_TABLE_NAME,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == \
            "Shapefile not found: {0}".format(toilets_shapefile_path)

    def test_init_with_import_toilets_sql_file_missing(
        self,
        toilets_shapefile_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(ValueError) as exception_info:
            ImportSettings(
                ENCODING,
                toilets_shapefile_path,
                None,
                DATABASE_TABLE_NAME,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == "SQL file for import not set."

    def test_init_with_import_toilets_sql_file_not_in_path(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(IOError) as exception_info:
            import_toilets_sql_file_path += ".wrong"
            ImportSettings(
                ENCODING,
                toilets_shapefile_path,
                import_toilets_sql_file_path,
                DATABASE_TABLE_NAME,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == \
            "SQL file for import not found: {0}" \
            .format(import_toilets_sql_file_path)

    def test_init_with_database_table_name_missing(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(ValueError) as exception_info:
            ImportSettings(
                ENCODING,
                toilets_shapefile_path,
                import_toilets_sql_file_path,
                None,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == "Database table name not set."

    def test_init_with_post_import_toilets_sql_file_missing(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path
    ):
        with pytest.raises(ValueError) as exception_info:
            ImportSettings(
                ENCODING,
                toilets_shapefile_path,
                import_toilets_sql_file_path,
                DATABASE_TABLE_NAME,
                None
            )
        assert str(exception_info.value) == "SQL file for post import not set."

    def test_init_with_post_import_toilets_sql_file_not_in_path(
        self,
        toilets_shapefile_path,
        import_toilets_sql_file_path,
        post_import_toilets_sql_file_path
    ):
        with pytest.raises(IOError) as exception_info:
            post_import_toilets_sql_file_path += ".wrong"
            ImportSettings(
                ENCODING,
                toilets_shapefile_path,
                import_toilets_sql_file_path,
                DATABASE_TABLE_NAME,
                post_import_toilets_sql_file_path
            )
        assert str(exception_info.value) == \
            "SQL file for post import not found: {0}" \
            .format(post_import_toilets_sql_file_path)
