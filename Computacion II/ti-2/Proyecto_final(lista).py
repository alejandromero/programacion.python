# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog as filedialog
from PIL import Image, ImageTk
from shutil import copy2
import os


class Img:
    def __init__(self, name, directory, tag, idi):
        self.name = name
        self.directory = directory
        self.tag = tag.strip().split(',')
        self.size = str(os.stat(directory+'/'+name).st_size)
        self.idi = str(idi)


class ImgDic:
    def __init__(self):
        self.dic = []
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        self.idi = 0
        self.copy = True
        self.load_library()

    def copy_images(self, selection):
        self.copy = selection

    def add_img(self, name_dir, tag):
        file1 = open(self.file_path+'/img_directory.txt', 'a')
        file2 = open(self.file_path+'/image_library/img_map.txt', 'a')

        if self.copy:
            if name_dir[0] in os.listdir(self.file_path+'/image_library'): # Si la imagen ya está copiada
                return False
            else: #Si la imagen no está
                copy2(name_dir[1]+'/'+name_dir[0], self.file_path+'/image_library')
                self.dic.append(Img(name_dir[0], name_dir[1], tag, self.idi))
                file2.write(name_dir[0]+'|'+self.file_path+'/image_library'+'|'+tag+'|'+str(self.idi)+'\n')
                self.idi += 1
        else:
            if name_dir[0] in self.txt_names():
                pass
            else:
                self.dic.append(Img(name_dir[0], name_dir[1], tag, self.idi))
                file1.write(name_dir[0]+'|'+name_dir[1]+'|'+tag+'|'+str(self.idi)+'\n')
                self.idi += 1

        file1.close()
        file2.close()

    def image_names(self, directory):
        names = []
        for name in os.listdir(directory):
            if name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                names.append([name, directory])
            elif os.path.isdir(directory + '/' + name):
                for i in self.image_names(directory + '/' + name):
                    names.append(i)
            else:
                pass
        return names

    def see_dic(self): # Funcion obsoleta para la GUI
        for i in self.dic:
            print '\n' + i + ':'
            for j in self.dic[i]:
                print '\n'
                print 'Nombre del archivo: ' + j.name
                print 'Ubicacion: ' + j.directory
                print 'Tamaño (bytes): ' + j.size

    def search_images(self, tags):
        images = []
        tags = tags.strip().split(',')
        for i in self.dic:
            if any(j in tags for j in i.tag):
                images.append(i)
            else:
                pass
        return images

    def change_tag(self, image, new_tag):
        self.dic.pop(self.dic.index(image))
        image.tag = new_tag.strip().split(',')
        self.dic.append(image)

    def graph_data(self):
        data = {}
        for img in self.dic:
            for tag in img.tag:
                if tag in data:
                    for sec_tag in img.tag:
                        if sec_tag in data[tag]:
                            pass
                        else:
                            sec_tag.append(tag)
                else:
                    data[tag] = filter((lambda x: x if x != tag else None), (t for t in img.tag))
        return data

    def rewrite(self):
        file1 = open(self.file_path + '/img_directory.txt', 'w')
        file2 = open(self.file_path + '/image_library/img_map.txt', 'w')

        for j in self.dic:
            if os.path.isfile(self.file_path+'/image_library/'+j.name):
                file2.write(j.name+'|'+j.directory+'|'+','.join(j.tag)+'|'+j.idi+'\n')
            else:
                file1.write(j.name+'|'+j.directory+'|'+','.join(j.tag)+'|'+j.idi+'\n')

        file1.close()
        file2.close()

    def txt_names(self):
        file1 = open(self.file_path + '/img_directory.txt', 'r')
        names = []
        for i in file1:
            i = i.rstrip().split('|')
            names.append(i[0])
        return names

    def load_library(self):
        paths = [self.file_path + '/img_directory.txt', self.file_path + '/image_library/img_map.txt']
        if os.path.isdir(self.file_path + '/image_library'):
            pass
        else:
            os.mkdir(self.file_path + '/image_library')
        for i in paths:
            if os.path.isfile(i):
                file1 = open(i, 'r')
                for j in file1:
                    j = j.rstrip().split('|')
                    self.dic.append(Img(j[0], j[1], j[2], j[3]))
                    self.idi += 1
                file1.close()
            else:
                open(i, 'w').close()


