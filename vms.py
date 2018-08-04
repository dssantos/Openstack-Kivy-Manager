#coding: utf-8

import requests, json

def get(host_id, headers): # O método deve receber um host_id e o headers(token)
	
	try:
		r = requests.get('http://controller:8774/v2.1/os-hypervisors/%s'%host_id, headers=headers)
		vms = json.loads(r.content)
		vms = vms[u'hypervisor']["running_vms"]

	except:
		vms = 0  # Caso o id não seja localizado na consulta, o comando resultará erro, então vms será zero

	return vms # Retorna a quantidade de vms em execução no host