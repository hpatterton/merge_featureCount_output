This Python script combines the tabular output files generated by 'featureCount', adding the integer entries in column 1 (index starts at 0)

The typical featureCount file looks like this:

Geneid	H1_ATCACG_L002__001.fastq
YAL069W	2
YAL068W-A	0
YAL068C	0
YAL067W-A	1
YAL067C	2
YAL066W	2
YAL065C	2

If the file has a header line, set
header = True
column_to_add = 1

define a file containing a list of filenames of the files that you want to merge, for instance:

file_of_filenames = 'C:\\Users\\hpatterton\\Downloads\\189_ featureCounts on collection 116_ Counts\\filenames.txt'

'filenames.txt' may look like this:

C:\Users\hpatterton\Downloads\featureCounts on collection 116_ Counts\H1_ATCACG_L002__001.fastq.tabular
C:\Users\hpatterton\Downloads\featureCounts on collection 116_ Counts\H1_ATCACG_L002__002.fastq.tabular
C:\Users\hpatterton\Downloads\featureCounts on collection 116_ Counts\H1_ATCACG_L002__003.fastq.tabular
C:\Users\hpatterton\Downloads\featureCounts on collection 116_ Counts\H1_ATCACG_L002__004.fastq.tabular
C:\Users\hpatterton\Downloads\featureCounts on collection 116_ Counts\H1_ATCACG_L002__005.fastq.tabular

merge_featureCount_output will write a singe text file called 'filenames_output.txt' in the same directory as the 'filename.txt' file that contains the merged featureCount output files

