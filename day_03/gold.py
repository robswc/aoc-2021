from helpers import helpers

lines = helpers.get_lines()

nums = lines
n_len = len(nums[0])
print('len is ', n_len)

gr = []

# DOCUMENTING BECAUSE IM ACTUALLY KINDA GLAD W/ SOLUTION lol

# Set up Co as a set, just going to filter it down
co = set(nums)
stp = None  # this went unused, thought I would need it

# make a loop with the length of the inputs
for idx in range(n_len):

    # create the number, based on vertical
    num = ''.join(i[idx] for i in co)

    # equal condition, make a selection set w/ numbers ending with a bit of 1
    if num.count('1') == num.count('0'):
        print('eq')
        select = set(i for i in co if i[idx] == '1')

    # if sum of bits favor 1, select 1, else select all the zeros
    elif num.count('1') > num.count('0'):
        select = set(i for i in co if i[idx] == '1')
    else:
        select = set(i for i in co if i[idx] == '0')

    # make a difference set
    print(select)
    diff = co - select
    print('diff', diff)
    co = diff

    # if we're left with just one number left, stop and thats our number
    if len(co) == 1:
        co = list(co)[0]
        break


# literally copy and paste the above, just flip the criteria and remember to go with the 1 vs the 0
ogr = set(nums)
stp = None
for idx in range(n_len):
    num = ''.join(i[idx] for i in ogr)

    if num.count('1') == num.count('0'):
        print('eq')
        select = set(i for i in ogr if i[idx] == '0')

    elif num.count('1') < num.count('0'):
        select = set(i for i in ogr if i[idx] == '1')
    else:
        select = set(i for i in ogr if i[idx] == '0')

    print(select)
    diff = ogr - select
    print('diff', diff)
    ogr = diff

    if len(ogr) == 1:
        ogr = list(ogr)[0]
        break

# check and convert to binary
print(ogr, co)
print(int(ogr, 2) * int(co, 2))


