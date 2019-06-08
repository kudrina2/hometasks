import re


#def get_list():
    #список всех файлов


def work_it(file):
    tags = []
    with open (file, encoding='utf-8')as f:
        for line in f:
            if 'newdoc' in line:
                puti = re.split(r'= ',line)
                tags.append(puti[1])
    for i in range(len(tags)):
        kek = str(tags[i])
        tags[i] = kek.strip() 
    print(tags)


def main():
    a = work_it('all_afz1.txt')


if __name__ == '__main__':
    main()
