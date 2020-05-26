import socket
import threading


def recv(udp_socket):
    #recvfrom
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send(udp_socket, dest_ip, dest_port):
   #send
    while True:
        send_data = input("请输入要发送的数据")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    # create  socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #bind
    udp_socket.bind(("", 9999))


    # peer ip + port
    dest_ip = input("请输入对端IP")
    dest_port = int(input("请输入对端port"))

    #create thread
    t_recv = threading.Thread(target = recv, args = (udp_socket, ))  #recv    udp 是广播的,无连接  不需要对端信息
    t_send = threading.Thread(target = send, args = (udp_socket, dest_ip, dest_port) )
    t_recv.start()
    t_send.start()



if __name__ =='__main__':
    main()
