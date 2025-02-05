"""
Lecture 13

Last class:
    Tying up parameters and scope
    Dictionaries

Today:
    Midterm information
    More on dictionaries
        Complexity
        Sets
        Structures
"""

def count_all_words(words):
    """
    Count the number of occurrences of each word in the list

    Input:
        words (list[str]): list of words
    
    Output (dict[str,int]): dictionary that maps a string to
        the number of times it appears in the list
    """
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
    return counts


def locate_all_words(words):
    """
    Locate the occurrences of each word in the list

    Input:
        words (list[str]): list of words
    
    Output (dict[str,list[int]]): dictionary that maps a string to
        the locations where it appears in the list
    """
    locations = {}
    for i, word in enumerate(words):
        if word not in locations:
            locations[word] = [i]
        else:
            locations[word].append(i)
    return locations

def count_kmers(k, seq):
    """
    Count the number of k-mers of in the given sequence

    Input:
        k (int): length of subsequences
        seq (str): DNA sequence
    
    Output (list[tuple[str,int]]): list of (kmer, count) pairs
    """
    counts = []
    for i in range(len(seq) - k + 1):
        subseq = seq[i:i+k]
        found = False
        for j, (kmer, count) in enumerate(counts):
            if kmer == subseq:
                counts[j] = (kmer, count + 1)
                found = True
                break
        if not found:
            counts.append((subseq, 1))
    return counts


def count_kmers2(k, seq):
    """
    Count the number of k-mers of in the given sequence

    Input:
        k (int): length of subsequences
        seq (str): DNA sequence
    
    Output (list[tuple[str,int]]): list of (kmer, count) pairs
    """
    counts = {}
    for i in range(len(seq) - k + 1):
        subseq = seq[i:i+k]
        if subseq not in counts:
            counts[subseq] = 1
        else:
            counts[subseq] += 1
    return counts
