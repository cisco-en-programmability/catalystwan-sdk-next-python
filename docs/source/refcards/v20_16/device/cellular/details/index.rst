=======================
device.cellular.details
=======================


Operation: GET /dataservice/device/cellular/details
---------------------------------------------------


Cellular count dashlet details

.. code:: python

    def cellular_count_dashlet_details(
        last_n_hours: Optional[LastNHoursParam] = None,
    ) -> List[CellularDetail]: ...


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
        client.device.cellular.details.cellular_count_dashlet_details()


.. toctree::
    :maxdepth: 1

    models

