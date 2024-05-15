from icmplib import traceroute

hops = traceroute('1.1.1.1')

print('Distance/TTL    Address    Average round-trip time')
last_distance = 0

for hop in hops:
    if last_distance + 1 != hop.distance:
        print('Some gateways are not responding')

    print(f'{hop.distance}    {hop.address}    {hop.avg_rtt} ms')

    last_distance = hop.distance
