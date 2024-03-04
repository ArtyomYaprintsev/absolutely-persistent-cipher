import random

from tools import hex_list_to_int, int_list_to_hex, key_to_hex_list, xor_lists


def generate_key(length: int) -> str:
    """Generate a random key of a given length."""
    return ''.join(f'{random.randint(0,255):02X}' for _ in range(length))


def encode_key(key: str, encoder: int) -> str:
    """Encode a key with a given encoder number.

    Convert the given encoder number to the hex format and insert in the
    middle of the encoded key.
    """
    encoder = ((encoder + 5) * 15) % 256

    key_as_int_list = hex_list_to_int(key_to_hex_list(key))
    encoder_as_list = [encoder for _ in range(len(key_as_int_list))]

    encoded = int_list_to_hex(xor_lists(key_as_int_list, encoder_as_list))
    encoded.insert(len(encoded) // 2, f'{encoder:02x}')

    return ''.join(encoded)


def decode_key(encoded_key: str) -> str:
    """Decode the given encoded key.

    Get the encoder number from the middle of the encoded key and return
    decoded key.
    """
    key_as_hex_list = key_to_hex_list(encoded_key)
    encoder_as_hex = key_as_hex_list[len(key_as_hex_list) // 2]

    # Use len - 1 because one of the elements is encoder
    encoder = int(encoder_as_hex, 16)
    encoder_as_list = [encoder for _ in range(len(key_as_hex_list) - 1)]

    decoded = int_list_to_hex(
        xor_lists(
            hex_list_to_int(
                [item for item in key_as_hex_list if item != encoder_as_hex],
            ),
            encoder_as_list
        ),
    )

    return ''.join(decoded)


def get_encoded_key_group(base_key: str, length: int = 10) -> list[str]:
    """Get a group of encoded keys from a base key."""
    group = [encode_key(base_key, index) for index in range(length)]

    with open('encoded_keys.txt', 'w') as file:
        file.write('\n'.join(group))

    return group


get_encoded_key_group(generate_key(10))
