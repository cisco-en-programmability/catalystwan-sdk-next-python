===========================
device.omp.tlocs.advertised
===========================


Operation: GET /dataservice/device/omp/tlocs/advertised
-------------------------------------------------------


Get advertised TLOCs list (Real Time)

.. code:: python

    def create_advertised_tlocs_list(device_id: str) -> List[Any]: ...


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
        client.device.omp.tlocs.advertised.create_advertised_tlocs_list()


