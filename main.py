#The goal of this project is use what I learn from code signal from unit one. 
#I would make an interactive with the user in the terminal 
#Would choose the matrix size and the entries 
#The input features and the output features
#Use linear layers and sigmoid activations
import torch
import torch.nn as nn
import numpy as np
while True:
    list_array = []
    print("Enter 1 for running the tensor program")
    print("Enter 2 to end the program")
    user_run_input = input("Enter: ")
    if(user_run_input.isnumeric() == False):
        print("Enter a number\n")
    else:
        if(int(user_run_input) == 1):
            print("Enter the matrix size using the -x- format")
            user_matrix_size = input("Enter the size: ")
            if( "x" not in user_matrix_size):
                print("It is not in the first format\n")
            else:
                row,col = user_matrix_size.split("x")
                if(row.isnumeric() == False or col.isnumeric() == False):
                    print(user_matrix_size)
                    print("You have to have be a number in the format")
                else:
                    dim = [int(x) for x in user_matrix_size.split("x")]    
                    print("Enter the entries")
                    entry_counter = 0
                    while entry_counter < dim[0] * dim[1]:
                        user_entry = input("Enter: ")
                        if(user_entry.isnumeric() == True):
                            entry = int(user_entry)
                            list_array.append(entry)
                            entry_counter += 1
                        else:
                            print("You need to input a number for the matrix\n")
                    numpy_arrry = np.array(list_array)
                    matrix = numpy_arrry.reshape(dim[0],dim[1])
                    tensor = torch.tensor(matrix, dtype=torch.float32)
                    print(tensor)
                    user_features = int(input("Enter the out features: "))
                    layer = nn.Linear(in_features=dim[1], out_features=user_features, bias=True)
                    output_tensor = layer(tensor)
                    correct_input = True
                    running = True
                    while running:
                        user_input_activation = input("Enter 1 for relu and Enter 2 for sigmoid: ")
                        if user_input_activation.isnumeric() == False:
                            print("Please enter a number\n")
                        else:
                            activation_number = int(user_input_activation)
                            if activation_number == 1:
                                relu = nn.ReLU()
                                activated_relu = relu(output_tensor)
                                print(f"Out tensor after ReLU actiation: \n: {activated_relu}\n")
                            if activation_number == 2:
                                sigmoid = nn.Sigmoid()
                                activated_sigmoid = sigmoid(output_tensor)
                                print(f"Out tensor after sigmoid actiation: \n: {activated_sigmoid}\n")
                            running = False
        if(int(user_run_input) == 2):
            break