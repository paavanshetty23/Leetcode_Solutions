class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> resvec;
        long long res =1;
        resvec.push_back((int)(res));
        for(int i =0 ; i<rowIndex;i++){
            res*=(rowIndex-i);
            res/=(i+1);

            resvec.push_back((int)(res));
    }
    return resvec;

    }
};
