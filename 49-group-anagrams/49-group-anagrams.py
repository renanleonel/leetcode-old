class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            if not hashmap.get(str(sorted(word))):
              hashmap[str(sorted(word))] = []
            hashmap[str(sorted(word))].append(word)

        return hashmap.values()