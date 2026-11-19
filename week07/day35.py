import streamlit as st


st.set_page_config(
    page_title="day35",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "这是一个streamlit的apex入门演示!"
    }
)
#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

st.write("Apex 进入训练场")
st.write("在训练场可以练习枪法")
st.write("在训练场可以练习身法")
st.write("在训练场可以跟朋友对战")


#图片
st.image("C:/Users/蒋博/Videos/Captures/启动中... 2024_3_30 11_30_03.png")


#音频
st.audio("E:/BaiduNetdiskDownload/fripside - only my railgun.mp3")

#视频
st.video("C:/Users/蒋博/Videos/Captures/Apex Legends 2024-05-13 21-01-57.mp4")



#表格
player_date = {
    "ID":["辛烷","地平线","电妹","麻吉","猎犬"],
    "PON":["游击","突击","守卫","进攻","侦查"],
    "使用率":["15%","12%","11%","18%","8%"]
}
st.table(player_date)

#输入框
name = st.text_input("请输入姓名:")
st.write(f"您输入的姓名为：{name}")

password = st.text_input("请输入密码",type="password")
st.write(f"您输入的密码为：{password}")


#单选按钮
gender = st.radio("请输入您的性别：",["男","女","未知"],index=2)
st.write(f"您的性别为：{gender}")


#布局
