def analisar_notas(notas):
    if not notas:
        return 0, [], 0

    media = sum(notas) / len(notas)
    notas_acima_media = [nota for nota in notas if nota > media]
    total_aprovados = sum(1 for nota in notas if nota >= 7.0)

    return media, notas_acima_media, total_aprovados


notas = [5.5, 8.0, 9.5, 6.0, 7.5, 4.0]
media, filtradas, aprovados = analisar_notas(notas)

print(f"Média: {media:.2f}")
print(f"Notas acima da média: {filtradas}")
print(f"Total de aprovados: {aprovados}")