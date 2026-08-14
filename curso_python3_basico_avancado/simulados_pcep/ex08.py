# What is the expected output of the following code ?

computers_RAM = {"server1": 12,"server2":16,"server3":24}

for computer in computers_RAM.values():
    print(str(computer)[0], end="")
