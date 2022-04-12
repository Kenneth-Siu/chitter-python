from rat import Rat


alice = Rat("Alice")
bob = Rat("Bob")

test_dm = alice.dm("The cheese stands alone", bob)
test_reply = bob.reply("Blah blah blah", test_dm)

print(alice)