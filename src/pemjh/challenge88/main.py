""" Challenge88 """


def product_finder(known=None):
    """ Return a function configured to find possible products using a
    cache. """
    __known = known or dict()

    def find_possible_products(limit):
        """ Return the set of possible products up to limit. """

        if limit in __known:
            return __known[limit]

        products = set()

        multi = 2
        while multi <= limit:
            for multi2, total, num_digits in find_possible_products(
                    limit // multi):
                products.add((multi * multi2, total + multi, num_digits + 1))

            products.add((multi, multi, 1))
            multi += 1

        __known[limit] = products
        return products

    return find_possible_products


def main(limit):
    """ challenge88 """
    found = [2 * i for i in xrange(limit + 1)]

    find_possible_products = product_finder()
    for product, total, num_digits in set(
            find_possible_products(limit * 2)):
        # Get digits so that total == product
        digits = product - total + num_digits
        if digits <= limit and found[digits] > product:
            found[digits] = product

    return sum(set(found[2:]))
