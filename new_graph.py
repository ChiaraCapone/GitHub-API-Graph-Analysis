from login import client,nx

USER = 'LcicC'
REPO = 'Simple-Calculus-in-Haskell-with-typechecker-and-parser'
user = client.get_user(USER)
repo = user.get_repo(REPO)

g = nx.DiGraph()
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)
nx.write_gpickle(g,"my_graph.gpickle.1")