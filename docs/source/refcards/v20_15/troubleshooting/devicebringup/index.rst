=============================
troubleshooting.devicebringup
=============================


Operation: GET /dataservice/troubleshooting/devicebringup
---------------------------------------------------------


Debug device bring up

.. code:: python

    def get_device_configuration(uuid: str) -> GetDeviceConfiguration: ...


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
        client.troubleshooting.devicebringup.get_device_configuration()


.. toctree::
    :maxdepth: 1

    models

