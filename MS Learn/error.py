

# def main():
#     open("/path/to/mars.jpg")



# if __name__ == '__main__':
#     main

# try:
#     open('config.txt')
# except FileNotFoundError:
#     print("Couldnt find the config.txt file")





loaded_config = """# Rocket Ship Configuration File!
fuel_tanks = 4
oxygen_tanks = 3
initial_propulsion_level = 84
$ End of file"""

parsed_config = {}

for line in loaded_config.split('\n'):

    try:
        key, value = line.split('=')

        parsed_config[key] = value

    except ValueError:

        print(f'Unable to parse {line}')

        print(parsed_config)