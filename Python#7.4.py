def join_with_comma(sequence_str):
  
    items = sequence_str.split()
    return ", ".join(items)


user_input = input("Enter words by species: ")

print(join_with_comma(user_input))