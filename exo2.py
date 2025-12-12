global_data = ""
def ma_fonction():
    global global_data
    global_data = "variable modifie"
    return global_data
print(ma_fonction())
#
