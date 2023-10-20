
def urlParser():
    url = 'ftp://www.helloworld.com/path/another/third/fourth?query=hello'
    
    buffer = []
    characters = []
    syms = []
    nextChar = ''
    possibleSyms = [':', '/', '?', '@', '#']

    for idx,chars in enumerate(url):
        if chars not in possibleSyms:
            characters.append(chars)
            nextChar = url[idx+1]


        if chars in possibleSyms:
            syms.append(chars)
            nextChar = url[idx+1]
            if nextChar not in possibleSyms:
                buffer.append(''.join(characters))
                buffer.append(''.join(syms))
                characters = []
                syms = []
        
    urlProps = {
        'protocol' : None,
        'domain' : None,
        'paths' : [],
        'query' : None
    }
    
    for idx, chars in enumerate(buffer):
        if chars == '://':
            urlProps['protocol'] = buffer[idx-1]
            urlProps['domain'] = buffer[idx+1]
        elif chars == '/':
            urlProps['paths'].append(buffer[idx+1])
        # elif chars == '?':
        #     urlProps['query'] = buffer[idx+1]

    print(buffer)
urlParser()