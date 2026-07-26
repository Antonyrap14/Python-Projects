inventario = {"pane","pasta","sugo","roll","temaki","nigiri","uramaki","gyoza","pasta"}
obsoleta = {"pane","pasta","sugo"}

def remove_vecchi(inventario,vecchi):
    for elementi in list(inventario):
        if elementi in vecchi:
            inventario.discard(elementi)
    return inventario

print(f"L'inventario è {inventario}")
print(f"Ora è {remove_vecchi(inventario,obsoleta)}")
        