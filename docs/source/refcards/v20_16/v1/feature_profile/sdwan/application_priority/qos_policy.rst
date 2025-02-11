========================================================
v1.feature_profile.sdwan.application_priority.qos_policy
========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy
-------------------------------------------------------------------------------------------------------------


Create QOS Policy feature for application-priority feature profile

.. code:: python

    def create_policy_application_profile_parcel(
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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.create_policy_application_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}
--------------------------------------------------------------------------------------------------------------------------


Get QOS Policy feature for application-priority feature profile

.. code:: python

    def get_policy_application_profile_parcel(
        application_priority_id: str, qos_policy_id: str
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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.get_policy_application_profile_parcel()


Operation: PUT /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}
--------------------------------------------------------------------------------------------------------------------------


Edit QOS Policy feature for application-priority feature profile

.. code:: python

    def edit_policy_application_profile_parcel(
        application_priority_id: str,
        qos_policy_id: str,
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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.edit_policy_application_profile_parcel()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}
-----------------------------------------------------------------------------------------------------------------------------


Delete QOS Policy feature for application-priority feature profile

.. code:: python

    def delete_policy_application_profile_parcel(
        application_priority_id: str, qos_policy_id: str
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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.delete_policy_application_profile_parcel()


