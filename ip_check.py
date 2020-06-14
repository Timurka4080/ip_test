ip, mask = (input('Введите IP-сети в формате: 10.1.1.0/24: ')).split('/')

oct1, oct2, oct3, oct4 = ip.split('.')
bin_ip = f'{int(oct1):08b}{int(oct2):08b}{int(oct3):08b}{int(oct4):08b}'
bin_mask = f'{"1"*int(mask):<032}'
bin_net = bin_ip[:int(mask) - 32] + '0' * (32 - int(mask))

print(f'''
Network:
{int(bin_net[0:8], 2):<8}  {int(bin_net[8:16], 2):<8}  {int(bin_net[16:24], 2):<8}  {int(bin_net[24:], 2):<8}
{bin_net[0:8]}  {bin_net[8:16]}  {bin_net[16:24]}  {bin_net[24:]}''')

print(f'''
Mask:
/{mask}
{int(bin_mask[0:8], 2):<8}  {int(bin_mask[8:16], 2):<8}  {int(bin_mask[16:24], 2):<8}  {int(bin_mask[24:], 2):<8}
{bin_mask[0:8]}  {bin_mask[8:16]}  {bin_mask[16:24]}  {bin_mask[24:]}''')
