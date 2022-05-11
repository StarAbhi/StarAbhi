#define crrent number 
crnt=1 
#define previous number  
pre=1
#define next number
next=0
count=1 
print("First 20 Fibonacci sequence :-")
while(count<=20):
    print(pre,end=" ")
    next = crnt
    crnt = pre + crnt
    pre = next
    count +=1