class App: #cyan4, gold2, olive drab, DarkOrange2

    def __init__(self, images):
        self.root = Tk()
        self.root.title('Organizador de fotos')
        self.root.geometry('735x670')
        self.root.resizable(0, 0)
        self.images = images
        self.main_menu()

    def main_menu(self):
        # self.root.geometry('')
        # self.root.resizable(0,0)
        for child in self.root.winfo_children():
            child.destroy()
        frame1 = Frame(self.root, bg='cyan4')#Primera division de la ventana
        frame1.pack(fill=BOTH, expand=1)
        frame2 = Frame(self.root, bg='gold2')
        frame2.pack(fill=BOTH, expand=1)
        frame3 = Frame(self.root, bg='olive drab')
        frame3.pack(fill=BOTH, expand=1)
        frame4 = Frame(self.root, bg='DarkOrange2')
        frame4.pack(fill=BOTH, expand=1)
        Button(frame1, fg='white', activeforeground='cyan4', bg='cyan4', activebackground='white', borderwidth=0, text='Agregar imagenes', command=self.import_window).pack(expand=1)
        Button(frame2, fg='white', activeforeground='gold2', bg='gold2', activebackground='white', borderwidth=0, text='Cambiar etiqueta', command=self.change_tag_window).pack(expand=1)
        Button(frame3, fg='white', activeforeground='olive drab', bg='olive drab', activebackground='white', borderwidth=0, text='Mi libreria', command=self.see_library).pack(expand=1)
        Button(frame4, fg='white', activeforeground='DarkOrange2', bg='DarkOrange2', activebackground='white', borderwidth=0, text='Buscador', command=self.searcher).pack(expand=1)
        self.menu()
        self.root.mainloop()

    def open_image(self, label, names, current, n, variable=None):
        if 0 <= current[0] + n < len(names):
            if all(isinstance(i, Img) for i in names):
                try:
                    current[0] += n
                    img = Image.open(names[current[0]].directory+'/'+names[current[0]].name)
                    img = img.resize((700, 600), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    label['image'] = img
                    label.image = img
                    if isinstance(variable, Entry):
                        variable.delete(0, END)
                        variable.insert(0, ','.join(names[current[0]].tag))
                    elif isinstance(variable, Label):
                        variable['text'] = ','.join(names[current[0]].tag)
                        variable.text = ','.join(names[current[0]].tag)
                    else:
                        pass
                except:
                    current[0] += n
            elif all(isinstance(j, list) for j in names):
                try:
                    name, path = names[current[0] + n]
                    img = Image.open(path + '/' + name)
                    current[0] += n
                    img = img.resize((700, 600), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    label['image'] = img
                    label.image = img
                except:
                    names.pop(current[0] + n)
        else:
            Label(Toplevel(), text='No hay mas imagenes, si ha terminado el etiquetado oprima boton agregar').pack()

    def import_window(self):

        dir = filedialog.askdirectory()

        if os.path.isdir(dir):
            for child in self.root.winfo_children():
                child.destroy()

            image_list = self.images.image_names(dir)
            current_element = [0]

            img_frame = Frame(self.root)
            img_frame.pack(side=TOP, fill=BOTH, expand=1)
            left_frame = Frame(self.root)
            left_frame.pack(side=LEFT, fill=BOTH, expand=1)
            right_frame = Frame(self.root)
            right_frame.pack(side=RIGHT, fill=BOTH, expand=1)
            central_frame = Frame(self.root)
            central_frame.pack(side=BOTTOM, fill=BOTH, expand=1)

            img_label = Label(img_frame)
            img_label.pack()

            Label(central_frame, text='Etiqueta: ').grid(row=0, column=0)
            tag = Entry(central_frame)
            tag.grid(row=0, column=1)
            Button(left_frame, text='Anterior', borderwidth=0, command=lambda: self.open_image(img_label, image_list, current_element, -1)).pack()
            Button(right_frame, text='Siguiente', borderwidth=0, command=lambda: self.open_image(img_label, image_list, current_element, 1)).pack()
            Button(central_frame, text='Agregar imagen', borderwidth=0, command=lambda: self.images.add_img(image_list[current_element[0]], tag.get())).grid(row=2, column=0)
            Button(central_frame, text='Regresar', borderwidth=0, command=self.main_menu).grid(row=2, column=1)

            self.open_image(img_label, image_list, current_element, 0)
            self.menu()

        else:
            return False

    def change_tag_window(self):

        image_list = []
        for im in self.images.dic:
            image_list.append(im)

        if len(image_list)>0:

            for child in self.root.winfo_children():
                child.destroy()

            def get_out():
                self.images.rewrite()
                self.main_menu()

            current_element = [0]

            img_frame = Frame(self.root)
            img_frame.pack(side=TOP, fill=BOTH, expand=1)
            left_frame = Frame(self.root)
            left_frame.pack(side=LEFT, fill=BOTH, expand=1)
            right_frame = Frame(self.root)
            right_frame.pack(side=RIGHT, fill=BOTH, expand=1)
            central_frame = Frame(self.root)
            central_frame.pack(side=BOTTOM, fill=BOTH, expand=1)

            img_label = Label(img_frame)
            img_label.pack()

            Label(central_frame, text='Etiqueta: ').grid(row=0, column=0)
            new_tag = Entry(central_frame)
            new_tag.grid(row=0, column=1)
            Button(left_frame, text='Anterior', borderwidth=0, command=lambda: self.open_image(img_label, image_list, current_element, -1, new_tag)).pack()
            Button(right_frame, text='Siguiente', borderwidth=0, command=lambda: self.open_image(img_label, image_list, current_element, 1, new_tag)).pack()
            Button(central_frame, text='Cambiar etiqueta', borderwidth=0, command=lambda: self.images.change_tag(image_list[current_element[0]], new_tag.get())).grid(row=2, column=0)
            Button(central_frame, text='Regresar', borderwidth=0, command=get_out).grid(row=2, column=1)

            self.open_image(img_label, image_list, current_element, 0, new_tag)
            self.menu()

        else:
            Label(Toplevel(), text='Necesita agregar imagenes primero').pack()

    def see_library(self):

        if len(self.images.dic)!=0:

            image_list = []
            for im in self.images.dic:
                image_list.append(im)

            for child in self.root.winfo_children():
                child.destroy()

            current_element = [0]

            img_frame = Frame(self.root)
            img_frame.pack(side=TOP, fill=BOTH, expand=1)
            left_frame = Frame(self.root)
            left_frame.pack(side=LEFT, fill=BOTH, expand=1)
            right_frame = Frame(self.root)
            right_frame.pack(side=RIGHT, fill=BOTH, expand=1)
            central_frame = Frame(self.root)
            central_frame.pack(side=BOTTOM, fill=BOTH, expand=1)

            img_label = Label(img_frame)
            img_label.pack()

            tag = Label(central_frame)
            tag.grid(row=0, column=1)
            Button(left_frame, text='Anterior', borderwidth=0, command=lambda: self.open_image(img_label, image_list, current_element, -1, tag)).pack()
            Button(right_frame, text='Siguiente', borderwidth=0, command=lambda: self.open_image(img_label, image_list, current_element, 1, tag)).pack()
            Button(central_frame, text='Regresar', borderwidth=0, command=self.main_menu).grid(row=2, column=1)

            self.open_image(img_label, image_list, current_element, 0, tag)
            self.menu()

        else:
            Label(Toplevel(), text='No tienes imagenes en tu bilbioteca').pack()

    def searcher(self):

        if len(self.images.dic) != 0:

            for child in self.root.winfo_children():
                child.destroy()

            search_frame = Frame(self.root)
            search_frame.pack(fill=BOTH, expand=1)
            img_frame = Frame(self.root)
            img_frame.pack(fill=BOTH, expand=1)

            Label(search_frame, text='Etiquetas a buscar').grid(row=0, column=0)
            search = Entry(search_frame)
            search.grid(row=0, column=1)
            Button(search_frame, text='Buscar', borderwidth=0, command=lambda: self.mosaic_view(self.images.search_images(search.get()), img_frame)).grid(row=1, column=1)
            Button(search_frame, text='Regresar', borderwidth=0, command=self.main_menu).grid(row=1, column=0)

        else:
            Label(Toplevel(), text='No tienes imagenes en tu bilbioteca').pack()

    def mosaic_view(self, results, frame):
        for child in frame.winfo_children():
            child.destroy()

        for i in range(len(results)):
            img = Image.open(results[i].directory+'/'+results[i].name)
            img = img.resize((182, 155), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            img_button = Button(frame, image=img, borderwidth=0, command=lambda p=results[i].directory+'/'+results[i].name: self.top_image(p))
            img_button.image = img
            img_button.grid(row=i//4, column=i%4)

    def top_image(self, path):
        img = Image.open(path)
        img = img.resize((600, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        image_label = Label(Toplevel(), image=img)
        image_label.image = img
        image_label.pack()

    def menu(self):
        option_menu = Menu(self.root)
        self.root.config(menu=option_menu)
        config_menu = Menu(option_menu)
        option_menu.add_cascade(label='Config', menu=config_menu)
        config_menu.add_command(label='Copiar images', command=lambda: self.images.copy_images(True))
        config_menu.add_command(label='No copiar images', command=lambda: self.images.copy_images(False))

images_d = ImgDic()
app = App(images_d)
