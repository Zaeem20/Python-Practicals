def hanoi(ndisk, pole_1, pole_3, pole_2):
    if ndisk == 0:
        return
    hanoi(ndisk-1, pole_1, pole_2, pole_3)
    print(f"Shifted {ndisk} disk's: {pole_1} -> {pole_3}")
    hanoi(ndisk-1, pole_2, pole_3, pole_1)

hanoi(3, "A", "C", "B")

