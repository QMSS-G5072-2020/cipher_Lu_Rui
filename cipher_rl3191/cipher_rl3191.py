def cipher(text, shift, encrypt=True):
    """
    Caesar cipher, one of the simplest and most widely known encryption techniques.
    In short, each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text: str
        A string that you want to encrypt or decrypt.
    shift: int
        The number of positions you want each letter in your 'text' to be shifted down the alphabet.
    encrypt: bool
        A boolean that indicates whether you want to encrypt (True) or decrypt (False) the text.

    Returns
    -------
    str
        The encrypted or decrypted new text.

    Examples
    --------
    >>> from cipher_rl3191 import cipher_rl3191
    >>> text = 'hello world!'
    >>> shift = 1
    >>> cipher_rl3191.cipher(text, shift, encrypt = True)
    'ifmmp xpsme!'
    >>> cipher_rl3191.cipher(text, shift, encrypt = False)
    'gdkkn vnqkc!'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text