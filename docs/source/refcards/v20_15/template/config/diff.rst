====================
template.config.diff
====================


Operation: GET /dataservice/template/config/diff/{deviceId}
-----------------------------------------------------------


Generates a JSON object that contains the diff for a given device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.template.config.diff.get()


