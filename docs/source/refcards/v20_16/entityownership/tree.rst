====================
entityownership.tree
====================


Operation: GET /dataservice/entityownership/tree
------------------------------------------------


Entity ownership info grouped by buckets

.. code:: python

    def entity_ownership_info() -> Any: ...


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
        client.entityownership.tree.entity_ownership_info()


