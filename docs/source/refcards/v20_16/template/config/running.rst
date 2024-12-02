=======================
template.config.running
=======================


Operation: GET /dataservice/template/config/running/{deviceId}
--------------------------------------------------------------


Get device running config

.. code:: python

    def get_running_config(device_id: str) -> Any: ...


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
        client.template.config.running.get_running_config()


