=========================================================
sdavc.protocol_pack.compliance.initiate_device_compliance
=========================================================


Operation: POST /dataservice/sdavc/protocol-pack/compliance/initiate-device-compliance
--------------------------------------------------------------------------------------


Initiate device compliance task

.. code:: python

    def initiate_device_compliance() -> None: ...


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
        client.sdavc.protocol_pack.compliance.initiate_device_compliance.initiate_device_compliance()


