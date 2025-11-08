# Script auxiliar para o professor: executa rapidamente as funções e imprime resultados esperados.
from src.desafios import eh_palindromo, intersecao_unica, soma_intervalos

print("Palíndromo:", eh_palindromo("À sogra má e amargosa"), " (esperado: True)")
print("Interseção:", intersecao_unica([1,2,2,3], [2,2,4]), " (esperado: [2])")
print("Intervalos:", soma_intervalos([(1,5),(3,7),(10,11)]), " (esperado: 7)")
