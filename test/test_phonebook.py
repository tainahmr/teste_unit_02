from src.phonebook import Phonebook


class TestPhonebook:

    def test_add(self):
        phonebook = Phonebook()
        resultado_esperado = "Numero adicionado"

        resultado = phonebook.add("Andre", "465465466")
        assert resultado == resultado_esperado


    def test_add_com_caracteres_especial_arroba(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("@", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_caracteres_especial_hashtag(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("#", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_caracteres_especial_exclamacao(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("!", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_caracteres_especial_cifrao(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("$", "11657897")
        assert resultado == resultado_esperado


    def test_add_com_caracteres_especial_percentual(self):
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        resultado = phonebook.add("%", "11657897")
        assert resultado == resultado_esperado

    def test_add_com_name_none(self):
        phonebook = Phonebook()
        resultado_esperado = "Numero adicionado"

        resultado = phonebook.add(" jose", " ")
        print(phonebook.get_phonebook_sorted())
        assert resultado == resultado_esperado

    def test_lookup(self):
        phonebook = Phonebook()
        phonebook.add("Andre", "465465466")
        resultado = "Andre", "465465466"
        resultado_esperado = phonebook.lookup("Andre")
        assert resultado == resultado_esperado
        print(resultado_esperado)

    def test_lookup_com_caracteres_especial_hashtag(self):
        phonebook = Phonebook()
        phonebook.add("#", "465465466")
        resultado = "Nome invalido"
        resultado_esperado = phonebook.lookup("#")
        assert resultado == resultado_esperado
        print(resultado_esperado)

    def test_lookup_com_caracteres_especial_arroba(self):
        phonebook = Phonebook()
        phonebook.add("@", "465465466")
        resultado = "Nome invalido"
        resultado_esperado = phonebook.lookup("@")
        assert resultado == resultado_esperado
        print(resultado_esperado)

    def test_lookup_com_caracteres_especial_exclamacao(self):
        phonebook = Phonebook()
        phonebook.add("ta!nah", "465465466")
        resultado = "Nome invalido"
        resultado_esperado = phonebook.lookup("ta!nah")
        assert resultado == resultado_esperado
        print(resultado_esperado)

    def test_lookup_com_caracteres_especial_cifrao(self):
        phonebook = Phonebook()
        phonebook.add("$aulo", "465465466")
        resultado = "Nome invalido"
        resultado_esperado = phonebook.lookup("$aulo")
        assert resultado == resultado_esperado
        print(resultado_esperado)

    def test_lookup_com_caracteres_especial_percentual(self):
        phonebook = Phonebook()
        phonebook.add("%", "465465466")
        resultado = "Nome invalido"
        resultado_esperado = phonebook.lookup("%")
        assert resultado == resultado_esperado
        print(resultado_esperado)

    def test_get_names(self):
        phonebook = Phonebook()
        phonebook.add("Luis", "12345678")
        resultado_esperado = {'POLICIA', 'Luis'}
        resultado = phonebook.get_names()
        assert resultado_esperado == resultado

    def test_get_numbers(self):
        phonebook = Phonebook()
        phonebook.add("Luis", "12345678")
        resultado_esperado = [ "190", "12345678"]
        resultado = phonebook.get_numbers()
        assert resultado_esperado == resultado

    def test_clear(self):
        phonebook = Phonebook()
        resultado_esperado = 'phonebook limpado'
        resultado = phonebook.clear()
        assert resultado_esperado == resultado
    def test_search(self):
        phonebook = Phonebook()
        phonebook.add("Andre", "123456")
        phonebook.add("Andreia", "123")
        phonebook.add("Andrea", "12345678")
        resultado_esperado = [{'Andre', "123456"}, {'Andreia', '123'}, {'Andrea', "12345678"}]
        resultado = phonebook.search("Andre")
        assert resultado_esperado == resultado

    def test_get_phonebook_sorted(self):
        phonebook = Phonebook()
        phonebook.add("Zebra", "000")
        phonebook.add("Caio", "111")
        resultado_esperado = ['Caio', 'POLICIA', 'Zebra']
        resultado = phonebook.get_phonebook_sorted()
        assert resultado == resultado_esperado

    def test_get_phonebook_reverse(self):
        phonebook = Phonebook()
        phonebook.add("Zebra", "000")
        phonebook.add("Caio", "111")
        resultado_esperado = ['Zebra', 'POLICIA', 'Caio']
        resultado = phonebook.get_phonebook_reverse()
        assert resultado == resultado_esperado

    def test_delete(self):
        phonebook = Phonebook()
        phonebook.add("Manoel", "333")
        resultado = phonebook.delete('Manoel')
        resultado_esperado = 'Numero deletado'
        assert resultado == resultado_esperado

    def test_change_number(self):
        phonebook = Phonebook()
        phonebook.add("Monica", "456")
        resultado = phonebook.change_number('Monica', '789')
        resultado_esperado = 'Numero alterado'
        assert resultado == resultado_esperado

    def test_get_name_by_number(self):
        phonebook = Phonebook()
        phonebook.add("Ze", "999")
        resultado = phonebook.get_name_by_number('999')
        resultado_esperado = 'Ze'
        assert resultado == resultado_esperado






