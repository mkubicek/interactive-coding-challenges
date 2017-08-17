class MergeSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError("data cannot be None") 
        return self._sort(data)
        pass
    
    def _sort(self, data):
        if len(data) < 2:
            return data
        
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = self._sort(left)
        right = self._sort(right)
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        l, r = 0, 0
        result = []
        
        # iterate both lists and add smallest item to result
        while l <= len(left) - 1 and r <= len(right) - 1:
            if left[l] <= right[r]:
                result.append(left[l])
                l = l + 1
            else:
                result.append(right[r])
                r = r + 1
        result.extend(left[l:])
        result.extend(right[r:])
        
        return result
    
    
# less resource hungry implementation:
class MergeSort2(object):
    def sort(self, data):
        if data is None:
            raise TypeError("data cannot be None")
        return self._sort(data, data[:], 0, len(data) - 1)
    
    # leftStart and rightEnd inclusive
    def _sort(self, data, temp, leftStart, rightEnd):
        if leftStart + 1 > rightEnd:
            return data
        
        leftEnd = (leftStart + rightEnd) // 2
        self._sort(temp, data, leftStart, leftEnd)
        self._sort(temp, data, leftEnd + 1, rightEnd)        
        self._merge(data, temp, leftStart, leftEnd + 1, rightEnd)
        
        return data
    
    def _merge(self, result, toMerge, leftStart, rightStart, rightEnd):
        l, r = leftStart, rightStart
        i = leftStart
        while l < rightStart and r <= rightEnd:
            if toMerge[l] <= toMerge[r]:
                result[i] = toMerge[l]
                l = l + 1
            else:
                result[i] = toMerge[r]
                r = r + 1
            i = i + 1
        if l < rightStart:
            result[i:rightEnd + 1] = toMerge[l:rightStart]
        if r <= rightEnd:
            result[i:rightEnd + 1] = toMerge[r:rightEnd + 1]

a, b = MergeSort(), MergeSort2()           
%timeit a.sort([5, 1, 7, 2, 6, -3, 5, 7, -1])
%timeit b.sort([5, 1, 7, 2, 6, -3, 5, 7, -1])
#%load_ext memory_profiler
#%memit a.sort([5, 1, 7, 2, 6, -3, 5, 7, -1])
#%memit b.sort([5, 1, 7, 2, 6, -3, 5, 7, -1])