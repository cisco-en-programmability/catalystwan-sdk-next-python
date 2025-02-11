==============================================================
sdavc.protocol_pack.compliance.application.initiate_compliance
==============================================================


Operation: POST /dataservice/sdavc/protocol-pack/compliance/application/initiate-compliance
-------------------------------------------------------------------------------------------


Initiate application name compliance task

.. code:: python

    def initiate_application_compliance_check() -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.initiate_compliance.initiate_application_compliance_check()


