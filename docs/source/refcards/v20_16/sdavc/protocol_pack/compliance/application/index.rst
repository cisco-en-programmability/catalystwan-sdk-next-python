==========================================
sdavc.protocol_pack.compliance.application
==========================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/application
----------------------------------------------------------------------


Get default application name compliance details

.. code:: python

    def get_default_application_compliance_details() -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.get_default_application_compliance_details()


Operation: GET /dataservice/sdavc/protocol-pack/compliance/application/{uuid}
-----------------------------------------------------------------------------


Get application name compliance details for given task uuid

.. code:: python

    def get_application_compliance_details(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.get_application_compliance_details()


.. toctree::
    :maxdepth: 1

    initiate_compliance
    is_compliance_detected
    status

