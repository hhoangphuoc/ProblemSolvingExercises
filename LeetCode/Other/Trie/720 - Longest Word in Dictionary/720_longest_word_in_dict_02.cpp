
class Solution {
    void dfs(int node, string so_far, string& answer,const vector<vector<int>>& nxt, const vector<bool>& is_terminal){
        if(so_far.length() > answer.length()){
            answer = so_far; // choosing lexicalgraphically word.
        }
        for(int c = 0; c < 26; c++){
            int tmp = nxt[node][c]; //temporary node.
            if(nxt[node][c] != 0 && is_terminal[nxt[node][c]]){
                so_far += char('a' + c);
                dfs(tmp, so_far, answer, nxt, is_terminal);
                so_far.pop_back();
            }
        }
    }
public:
    string longestWord(vector<string>& words) {
        vector<vector<int>> nxt(1, vector<int>(26));//int nxt[1][26]
        vector<bool> is_terminal{false};// bool is_terminal[1]
        
        //implementing the trie:
        int N = 0;
        for(string s : words){
            //node starting from the root:
            int node = 0;
            for (char c: s) {
                //create new child node if child node doesn't exist:
                if (nxt[node][c -'a'] == 0){
                    nxt.push_back(vector<int>(26));
                    is_terminal.push_back(false);
                    nxt[node][c -'a'] = ++N;
                }
                
                node = nxt[node][c - 'a']; // keep moving the node forward
            }
            is_terminal[node] = true;
        }
        string so_far ="";
        string answer = "";
        //run dfs from root
        dfs(0,so_far, answer, nxt, is_terminal);
        return answer;
    }
};