==============================
partner.aci.policy.dscpmapping
==============================


Operation: GET /dataservice/partner/aci/policy/dscpmapping/{partnerId}
----------------------------------------------------------------------


Get DSCP policy

.. code:: python

    def get_dscp_mappings(partner_id: str) -> Any: ...


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
        client.partner.aci.policy.dscpmapping.get_dscp_mappings()


Operation: POST /dataservice/partner/aci/policy/dscpmapping/{partnerId}
-----------------------------------------------------------------------


Create an ACI definition entry

.. code:: python

    def create_dscp_mappings(
        partner_id: str, payload: Optional[Any] = None
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
        client.partner.aci.policy.dscpmapping.create_dscp_mappings()


Operation: DELETE /dataservice/partner/aci/policy/dscpmapping/{partnerId}
-------------------------------------------------------------------------


Delete DSCP mapping

.. code:: python

    def delete_dscp_mappings(partner_id: str) -> Any: ...


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
        client.partner.aci.policy.dscpmapping.delete_dscp_mappings()


