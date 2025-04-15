====================================
multicloud.cloudgateway.config_group
====================================


Operation: POST /dataservice/multicloud/cloudgateway/config-group
-----------------------------------------------------------------


API to initiate a config group creation for a cloud gateway.

.. code:: python

    def post(
        cloud_type: str, payload: MultiCloudGatewaysConfiggroupBody
    ) -> PostCgwConfigGroupResponse: ...


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
        client.multicloud.cloudgateway.config_group.post()


.. toctree::
    :maxdepth: 1

    models

