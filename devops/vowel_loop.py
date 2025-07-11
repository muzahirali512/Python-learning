text = "yaalimaddad"
vowels = "aeiouAEIOU"
count = 0
for chr in text:
    if chr in vowels:
        count+= 1
print("chr in vowels: ", count)
