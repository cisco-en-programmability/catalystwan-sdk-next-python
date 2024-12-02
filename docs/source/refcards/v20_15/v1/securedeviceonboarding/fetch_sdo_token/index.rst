=========================================
v1.securedeviceonboarding.fetch_sdo_token
=========================================


Operation: POST /dataservice/v1/securedeviceonboarding/fetchSdoToken
--------------------------------------------------------------------


POST for fetching Secure Device Onboarding Token needed for Secure Device Onboarding APIs for eSim

.. code:: python

    def fetch_sdo_token(
        payload: Optional[
            DetailsForIdentityVerificationForSdoToken
        ] = None,
    ) -> None: ...


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
        client.v1.securedeviceonboarding.fetch_sdo_token.fetch_sdo_token()


.. toctree::
    :maxdepth: 1

    models

