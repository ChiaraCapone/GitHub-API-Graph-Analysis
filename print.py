import os
import json
from login import nx
from IPython.display import IFrame
from IPython.core.display import display
from networkx.readwrite import json_graph
# Visualize the social network of all people from the original interest graph.
g = nx.read_gpickle("my_graph.gpickle.1")
d = json_graph.node_link_data(g)
json.dump(d, open('force.json', 'w'))
# A D3 template for displaying the graph data.
viz_file = 'force.html'
# Display the D3 visualization.
display(IFrame(viz_file, '100%', '600px'))