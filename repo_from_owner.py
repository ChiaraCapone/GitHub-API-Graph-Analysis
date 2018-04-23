from login import client,nx
import sys

g = nx.read_gpickle("my_graph.gpickle.1")

users = [n for n in g.nodes_iter() if g.node[n]['type'] == 'user']

for user in users:
	u = client.get_user(user[:-6])
	if u.login != '573':
		starred = [n for n in u.get_starred() ][:10]
	#print (u)
	#print(len(starred))
	if len(starred) > 0:
		for starred in u.get_starred() [:10]:
			print (starred.owner.login)
			g.add_node(starred.name + '(repo)', type='repo', lang=starred.language, owner=starred.owner.login)
			g.add_edge(u.login + '(user)', starred.name + '(repo)',type='gazes') #g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)
	
nx.write_gpickle(g, "my_graph.gpickle.1")