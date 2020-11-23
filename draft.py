print("Enter private key of sender")
k1=int(input())
print("Enter private key of Receiver")
k2=int(input())
str =input("Enter your message: ")
print(str) 
b=0
c=0
str1=""
str_list = list(str)
for i in str:
        k=k1^k2
        e=ord(i)^k
        ##print(k,e,chr(e))
        str_list[b]=chr(e)
        b=b+1
        k2=k2+1
        k1=k1+1
str1="".join(str_list)
print("The Encrypted message ")
print(str1)

str1 = str1[::-1]
str2=""
str1_list = list(str1)
for i in str1:
        k2=k2-1
        k1=k1-1
        k=k1^k2
        d=ord(i)^k
       ## print(k,d,chr(d))
        str1_list[c]=chr(d)
        c=c+1
str2="".join(str1_list)
str2 = str2[::-1]
print("The Decrypted Message")
print(str2)