def read_input():
    choice = input()
    if ("I" in choice) or ("i" in choice):
      text = input()
      line = input()
      #print(text,line)
      return (text.rstrip(), line.rstrip())

    if ("F" in choice) or ("f" in choice):
      name = "tests/06"#+input()
      with open(name) as file:
        text = file.readline();
        line = file.readline();
        #print(text,line)
      return (text.rstrip(), line.rstrip())
    
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(output)

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    b = 25
    q = 222
    len_pat = len(pattern)
    len_txt = len(text)
    m=1
    k1=0
    k2=0
    result = ""
    for i in range(1,len_pat):
      m=(m*b)%q
    for i in range(len_pat):
      k1=(b*k1+ord(pattern[i]))%q
      k2=(b*k2+ord(text[i]))%q

    for i in range (1+len_txt-len_pat):
      if k1==k2:
        for j in range(len_pat):
          if text[i+j]!=pattern[j]:
            break

        j=j+1
        if j==len_pat:
          result=result+str(i)+" "
          

      if i<len_txt-len_pat:
        k2=(b*(k2-ord(text[i])*m) + ord(text[i+len_pat]))%q
        if k2<0:
          k2=k2+q
        

    
    # and return an iterable variable
    return result.rstrip()


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
