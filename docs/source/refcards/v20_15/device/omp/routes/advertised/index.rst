============================
device.omp.routes.advertised
============================


Operation: GET /dataservice/device/omp/routes/advertised
--------------------------------------------------------


Get OMP advertised routes list (Real Time)

.. code:: python

    def create_advertised_routes_list(device_id: str) -> List[Any]: ...


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
        client.device.omp.routes.advertised.create_advertised_routes_list()


.. toctree::
    :maxdepth: 1

    omp_ipv6

