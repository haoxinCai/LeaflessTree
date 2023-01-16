# 序列测试
test_item = ['A0', 'B1', 'C2', 'D3']
name = 'LeaflessTree'

# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', test_item[0])
print('Item 1 is', test_item[1])
print('Item 2 is', test_item[2])
print('Item 3 is', test_item[3])
print('Item -1 is', test_item[-1])
print('Item -2 is', test_item[-2])
print('Character 0 is', test_item[0])

# Slicing on a list #
print('Item 1 to 3 is', test_item[1:3])
print('Item 2 to end is', test_item[2:])
print('Item 1 to -1 is', test_item[1:-1])
print('Item start to end is', test_item[:])

# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
