def count_pattern(text):
    """
    We use the string method find() and a while loop:
    - We first look for "C" starting from a given index.
    - If a "C" is found, we then look for "jeb" starting at that "C".
    - If "jeb" is found after the "C", we count that as one match.
    - Then we update our start index to search for another occurrence.
    """
    count = 0  # To keep track of matches
    start = 0  # Starting index for our search

    while True:
        # Look for the letter "C" starting at index 'start'
        indexC = text.find("C", start)
        if indexC == -1:
            # No more "C" found, so exit the loop
            break

        # Now look for "jeb" after the "C"
        indexJeb = text.find("jeb", indexC)
        if indexJeb == -1:
            # If no "jeb" is found after this "C", then we exit the loop
            break

        # If both "C" and a following "jeb" are found, count one match.
        count += 1

        # Update the start index to search for further matches.
        # We move one character ahead from the current "C" to allow overlapping occurrences.
        start = indexC + 1

    return count


# Example usage:
sample_text = "This is an example: Cabcjeb and Cxyzjeb are matches, but Czzjib is not."
result = count_pattern(sample_text)
print(result)  # Expected output: 2
