def main():
    try:
        with open('states.txt', 'r') as file:
            states = []
            for line in file:
                states.append(line.strip())
                if len(states) == 4:
                    print('\t'.join(states))
                    states = []
            if states:
                print('\t'.join(states))
        file.close()
    except FileNotFoundError:
        print('File not found.')
