countries = input().split(", ")
capitals = input().split(", ")

paired = [f'{pair[0]} -> {pair[1]}' for pair in list(zip(countries, capitals))]
print("\n".join(paired))
