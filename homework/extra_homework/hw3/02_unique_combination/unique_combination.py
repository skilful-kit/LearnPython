def merge_sorted_lists(lst1, lst2):
    merged = []
    i = j = 0
    len1, len2 = len(lst1), len(lst2)
    
    while i < len1 and j < len2:
        if lst1[i] < lst2[j]:
            if not merged or merged[-1] != lst1[i]:
                merged.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            if not merged or merged[-1] != lst2[j]:
                merged.append(lst2[j])
            j += 1
        else:
            if not merged or merged[-1] != lst1[i]:
                merged.append(lst1[i])
            i += 1
            j += 1
    
    while i < len1:
        if not merged or merged[-1] != lst1[i]:
            merged.append(lst1[i])
        i += 1
    
    while j < len2:
        if not merged or merged[-1] != lst2[j]:
            merged.append(lst2[j])
        j += 1
    
    return merged

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
