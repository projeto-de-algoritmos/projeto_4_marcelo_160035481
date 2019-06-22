from consts import *
from classes import *

def find_solution(matrix, n, w,val,wt,itens):
    solution = []
    res = matrix[n][w]
    #print(res) 
    
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        if res == matrix[i - 1][w]: 
            continue
        else: 
            solution.insert(0,itens[i - 1]) 
              
            res = res - val[i - 1] 
            w = w - wt[i - 1]
    return solution, matrix[n][w-1]

def calc_knapsack(Wstr, itens, sol, knap_frame):
    try:
        W = int(Wstr)
    except ValueError:
        print("Valor inválido")
        sol.solution = []
        sol.max_weight = 0
        return sol

    val = []
    wt = []
    for i in itens:
        val.append(i.value)
        wt.append(i.weight)
    n = len(val)

    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    # return K, n+1, W+1
    rtrna, rtrnb = find_solution(K, n, W,val,wt,itens)
    sol.solution = rtrna
    sol.max_weight = rtrnb
    knap_frame.placed_itens = sol.solution
    knap_frame.fill()
    print("Peso total carregado: {}".format(rtrnb))
    print("ids dos itens carregados:")
    for i in rtrna:
        print(i.item_id)
    
    return sol

def read_itens():
    try:
        itens_data = open(ITENS_FILE,"r")
    except:
        itens_data = open(ITENS_FILE,"w")
        return []
    
    itens_lines = itens_data.readlines()
    itens = []
    
    for i in itens_lines:
        # read the item informations
        temp = i.split('|')
        itens.append( Item( int(temp[ITEM_ID]),
                            temp[NAME],
                            int(temp[VALUE]),
                            int(temp[WEIGHT]))
                    )

    itens_data.close()
    return itens

def save_to_file(file_name, itens):
    try:
        itens_data = open(file_name,"w")
    except:
        print("impossivel abrir arquivo")
        return False
    
    # itens_lines = itens_data.readlines()
    
    for item in itens:
        # read the item informations
        itens_data.write("{}|{}|{}|{}\n".format(item.item_id,item.name,item.value,item.weight))
        
    itens_data.close()
    return True

def set_window_geom(window):
    width = WINDOW_FORMAT[0]*WINDOW_TIMES_SIZE
    height = WINDOW_FORMAT[1]*WINDOW_TIMES_SIZE
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_geom = "{}x{}+{}+{}".format(
        width, height, int((screen_width-width)/2), int((screen_height-height)/2)
    )
    window.geometry(window_geom)