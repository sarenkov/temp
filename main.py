def intro(name: str) -> None:
    print(name)

if __name__ == "__main__":
    names = ["Ivan", "Fedot", "Givi"]
    for name in names:
        name = name.upper()
        intro(name)