=====================================
v1.feature_profile.sdwan.sig_security
=====================================


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security
-----------------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_sig_security_feature_profiles(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.sig_security.get_sdwan_sig_security_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/sig-security
------------------------------------------------------------------


Create a SDWAN Sig Security Feature Profile

.. code:: python

    def create_sdwan_sig_security_feature_profile(
        payload: Optional[str] = None,
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
        client.v1.feature_profile.sdwan.sig_security.create_sdwan_sig_security_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}
---------------------------------------------------------------------------------


Get a SDWAN Sig Security Feature Profile with sigSecurityId

.. code:: python

    def get_sdwan_sig_security_feature_profile_by_profile_id(
        sig_security_id: str, references: Optional[bool] = False
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.sig_security.get_sdwan_sig_security_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}
---------------------------------------------------------------------------------


Edit a SDWAN Sig Security Feature Profile

.. code:: python

    def edit_sdwan_sig_security_feature_profile(
        sig_security_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.sig_security.edit_sdwan_sig_security_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}
------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_sig_security_feature_profile(
        sig_security_id: str,
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
        client.v1.feature_profile.sdwan.sig_security.delete_sdwan_sig_security_feature_profile()


.. toctree::
    :maxdepth: 1

    sig

