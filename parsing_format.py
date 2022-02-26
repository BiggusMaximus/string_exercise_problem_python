filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new = []
for i in filenames:
    if i[-2:] == "pp":
        i = i[:-2] + ""
        new.append(i)
    else:
        new.append(i)
print(new)
        
 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]