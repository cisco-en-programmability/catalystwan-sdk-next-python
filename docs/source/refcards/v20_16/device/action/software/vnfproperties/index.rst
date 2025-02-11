====================================
device.action.software.vnfproperties
====================================


Operation: GET /dataservice/device/action/software/vnfproperties/{versionId}
----------------------------------------------------------------------------


Get VNF Properties

.. code:: python

    def get_vnf_properties(version_id: str) -> GetVnfProperties: ...


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
        client.device.action.software.vnfproperties.get_vnf_properties()


.. toctree::
    :maxdepth: 1

    models

