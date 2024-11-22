from src.phonebook import Phonebook


class TestPhonebook:

    def test_add(self):
        phonebook = Phonebook()
        resultado_esperado = "Numero adicionado"

        resultado = phonebook.add("Andre", "465465466")
        assert resultado == resultado_esperado


    def test_add_com_caracteres_especial_1(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("@", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_caracteres_especial_2(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("#", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_caracteres_especial_3(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("$", "11657897")
        assert resultado == resultado_esperado


    def test_add_com_caracteres_especial_4(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("%", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_name_none(self):
        phonebook = Phonebook()
        resultado_esperado = "Numero adicionado"

        resultado = phonebook.add(" ", "11657897")
        print(phonebook.get_phonebook_sorted())
        assert resultado == resultado_esperado

