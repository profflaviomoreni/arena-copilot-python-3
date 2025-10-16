import unicodedata
import re
from typing import Iterable, List, Tuple

def _remover_acentos(s: str) -> str:
    nf = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in nf if unicodedata.category(ch) != "Mn")

def eh_palindromo(texto: str) -> bool:
    if not isinstance(texto, str):
        return False
    s = _remover_acentos(texto.lower())
    s = re.sub(r"[^a-z0-9]", "", s)
    return s == s[::-1]

def intersecao_unica(lista1: Iterable, lista2: Iterable) -> List:
    set1, set2 = set(lista1), set(lista2)
    inter = sorted(set1 & set2)
    return inter

def soma_intervalos(intervalos: Iterable[Tuple[int,int]]) -> int:
    iv = list(intervalos)
    if not iv:
        return 0
    iv.sort(key=lambda x: x[0])

    total = 0
    cur_ini, cur_fim = iv[0]

    for ini, fim in iv[1:]:
        if fim < ini:
            ini, fim = fim, ini
        if ini <= cur_fim:  # mescla se toca (fim == ini) ou sobrepõe
            if fim > cur_fim:
                cur_fim = fim
        else:
            total += (cur_fim - cur_ini)
            cur_ini, cur_fim = ini, fim

    total += (cur_fim - cur_ini)
    return total
