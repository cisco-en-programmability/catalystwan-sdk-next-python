========================================
template.policy.definition.dialpeer.bulk
========================================


Operation: PUT /dataservice/template/policy/definition/dialpeer/bulk
--------------------------------------------------------------------


Create/Edit policy definitions in bulk

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.template.policy.definition.dialpeer.bulk.put()


