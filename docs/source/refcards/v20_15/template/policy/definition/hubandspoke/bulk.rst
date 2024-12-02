===========================================
template.policy.definition.hubandspoke.bulk
===========================================


Operation: PUT /dataservice/template/policy/definition/hubandspoke/bulk
-----------------------------------------------------------------------


Create/Edit policy definitions in bulk

.. code:: python

    def save_policy_definition_in_bulk_4(
        payload: Optional[Any] = None,
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
        client.template.policy.definition.hubandspoke.bulk.save_policy_definition_in_bulk_4()


