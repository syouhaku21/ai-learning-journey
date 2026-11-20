import streamlit as st

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")
#logo
st.logo("D:/apex-lengends-logo-apex-lengends-icon-transparent-free-png.webp")
#输入框
prompt = st.chat_input("请输入您的问题：", key="input")
if prompt:
    st.write(f"您输入的问题是：{prompt}")

