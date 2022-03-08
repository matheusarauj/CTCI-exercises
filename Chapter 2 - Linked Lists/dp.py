import time
horarios_emp = []

def procedure_schedule(node, horario):
    global procedures
    new_node = []
    for i in range(12):
        value = node[i] - horario[i]
        if value < 0:
            value = 0
        new_node.append(value)

    procedures[hash(str(node)) + hash(str(horario))] = new_node
    return new_node

def generate_horarios(horas_loja, qnt_hora_emp, cupons_emp):
    pivot = 0
    horarios = []
    while (pivot + qnt_hora_emp + 1) <= horas_loja:
        horario = []
        for i in range(horas_loja):
            if(i >= pivot and i < (qnt_hora_emp + pivot + 1) and i != 4 + pivot):
                horario.append(cupons_emp)
            else:
                horario.append(0)
        
        horarios.append(horario)
        pivot += 1
    
    return horarios

def run_tree(node, level, prev):
    global procedures
    global values
    if(level == qnt_emp):
        count = 0
        for i in node:
            count += i
        values[count] = [prev, node]

        return 

    node_prev = prev.copy()
    node_prev.append(1)
    if(hash(str(node)) + hash(str(array_horarios[1])) not in procedures):
        run_tree(procedure_schedule(node, array_horarios[1]), level + 1, node_prev)
    
    node_prev = prev.copy()
    node_prev.append(2)
    if(hash(str(node)) + hash(str(array_horarios[2])) not in procedures):
        run_tree(procedure_schedule(node, array_horarios[2]), level + 1, node_prev)

    node_prev = prev.copy()
    node_prev.append(3)
    if(hash(str(node)) + hash(str(array_horarios[3])) not in procedures):
        run_tree(procedure_schedule(node, array_horarios[3]), level + 1, node_prev)

def run_tree_without_dp(node, level, prev):
    global procedures
    global values
    if(level == qnt_emp):
        count = 0
        for i in node:
            count += i
        values[count] = [prev, node]

        return 

    node_prev = prev.copy()
    node_prev.append(1)
    run_tree_without_dp(procedure_schedule(node, array_horarios[1]), level + 1, node_prev)
    
    node_prev = prev.copy()
    node_prev.append(2)
    run_tree_without_dp(procedure_schedule(node, array_horarios[2]), level + 1, node_prev)

    node_prev = prev.copy()
    node_prev.append(3)
    run_tree_without_dp(procedure_schedule(node, array_horarios[3]), level + 1, node_prev)


start = time.time()
horario_func_loja = 13
array_cupons = [10, 15, 20, 30, 40, 50, 40, 30, 40, 60, 70, 40, 10]
cupons_emp = 10
qnt_emp = 14
qnt_hora_emp = 8

procedures = {}
values = {}

array_horarios = generate_horarios(horario_func_loja, qnt_hora_emp, cupons_emp)

new_values = procedure_schedule(array_cupons, array_horarios[0])
new_values = procedure_schedule(new_values, array_horarios[len(array_horarios) - 1])
list_prev = [0, len(array_horarios) - 1]

run_tree(new_values, 2, list_prev)

n = 0
i = 0


end = time.time()
for key in sorted(values):
    print("%s: %s" % (key, values[key]))
print(end - start)


