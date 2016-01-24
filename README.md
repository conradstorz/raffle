# raffle
A python script to make choosing a raffle winner entertaining.

The program runs in a standard terminal window. A file containing JSON data is expected
in the same directory where the program is run. If more than one JSON file is found
then the user is asked to specify. The file can also be specified on the command line.

The contents of the JSON file are displayed and the process of choosing one from all
individual items found in the file proceeds.

When only one item remains, the full data contained in the original JSON file is displayed
in the terminal window with a flashing CONGRATULATIONS! message.

If for any reason the choice is not acceptable like when must be present to win is required,
the user can press backspace and the runner-up will be awarded winner status.

If the runner-up is unsuitable, the user can opt to re-start the entire process.
