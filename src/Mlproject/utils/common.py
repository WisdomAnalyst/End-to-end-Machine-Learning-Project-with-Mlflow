import os
from box.exceptions import BoxValueError 
import yaml
from Mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Contents of the YAML file.

    Raises:
        ValueError: If the YAML file is empty or invalid.
        Exception: For any other exception that occurs during file reading.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or invalid")
    except Exception as e:
        raise e 

def create_directories(path_to_directories: List[Path], verbose: bool = True):
    """
    Create directories at the specified paths.

    Args:
        path_to_directories (List[Path]): List of paths where directories should be created.
        verbose (bool, optional): If True, log the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save data as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved as JSON.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return its contents as a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Contents of the JSON file.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data to a file using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to save the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data from a file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded data from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes (kB).
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} kB"