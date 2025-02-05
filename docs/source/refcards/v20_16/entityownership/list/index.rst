====================
entityownership.list
====================


Operation: GET /dataservice/entityownership/list
------------------------------------------------


List all entity ownership info

.. code:: python

    def list_entity_ownership_info() -> EntityOwnershipInfo: ...


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
        client.entityownership.list.list_entity_ownership_info()


.. toctree::
    :maxdepth: 1

    models

