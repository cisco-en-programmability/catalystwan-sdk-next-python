=======================
device.cellular.details
=======================


Operation: GET /dataservice/device/cellular/details
---------------------------------------------------


Cellular count dashlet details

.. code:: python

    def get(
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
        client.device.cellular.details.get()


.. toctree::
    :maxdepth: 1

    models

