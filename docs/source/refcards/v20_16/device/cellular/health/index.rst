======================
device.cellular.health
======================


Operation: GET /dataservice/device/cellular/health
--------------------------------------------------


Cellular Health Dashlet

.. code:: python

    def get(
        type_: Optional[TypeParam] = None,
        last_n_hours: Optional[LastNHoursParam] = None,
    ) -> List[CellularHealth]: ...


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
        client.device.cellular.health.get()


.. toctree::
    :maxdepth: 1

    models

