#include <math.h>
#include <stdio.h>

typedef struct {
    float x, y, z;
} Vec3;

Vec3 ray_color(Vec3* ray_direction) {
    float t = 0.5 * (ray_direction->y + 1.0);
    return (Vec3){(1.0 - t) * 1.0 + t * 0.5, (1.0 - t) * 1.0 + t * 0.7, 1.0};
}

void render(int width, int height, unsigned char* image) {
    int i, j;
    Vec3 ray_direction;

    for (j = 0; j < height; ++j) {
        for (i = 0; i < width; ++i) {
            ray_direction = (Vec3){
                2.0 * ((i + 0.5) / width) - 1.0,
                2.0 * ((j + 0.5) / height) - 1.0,
                -1.0
            };

            Vec3 color = ray_color(&ray_direction);

            int pixel_index = (j * width + i) * 3;
            image[pixel_index] = (unsigned char)(255.99 * color.x);
            image[pixel_index + 1] = (unsigned char)(255.99 * color.y);
            image[pixel_index + 2] = (unsigned char)(255.99 * color.z);
        }
    }
}
