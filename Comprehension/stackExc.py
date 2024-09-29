command = ''
browser_on = True
browser_session = []
while browser_on:

    # count = 1
    current_command = input('-<->- ')
    if current_command == 'off':
        browser_on = False
        break
    # forward
    if current_command == 'f' and not browser_session:
        browser_session = []
        count = 1
        browser_session.append(count)
        count += 1
        continue
    if current_command == 'f' and browser_session:
        browser_session.append(count)
        count += 1
        continue

    # session order
    if current_command == 's':
        num_of_pages = len(browser_session)
        print(f'{num_of_pages} pages path')

    # backward
    if current_command == 'b':
        last = browser_session.pop()
        count -= 1
        print(f"current page {browser_session[-1]}")
