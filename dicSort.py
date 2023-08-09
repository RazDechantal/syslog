#!/usr/bin/env python3
import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

"""
Sort function
"""
def sortDic():
    print(sorted(fruit.items()))

"""
We'll now sort the dictionary using the item's key. For this use the operator module.
Pass the function itemgetter() as an argument to the sorted() function. Since the second element of tuple needs to be sorted, pass the argument 0 to the itemgetter function of the operator module.
"""
def sortDicKey():
    print(sorted(fruit.items(), key=operator.itemgetter(0)))

"""
To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module.
"""
def sortDicVal():
    print(sorted(fruit.items(), key=operator.itemgetter(1)))

"""
Finally, you can also reverse the order of the sort using the reverse parameter. This parameter takes in a boolean argument.

To sort the fruit object from most to least occurrence, we pass the argument reverse=True.
"""
def revSortedDic():
    print(sorted(fruit.items(), key = operator.itemgetter(1), reverse=True))

def main():
    sortDic()
    sortDicKey()
    sortDicVal()
    revSortedDic()
    return 0


if __name__ == "__main__":
    main()
