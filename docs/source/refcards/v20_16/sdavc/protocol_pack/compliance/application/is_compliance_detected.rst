=================================================================
sdavc.protocol_pack.compliance.application.is_compliance_detected
=================================================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/application/is-compliance-detected
---------------------------------------------------------------------------------------------


Check if there is any Application Compliance detected in the system

.. code:: python

    def is_application_compliance_detected() -> Any: ...


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
        client.sdavc.protocol_pack.compliance.application.is_compliance_detected.is_application_compliance_detected()


