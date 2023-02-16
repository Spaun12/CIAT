def main():
    try:
        with open('states.txt', 'r') as file:
            states = [line.strip() for line in file]
            print_states('Descending List:', sorted(states, reverse=True))
            print_states('Ascending List:', sorted(states))
            file.close()
    except FileNotFoundError:
        print('File not found.')

def print_states(label, states):
    print(label)
    # Pad the states list with empty strings if necessary
    if len(states) % 4 != 0:
        states += [''] * (4 - len(states) % 4)
    for i in range(0, len(states), 4):
        print('{:<23}{:<23}{:<23}{:<23}'.format(*states[i:i+4]))
    print()

main()
