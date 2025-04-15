========================================================
v1.feature_profile.sdwan.application_priority.qos_policy
========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy
-------------------------------------------------------------------------------------------------------------


Create QOS Policy feature for application-priority feature profile

.. code:: python

    def post(
        application_priority_id: str,
        payload: CreatePolicyApplicationProfileParcelPostRequest,
    ) -> CreatePolicyApplicationProfileParcelPostResponse: ...


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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}
--------------------------------------------------------------------------------------------------------------------------


Get QOS Policy feature for application-priority feature profile

.. code:: python

    def get(
        application_priority_id: str, qos_policy_id: str
    ) -> GetSingleSdwanApplicationPriorityQosPolicyPayload: ...


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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.get()


Operation: PUT /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}
--------------------------------------------------------------------------------------------------------------------------


Edit QOS Policy feature for application-priority feature profile

.. code:: python

    def put(
        application_priority_id: str,
        qos_policy_id: str,
        payload: EditPolicyApplicationProfileParcelPutRequest,
    ) -> EditPolicyApplicationProfileParcelPutResponse: ...


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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/qos-policy/{qosPolicyId}
-----------------------------------------------------------------------------------------------------------------------------


Delete QOS Policy feature for application-priority feature profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.application_priority.qos_policy.delete()


.. toctree::
    :maxdepth: 1

    models

