#!/usr/bin/env python3
"""
yaml2excel.py

A utility to convert a Helm values.yaml file into a flattened Excel sheet.

Usage:
    python yaml2excel.py values.yaml dev_values.xlsx

Requirements:
    pip install pyyaml pandas openpyxl
"""

import sys
import os
import yaml
import pandas as pd


def flatten_yaml(data, parent_key='', sep='.'):
    """
    Recursively flattens a nested dictionary or list into a flat dictionary.
    flatten_yaml() function: This is the core recursive function that transforms the nested YAML structure into a flat dictionary. 
    It traverses the YAML data (which is a Python dictionary or list), and for each nested key-value pair, it constructs a new, flattened key by concatenating 
    the parent keys with a separator (a dot . by default). For lists, it appends the index in brackets [i] to the key. This process continues until all nested 
    structures are resolved into a single-level dictionary.


    :param data: The YAML data (dict or list) to flatten.
    :param parent_key: The base key string for recursion.
    :param sep: Separator between flattened keys.
    :return: A dictionary where keys are flattened paths and values are the corresponding values.
    """
    items = {}
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten_yaml(v, new_key, sep=sep))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            items.update(flatten_yaml(v, new_key, sep=sep))
    else:
        items[parent_key] = data
    return items


def read_yaml(file_path):
    """
    Reads a YAML file and returns its content as a Python object.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input YAML file not found: {file_path}")
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format in file {file_path}: {e}")


def write_excel(flattened_data, output_path):
    """
    Writes flattened YAML data to an Excel file.
    """
    try:
        df = pd.DataFrame(list(flattened_data.items()), columns=['Key', 'Value'])
        df.to_excel(output_path, index=False, engine='openpyxl')
    except Exception as e:
        raise IOError(f"Failed to write Excel file {output_path}: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python yaml2excel.py <input_yaml> <output_excel>")
        sys.exit(1)

    input_yaml = sys.argv[1]
    output_excel = sys.argv[2]

    try:
        yaml_data = read_yaml(input_yaml)
        flattened_data = flatten_yaml(yaml_data)
        write_excel(flattened_data, output_excel)
        print(f"Excel file created successfully: {output_excel}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
