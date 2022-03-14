from werkzeug.security import check_password_hash, generate_password_hash

password = input()
password_hash = generate_password_hash(password)

print(password_hash)

if check_password_hash(password_hash, password):
    print(True)
else:
    print(False)