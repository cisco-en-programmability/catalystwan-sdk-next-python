==================
certificate.record
==================


Operation: GET /dataservice/certificate/record
----------------------------------------------


get device certificate data

.. code:: python

    def get(
        request_id: Optional[str] = None,
        data_object: Optional[str] = None,
    ) -> List[str]: ...


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
        client.certificate.record.get()


