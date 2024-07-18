from memory_profiler import memory_usage
import time

data = [] # 會先存在記憶體，所以資料越大記憶體需要越大
def read_file():
    with open('reviews.txt', 'r') as f:
        for line in f :
            data.append(line)
    return (data)


#使用generator效能
def read_file_gen():
    with open('reviews.txt', 'r') as f:
        for line in f :
            yield line

it = read_file_gen()
count = 0 
sum_len = 0 
for line in it:
    sum_len += len(line)
    count += 1
print('avg len = ', sum_len / count)
print('avg len = ', sum_len / count)
   

print(f'Mem:{memory_usage()} MB')
start = time.time()
it = read_file()

#使用generator效能
it = read_file_gen()
next(it)

end = time.time()
print(f'共花費{end - start}secs')
print(f'Mem:{memory_usage()} MB')