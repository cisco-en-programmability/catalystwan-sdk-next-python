=====================
device.history.config
=====================


Operation: GET /dataservice/device/history/config
-------------------------------------------------


.. code:: python

    @overload
    def get(device_id: str, query: str) -> Any: ...


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
        client.device.history.config.get()


Operation: GET /dataservice/device/history/config/{config_id}
-------------------------------------------------------------


.. code:: python

    @overload
    def get(config_id: str) -> Any: ...


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
        client.device.history.config.get()


.. toctree::
    :maxdepth: 1

    diff/index

