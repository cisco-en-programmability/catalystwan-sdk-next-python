=======================
certificate.vsmart.list
=======================


Operation: GET /dataservice/certificate/vsmart/list
---------------------------------------------------


get vSmart list

.. code:: python

    def get() -> str: ...


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
        client.certificate.vsmart.list.get()


Operation: POST /dataservice/certificate/vsmart/list
----------------------------------------------------


save vSmart List(handleSendToVbond)

.. code:: python

    def post() -> str: ...


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
        client.certificate.vsmart.list.post()


