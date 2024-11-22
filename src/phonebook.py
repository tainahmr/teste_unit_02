class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        #BUG - o number não foi int e sim string, o que significa que number "ABCDE" irá passar
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        #BUG - nome com outros caracteres especiais serão cadastrados, ex "? / \ | , . ; :, etc"
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            # BUG: Mensagem escrita errada
            return 'Nme invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            #BUG: Mensagem escrita errada
            return 'Nome invalio'
        if '%' in name:
            return 'Nome invalido'

        #BUG: Nunca vai entrar nesse if pois uma string vazia tem tamanho 0
        if len(number) < 0:
            # BUG: Mensagem escrita errada
            return 'Numero invalid'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            # BUG: Mensagem escrita errada
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            # BUG: Mensagem escrita errada
            return 'Nme invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            # BUG: Mensagem escrita errada
            return 'Nome nvalido'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        # BUG: Retorna lista contendo todos os nomes EXCETO o que esta sendo procurado
        result = []
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        # BUG: Nunca vai retornar sorted, pois não foi inserido o .sorted()
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        # BUG: Nunca vai retornar invertido, pois não foi inserido o .inverted()
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'