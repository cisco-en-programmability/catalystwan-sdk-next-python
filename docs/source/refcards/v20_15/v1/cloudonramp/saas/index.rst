===================
v1.cloudonramp.saas
===================


Operation: GET /dataservice/v1/cloudonramp/saas
-----------------------------------------------


Get Cloud On Ramp For Saas apps status

.. code:: python

    def get_cloud_on_ramp_saas_status() -> None: ...


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
        client.v1.cloudonramp.saas.get_cloud_on_ramp_saas_status()


.. toctree::
    :maxdepth: 1

    cloud_tunnels
    configuration
    devices
    inactivesites
    legacydevicelist
    status
    webexsyncstatus

