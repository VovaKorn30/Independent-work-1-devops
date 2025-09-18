from string_utils import print_string, check_case, get_upper_list
from generator_utils import even_odd_generator


user_word = input("Введіть слово: ")

print_string(user_word)
check_case(user_word)
print(get_upper_list(user_word))


gen = even_odd_generator()
for _ in range(5):
    print(next(gen))
