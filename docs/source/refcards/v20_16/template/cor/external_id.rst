========================
template.cor.external_id
========================


Operation: GET /dataservice/template/cor/externalId
---------------------------------------------------


Deprecated!!!

Get the vManage external ID for AWS

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
        client.template.cor.external_id.get()


