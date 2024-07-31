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

"mountains:.upper()

"hello ".strip()
" hello ".lstrip()
" hello ".rstrip()

"forest".endswith("rest")  -- True

" ".isnumeric()
"12345".isnumeric()

int("123")

" ".join(["this", "is", "an", "apple"])

"split this".split() -- ["split", "this"]

"hello".count("l")  -- 2


name = "aaa"
age = 23
print("his name is {}, and his age is {}".format(name, age))

print("his name is {}, and his age * 3 is {}".format(name=name, age=age*3))


{:.2f}   - decimal

{:3>} - occupy 3 positions

{:6.2f} - occupies 6 positions and 2 for decimal

"hello".isalpha()  - True

"string".replace(old, new)

{}
{1}

{variable}

{:.<6s}

print(f"the price is {price:.2f})

list.append("hello")
list.insert(0, "hello")
list.remove("hello")
list.pop(3)


for index, person in enumurate(list_winners):
    print(f"{index} - {person}")


list methods:
1. append
2. pop
3. remove
4. reverse
5. insert
6. sort
7. clear
8. copy
9. extend(other list)
10. map
11. zip


new_tuple = tuple(list)


newtuple = (1, 2, [2, 3, 4])

the mutuable list in the above tuple can be modified newtuple[2][0] = 'a' --> (1, 2, ["a", 3, 4])







