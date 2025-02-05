============================
smart_licensing.authenticate
============================


Operation: POST /dataservice/smartLicensing/authenticate
--------------------------------------------------------


authenticate user for sle

.. code:: python

    def sleauthenticate(payload: Optional[Any] = None) -> Any: ...


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
        client.smart_licensing.authenticate.sleauthenticate()


