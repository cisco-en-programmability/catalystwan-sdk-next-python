================================
device.configuration.commit_list
================================


Operation: GET /dataservice/device/configuration/commit-list
------------------------------------------------------------


Get device commit list

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
        client.device.configuration.commit_list.get()


