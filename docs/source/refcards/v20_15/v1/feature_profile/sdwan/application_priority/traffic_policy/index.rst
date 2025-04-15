============================================================
v1.feature_profile.sdwan.application_priority.traffic_policy
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy
-----------------------------------------------------------------------------------------------------------------


Create a Traffic Policy Profile Parcel for application-priority feature profile

.. code:: python

    def post(
        application_priority_id: str,
        payload: CreateTrafficPolicyProfileParcelForapplicationPriorityPostRequest,
    ) -> (
        CreateTrafficPolicyProfileParcelForapplicationPriorityPostResponse
    ): ...


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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}
----------------------------------------------------------------------------------------------------------------------------------


Get Traffic Policy Profile Parcel by parcelId for application-priority feature profile

.. code:: python

    def get(
        application_priority_id: str, traffic_policy_id: str
    ) -> GetSingleSdwanApplicationPriorityTrafficPolicyPayload: ...


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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.get()


Operation: PUT /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}
----------------------------------------------------------------------------------------------------------------------------------


Update a Traffic Policy Profile Parcel for application-priority feature profile

.. code:: python

    def put(
        application_priority_id: str,
        traffic_policy_id: str,
        payload: EditTrafficPolicyProfileParcelForapplicationPriorityPutRequest,
    ) -> (
        EditTrafficPolicyProfileParcelForapplicationPriorityPutResponse
    ): ...


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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/traffic-policy/{trafficPolicyId}
-------------------------------------------------------------------------------------------------------------------------------------


Delete a Traffic Policy Profile Parcel for application-priority feature profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.application_priority.traffic_policy.delete()


.. toctree::
    :maxdepth: 1

    models

