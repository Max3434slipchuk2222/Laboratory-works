list = [121, "голова", 30, "борода", 4, "око", 57, "сонце", 12, "день", 22, "річка", 99, "вуса", 1, "лікар", 33, "горло", 234, "кіт"]

int_list = []
str_list = []

for element in list:
    if type(element) == int:
        int_list.append(element)
    elif type(element) == str:
        str_list.append(element)

sort_int = sorted(int_list)
sort_str = sorted(str_list)

new_list = sort_int + sort_str

krat_ints = []
for number in int_list:
    if number % 2 == 0:
        krat_ints.append(number)

upper_strs = []
for word in str_list:
    upper_strs.append(word.upper())

print("Початковий список:")
print(list)

print("Відсортований основний список: ")
print(new_list)

print("\n Список з елементами кратними 2: ")
print(krat_ints)

print("\n Список рядків, записаних великою літерою: ")
print(upper_strs)
