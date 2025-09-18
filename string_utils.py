def print_string(s):
    if not isinstance(s, str):
        print("Помилка: аргумент має бути рядком")
        return
    print(s)

def check_case(s):
    if not isinstance(s, str):
        print("Помилка: аргумент має бути рядком")
        return
    if s.isupper():
        print("Всі літери великі")
    elif s.islower():
        print("Всі літери малі")
    else:
        print("Змішаний регістр")

def get_upper_list(word):
    if not isinstance(word, str):
        print("Помилка: аргумент має бути рядком")
        return []
    return [ch.upper() for ch in word]
