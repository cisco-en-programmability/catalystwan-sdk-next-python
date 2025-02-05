==================================
settings.configuration.certificate
==================================


Operation: GET /dataservice/settings/configuration/certificate/{type}
---------------------------------------------------------------------


Retrieve certificate configuration value by type

.. code:: python

    def get_cert_configuration(type_: str) -> str: ...


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
        client.settings.configuration.certificate.get_cert_configuration()


Operation: PUT /dataservice/settings/configuration/certificate/{type}
---------------------------------------------------------------------


Update certificate configuration

.. code:: python

    def edit_cert_configuration(
        type_: str, payload: Optional[Any] = None
    ) -> str: ...


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
        client.settings.configuration.certificate.edit_cert_configuration()


Operation: POST /dataservice/settings/configuration/certificate/{type}
----------------------------------------------------------------------


Add new certificate configuration

.. code:: python

    def new_cert_configuration(
        type_: str, payload: Optional[Any] = None
    ) -> str: ...


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
        client.settings.configuration.certificate.new_cert_configuration()


