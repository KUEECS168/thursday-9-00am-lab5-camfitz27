def funtion():
    user=0
    shop_list=[]
    while user != '4':
        print('Welcome to your shopping list!')
        print('1) Add item')
        print('2) Check off item')
        print('3) Print list')
        print('4) Exit')

        user=input('Enter a choice: ')

        if user == '1':
            add=input('What will you add to the list?: ')
            shop_list.append(add)

        if user =='2':
            off=int(input('Which item will you check off?: '))
            item= shop_list[off-1]
            remove= item[0]+('-'*(len(item)-2))+item[-1]
            shop_list[off-1]=remove

        if user == '3':
            for i in range(0, len(shop_list)):
                print('\n',(i+1),')',shop_list[i])
                i=i+1

funtion()
print('Goodbye!')
            
    
