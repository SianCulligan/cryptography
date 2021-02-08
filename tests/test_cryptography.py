from cryptography import __version__
from cryptography.cryptography import decrypt, encrypt, crack


def test_version():
    assert __version__ == '0.1.0'

# encrypt_a_string_with_a_given_shift
def test_can_encrypt_a_string_with_a_given_shift():
    expected = "lipps"
    actual = encrypt("hello", 4)
    assert expected == actual

# decrypt_a_previously_encrypted_string_with_the_same_shift
def test_can_decrypt_a_previously_encrypted_string_with_the_same_shift():
    expected = "hello"
    actual = decrypt("lipps", 4)
    assert expected == actual

# encryption_should_handle_upper_and_lower_case_letters
def test_encryption_should_handle_upper_and_lower_case_letters():
    expected = "uijt jt b uftu"
    actual = encrypt("THIS is A test", 1)
    assert expected == actual


# encryption_should_allow_non-alpha_characters_but_ignore_them, including white space
def test_encryption_ncryption_should_allow_non_alpha_characters():
    expected = "xfmm ifsft b upvhi "
    actual = encrypt("Well here's a tough 1", 1)
    assert expected == actual

# can_decrypt_encrypted_version_of_It was the best of times it was the worst of times._WITHOUT knowing the shift used.

def test_can_decrypt_encrypted_versions_WITHOUT_the_shift():
    expected = "it was the best of times it was the worst of times "
    actual = crack("sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc")
    assert expected == actual



