=========================
device.cloudx.loadbalance
=========================


Operation: GET /dataservice/device/cloudx/loadbalance
-----------------------------------------------------


Get list of cloudexpress load balance applications from device (Real Time)

.. code:: python

    def get(
        vpn_id: Optional[VpnIdParam] = None,
        application: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Any: ...


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
        client.device.cloudx.loadbalance.get()


.. toctree::
    :maxdepth: 1

    models

