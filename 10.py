allTerms = [1, 2, 3, 4, 5, 6, 7, 8]
valid = [1, 3, 4]

invalid = [allTerms[j] for j in range(len(allTerms)) if allTerms[j] not in valid]
           
print invalid
