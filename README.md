# h9nt-protobuf-lib
my ready to use protobuf lib for Python
Thanks for **@xtekky** for the Protobuf Algo


## Installation

Install h9nt using pip:

```bash
pip install h9nt
```


```python
from h9nt import PbEnc

# Example usage:

def __get__payload() -> str:
    payload = {
        1: "Hello World!",
        2: 234,
        3: 556,
        4: 67,
        5: {
            1: 11,
        },
        11: "outpout"
    }
    return payload

def __to_buff(payload: str) -> str:
    try:
        return PbEnc().encrypt_pb_payload(payload)
    except:
        return None

`its just a basic example how its could be used.`
