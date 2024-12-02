=======================
dashboard.cci.authorize
=======================


Operation: POST /dataservice/dashboard/cci/authorize
----------------------------------------------------


Login into CCI

.. code:: python

    def cci_authorize() -> None: ...


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
        client.dashboard.cci.authorize.cci_authorize()


