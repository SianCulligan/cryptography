from cryptography import __version__


def test_version():
    assert __version__ == '0.1.0'





# encrypt a string with a given shift
# decrypt a previously encrypted string with the same shift
# encryption should handle upper and lower case letters
# encryption should allow non-alpha characters but ignore them, including white space
# decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
# refer to supplied unit tests.