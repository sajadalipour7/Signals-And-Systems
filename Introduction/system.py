import requests
import numpy as np
import json

def get_system_output(n: np.ndarray, x_n: np.ndarray):
    # Serializing input
    req_body = {"n": n.tolist(), "x_n": x_n.tolist()}

    # Issuing request
    URL = "https://radin-shayanfar.ir/SS/"
    resp = requests.post(URL, json=req_body)
    resp.raise_for_status()

    # Deserializing response
    resp = json.loads(resp.text)
    code = resp["code"]
    status = resp["status"]
    if code == 0:
        n = np.array(resp["n"])
        y_n = np.array(resp["y_n"])
    else:
        raise Exception(status)
    
    return n, y_n
