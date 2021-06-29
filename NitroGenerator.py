import random


import requests


def print_header():
    header = """

 +-------------------------+
 | Discord Nitro Generator |
 +-------------------------+
 
 Note: For Educational Purposes Only
 © ATRS 2021. All Rights Reserved.
 
 
"""
    print(header)


def get_code(nitro_type: str):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u',
                  'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E',
                  'F',
                  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if nitro_type == "Boost":
        return str("".join([random.choice(characters) for char in range(24)]))
    elif nitro_type == "Classic":
        return str("".join([random.choice(characters) for char in range(16)]))


def check_code(nitro_code: str):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        check_url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true"
        status = requests.get(url=check_url, headers=headers).status_code
        if status == 200:
            return "True"
        elif status == 429:
            return "None"
        else:
            return "False"
    except:
        print("Something went wrong while checking urls. Press any key to exit. ")
        input()
        quit()


def get_nitro_type():
    print("Enter what type of Discord Nitro you want to generate: \n\t1. Boost\n\t2. Classic")
    user_response = input("> ")
    if user_response.replace(" ", "").strip().lower() == "boost" or user_response.replace(" ",
                                                                                          "").strip().lower() == "1":
        return "Boost"
    elif user_response.replace(" ", "").strip().lower() == "classic" or user_response.replace(" ",
                                                                                              "").strip().lower() == "2":
        return "Classic"
    else:
        print("Not a valid input. Press any key to exit. ")
        input()
        quit()


print_header()
user_nitro_type = get_nitro_type()
print("Enter the number of Nitro Codes you want: ")
amount = int(input("> "))
valid_codes = 0
invalid_codes = 0
unchecked_codes = 0
print()
print()
f = open("All_Nitro_Codes.txt", "w", encoding='utf-8')
for i in range(amount):
    user_nitro_code = get_code(nitro_type=user_nitro_type)
    validity = check_code(nitro_code=user_nitro_code)
    if validity == "True":
        display = f"Valid.                   | https://discord.com/gifts/{user_nitro_code}"
        valid_codes += 1
        print(display)
        f.writelines(display + "\n")
    elif validity == "False":
        display = f"Invalid.                 | https://discord.com/gifts/{user_nitro_code}"
        invalid_codes += 1
        print(display)
        f.writelines(display + "\n")
    elif validity == "None":
        display = f"Unchecked. Rate limited. | https://discord.com/gifts/{user_nitro_code}"
        unchecked_codes += 1
        print(display)
        f.writelines(display + "\n")
print("\n\nSuccessfully generated Nitro Codes. ")
print("Valid Nitro Codes:     " + str(valid_codes))
print("Invalid Nitro Codes:   " + str(invalid_codes))
print("Unchecked Nitro Codes: " + str(unchecked_codes))
print("\nEnter any key to exit.")
input()
quit()
