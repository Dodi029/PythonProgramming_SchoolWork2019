def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    for line in infile:
        spaces +=line.count('')
        tabs +=line.count('\t')
    infile.close()

    return spaces, tabs
filename = input("파일 이름을 입력하시오 :");
spaces, tabs = parse_file(filename)
print("스페이스 수 = %d, 탭의 수 = %d"% (spaces, tabs))
