
#Задание№1(easy)

# import os
#
# os.mkdir("dir_1")
# os.mkdir("dir_2")
# os.mkdir("dir_3")
# os.mkdir("dir_4")
# os.mkdir("dir_5")
# os.mkdir("dir_6")
# os.mkdir("dir_7")
# os.mkdir("dir_8")
# os.mkdir("dir_9")
#
# os.rmdir("dir_1")
# os.rmdir("dir_2")
# os.rmdir("dir_3")
# os.rmdir("dir_4")
# os.rmdir("dir_5")
# os.rmdir("dir_6")
# os.rmdir("dir_7")
# os.rmdir("dir_8")
# os.rmdir("dir_9")

# import os
#
# def new_file(file):
#     path = os.path.join(file)
#     try:
#         os.makedirs(path)
#         print("Создана папка " + file)
#     except FileExistsError:
#         print("Папка с таким именем уже существует")
#
#
# if __name__ == "__main__":
#     for i in range(1, 10):
#         new_file("{}_{}".format("dir", i))
#
#
# def file_remove(file_to_remove):
#     you_sure = input("{} {} {}".format("Удалить папку? ", file_to_remove, "? Да или Нет'))
#
#     if you_sure == "да" or ui_sure == "Да" or you_sure == " да" or you_sure == " Да" :
#         try:
#             os.removedirs(file_to_remove)
#             print("Вы успешно удалили " + file_to_remove)
#         except (TypeError, FileNotFoundError):
#             print("Не верно указан путь")
#     else:
#         print("Операция отменена")
#
#
# if __name__ == "__main__":
#     for i in range(1, 10):
#         file_remove("{}_{}".format("dir", i))

#Задание№2(easy)

# import os
#
# l=os.listdir(path="C:\\Users\Пользователь\.PyCharmCE2018.1\config\scratches")
#
# print(l)

#Задание№3(easy)

# import shutil
#
# copy_task= shutil.copy("Задание№5.py","Задание№5_копия.py")






