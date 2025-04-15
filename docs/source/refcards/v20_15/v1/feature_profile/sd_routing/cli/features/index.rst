==========================================
v1.feature_profile.sd_routing.cli.features
==========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/features
----------------------------------------------------------------------


GetSdroutingFeatureProfilesByFamilyAndType

.. code:: python

    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        feature_type: Optional[str] = "config",
    ) -> List[GetGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.cli.features.get()


.. toctree::
    :maxdepth: 1

    models

