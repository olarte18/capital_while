
#input 


c= int(input("digite el capital: "))

#procesing
cf=c*2
m=0

while c<= cf:
    c=c+(0.05*c)
    m=m+1

#output
print("los meses que tarda en tener el doble del capital es: "+ str(m))