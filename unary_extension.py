from bf_interpreter import BFCompiler

conv_dic = {"000": ">",
            "001": "<",
            "010": "+",
            "011": "-",
            "100": ".",
            "101": ",",
            "110": "[",
            "111": "]",}

def convert_unary_to_bf(source_code):
    # source_code should be a string or base-10 representation of the program

    if type(source_code) == str:
        source_code = len(source_code)

    bin_rep = bin(source_code)[2:]
    assert (len(bin_rep) - 1) % 3 == 0
    bin_rep = bin_rep[1:]
    bf_rep = ""
    for i in range(len(bin_rep)//3):
        next_char = bin_rep[3*i:3*i+3]
        bf_rep = bf_rep + conv_dic[next_char]
    bfc = BFCompiler()
    bfc.parseBF(bf_rep)

if __name__ == "__main__":
    code = 239234107117088762456728667968602154633390994619022073954825877681363348343524058579165785448174718768772358485472231582844556848101441556
    convert_unary_to_bf(code)
    
