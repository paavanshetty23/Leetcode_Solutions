class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<int,int> maps;
        unordered_map<int,int> mapt;
        for(int i=0 ; i< s.size();i++){
            char cs= s[i];
            char ct = t[i];

            if(maps.count(cs) && maps[cs]!=ct) return false;
            if(mapt.count(ct) && mapt[ct]!=cs) return false;

            maps[cs]=ct;
            mapt[ct]=cs;

        }
        return true;
    }
};