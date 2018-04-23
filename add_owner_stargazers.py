from login import client, nx
import sys

g = nx.read_gpickle("my_graph.gpickle.1")

repos = [n for n in g.nodes_iter() if g.node[n]['type'] == 'repo']

for repo in repos:
	owner = client.get_user(g.node[repo]['owner'])
	g.add_node(owner.login + '(user)', type='user')
	g.add_edge(owner.login + '(user)', repo,type='owns')
	my_repo = owner.get_repo(repo[:-6])
	print(repo)
	for sg in my_repo.get_stargazers():
		g.add_node(sg.login + '(user)', type='user')
		g.add_edge(sg.login + '(user)', my_repo.name + '(repo)',type='gazes')
	print(repo[:-6])
	
nx.write_gpickle(g, "my_graph.gpickle.1")