# 字典测试
West_1_234 = {
            'C1': 'ShanTou',
            'C2': 'FoShan',
            'L3': 'ZhaoQing',
            'C4': 'DongGuan'
}

print("西1-234的C1舍友来自", West_1_234['C1'])

# 删除一堆键值-值配对
del West_1_234['L3']

print('\nWest_1_234中有{}个数据\n'.format(len(West_1_234)))

for name, places in West_1_234.items():
    print('舍友{}来自{}'.format(name, places))
# 添加一对键值-值配对
West_1_234['L3'] = 'Unknown'

if 'L3' in West_1_234:
    print("\nL3来自", West_1_234['L3'])
