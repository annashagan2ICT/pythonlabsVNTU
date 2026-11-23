def combine_sequences(seq1, seq2):
    result = []
    
    length = min(len(seq1), len(seq2))
    
    for i in range(length):
        result.append(seq1[i])
        result.append(seq2[i])
        
    return result


list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print(*combine_sequences(list1, list2))