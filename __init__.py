from pyproto    import ProtoBuf
from json       import loads
from user_agent import generate_user_agent
from re         import search

# Latest version. 2024 by @h9nt on Github


class PbEnc:
    @staticmethod
    def encrypt_pb_payload(payload: str) -> str:
        try:
            return ProtoBuf(payload).toBuf()
        except Exception:
            return None
    
    @staticmethod
    def pb_get_raw_body(data: bytes, a: int, b: int) -> str:
        return ''.join(ProtoBuf(data).getProtoBuf(a).getBytes(b)).decode("utf-8")
    
    @staticmethod
    def get_rresp(response_body: str) -> str:
        try:
            json_res = response_body[response_body.find('['):]
            parse_m = loads(json_res)
            return {"rresp": parse_m[1]}
        except ValueError:
            return None


def generateUa() -> str:
    return ''.join(str(generate_user_agent()))

def _resp(response_body: str) -> str:
    try:
        pattern = r'<input type="hidden" id="recaptcha-token" value="(.*?)">'
        match = search(pattern, response_body)
        if (match):
            return match.group(1)
        else:
            return None
    except Exception:
        return
