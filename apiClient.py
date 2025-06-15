import requests
import sys
import json
from dotenv import load_dotenv
import os


class apiClient:
    def __init__(self):
        load_dotenv()
        self.serverUrl = os.getenv("APISERVERURL")
        self.headers = {
            'Accept': 'application/json'
        }

    def get(self, method: str = "", params: dict = {}):
        try:
            response = requests.get(self.serverUrl + "/" + method, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if 'code' in data and 'result' in data:
                return (data['code'], json.loads(data['result']))
            else:
                return (9, f"Invalid response")
        except requests.exceptions.HTTPError as http_err:
            return (1, f"{http_err}")
        except requests.exceptions.Timeout:
            return (2, f"The request timed out")
        except requests.exceptions.RequestException as err:
            return (3, f"{err}")

    def post(self, method: str = "", params: dict = {}):
        try:
            response = requests.post(self.serverUrl + "/" + method, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if 'code' in data and 'result' in data:
                return (data['code'], json.loads(data['result']))
            else:
                return (9, f"Invalid response")
        except requests.exceptions.HTTPError as http_err:
            return (1, f"{http_err}")
        except requests.exceptions.Timeout:
            return (2, f"The request timed out")
        except requests.exceptions.RequestException as err:
            return (3, f"{err}")
