import hashlib


def crack_sha1_hash(hash, use_salts=False):
    # Load the top 10,000 passwords
    with open("top-10000-passwords.txt", "r") as file:
        passwords = [line.strip() for line in file.readlines()]

    # If salts are being used
    if use_salts:
        with open("known-salts.txt", "r") as file:
            salts = [line.strip() for line in file.readlines()]

        # Try cracking the hash with salts
        for password in passwords:
            for salt in salts:
                # Prepend salt
                salted_password_pre = salt + password
                salted_hash_pre = hashlib.sha1(salted_password_pre.encode()).hexdigest()

                if salted_hash_pre == hash:
                    return password

                # Append salt
                salted_password_post = password + salt
                salted_hash_post = hashlib.sha1(salted_password_post.encode()).hexdigest()

                if salted_hash_post == hash:
                    return password
    else:
        # Try cracking the hash without salts
        for password in passwords:
            password_hash = hashlib.sha1(password.encode()).hexdigest()
            if password_hash == hash:
                return password

    # If the password is not found in the database
    return "PASSWORD NOT IN DATABASE"
