def add_setting(settings, key_value_pair):
    key, value = key_value_pair
    key_lower = key.lower()
    value_lower = value.lower()
    
    if key_lower in settings:
        return f"Setting '{key_lower}' already exists! Cannot add a new setting with this name."
    else:
        settings[key_lower] = value_lower
        return f"Setting '{key_lower}' added with value '{value_lower}' successfully!"

def update_setting(settings, key_value_pair):
    key, value = key_value_pair
    key_lower = key.lower()
    value_lower = value.lower()
    
    if key_lower in settings:
        settings[key_lower] = value_lower
        return f"Setting '{key_lower}' updated to '{value_lower}' successfully!"
    else:
        return f"Setting '{key_lower}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key_lower = key.lower()
    
    if key_lower in settings:
        del settings[key_lower]
        return f"Setting '{key_lower}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings.items():
        capitalized_key = key.capitalize()
        result += f"{capitalized_key}: {value}\n"
    return result  
    
test_settings = {
    'theme': 'dark',
    'notifications': 'on',
    'volume': 'medium'
}
