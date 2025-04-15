===========================
sdavc.protocol_pack.default
===========================


Operation: GET /dataservice/sdavc/protocol-pack/default
-------------------------------------------------------


Get all default protocol pack details

.. code:: python

    def get() -> Any: ...


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
        client.sdavc.protocol_pack.default.get()


