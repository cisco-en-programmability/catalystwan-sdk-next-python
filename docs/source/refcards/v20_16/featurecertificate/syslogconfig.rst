===============================
featurecertificate.syslogconfig
===============================


Operation: GET /dataservice/featurecertificate/syslogconfig
-----------------------------------------------------------


Get Feature CA state<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def get() -> Any: ...


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
        client.featurecertificate.syslogconfig.get()


