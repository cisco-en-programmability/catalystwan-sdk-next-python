====================
template.cortex.sync
====================


Operation: POST /dataservice/template/cortex/sync
-------------------------------------------------


Sync WAN Resource Groups

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.cortex.sync.post()


