#include <stdio.h>
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
    data.device_id = get_random_int(101, 103);
    data.temperature_c = get_random_float(35.0f, 85.0f);
    data.voltage_kv = get_random_float(11.0f, 13.0f);
    data.optical_loss_db = get_random_float(0.1f, 3.5f);
    data.vibration_g = get_random_float(0.01f, .60f);

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