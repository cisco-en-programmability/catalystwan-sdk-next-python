====================
opentaccase.authcode
====================


Operation: GET /dataservice/opentaccase/authcode
------------------------------------------------


Deprecated!!!

Gets Access Token for SSO Logjn

.. code:: python

    def oauth_access(
        code: Optional[str] = None,
        redirect: Optional[str] = None,
        is_refresh_needed: Optional[bool] = None,
    ) -> List[Any]: ...


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
        client.opentaccase.authcode.oauth_access()


