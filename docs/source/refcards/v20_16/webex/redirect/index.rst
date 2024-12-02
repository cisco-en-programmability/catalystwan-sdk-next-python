==============
webex.redirect
==============


Operation: GET /dataservice/webex/redirect
------------------------------------------


Redirect Info

.. code:: python

    def redirect_webex_data_centers(
        code: str,
    ) -> RedirectCodeResponse: ...


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
        client.webex.redirect.redirect_webex_data_centers()


.. toctree::
    :maxdepth: 1

    models

