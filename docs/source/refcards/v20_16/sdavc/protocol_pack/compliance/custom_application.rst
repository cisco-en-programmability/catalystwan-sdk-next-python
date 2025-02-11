=================================================
sdavc.protocol_pack.compliance.custom_application
=================================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/custom-application
-----------------------------------------------------------------------------


Get All Custom Applications

.. code:: python

    def get_custom_application_list() -> Any: ...


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
        client.sdavc.protocol_pack.compliance.custom_application.get_custom_application_list()


