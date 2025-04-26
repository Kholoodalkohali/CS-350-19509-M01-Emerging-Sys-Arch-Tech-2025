# Final Project Reflection

**1. Summarize the project and what problem it was solving.**  
This project involved developing a smart thermostat prototype using a Raspberry Pi, a temperature and humidity sensor (AHT20), buttons, LEDs, and UART communication. The goal was to create a system that monitors room temperature, allows user input to adjust heating/cooling set points, and displays real-time system status. It solved the problem of efficiently managing temperature control based on real-time environmental data and user inputs.

**2. What did you do particularly well?**  
I successfully integrated multiple components—GPIO, I2C, UART, and LCD display—into a cohesive system. I built a working state machine that effectively managed different operating states (heating, cooling, off) and handled button interrupts. The real-time feedback through LEDs and UART communication worked seamlessly, providing consistent monitoring.

**3. Where could you improve?**  
While the logical flow of the system was solid, I could improve the code by implementing a more formalized state machine structure (using enums or state classes) for better scalability and readability. Additionally, enhancing error handling, such as managing sensor read failures or UART transmission errors, would make the system more robust.

**4. What tools and/or resources are you adding to your support network?**  
I have added resources such as Adafruit documentation, Raspberry Pi official forums, Stack Overflow discussions, and GitHub repositories with similar embedded systems examples. I also relied heavily on Python's documentation for the `gpiozero`, `RPi.GPIO`, and `smbus2` libraries, which I will continue to use for future projects.

**5. What skills from this project will be particularly transferable to other projects and/or course work?**  
Skills such as integrating sensors using I2C, handling real-time hardware interrupts, implementing UART communication, and modular Python coding will be highly transferable. The ability to manage hardware-software interaction and troubleshoot issues at both levels will also be essential for future embedded systems, IoT, and automation projects.

**6. How did you make this project maintainable, readable, and adaptable?**  
I structured the code into clear and modular functions, using meaningful variable names and adding comments to describe critical operations. By using libraries like `gpiozero`, I abstracted hardware control, making it easier to update or expand the system with minimal changes. The modular design and clean formatting ensure that future adaptations or debugging will be straightforward.
