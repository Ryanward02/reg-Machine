# Reg-Machine
Python Register Machine Emulator

This project is a relatively basic register machine emulator. The <<x, y>> converter is not yet implemented, however the emulator for the register machine is fully functional.

The syntax for the register machine is as follows:

> program = Program(input-configuration, program-as-instruction-list)

## Example instructions
> Minus(input-register, instruction-1-non-zero, instruction-2-if-zero)

> Plus(input-register, next-instruction)

> Halt(no-parameters)

In the program i have 2 examples. change variable p to your chosen program, with the instructions in order 

i.e program = Program([0, R0, R1, ...], [L0, L1, L2, ...])

When run, the program will output a) the program, so you can check it has been input correctly, and b) the computation of the program. Currently doesn't have halting check, so if it goes on forever, use ctrl-c to interrupt.

currently p = the question from the coursework which asked for the full computation, which i used to test the program worked correctly (it did).

