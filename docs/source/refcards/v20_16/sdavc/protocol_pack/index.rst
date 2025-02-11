===================
sdavc.protocol_pack
===================


Operation: GET /dataservice/sdavc/protocol-pack
-----------------------------------------------


Get all protocol packs details

.. code:: python

    def get_all_protocol_packs() -> Any: ...


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
        client.sdavc.protocol_pack.get_all_protocol_packs()


.. toctree::
    :maxdepth: 1

    bases_
    compliance/index
    default
    latest
    maintenance/index

