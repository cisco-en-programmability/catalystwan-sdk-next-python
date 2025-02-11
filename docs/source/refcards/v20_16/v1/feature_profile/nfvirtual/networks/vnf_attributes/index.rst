====================================================
v1.feature_profile.nfvirtual.networks.vnf_attributes
====================================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes
----------------------------------------------------------------------------------------------


Create VNF Attributes Profile config for Networks feature profile

.. code:: python

    def create_nfvirtual_vnf_attributes_parcel(
        networks_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.create_nfvirtual_vnf_attributes_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}
---------------------------------------------------------------------------------------------------------------


Get VNF Attributes Profile Parcels for Networks feature profile

.. code:: python

    def get_nfvirtual_vnf_attributes_parcel(
        networks_id: str, vnf_attributes_id: str
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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.get_nfvirtual_vnf_attributes_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}
---------------------------------------------------------------------------------------------------------------


Edit a VNF Attributes Profile Parcel for networks feature profile

.. code:: python

    def edit_nfvirtual_vnf_attributes_parcel(
        networks_id: str,
        vnf_attributes_id: str,
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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.edit_nfvirtual_vnf_attributes_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}
------------------------------------------------------------------------------------------------------------------


Delete VNF Attributes Profile config for Networks feature profile

.. code:: python

    def delete_nfvirtual_vnf_attributes_parcel(
        networks_id: str, vnf_attributes_id: str
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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.delete_nfvirtual_vnf_attributes_parcel()


.. toctree::
    :maxdepth: 1

    vnf

