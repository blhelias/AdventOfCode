import math

def apply_equation(fuel_quantity):
    # Apply equation to compute fuels quantity
    return ( math.floor( int(fuel_quantity) / 3 ) ) - 2

if __name__ == "__main__":
    reponse = 0
    # Read input file
    with open("input.txt", "r") as input_file:
        # Iterate over lines
        for line in input_file:
            temp = apply_equation(line)
            local_loop = temp
            while temp > 0:
                # update temp 
                temp = apply_equation(temp)
                if temp > 0:
                    local_loop += temp
                
            reponse += local_loop

        print(reponse)
        input_file.close()