def compress(self, chars: list[str]) -> int:
    idx = 0
    result_new_array_length = 0

    while idx < len(chars):
        group_length = 1
        while (group_length + idx < len(chars) and chars[idx + group_length] == chars[idx]):
            group_length += 1

        # needed because if you have aaab, it becomes a3ab in first intteration. In this line you place `b` right after the number: a3bb
        chars[result_new_array_length] = chars[idx]
        
        result_new_array_length += 1

        if group_length > 1:
            group_length_string = str(group_length)
            chars[result_new_array_length:result_new_array_length+len(group_length_string)] = list(group_length_string)
            result_new_array_length += len(group_length_string)
        
        idx += group_length
    
    return result_new_array_length
