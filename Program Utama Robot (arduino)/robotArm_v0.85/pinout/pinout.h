#ifndef PINOUT_H_
#define PINOUT_H_

/*
 * pinout of RAMPS 1.4
 *
 * source: http://reprap.org/wiki/RAMPS_1.4
 */

//RAMPS 1.4 PINS
#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN           2
 
#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN          18
#define Z_MAX_PIN          19

#define E0_STEP_PIN        26
#define E0_DIR_PIN         28
#define E0_ENABLE_PIN      24
#define E0_MIN_PIN         20

#define E1_STEP_PIN        36
#define E1_DIR_PIN         34
#define E1_ENABLE_PIN      30
#define E1_MIN_PIN         41
#define E1_MAX_PIN         43

#define BYJ_PIN_0          40
#define BYJ_PIN_1          63
#define BYJ_PIN_2          59
#define BYJ_PIN_3          64

#define SERVO_PIN           4

#define LG1_PIN            8
#define LG2_PIN            10
#define LG3_PIN            9

#define LED_PIN            13

#define SDPOWER            -1
#define SDSS               53

#define FAN_PIN            22

#define PS_ON_PIN          12
#define KILL_PIN           -1

#define IO1_PIN            16
#define IO2_PIN            17
#define IO3_PIN            57
#define IO4_PIN            25
#define IO5_PIN            27
#define IO6_PIN            29
#define IO7_PIN            31
#define IO8_PIN            33
#define IO9_PIN            35
#define IO10_PIN           37

//#define HEATER_0_PIN       10
//#define HEATER_1_PIN        8
#define TEMP_0_PIN         13   // ANALOG NUMBERING
#define TEMP_1_PIN         14   // ANALOG NUMBERING

//RAMPS AUX-2


#endif
