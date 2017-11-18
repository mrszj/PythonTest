#coding=utf8

def displayInventory(item):
    item_count=0
    print('*'*50)
    print('Inventory:\n '+'-'*24)
    for k,v in item.items():
        print('%7d | %-1s' %(v,k))
        print(' '+'-'*24)
        item_count+=v
    print("装备总数量为:" + str(item_count))
    print('*'*50)
#displayInventory(item)
def addToInventory(item,addedItems):
    print("战斗结算中....")
    for i in addedItems:
        item[i]=item.setdefault(i,0)+1
    return item
item={
    '金币':1
    }
dragonLoot = ['金币', '匕首', '金币', '金币', '红宝石','倚天剑','屠龙刀','爱奇艺30天会员卡']
print('勇士,你现在拥有:')
displayInventory(item)
n=0
while True:
    kill=raw_input('前面'+'又'*n +'出现一条巨龙,是否干掉他:Y/N\n').strip()
    if kill == 'Y' or kill == 'y':
        print("你非常勇敢,杀死了一条龙,获得了若干物品")
        n+=1
        item=addToInventory(item, dragonLoot)
        displayInventory(item)
        continue
    if kill == 'N' or kill=='n':
        print('懦夫,\n你的物品栏被清空了。\nGAME OVER !!!')
        break
    else:
        continue
    break
