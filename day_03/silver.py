from helpers import helpers

lines = helpers.get_lines()

nums = lines
n_len = len(nums[0])
print('len is ', n_len)

gr = []

for idx in range(n_len):
    num = ''.join(i[idx] for i in nums)
    if num.count('1') > num.count('0'):
        gr.append('1')
    else:
        gr.append('0')

tmp = ''.join(gr).replace('0', 'x').replace('1', 'y')
tmp = ''.join(tmp).replace('x', '1').replace('y', '0')
er = tmp
print(er)

gr = int(''.join(gr), 2)
er = int(''.join(er), 2)

print(gr * er)