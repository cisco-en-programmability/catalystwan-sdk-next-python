===========
cdna.server
===========


Operation: GET /dataservice/cdna/server
---------------------------------------


Get CDNA Server Details

.. code:: python

    def get_cdna_server() -> EnrollOtpResponse: ...


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
        client.cdna.server.get_cdna_server()


Operation: PUT /dataservice/cdna/server
---------------------------------------


Enroll CDNA Server with OTP

.. code:: python

    def enroll_cdna_server(
        payload: EnrollOtpSettings,
    ) -> EnrollOtpResponse: ...


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
        client.cdna.server.enroll_cdna_server()


Operation: DELETE /dataservice/cdna/server
------------------------------------------


Delete CDNA Server Details

.. code:: python

    def delete_cdna_server() -> None: ...


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
        client.cdna.server.delete_cdna_server()


.. toctree::
    :maxdepth: 1

    models

