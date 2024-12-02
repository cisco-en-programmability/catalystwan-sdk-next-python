==========================
sdavc.protocol_pack.bases_
==========================


Operation: GET /dataservice/sdavc/protocol-pack/base
----------------------------------------------------


Get all base protocol pack details

.. code:: python

    def get_base_system_pack() -> Any: ...


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
        client.sdavc.protocol_pack.bases_.get_base_system_pack()


