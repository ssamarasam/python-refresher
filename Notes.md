# Notes

type annotation for list
import typing
list_of_numbers: typing.List[int] = [1, 2, 3]

typing.Tuple[int, int, int]
typing.Dict[str, int]
typing.Set[int]

fromatted string
text_info = "abcde"
msg = f"this is a {text_info} received from machine"

len(variable)

!=

not - inverts the boolean value


end=" "
usually print writes a newline
if we want to override, then use 'end'

**list comprehension**
num = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in num]



**map**
- map applies the specified fucntion to each iterable

def square(x):
    return x ** 2

sqnum = map(square, numlist)



**Zip**
- takes multiple iterables and generates list of tuples
- *zip can be used for unzipping
- zip can be used to create lists, dicts


slicing:
- minus works reversely
- :: skips to the number specified



**for**

for x in range(7)"
    if x % 2 == 0:
    print(x)


[x for x in range(7) if x % 2 == 0]


list.append(number)


