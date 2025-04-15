============================
smart_licensing.fetch_all_sa
============================


Operation: GET /dataservice/smartLicensing/fetchAllSa
-----------------------------------------------------


fetch reports offline for sle

.. code:: python

    def get(payload: Optional[Any] = None) -> Any: ...


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
        client.smart_licensing.fetch_all_sa.get()


