def load_average(config):
	loadavg=open('/proc/loadavg','r')
	cur_avg=loadavg.read()
	loadavg.close()
	cur_avg=cur_avg.split(' ')[0]
	return cur_avg

def thermal(config):
	cur_temp_file=open(config['temp_file'],'r')
	cur_temp=cur_temp_file.read()
	cur_temp_file.close()
	cur_temp=float(cur_temp)/1000
	return cur_temp

def memory(config):
	cur_memory_file = open('/proc/meminfo','r')
	cur_memory = cur_memory_file.read()
	cur_memory_file.close()
	cur_memory = cur_memory.split('\n')
	mem_total = 0
	mem_free = 0
	mem_cached = 0
	for i in cur_memory:
		mem = i.split(' ')
		if mem[0] == 'MemTotal:':
			mem_total = mem[-2]
		if mem[0] == 'MemFree:':
			mem_free = mem[-2]
		if mem[0] == 'Cached:' and not config.getboolean('ignore_cached'):
			mem_cached = mem[-2]
	mem_used = int(mem_total) - int(mem_free) - int(mem_cached)
	return mem_used/1024
