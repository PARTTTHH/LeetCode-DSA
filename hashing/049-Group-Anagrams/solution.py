class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagram_dict = {}

        for s in strs:
            sorted_key = "".join(sorted(s))

            if sorted_key not in anagram_dict:
                anagram_dict[sorted_key] = []
            anagram_dict[sorted_key].append(s)

        return list(anagram_dict.values())