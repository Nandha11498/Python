print("\tBreak Statement")
name=['nandha','raja','bala']
for n in name:
    print(n)
    if n=="raja":
        break

print("\tBreak after Print Statement\n ")
for n in name:
    if n=="raja":
        print(n)
        break
    