# ELLA MARIE A. MALLARI
# BSCPE 1-4

# EVEN AND ODD
# open numbers.txt (read), even.txt (append) and odd.txt (append)
with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd: 
    for line in input_file:
        print(line.strip())
        input_num = int(line)
    # if even 
    if input_num % 2 == 0:
    # if odd 
    else: 