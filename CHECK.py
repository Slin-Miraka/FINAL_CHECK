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
    
copy_button = Button(label="粘贴成绩复制结果")
copy_button.js_on_event("button_click", CustomJS(code="""
    navigator.clipboard.readText().then(text => document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: text})))
    """))
    
result = streamlit_bokeh_events(
    copy_button,
    events="GET_TEXT",
    key="get_text",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        list_ = [*StringIO(result.get("GET_TEXT"))][0]
        data = json.loads(list_)
        st.write(pd.DataFrame(data[0]['periods'][1]['unitsOfStudy']))
    else: 
        st.error("成绩数据没有复制")

st.write("***如果成绩是 status = COMPLETED; CreditedPoints = 6, 恭喜该门课已通过***")
st.write("***注：这个网站只是帮助大家简化成绩查看流程，没有在后台设置爬虫程序，请放心食用！***")
