==========================
device.omp.routes.received
==========================


Operation: GET /dataservice/device/omp/routes/received
------------------------------------------------------


Get OMP received routes list (Real Time)

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.device.omp.routes.received.get()


.. toctree::
    :maxdepth: 1

    omp_ipv6

