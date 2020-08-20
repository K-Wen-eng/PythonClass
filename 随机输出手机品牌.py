# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：请不要修改其他已给出代码

import random
brandlist = ['三星','苹果','vivo','OPPO','魅族']
random.seed(0)
name = brandlist[random.randint(0,4)]
print(name)
‘’‘
import random
brandlist = ['三星','苹果','vivo','OPPO','魅族']
random.seed(0)
name = random.choice(brandlist)
print(name)
‘’‘
