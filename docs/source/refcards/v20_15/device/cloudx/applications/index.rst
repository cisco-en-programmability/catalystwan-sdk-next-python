==========================
device.cloudx.applications
==========================


Operation: GET /dataservice/device/cloudx/applications
------------------------------------------------------


Get list of cloudexpress applications from device (Real Time)

.. code:: python

    def create_applications_list(
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
        client.device.cloudx.applications.create_applications_list()


.. toctree::
    :maxdepth: 1

    models

