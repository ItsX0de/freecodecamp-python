def add_setting(dict_settings, tuple_key_value):
    key, value = tuple_key_value
    lower_key = str(key).lower()
    lower_value = str(value).lower()
    if lower_key in dict_settings:
        return f"Setting '{lower_key}' already exists! Cannot add a new setting with this name."
    else:
        dict_settings[lower_key] = lower_value
        return f"Setting '{lower_key}' added with value '{lower_value}' successfully!"
def update_setting(dict_settings, tuple_key_value):
    key, value = tuple_key_value
    lower_key = str(key).lower()
    lower_value = str(value).lower()
    if lower_key in dict_settings:
        dict_settings[lower_key] = lower_value
        return f"Setting '{lower_key}' updated to '{lower_value}' successfully!"
    else:
        return f"Setting '{lower_key}' does not exist! Cannot update a non-existing setting."
def delete_setting(dict_settings, key):
    lower_key = str(key).lower()
    if lower_key in dict_settings:
        del dict_settings[lower_key]
        return f"Setting '{lower_key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(dict_settings):
    if not dict_settings:
        return "No settings available."
    else:
        message = "Current User Settings:\n"
        for key, value in dict_settings.items():
            message = message + f"{key.capitalize()}: {value}\n"
        return message
test_settings = {
    "theme": "dark",
    "volume": "high"}