=======================
certificate.list.status
=======================


Operation: GET /dataservice/certificate/list/status
---------------------------------------------------


get certificate data

.. code:: python

    def get() -> List[str]: ...


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
        client.certificate.list.status.get()


