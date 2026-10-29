#include <stdio.h>

void main()
{
	int polya_index[100];
	double polya_coeff[100];
	int polyb_index[100];
	double polyb_coeff[100];
	int polyc_index[100];
	double polyc_coeff[100];
	int num_a;
	int num_b;
	int num_c;

	int i,j,k,t;
	int index;
	double coeff;
	int temp;
	double coeff_temp;

	i = 0;
	printf("Please enter polynomial A\n");
	while(1)
	{
		scanf("%d%lf", &index, &coeff);

		if(index < 0)
			break;
		else
		{
			polya_index[i] = index;
			polya_coeff[i] = coeff;
			i++;
		}
	}
	num_a = i;

	i = 0;
	printf("Please enter polynomial B\n");
	while(1)
	{
		scanf("%d%lf", &index, &coeff);

		if(index < 0)
			break;
		else
		{
			polyb_index[i] = index;
			polyb_coeff[i] = coeff;
			i++;
		}
	}
	num_b = i;

	// sort polynomial A according to the index
	for(i = 0; i < num_a; ++i)
		for(j = num_a-1; j>i; --j)
		{
			if(polya_index[j] < polya_index[j-1])
			{
				temp = polya_index[j];
				polya_index[j] = polya_index[j-1];
				polya_index[j-1] = temp;

				coeff_temp = polya_coeff[j];
				polya_coeff[j] = polya_coeff[j-1];
				polya_coeff[j-1] = coeff_temp;

			}
		}

			// sort polynomial B according to the index
	for(i = 0; i < num_b; ++i)
		for(j = num_b-1; j>i; --j)
		{
			if(polyb_index[j] < polyb_index[j-1])
			{
				temp = polyb_index[j];
				polyb_index[j] = polyb_index[j-1];
				polyb_index[j-1] = temp;

				coeff_temp = polyb_coeff[j];
				polyb_coeff[j] = polyb_coeff[j-1];
				polyb_coeff[j-1] = coeff_temp;

			}
		}

		// add polynomial A & B
		for(i = j = k = 0; i < num_a && j < num_b; )
		{
			if(polya_index[i] < polyb_index[j])
			{
				polyc_index[k] = polya_index[i];
				polyc_coeff[k] = polya_coeff[i];
				k++;i++;
			}
			else if(polya_index[i] == polyb_index[j]) 
			{
				polyc_index[k] = polya_index[i];
				polyc_coeff[k] = polya_coeff[i] + polyb_coeff[j];
				i++;j++;k++;
			}
			else if(polya_index[i] > polyb_index[j])
			{
				polyc_index[k] = polyb_index[j];
				polyc_coeff[k] = polyb_coeff[j];
				k++;j++;
			}
		}
		
		if(i != num_a)
		{
			for(t = i; t < num_a; ++t)
			{
				polyc_index[k] = polya_index[t];
				polyc_coeff[k] = polya_coeff[t];
				k++;
			}
		}
		else if(j != num_b)
		{
			for(t = j; t < num_b; ++t)
			{
				polyc_index[k] = polyb_index[t];
				polyc_coeff[k] = polyb_coeff[t];
				k++;
			}
		}


		num_c = k;

		// printf the result
		for(i = 0; i < num_c; ++i)
		{
			printf("%.1fx^%d", polyc_coeff[i],polyc_index[i]);
			if(i != num_c -1)
				printf("+");
			else
				printf("\n");
		}


}