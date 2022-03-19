from documents import Documents
from telephones import Telephone
from dates import Date
from cep import Cep


def functions():
    documents = input("Enter a cpf or cnpj in the Brazilian standard: ")
    document = Documents.create_documents(documents)
    phones = input("Enter a phone or cell phone: ")
    phone = Telephone(phones)
    register = Date()
    cep = input("Enter the zip number: ")
    zip = Cep(cep)
    print("Date, time and day of the week of your application: ",register)
    print("Document {} is valid".format(document))
    print("Phone {} is valid".format(phone))
    print("Below contains your zip code, such as number, street, neighborhood and state.\n", zip)

functions()