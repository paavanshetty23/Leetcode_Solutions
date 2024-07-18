// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
// •	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;
        vector<int> in_degree(numCourses, 0);
        
        for (const auto& pair : prerequisites) {
            int dest = pair[0], src = pair[1];
            graph[src].push_back(dest);
            in_degree[dest] += 1;
        }
        
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (in_degree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> order;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            order.push_back(node);
            for (int neighbor : graph[node]) {
                in_degree[neighbor] -= 1;
                if (in_degree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        if (order.size() == numCourses) {
            return order;
        } else {
            return {};
        }
    }
};
