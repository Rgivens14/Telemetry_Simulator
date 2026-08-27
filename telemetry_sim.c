#include <stdio.h>

int main(void) {
    printf("Really Working\n");
    return 0;
}
//Define the Readout
    /*Figure out what a single sensor measurement looks like.
    It needs to keep track of a few specific numbers (like device_id, temperature, voltage, and optical_loss).*/

//Generate the Values
    /*Put those numbers into a loop so they keep generating new values every second.
    Give them realistic numbers—like a baseline temperature around $45^\circ\text{C}$ that occasionally spikes up to $85^\circ\text{C}$.*/

//Format the output
    /*Turn those numbers into a single line of text formatted as JSON (e.g., {"device_id": 101, "temperature": 48.5, ...}) and print it out.*/

//Push the stream
    /*Immediately flush that line out so it doesn't get stuck waiting in memory.*/