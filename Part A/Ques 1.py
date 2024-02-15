
die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]

# Input the sum to calculate
sum_to_calculate = int(input("Enter the sum you want to calculate: "))

# Initialize variables for total outcomes and list of combinations
total_outcomes = 0
combinations = []

# Loop through all combinations of die A and die B
for face_A in die_A:
    for face_B in die_B:
        print(face_A, face_B)  # Print the combination
        if face_A + face_B == sum_to_calculate:
            combinations.append((face_A, face_B))  # Add combination to the list
            total_outcomes += 1  # Increment total outcomes

# Print total possible outcomes
print("Total possible outcomes:")
for combination in combinations:
    print(combination)

# Print total probability
print("Total probability of getting the sum {} is: {}/{}".format(sum_to_calculate, total_outcomes, len(die_A) * len(die_B)))
