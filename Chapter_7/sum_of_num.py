#funtion for finding sum of numbers from start to end
def sum(start,end):
    i=start
    sum=0
    while i<=end:
        sum+=i
        i+=1
    print(f"Sum of number from {start} to {end} = {sum}")
        
#Main function
start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
sum(start,end)