fruits_with_dupplicates = ["apple" , "banana" , "apple" , "cherry" , "apple" , "kiwi"]
while "apple" in fruits_with_dupplicates:
    fruits_with_dupplicates.remove("apple")
    print(f"fruits_with_dupplicates : {fruits_with_dupplicates}")