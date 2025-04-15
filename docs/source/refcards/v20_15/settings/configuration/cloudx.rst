=============================
settings.configuration.cloudx
=============================


Operation: GET /dataservice/settings/configuration/cloudx
---------------------------------------------------------


Deprecated!!!

Retrieve cloudx configuration value

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
        client.settings.configuration.cloudx.get()


Operation: PUT /dataservice/settings/configuration/cloudx
---------------------------------------------------------


Deprecated!!!

Update cloudx configuration setting

.. code:: python

    def put(payload: str) -> Any: ...


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
        client.settings.configuration.cloudx.put()


Operation: POST /dataservice/settings/configuration/cloudx
----------------------------------------------------------


Deprecated!!!

Add new cloudx configuration

.. code:: python

    def post(payload: str) -> str: ...


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
        client.settings.configuration.cloudx.post()


