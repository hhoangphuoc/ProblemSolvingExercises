class Solution:

    #---------------------------------------#
    # DFS backtracking & recursive solution:#
    #---------------------------------------#
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # create a hashmap to store numbers corresponding to it letter:
        dictionary = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        ans = []
        self.dfs(dictionary,digits,"",ans)
        return ans
    
    def dfs(self,dictionary,digits,path,ans):
        if not digits:
            ans.append(path)
            return
        for char in dictionary[digits[0]]:
             self.dfs(dictionary, digits[1:], path+char, ans)