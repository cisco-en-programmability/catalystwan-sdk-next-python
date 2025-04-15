=========================
device.tools.factoryreset
=========================


Operation: POST /dataservice/device/tools/factoryreset
------------------------------------------------------


Device factory reset

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.device.tools.factoryreset.post()


