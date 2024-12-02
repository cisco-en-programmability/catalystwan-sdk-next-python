=========================================
v1.feature_profile.sdwan.sig_security.sig
=========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig
-------------------------------------------------------------------------------------


Get Sig Security Profile Parcels for a given ParcelType

.. code:: python

    def get_sig_security_profile_parcel_1(
        sig_security_id: str,
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
        client.v1.feature_profile.sdwan.sig_security.sig.get_sig_security_profile_parcel_1()


Operation: POST /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig
--------------------------------------------------------------------------------------


Create Parcel for Sig Security Policy

.. code:: python

    def create_sig_security_profile_parcel_1(
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
        client.v1.feature_profile.sdwan.sig_security.sig.create_sig_security_profile_parcel_1()


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


Get SigSecurity Profile Parcel by parcelId

.. code:: python

    def get_sig_security_profile_parcel_by_parcel_id_1(
        sig_security_id: str, sig_security_profile_parcel_id: str
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
        client.v1.feature_profile.sdwan.sig_security.sig.get_sig_security_profile_parcel_by_parcel_id_1()


Operation: PUT /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


Update a Sig Security Profile Parcel

.. code:: python

    def edit_sig_security_profile_parcel_1(
        sig_security_id: str,
        sig_security_profile_parcel_id: str,
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
        client.v1.feature_profile.sdwan.sig_security.sig.edit_sig_security_profile_parcel_1()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}
---------------------------------------------------------------------------------------------------------------------


Delete a SigSecurity Profile Parcel

.. code:: python

    def delete_sig_security_profile_parcel_1(
        sig_security_id: str, sig_security_profile_parcel_id: str
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
        client.v1.feature_profile.sdwan.sig_security.sig.delete_sig_security_profile_parcel_1()


