from fake_useragent import UserAgent
from files import *
from config import register_mode

class Account:
    def __init__(self, email, password, proxy=None):
        self.name = email.split("@")[0]
        self.email = email
        self.password = password
        self.proxy = proxy
        self.user_agent = UserAgent(os='windows').random
        self.token = self.get_token()


    def headers(self):
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "If-None-Match": 'W/"46-s3SxJpZZwK+JVoHqxSZXYvW/sw"',
            "Priority": "u=1, i",
            "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": self.user_agent
        }

    def save_token(self, token):
        self.token = token
        return save_token_json(self.name, token)

    def get_token(self):
        return get_token_json(self.name)

    @staticmethod
    def account_info(name):
        accs = load_from_json("data/accounts.json")
        for acc in accs:
            if acc["name"] == name:
                return acc

class Accounts:
    def __init__(self):
        self.accounts = []

    def loads_accs(self):
        accs = txt_to_list("accs" if not register_mode else "register")
        proxies = txt_to_list("proxies")
        proxies = proxies * int(2 + len(accs) / len(proxies))

        for i, acc in enumerate(accs):
            acc = acc.split(":")
            self.accounts.append(Account(email=acc[0], password=acc[1], proxy=proxies[i]))