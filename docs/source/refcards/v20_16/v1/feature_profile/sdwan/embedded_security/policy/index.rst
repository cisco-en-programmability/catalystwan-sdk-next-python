=================================================
v1.feature_profile.sdwan.embedded_security.policy
=================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy
------------------------------------------------------------------------------------------


Get Security Features for a given ParcelType

.. code:: python

    def get_security_profile_parcel_1(security_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.embedded_security.policy.get_security_profile_parcel_1()


Operation: POST /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy
-------------------------------------------------------------------------------------------


Create Feature for Security Policy

.. code:: python

    def create_embedded_security_profile_parcel(
        security_id: str,
        payload: Optional[
            CreateEmbeddedSecurityProfileParcelPostRequest
        ] = None,
    ) -> CreateEmbeddedSecurityProfileParcelPostResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.policy.create_embedded_security_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}
--------------------------------------------------------------------------------------------------------------------


Get Security Feature by FeatureId

.. code:: python

    def get_security_profile_parcel_by_parcel_id_1(
        security_id: str, security_profile_parcel_id: str
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
        client.v1.feature_profile.sdwan.embedded_security.policy.get_security_profile_parcel_by_parcel_id_1()


Operation: PUT /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}
--------------------------------------------------------------------------------------------------------------------


Update a Security Feature

.. code:: python

    def edit_security_profile_parcel_1(
        security_id: str,
        security_profile_parcel_id: str,
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
        client.v1.feature_profile.sdwan.embedded_security.policy.edit_security_profile_parcel_1()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}
-----------------------------------------------------------------------------------------------------------------------


Delete a Security Feature

.. code:: python

    def delete_security_profile_parcel_1(
        security_id: str, security_profile_parcel_id: str
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
        client.v1.feature_profile.sdwan.embedded_security.policy.delete_security_profile_parcel_1()


.. toctree::
    :maxdepth: 1

    models

