=====================
certificate.syncvbond
=====================


Operation: GET /dataservice/certificate/syncvbond
-------------------------------------------------


sync vManage UUID to all vBond

.. code:: python

    def syncv_bond() -> str: ...


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
        client.certificate.syncvbond.syncv_bond()


