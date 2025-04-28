//  done by RIYOMA
//  done by RIYOMA
#include <stdio.h>
#include <math.h>

int main(void)
{
    
    int i = 0;
    int alt;
    double A, B, a, b, C, c;
    printf("entre a \n");

    scanf("\n%lf", &a);

    printf("entre b \n");

    scanf("\n%lf", &b);

    printf("entre f(a) \n");

    scanf("\n%lf", &A);

    printf("entre f(b)\n", &B);

    scanf("\n%lf", &B);
    printf("\nentrer l'altitude qui tu veux");
    scanf("\n%d", &alt);
    if (alt <= 0)
    {
        printf("\nl'altitude doit etre € N");
        return 1;
    }

    if (A * B < 0)
    {
        do
        {

            double c = (a + b) / 2;
            printf("\nle centre c est :%lf", c);
            printf("\ndonner l'image de c f(c)");
            scanf("\n%lf", &C);

            if (A * C < 0)
            {
                if (a > c)
                {
                    printf("\nl'intervalle est : [%lf,%lf]", c, a);
                }
                else if (a <= c)
                {
                    printf("\nl'intervalle est : [%lf,%lf]", a, c);
                }

                b = c;
            }

            else if (B * C < 0)
            {
                if (c > b)
                {
                    printf("\nl'intervalle est : [%lf,%lf]", b, c);
                }
                else if (c <= b)
                {
                    printf("\nl'intervalle est : [%lf,%lf]", c, b);
                }

                a = c;
            }

            else
            {

                printf("la solution est %lf", C);
            }

            i++;

        } while (i < alt);
    }
    else
    {
        printf("A*B>0");
        return 1;
    }

    printf("\ndone by RIYOMA");
}

//  done by RIYOMA
//  done by RIYOMA