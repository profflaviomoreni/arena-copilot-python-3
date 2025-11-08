import unicodedata
import re
from typing import Iterable, List, Tuple, TypeVar
from numbers import Real

T = TypeVar("T")


def _remover_acentos(s: str) -> str:
    """Remove marcas de acento de uma string usando normalização NFD."""
    if not isinstance(s, str):
        raise TypeError("_remover_acentos espera uma str")
    nf = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in nf if unicodedata.category(ch) != "Mn")


def eh_palindromo(texto: str) -> bool:
    """
    Retorna True se `texto` for palíndromo (ignorando acentos, case e caracteres não alfanuméricos).
    Retorna False se `texto` não for str.
    """
    if not isinstance(texto, str):
        return False
    s = _remover_acentos(texto.lower())
    s = re.sub(r"[^0-9a-z]", "", s)
    return s == s[::-1]


def intersecao_unica(lista1: Iterable[T], lista2: Iterable[T]) -> List[T]:
    """
    Retorna uma lista ordenada e sem duplicatas da interseção entre lista1 e lista2.
    - Tenta ordenar os elementos (sorted). Se não forem comparáveis, preserva a ordem de lista1.
    """
    li1 = list(lista1)
    li2 = list(lista2)

    # Primeiro, tente com conjuntos (requer elementos hashable)
    try:
        set1 = set(li1)
        set2 = set(li2)
        inter = set1 & set2
        try:
            return sorted(inter)
        except TypeError:
            # elementos não comparáveis; retornar em ordem arbitrária (conjunto)
            return list(inter)
    except TypeError:
        # elementos não-hashable: fazer interseção por igualdade preservando ordem de lista1
        res: List[T] = []
        for x in li1:
            if any(x == y for y in li2) and not any(x == z for z in res):
                res.append(x)
        return res


def soma_intervalos(intervalos: Iterable[Tuple[Real, Real]]) -> Real:
    """
    Soma o comprimento da união de intervalos fechados [início, fim].
    - Aceita intervalos com extremidades em qualquer ordem (internamente normalizados).
    - Intervalos que se tocam (ex.: (1,2) e (2,3)) são mesclados.
    - Retorna int se todas as entradas forem inteiras e o resultado for inteiro; caso contrário float.
    """
    iv_list = list(intervalos)

    normalized: List[Tuple[Real, Real]] = []
    for item in iv_list:
        if not (isinstance(item, tuple) and len(item) == 2):
            raise TypeError("Cada intervalo deve ser um tuple de duas coordenadas numéricas")
        a, b = item
        if not (isinstance(a, Real) and isinstance(b, Real)):
            raise TypeError("Coordenadas de intervalo devem ser numéricas (subclasse de numbers.Real)")
        start, end = (a, b) if a <= b else (b, a)
        normalized.append((start, end))

    if not normalized:
        return 0

    normalized.sort(key=lambda x: x[0])

    total = 0.0
    cur_start, cur_end = normalized[0]

    for start, end in normalized[1:]:
        if start <= cur_end:  # mescla se toca ou sobrepõe
            if end > cur_end:
                cur_end = end
        else:
            total += (cur_end - cur_start)
            cur_start, cur_end = start, end

    total += (cur_end - cur_start)

    # Preservar int quando apropriado
    all_ints = all(isinstance(x, int) for interval in normalized for x in interval)
    if all_ints and float(total).is_integer():
        return int(total)
    return total
