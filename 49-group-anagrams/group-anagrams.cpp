class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramGroups;
        for (string s : strs) {
        string sortedStr = s;         
        sort(sortedStr.begin(), sortedStr.end());  
        
        
        anagramGroups[sortedStr].push_back(s);
    }
    
    
    vector<vector<string>> result;
    for (auto& group : anagramGroups) {
        result.push_back(group.second);
    }
    
    return result; 
    }
};