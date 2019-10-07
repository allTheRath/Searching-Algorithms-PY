
#linear search loops through the list and compares each element to the search number and returnes index of that number ele returns none
#o(N)
def LinearSearch(numberarray, searchnumber) : 
  if type(numberarray) != type([1,2]) or len(numberarray) == 0:
    return None
  index = 0
  for value in numberarray:
    if value == searchnumber :    
      return index
    index += 1
  return None

#Binary search is done on sorted array. it divides interval lenth into half and based on value located at middle of interval 
# divides again on left or right.
#o(log(N))
def BinarySearch(numberarray, searchnumber) : 
  if type(numberarray) != type([1,2]) or len(numberarray) == 0:
   return None
  indexLength = len(numberarray)
  start = 0
  for value in range(start, indexLength):
    if numberarray[value] == searchnumber :      
      return value
    elif  numberarray[value] > searchnumber :
      #dont change start
      #end changes to half length
      indexLength = (int)(indexLength / 2)
    elif  numberarray[value] < searchnumber :
      #change start to dividor
      # dont change end
      start = (int)(indexLength / 2)
    elif indexLength - start == 1 : 
      if numberarray[indexLength] == searchnumber : return indexLength
      #if searching value is not found till listlength - 1 then chack for las value. 


# Jump search is done on sorted array.
# Jump search tries to find the perfect interval for given searchvalu in given list.
#o(root(N))
def JumpSearch(numberarray, searchnumber) :
  #type comparison
  if type(numberarray) != type([1,2]) or len(numberarray) == 0:
    return None
  incrementor = (int)(len(numberarray) / 10)
  start = 0
  end = len(numberarray)
  for value in range(start, end) :
    end += incrementor
    if numberarray[value] == searchnumber :
      return value
    elif numberarray[value] < searchnumber and numberarray[value + incrementor] > searchnumber :
      start = value
      end = value + incrementor
      break
    else : 
      start += incrementor  
  for value in range(start, end) :
    if numberarray[value] == searchnumber :
      return value 
  return None


#Interpolation search is done on sorted array of uniformaly distributed values.. 
#// The idea of formula is to return higher value of pos
#// when element to be searched is closer to arr[hi]. And
#// smaller value when closer to arr[lo]
#pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
# less then o(log(N))
def InterpolationSearch(numberarray, searchnumber) :
  if type(numberarray) != type([1,2]) or len(numberarray) == 0:
    return None
  lo = 0
  hi = len(numberarray) - 1
  if searchnumber > numberarray[hi] or searchnumber < numberarray[lo] :
    return None
  pos = lo + (int)((searchnumber - numberarray[lo]) * (hi - lo) / (numberarray[hi] - numberarray[lo]))
  if numberarray[pos] == searchnumber :
    return pos
  elif numberarray[pos] < searchnumber :
    lo = pos
  elif numberarray[pos] > searchnumber :
    hi = pos
  flag = True
  while flag == True :
    pos = lo + (int)((searchnumber - numberarray[lo]) * (hi - lo) / (numberarray[hi] - numberarray[lo]))
    if numberarray[pos] == searchnumber :
      return pos
    elif numberarray[pos] < searchnumber :
      lo = pos
    elif numberarray[pos] > searchnumber :
      hi = pos
    if hi - lo == 1 :
      flag = False
    if numberarray[hi] == searchnumber : return hi
    elif numberarray[lo] == searchnumber : return lo
    lo+=1
  else : return None

#Exponential search algorithm is for sorted array.
# It searches for values greater then search value . If it found one then do binary search between currentindex / 2 and current index.
# The incrementor is exponential in terms like multiple of 2. so currentIndex / 2 will be seen before.

def ExponentialSearch(numberarray, searchnumber) :
  if type(numberarray) != type([1,2]) or len(numberarray) == 0:
    return None
  start = 0
  end = len(numberarray) - 1
  if numberarray[start] == searchnumber : return start
  if numberarray[end] == searchnumber : return end
  start = 2
  while start <= end :
    if start > end :
      break
    if numberarray[start] == searchnumber : return start
    if numberarray[start] > searchnumber and numberarray[(int)(start / 2)] <= searchnumber: 
      break
    start *= 2  
  if start > end : start = end
  for value in range((int)(start / 2), start) :
    if numberarray[value] == searchnumber :
      return value
  return None

cache = {}
def Fibonaci(num) :
  
  if num in cache :
    return cache[num]
  if num == 0  : return 0
  elif num == 1 or num == 2:
    result =  1
  else :
    result =  Fibonaci(num - 2) + Fibonaci(num - 1)
  
  cache[num] = result
  return result

#Find a larger or same fibonacii number that match with given array length
def FibonaciSearch(numberarray, searchnumber) :
  if type(numberarray) != type([1,2]) or len(numberarray) == 0:
    return None
  if numberarray[0] == searchnumber : 
    return 0
  length = len(numberarray) 
  if numberarray[length - 1] == searchnumber :
    return length - 1
  #Checking for edge cases and one type check.
  
  flag = True
  i = 1
  num = 1
  while flag :
    num = Fibonaci(i)
    if num > length :
      flag = False
      break
    else : 
      i+=1
  #print(num)
  #The smallest possible fibonaci number that is greater then or equal to array length.
  offset = -1
  fbM = num
  fbm1 = cache[i-1]
  fbm2 = cache[i-2]
  #print(fbM,fbm1,fbm2)
  while fbM > 1 :
    i = min(offset + fbm2, length - 1)

    if numberarray[i] < searchnumber :
      fbM = fbm1
      fbm1 = fbm2
      fbm2 = fbM - fbm1
      offset = i
    elif numberarray[i] > searchnumber :
      fbM = fbm2
      fbm1 = fbm1 - fbm2
      fbm2 = fbM - fbm1
    else : return i

    if numberarray[offset + 1] == searchnumber :
      return offset + 1

  return None


