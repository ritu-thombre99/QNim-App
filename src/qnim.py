import numpy as np
from qiskit import BasicAer, QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit import IBMQ
# provider = IBMQ.load_account()


def misere_step(ones,piles):
    # even number of piles of 1 eg (1,1,3,0) or (0,0,3,0)
    if ones%2 == 0:
        objects_to_remove = []
        removable_amount = 1
        for i in range(len(piles)):
            if piles[i] > 1:
                objects_to_remove.append(piles[i]-1)
            else:
                objects_to_remove.append(0)
    # odd number of piles of 1 eg (1,1,3,1)
    else:
        objects_to_remove = []
        removable_amount = 1
        for i in range(len(piles)):
            if piles[i] > 1:
                objects_to_remove.append(piles[i])
            else:
                objects_to_remove.append(0)
    return objects_to_remove, removable_amount

def get_piles_to_remove(piles):
    nim_sum = 0
    for p in piles:
        nim_sum = nim_sum ^ p
    objects_to_remove = []
    removable_amount = 0
    for p in piles:
        new_p = p^nim_sum
        if new_p < p:
            objects_to_remove.append(p-new_p)
            removable_amount = removable_amount + 1
        else:
            objects_to_remove.append(0)
    return objects_to_remove, removable_amount

    
def custom_qft(data_qubits):
    qr_data = QuantumRegister(data_qubits)
    qc = QuantumCircuit(qr_data)
    i = data_qubits
    while i>=1:
        n = i - 1
        qc.h(qr_data[n]) 
        for qubit in range(n):
            qc.cp(np.pi/2**(n-qubit), qr_data[qubit], qr_data[n])
        i = i-1
    return qc

def subroutine_add_const(data_qubits: int, const: int, to_gate=True):
    qc = QuantumCircuit(data_qubits)
    for i in range(data_qubits):
        angle = const*np.pi/(2**i)
        qc.p(angle,i)
    return qc.to_gate(label=" ["+str(const)+"] ") if to_gate else qc

def diffusion_operation(qc, address, flag, removable_pile):
    def nim_oracle(qc,address,flag,removable_pile):

        # 0001 -> 001
        if removable_pile[0] != 0:
            qc.x(address[1])
            qc.x(address[2])
            qc.mct(address[:],flag)
            qc.x(address[2])
            qc.x(address[1])
        
        # 0010 -> 010
        if removable_pile[1] != 0:
            qc.x(address[0])
            qc.x(address[2])
            qc.mct(address[:],flag)
            qc.x(address[2])
            qc.x(address[0])
    
        # 0100 -> 011
        if removable_pile[2] != 0:
            qc.x(address[2])
            qc.mct(address[:],flag)
            qc.x(address[2])
        
        # 1000 -> 100
        if removable_pile[3] != 0:
            qc.x(address[0])
            qc.x(address[1])
            qc.mct(address[:],flag)
            qc.x(address[1])
            qc.x(address[0])


    qc.x(flag)
    qc.h(flag)

    qc.h(address[:])
    nim_oracle(qc,address,flag,removable_pile)
    qc.h(address[:])
    qc.x(address[:])
    qc.h(address[2])
    qc.mct(address[0:2], address[2])
    qc.h(address[2])
    qc.x(address[:])
    qc.h(address[:])

    
def qc_process(qc,objects_to_remove,address,flag,piles,removable_pile,removable_count):

    if removable_count == 0:
        for i in range(len(removable_pile)):
            if piles[i] > 0:
                removable_pile[i] = 1
                removable_count += 1

    if removable_count == 4:
        removable_pile[removable_pile.index(min(removable_pile))] = 0
        removable_count = removable_count - 1

    print(removable_pile, removable_count)

    qft_gate = custom_qft(3).to_gate()
    inverse_qft_gate = custom_qft(3).inverse().to_gate()

    if removable_count == 1:
        qc.swap(objects_to_remove[0],objects_to_remove[2])
        qc.append(qft_gate,objects_to_remove[:])
        # 0001 -> 001
        if removable_pile[0] != 0:
            add_gate = subroutine_add_const(3,removable_pile[0])
            qc.x(address[0])
        # 0010 -> 010
        elif removable_pile[1] != 0:
            add_gate = subroutine_add_const(3,removable_pile[1])
            qc.x(address[1])
        # 0100 -> 011
        elif removable_pile[2] != 0:
            add_gate = subroutine_add_const(3,removable_pile[2])
            qc.x(address[0])
            qc.x(address[1])
        # 1000 -> 100
        elif removable_pile[3] != 0:
            add_gate = subroutine_add_const(3,removable_pile[3])
            qc.x(address[2])

        qc.append(add_gate,objects_to_remove[:])
        qc.append(inverse_qft_gate,objects_to_remove[:])
        qc.swap(objects_to_remove[0],objects_to_remove[2])

    else:
        diffusion_operation(qc,address, flag, removable_pile)
        qc.swap(objects_to_remove[0],objects_to_remove[2])
        qc.append(qft_gate,objects_to_remove[:])
        for i,remove_amount in enumerate(removable_pile):
            if remove_amount != 0:

                bin_i = list(bin(i+1)[2:])
                while len(bin_i) != 3:
                    bin_i.insert(0,'0')
                bin_i = bin_i[::-1]
                for j in range(len(bin_i)):
                    if bin_i[j] == '0':
                        qc.x(address[j])

                controlled_add_gate = subroutine_add_const(3,remove_amount).control(3)    
                qc.append(controlled_add_gate,address[:]+objects_to_remove[:])

                for j in range(len(bin_i)):
                    if bin_i[j] == '0':
                        qc.x(address[j])

        qc.append(inverse_qft_gate,objects_to_remove[:])
        qc.swap(objects_to_remove[0],objects_to_remove[2])

def get_quantum_move(piles, backend=None):

    ones = piles.count(1)
    zeros = piles.count(0)
    non_zeros = 4 - (ones+zeros)

    # all zeros except one eg (0,0,0,7) OR some zeros some ones some non_zeros
    # leave odd piles of 1s
    if non_zeros == 1: 
        removable_pile, removable_count = misere_step(ones, piles) 
    else:
        removable_pile, removable_count = get_piles_to_remove(piles)

    objects_to_remove = QuantumRegister(3,'piles')
    flag = QuantumRegister(1,'flag')
    output_piles = ClassicalRegister(3,'final_piles')
    address = QuantumRegister(3,'address')
    pick_pile = ClassicalRegister(3,'choose_pile')
    qc = QuantumCircuit(objects_to_remove,address,flag,output_piles,pick_pile)
    qc_process(qc,objects_to_remove,address,flag,piles,removable_pile,removable_count)

    qc.measure(address[:],pick_pile[:])
    qc.measure(objects_to_remove[:],output_piles[:])
    
    if backend == None:
        backend = BasicAer.get_backend('qasm_simulator')
        # backend = provider.backends.ibmq_qasm_simulator
    job = execute(qc,backend,shots=500)
    result = job.result()
    counts = result.get_counts()

    try:
        qc_move = (counts.most_frequent())    
    except Exception as e:
        print(e)
        vals = list(dict(counts).values())
        max_count = max(vals,key=vals.count)
        for key in counts:
            if counts[key] == max_count:
                qc_move = key
                break
    
    board_choice = qc_move.split(' ')[0]
    board_choice = int(board_choice,2) - 1

    print("Pick from:",board_choice+1)

    board_state = qc_move.split(' ')[1]
    board_state = board_state[::-1]
    amount = int(board_state,2)
    print("Amount:", amount)
    return board_choice,amount








