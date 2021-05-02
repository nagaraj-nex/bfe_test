import os
os.environ['BFE_SSL_CERT'] = 'ubuntu2004.crt'

from pybfe.client.session import Session
bfe = Session('ubuntu2004')
network_list = bfe.list_networks()
print(network_list)