from github import Github
import networkx as nx
# XXX: Specify your own access token here
ACCESS_TOKEN = '****'
# Specify a username and repository of interest for that user.
client = Github(ACCESS_TOKEN, per_page=100)
