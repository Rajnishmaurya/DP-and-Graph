class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();

        queue<pair<int,int>>q;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==1)
                {
                    q.push({i,j});
                }
            }
        }
        if(q.size()==m*n)
        return -1;

        int dx[]={-1,1,0,0};
        int dy[]={0,0,-1,1};
        int distance=0;
        while(!q.empty())
        {
            int size=q.size();
            for(int i=0;i<size;i++)
            {
                auto temp=q.front();
                q.pop();
                int x=temp.first;
                int y=temp.second;

                for(int j=0;j<4;j++)
                {
                    int nx=x+dx[j];
                    int ny=y+dy[j];
                    if(nx>=0 && nx<n && ny>=0 && ny<m && grid[nx][ny]==0)
                    {
                        grid[nx][ny]=1;
                        q.push({nx,ny});
                    }
                }
            }
            distance++;
        }
        return distance-1;
    }
};