'''
    >>> from baralho_polimorfico import Baralho, BaralhoInverso, BaralhoIter
    >>> b = Baralho()
    >>> b[0]
    <A de copas>
    >>> b[:3]
    [<A de copas>, <2 de copas>, <3 de copas>]
    >>> b[-3:]
    [<J de paus>, <Q de paus>, <K de paus>]
    >>> for carta in b:                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    <5 de copas>
    ...
    >>> for carta in reversed(b):                   # doctest:+ELLIPSIS
    ...     print carta
    <K de paus>
    <Q de paus>
    <J de paus>
    <10 de paus>
    ...
    >>> b = BaralhoInverso()
    >>> for carta in b:                             # doctest:+ELLIPSIS
    ...     print carta
    <K de paus>
    <Q de paus>
    <J de paus>
    <10 de paus>
    ...
    >>> b = BaralhoIter()
    >>> for carta in b.iter_genexp():                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    ...
    >>> for carta in b.iter_genfun():                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    ...
    >>> for carta in b.iter_obj():                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    ...
'''


class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)


class Baralho(object):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self.cartas = [Carta(v, n)
                        for n in self.naipes
                        for v in self.valores]

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __len__(self):
        return len(self.cartas)


class BaralhoInverso(Baralho):
    def __iter__(self):
        return reversed(self.cartas)


class BaralhoIter(Baralho):
    def iter_genexp(self):
        return (carta for carta in self.cartas)

    def iter_genfun(self):
        for carta in self.cartas:
            yield carta

    def iter_obj(self):
        class MeuIterador(object):
            def __init__(self, cartas):
                self.cartas = cartas
                self.idx = 0

            def __iter__(self):
                return self

            def next(self):
                if (self.idx >= len(self.cartas)):
                    raise StopIteration()
                item = self.cartas[self.idx]
                self.idx += 1
                return item

        return MeuIterador(self.cartas)
