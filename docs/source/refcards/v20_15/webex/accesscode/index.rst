================
webex.accesscode
================


Operation: GET /dataservice/webex/accesscode
--------------------------------------------


Webex Access Code Details

.. code:: python

    def webex_access_code() -> AccessCodeResponse: ...


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
        client.webex.accesscode.webex_access_code()


.. toctree::
    :maxdepth: 1

    models

