|travisci| |license|


DeLorean PostgreSQL Importer
*****

This Python library wraps ogr2ogr_ commands and
SQL scripts to import ESRI Shapefiles into a PostgreSQL database.
The motivation for writing this library is to automate the import and
to make the process repeatable.


Configuration
=====

To use the library you need to prepare a few configuration files
which are specific to your database or to your Shapefiles.

1. Installation
------

.. code:: shell

    $ pip install path/to/delorean_postgresql_importer --user

or if you use virtualenv_:

.. code:: shell

    $ pip install path/to/delorean_postgresql_importer --ignore-installed


2. Database connection
------

Then manually create a **configurations file** which contains the
sensitive **connection settings** for your PostgreSQL database. The
default location for the file is: *~/.delorean/db_connection.cfg*
since this is a global setting. The file must contain the settings
shown in this example:

.. code:: properties

    [ConnectionSettings]
    db_user_name: john
    db_name: my_pet_project
    db_password: secret


3. Import settings
-----

Then create a configuration file specific to your Shapefiles
which contains the following settings:

.. code:: properties

    [ImportSettings]
    encoding: latin1
    db_table_name: "staging.my_pet_project.toilets"
    shapefile: toilets.shp
    import_sql_file: ../../import_toilets.sql


4. Import SQL file
-----

Further, create an import SQL file specific to your Shapefiles.
The ``import_sql_file`` configured in the ``[ImportSettings]`` contains
the SQL command to transform the geospatial data in any useful way.
Here is an example:

.. code:: sql

    SELECT
    CAST(STRASSE AS character(254)) AS street,
    FROM toilets


5. Post import SQL file
-----

Last, create another SQL file which will be executed after the
database import finished. This allows for any custom actions
such as adding columns. Make sure to use ``test.temp_import`` as
the table name in this SQL script. The table name will automatically
be replaced with what you configured as the ``db_table_name`` in
the ``[ImportSettings]``.


Usage
=====

The script can be started with the following command:

.. code:: shell

    $ delorean_postgresql_importer

The routine will prompt for the **locations of the configuration
and SQL files** prepared before. If you did not setup the files
correctly or just continue with the default locations you will
run into error messages.

Tests
=====

Tests can be executed with the following command:

.. code:: shell

    $ py.test tests


Author
=====

- `Tobias Preuss`_


Contributors
=====

- `Knut Kühne`_


License
=====

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


.. _ogr2ogr: http://www.gdal.org/ogr2ogr.html
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _Tobias Preuss: https://github.com/johnjohndoe
.. _Knut Kühne: https://github.com/k-nut/

.. |travisci| image:: https://travis-ci.org/Project-DeLorean/delorean_postgresql_importer.svg
    :target: https://travis-ci.org/Project-DeLorean/delorean_postgresql_importer
    :alt: Travis CI build status
.. |license| image:: https://img.shields.io/badge/license-AGPLv3%2B-lightgrey.svg
    :target: http://www.gnu.org/licenses/
    :alt: GNU Affero General Public License v3 or later (AGPLv3+)
