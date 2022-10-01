def fungsi_Pangkat(x,y):
    if y>1:
        return x*fungsi_Pangkat(x,y-1)
    return x
print(fungsi_Pangkat(3,2))