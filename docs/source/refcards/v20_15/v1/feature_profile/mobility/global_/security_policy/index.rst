===================================================
v1.feature_profile.mobility.global_.security_policy
===================================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy
------------------------------------------------------------------------------------------


Create an SecurityPolicy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateSecurityPolicyProfileParcelForMobilityPostRequest,
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
        client.v1.feature_profile.mobility.global_.security_policy.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}
------------------------------------------------------------------------------------------------------------


Edit an Security Policy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        security_policy_id: str,
        payload: EditSecurityPolicyProfileParcelForMobilityPutRequest,
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
        client.v1.feature_profile.mobility.global_.security_policy.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}
---------------------------------------------------------------------------------------------------------------


Delete a Security Policy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, security_policy_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.security_policy.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str,
    ) -> GetListMobilityGlobalSecuritypolicyPayload: ...


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
        client.v1.feature_profile.mobility.global_.security_policy.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, security_policy_id: str
    ) -> GetSingleMobilityGlobalSecuritypolicyPayload: ...


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
        client.v1.feature_profile.mobility.global_.security_policy.get()


.. toctree::
    :maxdepth: 1

    models

