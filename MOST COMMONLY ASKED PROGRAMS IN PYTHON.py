
# coding: utf-8

# In[1]:


#fizzbuzz problem
def fizzbuzz(n):
    result=[]
    for i in range(1,n+1):
        add=''
        if (i%3==0):
            add+='Fuzz'
        if (i%5==0):
            add+='Buzz'
        if (add==''):
            result.append(i)
        else:
            result.append(add)
    return result
print(fizzbuzz(20))


# In[2]:


#Two Sum Problem
#An array and some number S are given. Determine if any two numbers within the array sum to S.
#Order O(n) but uses extra space
def twoSum(arr,S):
    hashTable={}
    for i in range(0,len(arr)):
        sumMinusElement=S-arr[i]
        if (sumMinusElement in hashTable):
            return True
        hashTable[arr[i]]=True
    return False
arr=[1,2,4,5,8,9]
S=2
print(twoSum(arr,S))
arr=[1,2,4,5,8,9]
S=3
print(twoSum(arr,S))


# In[3]:


#Sum of nested array
def sumNested(arr):
    result=0
    for i in range(0,len(arr)):
        if (type(arr[i])!=int):
            result+=sumNested(arr[i])
        else:
            result+=arr[i]
    return result
arr=[1,2,3,[4,5],6,[7,8,9]]
print(sumNested(arr))


# In[4]:


#Angle between the hour and minute hands in a clock
def clockAngle(hour,mins):
    h=0
    h=0.5*(60*h+mins)
    m=6*mins
    angle=abs(h-m)
    if (angle>180):
        return 360-angle
    else:
        return angle
hour=1
mins=5
print(clockAngle(hour,mins))


# In[5]:


#prime number check
import math
def isprime(n):
    if(n<2):
        return False
    if(n==3):
        return True
    for i in range(2,math.ceil(math.sqrt(n))):
        if(n%i==0):
            return False
        else:
            return True
n=3
print(isprime(n))
    


# In[6]:


#Remove characters of a string which are also in an array
def removeChars(arr,string):
    hashTable={}
    for c in arr:
        hashTable[c]=True
    result=''
    for c in string:
        if(c not in hashTable):
            result+=c
    return result
arr=['v','i','m','l','e','s','h']
string='hello dixit'
print(removeChars(arr,string))


# In[7]:


def firstNonrepChar(string):
    hashTable={}
    for c in string:
        if(c not in hashTable):
            hashTable[c]=1
        else:
            hashTable[c]+=1
    for c in string:
        if(hashTable[c]==1):
            return c       
string='vimlesh kumar dixit'
print(firstNonrepChar(string))


# In[8]:


#continuous atleast three vowels in a word of a string
import re
def threeVowels(string):
    arr=string.split()
    count=0
    for word in arr:
        if(re.search(r'[aeiou]{3,}',word)):
            count +=1
    return count
string='iau oia vimlesh kumar dixit aio eua'
print(threeVowels(string))


# In[9]:


def removePairs(string):
    result=''
    i=0
    while(i<len(string)):
        if(i==len(string)-1):
            result +=string[i]
        elif(string[i]!=string[i+1]):
            result+=string[i]
        else:
            i+=1
        i+=1
    return result
string='akkabcdee'
print(removePairs(string))


# In[10]:


#Find majority element in an array
import math
def majorityElement(arr):
    candidate=None
    count=0
    for i in range(0,len(arr)):
        if(candidate is None or count==0):
            candidate=arr[i]
            count=1
        elif(arr[i]==candidate):
            count+=1
        else:
            count-=1
    count=0
    for el in arr:
        if(el==candidate):
            count+=1
        if(count>math.floor(len(arr)/2)):
            return candidate       
arr=[1,1,1,2,2,2,2,2,3]
print(majorityElement(arr))


# In[11]:


#mean, median and mode of an array
def meanMedianMode(arr):
    mean=sum(arr)/float(len(arr))
    arr=sorted(arr)
    median=arr[int(len(arr)/2)]
    mode=None
    hashTable={}
    for i in arr:
        if(i in hashTable):
            hashTable[i]+=1
        else:
            hashTable[i]=1
        if(mode is None or hashTable[i]>mode):
            mode=i
    return {'mean':mean, 'median':median, 'mode':mode}
arr=[1,2,3,4,5,1]

print(meanMedianMode(arr))


# In[12]:


def encodeConsonants(string):
    result=''
    vowels=['a','e','i','o','u']
    for i in string:
        if(i=='z'):
            result+='b'
            break
        elif(i not in vowels and i !=''):
            newCode=ord(i)+1
            if(chr(newCode) in vowels):
                newCode+=1
            result+=chr(newCode)
        else:
            result+=i
    return result
string='vimlesh'
print(encodeConsonants(string))

