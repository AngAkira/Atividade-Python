def comparar(arquivo):
    print(f"Comparando dados:{(arquivo["stroke"]==1).sum()}")
    print(f"Comparando dados:{(arquivo["stroke"]==0).sum()}")

