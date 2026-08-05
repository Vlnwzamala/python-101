numbers = [4,2,9,1,5,6]

length = len(numbers)
print(f"Length of the List: {length}")

total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}")

max_value = max(numbers)
print(f"Maximum value: {max_value}")

min_value = min(numbers)
print(f"Minimun value: {min_value}")

sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

bool_list = [False , True , False]
any_true = any(bool_list)
print(f"Ace all elements True? {any_true}")

all_true = all(bool_list)
print(f"are all elements true? {all_true}")

string = "hello"
char_list = list(string)
print(f"list of characters: {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"reversef list: {reversed_numbers}")

enumerate_numbers = list(enumerate(numbers))
print(f"{enumerate_numbers}")