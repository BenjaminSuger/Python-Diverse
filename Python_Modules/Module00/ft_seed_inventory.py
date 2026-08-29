def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit = unit.lower()  # pas sur de ca
    seed_type = seed_type.lower()
    match unit:
        case "packets":
            print(f"{seed_type} seeds: {quantity} availaable")
        case "grams":
            print(f"{seed_type} seeds: {quantity} grams total")
        case "area":
            print(f"{seed_type} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")


ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
