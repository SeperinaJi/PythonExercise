unconfirmed_users = ['jony', 'seperina', 'alice']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verfying user :" + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users has been verified:")
for user in confirmed_users:
    print(user.title())