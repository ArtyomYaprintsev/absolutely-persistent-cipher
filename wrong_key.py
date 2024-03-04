from source import BASE_KEY, INITIAL, DECODED_WRONG
from tools import \
    cp1251_decode, \
    int_list_to_hex, \
    format_hex, \
    xor_arrays, \
    encode_message, \
    get_key_for_decoded_message


encoded = encode_message(INITIAL, BASE_KEY)

key_wrong = get_key_for_decoded_message(encoded, DECODED_WRONG)

print("WRONG KEY:", format_hex(int_list_to_hex(key_wrong)))

# Decode encoded message with the wrong key
decode_with_wrong_hex = cp1251_decode(bytes(xor_arrays(encoded, key_wrong)))

print('DECODE WITH WRONG KEY:', decode_with_wrong_hex)

assert decode_with_wrong_hex == DECODED_WRONG, "The decode key is wrong"
