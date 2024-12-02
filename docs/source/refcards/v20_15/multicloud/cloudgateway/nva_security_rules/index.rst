==========================================
multicloud.cloudgateway.nva_security_rules
==========================================


Operation: GET /dataservice/multicloud/cloudgateway/nvaSecurityRules/{cloudGatewayName}
---------------------------------------------------------------------------------------


Get NVA Security Rules

.. code:: python

    def get_nva_security_rules(
        cloud_gateway_name: str,
    ) -> NvaRulesResponse: ...


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
        client.multicloud.cloudgateway.nva_security_rules.get_nva_security_rules()


Operation: PUT /dataservice/multicloud/cloudgateway/nvaSecurityRules/{cloudGatewayName}
---------------------------------------------------------------------------------------


Update NVA Security Rules

.. code:: python

    def update_nva_security_rules(
        cloud_gateway_name: str, payload: NvaRulesListRequest
    ) -> Taskid: ...


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
        client.multicloud.cloudgateway.nva_security_rules.update_nva_security_rules()


.. toctree::
    :maxdepth: 1

    models

