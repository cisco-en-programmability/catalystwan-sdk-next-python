======================
sig.umbrella.child_org
======================


Operation: GET /dataservice/sig/umbrella/childOrg/{type}
--------------------------------------------------------


Get the list of child org IDs given the type management or device

.. code:: python

    def get_child_orgs(type_: str) -> None: ...


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
        client.sig.umbrella.child_org.get_child_orgs()


