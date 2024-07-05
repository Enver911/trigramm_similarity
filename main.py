def trigram_similarity(word_check: str, string_check: str) -> int:
    """
    Trigram similarity between two strings is determined by the number of matching character triplets in both strings.
    The algorithm can be generalized to n-grams, where n=1, 2, ...

    The lines are then divided into triplets (trigrams). Finally, the similarity is calculated using the formula:

    s = 2*m / (a ​​+ b).

    Here:

    m - number of matching trigrams
    a - number of trigrams in string1
    b - number of trigrams in string2
    
    ---------------------------------
    
    Триграммное сходство (trigram similarity) между двумя строками определяется числом совпадающих символьных триплетов в обоих строках. 
    Алгоритм можно обобщить на n-граммы, где n=1, 2, ...

    Затем строки разделяются на триплеты (триграммы). Окончательно, сходство вычисляется по формуле:

    s = 2*m / (a + b).

    Здесь:

    m - число совпадающих триграмм
    a - число триграмм в string1
    b - число триграмм в string2
    """
    
    word_check = " " + word_check.upper() + " " 
    string_check = " " + string_check.upper() + " " 

    word_trigrams = [word_check[i: i + 3] for i in range(len(word_check) - 2)] #word trigrams list
    string_check_trigrams = [string_check[i: i + 3] for i in range(len(string_check) - 2)] #string_check trigrams
    
    matches = sum(trigram in string_check_trigrams for trigram in word_trigrams)
    
    similarity_rating = 2 * matches / (len(word_trigrams) + len(string_check_trigrams))
    
    return similarity_rating