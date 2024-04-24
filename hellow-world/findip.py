ip_address = ["192.3.3.3.", "111.1.1.1", "233.3.3.3", "493.3.3.3.3."]


def getFirstThreeOfIPS(list):
    for i in list:
        print(i[0:3])


getFirstThreeOfIPS(ip_address)
