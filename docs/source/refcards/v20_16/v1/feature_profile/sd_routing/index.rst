=============================
v1.feature_profile.sd_routing
=============================


Operation: GET /dataservice/v1/feature-profile/sd-routing
---------------------------------------------------------


Get all SD-Routing Feature Profiles

.. code:: python

    def get_sdrouting_feature_profiles(
        offset: Optional[int] = None, limit: Optional[int] = 0
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
        client.v1.feature_profile.sd_routing.get_sdrouting_feature_profiles()


.. toctree::
    :maxdepth: 1

    cli/index
    embedded_security/index
    other/index
    service/index
    sse/index
    system/index
    transport/index

