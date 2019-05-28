
path = "/Users/lethachlam/Desktop/Doan/tinhtoan/DoAn/test.txt"
def pathUrl(path):
        path = path[::-1]
        pathstr=''
        for i in path:
            if i=='/':
                break
            pathstr +=i
        return pathstr[::-1]   

a = pathUrl(path)
print(a)
