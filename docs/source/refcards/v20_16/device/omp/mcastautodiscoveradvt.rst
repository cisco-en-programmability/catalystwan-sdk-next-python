================================
device.omp.mcastautodiscoveradvt
================================


Operation: GET /dataservice/device/omp/mcastautodiscoveradvt
------------------------------------------------------------


Get OMP multicast autodiscover advertised list

.. code:: python

    def create_omp_mcast_auto_discover_advt(
        device_id: str,
    ) -> List[Any]: ...


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
        client.device.omp.mcastautodiscoveradvt.create_omp_mcast_auto_discover_advt()


