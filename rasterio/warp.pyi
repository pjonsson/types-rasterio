from rasterio.enums import Resampling as Resampling
from rasterio.env import GDALVersion as GDALVersion, ensure_env as ensure_env, require_gdal_version as require_gdal_version
from rasterio.errors import GDALBehaviorChangeException as GDALBehaviorChangeException, TransformError as TransformError
from rasterio.transform import array_bounds as array_bounds
from typing import Any

SUPPORTED_RESAMPLING: Any
GDAL2_RESAMPLING: Any

def transform(src_crs, dst_crs, xs, ys, zs: Any | None = ...): ...
def transform_geom(src_crs, dst_crs, geom, antimeridian_cutting: bool = ..., antimeridian_offset: float = ..., precision: int = ...): ...
def transform_bounds(src_crs, dst_crs, left, bottom, right, top, densify_pts: int = ...): ...
def reproject(source, destination: Any | None = ..., src_transform: Any | None = ..., gcps: Any | None = ..., rpcs: Any | None = ..., src_crs: Any | None = ..., src_nodata: Any | None = ..., dst_transform: Any | None = ..., dst_crs: Any | None = ..., dst_nodata: Any | None = ..., dst_resolution: Any | None = ..., src_alpha: int = ..., dst_alpha: int = ..., resampling=..., num_threads: int = ..., init_dest_nodata: bool = ..., warp_mem_limit: int = ..., **kwargs): ...
def aligned_target(transform, width, height, resolution): ...
def calculate_default_transform(src_crs, dst_crs, width, height, left: Any | None = ..., bottom: Any | None = ..., right: Any | None = ..., top: Any | None = ..., gcps: Any | None = ..., rpcs: Any | None = ..., resolution: Any | None = ..., dst_width: Any | None = ..., dst_height: Any | None = ..., **kwargs): ...
