class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransomNote_tracker = {}
        magazine_tracker = {}

        for i in range(len(ransomNote)):
            ransomNote_tracker[ransomNote[i]] = ransomNote_tracker.get(ransomNote[i], 0) + 1

        for i in range(len(magazine)):
            magazine_tracker[magazine[i]] = magazine_tracker.get(magazine[i], 0) + 1

        for key, required_count in ransomNote_tracker.items():
            if key not in magazine_tracker or magazine_tracker[key] < required_count:
                return False
        
        return True