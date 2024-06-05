class Solution {
public:
    string clearStars(string s) {
        vector<int> positions[26];
        // map<int, bool> deleted;
        vector<bool> deleted(s.size(), false);
        
        for(int i=0; i<s.size(); i++) {
            if(s[i] != '*') {
                positions[s[i]-'a'].push_back(i);
            }
            else {
                for(int j=0; j<26; j++) {
                    if(positions[j].size() > 0) {
                        deleted[positions[j].back()] = true;
                        deleted[i] = true;
                        positions[j].pop_back();
                        break;
                    }
                }
            }
        }
        
        string res="";
        for(int i=0; i<s.size(); i++) {
            if (deleted[i] == false) {
                res.push_back(s[i]);
            }
        }
    return res;
    }
};
