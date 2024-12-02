===================================================
v1.feature_profile.mobility.global_.security_policy
===================================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy
-----------------------------------------------------------------------------------------


Get an Mobility SecurityPolicy Profile Parcel list for Mobility Global Feature Profile

.. code:: python

    def get_security_policy_profile_parcel_list_for_mobility(
        profile_id: str,
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
        client.v1.feature_profile.mobility.global_.security_policy.get_security_policy_profile_parcel_list_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy
------------------------------------------------------------------------------------------


Create an SecurityPolicy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_security_policy_profile_parcel_for_mobility(
        profile_id: str,
        payload: Optional[
            CreateSecurityPolicyProfileParcelForMobilityPostRequest
        ] = None,
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
        client.v1.feature_profile.mobility.global_.security_policy.create_security_policy_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}
------------------------------------------------------------------------------------------------------------


Get an Mobility SecurityPolicy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def get_security_policy_profile_parcel_for_mobility(
        profile_id: str, security_policy_id: str
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
        client.v1.feature_profile.mobility.global_.security_policy.get_security_policy_profile_parcel_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}
------------------------------------------------------------------------------------------------------------


Edit an Security Policy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def edit_security_policy_profile_parcel_for_mobility(
        profile_id: str,
        security_policy_id: str,
        payload: Optional[
            CreateSecurityPolicyProfileParcelForMobilityPostRequest
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
        client.v1.feature_profile.mobility.global_.security_policy.edit_security_policy_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}
---------------------------------------------------------------------------------------------------------------


Delete a Security Policy Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete_security_policy_profile_parcel_for_mobility(
        profile_id: str, security_policy_id: str
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
        client.v1.feature_profile.mobility.global_.security_policy.delete_security_policy_profile_parcel_for_mobility()


.. toctree::
    :maxdepth: 1

    models

