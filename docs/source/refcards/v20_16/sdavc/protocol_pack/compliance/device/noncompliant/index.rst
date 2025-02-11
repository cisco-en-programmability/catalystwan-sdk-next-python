==================================================
sdavc.protocol_pack.compliance.device.noncompliant
==================================================


Operation: POST /dataservice/sdavc/protocol-pack/compliance/device/noncompliant
-------------------------------------------------------------------------------


Get all non compliant devices for given protocol pack and selected device or entire network

.. code:: python

    def get_non_compliant_devices_for_protocol_pack_1(
        payload: Optional[CompliantDeviceRequest] = None,
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
        client.sdavc.protocol_pack.compliance.device.noncompliant.get_non_compliant_devices_for_protocol_pack_1()


Operation: GET /dataservice/sdavc/protocol-pack/compliance/device/noncompliant/{protocolPackName}
-------------------------------------------------------------------------------------------------


Get all non compliant devices for given protocol pack

.. code:: python

    def get_non_compliant_devices_for_protocol_pack(
        protocol_pack_name: str,
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
        client.sdavc.protocol_pack.compliance.device.noncompliant.get_non_compliant_devices_for_protocol_pack()


.. toctree::
    :maxdepth: 1

    models

