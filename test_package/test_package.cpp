#include "FastNoiseLite.h"
#include <cstdio>

int main() {
    FastNoiseLite noise;
    noise.SetNoiseType(FastNoiseLite::NoiseType_OpenSimplex2);

    float v2 = noise.GetNoise(1.0f, 2.0f);
    float v3 = noise.GetNoise(1.0f, 2.0f, 3.0f);

    printf("FastNoiseLite OK: 2D=%f 3D=%f\n", v2, v3);
    return 0;
}
