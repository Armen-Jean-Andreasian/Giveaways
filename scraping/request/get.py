import requests


def get_url(url: str,
            headers: dict = None,
            cookies: dict = None,
            params: dict = None) -> requests.Response:
    """Sends GET request to API"""
    return requests.get(url=url, params=params, headers=headers, cookies=cookies)
