browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

last_in_stack = browsing_session[-1]
print(f"last in order {last_in_stack}")
forward_site = browsing_session.pop()
print('<--')
last_in_stack = browsing_session[-1]
print(f"last in order {last_in_stack}")
print(f'forward site {forward_site} -->')
