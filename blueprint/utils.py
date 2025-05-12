
import zlib
import base64

def deflate_and_encode(plantuml_text: str):
    zlibbed_str = zlib.compress(plantuml_text.encode("utf-8"))[2:-4]
    encoded = base64.b64encode(zlibbed_str).decode('utf-8')
    return encoded
def encode_plantuml(text):
    """
    Encodes PlantUML text for URL usage (DEFLATE + custom base64).
    """
    def encode_6bit(b):
        if b < 10:
            return chr(48 + b)
        b -= 10
        if b < 26:
            return chr(65 + b)
        b -= 26
        if b < 26:
            return chr(97 + b)
        b -= 26
        return '-' if b == 0 else '_'

    def append3bytes(b1, b2, b3):
        c1 = b1 >> 2
        c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
        c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
        c4 = b3 & 0x3F
        return ''.join([
            encode_6bit(c1 & 0x3F),
            encode_6bit(c2 & 0x3F),
            encode_6bit(c3 & 0x3F),
            encode_6bit(c4 & 0x3F),
        ])

    data = zlib.compress(text.encode('utf-8'))[2:-4]
    res = ""
    for i in range(0, len(data), 3):
        b1 = data[i]
        b2 = data[i + 1] if i + 1 < len(data) else 0
        b3 = data[i + 2] if i + 2 < len(data) else 0
        res += append3bytes(b1, b2, b3)
    return res