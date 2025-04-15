=======================================
dca.template.policy.definition.approute
=======================================


Operation: POST /dataservice/dca/template/policy/definition/approute
--------------------------------------------------------------------


Get template policy definitions

.. code:: python

    def post(payload: Any) -> List[Any]: ...


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
        client.dca.template.policy.definition.approute.post()


