===================
dashboard.cci.token
===================


Operation: POST /dataservice/dashboard/cci/token
------------------------------------------------


Get CCI token after Complete CCI Login

.. code:: python

    def cci_token(device_code: Optional[str] = None) -> None: ...


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
        client.dashboard.cci.token.cci_token()


