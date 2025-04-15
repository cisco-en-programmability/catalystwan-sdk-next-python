=====================================
v1.feature_profile.sdwan.cli.features
=====================================


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/features
-----------------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        feature_type: Optional[str] = "config",
    ) -> List[GetSdwanFeatureProfilesByFamilyAndTypeGetResponse]: ...


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
        client.v1.feature_profile.sdwan.cli.features.get()


.. toctree::
    :maxdepth: 1

    models

