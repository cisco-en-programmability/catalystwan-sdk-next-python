=============================
v1.config_group.device.deploy
=============================


Operation: POST /dataservice/v1/config-group/{configGroupId}/device/deploy
--------------------------------------------------------------------------


deploy config group to devices<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def post(
        config_group_id: str, payload: DeployConfigGroupPostRequest
    ) -> DeployConfigGroupPostResponse: ...


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
        client.v1.config_group.device.deploy.post()


.. toctree::
    :maxdepth: 1

    models

