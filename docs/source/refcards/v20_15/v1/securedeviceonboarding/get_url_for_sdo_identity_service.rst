==========================================================
v1.securedeviceonboarding.get_url_for_sdo_identity_service
==========================================================


Operation: GET /dataservice/v1/securedeviceonboarding/getUrlForSdoIdentityService
---------------------------------------------------------------------------------


Get URL for Secure Device Onboarding Identity Service that generates Session ID required for authentication to get Secure Device Onboarding token

.. code:: python

    def get() -> str: ...


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
        client.v1.securedeviceonboarding.get_url_for_sdo_identity_service.get()


