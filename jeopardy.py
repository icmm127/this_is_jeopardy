import pandas as pd
#from string import replace
pd.set_option('display.max_colwidth', -1)

jeopardy_df = pd.read_csv('jeopardy.csv')
jeopardy_df.columns = jeopardy_df.columns.str.strip().str.lower().str.replace(' ', '_')

def filter_df(df, word_list):
    word_filter = lambda x: all(word.lower() in x.lower() for word in word_list)
    return df.loc[df.question.apply(word_filter)]

#print(filter_df(jeopardy_df, ['King', 'England']).head(10))

jeopardy_df['value_float'] = jeopardy_df.value.apply(lambda x: float(x[1:].replace(',', '')) if x != 'None' else 0)
print(filter_df(jeopardy_df, ['King']).value_float.mean())
