print("Enter 'x' for exit.");
string1=input("enter first string to swap:");
if(string1=='x'):
exit()
string2=input("enter second string to swap:");
print("\nBoth string before swap:");
print("first string=",string1);
print("second string=",string2);
temp=string1;
string1=string2;
string2=temp;
print("\nBoth string after swap:");
print("first string=",string1);
print("second string=",string2);




