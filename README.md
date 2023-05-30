# SecretSanta
This is a purpose-built script to generate Secret Santa Assignments for a group. It checks that no-one is shopping for themselves, and as output, populates the results folder with .txt files in the following format:

- Name = person buying gift
- Content = person receiving gift

So if Taylor Swift was chosen to buy a gift for Uncle Mark, her file would be called "Taylor Swift.txt" and the contents would be "Uncle Mark." This way you can send Taylor Swift her own file without checking it, so you stay in the dark!

## How to Use
1. Update `names.txt` with the names of your group (on separate lines, like the example).
2. Remove the existing names (unless you want someone to buy a gift for The Late Queen Elizabeth).
3. Run the script (however you usually run python - if you're new to python [this web page](https://realpython.com/run-python-scripts/) may be able to help).
4. Check if you like who you have. If not, repeat from step 3.
5. Send people their `.txt` files and tell everyone it was a fair process.
6. Delete the `.txt` files so you don't get tempted to snoop.
