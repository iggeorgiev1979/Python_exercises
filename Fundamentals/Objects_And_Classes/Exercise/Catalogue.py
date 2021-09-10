class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [x for x in self.products if x.startswith(first_letter)]
        # return list(filter(lambda x: x[0] == first_letter, self.products))

    def __repr__(self):
        print_list = f'Items in the {self.name} catalogue:' + '\n' + '\n'.join(sorted(self.products))
        return print_list


catalogue = Catalogue('Furniture')
catalogue.add_product('Sofa')
catalogue.add_product('Mirror')
catalogue.add_product('Desk')
catalogue.add_product('Chair')
catalogue.add_product('Carpet')
print(catalogue.get_by_letter('C'))
print(catalogue)
