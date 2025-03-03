import streamlit
import pandas
streamlit.title("我的第一个个人网站💡")
streamlit.write("## hello")
"也会自动补充write方法"
streamlit.image("屏幕截图 2024-11-25 220528.png", width=200)

pandas.DataFrame({"小明":[10,9,10],
                  "小华":[9,9,9],
                  "小强":[10,7,9]})

name = streamlit.text_input("请输入你的名字： ")
if name:
    streamlit.write(f"你好，{name}")

#stream重新运行python文件的情况：源代码改变或用户与网站交互操作

streamlit.divider()

password = streamlit.text_input("请输入你的密码： ", type="password")

paragraph = streamlit.text_area("请输入长文段")

age = streamlit.number_input("请输入你的年龄", value=20, min_value=0, max_value=150,
                             step=1) #value为框中的初始值
streamlit.write(f"你的年龄是{age}")

checked = streamlit.checkbox("我同意以上条款") #输出为布尔值
if checked:
    streamlit.write("感谢您的同意")

submitted = streamlit.button("提交") #也返回布尔值，依据是否点击按钮
if submitted:
    print("提交成功！")

gender = streamlit.radio("您的性别是什么？", 
                ["男性","女性","跨性别"], #选项
                 index=None) #默认第一个选项是什么
if gender:
    streamlit.write(f"你选择的性别是{gender}")

streamlit.divider()

contact = streamlit.selectbox("你希望以什么方式联系？",
                              ["电话","邮件","微信","QQ","其它方式"])
if contact:
    streamlit.write(f"好的，我们会通过{contact}联系你")

game_device = streamlit.multiselect("请选择你进行游戏的设备",
                                     ["手机或平板","PC","PS5"]) #此时返回的是列表
for device in game_device:
    streamlit.write(f"你使用的游戏设备有{device}")

streamlit.divider()

height = streamlit.slider("你的身高是多少厘米？",value=170, min_value=100, max_value=230, step=1)
streamlit.write(f"你的身高是{height}厘米")

streamlit.divider()

uploaded_file = streamlit.file_uploader("上传文件", type=["png","jpg","jpeg"]) #上传文件，后面跟支持的文件格式
if uploaded_file:
    streamlit.write(f"你上传的文件是{uploaded_file.name}")
    streamlit.write(f"你上传的文件内容是{uploaded_file.read()}")

streamlit.divider()

with streamlit.sidebar:  #侧边栏
    name = streamlit.text_input("请输入名字")
    if name:
        streamlit.write(f"你好，{name}")

#多个列
column1, column2, column3 = streamlit.columns([1,2,1]) #定义各列大小比例，也可直接输入3，三个等大
with column1:
    streamlit.write("列表1")

with column2:
    streamlit.write("列表2")

with column2:
    streamlit.write("列表2")

#可选择的收缩表
tab1, tab2, tab3 = streamlit.tabs(["性别","联系方式","地址"])
with tab1:
    streamlit.write("列表1")

with tab2:
    streamlit.write("列表2")

with tab2:
    streamlit.write("列表2")

with streamlit.expander("身高信息"):
    height = streamlit.slider("你的身高是多少厘米？",value=170, min_value=100, max_value=230, step=1)
    streamlit.write(f"你的身高是{height}厘米")


#每次网页实现与用户交互后，代码会重新运行，此时可借用方法储存会话中变量的值
print(streamlit.session_state)
if "a" not in streamlit.session_state:
    streamlit.session_state.a = 0
    clicked = streamlit._button("加一")
    if clicked:
        streamlit.session_state.a+=1
    streamlit.write(streamlit.session_state.a)

#创建多页面网站，见page1
#也可结合session_state方法将变量储存到会话状态
