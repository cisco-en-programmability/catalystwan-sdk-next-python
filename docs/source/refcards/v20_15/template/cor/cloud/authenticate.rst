===============================
template.cor.cloud.authenticate
===============================


Operation: PUT /dataservice/template/cor/cloud/authenticate
-----------------------------------------------------------


Deprecated!!!

Authenticate and update cloud account credentials

.. code:: python

    def authenticate_cred_and_update(
        payload: Optional[Any] = None,
    ) -> Any: ...


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
        client.template.cor.cloud.authenticate.authenticate_cred_and_update()


Operation: POST /dataservice/template/cor/cloud/authenticate
------------------------------------------------------------


Deprecated!!!

Authenticate cloud account credentials

.. code:: python

    def authenticate_cloud_on_ramp_cred_and_add(
        payload: Optional[Any] = None,
    ) -> Any: ...


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
        client.template.cor.cloud.authenticate.authenticate_cloud_on_ramp_cred_and_add()


