class Solution {
    stack<int> s;
public:
    int evalRPN(vector<string>& tokens) {
        for (int i = 0; i < tokens.size(); i++) {
            if (isdigit(tokens[i][0]) || 
                (tokens[i].size() > 1 && tokens[i][0] == '-')) {  
                s.push(stoi(tokens[i]));  
            } else {
               
                int b = s.top();
                s.pop();
                int a = s.top();
                s.pop();
                int result;

                // Perform the operation based on the current token
                if (tokens[i] == "+") {
                    result = a + b;
                } else if (tokens[i] == "-") {
                    result = a - b;
                } else if (tokens[i] == "*") {
                    result = a * b;
                } else if (tokens[i] == "/") {
                    result = a / b;
                }
                
                
                s.push(result);
            }
        }
        return s.top();  
    }
};