#include <stdio.h>

int main() {
    int arr[50];
   
     int s = sizeof(arr) / sizeof(arr[0]);

     for (int i = 0; i < s; i++) {
        arr[i] = 50 - i;
    // // // }

    // // // printf("Enter the number you want to search: ");
    // // // int n;
    // // // scanf("%d", &n);

    // // // int low = 0, high = s - 1;
    // // // int steps = 0;
    // // // int found = 0;

    // // // while (low <= high) {
    // // //     steps++;
    // // //     int mid = (low + high) / 2;

    // // //     if (n == arr[mid]) {
    // // //         printf("Number found at index %d in %d steps\n", mid, steps);
    // // //         found = 1;
    // // //         break;
    // // //     } else if (n > arr[mid]) {
    // // //         high = mid - 1; 
    // // //     } else {
    // // //         low = mid + 1; 
    // // //     }
    // // // }

    // // // if (!found) {
    // // //     printf("Number not found in the array.\n");
    // // // }

    return 0;
}