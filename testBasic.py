### testBasic.py
### check out the script method


fileName = "test.py"
print('filename = ',fileName)

nums = [1, 2,3,4,5, 17]

for i in nums:
    print(i)

floatNum = 7.31345

print('first print %10i, %10.3f' % (nums[3], floatNum)) 
print('second print %5d %10o %20x' % (nums[5], nums[5], nums[5]) )

out = open('testResult.txt', 'w')
###inFile = open('C:/Users/user/Downloads/NSS PPE status 072516.csv', 'r')
'''

for line in inFile:
    line = line.strip()   ### strip whitespace
    parts = line.split(',')
    print(line, '*** length of line = ', len(line))
    module = parts[0]
    print(module, parts[1], ' len of parts = ', len(parts), ' <--- try cat')   ### parts[2], parts[3], '<--- try cat')
    if ('%' in parts[1]) and (len(parts) > 2):
       tpStatus = parts[1]
       tbStatus = parts[2]
       q0Passed = int(parts[3])
       q0Executed = int(parts[4])
       if (q0Executed):
           complete = q0Passed/q0Executed
       else:
           complete = 0
       print('passed = %3i, exec = %3d, percent = %3.2f' % (q0Passed, q0Executed, complete))
'''             
print('print 2 file: {:>10s} try different ways {:<10} {:>20}'.format(fileName, nums[1], nums[3]), file=out)
MIN = 3
MAX = 5
print('test=', MIN, 'max=', MAX)
string = 'test='+str(MIN)+',max='+str(MAX)
print(string)
Cities = {'Fremont':'6671/CA/Fremont', 'San_Jose':'17420/CA/San-Jose', 'Milpitas':'12204/CA/Milpitas',
          'Dublin':'5159/CA/Dublin', 'Pleasanton':'14986/CA/Pleasanton'}

print("Fremont = ", Cities.get('Fremont'), Cities.get('Pleasanton'))

import collections
cityList = list(collections.OrderedDict(Cities))

print(cityList)
print(cityList[1], cityList[3])


MIN_PRICE = 700000
MAX_PRICE = 1200000
BED = 4
BATH = 2
MIN_SQFT = 1250
MIN_LOT = 5000

MAX_WORKERS = 12

REDFIN = 'https://www.redfin.com/city/%s/filter/max-price='+str(MAX_PRICE)+',min-beds='+str(BED)+',min-baths='+str(BATH)+',min-sqft='+str(MIN_SQFT)+',min-lot-size='+str(MIN_LOT)

webpage = REDFIN % (Cities.get('Fremont'))

print(webpage)

out.close()
###inFile.close()      
