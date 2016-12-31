import matplotlib.pyplot as plt
import numpy as np

show_each=100
array = []
for i in range(10):
    with open('GALS/ATP_55_' + str(i) + '.txt', 'r') as f:
        index = 0
        if i > 0:
            for line in f:
                if index % show_each == 0:
                    array[int(index / show_each)].append(float(line))
                index += 1
        else:
            for line in f:
                if index % show_each == 0:
                    array.append([float(line)])
                index += 1  # basic plot
plt.boxplot(array,whis ='range')
'''plt.ylabel('Accuracy')
plt.xlabel('Samples processed')
new_locs=[]
new_labels=[]
for i in range(0,len(array)+1,1):
    new_locs.append(i)
    new_labels.append(i*1000)
plt.xticks(new_locs, new_labels)
name="Testing accuracy of labels 6-9 0.01 without fixed convolution and dropout"
plt.title(name)'''
sum=0
for i in range(10):
    sum+=array[len(array)-1][i]
print(sum/10)
plt.show()
# plt.savefig(name+".png")
