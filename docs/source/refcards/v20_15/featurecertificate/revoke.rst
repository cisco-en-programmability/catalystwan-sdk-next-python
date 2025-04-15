=========================
featurecertificate.revoke
=========================


Operation: PUT /dataservice/featurecertificate/revoke
-----------------------------------------------------


Revoke feature cert from cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.featurecertificate.revoke.put()


