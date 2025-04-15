===========
cdna.server
===========


Operation: GET /dataservice/cdna/server
---------------------------------------


Get CDNA Server Details

.. code:: python

    def get() -> EnrollOtpResponse: ...


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
        client.cdna.server.get()


Operation: PUT /dataservice/cdna/server
---------------------------------------


Enroll CDNA Server with OTP

.. code:: python

    def put(payload: EnrollOtpSettings) -> EnrollOtpResponse: ...


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
        client.cdna.server.put()


Operation: DELETE /dataservice/cdna/server
------------------------------------------


Delete CDNA Server Details

.. code:: python

    def delete() -> None: ...


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
        client.cdna.server.delete()


.. toctree::
    :maxdepth: 1

    models

