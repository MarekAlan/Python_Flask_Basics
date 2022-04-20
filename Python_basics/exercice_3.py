def check_palindrome(text):
    """Check if given text is palindrome.

    :param str text: some text
    :rtype: bool
    :return: True if given text is palindrome False elsewhere
    """
    text = text.lower().replace(' ', '')
    return text == text[::-1]


if __name__ == '__main__':
    print(check_palindrome("Do geese see God"))
    print(check_palindrome("This is not a palindrome"))
