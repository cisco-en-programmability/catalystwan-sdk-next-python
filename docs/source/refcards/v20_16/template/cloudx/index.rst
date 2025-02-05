===============
template.cloudx
===============


Operation: GET /dataservice/template/cloudx
-------------------------------------------


Get CloudX feature list

.. code:: python

    def get_cloud_x_status() -> List[Any]: ...


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
        client.template.cloudx.get_cloud_x_status()


.. toctree::
    :maxdepth: 1

    addcloudx
    attachedclient
    attacheddia
    attachedgateway
    availableapps
    clientlist
    dialist
    gatewaylist
    interfaces
    manage/index
    sig_tunnels
    status

