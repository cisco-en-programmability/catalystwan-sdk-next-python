=======================
device.cellular.counter
=======================


Operation: GET /dataservice/device/cellular/counter
---------------------------------------------------


Cellular count dashlet

.. code:: python

    def get(
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
        client.device.cellular.counter.get()


.. toctree::
    :maxdepth: 1

    models

