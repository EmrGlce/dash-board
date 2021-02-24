import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
df1 = pd.read_csv("Caste.csv")
df1 = df1[df1['state_name']=='Maharashtra']
df1 = df1.groupby(['year','gender',],as_index=False)[['detenues','under_trial','convicts','others']].sum()
#df1['err_plus'] = df1['convicts']/100
#df1['err_minus'] = df1['convicts']/40

bar_chart=px.bar(data_frame=df1,
       x="year",
       y="convicts",
       color="convicts",
       opacity=0.9,
       orientation="v",
       barmode="relative",
       #facet_row="caste",
       # facet_row='caste',          # assign marks to subplots in the vertical direction
       # facet_col='caste',          # assigns marks to subplots in the horizontal direction
       # facet_col_wrap=2,           # maximum number of subplot columns. Do not set facet_row!

       #color_discrete_sequence=["blue","purple"],
       #color_discrete_map={"Male" : "gray", "Female" : "red"},
       #color_continuous_scale=px.colors.diverging.Picnic,
       #color_continuous_midpoint =3000,
       #range_color=[1,10000],

       #text='convicts',
       #hover_name='under_trial',   # values appear in bold in the hover tooltip
       #hover_data=['detenues'],    # values appear as extra data in the hover tooltip
       #custom_data=['others'],

       #error_y="err_plus",  # y-axis error bars are symmetrical or for positive direction
       #error_y_minus="err_minus",
       labels={"convicts" : "Convicts in Maharashtra","gender" : "Gender"},  # map the labels of the figure
       title='Indian Prison Statistics',  # figure title
       width=1400,  # figure width in pixels
       height=720,  # figure height in pixels
       template='plotly_dark' # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                             # 'plotly_white', 'plotly_dark', 'presentation',
                            # 'xgridoff', 'ygridoff', 'gridon', 'none'
                 )

pio.show(bar_chart)