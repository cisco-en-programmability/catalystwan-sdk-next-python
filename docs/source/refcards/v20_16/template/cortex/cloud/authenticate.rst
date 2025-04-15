==================================
template.cortex.cloud.authenticate
==================================


Operation: POST /dataservice/template/cortex/cloud/authenticate
---------------------------------------------------------------


Authenticate Cloud Account Credentials

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.template.cortex.cloud.authenticate.post()


