import socket
import sys
from _thread import *

def main():
	global listen_port, buffer_size, max_conn
	try:
		listen_port = int(input('litening port: '))
	except KeyboardInterrupt:
		sys.exit(0)

	max_conn = 5
	buffer_size = 8192

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
			data = conn.recv(buffer_size)
			start_new_thread(conn_string, (conn, data, addr))
		except KeyboardInterrupt:
			s.close()
			print('\n[*] Shutting down...')
			sys.exit(1)


def conn_string(conn, data, addr):
	try:
		# print(data)
		first_line = data.split(b'\n')[0]
		url = first_line.split()[1]		

		http_pos = url.find(b'://')
		if http_pos == -1:
			temp = url
		else:
			temp = url[(http_pos + 3):]

		port_pos = temp.find(b':')

		webserver_pos = temp.find(b'/')

		if webserver_pos == -1:
			webserver_pos = len(temp)
		webserver = ""
		port = -1

		if port_pos == -1 or webserver_pos < port_pos:
			port = 80
			webserver = temp[:webserver_pos]
		else:
			port = int(temp[(port_pos + 1):][:webserver_pos - port_pos - 1])
			webserver = temp[:port_pos]

		print(webserver)
		proxy_server(webserver, port, conn, data, addr)
	except Exception:
		pass


def proxy_server(webserver, port, conn, data, addr):
	try:
		# print(data)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
				dar, socket.gethostbyname(webserver)))
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