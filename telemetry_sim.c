#include <stdio.h>
#include <time.h>
#include <stdlib.h> //use for rand() and srand()
#include <time.h> //helps to generate a new number each time it is ran

typedef struct {
    int device_id;
    float temperature_c;
    float voltage_kv;
    float optical_loss_db;
    float vibration_g;
} indicators;

//srand vs rand

int main(void) {
    int data_id = 101;
    indicators data;
    data.device_id = data_id;

    srand(time(NULL)); //seed the random num generator to use the current time

    int min = 1.00;
    int max = 100.00;

    int rand_num = (rand() % (max - min + 1)) + min;

    printf("{%d\n%d random number int form\n%f\n%f\n%f}\n", data.device_id, rand_num, data.voltage_kv, data.optical_loss_db, data.vibration_g);
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