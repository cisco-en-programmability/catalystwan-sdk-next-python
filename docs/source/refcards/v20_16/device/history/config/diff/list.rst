===============================
device.history.config.diff.list
===============================


Operation: GET /dataservice/device/history/config/diff/list
-----------------------------------------------------------


Get diff of two configs

.. code:: python

    def get_config_diff(config_id1: str, config_id2: str) -> Any: ...


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
        client.device.history.config.diff.list.get_config_diff()


