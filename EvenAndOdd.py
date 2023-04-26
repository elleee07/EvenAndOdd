# ELLA MARIE A. MALLARI
# BSCPE 1-4

# EVEN AND ODD

# open numbers.txt (read), even.txt (append) and odd.txt (append)
with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd:
    # read it line by line 
    for line in input_file:
        input_num = int(line)
        # if even, 
        if input_num % 2 == 0:
            output_even.write(str(input_num) + "\n")
        # if odd,
        else:
            output_odd.write(str(input_num) + "\n")