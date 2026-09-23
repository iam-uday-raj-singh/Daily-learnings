from collections import defaultdict
def group_anagram(strs):
    anagram_maps= defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_maps[sorted_word].append(word)
    
    return list(anagram_maps.values())

if __name__ == "__main__":
    anagram_input = input("Enter anagrams to be tested separated by spaces: ").split()
    group_anag = group_anagram(anagram_input)
    print(group_anag)