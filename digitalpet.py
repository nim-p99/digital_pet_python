import sys

current_energy = 0
EDR, MEL, IEL = 1, 15, 5


def start_game():
    global current_energy, EDR, MEL, IEL 
    welcome_text = (
        "=== digital pet simulator (MIPS32) ===\n"
        "initialising system...\n\n"
        "Please set parameters (press Enter for default):\n"
    )
    print(welcome_text)

    EDR = int(input("enter natural energy depletion rate (EDR) [Default: 1]: ") or "1")
    MEL = int(input("enter maximum energy level (MEL) [Default: 15]: ") or "15")
    IEL = int(input("enter initial energy level (IEL) [Defualt: 5]: ") or "5")
    current_energy = IEL 

    initial_text = (
        "parameters set successfully!\n"
        f"- EDR: {EDR} units/sec\n"
        f"- MEL: {MEL} units\n"
        f"- IEL: {IEL} units\n\n"
        "your digital pet is alive! current status:"
    )
    print(initial_text)


def health_bar():
    global current_energy, MEL
    print("[" + ("█" * current_energy) + ("-" * (MEL - current_energy)) + (f"] Energy: {current_energy}/{MEL}\n"))

def check_MEL():
    global current_energy
    global MEL
    if current_energy > MEL:
        print("Error, maximum energy level reached! capped to the max.")
        current_energy = MEL
        health_bar()
        return True

def feed(n):
    global current_energy
    current_energy += n
    print(f"command recognised: Feed {n}")
    if check_MEL():
        return True
    print(f"Energy incresaed by {n} units")
    health_bar()

def entertain(n):
    global current_energy
    current_energy += 2 * n 
    print(f"command recognised: entertain {n}")
    if check_MEL():
        return True
    print(f"energy increased by {2 * n} units (2x{n}).")
    health_bar()

def pet(n):
    global current_energy
    current_energy += 2 * n 
    print(f"command recognised: pet {n}")
    if check_MEL():
        return True
    print(f"energy increased by {2 * n} units (2x{n}).")
    health_bar()

def ignore(n):
    global current_energy
    current_energy -= 3 * n 
    print(f"command recognised: ignore {n}")
    print(f"energy decreased by {3 * n} units (3x{n}).")
    if current_energy < 0:
        game_loop()
    else:
        health_bar()
        return True

def quit():
    print("Command recognised: Quit.\nSaving session .. goodbye!\n--simulation terminated--")
    sys.exit()

def reset():
    main()



def game_loop():
    global current_energy

    if current_energy <= 0:
        if current_energy < 0:
            print("error, energy level equal or less than 0. DP is dead!")
            current_energy = 0
        health_bar()
        print("*** your digital pet has died! ***")
        died = input("what's your next move? (R, Q) > ")
        if died == "R":
            print("\n\n\n")
            reset()
        elif died == "Q":
            quit()

    health_bar()
    command = input("enter a command (F, E, P, I, R, Q) - eg F2 >")
    if not command:
        return True


    instruction = command[0]
    if len(command) > 1:
        n = int(command[1:])
    else:
        n = 1

    if instruction == "F":
        feed(n)
    elif instruction == "E":
        entertain(n)
    elif instruction == "P":
        pet(n)
    elif instruction == "I":
        ignore(n)
    elif instruction == "R":
        reset()
    elif instruction == "Q":
        quit()
    else:
        print("please provide a valid instruction")

    print("time +1s ... natural energy depletion!")
    current_energy -= EDR

    return True


def main():
    start_game()
    while True:
        alive = game_loop()
        if not alive:
            break

if __name__ == "__main__":
    main()




