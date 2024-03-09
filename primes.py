def check_prime(n):
    if n < 2 :
      print(f"check_prime({n}) = Please input positive integer and more than 1 !")
    else :
      prime = True
        #syarat bilangan prima
      for i in range (2,int(n**0.5)+1):
        if n % i == 0 :
          prime = False
          break
      if prime:
        print(f"check_prime({n}) =  {n} is prime")
      else:
        print(f"check_prime({n}) =  {n} is not prime")

#input nilai, bisa lebih dari satu
arr_value = [0,1,2,3,4,5,6,9,10,6]

for n in arr_value:
    check_prime(n)
