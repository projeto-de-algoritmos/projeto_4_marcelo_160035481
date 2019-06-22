
import os
import tkinter as tk
from classes import *
from funcs import *
from consts import *
import random

class MyFrame:
    def __init__(self, root, name, row, column,itens=[],show_del_button=False):
        self.frame = tk.Frame(root)
        self.name = tk.Label(self.frame, text=name)
        tk.Label(self.frame, text="    id          nome         valor      peso").grid(row=1,column=0,sticky=tk.W)
        self.frame.grid(row=row, column=column)
        self.name.grid(row=0, column=0)
        self.del_buttons = []
        self.itens_txt = []
        self.placed_itens = itens
        self.show_del_button=show_del_button
        if (itens != []):
            self.fill()
    def clean_frame(self):
        # for item in self.placed_itens:
        #     self.placed_itens.remove(item)
            #show.destroy()
        for bttn in self.del_buttons:
            self.del_buttons.remove(bttn)
            bttn.destroy()
        for txt in self.itens_txt:
            self.itens_txt.remove(txt)
            txt.destroy()
        
    def delete_item(self, item):
        self.clean_frame() # pog
        self.placed_itens.remove(item)
        print("excluindo",item.name)
        print("sobrou {} itens".format(len(self.placed_itens)))
        self.fill()
    '''
    3|lapis|10|2
    4|caneta|25|7
    5|borracha|10|2
    '''
    def fill(self, itens=None):
        itens_row = 2
        self.clean_frame()
        if itens != None:
            self.placed_itens = itens
        if len(self.placed_itens) > 0:
            line = 0
            for item in self.placed_itens:
                txt = "{:^10}|{:^20}|{:^10}|{:^10}".format(item.item_id,item.name,item.value,item.weight)
                temp = tk.Label(self.frame,text=txt)
                temp.grid(row=itens_row+line, column=0,sticky=tk.W)
                self.itens_txt.append(temp)
                if(self.show_del_button):
                    del_bttn = tk.Button(
                        self.frame,text="Excluir",command=lambda bttn=item:self.delete_item(bttn))
                    del_bttn.grid(row=itens_row+line, column=1)
                    self.del_buttons.append(del_bttn)
                line += 1
        else:
            print("sem itens para por no frame")

def save_exit(root, itens, knapsack):
    success = save_to_file(ITENS_FILE,itens) and save_to_file(KNAPSACK_FILE,knapsack)
    if(success):
        root.destroy()
    else:
        print("deu ruim")

def find_max_id(itens):
    max_id = 0
    for i in itens:
        if i.item_id > max_id:
            max_id = i.item_id
    return max_id

def add_rand_item(itens_frame):
    itens_frame.placed_itens.append(
        Item( 1+find_max_id(itens_frame.placed_itens),
                            "rand{}".format(random.randint(1,100)),
                            random.randint(1,100),
                            random.randint(1,30))
    )
    itens_frame.fill()

def run():
    os.system("clear")
    itens = read_itens()
    # root screen (login screen)
    root = tk.Tk()
    root.title('Mochila')
    bar_frame = tk.Frame(root)
    bar_frame.grid(row=0, column=0)
    itens_frame = MyFrame(root,'TODOS OS ITENS',1,0,show_del_button=True)
    knap_frame = MyFrame(root,'ITENS NA MOCHILA',1,1)
    
    itens_frame.fill(itens)
    result = Result()
    max_w_txt = tk.Label(bar_frame, text='Peso:')
    max_weight = tk.Entry(bar_frame)
    rand_item = tk.Button(bar_frame, text="Add item aleatório",command=lambda itf=itens_frame:add_rand_item(itf))
    max_weight.delete(0,tk.END)
    max_weight.insert(0,'11')
    calcule = tk.Button(bar_frame, text="Calcular",command=lambda m=max_weight,i=itens, r=result, kf=knap_frame:calc_knapsack(m.get(), i, r,kf))
    exit_bttn = tk.Button(bar_frame, text="Salvar e sair",command=lambda prog=root:save_exit(root,itens_frame.placed_itens, result.solution))
    rand_item.grid(row=0, column=4)
    exit_bttn.grid(row=0, column=3)
    calcule.grid(row=0, column=2)
    max_w_txt.grid(row=0, column=0)
    max_weight.grid(row=0, column=1,sticky=tk.W)
    
    

    #info_txt = tk.StringVar()
    # puttin all widgets
    
    # username.grid(row=0, column=1)  
    # login_txt.grid(row=0,column=0)
    # logbutton.grid(row=1,column=0)
    # info.grid(row=1,column=1)

  
    set_window_geom(root)
    root.mainloop()

if(__name__ == '__main__'):
    run()