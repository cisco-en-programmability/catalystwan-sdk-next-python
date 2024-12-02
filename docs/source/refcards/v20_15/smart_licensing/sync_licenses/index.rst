=============================
smart_licensing.sync_licenses
=============================


Operation: POST /dataservice/smartLicensing/syncLicenses
--------------------------------------------------------


Deprecated!!!

get all licenses for sa/va

.. code:: python

    def sync_licenses(
        payload: Optional[LicenseUplodFile] = None,
    ) -> Any: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.smart_licensing.sync_licenses.sync_licenses()


.. toctree::
    :maxdepth: 1

    models

