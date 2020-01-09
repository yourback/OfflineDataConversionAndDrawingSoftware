def read_fileline():
    f = open('data.txt', 'r+')
    # for i in range(100):
    line_context = f.readline()
    return line_context


def get_item_data(data, i):
    return (int(data[i], 16) << 8 + int(data[i + 1], 16)) / 100


def get_datas(data):
    LD = get_item_data(data, 0)
    LU = get_item_data(data, 2)
    RD = get_item_data(data, 4)
    RU = get_item_data(data, 6)
    K_R = get_item_data(data, 10)
    K_L = get_item_data(data, 12)
    return LD, LU, RD, RU, K_R, K_L


if __name__ == '__main__':
    one_line = read_fileline()
    end = one_line.index(" 0D 0A")
    start = 1
    line_result = one_line[start:end]
    item_data_list = line_result.split(" ")
    # print(item_data_list)
    data_LD, data_LU, data_RD, data_RU, data_K_R, data_K_L = get_datas(item_data_list)

    # print("data_LD: %s" % data_LD)
    # print("data_LU: %s" % data_LU)
    # print("data_RD: %s" % data_RD)
    # print("data_RU: %s" % data_RU)
    # print("data_K_R: %s" % data_K_R)
    # print("data_K_L: %s" % data_K_L)
