=================
dca.system.device
=================


Operation: POST /dataservice/dca/system/device
----------------------------------------------


Get device details

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
        client.dca.system.device.post()


