#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<vector<int>> colorGrid(int n, int m, vector<vector<int>> &sources) {

    vector<vector<int>> grid(n, vector<int>(m, 0));
    queue<pair<int, int>> q;

    for (auto &s : sources) {
      int r = s[0], c = s[1], color = s[2];
      grid[r][c] = color;
      q.push({r, c});
    }

    vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    while (!q.empty()) {

      unordered_map<long long, int> proposals;

      int sz = q.size();

      for (int i = 0; i < sz; i++) {

        auto [r, c] = q.front();
        q.pop();

        int color = grid[r][c];

        for (auto &d : dirs) {
          int nr = r + d.first;
          int nc = c + d.second;

          if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == 0) {

            long long key = 1LL * nr * m + nc;

            if (proposals.find(key) == proposals.end()) {
              proposals[key] = color;
            } else {
              proposals[key] = max(proposals[key], color);
            }
          }
        }
      }

      for (auto &it : proposals) {
        long long key = it.first;
        int color = it.second;

        int r = key / m;
        int c = key % m;

        grid[r][c] = color;
        q.push({r, c});
      }
    }

    return grid;
  }
};