import socket
import sys
from _thread import *
import configparser as confp

def main():
	global listen_port, buffer_size, max_conn
	it=0
	try:
		config = confp.ConfigParser()
		config.read("parser.ini")
		listen_port=int(config.get('DEFAULT','port'))
		max_conn=int(config.get('DEFAULT','max_conn'))
		buffer_size=int(config.get('DEFAULT','buffer_size'))
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
			ip_server_list=config.get('DEFAULT','ip_server')
			# Round Robin
			webserver = ip_server_list[it%len(ip_server_list)]
			it+=1
			start_new_thread(proxy_server, (webserver, listen_port, conn, data, addr))

		except KeyboardInterrupt:
			s.close()
			print('\n[*] Shutting down...')
			sys.exit(1)

def proxy_server(webserver, port, conn, data, addr):
	try:
		print(data)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#round
		s.connect((webserver, port))
		s.send(data)

		while True:
			reply = s.recv(buffer_size)

			if len(reply) > 0:
				conn.send(reply)

				dar = float(len(reply))
				dar = float(dar/1024)
				dar = '{}.3s'.format(dar)
				print('[*] Request done: {} => {} <= {}'.format(addr[0], 
				dar, webserver))
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