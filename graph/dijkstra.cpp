// 假定使用邻接矩阵储存graph
// 在矩阵中对角线都是0，每条边的weight都是1，不可达的为INT_MAX
vector<int>& dijkstra(int source, vector<vector<int>>& graph){
	int  n = graph[0].size();
	int minDist;
	vector<int> dist(n,0);
	vector<int> visited(n,0);
	
	// mark source
	visited[source] = 1;
	
	// init dist
	dist = graph[source];
	
	int neighbor;
	for(int i=0; i<n; i++){	
		// find the nearset neighbor of source
		minDist = INT_MAX;
		for(int j = 0; j < n; j++){
			if(!visited[j] && dist[j] < minDist){
				minDist = dist[j];
				neighbor = j;
			}
		}
		visited[neighbor] = 1;
		
		// update dist
		for(int k = 0; k<n; k++){
			if(graph[neighbor][k] < INT_MAX){
				if(!visited[k] && dist[neighbor] + graph[neighbor][k] < dist[k]){
					dist[k] = dist[neighbor] + graph[neighbor][k];
				}
			}
		}
	}
	/* 
	for(auto elem : dist)cout<<elem<<" ";
	cout<<endl;
	*/
  return dist;
}
