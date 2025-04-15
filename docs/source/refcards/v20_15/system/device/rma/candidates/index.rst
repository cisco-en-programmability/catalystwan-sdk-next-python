============================
system.device.rma.candidates
============================


Operation: GET /dataservice/system/device/rma/candidates/{deviceType}
---------------------------------------------------------------------


Get RMA candidates by device type

.. code:: python

    def get(
        device_type: str, uuid: Optional[str] = None
    ) -> GetRmaCandidates: ...


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
        client.system.device.rma.candidates.get()


.. toctree::
    :maxdepth: 1

    models

