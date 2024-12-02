========================================
v1.feature_profile.sdwan.service.lan.vpn
========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn
--------------------------------------------------------------------------------


Get Lan Vpn Profile Parcels for Service feature profile

.. code:: python

    def get_lan_vpn_profile_parcel_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.get_lan_vpn_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn
---------------------------------------------------------------------------------


Create a Lan Vpn Profile Parcel for Service feature profile

.. code:: python

    def create_lan_vpn_profile_parcel_for_service(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.lan.vpn.create_lan_vpn_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}
----------------------------------------------------------------------------------------


Get Lan Vpn Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_lan_vpn_profile_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.get_lan_vpn_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}
----------------------------------------------------------------------------------------


Update a Lan Vpn Profile Parcel for Service feature profile

.. code:: python

    def edit_lan_vpn_profile_parcel_for_service(
        service_id: str, vpn_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.lan.vpn.edit_lan_vpn_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}
-------------------------------------------------------------------------------------------


Delete a Lan Vpn Profile Parcel for Service feature profile

.. code:: python

    def delete_lan_vpn_profile_parcel_for_service(
        service_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.delete_lan_vpn_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    interface/index
    schema/index
    routing/index

