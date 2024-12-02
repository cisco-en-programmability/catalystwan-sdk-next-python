==============================================
sdavc.protocol_pack.compliance.new_application
==============================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/new-application/{deviceUUID}
---------------------------------------------------------------------------------------


Get New Application List for given Device UUID

.. code:: python

    def get_new_application_list(device_uuid: str) -> None: ...


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
        client.sdavc.protocol_pack.compliance.new_application.get_new_application_list()


