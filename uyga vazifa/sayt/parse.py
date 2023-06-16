def mmm(h):
    from bs4 import BeautifulSoup
    import requests
    import pytarjimon
    arr = requests.get(f'https://www.thefactsite.com/?s={h}')
    a=[]
    soup = BeautifulSoup(arr.text, 'html.parser')
    faktlar = soup.find_all('h2', class_='gb-headline gb-headline-e46d7748 gb-headline-text gb-headline-3e9d00e9')
    for f in faktlar:
        a.append(pytarjimon.tarjima(f.text.strip('.'), 'uz'))
    print(a)
    op=[]
    opi = soup.find_all('span', class_='excerpt_part')
    for o in opi:
        op.append(pytarjimon.tarjima(o.text.strip('.'), 'uz'))
    arr = []
    for i in range(len(a)):
        try:
            arr.append([a[i], op[i]])
        except:
            pass
    return arr