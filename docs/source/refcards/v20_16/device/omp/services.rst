===================
device.omp.services
===================


Operation: GET /dataservice/device/omp/services
-----------------------------------------------


Get OMP services list

.. code:: python

    def create_omp_services(device_id: str) -> List[Any]: ...


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
        client.device.omp.services.create_omp_services()


