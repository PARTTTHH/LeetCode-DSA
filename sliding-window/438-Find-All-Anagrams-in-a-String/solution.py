class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_dict = {}
        p_dict = {}
        
        for i in range(len(p)):
            p_dict[p[i]] = p_dict.get(p[i], 0) + 1
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        start_points = []

        if s_dict == p_dict:
            start_points.append(0)

        for i in range(len(p), len(s)):
            new_char = s[i]
            s_dict[new_char] = s_dict.get(new_char, 0) + 1

            old_char_index = i - len(p)
            old_char = s[old_char_index]
            s_dict[old_char] -= 1

            if s_dict[old_char] == 0:
                del s_dict[old_char]

            if s_dict == p_dict:
                start_points.append(old_char_index + 1)

        return start_points
