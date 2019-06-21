def load_label(filename):
   with open(filename,'r') as file:
    list = [line.rstrip() for line in file]
   return list



listt = load_label("cnn_labels.txt")
print(listt)
