// Link for this problem: 
// https://leetcode.com/problems/longest-word-in-dictionary/

// Approach #1: Brute-Force Solution:

class Solution {
public:
    string longestWord(vector<string>& words) {
        // create dictionary in set, to easily check if word exist.
        set<string> dictionary (words.begin(), words.end());
        set<string> good; //set of all good string, can be create character by character.
        
        //sorted the words by length from shortest to longest.
        sort(words.begin(),words.end(),[&](const string& a, const string& b) {
            return a.length() < b.length();
        }); 
        string answer = "";
             
        //choosing by lexicographical order:
        auto consider = [&](const string& s){
            if(s.length() > answer.length()){
                answer = s;
            }
            else if (s < answer){
                answer = s;
            }
        };
        for (string s : words){
            if((int)s.length() == 1){
                good.insert(s); // a single character will alway a good string.
                consider(s);
                continue;
            }
            string shorten = s;
            shorten.pop_back(); // remove the last character.
            
            // check if 'shorten' is inside the dictionary.
            if(dictionary.count(shorten) && good.count(shorten)){
                consider(s);
                good.insert(s); // if the character of 'shorten' is good, 'shorten' itself is also a good string.
            }
        }
             return answer;
    }
};