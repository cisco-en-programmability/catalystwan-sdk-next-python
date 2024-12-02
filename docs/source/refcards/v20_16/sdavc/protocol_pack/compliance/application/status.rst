=================================================
sdavc.protocol_pack.compliance.application.status
=================================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/application/status/{uuid}
------------------------------------------------------------------------------------


Get application name compliance task status

.. code:: python

    def get_application_compliance_status(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.status.get_application_compliance_status()


