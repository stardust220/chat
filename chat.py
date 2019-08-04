def read_file(filename):
    lines = []
    with open(filename,'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines 

def convert(lines):
    new = []
    person = None #虛無的值
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果有值這部分才會去處理
            new.append(person+ ': '+ line)
    return new 

def write_file(filename, lines):
    with open(filename,'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n') #的意思


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output_qinc.txt',lines) #把剛剛convert的檔案輸出來
main()