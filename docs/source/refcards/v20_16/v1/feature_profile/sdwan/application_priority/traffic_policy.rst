============================================================
v1.feature_profile.sdwan.application_priority.traffic_policy
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy
-----------------------------------------------------------------------------------------------------------------


Create a Traffic Policy Profile Parcel for application-priority feature profile

.. code:: python

    def create_traffic_policy_profile_parcel_forapplication_priority(
        application_priority_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.create_traffic_policy_profile_parcel_forapplication_priority()


Operation: GET /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}
----------------------------------------------------------------------------------------------------------------------------------


Get Traffic Policy Profile Parcel by parcelId for application-priority feature profile

.. code:: python

    def get_traffic_policy_profile_parcel_by_parcel_id_forapplication_priority(
        application_priority_id: str, traffic_policy_id: str
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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.get_traffic_policy_profile_parcel_by_parcel_id_forapplication_priority()


Operation: PUT /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}
----------------------------------------------------------------------------------------------------------------------------------


Update a Traffic Policy Profile Parcel for application-priority feature profile

.. code:: python

    def edit_traffic_policy_profile_parcel_forapplication_priority(
        application_priority_id: str,
        traffic_policy_id: str,
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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.edit_traffic_policy_profile_parcel_forapplication_priority()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}
-------------------------------------------------------------------------------------------------------------------------------------


Delete a Traffic Policy Profile Parcel for application-priority feature profile

.. code:: python

    def delete_traffic_policy_profile_parcel_forapplication_priority(
        application_priority_id: str, traffic_policy_id: str
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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.delete_traffic_policy_profile_parcel_forapplication_priority()


