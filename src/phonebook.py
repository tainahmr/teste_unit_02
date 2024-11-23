class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        if any(char in name for char in ['#', '@', '!', '%', '$']):
            return 'Nome invalido'

        #BUG: Nunca vai entrar nesse if pois uma string vazia não tem tamanho < 0
        #CORREÇÃO: substituido < por ==
        if len(number) == 0:
            # BUG: Mensagem escrita errada
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        BUG - o retorno tem sido apenas com número, deveria retornar número + nome
        :return: return number of person with name
        MELHORIA: retirado os if´s e deixei um único
        """
        if any(char in name for char in ['#', '@', '!', '%', '$']):
            return 'Nome invalido'
        #CORREÇÃO - inserido o name para listar number + name
        return name, self.entries[name]

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """
        BUG: os valores tem retornado como dict
        :return: return all numbers in phonebook
        BUG CORRIGIDO: transformar retorno dos valores em uma lista
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        BUG: Retorna lista contendo todos os nomes EXCETO o que esta sendo procurado, devido o NOT IN
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        CORREÇÃO: Retirado o 'not in' do if
        """

        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        BUG: Não vai retornar sorted, pois não foi inserido o sorted()
        :return: return phonebook in sorted order
        BUG CORRIGIDO: Foi inserido o sorted()
        """

        return sorted(self.entries)

    def get_phonebook_reverse(self):
        """
        BUG: Não vai retornar reverse, pois não foi inserido o .reversed() e os dados estão como dict.
        :return: return phonebook in reverse sorted order
        BUG CORRIGIDO: Inserir o reverse e transformar em lista
        """

        return sorted(self.entries.keys(), reverse=True)

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        if name in self.entries:
            self.entries[name] = number
            return 'Numero alterado'
        return 'Contato não encontrado'

    def get_name_by_number(self, number):
        for name, numero in self.entries.items():
            if numero in number:
                return name