# Teraki3DRecruitmentTestApr19


By using CloudCompare visualisation, the rank of the compression methods from best to worst accuracy is B,A,C.
The same result has been Obtained by implementing the logic in Python. The input files and output files are created in the tsv format.



To run the code:
python compression.py --data Enter uncompressed.tsv Input file name --dataA Enter dataA.tsv Input file name
  --dataB Enter dataC.tsv Input file name --dataC Enter dataC.tsv Input file name --output Enter output file name

Geometric Accuracy measure considered is Maximum distance. If the distance between the point sets of Uncompressed and decompressed point clouds is maximum then it is considered as the worst compression Technique.

Output of the program:

Maximum distance between the points sets of Uncompressed and Decompressed A 21.194809956055153
Maximum distance between the points sets of Uncompressed and Decompressed B 2.982278145404609
Maximum distance between the points sets of Uncompressed and Decompressed C 142.8205332553303
{21.194809956055153: 'A', 2.982278145404609: 'B', 142.8205332553303: 'C'}
Best compression Technique :  B
Worst compression Technique :  C


