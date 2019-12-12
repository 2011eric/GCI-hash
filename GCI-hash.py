from argparse import ArgumentParser
import hashlib
import os

crack_data = {}
def process_command():
    help_text = """ 
    This program supports:
    md5
    sha1
    sha224
    sha256
    sha384
    sha512
    """
    parser = ArgumentParser(description=help_text)
    parser.add_argument('--mode', '-m', type = str, required = True,help = "'-m hash' or '-m crack'")
    parser.add_argument('--hashtype', '-t', type = str, required= False, help = "type of hash")
    parser.add_argument('--string', '-s', type = str, required= True,help = "the input string")
    return parser.parse_args()
def hash(hashtype,string):
    hashobj = {
        "md5":lambda : hashlib.md5() ,
        "sha1":lambda : hashlib.sha1(),
        "sha224":lambda : hashlib.sha224(),
        "sha256":lambda : hashlib.sha256(),
        "sha384":lambda : hashlib.sha384(),
        "sha512":lambda : hashlib.sha512(),
    }
    if hashtype in hashobj:
        m = hashobj[hashtype]()
        m.update(string.encode("utf-8"))
        return m.hexdigest()
    else:
        return None
def readfile(path):
    with open(path,"r") as fp:
        for line in fp.readlines():
            (string,hashed) = line.split()
            crack_data[hashed]=string
        
       
args = process_command()
if args.mode == "hash":
    if args.hashtype == None:
        print("You must enter type of hash!")
    else:
        result = hash(args.hashtype,args.string)
        if result == None:
            print("Wrong type of hash!")
        else:
            print("Mode: hash")
            print("HashType: "+args.hashtype)
            print("Result: "+result)
elif args.mode =="crack":
    path = input("Please enter the path of wordlist:")
    readfile(path)
    if args.string in crack_data:
        print("hash cracked:"+crack_data[args.string])
    else:
        print("hash not found!")
else:
    print("Wrong mode!")