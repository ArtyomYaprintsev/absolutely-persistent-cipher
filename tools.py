from typing import Iterable, Any


def cp1251_encode(s: str) -> list[str]:
    """Encode a string to cp1251.

    Return a list of hex strings.
    """
    return int_list_to_hex(s.encode('cp1251'))


def cp1251_decode(b: bytes) -> str:
    """Decode a bytes to string with cp1251 encoding."""
    return b.decode('cp1251')


def int_list_to_hex(lst: Iterable[Any]) -> list[str]:
    """Convert a list of integers to a list of hex strings."""
    return [f'{item:02x}' for item in lst]


def hex_list_to_int(lst: Iterable[str]) -> list[int]:
    """Convert a list of hex strings to a list of integers."""
    return [int(item, 16) for item in lst]


def key_to_hex_list(key: str) -> list[str]:
    """Convert a key to a list of hex strings."""
    return [key[i:i + 2] for i in range(0, len(key), 2)]


def format_hex(lst: list[str]) -> str:
    """Nicely format a list of hex strings."""
    return ' '.join(item.upper() for item in lst)


def xor_arrays(l1: list[int], l2: list[int]) -> list[int]:
    """XOR two list of integers."""
    return [a ^ b for a, b in zip(l1, l2)]


def encode_message(message: str, key: str) -> list[int]:
    key_hex = [key[i:i + 2] for i in range(0, len(key), 2)]

    if len(key_hex) != len(message):
        raise ValueError(
            'Key length must be equal to the length of the message.',
        )

    return xor_arrays(
        hex_list_to_int(cp1251_encode(message)),
        hex_list_to_int(key_hex),
    )


def get_key_for_decoded_message(
    encoded: list[int],
    decoded: str,
) -> list[int]:
    """Get the decode key for a decoded message.

    Attributes:
        encoded (list[int]): The encoded message.
        decoded (str): The decoded message.

    Returns:
        The key which can be used to get decoded message from the encoded one.
    """
    if len(encoded) != len(decoded):
        raise ValueError(
            'Encoded message and decoded message must have the same length.',
        )

    return xor_arrays(encoded, hex_list_to_int(cp1251_encode(decoded)))
