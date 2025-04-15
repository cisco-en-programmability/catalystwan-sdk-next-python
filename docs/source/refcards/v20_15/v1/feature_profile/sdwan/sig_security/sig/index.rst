=========================================
v1.feature_profile.sdwan.sig_security.sig
=========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig
--------------------------------------------------------------------------------------


Create Parcel for Sig Security Policy

.. code:: python

    def post(
        sig_security_id: str,
        payload: CreateSigSecurityProfileParcel1PostRequest,
    ) -> CreateSigSecurityProfileParcel1PostResponse: ...


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
        client.v1.feature_profile.sdwan.sig_security.sig.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


Update a Sig Security Profile Parcel

.. code:: python

    def put(
        sig_security_id: str,
        sig_security_profile_parcel_id: str,
        payload: EditSigSecurityProfileParcel1PutRequest,
    ) -> EditSigSecurityProfileParcel1PutResponse: ...


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
        client.v1.feature_profile.sdwan.sig_security.sig.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}
---------------------------------------------------------------------------------------------------------------------


Delete a SigSecurity Profile Parcel

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.sig_security.sig.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        sig_security_id: str,
    ) -> GetListSdwanSigSecuritySigPayload: ...


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
        client.v1.feature_profile.sdwan.sig_security.sig.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        sig_security_id: str, sig_security_profile_parcel_id: str
    ) -> GetSingleSdwanSigSecuritySigPayload: ...


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
        client.v1.feature_profile.sdwan.sig_security.sig.get()


.. toctree::
    :maxdepth: 1

    models

