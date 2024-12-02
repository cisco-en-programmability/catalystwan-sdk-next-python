================================
v1.policy_group.device.associate
================================


Operation: GET /dataservice/v1/policy-group/{policyGroupId}/device/associate
----------------------------------------------------------------------------


Get devices association with a policy group

.. code:: python

    def get_policy_group_association(policy_group_id: str) -> None: ...


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
        client.v1.policy_group.device.associate.get_policy_group_association()


Operation: PUT /dataservice/v1/policy-group/{policyGroupId}/device/associate
----------------------------------------------------------------------------


Move the devices from one policy group to another

.. code:: python

    def update_policy_group_association(
        policy_group_id: str, payload: Optional[Any] = None
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
        client.v1.policy_group.device.associate.update_policy_group_association()


Operation: POST /dataservice/v1/policy-group/{policyGroupId}/device/associate
-----------------------------------------------------------------------------


Create associations with device and a policy group

.. code:: python

    def create_policy_group_association(
        policy_group_id: str, payload: Optional[Any] = None
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
        client.v1.policy_group.device.associate.create_policy_group_association()


Operation: DELETE /dataservice/v1/policy-group/{policyGroupId}/device/associate
-------------------------------------------------------------------------------


Delete Policy Group Association from devices

.. code:: python

    def delete_policy_group_association(
        policy_group_id: str, payload: Optional[Any] = None
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
        client.v1.policy_group.device.associate.delete_policy_group_association()


