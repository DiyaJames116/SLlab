def AtomicDictionary():
    atom={"Au":"Gold","O":"Oxygen","Ag":"Silver","H":"Hydrogen","Na":"Sodium"}
    print(atom)
    new_element=input("Enter new atomic element to be added")
    symbol=input("Enter symbol of the element")
    atom[symbol]=new_element
    print(atom)
    print("Number of elements in the dictionary are ",len(atom))
    key=input("Enter atomic element to be searched")
    if key in atom:
        print(f"{key}-{atom.get(key)} is found at {atom.index(key)}")
    else:
        print(f"{key} was not found")