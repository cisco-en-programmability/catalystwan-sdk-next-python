======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    ImageType = Literal[
        "ImageType{type='ackfile'}",
        "ImageType{type='container'}",
        "ImageType{type='dockertype'}",
        "ImageType{type='firmware'}",
        "ImageType{type='licensefile'}",
        "ImageType{type='lxc'}",
        "ImageType{type='na'}",
        "ImageType{type='rumreport'}",
        "ImageType{type='software'}",
        "ImageType{type='utdsignature'}",
        "ImageType{type='utdsignaturecustom'}",
        "ImageType{type='utdsignatureips'}",
        "ImageType{type='virtualmachine'}",
        "ImageType{type='virtualmachine-diskimg'}",
        "ImageType{type='virtualmachine-scaffold'}",
        "ImageType{type='waas'}",
    ]

    UtdsignatureParam = Literal["utdsignature"]


    class ImageData:
        application_vendor: Optional[str]
        application_vendor_vendor: Optional[str]
        arch: Optional[str]
        controller_version: Optional[str]
        cw_version: Optional[str]
        description: Optional[str]
        display_checksum: Optional[str]
        display_checksum_type: Optional[str]
        display_checksum_validity: Optional[str]
        family: Optional[str]
        file_entries: Optional[Dict[str, str]]
        file_name: Optional[str]
        file_size_str: Optional[str]
        file_sizebyte: Optional[str]
        image_properties_json: Optional[str]
        image_type: Optional[ImageType]
        image_type_name: Optional[str]
        md5_checksum: Optional[str]
        network_function_type: Optional[str]
        remote_server_id: Optional[str]
        remote_servers: Optional[str]
        sha256_checksum: Optional[str]
        sha512_checksum: Optional[str]
        smu_compatible_with: Optional[str]
        smu_defect_id: Optional[str]
        smu_description: Optional[str]
        smu_type: Optional[str]
        storage_data: Optional[str]
        system_properties_xml: Optional[str]
        tags: Optional[List[str]]
        temp_image_path: Optional[str]
        updated_file_name: Optional[str]
        version: Optional[str]
        version_type_name: Optional[str]
        vnf_properties_json: Optional[str]


