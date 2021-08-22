def make_dict(lst: list, tokens: list) -> list:
    dict_list = []
    for item in lst:
        x = item.split(':')
        this_dict = {tokens[0]: x[0], tokens[1]: int(x[1].strip())}
        dict_list.append(this_dict)
    return dict_list


def bs4d(d2s: list, token: str) -> list:
    changed = False
    for i in range(0,len(d2s)-1):
        if d2s[i][token] < d2s[i+1][token]:
            d2s[i], d2s[i+1] = d2s[i+1], d2s[i]
            changed = True
    if changed:
        return bs4d(d2s, token)
    else:
        return d2s


def main():
    final = bs4d(make_dict(my_file, tokens), tokens[1])
    for i in final:
        print(i)

if __name__ == '__main__':
    tokens = ['champ', 'pics']
    my_file = open("champs.txt", "r").readlines()
    main()
