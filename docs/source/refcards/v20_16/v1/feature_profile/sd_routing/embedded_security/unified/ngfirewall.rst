==================================================================
v1.feature_profile.sd_routing.embedded_security.unified.ngfirewall
==================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/embedded-security/{securityId}/unified/ngfirewall
-----------------------------------------------------------------------------------------------------------


Get Ngfirewall Feature

.. code:: python

    def get_ngfirewall_feature(security_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.unified.ngfirewall.get_ngfirewall_feature()


Operation: POST /dataservice/v1/feature-profile/sd-routing/embedded-security/{securityId}/unified/ngfirewall
------------------------------------------------------------------------------------------------------------


Create Parcel for Ngfirewall Policy

.. code:: python

    def create_ngfirewall_feature(
        security_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.unified.ngfirewall.create_ngfirewall_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------


Get Ngfirewall Feature by FeatureId

.. code:: python

    def get_ngfirewall_feature_by_feature_id(
        security_id: str, security_profile_parcel_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.unified.ngfirewall.get_ngfirewall_feature_by_feature_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------


Update a Ngfirewall Feature

.. code:: python

    def edit_ngfirewall_feature(
        security_id: str,
        security_profile_parcel_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.unified.ngfirewall.edit_ngfirewall_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}
----------------------------------------------------------------------------------------------------------------------------------------


Delete a Ngfirewall Feature

.. code:: python

    def delete_ngfirewall_feature(
        security_id: str, security_profile_parcel_id: str
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
        client.v1.feature_profile.sd_routing.embedded_security.unified.ngfirewall.delete_ngfirewall_feature()


