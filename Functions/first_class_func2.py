# def logger(msg):
    
#     def log_message():
#         print('Log', msg)

#     return log_message

# log_hi = logger('hi')
# log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text

print_h1 = html_tag('h1')
print(print_h1.__name__)
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')