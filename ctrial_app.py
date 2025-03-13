import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 配置页面
st.set_page_config(page_title="CTrial Platform", layout="wide")

# 初始化session状态
if 'login' not in st.session_state:
    st.session_state.login = False
if 'user_type' not in st.session_state:
    st.session_state.user_type = None

# 登录页面
def login_page():
    st.title("🩺 CTrial Platform Login")
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/565/565547.png", width=150)
        
    with col2:
        user_type = st.selectbox("选择用户类型", ["患者", "招募团队", "留存团队"])
        if st.button("登录"):
            st.session_state.login = True
            st.session_state.user_type = user_type
            st.rerun()

# 患者主页
def patient_dashboard():
    st.title(f"欢迎患者用户 | 健康积分: ★{np.random.randint(50,100)}")
    
    # 智能匹配模块
    with st.expander("🔍 智能试验匹配", expanded=True):
        col1, col2 = st.columns([3,1])
        with col1:
            st.subheader("推荐临床试验")
            trials = pd.DataFrame({
                '试验名称': ['肺癌靶向治疗III期', '糖尿病新药II期', '帕金森监测研究'],
                '匹配度': [92, 85, 78],
                '距离(km)': [15, 32, 8],
                '奖励': ['$2000', '健康监测套装', '$1500+免费体检']
            })
            st.dataframe(trials, hide_index=True)
            
        with col2:
            st.subheader("匹配筛选")
            st.slider("最大距离(km)", 0, 100, 50)
            st.multiselect("疾病类型", ["肺癌", "糖尿病", "帕金森"])
            st.checkbox("仅显示即时奖励")

    # 试验地图模块
    st.subheader("🏥 试验机构地图")
    locations = pd.DataFrame({
        'lat': [37.78 + np.random.rand()*0.1 for _ in range(5)],
        'lon': [-122.4 + np.random.rand()*0.1 for _ in range(5)],
        '机构名称': ['加州医疗中心', '斯坦福研究所', '凯撒医院', 'UCSF医学部', '社区诊所']
    })
    st.map(locations, zoom=12)

# 团队主页
def team_dashboard():
    st.title(f"试验团队控制台 | 今日新增: {np.random.randint(5,20)}人")
    
    # 招募分析
    with st.expander("📈 招募驾驶舱"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("患者漏斗")
            funnel_data = pd.DataFrame({
                '阶段': ['曝光', '点击', '申请', '筛选', '入组'],
                '人数': [1000, 300, 150, 80, 45]
            })
            st.plotly_chart(px.funnel(funnel_data, x='人数', y='阶段'))
            
        with col2:
            st.subheader("广告效果")
            ad_data = pd.DataFrame({
                '渠道': ['Google', 'Facebook', '医院合作', '医生推荐'],
                '转化率': [0.05, 0.03, 0.12, 0.18]
            })
            st.plotly_chart(px.bar(ad_data, x='渠道', y='转化率'))

    # 患者留存
    st.subheader("📉 患者留存分析")
    retention_data = pd.DataFrame({
        '周数': range(1,9),
        '留存率': [1.0, 0.85, 0.78, 0.72, 0.68, 0.65, 0.62, 0.60]
    })
    st.line_chart(retention_data, x='周数', y='留存率')

# 主程序
if not st.session_state.login:
    login_page()
else:
    if st.button("退出登录"):
        st.session_state.login = False
        st.rerun()
        
    if st.session_state.user_type == "患者":
        patient_dashboard()
    else:
        team_dashboard()
        
    # 通用教育模块
    with st.sidebar:
        st.header("📚 教育中心")
        st.selectbox("选择内容类型", ["试验流程", "权益保障", "常见问题"])
        st.video("https://www.youtube.com/watch?v=example")
        st.download_button("下载知情同意书模板", data="Sample PDF Content", file_name="consent_form.pdf")