=======================
device.omp.synced.peers
=======================


Operation: GET /dataservice/device/omp/synced/peers
---------------------------------------------------


Get OP session list

.. code:: python

    def create_synced_omp_session_list(device_id: str) -> List[Any]: ...


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
        client.device.omp.synced.peers.create_synced_omp_session_list()


