===================================
device.policy.userusergroupbindings
===================================


Operation: GET /dataservice/device/policy/userusergroupbindings
---------------------------------------------------------------


Show User-Usergroup bindings from Vsmart

.. code:: python

    def show_vsmart_user_usergroup_bindings(device_id: str) -> Any: ...


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
        client.device.policy.userusergroupbindings.show_vsmart_user_usergroup_bindings()


