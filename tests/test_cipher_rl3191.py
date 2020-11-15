from cipher_rl3191 import __version__
from cipher_rl3191 import cipher_rl3191

def test_version():
    assert __version__ == '0.1.1'

def test_cipher():
    text = 'hello'
    shift = 22
    encrypt = True
    expected = 'DAHHK'
    actual = cipher_rl3191.cipher(text, shift, encrypt)
    assert actual == expected