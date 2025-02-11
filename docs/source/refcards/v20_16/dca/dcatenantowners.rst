===================
dca.dcatenantowners
===================


Operation: GET /dataservice/dca/dcatenantowners
-----------------------------------------------


Get DCA tenant owners

.. code:: python

    def get_dca_tenant_owners() -> Any: ...


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
        client.dca.dcatenantowners.get_dca_tenant_owners()


