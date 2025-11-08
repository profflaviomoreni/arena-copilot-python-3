import os
import sys

# Garantir que o diretório do projeto esteja no sys.path para imports funcionarem ao executar como script
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.desafios import eh_palindromo, intersecao_unica, soma_intervalos


def _format_args_for_display(args):
    if isinstance(args, (list, tuple)):
        return ", ".join(repr(a) for a in args)
    return repr(args)


def main() -> int:
    print("== Arena Copilot - Demo ==\n")

    exemplos = [
        ("eh_palindromo", eh_palindromo, ("À sogra má e amargosa",)),
        ("intersecao_unica", intersecao_unica, ([1, 2, 2, 3], [2, 2, 4])),
        ("soma_intervalos", soma_intervalos, ([(1, 5), (3, 7), (10, 11)],)),
    ]

    for nome, fn, args in exemplos:
        try:
            resultado = fn(*args) if isinstance(args, (list, tuple)) else fn(args)
            print(f"{nome}({ _format_args_for_display(args) }) => {resultado}")
        except Exception as e:
            print(f"{nome}({_format_args_for_display(args)}) falhou: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())