---
title: "A Basic Computer"
start_date: "2024-01"
end_date: "2024-01"
featured: false
---
* Used an FPGA for this project.
* Developed the ALU (Arithmetic Logic Unit) of a basic computer:
    * Implemented simple arithmetic operations: addition, subtraction, multiplication by 2.
    * Implemented logical operations: AND.
* Developed a controller for the basic computer:
    * Capable of detecting set flags within the computer.
    * Example: When the CMA (Complement Accumulator) assembly instruction is called:
        * The controller checks the current instruction cycle.
        * The controller checks the first few bits of the instruction register.
    * Controller outputs are sent to a control register.
    * Control register ensures synchronous output using positive edge-triggered D-FF (flip-flops) connected to a common clock.