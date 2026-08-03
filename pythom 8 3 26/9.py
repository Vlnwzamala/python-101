def calculator_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    mainimum = min(numbers)
    return total_sum, average, maximum, mainimum

numbers = [5,10,15,20,25]
total,avg,max_num,min_num = calculator_stats(numbers)

print(f"total sum: {total}")
print(f"averafe: {avg}")
print(f"maximum: {max_num}")
print(f"mininum: {min_num}")

