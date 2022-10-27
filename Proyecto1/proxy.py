import socket
import sys
from _thread import *
import configparser as confp

config_prede={
        "port":8080,
        "max_conn": 5,
        "buffer_size": 8192,
        "ttl":180,
        "ip_server": [
            "54.90.229.206",
            "54.174.158.86",
            "34.201.172.25"
        ]
}
def main():
	global listen_port, buffer_size, max_conn
	it=0
	try:
		listen_port=int(config_prede["port"])
		max_conn=int(config_prede['max_conn'])
		buffer_size=int(config_prede['buffer_size'])
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
			ip_server_list=config_prede['ip_server']
			# Round Robin
			print('EMPIEZA EL ROUND ROBIN')
			if it>=len(ip_server_list):
				it=0
			webserver = ip_server_list[it]
			it+=1
			start_new_thread(proxy_server,(webserver, listen_port, conn, data, addr))

		except KeyboardInterrupt:
			s.close()
			print('\n[*] Shutting down...')
			sys.exit(1)

def proxy_server(webserver, port, conn, data, addr):
	print('empieza el proxy server')
	try:
		print(data)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#round
		s.connect((webserver, port))
		print('se conectó',webserver)
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