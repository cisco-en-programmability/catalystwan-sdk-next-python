=====================
dca.cloudservices.otp
=====================


Operation: GET /dataservice/dca/cloudservices/otp
-------------------------------------------------


Get cloud service OTP value

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
        client.dca.cloudservices.otp.get()


Operation: PUT /dataservice/dca/cloudservices/otp
-------------------------------------------------


Update cloud service OTP value

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.dca.cloudservices.otp.put()


