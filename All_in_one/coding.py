def print_full_name(first, last):
    text = 'You just delved into python.' 
    print(f'Hello {first_name} {last_name}! {text}')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
