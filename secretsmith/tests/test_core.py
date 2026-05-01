import unittest
from secretsmith.core import generate_password, generate_passphrase, generate_api_key

class TestSecretsmith(unittest.TestCase):
    def test_generate_password_length(self):
        pwd = generate_password(length=10)
        self.assertEqual(len(pwd), 10)

    def test_generate_password_charset(self):
        pwd = generate_password(length=100, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True)
        # Check that it contains at least one of each? Not required, but we can check that it's from the allowed set.
        import string
        allowed = string.ascii_letters + string.digits + string.punctuation
        self.assertTrue(all(c in allowed for c in pwd))

    def test_generate_passphrase(self):
        p = generate_passphrase(word_count=3, separator="-")
        self.assertEqual(p.count("-"), 2)

    def test_generate_api_key(self):
        key = generate_api_key(length=32)
        # Should be base64 URL safe, no padding, and length 43? Actually 32 bytes -> base64: 43 chars, but we strip padding.
        # 32 bytes * 8 = 256 bits -> base64: ceil(256/6) = 43 chars, but without padding it's 43 or 44? Let's just check it's alphanumeric plus - and _
        import re
        self.assertTrue(re.match(r'^[A-Za-z0-9_-]+$', key))

if __name__ == '__main__':
    unittest.main()