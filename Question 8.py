def is_valid_url(url):
    # First, check if the parameter is a string
    if type(url) != str:
        return False

    # Check if the URL starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    # Remove the protocol part to check the rest of the URL
    if url.startswith("http://"):
        remaining = url[7:]  # remove "http://"
    else:
        remaining = url[8:]  # remove "https://"

    # Check if there is at least one dot in the remaining part
    if "." not in remaining:
        return False

    # Check that there are no spaces in the URL
    if " " in url:
        return False

    # If all checks pass, we consider the URL valid
    return True


# Example usage:
print(is_valid_url("http://www.example.com"))  # Expected output: True
print(is_valid_url("https://example.com/haha"))  # Expected output: True
print(is_valid_url("ftp://example.com"))  # Expected output: False
print(is_valid_url("http://examplecom"))  # Expected output: False
print(is_valid_url("http://exa mple.com"))  # Expected output: False
