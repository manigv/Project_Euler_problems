#c=0
#n=7
#for i in range(1,n+1):
 #       if n%i==0:
  #          print (i)
   #         c=c+1
#print(c)
            #if c==5:
             #   print("There are 5 divisors for 28")




tot=0
c=0

for i in range(1,2000000+1):
        #print(i)
        tot=tot+i
        c=0
        
        #print("For",i,"is:",tot)
        for j in range(1,tot):
                if tot%j==0:
                        
                        c=c+1
                        #print("Factors of",tot,"is",j)
                        if c==500:
                                print("###########",tot,"##########")
                                exit()
       
        
        print("Number factors of",tot,"is",c)
        
        print("\n")
        
                        
