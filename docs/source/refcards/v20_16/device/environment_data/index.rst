=======================
device.environment_data
=======================


Operation: GET /dataservice/device/environmentData
--------------------------------------------------


get Cisco TrustSec Environment Data information from device

.. code:: python

    def get_environment_data(device_id: str) -> Any: ...


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
        client.device.environment_data.get_environment_data()


.. toctree::
    :maxdepth: 1

    radius_server

