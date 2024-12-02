=============
msla.licenses
=============


Operation: GET /dataservice/msla/licenses
-----------------------------------------


Get all the licenses

.. code:: python

    def get_msla_licenses(
        uuid: Optional[str] = None,
    ) -> List[MslaLicensesInner]: ...


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
        client.msla.licenses.get_msla_licenses()


.. toctree::
    :maxdepth: 1

    compliance
    sync
    models

