# Author: Krems

# insertion sort is faster then merge sort on extremely small sizes
def insertion_sort(a, lhs, rhs):
    if lhs >= rhs:
        return ""
    for i in xrange(1, rhs - lhs):
        tmp = a[lhs + i]
        hole_pos = i + lhs
        while hole_pos > lhs and a[hole_pos - 1] > tmp:
            a[hole_pos] = a[hole_pos - 1]
            hole_pos -= 1
        a[hole_pos] = tmp

# stable merge of a[lhs:rhs] and a[rhs:end]
def merge(a, lhs, rhs, end):
    if lhs >= rhs:
        return ""
    if rhs == end:
        return ""
    tmp = list(a[lhs:rhs])
    # bad naming, but have sence
    iter_l = 0
    iter_r = rhs
    iter_i = lhs
    while iter_l < rhs - lhs:
        if tmp[iter_l] <= a[iter_r]:
            a[iter_i] = tmp[iter_l]
            iter_l += 1
        else:
            a[iter_i] = a[iter_r]
            iter_r += 1
        iter_i += 1
        # copy the rest
        if iter_r == end:
            a[iter_i:end] = tmp[iter_l:]
            break

# stable merge(tim) sort
def merge_sort(a):
    chunk_size = 6
    if len(a) <= chunk_size:
        insertion_sort(a, 0, len(a))
        return ""
    chunks = 0
    appendix_length = len(a) % chunk_size
    chunks += len(a) / chunk_size
    print chunks, chunk_size
    # sorting chunks
    for i in xrange(0, chunks):
        insertion_sort(a, i * chunk_size,  (i + 1) * chunk_size)
    insertion_sort(a, chunks * chunk_size, len(a))
    # merging chunks
    while chunks > 1:
        shift = 0
        offset = 0
        i = 0
        # if odd then left last chunk for the next iteration
        if chunks % 2 == 1:
            shift = -1
        while i < chunks + shift:
            # begining of next chunk to merge
            offset = 2 * i * chunk_size
            merge(a, offset, offset + chunk_size, offset + 2 * chunk_size)
            # two chunks merged into one
            chunks -= 1
            i += 1
        chunk_size *= 2
    merge(a, 0, len(a) - appendix_length, len(a))


c = [4, 3, 5 ,6, 7 , 98, 2323, 4433, 3434, 4343 ,43434 ,343,434, 
     434, 565, 12, 567, 153, 567, 12, 234, 54, 2345, 3]
print c
merge_sort(c)
print c
a = [3, 12, 234, 10, 0, 345, 66, 13, 3, 12, 234, 10, 0, 345, 66, 13]
print a
merge_sort(a)
print a
d = [4, 3, 5 ,6, 7 , 98, 2323, 4433, 3434, 4343 ,43434 ,343]
print d
merge_sort(d)
print d
