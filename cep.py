import requests

class Cep:
    def __init__(self, cep):
        if self.validate_cep(cep):
            self.cep = str(cep)
        else:
            raise ValueError("Not found.")

    def __str__(self):
        return self.format_cep()

    def validate_cep(self, cep):
        cep = str(cep)
        if len(cep) == 8:
            return True
        else:
            raise ValueError("Invalid cep.")

    def format_cep(self):
        format_cep = "{}-{}".format(
            self.cep[:5],
            self.cep[5:]
        )
        return format_cep

    def access_api(self):
        url = "https://viacep.com.br/ws/{}}/json/".format(self.cep)
        r = requests.get(url)
        information = r.json()
        return("address information:/cep: {}/ street: {}/ district: {}/ state: {}".format(
            information['cep'],
            information['logradouro'],
            information['bairro'],
            information['localidade']
        ))