================================
device.cloudx.application.detail
================================


Operation: GET /dataservice/device/cloudx/application/detail
------------------------------------------------------------


Get list of cloudexpress applications from device (Real Time)

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
        client.device.cloudx.application.detail.get()


.. toctree::
    :maxdepth: 1

    models

