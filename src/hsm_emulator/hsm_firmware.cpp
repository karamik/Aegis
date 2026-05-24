```cpp
/**
 * HSM Aegis‑2 Emulator for Raspberry Pi Pico (RP2040)
 * 
 * Implements:
 * - Fixed clock cycle count signature timing (12,000,000 cycles @ 1.2GHz = 10ms)
 * - Temperature delta monitoring (max 2°C per signature)
 * - Dual‑key Apollo‑2 logic (simulated with test keys)
 * 
 * Compile with: pico-sdk, flash to Raspberry Pi Pico
 */

#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/adc.h"
#include "hardware/timer.h"
#include "hardware/watchdog.h"

// ==================== CONFIGURATION ====================
#define TARGET_CLOCK_CYCLES     12000000    // 12M cycles @ 1.2GHz = 10ms
#define CYCLE_TOLERANCE         1           // ±1 cycle
#define TEMP_THRESHOLD_DELTA    2.0f        // max 2°C change per signature

// Test keys (in production, these would be burned into OTP)
#define GLOBAL_KEY_TEST         "IBSA_GLOBAL_KEY_2026"
#define SOVEREIGN_KEY_TEST      "STATE_TEST_KEY_0001"

// ==================== GLOBAL STATE ====================
static uint32_t signature_count = 0;
static float last_temperature = 25.0f;
static bool apollo_armed = false;

// ==================== HARDWARE INIT ====================
void init_hsm() {
    stdio_init_all();
    adc_init();
    adc_set_temp_sensor_enabled(true);
    adc_select_input(4);  // Temperature sensor
    
    // Wait for USB serial
    sleep_ms(2000);
    printf("\n[HSM Aegis-2] Emulator started\n");
    printf("[HSM] Target cycles: %u, tolerance: ±%d\n", TARGET_CLOCK_CYCLES, CYCLE_TOLERANCE);
    
    last_temperature = read_core_temperature();
}

float read_core_temperature() {
    uint16_t raw = adc_read();
    const float conversion_factor = 3.3f / (1 << 12);
    float voltage = raw * conversion_factor;
    // RP2040 temperature formula: 27 - (voltage - 0.706) / 0.001721
    return 27.0f - (voltage - 0.706f) / 0.001721f;
}

// ==================== CRYPTO SIMULATION ====================
void compute_sha256_sim(const char* input, uint32_t* out_hash) {
    // Simple XOR hash for emulation (not cryptographic in emulator)
    uint32_t hash = 0x55AA55AA;
    for (const char* p = input; *p; p++) {
        hash = ((hash << 5) + hash) ^ (*p);
    }
    *out_hash = hash;
}

// ==================== CORE SIGNATURE FUNCTION ====================
bool hardware_secure_sign(const char* payload, char* out_signature, size_t out_size) {
    uint32_t start_cycles = timer_hw->timerawl;
    float temp_before = read_core_temperature();
    
    // Simulate cryptographic computation (Ed25519 + Dilithium)
    uint32_t hash_val;
    compute_sha256_sim(payload, &hash_val);
    
    // Busy-wait to achieve exact cycle count
    // This is simplified; real HSM would use hardware timer interrupt
    while ((timer_hw->timerawl - start_cycles) < (TARGET_CLOCK_CYCLES - 10)) {
        __asm volatile("nop");
    }
    
    uint32_t elapsed_cycles = timer_hw->timerawl - start_cycles;
    float temp_after = read_core_temperature();
    float temp_delta = temp_after - temp_before;
    
    // Check invariants
    if (abs((int)(elapsed_cycles - TARGET_CLOCK_CYCLES)) > CYCLE_TOLERANCE) {
        printf("[HSM:CRITICAL] Cycle count mismatch: expected %u, got %u\n", 
               TARGET_CLOCK_CYCLES, elapsed_cycles);
        return false;
    }
    
    if (temp_delta > TEMP_THRESHOLD_DELTA) {
        printf("[HSM:CRITICAL] Thermal glitch: delta = %.2f°C\n", temp_delta);
        return false;
    }
    
    // Success – generate signature
    signature_count++;
    snprintf(out_signature, out_size, 
             "AEGIS2_SIG:%08X:%08X:cnt=%u", 
             start_cycles, hash_val, signature_count);
    
    last_temperature = temp_after;
    return true;
}

// ==================== APOLLO‑2 DUAL‑KEY LOGIC ====================
bool verify_apollo_keys(const char* global_key, const char* sovereign_key) {
    // In production: hardware‑accelerated signature verification
    // In emulator: simple string compare with test keys
    return (strcmp(global_key, GLOBAL_KEY_TEST) == 0) &&
           (strcmp(sovereign_key, SOVEREIGN_KEY_TEST) == 0);
}

void activate_apollo_kill_switch() {
    printf("[HSM:APOLLO] ***** KILL SWITCH ACTIVATED *****\n");
    printf("[HSM:APOLLO] Power cutoff MOSFET open. System halted.\n");
    
    // In real hardware: GPIO to MOSFET gate
    // Here: simulate by watchdog reset loop
    while (1) {
        watchdog_enable(100, 1);
        tight_loop_contents();
    }
}

bool receive_apollo_command(const char* global_key, const char* sovereign_key) {
    if (verify_apollo_keys(global_key, sovereign_key)) {
        printf("[HSM:APOLLO] Valid dual keys received. Arming kill switch.\n");
        apollo_armed = true;
        activate_apollo_kill_switch();
        return true;
    } else {
        printf("[HSM:APOLLO] Invalid keys – ignoring command.\n");
        return false;
    }
}

// ==================== MAIN LOOP ====================
int main() {
    init_hsm();
    
    char signature_buffer[128];
    char input_buffer[256];
    int input_len = 0;
    
    printf("\n[HSM] Ready. Commands:\n");
    printf("  sign <payload>   – generate hardware signature\n");
    printf("  apollo <global> <sovereign> – test Apollo‑2 activation\n");
    printf("  status           – show HSM state\n\n");
    
    while (true) {
        printf("HSM> ");
        fflush(stdout);
        
        // Read line
        input_len = 0;
        while (input_len < sizeof(input_buffer)-1) {
            int c = getchar_timeout_us(1000000);
            if (c == PICO_ERROR_TIMEOUT) {
                // No input, loop
                break;
            }
            if (c == '\n' || c == '\r') {
                input_buffer[input_len] = '\0';
                break;
            }
            input_buffer[input_len++] = (char)c;
        }
        
        if (input_len == 0) continue;
        
        // Parse command
        if (strncmp(input_buffer, "sign ", 5) == 0) {
            const char* payload = input_buffer + 5;
            bool ok = hardware_secure_sign(payload, signature_buffer, sizeof(signature_buffer));
            if (ok) {
                printf("[HSM] Signature: %s\n", signature_buffer);
            } else {
                printf("[HSM] SIGNATURE FAILED – hardware invariant violated\n");
                printf("[HSM] Entering fail‑secure state. Power will be cut.\n");
                activate_apollo_kill_switch();
            }
        } 
        else if (strncmp(input_buffer, "apollo ", 7) == 0) {
            char global_key[64];
            char sovereign_key[64];
            int n = sscanf(input_buffer + 7, "%63s %63s", global_key, sovereign_key);
            if (n == 2) {
                receive_apollo_command(global_key, sovereign_key);
            } else {
                printf("[HSM] Usage: apollo <global_key> <sovereign_key>\n");
            }
        }
        else if (strcmp(input_buffer, "status") == 0) {
            float temp = read_core_temperature();
            printf("[HSM] Status:\n");
            printf("  Signatures issued: %u\n", signature_count);
            printf("  Current temperature: %.2f°C\n", temp);
            printf("  Apollo armed: %s\n", apollo_armed ? "YES" : "NO");
            printf("  Cycle target: %u\n", TARGET_CLOCK_CYCLES);
        }
        else {
            printf("[HSM] Unknown command: %s\n", input_buffer);
        }
    }
    
    return 0;
}
```
