print("\t\t\t\t**************************************\n  "
      "\t\t\t\t**************************************\n "
      "\t\t\t\t**********                   *********\n"
      "\t\t\t\t*****************   ******************\n  "
      "\t\t\t\t*****************   ******************\n  "
      "\t\t\t\t*****************   ******************\n  "
      "\t\t\t\t****   **********   ******************\n  "
      "\t\t\t\t****   **********   ******************\n  "
      "\t\t\t\t****                ******************\n  "
      "\t\t\t\t**************************************\n  "
      "\t\t\t\t**************************************\n  ")

def menu():
    print("------------------MENU------------------")
    print("1.Encrypting(DISGUISE) a data.\n2.Decrypting(UNDRESS) a data.\n3.EXIT")
    ch=int(input("select(1 , 2 or 3):"))
    if ch==1:

        def encode():
            print("\nLevel of Encryption\n1.LOW\n2.INTERMEDIATE\n3.HIGH\n4.Main menu")
            chl=int(input("select(1,2,3):"))
            if chl==1:
                print("-------------------LOW LEVEL ENCRYPTION-------------------\n")
                a = input("Enter the data:")
                sol1 = a[::-1]
                print("\nENCRYPTED DATA:")
                print(sol1)
                print("\n\n************************************END*******************************************")
                encode()
            elif chl==2:
                print("-------------------MID LEVEL ENCRYPTION-------------------\n")
                print("Enter the data:")
                a=input()
                ctr={'a':'q','s':'w','d':'e','f':'r','g':'t','h':'y','j':'u','k':'i','l':'o','p':'l','o':'k','i':'j','u':'h','y':'g',
                 't':'f','r':'d','e':'s','w':'a','q':'m','z':'n','x':'b','c':'v','v':'c','b':'x','n':'z','m':'0'}
                b=a.translate(str.maketrans(ctr))
                print("ENCRYPTED DATA:")
                print(b)
                print("\n\n********************************************END************************************")
                encode()
            elif chl==3:
                print("-------------------HIGH LEVEL ENCRYPTION-------------------\n")
                print("Enter the data(lowercase):")
                a = input()
                print("Create a privacy key(enter random number):")
                q = int(input())
                rend = {'a': q + 1, 's': q + 2, 'd': q + 3, 'f': q + 4, 'g': q + 5, 'h': q + 6, 'j': q + 7, 'k': q + 8,
                        'l': q + 9, 'q': q + 10, 'w': q + 11, 'e': q + 12, 'r': q + 13, 't': q + 14, 'y': q + 15, 'u': q + 16,
                        'i': q + 17, 'o': q + 18, 'p': q + 19, 'z': q + 20, 'x': q + 21, 'c': q + 22, 'v': q + 23, 'b': q + 24,
                        'n': q + 25, 'm': q + 26
                        }
                b = a.translate(str.maketrans(rend))
                print("ENCRYPTED DATA:")
                print(b)
                print("\n\n***************************END****************************")
                encode()
            elif chl==4:
                menu()
            else:
                print("Invalid choice select level of encryption 1,2 or 3")
                encode()
        encode()
    elif ch==2:
            def decode():
                print("\nLEVEL OF DECRYPTION\n1.Low level\n2.Mid level\n3.High level(require privacy key)\n4.Main menu")
                chd=int(input("select(1,2,3):"))
                if chd==1:
                    print("---------Low-level Decrypting-------------")
                    print("Enter the scrambled data:")
                    rev=input()
                    revs=rev[::-1]
                    print("DECRYPTED DATA:")
                    print(revs)
                    print("*********************END***********************")
                    decode()
                elif chd==2:
                    print("---------Mid-level Decryption-------------")
                    decodetwo=input("Enter the scrambled data:")

                    dtr = {'q': 'a', 'w': 's', 'e': 'd', 'r': 'f', 't': 'g', 'y': 'h', 'u': 'j', 'i': 'k', 'o': 'l', 'k': 'o',
                           'l': 'k', 'j': 'i', 'h': 'u', 'g': 'y', 'f': 't',
                           'd': 'r', 's': 'e', 'a': 'w', 'm': 'q', 'n': 'z', 'b': 'x', 'v': 'c', 'c': 'v', 'x': 'b', 'z': 'n',
                           '0': 'm'}
                    middecode= decodetwo.translate(str.maketrans(dtr))
                    print("DECRYPTED DATA:")
                    print(middecode)
                    print("************************END**********************")
                    decode()
                elif chd==3:
                    print("---------High-level Decryption-------------")
                    decodethree=input("Enter the Encrytped data:")

                    r = int(input("Enter The private key:"))
                    rdend = {r + 1: 'a', r + 2: 's', r + 3: 'd', r + 4: 'f', r + 5: 'g', r + 6: 'h', r + 7: 'j', r + 8: 'k',
                             r + 9: 'l', r + 10: 'q', r + 11: 'w', r + 12: 'e', r + 13: 'r', r + 14: 't', r + 15: 'y', r + 16: 'u',
                             r + 17: 'i', r + 18: 'o',
                             r + 19: 'p', r + 20: 'z', r + 21: 'x', r + 22: 'c', r + 23: 'v', r + 24: 'b', r + 25: 'n', r + 26: 'm'
                             }
                    highdecode = decodethree.translate(str.maketrans(rdend))
                    print("DECRYPTED DATA:")
                    print(highdecode)
                    print("******************************END**************************")
                    decode()
                elif chd==4:
                    menu()
                else:
                    print("Invalid choice select which level of decryption 1,2 or 3 ")
                    decode()
            decode()
    elif ch==3:
        exit()
    else:
        print("Invalid choice please select 1 or 2")
        menu()
menu()