=====================
device.history.config
=====================


Operation: GET /dataservice/device/history/config
-------------------------------------------------


Get device config history

.. code:: python

    def get_last_thousand_config_list(
        device_id: str, query: str
    ) -> Any: ...


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
        client.device.history.config.get_last_thousand_config_list()


Operation: GET /dataservice/device/history/config/{config_id}
-------------------------------------------------------------


Get device config

.. code:: python

    def get_device_config(config_id: str) -> Any: ...


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
        client.device.history.config.get_device_config()


.. toctree::
    :maxdepth: 1

    diff/index

