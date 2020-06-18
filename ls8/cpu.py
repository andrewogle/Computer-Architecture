"""CPU functionality."""

import sys

sp = 1 # stack pointer

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""
     
     

    def __init__(self):
        """Construct a new CPU."""
        # 256 bytes of memory and 8 general-purpose registers.
        self.ram = [0] * 256 # 256 bytes of memory for instructions
        self.reg = [0] * 8 # 8 general-purpose registers
        self.pc = 0 # Program Counter, the address of the current instruction
        self.branch_table = {
            HLT : self.op_hlt,
            LDI : self.op_LDI,
            PRN : self.op_prn,
            MUL : self.op_mul         
        }
        self.running = True
    def ram_read(self, MAR):
        #  accept the address to read and return the value stored there
        return self.ram[MAR]

    def ram_write(self, MAR, MDR ):
        # accept a value to write, and the address to write it to.
        self.ram[MAR] = MDR

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
       
        with open(filename) as file:
            for line in file:
                command_split = line.split('#')
                instruction = command_split[0]

                if instruction == "":
                    continue

                first_bit = instruction[0]

                if first_bit == '0' or first_bit == '1':
                    self.ram[address] = int(instruction[:8], 2) # convert instructions to binary
                    address += 1



    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        
        




        # running = True

        while self.running :
            opperand_a = self.ram_read(self.pc +1)
            opperand_b = self.ram_read(self.pc +2)
            IR = self.ram_read(self.pc) #instruction register 
            if IR in self.branch_table :
                self.branch_table[IR](opperand_a, opperand_b)
            # else:

            # if IR == HLT:
            #     running = False
            # elif IR == LDI:

            #     self.reg[opperand_a] = opperand_b
            #     self.pc += 3
            # elif IR == PRN:
            #     value = self.reg[opperand_a]
            #     print(value)
            #     self.pc += 2
            # elif IR == MUL:
            #     pass
    def op_hlt(self,opperand_a, opperand_b):
        self.running = False
    
    def op_LDI(self, opperand_a, opperand_b):
        self.reg[opperand_a] = opperand_b
        self.pc += 3
    def op_prn(self, opperand_a, opperand_b):
        value = self.reg[opperand_a]
        print(value)
        self.pc += 2

    def op_mul(self, opperand_a, opperand_b):
        # self.reg[opperand_a] = self.reg[opperand_a] * self.reg[opperand_b]
        self.reg[opperand_a] *= self.reg[opperand_b]
        
        self.pc += 3



            

            

