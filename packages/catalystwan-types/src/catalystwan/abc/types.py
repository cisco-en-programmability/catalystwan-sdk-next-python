from typing import Dict, List, Literal, Union

JSON = Union[Dict[str, "JSON"], List["JSON"], str, int, float, bool, None]
HTTP_METHOD = Literal["GET", "PUT", "POST", "DELETE"]
