==================================
settings.configuration.certificate
==================================


Operation: GET /dataservice/settings/configuration/certificate/{type}
---------------------------------------------------------------------


Retrieve certificate configuration value by type

.. code:: python

    def get(type_: str) -> str: ...


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
        client.settings.configuration.certificate.get()


Operation: PUT /dataservice/settings/configuration/certificate/{type}
---------------------------------------------------------------------


Update certificate configuration

.. code:: python

    def put(type_: str, payload: Any) -> str: ...


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
        client.settings.configuration.certificate.put()


Operation: POST /dataservice/settings/configuration/certificate/{type}
----------------------------------------------------------------------


Add new certificate configuration

.. code:: python

    def post(type_: str, payload: Any) -> str: ...


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
        client.settings.configuration.certificate.post()


