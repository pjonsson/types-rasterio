from typing import Dict, Tuple, Union

from rasterio.path import Path

blacklist: Dict[str, Tuple[str, ...]]


def raster_driver_extensions() -> Dict[str, str]:
    ...


def driver_from_extension(path: Union[str, Path]):
    ...


def is_blacklisted(name: str, mode: str) -> bool:
    ...
