class GroupAnagrams:
    
    def __getPrimeProduct(self, word: str, primes: List[int]) -> int:
        
        #   For each character, there is corresponding prime number, calculate the product.
        prod = 1
        
        for char in word:
            index = ord(char) - ord('a')
            prod *= primes[index]
            
        return prod
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #   Time:   O(kN) -- k - avg length of word; N - number of words
        #   Space:  O(N) -- HashMap

        #   prime number corresponding to each lowercase character
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        
        prodsAnagsMap = {}
        
        #   for each word, calculate prime product which would be the key in the HashMap
        for word in strs:
            
            product = self.__getPrimeProduct(word, primes)
            
            if (product in prodsAnagsMap):
                prodsAnagsMap[product].append(word)
            else:
                prodsAnagsMap[product] = [word]
        
        #   append each list corresponding to a product in the HashMap, to the final result.
        finalResult = []
        for prod in prodsAnagsMap:
            finalResult.append(prodsAnagsMap[prod])
        return finalResult