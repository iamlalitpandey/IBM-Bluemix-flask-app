# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def Welcome():
	print results
	return 'This is test'
	#return app.send_static_file('index.html')

	
@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!oooooooooooooooooooooonew'

#port = os.getenv('PORT', '8080')
port = int(os.getenv('VCAP_APP_PORT', '5000'))

if __name__ == "__main__":
	import json
	from watson_developer_cloud import RetrieveAndRankV1


	retrieve_and_rank = RetrieveAndRankV1(
		username='fd3935a6-48b0-483f-9c38-4fff2aa09472',
		password='ZuidU7Pg2Pxn')

	# Solr clusters

	solr_clusters = retrieve_and_rank.list_solr_clusters()
	print(json.dumps(solr_clusters, indent=2))

	# created_cluster = retrieve_and_rank.create_solr_cluster(cluster_name='Test Cluster', cluster_size='1')
	# print(json.dumps(created_cluster, indent=2))

	# Replace with your own solr_cluster_id
	solr_cluster_id = 'sc264f32f5_8d7d_4da4_951b_49709a857a38'

	status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
	print(json.dumps(status, indent=2))

	# Solr cluster config
	# with open('../resources/solr_config.zip', 'rb') as config:
	#     config_status = retrieve_and_rank.create_config(solr_cluster_id, 'test-config', config)
	#     print(json.dumps(config_status, indent=2))

	# deleted_response = retrieve_and_rank.delete_config(solr_cluster_id, 'test-config')
	# print(json.dumps(deleted_response, indent=2))

	configs = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
	print(json.dumps(configs, indent=2))

	# collection = retrieve_and_rank.create_collection(solr_cluster_id, 'test-collection', 'test-config')
	# print(json.dumps(collection, indent=2))

	if (len(configs['solr_configs']) > 0):
		collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
		print(json.dumps(collections, indent=2))

		pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, 'test-collection')
		results = pysolr_client.search('what is the basic mechanism of the transonic aileron buzz')

	app.run(host='0.0.0.0',port=port)
