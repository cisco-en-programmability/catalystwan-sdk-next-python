==========================
device.cellular.data_usage
==========================


Operation: GET /dataservice/device/cellular/dataUsage
-----------------------------------------------------


Cellular DataUsage Dashlet

.. code:: python

    def data_usage(
        last_n_hours: Optional[LastNHoursParam] = None,
        drill_down: Optional[bool] = None,
    ) -> List[CellularDataUsage]: ...


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
        client.device.cellular.data_usage.data_usage()


.. toctree::
    :maxdepth: 1

    models

