numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

number_with_no_nonetype = numbers[:4] + numbers[5:]
numbers[4] = sum(number_with_no_nonetype) / len(numbers)

print("Измененный список:", numbers)