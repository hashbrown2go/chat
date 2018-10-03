def read_file(filename):	
	with open(filename, 'r') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return(lines)
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Abbie':
			person = 'Abbie'
			continue
		elif line == 'Henry':
			person = 'Henry'
			continue
		if person:
			new.append(person + ': ' +  line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
