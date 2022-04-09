import ipaddress

def cal_ip(ip_net):
    try:
        net = ipaddress.ip_network(ip_net, strict=False)
        print('the net ID ： ' + str(net.network_address))
        print('the broadcast address ： ' + str(net.broadcast_address))
        print('host range ： ' + str([x for x in net.hosts()][0]) + ' ~ ' + str([x for x in net.hosts()][-1]))
        print ('subnet mask: ' + str([net.netmask]))
        
    except ValueError:
        print(' your input format is incorrect, please check ！')

if __name__ == '__main__':
    ip_net = input('Please enter IP with the CIDR using this [xxx.xxx.xxx.xxx/cidr] format : ')
    cal_ip(ip_net) 

