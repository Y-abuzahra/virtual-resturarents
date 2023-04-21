def naive_pattern_search(text, pattern):  
    if pattern in text[:len(pattern)]:
        return True
    
                