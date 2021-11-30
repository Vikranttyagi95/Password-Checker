import requests
import hashlib

def request_data(query_str):
    url = "https://api.pwnedpasswords.com/range/" + query_str

    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Oops! There is an error! Status code: {response.status_code}")
    else:
        return response

def get_password_leaks(response, hash_tocheck):
    for hash in response.text.splitlines():
        hash_list = hash.split(':')
        hash = hash_list[0]
        count = hash_list[1]

        if hash == hash_tocheck:
            return count
    return 0

def get_password_breach_count(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, rest_char = sha1_password[:5], sha1_password[5:]
    response = request_data(first_5char)
    return get_password_leaks(response, rest_char)


def main():
    with open('Passwords_to_check.txt', 'r') as file:
        password_file = file.readlines()

        for password in password_file:
            password = password.strip()
            count = get_password_breach_count(password)

            if count:
                print(f"Oops! Your password has been hacked {count} no. of times.")
            else:
                print("Your password is good!")

if __name__ == '__main__':
    main()
