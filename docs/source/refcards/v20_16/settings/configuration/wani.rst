===========================
settings.configuration.wani
===========================


Operation: GET /dataservice/settings/configuration/wani
-------------------------------------------------------


Deprecated!!!

Retrieve wani configuration value

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
        client.settings.configuration.wani.get()


Operation: PUT /dataservice/settings/configuration/wani
-------------------------------------------------------


Deprecated!!!

Update wani configuration setting

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
        client.settings.configuration.wani.put()


Operation: POST /dataservice/settings/configuration/wani
--------------------------------------------------------


Deprecated!!!

Add new wani configuration

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
        client.settings.configuration.wani.post()


