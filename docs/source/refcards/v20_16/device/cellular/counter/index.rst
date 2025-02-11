=======================
device.cellular.counter
=======================


Operation: GET /dataservice/device/cellular/counter
---------------------------------------------------


Cellular count dashlet

.. code:: python

    def cellular_count_dashlet(
        type_: Optional[TypeParam] = None,
        last_n_hours: Optional[LastNHoursParam] = None,
    ) -> List[CellularCount]: ...


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
        client.device.cellular.counter.cellular_count_dashlet()


.. toctree::
    :maxdepth: 1

    models

