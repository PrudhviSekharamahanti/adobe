import streamlit as st
import pandas as pd
import re
import datetime

st.set_option('deprecation.showfileUploaderEncoding', False)
CURRENT_THEME = "IS_DARK_THEME"
IS_DARK_THEME = True
def rev_calculator(row):
    revenue=0
    if row['event_list']==1:
        for i in list(row['product_list'].split(',')):
            revenue=revenue+(int(i.split(';')[2])*int(i.split(';')[3]))
        return revenue
    return 0

def main():
	st.header("Hit Data Analytics")
	img_file = st.sidebar.file_uploader(label='Upload a file', type=['tsv'])
	if img_file is not None:
		df=pd.read_csv(img_file,sep='\t')

		df['search_engine'] = df.referrer.str.extract('(http://.*(?=.com))')
		df['search_engine'] = [str(row).split('.')[-1] for row in df['search_engine']]
		df['search_keyword'] = [re.search(r'[&q | &p]=(.*?)&', s).group(1) if re.search(r'[&q | &p]=(.*?)&',s) is not None else 'no keywords' for s in df['referrer']]

		df['total_revenue'] = df.apply(lambda row: rev_calculator(row), axis=1)
		new_df=df[['search_engine','search_keyword','total_revenue']]
		new_df = new_df.dropna()
		new_df = new_df[new_df['search_engine'] != 'nan']
		new_df['search_engine']=new_df['search_engine'].str.upper()
		new_df['search_keyword'] = new_df['search_keyword'].str.upper()
		new_df=new_df[new_df['search_engine']!='ESSHOPZILLA']



		new_df1=new_df.groupby(['search_engine','search_keyword'])['total_revenue'].sum().reset_index()
		st.dataframe(new_df1)


		st.download_button(label='Download Current Result',
						   data=new_df.to_csv().encode('utf-8'),
						   file_name='{}_SearchKeywordPerformance.tab'.format(str(datetime.datetime.today()).split()[0])
)
if __name__ == '__main__':
	main()
