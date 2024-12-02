================================
networkdesign.profile.attachment
================================


Operation: POST /dataservice/networkdesign/profile/attachment/{profileId}
-------------------------------------------------------------------------


Deprecated!!!

Attach to device profile

.. code:: python

    def push_device_profile_template(
        profile_id: str, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.networkdesign.profile.attachment.push_device_profile_template()


