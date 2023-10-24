#include <iostream>
using namespace std;
#define M_PI    3.14159265358979323846
int main()
{
    int i,j,k;
    int n = 4;
    
    double mat[n][n+1] = {
        {7*M_PI,3,2,1,3},
        {2,8*M_PI,2,4,8},
        {3,4,6*M_PI,3,1},
        {3,1,4,9*M_PI,8},
    };
    double res[n];
    cout << "Matrix A and vector b:" << endl;
    for(i=0;i<n;i++){
        for(j=0;j<n+1;j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    for(i=0;i<n;i++) 
    {                   
        for(j=i+1;j<n;j++)
        {
            if(abs(mat[i][i]) < abs(mat[j][i]))
            {
                for(k=0;k<n+1;k++)
                {
                    mat[i][k]=mat[i][k]+mat[j][k];
                    mat[j][k]=mat[i][k]-mat[j][k];
                    mat[i][k]=mat[i][k]-mat[j][k];
                }
            }
      }
    }
    cout << endl;
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            float f=mat[j][i]/mat[i][i];
            for(k=0;k<n+1;k++)
            {
                mat[j][k]=mat[j][k]-f*mat[i][k];
            } 
        }
    }
    cout << endl;
    for(i=n-1;i>=0;i--)          
    {                     
        res[i]=mat[i][n];
                    
        for(j=i+1;j<n;j++)
        {
            if(i!=j)
            {
              res[i]=res[i]-mat[i][j]*res[j];
            }          
        }
        res[i]=res[i]/mat[i][i];  
    }
    cout << "Upper triangle A and vector b:" << endl;
    for(i=0;i<n;i++){
        for(j=0;j<n+1;j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    char arr[9] = {'x','y','z','t','d','e','k','i','j'};
    cout << "Solution vector:" << endl;
    for(i=0;i<n;i++)
    {
      cout << arr[i] << ": " << res[i] << "\n";
    }
    return 0;
}