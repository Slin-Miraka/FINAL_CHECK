import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from io import StringIO
import pandas as pd
import json


st.set_page_config(layout="wide")
st.write("***成绩查询地址：https://myuni.sydney.edu.au/api/student/degrees***")
st.write("***查询步骤：复制目标网址的字典数据到此网站即可***")


docs = st.text_area('**将数据全部复制到此粘贴板后点击确认即可**')
check = st.button('确认生成表格')
clear = st.button('清空数据表格')

if clear:
    st.write("")
elif check:
    try:
        data = json.loads(docs)
        df = pd.DataFrame(data[0]['periods'][1]['unitsOfStudy'])
        df = df.set_index(["code"])
        st.write(df)
    except:
        st.error("无成绩数据")



st.write("***如果成绩是 status = COMPLETED; CreditedPoints = 6, 恭喜该门课已通过***")
st.write("***注：这个网站只是帮助大家简化成绩查看流程，没有在后台设置爬虫程序，请放心食用！***")

st.write("***网站代码地址：https://github.com/Slin-Miraka/FINAL_CHECK/blob/main/CHECK.py***")
