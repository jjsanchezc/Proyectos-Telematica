import socket
import sys
from _thread import *
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('parser.ini')

cache={}

def main():
	global listen_port, buffer_size, max_conn
	it=0
	try:
		listen_port=int(config["port"])
		max_conn=int(config['max_conn'])
		buffer_size=int(config['buffer_size'])
		ttl=int(config['ttl'])
	except KeyboardInterrupt:
		sys.exit(0)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('', listen_port))
		s.listen(max_conn)
		print('[*] Init socket... Done.')
		print('[*] socket binded successfully...')
		print('[*] Server started successfully [{}]'.format(listen_port))
		
	except Exception as e:
		print(e)
		sys.exit(2)

	while True:
		try:
			conn, addr = s.accept()
			#print(f'conn= {conn}, \naddr= {addr}', conn, addr)
			data = conn.recv(buffer_size)
			#ACA VA EL chache_server()
			#deco_data=conn.recv(1024).decode()
			header=data.split(b'\n')[0]
			#header=headers[0].split()
			curr_time = time.mktime(time.gmtime())
			if header in cache and abs(cache[header][1]-curr_time) <= ttl:
				cache_server(header, conn, addr)
			else:
				ip_server_list=[config['ip_server1'], config['ip_server2'], config['ip_server3']]
			# Round Robin
				print('EMPIEZA EL ROUND ROBIN')
				if it>=len(ip_server_list):
					it=0
				webserver = ip_server_list[it]
				it+=1
				start_new_thread(proxy_server,(webserver, listen_port, conn, data, addr, header))

		except KeyboardInterrupt:
			s.close()
			print('\n[*] Shutting down...')
			sys.exit(1)
   
def cache_server(header, conn, addr):
    '''
    implentación caché
    se verifica en el diccionario si la llave(header) ya existe, es decir,
    ya se ha hecho ese request, en caso de que si, se verifica el time del request en el dic.
    key --> header
    content --> tupla(contenido, time)
    TTL --> now-time, si now-time > TTL:
			hace request, se envía request proxy_server
			crea la nueva copia en el caché
		else:
			se envía lo que hay en caché
    '''
    resp = cache[header][0]
    conn.send(resp)
    print(f'[*] Request done. Cache response to => {addr[0]}\n{resp}')




def proxy_server(webserver, port, conn, data, addr, header):
	print('empieza el proxy server')
	try:
		print(data)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#round
		s.connect((webserver, port))
		#Aca debe de guardar el valor en el cache (TOCA VER QUE PONEMOS DESPUES)
		print('se conectó a ',webserver)
		s.send(data)
		print('se envio la data')
		while True:
			reply = s.recv(buffer_size)

			if len(reply) > 0:
				conn.send(reply)
				dar = float(len(reply))
				dar = float(dar/1024)
				dar = '{}.3s'.format(dar)
				print('[*] Request done: {} => {} <= {}'.format(addr[0], 
				dar, webserver))
				print(reply)
				new_time = time.mktime(time.gmtime())
				cache[header] = (reply, new_time)
			else:
				break

		s.close()

		conn.close()
	except OSError as e:
		print(e)
		s.close()
		conn.close()
		sys.exit(1)

if __name__ == '__main__':
	main()