# Runtime : 48 ms
# Memory Usage : 7.7 MB
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> m(n, vector<bool>(n, false));
        int count = 0;
        for(int i = 0; i < n; i++) {
            m[i][i] = true;
            count++;
            if(i+1 < n && s[i] == s[i+1]) {
                m[i][i+1] = true;
                count++;
            }
        }
        for(int i = n - 2; i >= 0; i--) {
            for(int j = i + 2; j < n; j++) {
                if(m[i + 1][j - 1] && s[i] == s[j]) {
                    m[i][j] = true;
                    count++;
                }
            } 
        }
        return count;
    }
};
