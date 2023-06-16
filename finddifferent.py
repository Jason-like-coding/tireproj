import os


def find_different_files(folder1, folder2):
    files1 = set(os.path.splitext(filename)[0] for filename in os.listdir(folder1))
    files2 = set(os.path.splitext(filename)[0] for filename in os.listdir(folder2))

    different_files = files1.symmetric_difference(files2)

    return different_files



# 请提供两个文件夹的路径
folder1 = 'C:\\Users\\jeffe\\Desktop\\model\\yolov7-pytorch-master\\VOCdevkit\\VOC2007\\Annotations'
folder2 = 'C:\\Users\\jeffe\\Desktop\\model\\yolov7-pytorch-master\\VOCdevkit\\VOC2007\\JPEGImages'

different_files = find_different_files(folder1, folder2)
print("名称不同的文件:")
for file in different_files:
    print(file)
