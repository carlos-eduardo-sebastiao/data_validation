from validate_docbr import CPF, CNPJ

class Documents:
    
    @staticmethod
    def create_documents(document):
        document = str(document)
        if len(document) == 11:
            return Cpf(document)
        elif len(document) == 14:
            return Cnpj(document)
        else:
            raise ValueError("Invalid document type.")

class Cpf:

    def __init__(self, document):
        self.document = str(document)
        if self.validate_cpf(document):
            self.cpf = document
        else:
            raise ValueError("Invalid CPF.")

    def __str__(self):
        return self.format_cpf()

    def validate_cpf(self, document):
        validator = CPF()
        return validator.validate(document)

    def format_cpf(self):
        mask_cpf = CPF()
        return mask_cpf.mask(self.cpf)

class Cnpj:

    def __init__(self, document):
        self.document = str(document)
        if self.validate_cnpj(document):
            self.cnpj = document
        else:
            raise ValueError("Invalid CNPJ.")

    def __str__(self):
        return self.format_cnpj()

    def validate_cnpj(self, document):
        validator = CNPJ()
        return validator.validate(document)

    def format_cnpj(self):
        mask_cnpj = CNPJ()
        return mask_cnpj.mask(self.cnpj)