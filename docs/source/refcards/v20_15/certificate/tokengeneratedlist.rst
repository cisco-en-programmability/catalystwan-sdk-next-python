==============================
certificate.tokengeneratedlist
==============================


Operation: GET /dataservice/certificate/tokengeneratedlist
----------------------------------------------------------


get token generated list

.. code:: python

    def get_token_list() -> str: ...


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
        client.certificate.tokengeneratedlist.get_token_list()


