1.  𝐢 = "𝐆𝐎𝐀𝐓" 𝐓𝐡𝐞 𝐨𝐮𝐭𝐩𝐮𝐭 𝐨𝐟 𝐩𝐫𝐢𝐧𝐭(*𝐢) 𝐢𝐬 ?
Variable i:

i = "GOAT"
i is a string with the value "GOAT".

Using the * Operator in print:

print(*i)
The * operator in this context is known as the unpacking operator. When used in a function call, 
it unpacks the elements of an iterable (like a string) into separate arguments.

Here, i is "GOAT", which is a string. When unpacked, each character of the string is treated as a separate argument to print.

Thus, print(*i) is equivalent to:
print("G", "O", "A", "T")

Default Separator in print:
By default, print separates arguments with a space.

Therefore, the output of print(*i) will be:
G O A T
