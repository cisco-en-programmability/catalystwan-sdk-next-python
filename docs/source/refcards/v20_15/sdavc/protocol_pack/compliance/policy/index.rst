=====================================
sdavc.protocol_pack.compliance.policy
=====================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/policy
-----------------------------------------------------------------


Get all policy compliance details

.. code:: python

    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        protocol_pack_name: Optional[str] = None,
    ) -> None: ...


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
        client.sdavc.protocol_pack.compliance.policy.get()


.. toctree::
    :maxdepth: 1

    status

