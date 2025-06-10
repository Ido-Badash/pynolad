def get_next_key(data_dict, current_key) -> str:
    """
    Changes the current key to the next key in the dictionary.
    If the current key is the last one, it loops around to the first key.
    """
    keys = list(data_dict.keys())
    if not keys:
        return None
    try:
        current_index = keys.index(current_key)
        next_index = (current_index + 1) % len(keys)
        return keys[next_index]
    except ValueError:
        # If current_key is not found in the dict, return the first key
        return keys[0] if keys else None


def get_previous_key(data_dict, current_key) -> str:
    """
    Changes the current key to the previous key in the dictionary.
    If the current key is the first one, it loops around to the last key.
    """
    keys = list(data_dict.keys())
    if not keys:
        return None

    try:
        current_index = keys.index(current_key)
        previous_index = (current_index - 1 + len(keys)) % len(keys)
        return keys[previous_index]
    except ValueError:
        # If current_key is not found in the dict, return the last key
        return keys[-1]
