====================================================
v1.feature_profile.nfvirtual.networks.vnf_attributes
====================================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes
----------------------------------------------------------------------------------------------


Create VNF Attributes Profile config for Networks feature profile

.. code:: python

    def post(
        networks_id: str,
        payload: CreateNfvirtualVnfAttributesParcelPostRequest,
    ) -> CreateNfvirtualVnfAttributesParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}
---------------------------------------------------------------------------------------------------------------


Get VNF Attributes Profile Parcels for Networks feature profile

.. code:: python

    def get(
        networks_id: str, vnf_attributes_id: str
    ) -> GetSingleNfvirtualNetworksVnfAttributesPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}
---------------------------------------------------------------------------------------------------------------


Edit a VNF Attributes Profile Parcel for networks feature profile

.. code:: python

    def put(
        networks_id: str,
        vnf_attributes_id: str,
        payload: EditNfvirtualVnfAttributesParcelPutRequest,
    ) -> EditNfvirtualVnfAttributesParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}
------------------------------------------------------------------------------------------------------------------


Delete VNF Attributes Profile config for Networks feature profile

.. code:: python

    def delete(networks_id: str, vnf_attributes_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.delete()


.. toctree::
    :maxdepth: 1

    vnf/index
    models

