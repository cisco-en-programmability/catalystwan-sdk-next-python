==========================================
sdavc.protocol_pack.compliance.application
==========================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/application
----------------------------------------------------------------------


.. code:: python

    @overload
    def get() -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.get()


Operation: GET /dataservice/sdavc/protocol-pack/compliance/application/{uuid}
-----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.get()


.. toctree::
    :maxdepth: 1

    initiate_compliance
    is_compliance_detected
    status

