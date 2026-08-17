def letter_stew(jar_a: str, jar_b: str) -> bool:
    jar_a = jar_a.lower().replace(' ', '')
    jar_b = jar_b.lower().replace(' ', '')
    list_jar_a = sorted(list(jar_a)) 
    list_jar_b = sorted(list(jar_b))
    if len(list_jar_a) != len(list_jar_b):
        return False
    for i in range(0, len(list_jar_a)):
        if list_jar_a[i] != list_jar_b[i]:
            return False
    return True

my_str = "aab"
my_str_b = "abb"
print(letter_stew(my_str, my_str_b))
print(letter_stew("a gentleman", "elegant man"))
