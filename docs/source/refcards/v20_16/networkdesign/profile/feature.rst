=============================
networkdesign.profile.feature
=============================


Operation: GET /dataservice/networkdesign/profile/feature
---------------------------------------------------------


Deprecated!!!

Generate device profile template list

.. code:: python

    def get_device_profile_feature_template_list() -> List[Any]: ...


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
        client.networkdesign.profile.feature.get_device_profile_feature_template_list()


