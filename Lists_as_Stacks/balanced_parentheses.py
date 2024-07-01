data = input()

stack = []
open_par_right = False


for p in data:
    if p in '{[(':
        stack.append(p)
    elif p in '}])':
        if len(stack) > 0:
            opening_p = stack.pop()

        else:
            open_par_right = True
            print('not balanced')
            break

if len(stack) == 0 and not open_par_right:
    print('balanced')
elif len(stack) > 0:
    print('not balanced')
# data_inp = {[()]}
