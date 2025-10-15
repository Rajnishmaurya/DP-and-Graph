#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>>adj(n+1);

        for(auto& time: times)
        {
            int u=time[0];
            int v=time[1];
            int w=time[2];
            adj[u].push_back({v,w});
        }

        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>>pq;
        pq.push({0,k});

        vector<int>distance(n+1,INT_MAX);
        distance[k]=0;

        while (!pq.empty())
        {
            int time=pq.top().first;
            int node=pq.top().second;
            pq.pop();

            for(auto& [neighbour,weight]:adj[node])
            {
                if(distance[neighbour]>time+weight)
                {
                    distance[neighbour]=time+weight;
                    pq.push({distance[neighbour],neighbour});
                }
            }
        }

        int ans=*max_element(distance.begin()+1,distance.end());
        return ans==INT_MAX? -1 : ans;
        
    }
};