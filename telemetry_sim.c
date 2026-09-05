#include <stdio.h>
#include <time.h>
#include <stdlib.h> //use for rand() and srand()
#include <time.h> //helps to generate a new number each time it is ran
#include <unistd.h> //this should use the sleep library

typedef struct {
    int device_id;
    float temperature_c;
    float voltage_kv;
    float optical_loss_db;
    float vibration_g;
} indicators;

float get_random_float(float min, float max) {
    return min + ((float)rand() / (float)RAND_MAX) * (max - min);
}

int get_random_int(int min, int max) {
    return (rand() % (max - min + 1)) + min;
}

int main(void) {
    srand(time(NULL)); //seed the random num generator to use the current time

indicators data;


while (1) {
    data.device_id = get_random_int(101, 10001);
    data.temperature_c = get_random_float(10.0f, 100.0f);
    data.voltage_kv = get_random_float(10.0f, 100.0f);
    data.optical_loss_db = get_random_float(10.0f, 100.0f);
    data.vibration_g = get_random_float(10.0f, 100.0f);

    printf(
        "{\"device_id\": %d, "
        "\"temperature_c\": %.2f, "
        "\"voltage_kv\": %.2f, "
        "\"optical_loss_db\": %.2f, "
        "\"vibration_g\": %.2f}\n",
        data.device_id,
        data.temperature_c,
        data.voltage_kv,
        data.optical_loss_db,
        data.vibration_g
    );

    fflush(stdout);

    sleep(2);
}
    
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