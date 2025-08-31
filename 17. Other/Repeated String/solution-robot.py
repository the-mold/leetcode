def count_letters_a(string, n):
    if not string or n <= 0:
        return 0
        
    count = 0
    str_pointer = 0
    
    for i in range(n):
        if str_pointer >= len(string):
            str_pointer = 0
            
        if string[str_pointer].lower() == "a":
            count += 1
            
        str_pointer += 1
    
    return count
