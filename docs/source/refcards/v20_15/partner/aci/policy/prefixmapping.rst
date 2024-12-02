================================
partner.aci.policy.prefixmapping
================================


Operation: GET /dataservice/partner/aci/policy/prefixmapping/{partnerId}
------------------------------------------------------------------------


Get prefix mapping

.. code:: python

    def get_data_prefix_mappings(partner_id: str) -> Any: ...


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
        client.partner.aci.policy.prefixmapping.get_data_prefix_mappings()


Operation: POST /dataservice/partner/aci/policy/prefixmapping/{partnerId}
-------------------------------------------------------------------------


Create data prefix mapping

.. code:: python

    def set_data_prefix_mappings(
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
        client.partner.aci.policy.prefixmapping.set_data_prefix_mappings()


