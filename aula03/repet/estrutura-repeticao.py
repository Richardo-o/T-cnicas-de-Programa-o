names = ["Jimmy", "Rose", "Max", "Nina", "Philip"]

for name in names:
    if len(name) != 4:
        continue
    print(f"Hello,{name}")
    if name == "Nina":
        break
    
print("Done!")

count = 5
while count>0:
    print(count)
    count-=1