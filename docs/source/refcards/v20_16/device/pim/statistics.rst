=====================
device.pim.statistics
=====================


Operation: GET /dataservice/device/pim/statistics
-------------------------------------------------


Get PIM statistics list from device

.. code:: python

    def create_pim_statistics_list(device_id: str) -> List[Any]: ...


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
        client.device.pim.statistics.create_pim_statistics_list()


