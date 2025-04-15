==========================================
v1.service_insertion.service_chain_mapping
==========================================


Operation: GET /dataservice/v1/service-insertion/service-chain-mapping
----------------------------------------------------------------------


Gets all the Service Chain Mapping with service chain definition name and service chain number.

.. code:: python

    def get() -> List[Any]: ...


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
        client.v1.service_insertion.service_chain_mapping.get()


