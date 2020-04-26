filepath = 'modules.txt'
with open(filepath) as fp:
   lines = fp.readlines()
   total = 0
   for line in lines:
       amt = int(line.strip())
       fuel_needed = (amt // 3) -2 
       additional = (fuel_needed // 3) - 2
       while additional > 0 :
           fuel_needed += additional
           additional = (additional // 3) - 2

       total += fuel_needed
   print(total)


       
