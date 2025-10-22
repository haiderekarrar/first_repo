import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("/Users/haidergilani/Downloads/Mantamonis_bacterial_contamination_analysis.xlsx")

columns_ls = df.columns.tolist()

filtered_df = df[['contig ID', 'Seq Coverage']]
filtered_df = filtered_df.sort_values(by='Seq Coverage', ascending=False)

filtered_df.to_excel('filtered_mantamonis.xlsx', index=False)

#categories = df['Preliminary Verdict:'].unique()
counts = df['Preliminary Verdict:'].value_counts()
counts.plot(kind='bar')
plt.xlabel('Verdict')
plt.ylabel('Count')
plt.title('Preliminary Verdict')

plt.savefig('preliminary_classification.png')
plt.show()
