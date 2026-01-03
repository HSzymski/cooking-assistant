import os
from unidecode import unidecode

def get_cookbook_path() -> str:
    """
    Get the path to the cookbook directory.
    
    Returns:
        The absolute path to the cookbook directory.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cookbook_path = os.path.join(base_dir, '..', 'cookbook_db')
    return cookbook_path

def remove_accents(text: str) -> str:
    """
    Remove accents from a given string.
    
    Args:
        text: The input string

    Returns:
        The input string without accents
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    return unidecode(text)

def map_category_names(categories: list[str]) -> dict[str, str]:
    """
    Map category names to their corresponding folder names without accents and spaces.
    
    Args:
        categories: List of category names
        
    Returns:
        A dictionary mapping category names to their paths
    """
    
    return {category: remove_accents(category).replace(' ', '_').lower() for category in categories}

def init_cookbook(categories: list[str]) -> None:
    """
    Create cookbook categories in the simple database.
    
    Args:
        categories: List of category names to create
    """
    os.makedirs('cookbook_db', exist_ok=True)

    cookbook_path = get_cookbook_path()
    for category in categories:
        os.makedirs(rf'{cookbook_path}\{category}', exist_ok=True)

def get_recipe_headers() -> list[str]:
    """
    Get the standard headers for a recipe JSON file.
    
    Returns:
        A list of standard recipe headers
    """
    import json

    with open('cookbook_db/ciasta/biszkopt.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        headers = list(data.keys())

    return headers