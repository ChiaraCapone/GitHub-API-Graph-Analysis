from login import client,nx
import sys

g = nx.read_gpickle("my_graph.gpickle.1")

repos = [n for n in g.nodes_iter() if g.node[n]['type'] == 'repo']
#repos = [n for n in g.nodes_iter() if g.node[n]['type'] == 'repo']

for rp in repos [:len(repos)]:
	#rps = g.node[repos[i]]
	print(g.node[rp])

reporz = client.get_user(g.node[repos[0]]['owner']).get_repo(repos[0][:-6])
print (repos[0])

reporz = client.get_user(g.node[repos[0]]['owner']).get_repo(repos[0][:-6])
stargazers = [ s for s in reporz.get_stargazers() ]
print(len(stargazers));
print(stargazers[0]);
#	stargazers = repo.get_stargazers(user[:-6])
print (reporz)
	
nx.write_gpickle(g, "my_graph.gpickle.1")