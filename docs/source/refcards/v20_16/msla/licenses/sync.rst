==================
msla.licenses.sync
==================


Operation: POST /dataservice/msla/licenses/sync
-----------------------------------------------


Retrieve MSLA subscription/licenses

.. code:: python

    def sync_licenses_1(payload: Optional[Any] = None) -> Any: ...


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
        client.msla.licenses.sync.sync_licenses_1()


