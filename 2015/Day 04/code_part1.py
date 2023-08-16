import hashlib

input = 'bgvyzdsv'

num = 0
answer = 'unknown'
while num < 1000000:
    string = input+str(num)
    md5hash = hashlib.md5(string.encode()).hexdigest()
    if md5hash[0:5] == '00000':
        answer = num
        break
    num += 1

print('Answer is: ',answer)