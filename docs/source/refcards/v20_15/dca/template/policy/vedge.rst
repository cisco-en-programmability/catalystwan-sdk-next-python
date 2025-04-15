=========================
dca.template.policy.vedge
=========================


Operation: POST /dataservice/dca/template/policy/vedge
------------------------------------------------------


Get vEdge template list

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
        client.dca.template.policy.vedge.post()


