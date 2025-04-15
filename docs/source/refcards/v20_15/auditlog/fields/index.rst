===============
auditlog.fields
===============


Operation: GET /dataservice/auditlog/fields
-------------------------------------------


Get fields and type

.. code:: python

    def get() -> List[GetStatDataFields]: ...


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
        client.auditlog.fields.get()


.. toctree::
    :maxdepth: 1

    models

