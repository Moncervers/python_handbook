while (line := input()):
    if not line.startswith('#'):
        print(line[:(line.index('#') if '#' in line else len(line))])
        if '#' in line:
            print(line[:(line.index('#'))])