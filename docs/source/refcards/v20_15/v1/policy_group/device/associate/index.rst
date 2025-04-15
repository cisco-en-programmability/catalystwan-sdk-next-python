================================
v1.policy_group.device.associate
================================


Operation: GET /dataservice/v1/policy-group/{policyGroupId}/device/associate
----------------------------------------------------------------------------


Get devices association with a policy group

.. code:: python

    def get(policy_group_id: str) -> None: ...


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
        client.v1.policy_group.device.associate.get()


Operation: PUT /dataservice/v1/policy-group/{policyGroupId}/device/associate
----------------------------------------------------------------------------


Move the devices from one policy group to another

.. code:: python

    def put(
        policy_group_id: str,
        payload: UpdatePolicyGroupAssociationPutRequest,
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
        client.v1.policy_group.device.associate.put()


Operation: POST /dataservice/v1/policy-group/{policyGroupId}/device/associate
-----------------------------------------------------------------------------


Create associations with device and a policy group

.. code:: python

    def post(
        policy_group_id: str,
        payload: CreatePolicyGroupAssociationPostRequest,
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
        client.v1.policy_group.device.associate.post()


Operation: DELETE /dataservice/v1/policy-group/{policyGroupId}/device/associate
-------------------------------------------------------------------------------


Delete Policy Group Association from devices

.. code:: python

    def delete(
        policy_group_id: str,
        payload: Optional[
            DeletePolicyGroupAssociationDeleteRequest
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
        client.v1.policy_group.device.associate.delete()


.. toctree::
    :maxdepth: 1

    models

